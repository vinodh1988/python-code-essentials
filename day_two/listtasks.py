numberlist=[254,2356,34634,1523,-5634,356,5633,156,-2166,36634]

#if a function is passed as a reference to map
#the function should take one parameter and it should return a value
def changeSign(x):
    return x*-1

newlist=map(changeSign,numberlist)

print(changeSign(5))

print(list(newlist))