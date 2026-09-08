import numpy as np

# Playing around with the basic ways to build a numpy array.
# All of these lines are commented out on purpose -- this file is a
# scratchpad of different array-creation functions. Only ever one of them
# is meant to be "live" (uncommented) at a time, feeding the final
# print(result) at the bottom. Each comment below explains what that
# particular line would produce if you uncommented it.

# np.array([1,3,5,7,9]) wraps a plain Python list into a numpy array,
# straight up -- no generation logic, just "here are the exact numbers I
# want". Result: array([1, 3, 5, 7, 9]).
# result = np.array([1,3,5,7,9])

# np.arange(start, stop) works like Python's built-in range(): it produces
# every integer starting at "start", stepping by 1, up to but NOT including
# "stop". So np.arange(1,10) gives array([1,2,3,4,5,6,7,8,9]) -- 9 comes in,
# 10 does not, exactly like range(1, 10).
# result = np.arange(1,10)

# np.arange also accepts a third argument for the step size:
# np.arange(start, stop, step). np.arange(10,100,3) starts at 10 and keeps
# adding 3 (10, 13, 16, 19, ...) while staying below 100.
# result = np.arange(10,100,3)

# np.zeros(n) builds a 1D array of length n filled entirely with 0.0
# (floats, by default). Handy as a "blank canvas" you fill in later.
# result = np.zeros(10)

# np.ones(n) is the same idea as np.zeros, but fills the array with 1.0
# instead of 0.0.
# result = np.ones(10)

# np.linspace(start, stop, count) generates "count" numbers that are evenly
# spaced between start and stop, and -- unlike arange -- it INCLUDES both
# endpoints. np.linspace(0,100,5) gives 5 evenly spaced values from 0 to
# 100 inclusive: array([0., 25., 50., 75., 100.]).
# result = np.linspace(0,100,5)

# Same function, different range: 5 evenly spaced values between 0 and 5
# inclusive: array([0., 1.25, 2.5, 3.75, 5.]).
# result = np.linspace(0,5,5)

# np.random.randint(low, high) returns a single random integer that is
# >= low and < high (high itself is never included, just like arange's
# stop). Every time you run this you can get a different number.
# result = np.random.randint(0,10)

# np.random.randint(high) with just one argument treats "low" as 0, so this
# returns a single random integer from 0 up to (but not including) 20.
# result = np.random.randint(20)

# Adding a third argument requests that many random integers at once, as an
# array, instead of just one number: 3 random integers, each from 1 up to
# (not including) 10.
# result = np.random.randint(1,10,3)

# np.random.rand(n) returns n random floats drawn uniformly from the range
# [0, 1) -- every value in that range is equally likely.
# result = np.random.rand(5)

# np.random.randn(n) is different: it draws n random floats from the
# STANDARD NORMAL distribution (the classic bell curve), which is centered
# on 0 with a standard deviation of 1. Most values land roughly between -3
# and 3, with values near 0 being the most common.
# result = np.random.randn(5)

# You can build a bigger array and then reshape it into a matrix to explore
# how row/column math works.
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)

# .sum(axis=1) adds up the values ACROSS each row (collapsing the column
# axis), giving you one total per row -- so the result has 5 numbers (one
# per row) when the matrix has 5 rows.
# print(np_multi.sum(axis=1))
# .sum(axis=0) adds up the values DOWN each column (collapsing the row
# axis), giving you one total per column -- 10 numbers here, one per
# column. A good way to remember it: axis=0 walks down the rows, axis=1
# walks across the columns.
# print(np_multi.sum(axis=0))

# rnd_numbers = np.random.randint(1,100,10)
# print(rnd_numbers)
# Once you have an array of numbers, NumPy gives you built-in statistics
# methods instead of writing your own loops:
# .max() / .min() return the single largest / smallest value in the array.
# result = rnd_numbers.max()
# result = rnd_numbers.min()
# .mean() returns the arithmetic average (sum of all values / how many
# there are).
# result = rnd_numbers.mean()
# .argmax() / .argmin() don't return the max/min VALUE itself -- they
# return the INDEX (position) where that value lives in the array. "arg"
# here means "argument that produces the extreme value".
# result = rnd_numbers.argmax()
# result = rnd_numbers.argmin()

print(result)
