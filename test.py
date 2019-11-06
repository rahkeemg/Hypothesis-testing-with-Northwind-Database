import sqlite3
import MyConn as mc


myconn = mc.MyConn('./Northwind_small.sqlite')
print(myconn.database_tables())

myconn.close_connection()