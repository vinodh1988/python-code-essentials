def getlines(filename):
    file=None
    try:
        file=open(filename,'r')
        return file.readlines()
    except:
        print('failed')
    else:
        file.close()

store={
    "peoplelist":['Roger','Rakesh','Harry','Jimmy','Joseph','Raj','Naveen'],
    "placelist":["Chennai","Mumbai","Bangalore","Delhi",'Kolkatta'],
    "linelist": getlines
}