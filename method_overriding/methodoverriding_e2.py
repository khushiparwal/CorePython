class Vehicle:
    def execute(self):
        self.name()
    def name(self):
        print("No vehicle")

class Fourwheeler(Vehicle):
    def name(self):
        print("Creta")

class Twowheeler(Vehicle):
    def name(self):
        print("Activa")

class Test(Vehicle):
    pass

f1 = Fourwheeler()
f1.execute()
t1 = Twowheeler()
t1.execute()
te1 = Test()
te1.execute()