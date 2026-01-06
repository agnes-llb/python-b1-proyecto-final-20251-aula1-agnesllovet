from users import *
from products.product import *

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    #Write your code here
    self.products.append(product)

  def calculateTotal(self) -> float:
    #Write your code here
    total_price=0
    for product in self.products:
        total_price += product.price
    return total_price
  
  def show(self):    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total price : {self.calculateTotal():.2f}")
