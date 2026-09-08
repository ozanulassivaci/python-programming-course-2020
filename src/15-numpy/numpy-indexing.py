import numpy as np

numbers = np.array([0,5,10,15,20,25,50,75])

# Basic indexing works like Python lists: numbers[5] is the element at
# index 5 (0-based counting: 0,5,10,15,20 -> index 5 is 25).
result = numbers[5]
# Negative indices count from the END of the array: -1 is the last
# element, -2 the second-to-last, and so on. numbers[-1] is 75.
result = numbers[-1]
# Slicing with [start:stop] returns a NEW array containing elements from
# "start" up to (but not including) "stop". numbers[0:3] gives the first
# three elements: array([0, 5, 10]).
result = numbers[0:3]
# When "start" is left out, it defaults to the very beginning (index 0),
# so numbers[:3] is identical to numbers[0:3].
result = numbers[:3]
# When "stop" is left out, it defaults to the very end of the array, so
# numbers[3:] means "everything from index 3 onward".
result = numbers[3:]
# Leaving out both start and stop (and no step) just returns every
# element -- effectively a full copy-like view of the whole array.
result = numbers[::]
# A step of -1 with no start/stop walks the array backwards, which is the
# standard idiom for reversing a sequence: numbers[::-1] reverses the
# whole array.
result = numbers[::-1]

# A 2D array (a "matrix") is built from a list of lists -- each inner list
# becomes one row.
numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
# Indexing a 2D array with one number selects an entire ROW as a 1D array.
# numbers2[0] is the first row: array([0, 5, 10]).
result = numbers2[0]
# numbers2[2] is the third row (index 2): array([50, 75, 85]).
result = numbers2[2]
# Two comma-separated indices, numbers2[row, col], pick out a single
# element: row index 0, column index 2 -> the value 10.
result = numbers2[0,2]
# Row index 2, column index 1 -> the value 75.
result = numbers2[2,1]
# numbers2[:,2] means "all rows, column index 2 only" -- this slices out
# an entire COLUMN (the third one) as a 1D array: array([10, 25, 85]).
result = numbers2[:,2]
# Same idea for the first column (index 0): array([0, 15, 50]).
result = numbers2[:,0]
# Combining a full-row slice (:) with a column slice (0:2) selects all
# rows but only columns 0 and 1, giving a smaller 2D sub-matrix.
result = numbers2[:,0:2]
# numbers2[-1,:] means "last row, all columns" -- the entire last row.
result = numbers2[-1,:]
# numbers2[:2,:2] takes rows 0 and 1 (":2" = up to index 2, exclusive) and
# columns 0 and 1, giving the top-left 2x2 corner of the matrix.
result = numbers2[:2,:2]

# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # this would just be a reference to the same array
# Learning note: .copy() actually copies the data, plain assignment does not - this bit me once.
# In Python (and NumPy), plain assignment like "arr2 = arr1" does NOT
# duplicate the array's data -- it just makes arr2 another name pointing
# at the exact same array in memory. Changing arr2 through that reference
# would also change arr1, which usually surprises beginners.
# .copy() explicitly allocates a brand-new array with its own memory and
# copies all the values into it, so afterward arr1 and arr2 are completely
# independent -- modifying one will never affect the other.
arr2 = arr1.copy()

# Because arr2 is an independent copy, changing its first element...
arr2[0] = 20

# ...leaves arr1 completely untouched (still starts with 0), while arr2
# now starts with 20 instead of 0. This demonstrates exactly why .copy()
# matters: without it, this same edit would have changed arr1 too.
print(arr1)
print(arr2)
