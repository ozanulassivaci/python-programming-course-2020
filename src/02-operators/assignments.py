# x = 5
# y = 10
# z = 20

# Multiple assignment: Python evaluates all the values on the right first,
# then assigns them to the names on the left, one-to-one, in a single
# statement.
# x, y, z = 5, 16, 20

# A classic trick: swapping two variables' values without needing a
# temporary third variable. Python builds a tuple (y, x) from the
# CURRENT values first, then unpacks it into x, y -- so both swap at once
# instead of the second assignment overwriting the first before it's used.
# x, y = y, x

# "Augmented assignment" operators combine an operation with assignment,
# shorthand for "take the current value, apply the operator, store it back
# in the same name":
# x += 5          # x = x + 5   (add 5)
# x -= 5          # x = x - 5   (subtract 5)
# x *= 5          # x = x * 5   (multiply by 5)
# x /= 5          # x = x / 5   (divide by 5 -- always produces a float)
# x %= 5          # x = x % 5   (remainder after dividing by 5)
# y //= 5         # y = y // 5  (floor division -- divide and round down
                   #             to the nearest whole number)
# y **= z         # y = y ** z  (raise y to the power of z)


# A comma-separated list of values with no brackets at all is still a
# tuple -- the commas are what create it, not parentheses (which are only
# needed here for grouping/readability in other contexts).
values = 1, 2, 3, 4, 5

print(values)
print(type(values))  # <class 'tuple'>

# Unpacking with a "starred" name: x takes the 1st value, y takes the 2nd,
# and *z scoops up ALL the remaining values into a list. This is called
# "extended iterable unpacking" -- the single * marks the one name that's
# allowed to soak up "everything left over".
# values = (1, 2, 3, 4, 5) -> x=1, y=2, z=[3, 4, 5]
x, y, *z = values

print(x, y, z)     # 1 2 [3, 4, 5]
print(x, y, z[1])  # 1 2 4   (z[1] is the 2nd item of the leftover list)
