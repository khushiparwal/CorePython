class Shape:
    def __init__(self):
        self.color = ""
        self.borderwidth=0
    def set_color(self, co):
         self.color = co
    def get_color(self):
        return self.color
    def set_borderwidth(self,bd):
        self.borderwidth = bd
    def get_borderwidth(self):
        return self.borderwidth

s1 = Shape()
s1.set_color("Blue")
s1.set_borderwidth(10)

print(s1.get_color())
print(s1.get_borderwidth())
