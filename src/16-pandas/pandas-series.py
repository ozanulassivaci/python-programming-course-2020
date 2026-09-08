import pandas as pd
import numpy as np

# pandas is built on top of numpy and adds two key data structures:
# - Series: a single labeled 1D column of data (like a spreadsheet column).
# - DataFrame: a labeled 2D table made of multiple Series (like a whole
#   spreadsheet). This file focuses on Series.

# data
numbers = [20,30,40,50]
letters = ['a','b','c','d']
dict = {'a':10,'b':20,'c':30,'d':40}
random_numbers = np.random.randint(10,100,6)

# A pandas Series wraps a sequence of values together with an "index" --
# a label for each value (by default 0, 1, 2, ... but you can supply your
# own, like letters or dates). Think of it as a numpy array that
# remembers a name for every position, instead of just a numeric offset.

# pd.Series() with no arguments creates an empty Series (no data, no
# index) -- rarely useful on its own, but shows the "base case".
# pandas_series = pd.Series()
# Passing just a list uses the list's values with a DEFAULT index of
# 0, 1, 2, 3 (since no explicit labels were given).
# pandas_series = pd.Series(numbers)
# Series values don't have to be numbers -- here we build one from a list
# of strings, again with the default 0,1,2,3 index.
# pandas_series = pd.Series(letters)
# pd.Series(scalar, index_list) "broadcasts" a single value across every
# label in the given index -- this creates 4 entries (indices 0,1,2,3),
# each holding the value 5.
# pandas_series = pd.Series(5, [0,1,2,3])
# Here we explicitly pair up the `numbers` values with custom labels
# ['a','b','c','d'] -- so instead of numbers[0] you'd access it as
# pandas_series['a'].
# pandas_series = pd.Series(numbers, ['a','b','c','d'])
# Building a Series straight from a dict: the dict's KEYS automatically
# become the index labels, and the dict's VALUES become the Series data.
# pandas_series = pd.Series(dict)
# You can also build a Series directly from a numpy array; it behaves the
# same as building one from a list.
# pandas_series = pd.Series(random_numbers)

# The "live" Series used for the examples below: values [20,30,40,51]
# labeled 'a','b','c','d' respectively (a->20, b->30, c->40, d->51).
pandas_series = pd.Series([20,30,40,51], ['a','b','c','d'])


# Even with custom string labels, you can STILL use plain integer position
# to look things up -- pandas_series[0] is the first entry by position
# (20, labeled 'a').
# result = pandas_series[0]
# Negative indices count from the end, same idea as Python lists/numpy:
# the last entry (51, labeled 'd').
# result = pandas_series[-1]
# Slicing by position works too: the first two entries ('a' and 'b').
# result = pandas_series[:2]
# The last two entries ('c' and 'd').
# result = pandas_series[-2:]
# You can also look values up by their LABEL instead of position --
# pandas_series['a'] returns the value stored under label 'a' (20).
# result = pandas_series['a']
# result = pandas_series['d']
# Passing a LIST of labels returns a new Series with just those entries,
# in that order. Note 'e' does not exist in this Series -- asking for a
# missing label like this raises a KeyError (in newer pandas versions),
# so this particular commented-out line is here to highlight that gotcha,
# not something you'd want to actually run as-is.
# result = pandas_series[['a','c','e']]
# .ndim reports the number of dimensions -- a Series is always 1D, so this
# is always 1.
# result = pandas_series.ndim
# .dtype reports the underlying data type of the values (e.g. int64 for
# whole numbers, float64 for decimals, object for strings/mixed types).
# result = pandas_series.dtype
# .shape reports the size as a tuple, just like numpy -- (4,) here, since
# there are 4 values.
# result = pandas_series.shape
# Series come with the same kind of aggregate methods as numpy arrays:
# .sum() adds up every value.
# result = pandas_series.sum()
# .max() / .min() return the largest / smallest value.
# result = pandas_series.max()
# result = pandas_series.min()
# Arithmetic on a Series is vectorized just like numpy: adding a Series to
# itself doubles every value, matched up by index label.
# result = pandas_series + pandas_series
# Adding a scalar broadcasts it across every value (each element + 50).
# result = pandas_series + 50
# numpy functions like np.sqrt() also work directly on a Series, applying
# element-wise and returning a new Series with the same labels.
# result = np.sqrt(pandas_series)

# Comparisons produce a Series of True/False values, one per label,
# instead of a single answer -- this is what lets you build boolean masks
# for filtering, just like with numpy arrays.
# result = pandas_series >=50
# result = pandas_series % 2 == 0

# print(pandas_series[pandas_series % 2 == 0])
# print(pandas_series)
# print(result)


# Learning note: adding two Series aligns them by index label, mismatched labels become NaN.
# These two Series both describe car sales but have slightly different
# labels: opel2018 has "mokka" where opel2019 has "Grandland" instead.
opel2018 = pd.Series([20,30,40,10],["astra","corsa","mokka","insignia"])
opel2019 = pd.Series([40,30,20,10],["astra","corsa","Grandland","insignia"])

# When you add two Series together, pandas does NOT just add them
# position-by-position like numpy would -- it first ALIGNS the two Series
# by their index labels. Matching labels ("astra", "corsa", "insignia")
# get added together normally. A label that exists in only ONE of the two
# Series ("mokka" from 2018, "Grandland" from 2019) has nothing to pair
# with, so pandas can't compute a real sum for it and fills that spot with
# NaN ("Not a Number", pandas'/numpy's marker for missing data) in the
# result.
total = opel2018 + opel2019
# "astra" exists in both Series (20 from opel2018, 40 from opel2019), so
# this prints their aligned sum: 60.
print(total["astra"])
