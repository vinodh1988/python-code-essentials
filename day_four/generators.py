import random

""" for x in range(1,10):
    print(round(random.random()*100)) """

def dataEmitter():
    while True:
        temp=round(random.random()*100)
        if temp==99:
            break
        yield temp
        print('back in function')

result=dataEmitter()

"""
for x in result:
    print(x)
"""
""" 
while True:
    try:
        print(next(result))
    except StopIteration:
        print('the function has finished yielding')
        break """

def multi():
    print("line1")
    yield "India"
    print("line2")
    yield "China"
    print("line3")
    yield("Russia")

p=multi()
print(next(p))
print(next(p))