# import functools

#functools.reduce
from functools import reduce

numbers=[12,5346,34,35666,123,3556,343,3456,3456,123,56]
strings=['Rajan','arjun','Rahul','naresh','Gautham','Benny','Krishna']

sum=reduce(lambda x,y: x+y,numbers)

print('sum of numbers in list',sum)

first_in_dictionary=reduce(lambda x,y:x if x<y else y,strings)
last_in_dictionary=reduce(lambda x,y:x if x>y else y,strings)
print(first_in_dictionary) 
print(last_in_dictionary)

