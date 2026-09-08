# def power_of(number):
#     def inner(power):
#         return number ** power
#
#     return inner
# A function can RETURN another function instead of returning a plain
# value. Here, calling power_of(2) does not compute anything numeric
# itself -- it defines `inner` (which remembers `number` = 2, even after
# power_of has already finished running) and returns that function
# object. This "remembering" of variables from an enclosing function
# even after that function has returned is called a CLOSURE: `inner`
# stays connected ("closed over") to the `number` variable from its
# birthplace, power_of's local scope.

# two = power_of(2) # 2-3
# three = power_of(3) # 3-4
# `two` is now the `inner` function with `number` permanently fixed at
# 2; `three` is a completely separate `inner` function with `number`
# fixed at 3.

# print(two(3))
# print(three(4))
# two(3) computes 2 ** 3 = 8. three(4) computes 3 ** 4 = 81. Even though
# both came from the exact same `inner` function definition, each
# remembers its OWN `number` from when it was created -- that's the
# power of closures: multiple independent functions built from the same
# template, each with their own private memory.

# def check_role(page):
#     def inner(role):
#         if role == 'Admin':
#             return "{0} role can access {1} page.".format(role,page)
#         else:
#             return "{0} role cannot access {1} page.".format(role,page)
#     return inner
# str.format(...) is another way to build strings with placeholders:
# "{0}" and "{1}" get replaced by the first and second arguments passed
# to .format(), in order (equivalent in spirit to an f-string like
# f"{role} role can access {page} page."). check_role(page) closes over
# `page`, just like power_of closed over `number` above.

# user1 = check_role("Product Edit")
# print(user1("Admin"))
# print(user1("User"))
# user1 is `inner` with page fixed at "Product Edit". user1("Admin")
# returns "Admin role can access Product Edit page.". user1("User")
# returns "User role cannot access Product Edit page." -- same closed-
# over `page`, different `role` argument each time changes the outcome.


# Learned that a function can return a different inner function depending
# on its argument - that's how "operation" picks between sum and product.
# Unlike power_of/check_role above (which always return the same single
# inner function), `operation` defines TWO different inner functions and
# decides, based on its argument, WHICH one to hand back -- this is a
# simple version of what's often called a "factory function": a function
# whose job is to build and return another function.
def operation(operation_name):
    # *args collects any number of positional arguments passed to
    # total() into a tuple, e.g. total(1,3,5,6,7) makes args == (1,3,5,6,7).
    # This lets `total` accept any number of numbers to add up, not just
    # a fixed count.
    def total(*args):
        result = 0
        # Looping over the tuple and adding each value to `result` in
        # turn computes the sum of all of them.
        for i in args:
            result += i
        return result

    def product(*args):
        # Starting at 1 (not 0) matters here: 0 multiplied by anything
        # is always 0, so the running product has to start at the
        # multiplicative identity, 1, instead.
        result = 1
        for i in args:
            result *= i
        return result

    # Notice `operation` returns the FUNCTION ITSELF (total or product),
    # not the result of calling it -- there are no parentheses after
    # `total`/`product` here. The actual numbers to compute with aren't
    # known yet at this point; they'll be supplied later, when the
    # returned function is finally called.
    if operation_name == "add":
        return total
    else:
        return product


# add now refers to the `total` function returned by operation("add").
add = operation("add")
# Calling it with five numbers sums them: 1+3+5+6+7 = 22.
print(add(1, 3, 5, 6, 7))

# multiply now refers to the `product` function returned by
# operation("multiply") (any name other than "add" falls into the
# else branch, so "multiply" works here even though it isn't checked
# for explicitly).
multiply = operation("multiply")
# Calling it with five numbers multiplies them all together:
# 1*2*3*6*4 = 144.
print(multiply(1, 2, 3, 6, 4))
