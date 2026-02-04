class Account:
    def __init__(self):
        self.number = None
        self.accType = ""
        self.balance = 0.0

    def set_number(self,n):
        self.number = n
    def get_number(self):
        return self.number
    def set_acctype(self,at):
        self.accType = at
    def get_acctype(self):
        return self.accType
    def set_balance(self,b):
        self.balance = b
    def get_balance(self):
        return self.balance

    def deposit(self,amount):
        return "Balance after deposit:%s"%(self.balance+amount)
    def withdraw(self,amount):
        if amount > self.balance:
            return "Insufficient amount in account"
        else:
            return "Balance after withdrawal:%s"%(self.balance-amount)

b1 = Account()
b1.set_number(101)
b1.set_acctype("Savings")
b1.set_balance(2500)
print(b1.get_balance())
print(b1.deposit(500))
print(b1.withdraw(1000))
