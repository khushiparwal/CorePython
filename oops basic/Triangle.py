class Triangle:
    def __init__(self,height,base):
        self.height = height
        self.base = base

    def get_measures(self):
        return "Height:%s, Base:%s"%(self.height, self.base)
    def area(self):
        return 0.5*self.base*self.height

t1 = Triangle(5,10)
print(t1.get_measures())
print("Area:",t1.area())