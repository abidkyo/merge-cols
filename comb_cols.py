#! /usr/bin/env python3
"""
Script to combine multiple columns with separation character.

- Read the data as string.
- Join the columns with separation character in the middle.
- Delete the columns if specified.
- Export the dataframe.

Usage:
    python3 comb_cols.py -v -f data.xlsx --cols "First Name" "Last Name" --sep " " --colname "Name" -d -o output.xlsx
"""


import argparse

import pandas as pd


# Create argument parser
parser = argparse.ArgumentParser(description="Combine multiple columns with separation character.")
required_argument = parser.add_argument_group("required named arguments")
parser.add_argument("-v", "--verbose", action="store_true", help="verbosity")
required_argument.add_argument("-f", "--file", help="excel filename", required=True)
parser.add_argument("-s", "--sheet", default=0, help="sheet name or number")
parser.add_argument("-n", "--nrows", default=None, type=int, help="number of rows to read")
required_argument.add_argument("--cols", nargs="+", help="columns to combine", required=True)
required_argument.add_argument("--sep", help="separation character", required=True)
required_argument.add_argument("--colname", help="new column name", required=True)
parser.add_argument("-d", "--delete", action="store_true", help="option to delete given columns")
required_argument.add_argument("-o", "--output", help="output filename", required=True)

args = parser.parse_args()

# Store arguments in variables.
verbose = args.verbose
fileName = args.file

try:
    sheet = int(args.sheet)
except ValueError:
    sheet = args.sheet

nRows = args.nrows
cols = args.cols
colname = args.colname
sep = args.sep
delete = args.delete
outFileName = args.output


# Read excel file with dtype set to str (easier to join).
df = pd.read_excel(fileName, sheet_name=sheet, nrows=nRows, dtype=str)
if verbose:
    print("Original Data")
    print(df)
    print()


# Combine the columns with separation character.
df[colname] = df[cols].agg(sep.join, axis=1)


# Delete the columns if specified.
if delete:
    df.drop(columns=cols, inplace=True)

if verbose:
    print("Combined Data")
    print(df)
    print()


# Export to an excel file.
df.to_excel(outFileName, index=False)
