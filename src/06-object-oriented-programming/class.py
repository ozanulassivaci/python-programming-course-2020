# Object Oriented Programming (OOP) lets you bundle related data and the
# functions that work on that data into a single blueprint, called a
# "class". Once you have a class, you can stamp out as many independent
# "objects" (also called "instances") from it as you like.

# class
# A class is defined with the "class" keyword followed by a name (by
# convention written in CapitalizedWords, e.g. "Person"). Everything
# indented under it belongs to the class: its attributes (data) and its
# methods (functions that belong to the class).
class Person:
    # class attributes
    # A class attribute is defined directly inside the class body, not
    # inside a method. It is shared by ALL instances of the class unless
    # an individual instance overrides it with its own attribute of the
    # same name (which is exactly what happens to p1.address below).
    address = 'no information'

    # constructor method
    # __init__ is a "dunder" (double underscore) method: Python
    # automatically calls it every time you create a new object from this
    # class, e.g. when you write Person(name='ali', year=1990). Its job is
    # to set up ("initialize") the brand-new object with starting values.
    # "self" is the first parameter of every regular method and always
    # refers to the specific object the method was called on -- Python
    # passes it in automatically, you never supply it yourself when
    # calling the method.
    def __init__(self, name, year):
        # object attributes
        # Writing to self.<name> stores the value ON THIS PARTICULAR
        # OBJECT. Unlike the class attribute above, each instance gets
        # its own independent copy of name/year -- changing one object's
        # name does not affect any other object.
        self.name = name
        self.year = year
        print('init method ran.')

        # methods
        # (Person defines no other methods here besides __init__.)


# object (instance)
# Calling the class like a function -- Person(...) -- creates a new
# object and runs __init__ on it. p1 and p2 are two separate objects,
# each with their own name/year, even though they came from the same
# class. That's why "init method ran." is printed twice below: once for
# each object that gets constructed.
# Learned that each instance gets its own copy of the object attributes.
p1 = Person(name='ali', year=1990)
p2 = Person(name='yagmur', year=1995)

# updating
# Attributes can be reassigned after creation just like any variable.
p1.name = 'ahmet'
# p1 didn't have its own "address" attribute yet (it was only using the
# shared class attribute 'no information'). Assigning to p1.address here
# creates a NEW instance attribute on p1 specifically. This does not
# touch the class attribute, so p2.address (and Person.address) are
# still 'no information' afterwards.
p1.address = 'kocaeli'

# accessing object attributes
# Python looks up p1.address by first checking if p1 itself has an
# "address" attribute; if not, it falls back to the class. p1 now has
# its own, so it prints 'kocaeli'. p2 has none of its own, so Python
# falls back to the class attribute and prints 'no information'.
print(f'p1 :name: {p1.name} year: {p1.year} address: {p1.address}')
print(f'p2 :name: {p2.name} year: {p2.year} address: {p2.address}')

# print(p1) calls str(p1) under the hood. Because Person does not define
# a __str__ method (see specials.py in this same folder for what that
# would look like), Python falls back to its default object
# representation, which looks something like
# "<__main__.Person object at 0x000001A2B3C4D5E6>" -- a fairly useless
# string containing the class name and the object's memory address.
print(p1)
print(p2)

# type() returns the class that an object was built from. For both p1
# and p2 this prints "<class '__main__.Person'>", since both were built
# from the Person class defined above ("__main__" just means "this
# script").
print(type(p1))
print(type(p2))

# Using == on two objects compares them with Person's __eq__ method.
# Because Person doesn't define a custom __eq__, Python falls back to
# the default behavior: two objects are only equal if they are literally
# the SAME object in memory (identity comparison, like "is"). p1 and p2
# are two distinct objects, so this prints False even though nothing
# here compares their name/year values.
print(p1 == p2)
