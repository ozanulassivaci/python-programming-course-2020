import mysql.connector

# your_password: replace this with your own local MySQL password
mydb = mysql.connector.connect(
    host = "localhost", # 192.23.45.56
    user = "root",
    password = "your_password",
    database = "node-app"
)

mycursor = mydb.cursor()

