# This is my first look at sqlite3 - no server, no password, just a local file database
#
# sqlite3 is part of Python's standard library (no "pip install" needed) and
# talks to SQLite, a lightweight SQL database engine that stores an entire
# database as a single ordinary file on disk. Unlike MySQL, there's no
# separate server process to start, no host/user/password to configure --
# you just point at a file and SQLite reads/writes it directly. That makes
# it great for learning, small tools, and embedded apps, though it's not
# built for many programs writing to it at the same time over a network the
# way MySQL is.
import sqlite3

# sqlite3.connect(path) opens (or creates, if it doesn't exist yet) the
# database file at that path. "chinook.db" is a well-known sample database
# (a fictional digital media store) used for practicing SQL.
connection = sqlite3.connect("chinook.db")

# A cursor is the object used to actually run SQL statements and read back
# whatever rows they return, similar to mysql.connector's cursor.
cursor = connection.cursor()

# cursor.execute(sql) sends a raw SQL statement to the database engine.
# "select * from customers" means: from the "customers" table, give me every
# column (that's what the * wildcard means) for every row -- i.e. return the
# whole table as it currently stands, with no filtering.
cursor.execute("select * from customers")

# fetchall() pulls back ALL of the rows the query produced, as a Python list
# of tuples (one tuple per row, with values in the same order as the table's
# columns). Use fetchall() when you expect (and can afford to hold in memory)
# every matching row; fetchone() below in other files is used instead when
# you only want a single row at a time.
result = cursor.fetchall()

for i in result:
    print(i)

# Always close the connection when you're done with it, to release the file
# lock/handle SQLite is holding open. Forgetting this in a long-running
# program can eventually exhaust available file handles or leave the
# database file locked for other processes.
connection.close()