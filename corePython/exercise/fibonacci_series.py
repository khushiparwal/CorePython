def fib(n):
    a,b = 0,1
    f = []
    for i in range(n):
        f.append(a)
        a, b = b, a+b
    return f

n = int(input("enter a number:"))
print(fib(n))
