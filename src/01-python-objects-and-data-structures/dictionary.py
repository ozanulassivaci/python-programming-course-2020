# key - value
#
# A dictionary (dict) stores data as key-value pairs instead of ordering
# items by numeric position like a list does. You look things up by their
# key, not by their index.

# 41 => kocaeli 34 => istanbul

# Here's the problem with using two parallel lists to represent this
# relationship: to find a plate number for a city, you first have to
# search the cities list for a matching name, THEN use its position
# (index) to look up the matching plate. That's clunky and slow.

# cities = ['kocaeli','istanbul']
# plates = [41, 34]

# print(plates[cities.index('istanbul')])
# cities.index('istanbul') finds the position of 'istanbul' in the cities
# list (position 1), and then plates[1] reads the value at that same
# position in the OTHER list. Two lookups just to answer one question.

# print(plates['kocaeli']) => 41
# print(plates['istanbul']) => 34
# You can't actually do this with a list -- lists only accept integer
# indices, not string keys. This is exactly the problem a dictionary
# solves.

# plates = { 'kocaeli' : 41, 'istanbul': 34 }
# A dict literal is written with curly braces, and each entry is
# "key: value". Now the city name IS the way you look things up, directly.

# print(plates['kocaeli'])
# print(plates['istanbul'])

# plates['ankara'] = 6
# Assigning to a key that doesn't exist yet ADDS a new key-value pair to
# the dictionary.
# plates['kocaeli'] = 'new value'
# Assigning to a key that already exists OVERWRITES its value. Dictionary
# values can be any type -- mixing a number and a string as values in the
# same dict, like here, is perfectly fine.

# print(plates)

# Learned that a dict key can be any immutable type, so this reads a
# lot like a list indexed by name instead of by position.
# Here the values are themselves dictionaries -- a "dictionary of
# dictionaries" -- which is a very common way to represent a small
# "table" of records, each identified by a unique key (here, a username).
users = {
    'ozanulassivaci': {
        'age': 36,
        'roles': ['user'],
        'email': 'ozan@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    },
    'keremdeniz': {
        'age': 2,
        'roles': ['admin', 'user'],
        'email': 'kerem@gmail.com',
        'address': 'kocaeli',
        'phone': '1231321'
    }
}

# Reading a nested structure works by chaining lookups left to right:
# users['keremdeniz']       -> the inner dict for that user
# users['keremdeniz']['roles']    -> the list ['admin', 'user'] stored
#                                    under the 'roles' key
# users['keremdeniz']['roles'][0] -> the first element of that list,
#                                    which is the string 'admin'
print(users['keremdeniz']['roles'][0])
