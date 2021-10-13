class Shape:
    def __init__(self,name=None):
        print('super class constructor called')
        self.name=name
    
    def _display(self):
        print('Shape is {}'.format(self.name))


class Square(Shape):
    __side=None
    def __init__(self,name,side):
        super().__init__(name)
        self.__side=side
    
    def display(self):
        self._display()
        print('Length of square is  {}'.format(self.__side))