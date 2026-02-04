class Vehicle:
    def get_vehicle(self):
        self.color = input("Enter color:")
        self.wheels = int(input("Enter no of wheels"))

class Fourwheeler(Vehicle):
    def get_type(self):
        self.type = input("Enter car type:")
        self.name = input("Enter name:")
        self.capacity = int(input("Enter capacity of car:"))

class Display(Fourwheeler):
    def dis(self):
        print("\nName:",self.name)
        print("Type:",self.type)
        print("Color:",self.color)
        print("Wheels:",self.wheels)
        print("Capacity:", self.capacity)

m = Display()
m.get_vehicle()
m.get_type()
m.dis()