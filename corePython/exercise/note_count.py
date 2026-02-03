notes = [500,200,100,50,20,10]
amount = 65340

count = 0
for i in notes:
    count = amount//i
    if count >0:
        print(i,":",count)
    amount = amount%i