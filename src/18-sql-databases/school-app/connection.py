import mysql.connector

# your_password: replace this with your own local MySQL password
connection = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "your_password",
    database = "schooldb"
)
