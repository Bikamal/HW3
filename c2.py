# Write a class called Product. 
# The class should have ﬁelds called name, amount, and price.
#  There should be a method get_price that receives the number of items to be bought and returns
#  a the cost of buying that many items, where the regular price is charged for orders of less than 10 items,
#  a 10% discount is applied for orders of between 10 and 99 items, and a 20% discount is applied for orders of 
# 100 or more items. There should also be a method called make_purchase that receives the number of items to be
#  bought and decreases amount by that much.

class Product():
    def __init__(self,name,amount,price):
        self.name=name
        self.amount=amount
        self.price=price
    def get_price(self):
        
            return 'regular price :', self.amount*self.price
        
    def make_purchase(self):
        if self.amount<10:
            return 'price with discount:', self.amount*self.price
        elif self.amount>+10 and self.amount<=99:
            return 'price with discount:',(self.amount*self.price)- ((self.amount*self.price)/10)
        elif self.amount>=100:
            return 'price with discount:',(self.amount*self.price)- ((self.amount*self.price)/5)

n=input("name of item")
a=int(input("amount of item"))
p=int(input("price"))

k= Product(n,a,p)
print(k.get_price())
print(k.make_purchase())