import threading
from threading import *

def hi(name):
    for i in range(1,11):
        print(name, i)

def hello(name):
    for i in range(1,11):
        print(name, i)

t1 = threading.Thread(target=hi,args=("Ram",))
t2 = threading.Thread(target=hello,args=("xyz",))
t1.start()
t2.start()
