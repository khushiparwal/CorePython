class Shape:
    def execute(self):
        self.area()
    def area(self):
        print("Area of shape class")

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        r_area = self.length*self.breadth
        print("Rectangle area:",r_area)
        return r_area

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        c_area = 3.14*self.radius*self.radius
        print("circle area: ",c_area)

class Test(Shape):
    pass

r1 = Rectangle(10,10)
r1.execute()
c1 = Circle(100)
c1.execute()
t1 = Test()
t1.execute()