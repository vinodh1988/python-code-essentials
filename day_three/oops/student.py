class Student:
    def __init__(self,sno,name,city):
        self.sno=sno
        self.name=name
        self.city=city
    
    def display(self):
        print("sno: {} name:{} city:{}".format(self.sno,self.name,self.city))

