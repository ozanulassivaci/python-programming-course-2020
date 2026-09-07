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
import math
import time

# Learned that a decorator is just a function that takes a function and
# returns a wrapped version of it - @calculate_time is sugar for
# usalma = calculate_time(usalma).
def calculate_time(func):
    def inner(*args, **kwargs):
        start = time.time()
        time.sleep(1)
        func(*args, **kwargs)
        finish = time.time()
        print("function " + func.__name__ + " took " + str(finish-start) + " seconds.")
    return inner

@calculate_time
def power(a, b):
    print(math.pow(a, b))

@calculate_time
def factorial(num):
    print(math.factorial(num))

@calculate_time
def addition(a, b):
    print(a+b)

power(2, 3)
factorial(4)
addition(10, 20)
