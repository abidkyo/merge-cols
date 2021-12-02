# comb_cols

## Description
Script to combine multiple columns with separation character.

- Read the data as string.
- Join the columns with separation character in the middle.
- Delete the columns if specified.
- Export the dataframe.


## Usage
```bash
python3 comb_cols.py -v -f data.xlsx --cols "First Name" "Last Name" --sep " " --colname "Name" -d -o output.xlsx
```

## Dependencies
[pandas](https://pandas.pydata.org/)
[openpyxl](https://openpyxl.readthedocs.io)
```bash
python3 -m pip install pandas openpyxl
```

## Help Message
```bash
usage: comb_cols.py [-h] [-v] -f FILE [-s SHEET] [-n NROWS] --cols COLS [COLS ...] --sep SEP --colname COLNAME [-d] -o OUTPUT

Combine multiple columns with separation character.

optional arguments:
  -h, --help            show this help message and exit
  -v, --verbose         verbosity
  -s SHEET, --sheet SHEET
                        sheet name or number
  -n NROWS, --nrows NROWS
                        number of rows to read
  -d, --delete          option to delete given columns

required named arguments:
  -f FILE, --file FILE  excel filename
  --cols COLS [COLS ...]
                        columns to combine
  --sep SEP             separation character
  --colname COLNAME     new column name
  -o OUTPUT, --output OUTPUT
                        output filename
```

### Note
Tested with Python 3.8.10 and Pandas 1.3.4
