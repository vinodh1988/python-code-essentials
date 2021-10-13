from files import fileseeker

while True:
    p=input("Enter file path with filename [Text file] >>>")
    if(len(p)==0):
        break
    pos=int(input("enter file position"))
    fileseeker(p,pos)
  

