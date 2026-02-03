def largest(l1):
    n = len(l1)
    max = l1[0]
    for i in range(n):
        if l1[i] > max:
            max = l1[i]
    return max

l = [45,68,10,3,94,75,101]
print(largest(l))