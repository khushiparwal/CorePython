class Shape:
    def __init__(self,color='',borderwidth=0):
        self.color = color
        self.borderwidth = borderwidth
    def get_color(self):
        return self.color
    def get_borderwidth(self):
        return self.borderwidth

class Rectangle(Shape):
    def __init__(self,length=0.0,breadth=0.0,color='',borderwidth=0):
        self.length = length
        self.breadth = breadth
        super().__init__(color, borderwidth)
    def get_length(self):
        return self.length
    def get_breadth(self):
        return self.breadth
    def get_area(self):
        return self.length*self.breadth

class Circle(Shape):
    def __init__(self,radius=0.0,color='',borderwidth=0):
        self.radius = radius
        super().__init__(color,borderwidth)
    def get_radius(self):
        return self.radius
    def get_area(self):
        return 3.14*self.radius*self.radius

r1 = Rectangle(10,20,'Red',5)
print("Rectangle:")
print("Length:",r1.get_length())
print("Breadth:",r1.get_breadth())
print("Area:",r1.get_area())
print("Color:",r1.get_color())
print("Borderwidth:",r1.get_borderwidth())
print('\n')
c1 = Circle(7,'Blue',3)
print("Circle:")
print("Radius:",c1.get_radius())
print("Area:",c1.get_area())
print("Color:",c1.get_color())
print("Borderwidth:",c1.get_borderwidth())
