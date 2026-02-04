i = int(input("enter a number:"))
n = str(i)
l1 = list(n)
i = 0
j = len(l1)-1
is_armstrong = True
while i<j and i!=j:
    if l1[i] == l1[j]:
        print("True")
        i += 1
        j -= 1
    else:
        print("False")
        break


