class Store:
    def __init__(self):
        self.item = input("Enter item name:")
        self.quantity = int(input("Enter quantity:"))
    def get_item(self):
        return self.item
    def get_quantity(self):
        return self.quantity
    def buy(self):
        self.bought = int(input("Enter no. of items to be bought:"))
        self.bs = self.bought + self.quantity
        return "Quantity after buying:%s"%(self.bs)
    def sell(self):
        self.sold = int(input("Enter no. of items sold:"))
        return "Quantity left after selling:%s"%(self.bs-self.sold)

p = Store()
print("Item:",p.get_item())
print("Quantity:",p.get_quantity())
print(p.buy())
print(p.sell())