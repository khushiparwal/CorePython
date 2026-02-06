class Shape:
    def area(self):
        return -1

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius


r1 = Rectangle(5,20)
print("Area of rectangle: ",r1.area())

c1 = Circle(10)
print("Area of circle: ",c1.area())

shape : Shape=Rectangle(5,10)
shape.area()