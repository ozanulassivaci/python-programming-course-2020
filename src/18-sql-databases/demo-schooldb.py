# 1- Using Workbench IDE, create a database named schooldb and add the Student table.
    # Id,StudentNumber,Name,Surname,Birthdate,Gender

# 2- Set up the database connection. (connection.py)

# 3- Write insert queries to add the following records.

    # ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    # ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    # ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    # ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    # ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    # ("306","Ali","Cenk",datetime(2003, 8, 25),"E")

"""
*** Inserting a single record
ahmet = Student("202","ahmet","yılmaz",datetime(2005, 5, 17),"E")
ahmet.saveStudent()
"""

"""
*** Inserting multiple records
students = [
    ("301","Ahmet","Yılmaz",datetime(2005, 5, 17),"E"),
    ("302","Ali","Can",datetime(2005, 6, 17),"E"),
    ("303","Canan","Tan",datetime(2005, 7, 7),"K"),
    ("304","Ayşe","Taner",datetime(2005, 9, 23),"K"),
    ("305","Bahadır","Toksöz",datetime(2004, 7, 27),"E"),
    ("306","Ali","Cenk",datetime(2003, 8, 25),"E")
]
Student.saveStudents(students)
"""

# 4- Write the following queries.
#   a- Get all student records.
#   b- Get only student number, name and surname for all students.
#   c- Get name and surname of the female students only.
#   d- Get the students born in 2003.
#   e- Get the student named Ali who was born in 2005.
#   f- Get records where name or surname contains 'an'.
#   g- How many male students are there?
#   h- Get the female students sorted alphabetically.

# 5- Do the following update queries.
#   a- Update a student's info based on their id.
#   b- Update a student's info based on their gender.

import mysql.connector
from datetime import datetime
from connection import connection

class Student:
    connection = connection
    mycursor = connection.cursor()

    def __init__(self, id,studentNumber,name,surname,birthdate,gender):
        if id is None:
            self.id = 0
        else:
            self.id = id
        self.studentNumber = studentNumber
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.gender = gender

    def saveStudent(self):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name, self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} record(s) inserted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} record(s) inserted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            Student.connection.close()

    @staticmethod
    def StudentInfo():
        # This is where I practiced writing different SELECT queries with WHERE, LIKE and ORDER BY
        # sql = "select * from student"
        # sql = "select * from student LIMIT 3"
        # sql = "select studentnumber,name,surname from student"
        # sql = "select name,surname from student where gender='K'"
        # sql = "select * from student where YEAR(birthdate) = 2003"
        # sql = "select * from student where YEAR(birthdate) = 2005 and name = 'Ali'"
        # sql = "select * from student where name like '%an%' or surname like '%an%'"
        # sql = "select COUNT(id) from student where gender='E'"
        # sql = "select name,surname from student where gender='K' order by name,surname"

        Student.mycursor.execute(sql)

        try:
            results = Student.mycursor.fetchall()
            for result in results:
                print(f'{result}')

        except mysql.connector.Error as err:
            print('error', err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            obj = Student.mycursor.fetchone()
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Error', err)

    def updateStudent(self):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} record(s) updated')
        except mysql.connector.Error as err:
            print('Error:',err)

    @staticmethod
    def updateStudents(student_list):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        order = [1,2,3,4,5,0]

        for item in student_list:
            item = [item[i] for i in order]
            values.append(item)

        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} record(s) updated')
        except mysql.connector.Error as err:
            print('Error:',err)

    @staticmethod
    def getStudentsGender(gender):
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err)


# student = Student.getStudentById(8)

# student.name = 'Kerem'
# student.surname = 'Deniz'

# student.updateStudent()


# This is where I learned I could pull a whole filtered group back, tweak it in Python, then push it all back with executemany
students = Student.getStudentsGender('E')
print(students)

updated_students = []
for std in students:
    std = list(std)
    std[2] = 'Mr ' + std[2]
    updated_students.append(std)

Student.updateStudents(updated_students)
