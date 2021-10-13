from oops import SquareSpace

ground1=SquareSpace(100)
ground2=SquareSpace(120)
if(ground1>ground2):
    ground3=ground1-ground2
else:
    ground3=ground2-ground1
ground1.area()
ground2.area()
ground3.area()
