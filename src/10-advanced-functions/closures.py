# def greeting(name):
#     print('hello ', name)

# print(greeting('ali'))
# print(greeting)
# In Python, functions are themselves values ("first-class citizens"),
# just like numbers or strings. greeting('ali') CALLS the function
# (running its body and printing 'hello  ali'), and since greeting has
# no return statement, that call itself evaluates to None -- so
# print(greeting('ali')) prints "hello  ali" first, then "None" on the
# next print. print(greeting), with no parentheses, does NOT call the
# function at all; it prints a description of the function object
# itself, something like "<function greeting at 0x...>".

# say_hello = greeting
# del say_hello
# print(say_hello)
# Because functions are values, you can assign one to another name, like
# say_hello = greeting -- now say_hello and greeting both refer to the
# SAME function. "del say_hello" removes just that name binding (the
# underlying function object still exists and is still reachable as
# `greeting`). Afterwards, print(say_hello) would raise a NameError,
# since the name "say_hello" no longer exists.

# encapsulation
# def outer(num1):
#     print('outer')
#     def inner_increment(num1):
#         print('inner')
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1, num2)
# A function defined INSIDE another function (a "nested function") is
# only visible/callable from within that enclosing function -- this is a
# form of encapsulation, hiding an implementation detail that callers of
# `outer` don't need to know about. Calling outer(10) would print
# 'outer', then call inner_increment(10) which prints 'inner' and
# returns 11, then print '10 11' (num1 stays 10, num2 becomes 11).

# outer(10)
# inner_increment(10)
# outer(10) works fine. inner_increment(10) on its own would raise a
# NameError, because inner_increment only exists inside outer's local
# scope -- it was never defined at the top level of this file.


# Learned that a nested function can only be called from inside its
# enclosing function - inner_factorial isn't visible outside factorial().
# factorial(number) computes number! (number factorial) using a nested
# helper function, after first validating the input.
def factorial(number):
    # isinstance(value, type) checks whether `value` is (or is built
    # from) the given type, returning True/False. This guards against
    # being handed something that isn't a whole number at all, like a
    # string or a float.
    if not isinstance(number, int):
        raise TypeError("number must be an integer")

    if not number >= 0:
        raise ValueError("number must be zero or positive")

    # inner_factorial is defined fresh every time factorial() runs, and
    # only exists inside this call. It computes the factorial
    # RECURSIVELY: a recursive function is one that calls itself, each
    # time working on a smaller version of the same problem, until it
    # reaches a "base case" that can be answered directly without
    # calling itself again.
    def inner_factorial(number):
        # Base case: 0! and 1! are both defined as 1, so once we count
        # down to number <= 1, we stop recursing and just return 1
        # directly -- this is what eventually stops the recursion from
        # going forever.
        if number <= 1:
            return 1

        # Recursive case: number! = number * (number-1)!. Each call
        # waits for the call it makes to itself to finish before it can
        # multiply and return its own result, so the calls "stack up"
        # (4 waits on 3, which waits on 2, which waits on 1) and then
        # unwind back up once the base case is hit.
        return number * inner_factorial(number - 1)

    return inner_factorial(number)

try:
    # "4" is a string, not an int, so isinstance(number, int) is False,
    # meaning "not isinstance(number, int)" is True, and the TypeError
    # is raised immediately -- inner_factorial never even gets defined
    # or called for this particular input.
    print(factorial("4"))
except Exception as ex:
    # Catching the broad "Exception" here means this would catch either
    # the TypeError or the ValueError that factorial() might raise.
    # Printing `ex` shows the message that was passed to raise
    # TypeError(...): "number must be an integer".
    print(ex)
