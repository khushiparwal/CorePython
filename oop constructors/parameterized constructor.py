class Shape:
    def __init__(self,color='',borderwidth=0):
        self.color = color
        self.borderwidth = borderwidth
    def set_color(self,c):
        self.color = c
    def get_color(self):
        return self.color
    def set_borderwidth(self,b):
        self.borderwidth = b
    def get_borderwidth(self):
        return self.borderwidth

s1 = Shape('Green',2)
print("Color of s1: ",s1.get_color())
print("borderwidth of s1: ",s1.get_borderwidth())

s2 = Shape()
s2.set_color('White')
s2.set_borderwidth(6)
print("\nColor of s2:",s2.get_color())
print("borderwidth of s2:",s2.get_borderwidth())