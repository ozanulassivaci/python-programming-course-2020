# Object Oriented Programming (OOP)
# OOP is a way of organizing code around "objects" -- bundles of data
# (attributes) and behavior (methods) -- instead of just a flat sequence
# of variables and functions. Everything you work with in Python,
# including the built-in types like lists, strings, and numbers, is
# actually an object of some class.

# class => Person (name, surname, birthday, calculate_age())
# instance (object)

# Learned that even built-in things like lists are objects with a type.
# lst1 and lst2 are both created from Python's built-in "list" class.
# Different lists can have different lengths/contents, but they still
# both belong to the same underlying class.
lst1 = [1, 2, 3]
lst2 = [1, 2, 3, 4]


# type() is a built-in function that returns the class an object was
# built from. Since both lst1 and lst2 are ordinary Python lists, both
# calls return the exact same thing: <class 'list'>.
result = type(lst1)
result = type(lst2)

# Only the second assignment to `result` (type(lst2)) actually survives,
# since the first one gets overwritten before it's ever printed. Either
# way, the printed value is <class 'list'>, because both lst1 and lst2
# share the same type regardless of how many elements they contain.
print(result)
