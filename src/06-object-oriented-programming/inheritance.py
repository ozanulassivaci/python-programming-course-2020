# Inheritance

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

class Person():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        self.student_number = number
        print('Student Created')

    # override
    def who_am_i(self):
        print('I am a student')

    def say_hello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)
        self.branch = branch

    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

# Learned that a subclass can call the parent's __init__ either directly (Person.__init__)
# or through super() - both end up doing the same thing here.
p1 = Person('Ali', 'Yilmaz')
s1 = Student('Kerem', 'Deniz', 1256)
t1 = Teacher('Serkan', 'Yilmaz', 'Math')

t1.who_am_i()

print(p1.first_name + ' ' + p1.last_name)
print(s1.first_name + ' ' + s1.last_name + ' ' + str(s1.student_number))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.say_hello()
