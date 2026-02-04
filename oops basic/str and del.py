class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __del__(self):
        classname = self.__class__.__name__
        print("Destroying ",classname)
    def __str__(self):
        return "Person: name: %s, age: %s"%(self.name,self.age)

p1 = Person("Khushi",21)
p2 = Person("Ram",30)
print(p1)
print(p2)