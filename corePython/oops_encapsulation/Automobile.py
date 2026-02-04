class Automobile:
    NO_OF_GEARS = 6
    def __init__(self,color,speed,make):
        self.color = ""
        self.speed = 0.0
        self.make = ""
    def set_color(self,c):
        self.color = c
    def get_color(self):
        return self.color
    def set_make(self,m):
        self.make = m
    def get_make(self):
        return self.make
    def set_speed(self,s):
        self.speed = s
    def get_speed(self):
        return self.speed
