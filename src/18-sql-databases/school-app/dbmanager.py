import mysql.connector
from datetime import datetime
# Reuse the single shared `connection` object from connection.py instead of
# opening a brand-new connection to MySQL every time we need one.
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class

class DbManager:
    # DbManager centralizes every SQL statement the app needs behind plain
    # Python methods (getStudentById, addStudent, ...), so the rest of the
    # app (app.py) never has to write raw SQL itself -- it just calls
    # db.addStudent(student) and so on. This separation is a common pattern:
    # keep all database access in one place so it's easy to find, reuse, and
    # change later.
    def __init__(self):
        self.connection = connection
        # A cursor is what actually sends SQL statements to the server and
        # reads back whatever rows they return.
        self.cursor = self.connection.cursor()

    def getStudentById(self,id):
        # WHERE id = %s filters the SELECT down to (at most) the single row
        # matching that id. Using a %s placeholder rather than pasting `id`
        # directly into the SQL string is what protects this from SQL
        # injection -- the driver always substitutes it as plain data.
        sql = "select * from student where id = %s"
        value  = (id,)
        self.cursor.execute(sql,value)
        try:
            # Since id is a primary key, at most one row can match, so
            # fetchone() (a single tuple, or None) is the right call here.
            obj = self.cursor.fetchone()
            # Wrap the raw tuple into a friendly Student object (or a list
            # containing one, per CreateStudent's contract) instead of
            # returning bare tuple data.
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            # mysql.connector.Error covers driver-level failures (bad SQL,
            # constraint violations, connection problems, etc.).
            print('Error:', err)

    def deleteStudent(self,studentid):
        # DELETE removes an entire row. The WHERE clause is what limits this
        # to just the one student -- without it, MySQL would delete every
        # row in the table.
        sql = "delete from student where id=%s"
        value = (studentid,)
        self.cursor.execute(sql,value)

        try:
            # Nothing is actually removed from the table until commit()
            # runs.
            self.connection.commit()
            # rowcount reports how many rows actually matched and were
            # deleted (0 if no student had that id).
            print(f'{self.cursor.rowcount} record(s) deleted.')
        except mysql.connector.Error as err:
            print('error:', err)

    def getClasses(self):
        # No WHERE clause here, so this returns every row in the class
        # table -- the full list of classes.
        sql = "select * from class"
        self.cursor.execute(sql)
        try:
            # fetchall() returns every matching row as a list of tuples;
            # Class.CreateClass turns each tuple into a Class object.
            obj = self.cursor.fetchall()
            return Class.CreateClass(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def getStudentsByClassId(self,classid):
        # Filters students down to just the ones enrolled in one particular
        # class, using classid as a foreign key that links a student row
        # back to a row in the class table.
        sql = "select * from student where classid = %s"
        value  = (classid,)
        self.cursor.execute(sql,value)
        try:
            obj = self.cursor.fetchall()
            return Student.CreateStudent(obj)
        except mysql.connector.Error as err:
            print('Error:', err)

    def addorEditStudent(self,student: Student):
        # Left unimplemented (just `pass`, meaning "do nothing") -- this
        # looks like it was meant to be a single combined
        # insert-or-update method, but addStudent() and editStudent() below
        # ended up implemented separately instead, so this one was never
        # finished or wired up.
        pass

    def addStudent(self, student: Student):
        # A parameterized INSERT: each %s is filled in from `value` by the
        # driver, which is what keeps this safe from SQL injection (a
        # student's name or surname can never be interpreted as SQL syntax,
        # only ever as plain text data).
        sql = "INSERT INTO Student(StudentNumber,Name,Surname,Birthdate,Gender,ClassId) VALUES (%s,%s,%s,%s,%s,%s)"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid)
        self.cursor.execute(sql,value)

        try:
            # The new row isn't permanent until commit() is called.
            self.connection.commit()
            print(f'{self.cursor.rowcount} record(s) inserted.')
        except mysql.connector.Error as err:
            print('error:', err)

    def editStudent(self, student: Student):
        # UPDATE rewrites the listed columns on the one row matching
        # "where id=%s" -- that WHERE clause is what keeps the change
        # scoped to this single student instead of the entire table.
        sql = "update student set studentnumber=%s,name=%s,surname=%s,birthdate=%s,gender=%s,classid=%s where id=%s"
        value = (student.studentNumber,student.name, student.surname,student.birthdate,student.gender,student.classid,student.id)
        self.cursor.execute(sql,value)

        try:
            self.connection.commit()
            print(f'{self.cursor.rowcount} record(s) updated.')
        except mysql.connector.Error as err:
            print('error:', err)


    def editTeacher(self, teacher: Teacher):
        # Not implemented yet -- Teacher support in this demo app was left
        # incomplete (see the note in Teacher.py about its constructor
        # never storing classid either).
        pass

    def __del__(self):
        # __del__ is a special method Python calls when an object is about
        # to be garbage-collected (i.e. when nothing references it anymore
        # and it's cleaned up). Closing the connection here means that once
        # a DbManager instance goes away, its database connection is
        # released too, instead of being left open indefinitely.
        self.connection.close()
        print('database connection closed')
