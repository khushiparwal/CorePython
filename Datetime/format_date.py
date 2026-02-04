import datetime
t = datetime.date.today()

f = t.strftime("%d-%m-%Y")
p = t.strftime("%A,%B,%C,%D")
print(p)
print(f)