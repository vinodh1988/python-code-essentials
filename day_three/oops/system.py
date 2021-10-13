class Shape:
    def __init__(self,name=None):
        print('super class constructor called')
        self.name=name
    
    def _display(self):
        print('Shape is {}'.format(self.name))

class Box:
    def __init__(self,type=None):
        self.type=type
   
    def _display(self):
        print('Box is {}'.format(self.type))


class Square(Box,Shape):
    __side=None
    def __init__(self,name,type,side):
        #super().__init__(name)
        Box.__init__(self,type)
        Shape.__init__(self,name)

        self.__side=side
    
    def display(self):
        Shape._display(self)
        Box._display(self)
        print('Length of square is  {}'.format(self.__side))