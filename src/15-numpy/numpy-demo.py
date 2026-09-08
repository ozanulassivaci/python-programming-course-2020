import numpy as np

# 1- Create a numpy array with values (10,15,30,45,60).
# np.array() takes a plain Python list of specific values and turns it into
# a numpy array holding exactly those values, in that order.
result = np.array([10,15,30,45,60])

# 2- Create a numpy array with numbers between 5 and 15.
# np.arange(start, stop) counts up from "start" in steps of 1, stopping
# just BEFORE "stop" (stop itself is excluded). So this gives
# array([5,6,7,8,9,10,11,12,13,14]) -- 10 numbers, ending at 14, not 15.
result = np.arange(5,15)

# 3- Create a numpy array from 50 to 100, stepping by 5.
# The optional third argument to arange is the step size: start at 50, add
# 5 each time, stop before passing 100 -> array([50,55,60,...,95]).
result = np.arange(50,100,5)

# 4- Create an array of 10 zeros.
# np.zeros(n) makes a length-n array of the float 0.0, useful as a starting
# "empty" container you plan to fill in later.
result = np.zeros(10)

# 5- Create an array of 10 ones.
# np.ones(n) is the same idea as np.zeros but fills with 1.0 instead.
result = np.ones(10)

# 6- Generate 5 evenly spaced numbers between 0 and 100.
# np.linspace(start, stop, count) picks "count" numbers evenly spaced
# across the range, and it includes BOTH endpoints (unlike arange, which
# excludes the stop value). Here: array([0., 25., 50., 75., 100.]).
result = np.linspace(0,100,5)

# 7- Generate 5 random integers between 10 and 30.
# np.random.randint(low, high, size) draws "size" random integers, each
# one >= low and < high (high is excluded). Every run of this line can
# produce different numbers since it's random.
result = np.random.randint(10,30,5)

# 8- Generate 10 random numbers (roughly between -1 and 1).
# np.random.randn(n) draws n samples from the standard normal (bell curve)
# distribution: centered on 0, with about 68% of values falling within
# +/-1 and almost all of them within +/-3. "Roughly between -1 and 1" is
# describing where MOST (not all) of the values will typically land.
result = np.random.randn(10)

# 9- Create a (3x5) matrix with random values between 10 and 50.
# .reshape(3,5) takes a flat array of 15 random integers and folds it into
# a grid of 3 rows and 5 columns (3 * 5 = 15, so all the values fit exactly
# with none left over and none missing).
# result = np.random.randint(10,50,15).reshape(3,5)

# 10- What are the row and column totals of the generated matrix?
# Learning note: reshape lets me turn a flat array into a matrix without copying data.
# (This matrix uses the range -50 to 50 instead of 10 to 50, just to make
# the "positive/negative" filtering exercise further down more interesting.)
matrix = np.random.randint(-50,50,15).reshape(3,5)
print(matrix)
# .sum(axis=1) sums each ROW across its columns, so you get one total per
# row (3 numbers here, since there are 3 rows).
# row_total = matrix.sum(axis = 1)
# .sum(axis=0) sums each COLUMN down its rows, giving one total per column
# (5 numbers here, since there are 5 columns).
# col_total = matrix.sum(axis = 0)
# print(matrix)
# print(row_total)
# print(col_total)

# 11- What are the max, min and mean of the generated matrix?
# Called with no axis argument, these methods look at EVERY element in the
# whole matrix (ignoring row/column structure) and return a single number:
# the overall biggest value, smallest value, and average, respectively.
result = matrix.max()
result = matrix.min()
result = matrix.mean()

# 12- What is the index of the largest value in the matrix?
# .argmax()/.argmin() on a multi-dimensional array first FLATTEN the array
# (treat it as one long 1D sequence, row by row) and then report the
# position of the max/min value within that flattened sequence.
result = matrix.argmax()
result = matrix.argmin()

# 13- Select the first 3 elements of an array containing numbers 10 to 20.
arr = np.arange(10,20)
print(arr)

# Slicing syntax array[start:stop] works just like Python list slicing:
# arr[:3] means "from the beginning up to (not including) index 3", i.e.
# the first 3 elements: array([10, 11, 12]).
result = arr[:3]

# 14- Print the elements of the array in reverse order.
# The slice [::-1] means "every element (no start/stop given), stepping by
# -1" -- i.e. walk the array backwards from the last element to the first.
# This is a very common Python/NumPy idiom for reversing a sequence.
result = arr[::-1]

# 15- Select the first row of the matrix.
# For a 2D array, a single index like matrix[0] selects the entire first
# row (index 0) as a 1D array.
result = matrix[0]

# 16- Which element is in row 2, column 3 of the matrix?
# NumPy uses 0-based indexing, so "row 2, column 3" (counting from 1, as a
# human would) corresponds to index [1, 2] in code. matrix[1,2] reads: row
# at index 1, column at index 2 -- a single scalar value.
result = matrix[1,2]

# 17- Select the first element of every row in the matrix.
# matrix[:,0] means "all rows (:), column index 0" -- this pulls out the
# entire first COLUMN as a 1D array, which is the same thing as "the first
# element of every row".
result = matrix[:,0]

# 18- Square every element of the matrix.
# matrix ** 2 is a vectorized operation: NumPy applies "raise to the power
# of 2" to every single element of the matrix at once, with no explicit
# loop needed, and returns a new matrix of the same shape.
result = matrix ** 2

# 19- Which elements of the matrix are positive even numbers?
#     Use a range of (-50, +50).
# Learning note: boolean masking (matrix[condition]) still feels like magic compared to writing a loop.
# matrix % 2 == 0 computes the remainder of every element divided by 2 and
# compares it to 0, producing a same-shaped array of True/False values (a
# "boolean mask") -- True wherever the original element is even. Since the
# matrix holds random values from -50 to 49, this mask marks both negative
# and positive even numbers.
# Using that boolean mask INSIDE square brackets, matrix[mask], tells NumPy
# to keep only the elements where the mask is True and drop the rest,
# flattening the result into a 1D array. So `evens` ends up holding just
# the even numbers from the matrix (positive, negative, or zero).
evens = matrix[matrix % 2 == 0]
# Repeating the same boolean-masking trick on `evens` with the condition
# > 0 keeps only the positive values, leaving positive even numbers only.
result = evens[evens>0]

print(result)
