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
def operation(f1, f2, f3, f4, operation_name):
    if operation_name == "add":
        print(f1(2, 3))
    elif operation_name == "subtract":
        print(f2(5, 3))
    elif operation_name == "multiply":
        print(f3(3, 4))
    elif operation_name == "divide":
        print(f4(10, 2))
    else:
        print("invalid operation...")

operation(add, subtract, multiply, divide, "add")
operation(add, subtract, multiply, divide, "subtract")
operation(add, subtract, multiply, divide, "divide")
operation(add, subtract, multiply, divide, "multiply")
operation(add, subtract, multiply, divide, "multiplyy")
