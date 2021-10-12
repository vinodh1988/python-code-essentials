listitems=[34,6345,343,513,577,432,12,5772,256,1567,15,1578,1677,64342]

def isPrime(n):
    for x in range(2,int(n/2)):
        if(n%x==0):
            return False

    return True

filtered=filter(isPrime,listitems)
filtered2=filter(lambda x:True if x%2==0 else False,listitems)

print(listitems)
print(list(filtered))
print(list(filtered2))