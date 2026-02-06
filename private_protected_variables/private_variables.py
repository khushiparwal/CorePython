class Shape:
    def __init__(self):
        self.__color = ""
        self.__borderwidth = 0
    def set_color(self,c):
        self.__color = c
    def get_color(self):
        return self.__color
    def set_borderwidth(self,bd):
        self.__borderwidth = bd
    def get_borderwidth(self):
        return self.__borderwidth

s= Shape()
s.set_color("Green")
print(s.get_color())
s.set_borderwidth(5)
print(s.get_borderwidth())

