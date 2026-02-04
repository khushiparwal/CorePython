notes = [500,200,100,50,20,10]
coin = [5,2,1]
amount = int(input("enter an amount:"))

n_count = 0
c_count = 0
for i in notes:
    n_count = amount//i
    if n_count >0:
        print(i,":",n_count)
    amount = amount%i
for j in coin:
    c_count = amount//j
    if c_count > 0:
        print(j,":",c_count)
    amount = amount % j
