import pickle
class Employee:
    def __init__(self,id,name,age):
        self.id = id
        self.name = name
        self.age = age
    def display(self):
        print(self.id,"\t",self.name,"\t",self.age)

with open("../files/Employee.txt","wb") as file:
    e1 = Employee(1,"Khushi",21)
    pickle.dump(e1,file)
