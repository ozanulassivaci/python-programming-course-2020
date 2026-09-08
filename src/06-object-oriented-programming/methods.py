# # class
# # This commented-out block is an earlier example kept for reference. It
# # shows a Person class with two INSTANCE METHODS: intro() and
# # calculate_age(). An instance method is just a function defined inside
# # a class that takes "self" as its first parameter, which lets it read
# # and use the specific object's own attributes (self.name, self.year).
# # If this code were run, p1.intro() would print
# # "Hello There. I am ali" and p1.calculate_age() would return
# # 2019 - 1990 = 29 (a hard-coded reference year of 2019 minus the
# # object's stored birth year).
# class Person:
#     # class attributes
#     address = 'no information'

#     # constructor method
#     def __init__(self, name, year):

#         # object attributes
#         self.name = name
#         self.year = year

#     # instance methods
#     def intro(self):
#         print('Hello There. I am ' + self.name)

#     # instance methods
#     def calculate_age(self):
#         return 2019 - self.year


# # object (instance)
# p1 = Person(name='ali', year=1990)
# p2 = Person(name='yagmur', year=1995)

# p1.intro()
# p2.intro()

# print(f'my name: {p1.name} and my age: {p1.calculate_age()}')
# print(f'my name: {p2.name} and my age: {p2.calculate_age()}')


# Circle models a circle by its radius, and provides methods that
# compute values derived from that radius (its area and circumference).
class Circle:
    # Class object attribute
    # pi is defined at the class level (not inside __init__), so it's
    # shared by every Circle instance. All Circle objects use the exact
    # same value 3.14 for pi unless a specific instance is given its own
    # override.
    pi = 3.14

    # radius=1 gives the "radius" parameter a DEFAULT VALUE. If you call
    # Circle() with no arguments at all, radius will automatically be 1
    # instead of raising a "missing argument" error. If you do pass a
    # value, like Circle(5), that value is used instead of the default.
    def __init__(self, radius=1):
        self.radius = radius

    # Methods
    # Learned that a method just reads self.radius / self.pi like any other variable.
    # Circumference of a circle = 2 * pi * radius. self.pi looks up the
    # class attribute (3.14, since no instance overrides it), and
    # self.radius looks up the value stored on this particular object.
    def calculate_circumference(self):
        return 2 * self.pi * self.radius

    # Area of a circle = pi * radius^2. The ** operator raises a number
    # to a power, so self.radius**2 means "self.radius squared".
    def calculate_area(self):
        return self.pi * (self.radius**2)

# c1 uses the default radius of 1 (no argument passed to Circle()).
c1 = Circle()
# c2 explicitly overrides the default, using a radius of 5.
c2 = Circle(5)

# For c1 (radius=1): area = 3.14 * 1**2 = 3.14,
# circumference = 2 * 3.14 * 1 = 6.28.
print(f'c1 : area = {c1.calculate_area()} circumference = {c1.calculate_circumference()}')
# For c2 (radius=5): area = 3.14 * 5**2 = 3.14 * 25 = 78.5,
# circumference = 2 * 3.14 * 5 = 31.4.
print(f'c2 : area = {c2.calculate_area()} circumference = {c2.calculate_circumference()}')
