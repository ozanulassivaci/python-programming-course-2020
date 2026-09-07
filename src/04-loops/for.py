numbers = [1, 2, 3, 4, 5]

for a in numbers:
    print('Hello')

names = ['kerem', 'ozan', 'sena']

for name in names:
    print(f'my name is {name}')

name = 'Ozan Ulas Sivaci'

for n in name:
    print(n)

# Careful: naming this `tuple` shadows the built-in tuple type
tuple = [(1, 2), (1, 3), (3, 5), (5, 7)]

for a, b in tuple:
    print(a, b)

d = {'k1': 1, 'k2': 2, 'k3': 3}

for key, value in d.items():
    print(key, value)
