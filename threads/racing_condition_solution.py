from time import sleep
from threading import *
import threading
from tkinter.font import names

class Account:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()
    def set_balance(self,b):
        sleep(1)
        self.balance = b
    def get_balance(self):
        sleep(1)
        return self.balance
    def deposit(self,amount):
        self.lock.acquire()
        bal = self.get_balance()
        self.set_balance(bal+amount)
        self.lock.release()


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
    t1.join()
    t2.join()
    print("Final balance: ",a1.get_balance())
main()