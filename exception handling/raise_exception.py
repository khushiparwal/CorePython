try:
    n = int(input("enter a number:"))
    if n>10:
        raise Exception("invalid number")
except Exception as e:
    print("Exception :",e)
