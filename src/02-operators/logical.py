# Logical operators combine one or more True/False conditions into a single
# True/False result. Python has three of them: 'and', 'or', and 'not'.

x = 5

attempts_left = 0
keep_going = 'y'

# Python lets you chain comparisons together, which reads almost like plain
# English. "5 < x < 10" is shorthand for "5 < x and x < 10" -- it checks
# whether x is strictly between 5 and 10. Here x is 5, so "5 < x" is already
# False, which makes the whole chained comparison False.
result = 5 < x < 10

# --- and ---
# "and" returns True only if BOTH sides are True. If either side is False,
# the whole expression is False.
# Truth table for "A and B":
#   True  and True  -> True
#   True  and False -> False
#   False and True  -> False
#   False and False -> False

# Both (x > 5) and (x < 10) need to be True for this to be True.
# x is 5, so (x > 5) is False -> the whole expression evaluates to False.
result = (x > 5) and (x < 10)

# A more "real world" example of "and": keep looping only if there are
# attempts left AND the user hasn't chosen to stop.
# attempts_left is 0, so (attempts_left > 0) is False, which makes the
# whole expression False regardless of keep_going.
result = (attempts_left > 0) and (keep_going == 'y')

# --- or ---
# "or" returns True if AT LEAST ONE side is True. It's only False when both
# sides are False.
# Truth table for "A or B":
#   True  or True  -> True
#   True  or False -> True
#   False or True  -> True
#   False or False -> False

# x is 5, and (x > 0) is True, so this is True -- it doesn't matter what
# (x % 2 == 0) evaluates to, since one True side is already enough for "or".
result = (x > 0) or (x % 2 == 0)

# --- not ---
# "not" flips a True/False value to its opposite:
#   not True  -> False
#   not False -> True

# (x > 0) is True, so "not (x > 0)" flips it to False.
result = not (x > 0)

# You can combine and/or/not to ask more complex questions in one expression.
# Here we're asking: "is x an even number between 5 and 10?"
#   (x > 5) and (x < 10)  -> is x strictly between 5 and 10?
#   (x % 2 == 0)          -> is x divisible by 2, i.e. even? (the remainder
#                            of x divided by 2 is 0)
# Both parts are combined with "and", so BOTH conditions must be True.
result = ((x > 5) and (x < 10)) and (x % 2 == 0)

print(result)
