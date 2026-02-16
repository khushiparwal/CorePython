import threading
from threading import *
class Hi(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        for i in range(1,11):
            print(self.name,i)

h = Hi("Khushi")
h.start()
