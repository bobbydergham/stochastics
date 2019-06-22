import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "admin",
    port = 3306,
    database = "testdb",
    auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

