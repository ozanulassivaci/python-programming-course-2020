# def change_name(n):
#     n = 'ada'

# name = 'yigit'

# change_name(name)
# print(name)
# Would still print 'yigit'. Passing `name` into the function copies the
# REFERENCE into the parameter `n`, but reassigning `n = 'ada'` only
# repoints the LOCAL name `n` at a new string -- it has no way to reach
# back and change what the caller's `name` variable points to. This is
# true for any reassignment, regardless of whether the value is mutable
# or not.

# def change(n):
#     n[0] = 'istanbul'

# cities = ['ankara','izmir']

# change(cities[:])
# cities[:] is a full slice, which makes a SHALLOW COPY of the list
# before passing it in -- so `change` mutates that copy's contents, not
# the original `cities` list. That's why, even though list mutation
# normally IS visible outside a function (mutating a list in place
# affects every name pointing at that same list), passing a copy here
# means the original `cities` is left untouched.

# print(cities)
# Would still print ['ankara', 'izmir'] -- unchanged, thanks to the copy.

# *params collects any number of positional arguments into a tuple named
# `params` inside the function -- this is how you write a function that
# accepts a variable, unknown-in-advance number of arguments.
def add(*params):
    print(type(params))  # <class 'tuple'>
    # Renamed this from `sum` to avoid shadowing the built-in sum() function
    total = 0
    for n in params:
        total = total + n
    return total

print(add(10, 20, 50))              # 80
print(add(10, 20, 30))              # 60
print(add(10, 20, 30, 50, 60, 10, 20))  # 200

# **args collects any number of KEYWORD arguments into a dict named
# `args` inside the function -- the argument names the caller uses become
# the dict's keys, and the values they pass become the dict's values.
def display_user(**args):
    print(type(args))  # <class 'dict'>
    for key, value in args.items():
        print('{} is {}'.format(key, value))

display_user(name='Kerem', age=2, city='istanbul')
display_user(name='Ada', age=12, city='kocaeli', phone='123132')
display_user(name='Yigit', age=14, city='ankara', phone='123132', email='yigit@gmail.com')

# A function can combine regular (positional) parameters, *args, and
# **kwargs all together, but they must appear in this order: normal
# parameters first, then *args (extra positional arguments), then
# **kwargs (extra keyword arguments). This lets a single function accept
# a fixed "required" shape of arguments PLUS any number of additional
# ones of either kind.
def my_func(a, b, c, *args, **kwargs):
    print(a)      # the 1st positional argument (10)
    print(b)      # the 2nd positional argument (20)
    print(c)      # the 3rd positional argument (30)
    print(args)   # every extra positional argument, as a tuple: (40, 50, 60, 70)
    print(kwargs)  # every keyword argument, as a dict: {'key1': 'value 1', 'key2': 'value 2'}

my_func(10, 20, 30, 40, 50, 60, 70, key1='value 1', key2='value 2')
