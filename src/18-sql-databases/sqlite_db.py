# This is my first look at sqlite3 - no server, no password, just a local file database
import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

cursor.execute("select * from customers")
result = cursor.fetchall()

for i in result:
    print(i)

connection.close()