from dbmanager import DbManager
from Student import Student
import datetime

class App:
    def __init__(self):
        self.db = DbManager()

    def initApp(self):
        # This is where I built my first simple text menu loop in Python
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
                break
            else:
                print('invalid choice')


    def deleteStudent(self):
        classid = self.displayStudents()
        studentid = int(input('student id: '))

        self.db.deleteStudent(studentid)

    def editStudent(self):
        classid = self.displayStudents()
        studentid = int(input('student id: '))

        student = self.db.getStudentById(studentid)

        student[0].name = input('name:') or student[0].name
        student[0].surname = input('surname:') or student[0].surname
        student[0].gender = input('gender (E/K):') or student[0].gender
        student[0].classid = input('class: ') or student[0].classid

        year = input("year: ") or student[0].birthdate.year
        month = input("month: ") or student[0].birthdate.month
        day = input("day: ") or student[0].birthdate.day

        student[0].birthdate = datetime.date(year,month,day)
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

        student = Student(None,number,name,surname,birthdate,gender,classid)
        self.db.addStudent(student)

    def displayClasses(self):
        classes = self.db.getClasses()
        for c in classes:
            print(f'{c.id}: {c.name}')

    def displayStudents(self):
        self.displayClasses()
        classid = int(input('which class: '))

        students = self.db.getStudentsByClassId(classid)
        print("Student List")
        for std in students:
            print(f'{std.id}-{std.name} {std.surname}')

        return classid




app = App()
app.initApp()
