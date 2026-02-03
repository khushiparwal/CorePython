l1 = [68,45,20,36,90]
max = l1[0]
i = 0
while i<len(l1):
    if l1[i] > max:
        max = l1[i]
    i += 1
print(max)