n = int(input("enter a number:"))
no = n
sum = 0
rem = 0
while n!=0:
    rem = n%10
    sum = (sum*10)+rem
    n = n//10

if no == sum:
    print("number is palindrome")
else:
    print("number is not palindrome")
