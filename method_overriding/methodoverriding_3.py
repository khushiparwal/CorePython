class Shape:
    def execute(self):
        if self.validate():
            self.area()
        else:
            print("Validation failed")
    def validate(self):
        return False
    def area(self):
        print("Shape class area")

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def validate(self):
        if self.length>0 and self.breadth>0:
            return True
        else:
            return False
    def area(self):
        r_area = self.length*self.breadth
        print("Area of rectangle: ",r_area)

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def validate(self):
        if self.radius>0:
            return True
        else:
            return False
    def area(self):
        c_area = 3.14*self.radius*self.radius
        print("Area of circle: ",c_area)

class Test(Shape):
    pass

r = Rectangle(5,10)
r.execute()
c = Circle(100)
c.execute()
t = Test()
t.execute()

r1 = Rectangle(20,-10)
r1.execute()
c1 = Circle(-5)
c1.execute()

