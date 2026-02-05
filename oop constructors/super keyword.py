class Shape:
    def __init__(self,length=0,breadth=0):
        self.length = length
        self.breadth = breadth
    def get_length(self):
        return self.length
    def get_breadth(self):
        return self.breadth

class Square(Shape):
    def __init__(self,color='',length=0,breadth=0):
        self.color = color
        super().__init__(length,breadth)
    def get_color(self):
        return self.color

s = Square('blue',15,20)
print("Color:",s.get_color())
print("Length:",s.get_length())
print("breadth:",s.get_breadth())