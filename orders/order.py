from users import Cashier, Customer
from products.product import Product

"""
    Represents a purchase order made by a customer and handled by a cashier.
    An order contains a list of products and provides functionality to
    calculate and display the total price.
Args:
    cashier (Cashier): Cashier responsible for the order.
    customer (Customer): Customer who places the order.
"""
class Order:

  def __init__(self, cashier:Cashier, customer:Customer):
    self.cashier = cashier
    self.customer = customer
    self.products = []
  
  """
    Add a product to the order.
      Args:
         product (Product): Product to add to the order.
      Returns:
         None
  """
  def add(self, product : Product):
    # Append the new product to the list
    self.products.append(product)

  """
   Calculate the total price of all products in the order.
    Returns:
     float: Total price of the order.
  """
  def calculateTotal(self) -> float:
    # Init result total price
    total_price=0
    # iterate throught all the list
    for product in self.products:
        # Add the price for each product
        total_price += product.price
    # Return the total_price
    return total_price
  
  """
   Display the order details in the console.
    This includes:
      - Customer information
      - Cashier information
      - List of products
      - Total price formatted to two decimals
    Returns:
           None
  """
  def show(self):    
    print("Hello : "+self.customer.describe())
    print("Was attended by : "+self.cashier.describe())
    for product in self.products:
      print(product.describe())
    print(f"Total price : {self.calculateTotal():.2f}")
