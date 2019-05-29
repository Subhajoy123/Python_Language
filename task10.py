# finding area using class 
class Rectangle:
    def __init__(self,l=0,b=0):
        self.leng=l
        self.bred=b
    def area(self):
        print(" the area is ",self.leng * self.bred)
l=int(input(" enter the length "))
b=int(input(" enter the breadth "))
a= Rectangle(l,b)
a.area()
