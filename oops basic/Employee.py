class Employee:
    def __init__(self):
        self.salary = 0.0
    def set_salary(self,s):
        self.salary = s
    def get_salary(self):
        return self.salary

e1 = Employee()
e1.set_salary(20900)
print(e1.get_salary())
