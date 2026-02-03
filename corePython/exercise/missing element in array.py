a = [5,10,15,20,25]
b = [5,15,20,25]
for i in range(len(a)):
    if a[i] not in b:
        print(a[i])