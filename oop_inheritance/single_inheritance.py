class Shape:
    def __init__(self):
        self.color = ""
        self.borderwidth = 0
    def set_color(self,c):
        self.color=c
    def get_color(self):
        return self.color
    def set_borderwidth(self,bd):
        self.borderwidth=bd
    def get_borderwidth(self):
        return self.borderwidth

class Square(Shape):
    def __init__(self):
        self.side = 0
    def set_side(self,s):
        self.side=s
    def get_side(self):
        return self.side
    def area(self):
        return self.side*self.side
    def perimeter(self):
        return 4*self.side

s1 = Square()
s1.set_side(2)
s1.set_color("Blue")
s1.set_borderwidth(5)
print("Side:",s1.get_side())
print("Area:",s1.area())
print("Perimeter:",s1.perimeter())
print("color:",s1.get_color())
print("border:",s1.get_borderwidth())