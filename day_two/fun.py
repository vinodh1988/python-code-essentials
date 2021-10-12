def add(*a):
    result=0
    print(type(a))
    for x in a:
        result+=x
    return result

print(add(1,2,3))
print(add(12,335))
print(add(34534,3434,334,32,3,56345))
print(add(34.43,345.32))