# mysql-connector-python is the official driver that lets Python talk to a
# MySQL server. A "driver" (also called a database adapter) is just a library
# that knows how to speak the network protocol a particular database expects,
# and translates our Python calls (like .execute() or .commit()) into that
# protocol under the hood.
import mysql.connector

# mysql.connector.connect(...) opens a network connection to a running MySQL
# server and logs in with the given credentials. Think of it like logging
# into a website: you need an address (host), a username, a password, and
# here you also pick which "database" (a named collection of tables living
# on that server) you want to work with.
#   host     - where the MySQL server is running. "localhost" means "this
#              same computer" (MySQL is listening on 127.0.0.1).
#   user     - the MySQL account name to log in as. "root" is the default
#              administrator account created when MySQL is installed.
#   password - the password for that account.
#   database - the specific database (schema) to connect to on that server;
#              here it's "schooldb", which must already exist on the server.
#
# your_password: replace this with your own local MySQL password
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_password",
    database = "schooldb"
)

# This module is imported by other files in this folder (e.g. Student.py via
# "from connection import connection") so that every part of the program
# shares the same open connection instead of each one opening its own.
