
def modify(li,k,p,r):
    li.append(k)
    li.insert(1,p)
    li.append(r)
    print(li)
    del li[0]
    li.remove(645)
    print(li)

mylist=[13,45,645,54]

print(mylist)
modify(mylist,12,34,64)
print(mylist)


