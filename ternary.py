name=input('enter name')
valid=True if len(name)>=5 else False
print(valid)
a,b=12,15
bigger=a if a>b else b
print("in",a,b,bigger,' is bigger')