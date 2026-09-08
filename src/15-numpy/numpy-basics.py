import numpy as np

# NumPy ("Numerical Python") is a library for working with arrays of numbers
# very fast. Its core object is the "ndarray" (n-dimensional array). The
# convention "import numpy as np" is used almost everywhere in the Python
# world, so np.array(...), np.arange(...), etc. will look familiar in any
# NumPy code you read later.

# plain python list
# A regular Python list can hold ANY mix of types (numbers, strings, other
# lists...) and Python stores it as a collection of separate objects. That
# flexibility makes lists slow for heavy numeric work: doing math over a
# list normally means writing a for-loop and touching each element one by
# one, with Python's per-element overhead every time.
py_list = [1,2,3,4,5,6,7,8,9]

# numpy array
# same numbers, but numpy gives it shape/dim info a plain list doesn't have
# np.array() converts a Python list (or nested list) into an ndarray. Under
# the hood, NumPy stores all the values contiguously in memory as a single
# fixed data type (here, integers), which is what lets it do math on the
# whole array at once ("vectorized" operations) instead of looping in
# Python. It's also what unlocks extra attributes like .shape and .ndim
# that a plain list simply doesn't have.
np_array = np.array([1,2,3,4,5,6,7,8,9])

# type() reports the Python class of an object. This will show that py_list
# is a <class 'list'> while np_array is a <class 'numpy.ndarray'> -- two
# genuinely different kinds of objects, even though they hold the "same"
# numbers.
print(type(py_list))
print(type(np_array))

# A "list of lists" is how you'd fake a 2D grid/matrix using only plain
# Python -- each inner list is one row.
py_multi = [[1,2,3],[4,5,6],[7,8,9]]

# .reshape(rows, cols) takes the 9 values already sitting in np_array (which
# is currently a flat, 1-dimensional array of length 9) and reinterprets
# them as a 3x3 grid, filling row by row. It does NOT create new data or
# lose any values -- it just changes how the same 9 numbers are organized/
# viewed. Reshaping requires the total element count to match: 3 rows * 3
# columns = 9, which is exactly how many numbers we started with.
np_multi = np_array.reshape(3,3)

# Printing the plain Python list of lists shows Python's own repr: nested
# square brackets, e.g. [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
print(py_multi)
# Printing a 2D numpy array shows NumPy's own nicer, aligned-columns repr,
# which visually looks like a real matrix (each row on its own line).
print(np_multi)

# .ndim tells you how many dimensions/axes an array has.
# np_array is flat (just one axis of 9 elements), so np_array.ndim is 1.
print(np_array.ndim)
# np_multi was reshaped into rows and columns (two axes), so np_multi.ndim
# is 2.
print(np_multi.ndim)

# .shape reports the size along each axis, as a tuple.
# np_array is 1D with 9 elements, so its shape is (9,) -- note the trailing
# comma, which is Python's way of writing a 1-element tuple.
print(np_array.shape)
# np_multi is 3 rows by 3 columns, so its shape is (3, 3).
print(np_multi.shape)
