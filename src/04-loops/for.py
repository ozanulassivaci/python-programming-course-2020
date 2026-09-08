numbers = [1, 2, 3, 4, 5]

# "for a in numbers:" runs the indented block once for every item in
# numbers, binding `a` to each item in turn. Since the body here doesn't
# actually use `a`, this just prints 'Hello' exactly 5 times -- once per
# element in the list, regardless of what the elements' values are.
for a in numbers:
    print('Hello')

names = ['kerem', 'ozan', 'sena']

# Here the loop variable IS used inside the f-string on each pass.
for name in names:
    print(f'my name is {name}')

name = 'Ozan Ulas Sivaci'

# Strings are iterable too -- looping over one visits it one CHARACTER
# at a time (including spaces), in order.
for n in name:
    print(n)

# Careful: naming this `tuple` shadows the built-in tuple type
tuple = [(1, 2), (1, 3), (3, 5), (5, 7)]

# When each item in the sequence being looped over is itself a 2-item
# tuple, you can unpack it directly in the for-loop header: `a, b` grabs
# the 1st and 2nd values of each tuple automatically, no manual indexing
# needed. This is the exact same unpacking idea as `x, y = (1, 2)`,
# just applied automatically on every loop iteration.
for a, b in tuple:
    print(a, b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

# Looping directly over a dict (`for key in d:`) only gives you the keys.
# .items() instead gives you (key, value) pairs, one per entry, which we
# unpack into two loop variables just like the tuple example above.
for key, value in d.items():
    print(key, value)
