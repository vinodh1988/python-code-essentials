def fun():
    print('fun is running')

def sayHi(a):
    if isinstance(a,str):
        print("Hi", a)
    else:
        print('Not a right value')

fun()

print(fun())
for x in ['Raj','Ravi','Sam','Lara',12,455,True,[1,3254,4]]:
    sayHi(x)