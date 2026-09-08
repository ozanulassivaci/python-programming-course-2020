# mysql-connector-python is the official Python driver for MySQL: it handles
# the network conversation with the MySQL server so we can just call plain
# Python methods like .execute() and .commit().
import mysql.connector

# mysql.connector.connect(...) opens a connection to a MySQL server using
# credentials, similar to logging into a remote machine:
#   host     - address of the machine running MySQL. "localhost" means this
#              same computer; the commented-out "192.23.45.56" shows that in
#              real life this could just as easily be a different machine's
#              IP address on the network.
#   user     - the MySQL account name ("root" = default administrator).
#   password - that account's password.
#   database - which database/schema on the server to use ("node-app" here).
#
# your_password: replace this with your own local MySQL password
mydb = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "your_password",
    database = "node-app"
)

# A "cursor" is the object you actually use to run SQL statements and read
# back their results over this connection. Think of the connection as the
# open phone line to the database, and the cursor as the handset you speak
# into and listen through -- .execute() sends a query, and .fetchone() /
# .fetchall() read back whatever rows came back.
mycursor = mydb.cursor()

