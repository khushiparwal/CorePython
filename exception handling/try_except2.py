d1 = {'Name':'Ram','Age':25}
print(d1)
print("Age using get method: ",d1.get("Age"))
try:
    print(d1.get())
except TypeError as t:
    print("Exception: ",t)
