# def change_name(n):
#     n = 'ada'

# name = 'yigit'

# change_name(name)
# print(name)

# def change(n):
#     n[0] = 'istanbul'

# cities = ['ankara','izmir']

# change(cities[:])

# print(cities)

def add(*params):
    print(type(params))
    # Renamed this from `sum` to avoid shadowing the built-in sum() function
    total = 0
    for n in params:
        total = total + n
    return total

print(add(10, 20, 50))
print(add(10, 20, 30))
print(add(10, 20, 30, 50, 60, 10, 20))

def display_user(**args):
    print(type(args))
    for key, value in args.items():
        print('{} is {}'.format(key, value))

display_user(name='Kerem', age=2, city='istanbul')
display_user(name='Ada', age=12, city='kocaeli', phone='123132')
display_user(name='Yigit', age=14, city='ankara', phone='123132', email='yigit@gmail.com')

def my_func(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

my_func(10, 20, 30, 40, 50, 60, 70, key1='value 1', key2='value 2')
