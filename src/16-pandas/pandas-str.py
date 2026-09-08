import pandas as pd

# Load an NBA player dataset (Name, Team, and other columns) from CSV.
data = pd.read_csv("datasets/nba.csv")

# Remove any row with a missing value in ANY column, modifying `data`
# directly (inplace=True) rather than returning a new DataFrame. This
# guards the string operations below against crashing on NaN entries
# (NaN isn't a string, so calling string methods on a missing "Name"
# would fail or behave oddly).
data.dropna(inplace = True)

# Learning note: .str lets you run normal string methods across a whole column at once.
# A Series of text values doesn't automatically give you Python's string
# methods (like .upper(), .split()) directly, because a Series is a
# column of many values, not one string. The special `.str` ACCESSOR
# bridges that gap: `series.str.method()` applies the normal string
# method to EVERY value in the column at once (vectorized), skipping NaNs
# automatically, and returns a new Series of the results.

# .str.upper() would turn every name into ALL CAPS.
# data["Name"] = data["Name"].str.upper()
# .str.lower() would turn every name into lowercase.
# data["Name"] = data["Name"].str.lower()
# .str.find(sub) returns the index position of the first occurrence of
# `sub` within each string (or -1 if it's not found there) -- just like
# Python's str.find(), but applied across the whole column at once.
# data["index"] = data["Name"].str.find('a')
# .str.contains(sub) returns a boolean Series: True for every row whose
# Name contains the given substring. Using that boolean Series to filter
# `data` keeps only the matching rows -- here, players named "Jordan".
# data = data[data.Name.str.contains('Jordan')]
# .str.replace(old, new) swaps every occurrence of `old` with `new` in
# each string of the column -- here replacing spaces with dashes in team
# names (e.g. "New York" -> "New-York").
# data = data.Team.str.replace(' ','-')

# This final line is doing several string operations chained together:
# 1. data['Name'].str.split() splits each name into a list of words on
#    whitespace (e.g. "Michael Jordan" -> ["Michael", "Jordan"]).
# 2. .str.len() then measures how many words resulted from that split
#    (NOT the character length -- .str.len() works on whatever the
#    current values are, and here they are lists of words).
# 3. == 2 builds a boolean mask: True only for names that split into
#    EXACTLY two words (a clean "First Last" pattern), filtering out
#    single-word names, or names with a middle name/suffix.
# 4. data['Name'].loc[mask] uses that mask to keep only the matching
#    names (via label-based .loc filtering).
# 5. .str.split(expand=True) splits those filtered names again, but this
#    time expand=True turns the result into a DataFrame with one column
#    per split piece (column 0 = first word, column 1 = second word)
#    instead of a Series of lists.
# 6. Assigning that two-column result to data[['FirstName','LastName']]
#    creates two brand-new columns in `data`, filled in for the rows that
#    had a clean two-word name (rows with more/fewer words end up with
#    NaN in these new columns, since they weren't part of the filtered
#    split).
data[['FirstName','LastName']] = data['Name'].loc[data['Name'].str.split().str.len()==2].str.split(expand=True)


# .head(10) shows the first 10 rows of the now-modified `data`, including
# the new FirstName/LastName columns.
print(data.head(10))
