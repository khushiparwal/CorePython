class Insufficientbalance(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Amountlimitexceeded(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Transactionlimit(Exception):
    def __init__(self,msg):
        super().__init__(msg)

class Account:
    def __init__(self):
        self.count  = 0
        self.balance = 0
    def set_balance(self,b):
        self.balance = b
    def get_balance(self):
        return self.balance
    def deposit(self,amount):
        if self.count >= 3:
            raise Transactionlimit("No. of transactions exceeded.")
        self.count += 1
        self.balance += amount
        print(f"Deposited amount :{amount}, total balance:{self.balance}")
    def withdrawal(self,amount):
        if self.count >= 3:
            raise Transactionlimit("No. of transactions exceeded.")
        if amount > 50000:
            raise Amountlimitexceeded("Withdrawal limit of 50000 exceeded.")
        if self.balance - amount >= 2000:
            self.count += 1
            self.balance -= amount
            print(f"Withdrawal amount:{amount}, Total balance:{self.balance}")
        else:
            raise Insufficientbalance("Insufficient balance.Minimum balance in account should be 2000")

a1 = Account()
a1.set_balance(50000)
print("Balance:",a1.get_balance())
try:
    a1.deposit(2000)
    a1.withdrawal(3000)
    a1.deposit(5000)
    a1.withdrawal(51000)
except Insufficientbalance as e:
    print("Exception:",e)
except Amountlimitexceeded as l:
    print("Exception:",l)
except Transactionlimit as t:
    print("Exception:",t)

