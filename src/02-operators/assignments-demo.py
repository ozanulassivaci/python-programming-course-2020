x, y, z = 2, 5, 10

# 1- What is the difference between the product of two user-entered numbers
#    and the sum of x, y, z?

# a = int(input('1st number: '))
# b = int(input('2nd number: '))

# "*" multiplies (product), "+" adds (sum); the outer parentheses just
# make the two sub-results explicit before subtracting them.
# result = (a * b) - (x+y+z)

# 2- Calculate y divided by x, without remainder.
# "//" is floor division: it divides and then rounds DOWN to the nearest
# whole number, discarding any remainder entirely (unlike "/", which
# would give a float with a decimal part).
# y=5, x=2 -> 5/2 = 2.5 -> floor division rounds down to 2.
result = y // x

# 3- What is (x, y, z) sum mod 3?
# "%" (modulo) gives the remainder of a division.
total = (x + y + z)          # 2 + 5 + 10 = 17
result = total % 3           # 17 divided by 3 is 5 remainder 2, so this is 2


# 4- Calculate y to the power of x.
# "**" is exponentiation: y ** x means "y raised to the power of x".
# 5 ** 2 = 25
result = y ** x

# 5- Given x, *y, z = numbers, what is z cubed?
numbers = 1, 5, 7, 10, 6
# Starred unpacking: x grabs the first value, z grabs the last value, and
# *y scoops up everything left in between into a list.
# x = 1, y = [5, 7, 10], z = 6
x, *y, z = numbers
# "cubed" means raised to the power of 3. 6 ** 3 = 216.
result = z ** 3


# 6- Given x, *y, z = numbers, what is the sum of the values in y?

numbers = 1, 5, 7, 10, 6
x, *y, z = numbers  # y = [5, 7, 10]

# Adding the three items of y up individually by index: 5 + 7 + 10 = 22.
result = y[0] + y[1] + y[2]

print(result)
