from files import store
from files import fileappender
from time import localtime,time

""" 
while True:
    record=input()
    if(len(record)==0):
        break
    fileappender('x.txt',record)
     """

""" for x in store["peoplelist"]:
    fileappender('new.txt',x) """

datalist=store["linelist"]('sample.py')
fileappender('appender.txt',"\n-----------{}------------\n".format("New Entry"))
firstline=int(input('enter the beginning line no to read-->'))
lastline=int(input('enter the ending line no to read-->'))
sliced=datalist[firstline-1:lastline+1]
for x in sliced: 
    fileappender('appender.txt',x)
