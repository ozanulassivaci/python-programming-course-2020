name = 'Ozan'
surname = 'Sivaci'
age = 36

# str.format() fills in {} placeholders from left to right by default,
# matching them to the arguments in the order given.
# print('My name is {} {}'.format(name, surname))

# You can also number the placeholders explicitly to control (or change)
# the order they're filled in -- {1} means "use the 2nd argument here",
# {0} means "use the 1st argument here", regardless of where they sit in
# the string.
# print('My name is {1} {0}'.format(name, surname))

# Or name them, and pass matching keyword arguments -- this can make long
# format strings much easier to read, since you don't have to count
# positions.
# print('My name is {s} {n}'.format(n=name, s=surname))

# Placeholders don't have to be filled with different arguments -- and
# non-string values like age (an int) are automatically converted to text.
# print("My name is {} {} and I'm {} years old.".format(name, surname, age))

# The exact same argument can also be reused for every placeholder.
# print("My name is {} {} and I'm {} years old.".format(name, name, name))

# result = 200 / 700
# format() also supports a "format spec" after a colon inside the braces,
# for controlling how a number is displayed. {r:1.4} means "show the
# value of r with 4 significant digits total".
# print('the result is {r:1.4}'.format(r=result))

# f-strings feel a lot more readable than .format() once you get used to
# them: put an f right before the opening quote, and any {expression}
# inside the string is evaluated live and inserted directly -- no need to
# call a separate method or pass positional/keyword arguments at all.
print(f"My name is {name} {surname} and I'm {age} years old.")
