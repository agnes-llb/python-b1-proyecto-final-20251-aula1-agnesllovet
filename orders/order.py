from users import *
from products.product import *

class Order:
  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []

  def add(self, product : Product):
    # Append the new product to the list
    self.products.append(product)

  def calculateTotal(self) -> float:
    # Init result total price
    total_price=0
    # iterate throught all the list
    for product in self.products:
        # Add the price for each product
        total_price += product.price
    # Return the total_price
    return total_price
  
  def show(self):    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total price : {self.calculateTotal():.2f}")
