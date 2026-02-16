from time import sleep
from threading import *
import threading
from tkinter.font import names

class Account:
    def __init__(self):
        self.balance = 0
    def set_balance(self,b):
        sleep(1)
        self.balance = b
    def get_balance(self):
        sleep(1)
        return self.balance
    def deposit(self,amount):
        bal = self.get_balance()
        self.set_balance(bal+amount)

class Racing(Thread):
    def __init__(self, account:Account, name):
        super().__init__()
        self.account = account
        self.name = name
    def run(self):
        for i in range(5):
            self.account.deposit(200)
            print(self.name, self.account.get_balance())

def main():
    a1 = Account()
    t1 = Racing(a1, 'abc')
    t2 = Racing(a1, 'xyz')
    t1.start()
    t2.start()
main()