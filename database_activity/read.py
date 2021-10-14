import sqlite3

import sqlite3

connection=sqlite3.connect('testdb.db')

print("Connection established")

cursor=connection.execute("select * from people")

for row in cursor:
    print("{} {} {}".format(row[0],row[1],row[2]))