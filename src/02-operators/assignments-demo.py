x, y, z = 2, 5, 10

# 1- What is the difference between the product of two user-entered numbers
#    and the sum of x, y, z?

# a = int(input('1st number: '))
# b = int(input('2nd number: '))

# result = (a * b) - (x+y+z)

# 2- Calculate y divided by x, without remainder.
result = y // x

# 3- What is (x, y, z) sum mod 3?

total = (x + y + z)
result = total % 3


# 4- Calculate y to the power of x.
result = y ** x

# 5- Given x, *y, z = numbers, what is z cubed?
numbers = 1, 5, 7, 10, 6
x, *y, z = numbers
result = z ** 3


# 6- Given x, *y, z = numbers, what is the sum of the values in y?

numbers = 1, 5, 7, 10, 6
x, *y, z = numbers

result = y[0] + y[1] + y[2]

print(result)
