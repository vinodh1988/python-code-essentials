numberlist=[254,2356,34634,1523,-5634,356,5633,156,-2166,36634]
stringlist=['ram','John','irwin','mahesh','john','ray']

#if a function is passed as a reference to map
#the function should take one parameter and it should return a value
def changeSign(x):
    return x*-1

def evenOrOdd(x):
    return "Even" if x%2==0 else "Odd" 


newlist=map(changeSign,numberlist)
newlist2=map(evenOrOdd,numberlist)

newlist3=map(lambda x:x*-1,numberlist)
newlist4=map(lambda x:"Even" if x%2==0 else "Odd",numberlist)
newlist5=map(lambda x:x.capitalize(),stringlist)
print(changeSign(5))

print(list(newlist))
print(list(newlist2))
print("-----------------------------------------------")
print(list(newlist3))
print(list(newlist4))
print(list(newlist5))