import datetime
class Person:
    AVG_AGE = 18
    def __init__(self):
        self.name = ""
        self.dob = None
        self.address = ""
    def set_name(self,n):
        self.name = n
    def get_name(self):
        return self.name
    def set_dob(self,y,m,d):
        self.dob = datetime.date(y,m,d)
    def get_dob(self):
        return self.dob
    def set_address(self,a):
        self.address = a
    def get_address(self):
        return self.address

    def get_age(self):
        today = datetime.date.today()
        if self.dob==None:
            return "No input date"
        else:
            age = today.year - self.dob.year
            if (today.day,today.month) < (self.dob.day,self.dob.month):
                age -= 1
        return age

p1 = Person()
p1.set_name("Ram")
p1.set_address("Delhi")
p1.set_dob(2005,6,23)
print(p1.get_age())