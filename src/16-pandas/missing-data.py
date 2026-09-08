import pandas as pd
import numpy as np

# 15 random integers 10-99, reshaped into a 5-row by 3-column grid.
data = np.random.randint(10,100,15).reshape(5,3)

# Custom row labels 'a','c','e','f','h' -- notice 'b','d','g' are
# deliberately skipped, which sets up the next line's reindexing gap.
df = pd.DataFrame(data, index = ['a','c','e','f','h'], columns = ['column1','column2','column3'])

# .reindex(new_labels) rebuilds the DataFrame to have EXACTLY the given
# row labels, in that order. Labels that already existed keep their data;
# labels that are NEW (here: 'b','d','g') get inserted as brand-new rows
# filled entirely with NaN, since there's no existing data for them. This
# is a common way to deliberately introduce gaps/missing data for
# practice, or to align a DataFrame to a specific expected set of rows.
df = df.reindex(['a','b','c','d','e','f','g','h'])

# np.nan is numpy's/pandas' standard "missing value" marker for floating
# point data. Building a new column with some np.nan entries mixed in
# simulates real-world messy data where some measurements are missing.
new_column = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["column4"] = new_column

result = df
# .drop(label, axis=1) removes a COLUMN by name (axis=1 = columns).
result = df.drop("column1", axis = 1)
# You can drop several columns at once by passing a list of names.
result = df.drop(["column1","column2"], axis = 1)
# .drop(label, axis=0) removes a ROW by its index label (axis=0 = rows,
# and is also the default if you omit axis entirely).
result = df.drop('a', axis = 0)
result = df.drop(['a','b','h'], axis = 0)

# .isnull() returns a same-shaped DataFrame of True/False: True wherever a
# cell holds a missing value (NaN), False where real data exists.
result = df.isnull()
# .notnull() is the exact opposite of .isnull(): True where data IS
# present.
result = df.notnull()
# Summing a boolean DataFrame treats True as 1 and False as 0, so
# .isnull().sum() gives a per-COLUMN count of how many missing values each
# column has.
result = df.isnull().sum()
# Doing the same on a single column (Series) gives just that one column's
# missing-value count as a plain number.
result = df["column1"].isnull().sum()
# Using the boolean mask df["column1"].isnull() to filter the WHOLE
# DataFrame keeps only the rows where column1 is missing -- handy for
# inspecting exactly which records have a gap.
result = df[df["column1"].isnull()]
# Same filter, but narrowed down to just show the (all-missing, by
# definition) column1 values for those rows.
result = df[df["column1"].isnull()]["column1"]
# The opposite filter -- keep only rows where column1 IS present -- shows
# the real, non-missing values.
result = df[df["column1"].notnull()]["column1"]

# .dropna() removes any ROW that contains at least one NaN anywhere in it
# (axis=0 is the default, meaning "drop along rows").
result = df.dropna() # axis = 0 => drop rows
# axis=1 instead drops any COLUMN that contains at least one NaN --
# since column4 has several NaNs, and the reindexed rows introduced NaNs
# into every original column too, this can end up dropping most/all
# columns depending on how much missing data exists.
result = df.dropna(axis = 1) # axis = 1 => drop columns
# how="any" (the default for dropna) drops a row if ANY of its values are
# missing -- equivalent to the plain df.dropna() above.
result = df.dropna(how = "any")
# how="all" is stricter about what counts as droppable: only drops a row
# if EVERY single value in it is missing (all-NaN rows) -- e.g. the fully
# blank rows 'b','d','g' that reindex() introduced.
result = df.dropna(how = "all")
# subset=[...] restricts which columns are even considered when deciding
# whether to drop a row -- other columns' missing values are ignored.
# Combined with how="all", this drops a row only if BOTH column1 and
# column2 are missing in it.
result = df.dropna(subset  = ["column1","column2"], how = "all")
# Combined with how="any" instead, this drops a row if EITHER column1 or
# column2 (or both) is missing.
result = df.dropna(subset  = ["column1","column2"], how = "any")
# thresh=N keeps a row only if it has AT LEAST N non-null (real, present)
# values -- rows with fewer real values than that get dropped.
result = df.dropna(thresh = 2)
# thresh => minimum number of non-null values required to keep the row
result = df.dropna(thresh = 3) # thresh => minimum number of non-null values required to keep the row

# .fillna(value) replaces every NaN in the DataFrame with the given value
# -- here, the literal string 'no input' (mixing text into numeric columns
# like this is fine in pandas, though it can change a column's dtype to
# "object").
result = df.fillna(value = 'no input')
# Filling with a number (1) instead keeps things numeric.
result = df.fillna(value = 1)

# .sum() on a whole DataFrame sums each column independently, returning a
# Series of per-column totals (NaNs are skipped/treated as 0 by default).
result = df.sum()
# Chaining another .sum() adds those per-column totals together into one
# single grand-total number across the entire table.
result = df.sum().sum()
# .size is the TOTAL number of cells in the DataFrame (rows * columns),
# including any that are NaN -- a plain count, not a computation.
result = df.size
result = df.isnull().sum()
# Total count of missing values across the ENTIRE DataFrame (sum of
# per-column missing counts).
result = df.isnull().sum().sum()


# Learning note: had to subtract the null count from the total size to get the real count of values.
# A hand-written helper to compute the TRUE average of every real
# (non-missing) value across the whole DataFrame. df.sum().sum() adds up
# every actual number present (NaNs contribute nothing to a sum). But to
# get a correct average, we can't just divide by df.size, because that
# would count the missing cells too and understate the true average --
# so we subtract the total NaN count from df.size to get the real count
# of numbers that were actually summed.
def average(df):
    total = df.sum().sum()
    count = df.size - df.isnull().sum().sum()
    return total / count

# Using that computed average to fill in every missing value -- a common
# simple strategy ("mean imputation") for dealing with gaps in numeric
# data without just throwing rows/columns away.
result = df.fillna(value = average(df))

print(result)
