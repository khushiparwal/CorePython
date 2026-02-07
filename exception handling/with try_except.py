print("before")
a = 10
b= 0
print("mid")
try:
    c = a/b
    print("Division: ",c)
except ZeroDivisionError as e:
    print("Exception raised: ",e)

print("after")

