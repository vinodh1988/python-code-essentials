def fileappender(filename,record):
    file=None
    try:
        file=open(filename,'a')
        file.write(record+'\n')  
    except Exception as e:
        print(e)
        print('failed')
    finally:
        if(file):
            file.close()
