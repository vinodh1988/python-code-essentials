

for x in range(2,100):
    if(x%2==0 and x%3==0 and x%9==0):
        print(x,end=":::")

x=1

while x<10:
    print(x)
    x+=1
print("--------------------------------------")
for x in range(0,20,3):
    if(x!=0 and x%5==0):
        break
    if(x==6):
        continue
    print(x)

print("------------------------------------------------")

temp=105

if temp >= 98 and temp <=99:
    pass
elif temp >=99 and temp <= 101:
    print('Give moderated medicine')
else:
    print('Take to hospital')