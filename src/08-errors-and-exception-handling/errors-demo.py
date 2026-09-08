numbers = ["1", "2", "5a", "10b", "abc", "10", "50"]

# 1: Find the numeric values inside the list elements.

# for x in numbers:
#     try:
#         result = int(x)
#         print(result)
#     except ValueError:
#         continue
# A "try" block lets you attempt code that MIGHT fail, and an "except"
# block right after it says what to do if it does fail, instead of
# letting the program crash. int(x) raises a ValueError whenever x isn't
# a clean whole number string (e.g. int("5a") fails because "5a" isn't a
# valid integer, but int("10") succeeds). "except ValueError:" only
# catches THAT specific kind of error; "continue" then skips straight to
# the next loop iteration without printing anything for the bad values.
# Run against `numbers` above, this pattern would print 1, 2, 10, 50 and
# silently skip "5a", "10b", and "abc".

# 2: Keep asking for input until the user enters 'q', making sure every
# input is a number, otherwise print an error message.

# while True:
#     number = input('number: ')
#     if number == 'q':
#         break

#     try:
#         result = float(number)
#         print('you entered: ', result)
#         break
#     except ValueError:
#         print('invalid number')
#         continue
# "while True" starts a loop that would run forever unless something
# inside it explicitly stops it. Here, typing 'q' hits "break", which
# immediately exits the loop. Otherwise, float(number) is attempted; if
# it succeeds, the value is printed and "break" ends the loop; if it
# raises ValueError (e.g. the user typed "abc"), an error message is
# shown and "continue" jumps back to asking for input again.

# 3: Raise an error if the entered password contains Turkish characters.

# def check_password(password):
#     turkish_chars = 'şçğüöıİ'
#
#     for i in password:
#         if i in turkish_chars:
#             raise TypeError('Password cannot contain Turkish characters.')
#         else:
#             pass
#     print('valid password')
# "raise" manually triggers an exception yourself, instead of waiting
# for Python to trigger one from a built-in operation. Here, as soon as
# any character of the password is found inside the turkish_chars
# string, a TypeError is raised with a custom message, which immediately
# stops check_password() from running any further (the print('valid
# password') line is never reached in that case).

# password = input('password: ')

# try:
#     check_password(password)
# except TypeError as err:
#     print(err)
# "except TypeError as err:" catches the TypeError raised inside
# check_password() and binds the exception object itself to the name
# `err`. Printing `err` shows the custom message that was passed to
# raise TypeError(...) above ('Password cannot contain Turkish
# characters.'), rather than crashing the program with a traceback.

# 4: Build a factorial function and raise error messages for bad input.

# Learned that raising a ValueError lets the caller catch it with a
# regular try/except instead of the program crashing.
# factorial(x) computes x! (x factorial): x * (x-1) * (x-2) * ... * 1.
def factorial(x):
    # int(x) converts x to a whole number. If x is already an int this
    # does nothing meaningful; if x is a numeric string like "10" it
    # converts it to 10; if x is something int() can't parse (like
    # "10a"), this line itself raises a ValueError before we even reach
    # our own explicit check below.
    x = int(x)

    if x < 0:
        # raise creates and immediately throws a ValueError with a
        # custom message. This stops factorial() right here -- none of
        # the code below (the loop building up `result`) runs -- and
        # control jumps to wherever this function was called from,
        # looking for a matching except block.
        raise ValueError('Negative value')

    result = 1

    # range(1, x + 1) produces 1, 2, ..., x (the +1 is needed because
    # range's upper bound is exclusive). Multiplying `result` by each of
    # these in turn builds up the factorial: e.g. for x=5,
    # result ends up as 1*1*2*3*4*5 = 120.
    for i in range(1, x + 1):
        result *= i

    return result

# Trying the function on a mix of valid and invalid inputs shows how the
# raised errors get handled one at a time without stopping the whole
# loop:
#   x=5    -> factorial(5)  = 120, printed.
#   x=10   -> factorial(10) = 3628800, printed.
#   x=20   -> factorial(20) = 2432902008176640000, printed.
#   x=-3   -> int(-3) is already -3, then "x < 0" is True, so
#             ValueError('Negative value') is raised and caught below;
#             its message is printed instead of a result.
#   x='10a'-> int('10a') itself raises ValueError (can't parse "10a" as
#             an integer) before our own check even runs; that error is
#             caught the same way, printing its own message.
for x in [5, 10, 20, -3, '10a']:
    try:
        y = factorial(x)
    except ValueError as err:
        # Printing the exception object shows its message string, and
        # "continue" skips the "print(y)" below for this iteration since
        # `y` was never successfully assigned when an error occurred.
        print(err)
        continue
    print(y)
