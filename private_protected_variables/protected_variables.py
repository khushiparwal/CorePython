class Shape:
    def __init__(self):
        self._color = ""
        self._borderwidth = 0
    def set_color(self,c):
        self._color = c
    def get_color(self):
        return self._color
    def set_borderwidth(self,bd):
        self._borderwidth = bd
    def get_borderwidth(self):
        return self._borderwidth

s1 = Shape()
s1.set_color("Red")
print(s1.get_color())
s1.set_borderwidth(10)
print(s1.get_borderwidth())

print("protected shape color: ",s1._color)

