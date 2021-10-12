a=20
def process(b):
    global a
    a=b
    print('inside ',a)
    b=40

process(40)
print('outside ',a)
process("Rakesh")
print('outside ',a)
c=89
process(c)
print('outside ',a)
