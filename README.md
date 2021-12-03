# comb_cols

## Description
Script to combine multiple columns with separation character.

- Read the data.
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


## Example Output
```
Original Data
  First Name   Last Name  Gender  Age                        Email        City  Postcode
0  Charlotte      Walker  Female   21      c.walker@randatmail.com      Xusall     53572
1     Ashton  Richardson    Male   19  a.richardson@randatmail.com      Bensey     45529
2      Ellia     Spencer  Female   28     e.spencer@randatmail.com   Strirving     16901
3      Edwin      Gibson    Male   29      e.gibson@randatmail.com     Tulwell     81507
4    Brianna       Adams  Female   26       b.adams@randatmail.com       Faton     56357
5     Amanda      Miller  Female   22      a.miller@randatmail.com        Barc     58332
6   Madaline    Sullivan  Female   30    m.sullivan@randatmail.com       Zrurg     80903
7     Victor        Reed    Male   25        v.reed@randatmail.com      Perton     29229
8     Gianna       Payne  Female   19       g.payne@randatmail.com   Inasridge     87493
9    Miranda      Martin  Female   20      m.martin@randatmail.com  Ouverpolis     83293


Combined Data
   Gender  Age                        Email        City  Postcode               Name
0  Female   21      c.walker@randatmail.com      Xusall     53572   Charlotte Walker
1    Male   19  a.richardson@randatmail.com      Bensey     45529  Ashton Richardson
2  Female   28     e.spencer@randatmail.com   Strirving     16901      Ellia Spencer
3    Male   29      e.gibson@randatmail.com     Tulwell     81507       Edwin Gibson
4  Female   26       b.adams@randatmail.com       Faton     56357      Brianna Adams
5  Female   22      a.miller@randatmail.com        Barc     58332      Amanda Miller
6  Female   30    m.sullivan@randatmail.com       Zrurg     80903  Madaline Sullivan
7    Male   25        v.reed@randatmail.com      Perton     29229        Victor Reed
8  Female   19       g.payne@randatmail.com   Inasridge     87493       Gianna Payne
9  Female   20      m.martin@randatmail.com  Ouverpolis     83293     Miranda Martin

```


### Note
Tested with Python 3.8.10 and Pandas 1.3.4
