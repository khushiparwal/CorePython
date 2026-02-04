class Circle:
    def __init__(self):
        self.radius = 0.0
    def set_radius(self,r):
        self.radius = r
    def get_radius(self):
        return self.radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius

c1 = Circle()
c1.set_radius(7)
print("Radius:",c1.get_radius())
print("Area:",c1.area())
print("Circumference:",c1.perimeter())