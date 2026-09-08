import numpy as np

# Two independent arrays of 6 random integers each, drawn from [10, 100).
numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)

print(numbers1)
print(numbers2)

# NumPy arithmetic is "vectorized" and (when both operands are arrays of
# the same shape) element-wise: numbers1 + numbers2 adds the first element
# of numbers1 to the first element of numbers2, the second to the second,
# and so on, producing a new array of the same length -- all without
# writing a single explicit loop.
result = numbers1 + numbers2
# When one side is a single number (a "scalar") instead of an array, NumPy
# "broadcasts" it: the scalar is conceptually stretched to match the
# array's shape, so numbers1 + 10 adds 10 to every element individually.
result = numbers1 + 10
result = numbers1 - numbers2
result = numbers1 - 10
# Multiplication here is also element-wise (NOT matrix/dot-product
# multiplication) -- each pair of matching elements is multiplied
# together.
result = numbers1 * numbers2
result = numbers1 * 10
# Division works the same element-wise way; dividing integer arrays like
# this still produces a float array, since division can create fractions.
result = numbers1 / numbers2
result = numbers1 / 10

# Learning note: these operate element-wise on the whole array, no loop needed.
# NumPy provides vectorized math functions that mirror Python's `math`
# module but work on entire arrays at once, applying the function to every
# element independently and returning a new array of the same shape.
result = np.sin(numbers1)   # sine of each element (in radians)
result = np.cos(numbers1)   # cosine of each element (in radians)
result = np.sqrt(numbers1)  # square root of each element
result = np.log(numbers1)   # natural logarithm (base e) of each element

# Reshaping both 6-element 1D arrays into 2x3 matrices, so we can explore
# how stacking works on 2D data.
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)

# print(mnumbers1)
# print(mnumbers2)

# np.vstack (vertical stack) stacks arrays on top of each other, adding
# more ROWS. Two (2,3) matrices stacked vertically become one (4,3)
# matrix: mnumbers1's rows, then mnumbers2's rows, one below the other.
result = np.vstack((mnumbers1,mnumbers2))
# np.hstack (horizontal stack) stacks arrays side by side, adding more
# COLUMNS. Two (2,3) matrices stacked horizontally become one (2,6)
# matrix: each row gets mnumbers1's columns followed by mnumbers2's
# columns.
result = np.hstack((mnumbers1,mnumbers2))

# Comparison operators on an array also work element-wise and produce a
# boolean array (a "mask") of the same shape, with True/False for whether
# each individual element satisfies the condition.
result = numbers1 >= 50
result = numbers1 % 2 == 0

# Using a boolean array as an index -- numbers1[result] -- is called
# "boolean masking": NumPy keeps only the elements of numbers1 where the
# mask is True and drops the rest. Since `result` was just reassigned to
# "numbers1 % 2 == 0" above, this prints only the even values from
# numbers1.
print(numbers1[result])

# This prints the boolean mask itself (the array of True/False values),
# not the filtered numbers -- useful for seeing exactly which positions
# were True.
print(result)
