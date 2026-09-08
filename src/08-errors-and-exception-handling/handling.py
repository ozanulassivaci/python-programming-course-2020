# error handling

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print('you entered wrong info')
#     print(e)
# A single except clause can catch MULTIPLE exception types at once by
# listing them in a tuple, like (ZeroDivisionError, ValueError). If
# EITHER kind of error happens anywhere inside the try block -- int()
# failing to parse non-numeric input (ValueError), or dividing by a y of
# 0 (ZeroDivisionError) -- this except block runs and `e` is bound to
# whichever exception object was actually raised.

# try:
#     x = int(input('x: '))
#     y = int(input('y: '))
#     print(x/y)
# except:
#     print('you entered wrong info')
# A bare "except:" with no exception type listed catches ANY exception
# at all, not just the ones you're expecting. This is usually considered
# poor practice, because it can silently swallow bugs you didn't
# anticipate (like a typo causing a NameError) along with the ones you
# meant to handle.

# Learned that else runs only when no exception was raised, and finally
# always runs, even after break.
# The full anatomy of try/except/else/finally, tied together with a
# loop, so the user gets to keep retrying until they succeed:
#   try:      code that might fail goes here.
#   except:   runs ONLY if an exception was raised inside try, and only
#             if it matches the exception type(s) listed.
#   else:     runs ONLY if the try block completed with NO exception at
#             all -- it's a place to put code that should happen after a
#             successful try, but that you don't want protected by the
#             try itself (so its own errors, if any, aren't swallowed by
#             this except clause).
#   finally:  ALWAYS runs no matter what -- whether try succeeded,
#             failed, or even if a break/return/continue is executed
#             inside try/except/else. It's typically used for cleanup
#             work (like closing a file) that must happen either way.
while True:
    try:
        # input() always returns a string; int() converts it to a whole
        # number, raising ValueError if the text isn't a valid integer
        # (e.g. the user types "abc").
        x = int(input('x: '))
        y = int(input('y: '))
        # If y is 0, this division raises ZeroDivisionError.
        print(x/y)
    except Exception as ex:
        # "Exception" is the common base class that almost all built-in
        # errors inherit from (including ValueError and
        # ZeroDivisionError), so catching "Exception" here catches both
        # of those problems (and most others) in one except clause.
        # Binding it to `ex` lets us print Python's own description of
        # what went wrong alongside our own message.
        print('you entered wrong info', ex)
    else:
        # This only runs if x and y were both parsed successfully AND
        # the division didn't raise -- i.e. everything in try succeeded.
        # Breaking here is what actually ends the "keep asking" loop
        # once valid input has been given.
        break
    finally:
        # Runs after every single iteration of the loop, whether that
        # iteration hit the except branch or the else/break branch --
        # useful for a message (or real cleanup code) that should always
        # happen regardless of outcome.
        print('try except finished.')
