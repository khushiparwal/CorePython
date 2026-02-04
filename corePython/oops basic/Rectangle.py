class Rectangle:
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
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.breadth+self.length)

r1 = Rectangle()
r1.set_length(5)
r1.set_breadth(10)
print("length:",r1.get_length())
print("breadth:",r1.get_breadth())
print("Area:",r1.area())
print("perimeter:",r1.perimeter())