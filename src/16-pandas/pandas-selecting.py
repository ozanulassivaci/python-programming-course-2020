import pandas as pd
from numpy.random import randn

# randn(3,3) gives a 3x3 matrix of random values from the standard normal
# distribution (centered on 0). Wrapping it in a DataFrame with explicit
# row labels ("A","B","C") and column labels ("Column1","Column2",
# "Column3") turns that raw numeric grid into a labeled table.
df = pd.DataFrame(randn(3,3), index = ["A","B","C"], columns = ["Column1","Column2","Column3"])

# Just the DataFrame itself, unchanged.
result = df
# Selecting a DataFrame with a single column NAME in square brackets
# returns that column as a Series (not a DataFrame).
result = df["Column1"]
# Confirms the above: type() shows this is a pandas.core.series.Series.
result = type(df["Column1"])
# Passing a LIST of column names (double square brackets: the outer ones
# are "select columns", the inner ones build the list) returns a
# DataFrame containing just those columns, keeping the 2D table shape
# instead of collapsing to a Series.
result = df[["Column1","Column2"]]

# loc["row","column"] => loc["row"] => loc[":","column"]
# Learning note: loc is label-based, iloc is position-based - kept mixing these up at first.
# .loc[...] selects data by LABEL (the actual row/column names you gave
# the DataFrame), while .iloc[...] selects by integer POSITION (0, 1, 2,
# ...), exactly like plain list indexing, regardless of what the labels
# are. Both accept the row selector first, then (optionally) the column
# selector, separated by a comma: df.loc[row_selector, column_selector].

# .loc["A"] selects the row labeled "A" -> returns it as a Series (its
# index becomes the original column names, Column1/2/3).
result = df.loc["A"]
result = type(df.loc["A"])
# .iloc[2] selects the row at POSITION 2 (the third row, 0-based) --
# which happens to be row "C" here, but iloc doesn't care about the label,
# only the position.
result = df.iloc[2]
# df.loc[:, "Column1"] means "all rows (:), just the Column1 column" --
# this pulls out an entire column as a Series, same effect as df["Column1"]
# but written the explicit loc way.
result = df.loc[:,"Column1"]
# Passing a list of column labels after the comma selects multiple whole
# columns, keeping the table (DataFrame) shape.
result = df.loc[:,["Column1","Column2"]]
# A LABEL-based slice "Column1":"Column2" selects every column starting at
# "Column1" through "Column2" INCLUSIVE. This is a key difference from
# normal Python slicing: label-based slicing with .loc includes both
# endpoints, unlike position-based slicing which excludes the stop.
result = df.loc[:,"Column1":"Column2"]
# Leaving the start empty (:"Column2") means "from the first column
# through Column2 inclusive" -- here that's the same result as above since
# Column1 is already the first column.
result = df.loc[:,:"Column2"]
# Combining row and column label slices: rows "A" through "B" inclusive,
# columns up through "Column2" inclusive -- selects a sub-table.
result = df.loc["A":"B",:"Column2"]
# Row slice with no explicit start (:"B") means "from the first row
# through B inclusive" -- equivalent to "A":"B" here since A is first.
result = df.loc[:"B",:"Column2"]
# A single row label AND a single column label together selects one exact
# cell/value (row "A", column "Column2").
result = df.loc["A","Column2"]
result = df.loc["C","Column1"]
# Lists on both sides select a smaller sub-table: rows A and B, columns
# Column1 and Column2 only.
result = df.loc[["A","B"],["Column1","Column2"]]

# Assigning a new Series to a column name that doesn't exist yet CREATES a
# new column, aligned by index label (A, B, C) just like Series addition.
df["Column4"] = pd.Series(randn(3), ["A","B","C"])
# You can also create a new column from an expression combining existing
# columns -- this adds Column1 and Column3 element-wise (matched by row)
# and stores the result as Column5.
df["Column5"] = df["Column1"] + df["Column3"]

# .drop(label, axis=1) removes a column (axis=1 means "act along columns";
# axis=0 would mean "act along rows" and remove a row instead).
# inplace=True modifies df directly instead of returning a new DataFrame
# and leaving the original untouched -- so after this line, Column5 is
# gone from df for good.
df.drop("Column5", axis = 1, inplace = True)


print(df)
