import datetime

t = datetime.date.today()
birth = datetime.date(2004,7,29)

age = t.year - birth.year

if (t.month, t.day)<(birth.month, birth.day):
    age -= 1
print(age)

