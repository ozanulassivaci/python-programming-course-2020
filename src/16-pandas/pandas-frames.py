import pandas as pd

# A DataFrame is pandas' 2D table type: rows and columns, each column
# potentially holding a different data type, with labels for both rows
# (the "index") and columns. You can think of it as a dict of Series that
# all share the same row index, or as a spreadsheet loaded into Python.

# Learning note: a DataFrame can be built from a list of lists, a dict of lists, or a list of dicts - trying all three here.
# 1) A list of lists: each inner list is one ROW of data, in column order.
list = [["Ahmet",50], ["Ali",60], ["Yağmur",70], ["Çınar",80]]
# 2) A dict of lists: each KEY becomes a column name, and each VALUE (a
# list) becomes that column's data, read top-to-bottom in parallel across
# all keys (so index 0 of every list forms row 0, and so on).
dict = {"Name": ["Ahmet","Ali","Yağmur","Çınar"], "Grade": [50,60,70,80]}
# 3) A list of dicts: each dict is one ROW, and its keys become column
# names. pandas matches up dicts that share the same keys into columns
# automatically.
dict_list = [
                {"Name":"Ahmet","Grade":50},
                {"Name":"Ali","Grade":60},
                {"Name":"Yağmur","Grade":70},
                {"Name":"Çınar","Grade":80}
            ]

# pd.DataFrame() with no arguments makes an empty table.
# df = pd.DataFrame()
# A single flat list becomes a one-column DataFrame with default column
# name 0 and default row index 0,1,2,3.
# df = pd.DataFrame([1,2,3,4])
# Building from the list-of-lists: without column names, pandas would
# default to numbering the columns 0, 1, 2... To make them readable, we
# supply "columns" explicitly. "index" replaces the default 0,1,2,3 row
# labels with 1,2,3,4, and "dtype=float" forces every value (even the
# text ones, where possible) to be stored/read as a float.
# df = pd.DataFrame(list, index = [1,2,3,4], columns = ['Name','Grade'], dtype = float)
# Building straight from the dict-of-lists: the dict keys ("Name",
# "Grade") automatically become the column headers.
# df = pd.DataFrame(dict)
# Same dict, but this time overriding the default 0,1,2,3 row labels with
# custom string labels for the index.
# df = pd.DataFrame(dict, index = ["212","232","236","456"])
# Building from the list-of-dicts: pandas reads each dict as a row and
# lines them up into a table using the shared "Name"/"Grade" keys as
# columns.
# df = pd.DataFrame(dict_list)
# Same as above, but also giving the rows custom string index labels
# instead of the default 0,1,2,3.
df = pd.DataFrame(dict_list,index = ["212","232","236","456"])


# Printing a DataFrame shows a neatly aligned table: the index labels on
# the left, column headers on top, and the "Name"/"Grade" values filled
# in for each of the four students (Ahmet/50, Ali/60, Yağmur/70,
# Çınar/80), using the custom "212","232","236","456" row labels.
print(df)



# s1 = pd.Series([3,2,0,1])
# s2 = pd.Series([0,3,7,2])

# A dict of Series works just like a dict of lists for building a
# DataFrame: each key names a column, and each Series supplies that
# column's values (aligned by their shared default index 0,1,2,3).
# data = dict(apples = s1 , oranges = s2)

# df = pd.DataFrame(data)

# print(df)
