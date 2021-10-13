class SquareSpace:
    __side=None

    def __init__(self,side=0):
        self.__side=side

    def __gt__(self,second):
        return True if self.__side > second.__side else False

    def __sub__(self,second):
        result=SquareSpace()
        result.__side=self.__side-second.__side  
        return result      

    def area(self):
        print("length of Square -> {}".format(self.__side))
        print("Area of Square -> {} sq mts".format(self.__side*self.__side))