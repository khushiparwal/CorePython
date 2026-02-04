class Personcount:
    count = 0
    def __init__(self):
        self.name = ""
        Personcount.count += 1
    def set_name(self,n):
        self.name = n
    def get_name(self):
        return self.name

p1 = Personcount()
p1.set_name("Ram")
p2 = Personcount()
p2.set_name("Mohan")
print(p1.get_name())
print(p2.get_name())
print("no of people:",Personcount.count)