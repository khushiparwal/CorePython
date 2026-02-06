from operator import length_hint
from typing import List
class Shape:
    def area(self):
        print("Area of shape class")

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        r_area = self.length*self.breadth
        print("area of rectangle: ",r_area)

class Circle(Shape):
    PI = 3.14
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        c_area = self.PI*self.radius*self.radius
        print("Area of circle: ",c_area)

shapes: List[Shape] = [Rectangle(10,5),Circle(10)]

for s in shapes:
    s.area()