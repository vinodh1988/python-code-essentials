import pickle

""" students={}
i=0
while True:
    sno=int(input("Enter Sno ->"))
    name=input("Enter Name ->")
    city=input("Enter City ->")
    i+=1
    students['student'+str(i)]={'sno':sno,'name':name,'city':city}
    x=input('press Enter to terminate any input to continue')
    if(len(x)==0):
        break

picklefile=open('studentData','wb')

pickle.dump(students,picklefile)
picklefile.close()

 """
picklefile=open('studentData','rb')
data=pickle.load(picklefile)

#print(data)

for keys in data:
    print(data[keys])