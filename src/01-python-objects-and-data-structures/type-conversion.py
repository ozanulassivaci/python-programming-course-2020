"""
x = input('1st number: ')
y = input('2nd number: ')

print(type(x))
print(type(y))

total = int(x) + int(y)

print(total)
"""
# The block above (kept as a triple-quoted string so it doesn't execute)
# illustrates why type conversion matters: input() ALWAYS returns a
# string, so both type(x) and type(y) would print <class 'str'> even if
# the user typed digits. Without wrapping each one in int(...), writing
# `x + y` would concatenate the two strings of digits together instead of
# adding them numerically (e.g. '2' + '3' -> '23', not 5).

x = 5                # int   -- a whole number, no decimal point
y = 2.5               # float -- has a decimal point
name = 'Kerem'        # str   -- text, in quotes
is_online = True      # bool  -- True or False

# type() is a built-in function that tells you the exact type of a value
# at runtime -- handy for confirming your assumptions while learning.
# print(type(x))
# print(type(y))
# print(type(name))
# print(type(is_online))

# Type Conversion
# Converting between types is done by calling the target type as a
# function on the value: int(...), float(...), str(...), bool(...).

# int to float

# x = float(x)
# print(x)          # 5.0 -- note the added decimal point
# print(type(x))    # <class 'float'>

# float to int

# y = int(y)
# int() TRUNCATES the decimal part rather than rounding -- int(2.5) gives
# 2, not 3. (round(2.5) would round instead, but that's a different
# function with different behavior.)
# print(y)
# print(type(y))

# result = str(x) + str(y)
# Converting numbers to strings first lets you concatenate them with "+"
# the same way you would join two pieces of text.
# print(result)
# print(type(result))

# bool to str

# is_online = str(is_online)
# print(is_online)       # the text 'True' (still needs quotes to use as
                          # a string afterward -- it's no longer a bool)
# print(type(is_online))  # <class 'str'>

# bool to int
# Learned that True/False convert to 1/0 when cast to int

is_online = False

# Internally, Python treats True as equal to 1 and False as equal to 0 --
# int() on a bool makes that numeric identity explicit.
is_online = int(is_online)
print(is_online)        # 0
print(type(is_online))  # <class 'int'>
