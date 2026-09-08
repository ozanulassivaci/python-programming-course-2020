# mysql-connector-python is the official driver that lets Python talk to a
# MySQL server -- it turns Python calls like .execute() or .commit() into the
# network protocol the MySQL server understands.
import mysql.connector

# mysql.connector.connect(...) opens one network connection to a running
# MySQL server and authenticates against it, the same way logging into a
# website needs an address, a username and a password.
#   host     - "localhost" means the MySQL server is running on this same
#              machine.
#   user     - the MySQL account to log in as ("root" is the default admin
#              account MySQL creates on install).
#   password - the password for that account.
#   database - which database (a named collection of tables) on the server
#              to use; "schooldb" must already exist.
#
# your_password: replace this with your own local MySQL password
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_password",
    database = "schooldb"
)

# dbmanager.py imports this single `connection` object ("from connection
# import connection") so that every method on DbManager reuses the same
# open connection instead of each one reconnecting to the server.
