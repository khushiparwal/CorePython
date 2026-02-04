class Student:
    def get_student(self):
        self.name = input("Enter name:")
        self.age = int(input("enter age:"))
        self.gender = input("Enter gender:")

class Test(Student):
    def get_marks(self):
        self.studentclass = input("Enter class:")
        self.lit = int(input("Enter marks of literature:"))
        self.mth = int(input("Enter marks of maths:"))
        self.sci = int(input("Enter marks of science:"))

class Display(Test):
    def dis(self):
        print("\nName:",self.name)
        print("Age:",self.age)
        print("Gender:",self.gender)
        print("Class:",self.studentclass)
        print("Total marks:",self.lit+self.mth+self.sci)

m = Display()
m.get_student()
m.get_marks()
m.dis()