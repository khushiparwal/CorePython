class Addition:
    def add(self,a,b):
        return a+b
class Multiplication:
    def multiply(self,a,b):
        return a*b

class Operations(Addition, Multiplication):
    def divide(self,a,b):
        return a/b

d1 = Operations()
print("Sum:",d1.add(50,25))
print("Product:",d1.multiply(50,25))
print("Quotient:",d1.divide(50,25))
