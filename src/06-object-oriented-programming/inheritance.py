# Inheritance
# Inheritance lets one class (the "subclass" or "child class") reuse and
# extend everything defined in another class (the "superclass" or
# "parent class"), instead of copy-pasting the same code. It models an
# "is-a" relationship: a Student IS A Person (plus some extra bits that
# make it specifically a student), and so is a Teacher.

# Person => name, lastname, age, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal => Dog(Animal), Cat(Animal)

# Person is the parent class here. It has nothing special about
# inheritance yet -- it's just a normal class with a constructor and two
# regular methods.
class Person():
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname
        print('Person Created')

    def who_am_i(self):
        print('I am a person')

    def eat(self):
        print('I am eating')

# Writing "class Student(Person):" means Student INHERITS from Person:
# every attribute and method Person has, Student automatically gets too
# (eat(), who_am_i(), the first_name/last_name pattern), without
# rewriting any of that code here.
class Student(Person):
    def __init__(self, fname, lname, number):
        # Because Student defines its OWN __init__, Python will use this
        # one instead of Person's when you create a Student -- Person's
        # __init__ is NOT called automatically just because Student
        # inherits from it. So we call it explicitly here, passing "self"
        # by hand, to reuse Person's logic for setting first_name/
        # last_name instead of duplicating those two lines.
        Person.__init__(self, fname, lname)
        # Then we add the extra piece of data that only a Student has.
        self.student_number = number
        print('Student Created')

    # override
    # Defining a method with the same name as one already in the parent
    # class REPLACES it for this subclass -- this is called "overriding".
    # Any Student object will now use this version of who_am_i(), not
    # Person's.
    def who_am_i(self):
        print('I am a student')

    # A new method that only Student objects have; Person and Teacher
    # objects cannot call say_hello().
    def say_hello(self):
        print('Hello I am a student')

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        # super() is another way to reach the parent class, and it's
        # generally the preferred style over calling Person.__init__
        # directly (as Student does above) because it doesn't hard-code
        # the parent class's name -- handy if the class hierarchy changes
        # later. super().__init__(fname, lname) does the exact same thing
        # here as Person.__init__(self, fname, lname) would, except you
        # don't pass "self" yourself; super() already knows which object
        # it's operating on.
        super().__init__(fname, lname)
        self.branch = branch

    # Teacher also overrides who_am_i(), but this version uses the
    # branch attribute that's specific to Teacher objects.
    def who_am_i(self):
        print(f'I am a {self.branch} teacher')

# Learned that a subclass can call the parent's __init__ either directly (Person.__init__)
# or through super() - both end up doing the same thing here.
# Creating each object runs its class's __init__, which prints a message
# along the way. Watch the order these prints appear in when you run the
# file: 'Person Created' for p1, then 'Person Created' followed by
# 'Student Created' for s1 (because Student.__init__ calls Person's
# logic first via Person.__init__, then does its own extra work), then
# just 'Person Created' for t1 (Teacher has no extra print of its own).
p1 = Person('Ali', 'Yilmaz')
s1 = Student('Kerem', 'Deniz', 1256)
t1 = Teacher('Serkan', 'Yilmaz', 'Math')

# t1 is a Teacher, so this calls Teacher's overridden who_am_i(), which
# reads t1.branch ('Math') and prints "I am a Math teacher".
t1.who_am_i()

print(p1.first_name + ' ' + p1.last_name)
print(s1.first_name + ' ' + s1.last_name + ' ' + str(s1.student_number))

# p1 is a plain Person, so it uses Person.who_am_i() and prints
# "I am a person".
p1.who_am_i()
# s1 is a Student; Student overrides who_am_i(), so this prints
# "I am a student" instead of falling back to Person's version.
s1.who_am_i()
# eat() is NOT overridden anywhere, so both p1 and s1 fall back to the
# same inherited Person.eat() method and both print "I am eating".
p1.eat()
s1.eat()
# say_hello() only exists on Student, not on Person or Teacher -- calling
# p1.say_hello() or t1.say_hello() would raise an AttributeError.
s1.say_hello()
