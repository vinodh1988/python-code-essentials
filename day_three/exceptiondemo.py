from exceptions import DenominatorError,NegativeError

try:
    a=int(input("enter an integer->"))
    if(a<0):
        raise NegativeError(a)
    b=int(input("enter an integer->"))
    if(b<0):
        raise NegativeError(b)
    if(b>a):
        raise DenominatorError(b)
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