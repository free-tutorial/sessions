# CSV

## What Is a CSV File?
A CSV file (Comma Separated Values file) is a type of plain text file that uses specific structuring to arrange tabular data. Because it’s a plain text file, it can contain only actual text data—in other words, printable ASCII or Unicode characters.

The structure of a CSV file is given away by its name. Normally, CSV files use a comma to separate each specific data value. Here’s what that structure looks like:

```
column 1 name,column 2 name, column 3 name
first row data 1,first row data 2,first row data 3
second row data 1,second row data 2,second row data 3
```

In general, the separator character is called a delimiter, and the comma is not the only one used. Other popular delimiters include the tab (`\t`), colon (`:`) and semi-colon (`;`) characters. Properly parsing a CSV file requires us to know which delimiter is being used.

## Where Do CSV Files Come From?
CSV files are normally created by programs that handle large amounts of data. They are a convenient way to export data from spreadsheets and databases as well as import or use it in other programs. For example, you might export the results of a data mining program to a CSV file and then import that into a spreadsheet to analyze the data, generate graphs for a presentation, or prepare a report for publication.

CSV files are very easy to work with programmatically. Any language that supports text file input and string manipulation (like Python) can work with CSV files directly.

## Parsing CSV Files With Python’s Built-in CSV Library
The [csv library](https://docs.python.org/3/library/csv.html) provides functionality to both read from and write to CSV files. Designed to work out of the box with Excel-generated CSV files, it is easily adapted to work with a variety of CSV formats. The csv library contains objects and other code to read, write, and process data from and to CSV files.

### Reading CSV Files With csv
Reading from a CSV file is done using the reader object. The CSV file is opened as a text file with Python’s built-in open() function, which returns a file object. This is then passed to the reader, which does the heavy lifting.

Here’s the `employee_birthday.txt` file:
```
name,department,birthday month
John Smith,Accounting,November
Erica Meyers,IT,March
```

[`read_csv.py`](./read_csv.py) is the code to read it.


#### CSV `reader` Parameters
- `delimiter` specifies the character used to separate each field. The default is the comma (`','`).
  - `csv_reader = csv.reader(csv_file, delimiter=';')`
- `quotechar` specifies the character used to surround fields that contain the delimiter character. The default is a double quote (`' " '`).
  - `csv_reader = csv.reader(csv_file)`
- `escapechar` specifies the character used to escape the delimiter character, in case quotes aren’t used. The default is no escape character.
  - `csv_reader = csv.reader(csv_file, escapechar='\\')`

### Writing CSV Files With csv
You can also write to a CSV file using a writer object and the `.write_row()` method:

```python
import csv

with open('employee_file.csv', mode='w') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    employee_writer.writerow(['John Smith', 'Accounting', 'November'])
    employee_writer.writerow(['Erica Meyers', 'IT', 'March'])
```

The quotechar optional parameter tells the writer which character to use to quote fields when writing. Whether quoting is used or not, however, is determined by the quoting optional parameter:
- If quoting is set to `csv.QUOTE_MINIMAL`, then `.writerow()` will quote fields only if they contain the delimiter or the quotechar. This is the default case.
- If quoting is set to `csv.QUOTE_ALL`, then `.writerow()` will quote all fields.
- If quoting is set to `csv.QUOTE_NONNUMERIC`, then `.writerow()` will quote all fields containing text data and convert all numeric fields to the float data type.
- If quoting is set to `csv.QUOTE_NONE`, then `.writerow()` will escape delimiters instead of quoting them. In this case, you also must provide a value for the escapechar optional parameter.
  - `csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_NONE, escapechar='\\')`


## References
- https://realpython.com/python-csv/