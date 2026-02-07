from abc import ABC, abstractmethod
class Vehicle(ABC):
    def execute(self):
        self.name()
    @abstractmethod
    def name(self):
        pass

class Fourwheeler(Vehicle):
    def __init__(self,n):
        self.n = n
    def name(self):
        print("Name of car is",self.n)

v1 = Fourwheeler("XUV")
v1.execute()
