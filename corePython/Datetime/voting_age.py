import datetime
b = datetime.date(2009,6,18)
t = datetime.date.today()

age = t.year-b.year
if (t.day,t.month)<(b.day,b.month):
    age -= 1

if age>=18:
    print("Person is eligible to vote")
else:
    print("not eligible to vote")