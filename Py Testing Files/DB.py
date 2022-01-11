from PyQt5 import QtSql
import sqlite3

try:
    conn= sqlite3.connect("DataBaseTable.db")
    print("database opened")

except:
    print("error opening database")

#conn.execute("select * from UsersTable where User_Name=admin and User_Password=4186")