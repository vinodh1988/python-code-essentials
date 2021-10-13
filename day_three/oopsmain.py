from oops import Student

obj1=Student(1,'Rahul','Chennai','C++')
obj2=Student(2,'Jose','Mumbai','Java')

obj1.display()
obj2.display()


obj1.__sno=89
obj2.__name='Rakesh'
obj2.skill='Python'

obj1.display()
obj2.display()
#obj1.__callme()
