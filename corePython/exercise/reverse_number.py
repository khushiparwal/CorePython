no = 153
n = no
remainder = 0
sum = 0

while n>0:
    remainder = n%10            #r = 3, s = 3, n = 150
    sum = (sum*10)+remainder    #r = 5, s=35,n=1
    n = n//10                   #r=1,s=351,n=0
print("reversed number is: ",sum)
