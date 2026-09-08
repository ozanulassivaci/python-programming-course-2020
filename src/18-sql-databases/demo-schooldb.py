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
# Reuse the single `connection` object created in connection.py, instead of
# each class/function opening its own separate connection to the server.
from connection import connection

class Student:
    # These two lines are CLASS attributes (defined directly under the class
    # body, not inside __init__), so they belong to the Student class itself
    # rather than to any one instance. Every Student object -- and every
    # @staticmethod below -- shares this same `connection` and `mycursor`,
    # which is why the rest of the class can just write "Student.mycursor"
    # to reach the one cursor everyone uses.
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
        # A parameterized INSERT: the five %s placeholders are filled in
        # from `value` by the driver rather than being pasted into the SQL
        # text by hand. That's what protects this against SQL injection --
        # even if self.name contained SQL-looking characters, the driver
        # always treats it as plain data, never as part of the command.
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        value = (self.studentNumber,self.name, self.surname,self.birthdate,self.gender)
        Student.mycursor.execute(sql,value)

        try:
            # The row isn't actually saved to the table until commit() runs.
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} record(s) inserted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            Student.connection.close()

    @staticmethod
    def saveStudents(students):
        # `students` is expected to be a list of tuples, each shaped like
        # (studentNumber, name, surname, birthdate, gender) -- the same
        # column order the INSERT statement below expects.
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender) VALUES (%s,%s,%s,%s,%s)"
        values = students
        # executemany() runs that INSERT once per tuple in `values`, adding
        # every student in the list with a single call instead of looping
        # execute() ourselves.
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            # rowcount is the total number of rows inserted across the
            # whole batch, not just one.
            print(f'{Student.mycursor.rowcount} record(s) inserted.')
        except mysql.connector.Error as err:
            print('error:', err)
        finally:
            Student.connection.close()

    @staticmethod
    def StudentInfo():
        # This is where I practiced writing different SELECT queries with WHERE, LIKE and ORDER BY
        #
        # Only one of the lines below is ever actually assigned to `sql` at
        # a time (the rest stay commented out); they're kept here together
        # to show the different flavors of SELECT explored while learning.
        # sql = "select * from student"
        #
        # LIMIT caps how many rows come back, regardless of how many rows
        # actually match -- useful for previewing a big table without
        # pulling every row.
        # sql = "select * from student LIMIT 3"
        #
        # Naming specific columns after SELECT (instead of using *) returns
        # only those columns for every row.
        # sql = "select studentnumber,name,surname from student"
        #
        # WHERE gender='K' filters to just the rows where the gender column
        # equals 'K' (in this dataset, 'K' = female / "Kadın" and
        # 'E' = male / "Erkek").
        # sql = "select name,surname from student where gender='K'"
        #
        # YEAR(birthdate) is a MySQL date function that extracts just the
        # year part out of a full date column, so this WHERE clause matches
        # every student whose birthdate falls anywhere in 2003 -- it doesn't
        # matter what month or day.
        # sql = "select * from student where YEAR(birthdate) = 2003"
        #
        # Combining two conditions with AND means BOTH must be true for a
        # row to be included: born in 2005 AND named 'Ali'.
        # sql = "select * from student where YEAR(birthdate) = 2005 and name = 'Ali'"
        #
        # LIKE does pattern matching on text instead of an exact match.
        # '%an%' means "any characters, then 'an', then any characters" --
        # i.e. the column contains 'an' anywhere in it (like "Ahmet" does
        # not, but "Canan" or "Taner" would). Combining the two LIKE checks
        # with OR means a row matches if EITHER the name OR the surname
        # contains 'an' (only one of the two needs to be true).
        # sql = "select * from student where name like '%an%' or surname like '%an%'"
        #
        # COUNT(id) is an aggregate function: instead of returning one row
        # per matching student, it collapses all the matching rows down
        # into a single number -- here, how many rows have gender='E'.
        # sql = "select COUNT(id) from student where gender='E'"
        #
        # ORDER BY name,surname sorts the results alphabetically by name
        # first, using surname only to break ties between students who
        # share the same name. This runs only on the students already
        # filtered by WHERE gender='K'.
        # sql = "select name,surname from student where gender='K' order by name,surname"

        Student.mycursor.execute(sql)

        try:
            # fetchall() gets every row the query produced, as a list of
            # tuples, so this loop prints one line per matching student.
            results = Student.mycursor.fetchall()
            for result in results:
                print(f'{result}')

        except mysql.connector.Error as err:
            print('error', err)
        finally:
            Student.connection.close()

    @staticmethod
    def getStudentById(id):
        # WHERE id=%s narrows the SELECT down to (at most) the one row
        # whose id matches; the %s placeholder keeps the value safely out of
        # the raw SQL text.
        sql = "select * from student where id=%s"
        value = (id,)

        Student.mycursor.execute(sql,value)

        try:
            # Since an id lookup can match at most one row, fetchone() (a
            # single tuple, or None) is the right call rather than
            # fetchall().
            obj = Student.mycursor.fetchone()
            # Wrap the raw tuple of column values back into a Student
            # object, so callers get a friendly object with named
            # attributes (obj.name, obj.gender, ...) instead of a bare
            # tuple they'd have to remember the column order for.
            return Student(obj[0],obj[1],obj[2],obj[3],obj[4],obj[5])
        except mysql.connector.Error as err:
            print('Error', err)

    def updateStudent(self):
        # UPDATE changes an existing row's columns; the WHERE clause at the
        # end ("where id=%s") is what keeps this scoped to just this one
        # student's row instead of touching every row in the table.
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = (self.studentNumber,self.name,self.surname,self.birthdate,self.gender,self.id)
        Student.mycursor.execute(sql,values)

        try:
            # As with INSERT, the change only becomes permanent once
            # commit() runs.
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} record(s) updated')
        except mysql.connector.Error as err:
            print('Error:',err)

    @staticmethod
    def updateStudents(student_list):
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s where id=%s"
        values = []
        # Each row coming into this method (see `updated_students` at the
        # bottom of this file) is shaped like
        # (id, studentNumber, name, surname, birthdate, gender) -- id first.
        # But the UPDATE statement above needs its values in the order
        # (studentNumber, name, surname, birthdate, gender, id) -- id LAST,
        # since that's the order its %s placeholders appear in (the first
        # five fill in the SET clause, and the final one fills in the WHERE
        # clause). `order` describes that reshuffle: index 1 (studentNumber)
        # comes first, ... , and index 0 (id) comes last.
        order = [1,2,3,4,5,0]

        for item in student_list:
            # Rebuild each row in the new column order using a list
            # comprehension: for every position i in `order`, take item[i].
            item = [item[i] for i in order]
            values.append(item)

        # executemany() then runs the UPDATE once per reordered row, so a
        # whole batch of students can be updated in one call.
        Student.mycursor.executemany(sql,values)

        try:
            Student.connection.commit()
            print(f'{Student.mycursor.rowcount} record(s) updated')
        except mysql.connector.Error as err:
            print('Error:',err)

    @staticmethod
    def getStudentsGender(gender):
        # WHERE gender=%s filters to only the rows matching the given
        # gender value ('E' or 'K' in this dataset).
        sql = "select * from student where gender=%s"
        value = (gender,)

        Student.mycursor.execute(sql,value)

        try:
            # fetchall() here returns every matching student as a list of
            # raw tuples (not wrapped into Student objects, unlike
            # getStudentById above) -- that's fine because the caller below
            # just wants to read and rewrite plain values.
            return Student.mycursor.fetchall()
        except mysql.connector.Error as err:
            print('Error', err)


# student = Student.getStudentById(8)

# student.name = 'Kerem'
# student.surname = 'Deniz'

# student.updateStudent()


# This is where I learned I could pull a whole filtered group back, tweak it in Python, then push it all back with executemany
#
# Step 1: fetch every male student ('E') as a list of raw row-tuples.
students = Student.getStudentsGender('E')
print(students)

# Step 2: modify that data in plain Python (not in SQL) -- here, prefixing
# every one of those students' surnames with "Mr ".
updated_students = []
for std in students:
    # Tuples are immutable, so std is first converted to a list to allow
    # changing one of its elements in place.
    std = list(std)
    # The Student table's columns are, in order: Id(0), StudentNumber(1),
    # Name(2), Surname(3), Birthdate(4), Gender(5) -- so index 2 is the
    # `Name` column, meaning this line prefixes "Mr " onto each student's
    # first name (not their surname).
    std[2] = 'Mr ' + std[2]
    updated_students.append(std)

# Step 3: send the whole modified batch back to the database in one shot.
Student.updateStudents(updated_students)
