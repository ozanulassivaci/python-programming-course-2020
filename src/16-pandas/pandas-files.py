import sqlite3
import pandas as pd

# Learning note: pandas can read straight from csv/json/excel/sql, no manual parsing needed.
# pandas has built-in "read_*" functions that load common file formats
# directly into a DataFrame, handling all the format-specific parsing for
# you -- no manual splitting on commas or writing a custom parser needed.

# pd.read_csv(path) reads a comma-separated-values text file, using the
# first line as column headers by default.
# df = pd.read_csv('datasets/sample.csv')
# pd.read_json(path) parses a JSON file/string into a DataFrame. The
# encoding argument tells pandas how the text bytes should be decoded
# (UTF-8 handles a wide range of characters, including non-English ones).
# df = pd.read_json('datasets/sample.json',encoding="UTF-8")
# pd.read_excel(path) reads an Excel spreadsheet file (.xlsx) -- pandas
# uses the openpyxl/xlrd library under the hood to understand the Excel
# format.
# df = pd.read_excel("datasets/sample.xlsx")

# For SQL databases, pandas doesn't connect to the database itself --
# instead you open a connection with the appropriate database library
# (here, Python's built-in sqlite3 module for SQLite files) and hand that
# connection to pandas.
connection = sqlite3.connect("datasets/sample.db")
# pd.read_sql_query(sql, connection) runs the given SQL query against the
# open connection and loads the returned rows straight into a DataFrame,
# using the query's result columns as the DataFrame's columns. Here it
# selects every row and column from the "students" table.
df = pd.read_sql_query("SELECT * FROM students",connection)

print(df)
