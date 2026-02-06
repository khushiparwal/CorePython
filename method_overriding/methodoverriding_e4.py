from typing import List

class Vehicle:
    def color(self):
        print("No vehicle")

class Fourwheeler(Vehicle):
    def color(self):
        print("White suv")

class Twowheeler(Vehicle):
    def color(self):
        print("Black activa")

vehicles: List[Vehicle] = [Fourwheeler(),Twowheeler()]
for v in vehicles:
    v.color()
