import pandas as pd
import numpy as np

# 75 random integers from 10-99, reshaped into a 15-row by 5-column grid,
# then wrapped in a DataFrame with explicit column names.
data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data, columns = ["Column1","Column2","Column3","Column4","Column5"])

result = df
# .columns lists the column labels (an Index object, printable like a
# list): Column1..Column5.
result = df.columns
# .head() with no argument shows the first 5 rows by default -- a quick
# way to sanity-check a table without dumping the whole thing.
result = df.head()
# .head(10) explicitly asks for the first 10 rows instead of the default 5.
result = df.head(10)
# .tail() mirrors .head() but from the END of the table: last 5 rows by
# default.
result = df.tail()
# .tail(10) explicitly asks for the last 10 rows.
result = df.tail(10)
# Selecting one column (Series) and then chaining .head() shows just the
# first 5 values of that column.
result = df["Column1"].head()
# Columns can also be accessed as attributes (dot notation) when the name
# is a valid Python identifier -- df.Column1 is equivalent to
# df["Column1"]. The bracket form is generally safer/more general (works
# with names containing spaces, etc.), but the dot form is common for
# quick, readable exploration.
result = df.Column1.head()
# Selecting a LIST of columns keeps the 2D table shape (DataFrame, not
# Series), then .head() shows its first 5 rows.
result = df[["Column1","Column2"]].head()
result = df[["Column1","Column2"]].tail()
# df[5:15] uses POSITION-based row slicing directly on the DataFrame
# (rows at index positions 5 through 14), then [["Column1","Column2"]]
# narrows down to just those two columns, and .head() shows the first 5
# of that already-sliced subset.
result = df[5:15][["Column1","Column2"]].head()
result = df[5:15][["Column1","Column2"]].tail()

# Comparing an entire DataFrame to a scalar produces a same-shaped
# DataFrame of True/False values -- True wherever that cell's value is
# greater than 50.
result = df > 50
# Using that boolean DataFrame as a mask, df[df > 50], keeps the actual
# values where the condition was True and replaces every False spot with
# NaN (missing value) -- it does NOT drop rows/columns, the shape stays
# the same.
result = df[df > 50]
# Same idea with a different condition: True wherever a value is
# divisible by 2 (even); everything else becomes NaN when used as a mask.
result = df[df % 2==0]
# df["Column1"] > 50 produces a 1D boolean Series (one True/False per
# ROW, based only on Column1's value). Using THAT to index the whole
# DataFrame, df[condition], keeps entire ROWS where the condition is True
# and drops the rest -- this is the standard pandas row-filtering pattern.
# Chaining [["Column1","Column2"]] afterward narrows the surviving rows
# down to just those two columns.
result = df[df["Column1"] > 50][["Column1","Column2"]]
# Combining two row conditions with "&" (element-wise AND for pandas/
# numpy boolean arrays -- NOT Python's plain "and", which doesn't work
# element-wise). Each condition MUST be wrapped in its own parentheses
# because of how Python evaluates operator precedence with "&". This
# keeps rows where Column1 is in the range (50, 70].
result = df[(df["Column1"] > 50) & (df["Column1"] <= 70)]
# Same "&" pattern but combining conditions from two DIFFERENT columns:
# keeps rows where Column1 > 50 AND Column2 <= 70.
result = df[(df["Column1"] > 50) & (df["Column2"] <= 70)]
# "|" is the element-wise OR: keeps rows where EITHER Column1 > 50 OR
# Column2 > 50 (or both), then narrows to those two columns.
result = df[(df["Column1"] > 50) | (df["Column2"] > 50)][["Column1","Column2"]]
# .query() lets you write the same filtering logic as a plain string
# expression instead of the bracket/& syntax -- often more readable for
# complex conditions. "&" still means AND here.
result = df.query("Column1 >= 50 & Column1 % 2 == 0")
result = df.query("Column1 >= 50 & Column1 % 2 == 0")[["Column1","Column2"]]
# "|" inside a query string means OR, same as the bracket syntax.
result = df.query("Column1 >= 50 | Column1 % 2 == 0")[["Column1","Column2"]]


print(result)
