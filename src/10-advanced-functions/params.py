def add(a, b):
    return a+b
def subtract(a, b):
    return a-b
def multiply(a, b):
    return a*b
def divide(a, b):
    return a/b

# Learned that functions can be passed around as regular arguments,
# and picked between with plain if/elif on a name string.
# Because functions are values in Python (see closures.py in this same
# folder for more on that idea), you can pass several different
# functions into another function as ordinary arguments, exactly like
# you'd pass numbers or strings. Here, `operation` receives all four
# math functions (f1, f2, f3, f4) PLUS a string telling it which one to
# actually use -- f1/f2/f3/f4 are just local names inside `operation`
# for whatever functions were passed in as add/subtract/multiply/divide.
def operation(f1, f2, f3, f4, operation_name):
    if operation_name == "add":
        # f1 is whatever was passed as the first argument (add, in every
        # call below). f1(2, 3) calls it with 2 and 3, printing 5.
        print(f1(2, 3))
    elif operation_name == "subtract":
        # f2(5, 3) calls whatever was passed as the second argument
        # (subtract), printing 5 - 3 = 2.
        print(f2(5, 3))
    elif operation_name == "multiply":
        # f3(3, 4) calls whatever was passed as the third argument
        # (multiply), printing 3 * 4 = 12.
        print(f3(3, 4))
    elif operation_name == "divide":
        # f4(10, 2) calls whatever was passed as the fourth argument
        # (divide), printing 10 / 2 = 5.0 (division in Python 3 always
        # produces a float, even when the result is a whole number).
        print(f4(10, 2))
    else:
        # No operation_name matched any of the branches above, so
        # neither f1, f2, f3, nor f4 gets called at all in this case.
        print("invalid operation...")

# Every call below passes the SAME four functions in the SAME order
# (add, subtract, multiply, divide); only the operation_name string
# changes, which decides which one of the four actually gets used.
operation(add, subtract, multiply, divide, "add")       # prints 5
operation(add, subtract, multiply, divide, "subtract")  # prints 2
operation(add, subtract, multiply, divide, "divide")    # prints 5.0
operation(add, subtract, multiply, divide, "multiply")  # prints 12
# "multiplyy" (note the typo, extra 'y') matches none of the if/elif
# branches, so this falls through to the else and prints
# "invalid operation..." instead of calling multiply.
operation(add, subtract, multiply, divide, "multiplyy")
