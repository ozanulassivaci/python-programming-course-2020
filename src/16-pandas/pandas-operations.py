import pandas as pd
import numpy as np

data = {
    "Column1": [1,2,3,4,5],
    "Column2": [10,20,13,20,25],
    "Column3": ["abc","bcaa","ade","cb","dea"]
}

df = pd.DataFrame(data)

# A plain Python function, usable anywhere a "callable" is expected --
# including as an argument to pandas' .apply().
def square(x):
    return x * x

# A lambda is a small, unnamed (anonymous) function written inline. This
# one does exactly the same thing as square() above: takes x, returns
# x * x. Lambdas are handy for one-off, throwaway logic where defining a
# whole named function feels like overkill.
square2 = lambda x: x * x

result = df
# .unique() lists each DISTINCT value that appears in the column, in the
# order first encountered, with duplicates removed. Column2 has values
# [10,20,13,20,25] -- 20 appears twice, so unique() returns [10,20,13,25].
result = df["Column2"].unique()
# .nunique() is like .unique() but returns just the COUNT of distinct
# values instead of the values themselves -- 4 here (10,20,13,25).
result = df["Column2"].nunique()
# .value_counts() tells you how many times EACH distinct value appears,
# sorted from most frequent to least -- so this would show 20 appearing
# twice, and 10/13/25 each appearing once.
result = df["Column2"].value_counts()
# Multiplying a whole column (Series) by 2 is a vectorized operation: each
# value in Column1 gets doubled, no explicit loop required.
result = df["Column1"] * 2
# .apply(function) runs the given function on EVERY value in the Series,
# one at a time, and collects the results into a new Series. This is
# pandas' general-purpose "map this function over my data" tool, useful
# when the transformation isn't a simple built-in vectorized operation.
result = df["Column1"].apply(square)
# Same effect, but passing the lambda-based function defined above.
result = df["Column1"].apply(square2)
# You can also skip naming the lambda at all and write it directly inline
# as the argument -- common when the logic is simple and used just once.
result = df["Column1"].apply(lambda x: x * x)
# len is itself just a function, so it can be passed straight to .apply()
# without wrapping it: this creates a NEW column "Column4" holding the
# length (number of characters) of each string in Column3
# (abc->3, bcaa->4, ade->3, cb->2, dea->3).
df["Column4"] = df["Column3"].apply(len)

# .columns lists all column labels currently in the DataFrame (now
# including the new Column4).
result = df.columns
# len() on the .columns Index gives you the COUNT of columns (an integer).
result = len(df.columns)
# .index gives you the row labels (here, the default RangeIndex 0..4).
result = df.index
# len() on the index gives the number of ROWS.
result = len(df.index)
# .info is the METHOD OBJECT itself, not a call to it -- note there are no
# parentheses. Printing/assigning this just shows something like
# "<bound method DataFrame.info ...>" rather than the actual summary; you'd
# need df.info() (with parentheses) to actually print the DataFrame's
# summary (column names, non-null counts, dtypes, memory usage).
result = df.info

# .sort_values(column) returns a NEW DataFrame with rows reordered by that
# column's values, ascending by default (smallest/earliest first).
result = df.sort_values("Column2")
# Sorting works on text columns too -- alphabetical order by default.
result = df.sort_values("Column3")
# ascending=False reverses the sort order (largest/last-alphabetically
# first).
result = df.sort_values("Column3", ascending = False)

# Learning note: pivot_table is basically a groupby + reshape in one call.
# A fresh dataset: sales revenue broken down by month and product
# category (note the data is reassigned here -- `df` above and this new
# `data`/`df` are unrelated to each other).
data = {
    "Month": ["May","June","April","May","June","April","May","June","April"],
    "Category": ["Electronics","Electronics","Electronics","Books","Books","Books","Clothing","Clothing","Clothing"],
    "Revenue": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(data)

# .pivot_table(index=..., columns=..., values=...) reshapes "long" data
# (one row per Month/Category/Revenue observation) into a "wide" summary
# table: one row per distinct Month, one column per distinct Category,
# and each cell filled with the Revenue value for that Month+Category
# combination (averaging, by default, if there were multiple matching
# rows -- here each Month/Category pair only has one row, so the average
# is just that single value). This is conceptually a groupby on
# [Month, Category] followed by reshaping the Category values out into
# their own columns.
print(df.pivot_table(index="Month",columns= "Category", values= "Revenue"))
