try:
    a = 10
    b = 2
    c = a/b
    print("Division: ",c)
except ZeroDivisionError as e:
    print("Exception: ",e)
else:
    print("Division successful")
finally:
    print("Code executed")

try:
    n = int(input("Enter a number: "))
    print("Square: ",n*n)
except ValueError as e:
    print("Exception: ",e)
except Exception as e:
    print("Exception: ",e)
else:
    print("Successful")