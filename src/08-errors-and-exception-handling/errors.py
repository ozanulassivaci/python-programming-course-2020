# error
# An "error" (also called an "exception" in Python) is what happens when
# something goes wrong while your code is running, and Python can't
# figure out how to continue. If nothing "handles" (catches) the error,
# the program stops immediately and prints a "traceback" describing what
# went wrong and where. Python groups errors into different built-in
# TYPES (classes) depending on what kind of problem occurred, which lets
# you catch specific kinds of errors on purpose (see handling.py in this
# same folder). This file just lists a few of the most common ones and
# what triggers each:

# Error
# print(a) => NameError
# Using a variable name that was never defined/assigned anywhere raises
# a NameError -- Python has no idea what "a" refers to.
# int('1a2') => ValueError
# int() expects a string that looks like a valid whole number. '1a2'
# contains a letter, so it can't be parsed as an integer, and int()
# raises a ValueError to say "the value itself is the wrong shape for
# this operation", even though its TYPE (a string) is fine.
# print(10/0) => ZeroDivisionError
# Dividing any number by zero is mathematically undefined, so Python
# raises a ZeroDivisionError instead of returning something like
# infinity.
# print('tes't) => SyntaxError
# This one isn't a runtime error at all -- it's a mistake in the code's
# grammar itself (an unescaped/mismatched quote breaks the string
# literal), caught by Python before the program even starts running.
# SyntaxErrors can't be "caught" with try/except, because the code never
# successfully runs in the first place.

# error handling
# "Handling" an error means catching it with try/except (see
# handling.py) so your program can respond gracefully -- print a
# friendly message, retry, use a default value, etc. -- instead of
# crashing with a raw traceback.
