try:
    x = input("Enter a name:")
    if x=="Ram":
        raise Exception("Enter new name")
except Exception as e:
    print("Name already exists.",e)
else:
    print("Name is:",x)