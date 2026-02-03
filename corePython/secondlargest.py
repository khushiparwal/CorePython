def second_largest(l):
    largest = l[0]
    second_largest = l[1]
    n = len(l)
    for i in range(n):
        if l[i] > largest:
            second_largest = largest
            largest = l[i]
        if l[i]<largest and l[i]>second_largest:
            second_largest = l[i]
    return second_largest

l1 = [25,65,47,98,101,3,29]
print(second_largest(l1))