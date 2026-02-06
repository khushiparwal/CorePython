from operator import length_hint
from typing import List
class Shape:
    def area(self):
        print("Area of shape class")

class Rectangle(Shape):
    def __init__(self):
        self.length = 0
        self.breadth = 0
    def set_length(self,l):
        self.length = l
    def get_length(self):
        return self.length
    def set_breadth(self,b):
        self.breadth = b
    def get_breadth(self):
        return self.breadth
    def area(self):
        r_area = self.length*self.breadth
        print("area of rectangle: ",r_area)

class Circle(Shape):
    PI = 3.14
    def __init__(self):
        self.radius = 0.0
    def set_radius(self,r):
        self.radius = r
    def get_radius(self):
        return self.radius
    def area(self):
        c_area = self.PI*self.radius*self.radius
        print("Area of circle: ",c_area)

shapes: List[Shape] = [Rectangle(),Circle()]

r1 : Rectangle = shapes[0]
r1.set_length(10)
r1.set_breadth(5)

c1: Circle = shapes[1]
c1.set_radius(100)

for s in shapes:
    s.area()