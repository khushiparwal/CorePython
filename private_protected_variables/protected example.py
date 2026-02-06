class Vehicle:
    def __init__(self):
        self._name = ""
        self._speed = 0
    def set_name(self,n):
        self._name = n
    def get_name(self):
        return self._name
    def set_speed(self,s):
        self._speed= s
    def get_speed(self):
        return self._speed

v= Vehicle()
v.set_name("Truck")
print("name: ",v.get_name())
v.set_speed(120)
print("speed: ",v.get_speed())

print("Protected vehicle name: ",v._name)