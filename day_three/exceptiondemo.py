
try:
    a=int(input("enter an integer->"))
    b=int(input("enter an integer->"))
    c=a/b
    print(c)
except ValueError:
    print("You have not entered an integer") 
except ZeroDivisionError:
    print("Denominator should not be zero")
except Exception as e:
    print(e)

print('program is still working')