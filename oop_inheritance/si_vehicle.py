class Vehicle:
    def __init__(self):
        self.speed= int(input("Enter speed:"))
        self.capacity = int(input("Enter capacity:"))
    def get_speed(self):
        return self.speed
    def get_capacity(self):
        return self.capacity
class Car(Vehicle):
    def __init__(self):
        super().__init__()
        self.name = input("Enter name of car:")
        self.color = input("Enter color of car:")
    def get_name(self):
        return self.name
    def get_color(self):
        return self.color

c1 = Car()
print("Name:",c1.get_name())
print("Color:",c1.get_color())
print("Speed:",c1.get_speed())
print("Capacity:",c1.get_capacity())
