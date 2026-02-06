class Fruit:
    def color(self):
        return None

class Apple(Fruit):
    def color(self):
        return "Red"
class Orange(Fruit):
    def color(self):
        return "Orange"

a1 = Apple()
print(a1.color())
o1 = Orange()
print(o1.color())
f1 = Fruit()
print(f1.color())