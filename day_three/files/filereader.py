def filereader(filename):
    file=None
    try:
        file=open(filename,'r')
        result=file.readlines()
        for x in result:
            print(x)
    except FileNotFoundError:
        print("File Not Found")
    finally:
        if(file):
            file.close()