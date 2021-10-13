from files import filereader

while True:
    p=input("Enter file path with filename [Text file] >>>")
    if(len(p)==0):
        break
    filereader(p)
  