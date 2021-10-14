import re

listitem=['India','Interest','cat','mat','bat','put','Apple','Instrument',
'15345','jug123','Nation','ration','Friction','track','crack','manoj@gmail.com',
'manoj_123@gmail.com','test@gmail','123India','Dry','fry','Read','rock','Station','Man',
'K123an','123','324','a$1','c21','s2345','paul.j@gmail.com']


for x in listitem:
    #if re.match('^[INR]',x):
    #if re.match('^[A-Z][a-z]+n$',x):
    #if re.match('^[A-Za-z0-9].[A-Za-z0-9]$',x):
    #if re.match('^[A-Za-z]....$',x):
    #if re.match('^.{6}$',x):
    #if re.match('^.{3,5}$',x): 
    if re.match('^[a-z][a-z_\.0-9]+@[a-z]{3,10}\.(com|in|net)$',x):  
        print(x)

