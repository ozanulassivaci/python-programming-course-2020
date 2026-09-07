# # class
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


class Circle:
    # Class object attribute
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    # Methods
    # Learned that a method just reads self.radius / self.pi like any other variable.
    def calculate_circumference(self):
        return 2 * self.pi * self.radius

    def calculate_area(self):
        return self.pi * (self.radius**2)

c1 = Circle()
c2 = Circle(5)

print(f'c1 : area = {c1.calculate_area()} circumference = {c1.calculate_circumference()}')
print(f'c2 : area = {c2.calculate_area()} circumference = {c2.calculate_circumference()}')
