from abc import ABC, abstractmethod

class Shape(ABC):
    def execute(self):
        self.area()
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        self.ar = self.length*self.breadth
        print("Area:",self.ar)

r1 = Rectangle(5,10)
r1.execute()