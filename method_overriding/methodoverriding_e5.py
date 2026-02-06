from typing import List
class Vehicle:
    def get_color(self):
        print("No vehicle found")

class Fourwheeler(Vehicle):
    def __init__(self):
        self.color = ""
    def set_color(self,c):
        self.color = c
    def get_color(self):
        print(self.color)

class Twowheeler(Vehicle):
    def __init__(self):
        self.color = ""
    def set_color(self,c):
        self.color = c
    def get_color(self):
        print(self.color)

veh : List[Vehicle] = [Fourwheeler(),Twowheeler()]

f1: Fourwheeler() = veh[0]
f1.set_color("Blue car")

t1: Twowheeler() = veh[1]
t1.set_color("Black bike")

for v in veh:
    v.get_color()
