import sqlite3

connection=sqlite3.connect('testdb.db')

print("Connection established")

connection.execute("""
 create table people
 (
     sno int primary key,
     name text not null,
     city text not null
 )
""")

