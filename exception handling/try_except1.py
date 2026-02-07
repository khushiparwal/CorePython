l1 = (2,4,6)
print(l1)
try:
    l1.append(5)
    print(l1)
except AttributeError as a:
    print("Exception raised: ",a)

try:
    print(x)
except NameError as n:
    print("Exception: ",n)