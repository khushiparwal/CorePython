import datetime
d = datetime.date.today()

future = d + datetime.timedelta(days=7)
past = d - datetime.timedelta(days=7)

print("Future is: ",future)
print("past is : ",past)