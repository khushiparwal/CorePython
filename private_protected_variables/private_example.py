class Vehicle:
    def __init__(self):
        self.__name = ""
        self.__speed = 0
    def set_name(self,n):
        self.__name = n
    def get_name(self):
        return self.__name
    def set_speed(self,s):
        self.__speed= s
    def get_speed(self):
        return self.__speed

v= Vehicle()
v.set_name("Truck")
print("name: ",v.get_name())
v.set_speed(120)
print("speed: ",v.get_speed())
