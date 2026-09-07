"""
x = input('1st number: ')
y = input('2nd number: ')

print(type(x))
print(type(y))

total = int(x) + int(y)

print(total)
"""

x = 5               # int
y = 2.5              # float
name = 'Kerem'       # str
is_online = True     # bool

# print(type(x))
# print(type(y))
# print(type(name))
# print(type(is_online))

# Type Conversion

# int to float

# x = float(x)
# print(x)
# print(type(x))

# float to int

# y = int(y)
# print(y)
# print(type(y))

# result = str(x) + str(y)
# print(result)
# print(type(result))

# bool to str

# is_online = str(is_online)
# print(is_online)
# print(type(is_online))

# bool to int
# Learned that True/False convert to 1/0 when cast to int

is_online = False

is_online = int(is_online)
print(is_online)
print(type(is_online))
