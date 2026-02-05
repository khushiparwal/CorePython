class Bank:
    def __init__(self,accno=0,acctype=''):
        self.accno = accno
        self.acctype = acctype
    def get_accno(self):
        return self.accno
    def get_acctype(self):
        return self.acctype

class Withdraw(Bank):
    def __init__(self,balance=0,amount=0,accno=0,acctype=''):
        self.balance = balance
        self.amount = amount
        super().__init__(accno, acctype)
    def get_balance(self):
        return self.balance
    def get_amount(self):
        return self.amount
    def withdrawal(self):
        self.b = self.balance-self.amount
        return "Balance after withdrawal:%s"%self.b

class Depositing(Bank):
    def __init__(self,balance=0,amount=0,accno=0,acctype=''):
        self.balance = balance
        self.amount = amount
        super().__init__(accno, acctype)
    def get_balance(self):
        return self.balance
    def get_amount(self):
        return self.amount
    def deposit(self):
        self.b = self.balance+self.amount
        return "Balance after deposit:%s"%self.b

w1 = Withdraw(500,200,2,'Savings')
print("Withdrawal")
print("Account no:",w1.get_accno())
print("Account type:",w1.get_acctype())
print("Balance before withdrawal:",w1.get_balance())
print("Amount to withdraw:",w1.get_amount())
print(w1.withdrawal())
print('\n')
d1 = Depositing(1000,500,3,'Savings')
print("Deposit")
print("Account no:",d1.get_accno())
print("Account type:",d1.get_acctype())
print("Balance before depositing:",d1.get_balance())
print("Amount to deposit:",d1.get_amount())
print(d1.deposit())