# key - value

# 41 => kocaeli 34 => istanbul

# cities = ['kocaeli','istanbul']
# plates = [41, 34]

# print(plates[cities.index('istanbul')])

# print(plates['kocaeli']) => 41
# print(plates['istanbul']) => 34

# plates = { 'kocaeli' : 41, 'istanbul': 34 }

# print(plates['kocaeli'])
# print(plates['istanbul'])

# plates['ankara'] = 6
# plates['kocaeli'] = 'new value'

# print(plates)

# Learned that a dict key can be any immutable type, so this reads a
# lot like a list indexed by name instead of by position.
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

print(users['keremdeniz']['roles'][0])
