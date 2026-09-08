# def my_decorator(func):
#     def wrapper(name):
#         print("stuff to do before the function")
#         func(name)
#         print("stuff to do after the function")
#     return wrapper

# @my_decorator
# def say_hello(name):
#     print("hello", name)

# say_hello("ali")
# A DECORATOR is a function that takes another function as its input and
# returns a new function that usually calls the original one plus adds
# extra behavior around it. Writing "@my_decorator" directly above a
# function definition is special Python syntax ("syntactic sugar") that
# means "after defining say_hello, immediately replace it with
# my_decorator(say_hello)". So after this, the name `say_hello` no
# longer points at the original function -- it points at `wrapper`
# instead. Calling say_hello("ali") therefore actually calls wrapper("ali"),
# which prints "stuff to do before the function", then calls the
# ORIGINAL say_hello("ali") (captured as `func` inside wrapper) which
# prints "hello ali", and finally prints "stuff to do after the
# function".
import math
import time

# Learned that a decorator is just a function that takes a function and
# returns a wrapped version of it - @calculate_time is sugar for
# usalma = calculate_time(usalma).
# calculate_time is a decorator that measures and reports how long the
# decorated function takes to run.
def calculate_time(func):
    # *args and **kwargs let `inner` accept ANY combination of
    # positional and keyword arguments, and simply forward them along to
    # `func`, whatever `func` happens to need. *args collects any number
    # of positional arguments into a tuple (e.g. calling inner(2, 3)
    # makes args == (2, 3)); **kwargs collects any keyword arguments into
    # a dictionary. This makes calculate_time reusable on functions with
    # completely different parameter lists, like power(a, b),
    # factorial(num), and addition(a, b) below.
    def inner(*args, **kwargs):
        # time.time() returns the current time as a number of seconds
        # since a fixed reference point (the "epoch") -- on its own it's
        # not very meaningful, but the DIFFERENCE between two calls to
        # it tells you how much time elapsed between them.
        start = time.time()
        # An artificial 1-second delay, added here just so the measured
        # duration is long enough to clearly show up as roughly 1 second
        # rather than a near-zero number.
        time.sleep(1)
        # Actually calling the original function with whatever arguments
        # were passed in. Its own return value is discarded here (not
        # captured or returned by `inner`), only its side effects (the
        # print() calls inside power/factorial/addition) are visible.
        func(*args, **kwargs)
        finish = time.time()
        # func.__name__ is a built-in attribute every function object
        # has, giving you its name as a string -- useful for generic
        # logging code like this that doesn't know in advance which
        # function it's wrapping.
        print("function " + func.__name__ + " took " + str(finish-start) + " seconds.")
    return inner

# Equivalent to: power = calculate_time(power). Every call to power(...)
# from here on actually calls calculate_time's `inner`, which calls the
# real power function inside it and reports the timing.
@calculate_time
def power(a, b):
    # math.pow(a, b) returns a raised to the power b, as a float.
    print(math.pow(a, b))

@calculate_time
def factorial(num):
    # math.factorial(num) returns num! (see closures.py in this same
    # folder for a hand-written version of this same calculation).
    print(math.factorial(num))

@calculate_time
def addition(a, b):
    print(a+b)

# power(2, 3): prints 8.0 (2 raised to the power 3), then prints a
# timing message showing roughly 1 second elapsed (because of the
# time.sleep(1) inside `inner`).
power(2, 3)
# factorial(4): prints 24 (4! = 4*3*2*1), plus its own timing message.
factorial(4)
# addition(10, 20): prints 30, plus its own timing message.
addition(10, 20)
