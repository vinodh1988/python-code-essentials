def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def isPrime(n):
    for x in range(2,int((n/2)+1)):
        if(n%x==0):
            return False
    return True