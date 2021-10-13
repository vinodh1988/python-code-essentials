def fileseeker(filename,position):
    file=open(filename,'r')
    file.seek(position)
    print(file.read(10))