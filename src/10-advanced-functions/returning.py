# def power_of(number):
#     def inner(power):
#         return number ** power
#
#     return inner

# two = power_of(2) # 2-3
# three = power_of(3) # 3-4

# print(two(3))
# print(three(4))

# def check_role(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} role can access {1} page.".format(role,page)
#         else:
#             return "{0} role cannot access {1} page.".format(role,page)
#     return inner

# user1 = check_role("Product Edit")
# print(user1("Admin"))
# print(user1("User"))


# Learned that a function can return a different inner function depending
# on its argument - that's how "operation" picks between sum and product.
def operation(operation_name):
    def total(*args):
        result = 0
        for i in args:
            result += i
        return result

    def product(*args):
        result = 1
        for i in args:
            result *= i
        return result

    if operation_name == "add":
        return total
    else:
        return product


add = operation("add")
print(add(1, 3, 5, 6, 7))

multiply = operation("multiply")
print(multiply(1, 2, 3, 6, 4))
