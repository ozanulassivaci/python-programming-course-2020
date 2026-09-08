import pandas as pd

# Load the IMDB movies dataset (one row per movie, with columns such as
# Movie_Title, Rating, YR_Released, Num_Reviews, etc.) straight from CSV.
df = pd.read_csv("datasets/imdb.csv")

# 1- General info about the file.
result = df
# .columns lists every column name in the dataset.
result = df.columns
# NOTE: df.info WITHOUT parentheses is just a reference to the method
# itself, not a call to it -- it won't print the actual summary. Calling
# df.info() (with parentheses) would show column names, non-null counts,
# and dtypes.
result = df.info

# 2- Show the first 5 records
# .head() defaults to the first 5 rows -- a quick peek at the data.
result = df.head()

# 3- Show the first 10 records
result = df.head(10)

# 4- Show the last 5 records
# .tail() mirrors .head() but from the end of the table.
result = df.tail()

# 5- Show the last 10 records
result = df.tail(10)

# 6- Take only the Movie_Title column.
# Selecting one column name returns it as a Series.
result = df["Movie_Title"]

# 7- Take the first 5 records, only the Movie_Title column.
# Chaining .head() after selecting a column narrows both which column AND
# how many rows you see.
result = df["Movie_Title"].head()

# 8- Take the first 5 records, only Movie_Title and Rating columns.
# A list of column names keeps the 2D DataFrame shape instead of
# collapsing to a single Series.
result = df[["Movie_Title","Rating"]].head()

# 9- Take the last 7 records, only Movie_Title and Rating columns.
result = df[["Movie_Title","Rating"]].tail(7)

# 10- Take the second batch of 5 records, only Movie_Title and Rating columns.
# df[5:20] slices rows by POSITION (rows at index 5 through 19), then
# narrows to two columns, then .head() takes just the first 5 of that
# already-sliced subset -- effectively rows 5 through 9 ("the second
# batch of 5" after the first 5).
result = df[5:20][["Movie_Title","Rating"]].head()

# 11- Take the first 50 records with an imdb rating of 8.0 or above,
#     only the Movie_Title and Rating columns.
# df["Rating"] >= 8.0 builds a boolean Series (one True/False per row).
# Using it to index df keeps only the rows where Rating is 8.0+; narrowing
# to the two columns and calling .head(50) then takes the first 50 of
# those highly-rated movies.
result = df[df["Rating"] >= 8.0][["Movie_Title","Rating"]].head(50)


# 12- Get the titles of movies released between 2014 and 2015.
# Learning note: chaining boolean conditions with & needs each side wrapped in parentheses.
# "&" is the element-wise AND for boolean Series/arrays (regular Python
# "and" does not work element-wise on a whole column). Each side of "&"
# must be wrapped in parentheses because "&" binds more tightly than
# comparison operators like ">=", so without parentheses Python would try
# to evaluate the "&" before the comparisons, which breaks. This keeps
# rows released in 2014 or 2015 inclusive.
result = df[(df["YR_Released"] >= 2014) & (df["YR_Released"] <= 2015)][["Movie_Title","YR_Released"]]

# 13- List movies with more than 100,000 reviews (Num_Reviews) or an
#     imdb rating between 8 and 9.

# "|" is the element-wise OR. This keeps a movie if EITHER it has more
# than 100,000 reviews, OR its rating falls between 8 and 9 inclusive (the
# rating condition itself is grouped in its own parentheses since it's
# two ANDed comparisons being combined with the review-count condition via
# OR).
result = df[(df["Num_Reviews"] >= 100000) | ((df["Rating"] >= 8) & (df["Rating"] <= 9))][["Movie_Title","Num_Reviews","Rating"]]

print(result)
print(df.columns)
