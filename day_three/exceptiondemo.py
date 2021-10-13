
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
else:
    print('Excecutes only when everything went fine')
finally: 
    print('XXXXXXX Mandatory logic executing XXXXXX')

print('program is still working')