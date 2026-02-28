class Item:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def calc(self):
         return self.price * self.quantity
item1=Item("lidnt",100)
item2=Item("ferrero",200)
item1.quantity=2
item2.quantity=4
print(item1.calc())
print(item2.calc())


