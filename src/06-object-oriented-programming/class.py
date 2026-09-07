# class
class Person:
    # class attributes
    address = 'no information'

    # constructor method
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.year = year
        print('init method ran.')

        # methods


# object (instance)
# Learned that each instance gets its own copy of the object attributes.
p1 = Person(name='ali', year=1990)
p2 = Person(name='yagmur', year=1995)

# updating
p1.name = 'ahmet'
p1.address = 'kocaeli'

# accessing object attributes
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')

print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)
