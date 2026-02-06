class Vehicle:
    def execute(self):
        if self.isColor() == "white":
            self.name()
        else:
            print("No white vehicle")
    def isColor(self):
        return ""
    def name(self):
        print("No vehicle given")

class Fourwheeler(Vehicle):
    def isColor(self):
        return "white"
    def name(self):
        print("Creta")

class Twowhheler(Vehicle):
    def isColor(self):
        return ("white")
    def name(self):
        print("Activa")
class Test(Vehicle):
    pass

f1 = Fourwheeler()
f1.execute()
t1 = Twowhheler()
t1.execute()
te1 = Test()
te1.execute()
