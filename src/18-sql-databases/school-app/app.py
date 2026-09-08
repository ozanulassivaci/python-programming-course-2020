from dbmanager import DbManager
from Student import Student
import datetime

# This App class is the "UI" layer of a tiny console application: it never
# writes SQL itself, it just asks the user questions with input() and hands
# the real database work off to self.db (a DbManager). This is a common way
# to structure a small program -- keep the "talk to the database" logic
# separate from the "talk to the user" logic, so each part can be understood
# and changed on its own.
class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        # This is where I built my first simple text menu loop in Python
        #
        # A "menu loop" just means: show the same list of options forever,
        # read what the user typed, act on it, and then loop back to show
        # the menu again -- until the user picks the option that breaks out
        # of the loop.
        msg = "*****\n1-Student List\n2-Add Student\n3-Update Student\n4-Delete Student\n5-Add Teacher\n6-Lessons By Class\n7-Exit (E/X)"
        while True:
            print(msg)
            choice = input("Choice: ")
            if choice == '1':
                self.displayStudents()
            elif choice == '2':
                self.addStudent()
            elif choice == '3':
                self.editStudent()
            elif choice == '4':
                self.deleteStudent()
            elif choice == 'E' or choice == 'X':
                # break immediately exits the while loop, ending the
                # program's main menu (there's nothing after this loop to
                # fall through to, so the script simply ends).
                break
            else:
                print('invalid choice')


    def deleteStudent(self):
        # Reuses displayStudents() first so the user can see which class
        # and which student ids exist before typing one in to delete.
        classid = self.displayStudents()
        studentid = int(input('student id: '))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('student id: '))

        student = self.db.getStudentById(studentid)

        # `input(...) or student[0].name` is a common Python idiom for
        # "optional field, keep the old value if left blank": input()
        # returns an empty string '' when the user just presses Enter, and
        # an empty string is "falsy" in Python (it counts as False in a
        # boolean context), so `or` falls through to the value on its right
        # -- the student's existing name -- whenever nothing was typed.
        student[0].name = input('name:') or student[0].name
        student[0].surname = input('surname:') or student[0].surname
        student[0].gender = input('gender (E/K):') or student[0].gender
        student[0].classid = input('class: ') or student[0].classid

        year = input("year: ") or student[0].birthdate.year
        month = input("month: ") or student[0].birthdate.month
        day = input("day: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
        # Hands the modified Student object to DbManager, which builds and
        # runs the actual UPDATE statement.
        self.db.editStudent(student[0])


    def addStudent(self):
        self.displayClasses()

        classid = int(input('which class: '))
        number = input('student number: ')
        name = input('name')
        surname = input('surname')
        year = int(input('year'))
        month = int(input('month'))
        day = int(input('day'))
        birthdate = datetime.date(year,month,day)
        gender = input('gender (E/K)')

        # id=None signals "this student doesn't exist in the database yet";
        # Student's constructor stores a placeholder 0 until the INSERT
        # gives it a real id.
        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def displayClasses(self):
        # Reads every class from the database (via DbManager -> "select *
        # from class") and prints it as "id: name" so the user knows which
        # class id to type in elsewhere.
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):
        self.displayClasses()
        classid = int(input('which class: '))

        # Asks the database for only the students whose classid matches the
        # one the user picked (a WHERE classid = ... query under the hood).
        students = self.db.getStudentsByClassId(classid)
        print("Student List")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        # Returning classid lets callers like deleteStudent()/editStudent()
        # reuse the class the user just picked without asking again.
        return classid




app = App()
app.initApp()
