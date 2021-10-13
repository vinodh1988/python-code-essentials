class Student:
    __sno = None
    __name = None
    __city = None
    def __init__(self,sno,name,city,skill):
        self.__sno=sno
        self.__name=name
        self.__city=city
        self.skill=skill
    
    def display(self):
        self.__callme()
        print("sno: {} name:{} city:{} skill:{}".format(self.__sno,self.__name,self.__city,self.skill))

    def __callme(self):
        print('did you callme')
