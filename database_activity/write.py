import sqlite3

connection=sqlite3.connect('testdb.db')

statement="insert into people(sno,name,city) values(?,?,?)"

while True:
    sno=int(input("Enter Sno ->"))
    name=input("Enter Name ->")
    city=input("Enter City ->")
    connection.execute(statement,(sno,name,city))
    data=input('press enter to terminate any other character to continue')
    if(len(data)==0):
        break
 
cursor=connection.execute("select * from people")   
for row in cursor:
    print("{} {} {}".format(row[0],row[1],row[2]))

connection.commit()
connection.close()

