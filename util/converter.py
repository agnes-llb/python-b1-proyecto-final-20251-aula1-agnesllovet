from abc import ABC, abstractmethod
import pandas as pd

#''' provisional per poder executar-ho'''
#import sys, os
#sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from users.user import Cashier, Customer
from products.product import Product, Hamburger, Soda, Drink, HappyMeal
from util.file_manager import CSVFileManager

class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, objects):
    for item in objects:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    #Write your code here
    #convertir dataframe a instancies d'objecte
    list_Cashiers = []
    for row in dataFrame.itertuples(False):
      list_Cashiers.append (Cashier (str(row.dni),str(row.name),int(row.age),row.timetable,float(row.salary)))
    return list_Cashiers

class CustomerConverter(Converter):
  def convert(self,dataFrame):   
    #Write your code here
    #convertir dataframe a instancies d'objecte
    list_Customers =[]
    for row in dataFrame.itertuples(False):
      list_Customers.append (Customer(str(row.dni),str(row.name),int(row.age), str(row.email),str(row.postalcode)))
    return list_Customers 

class ProductConverter(Converter):
   def convert(self, dataFrame:pd.DataFrame, ProductClass: type[Product]):
    list=[]
    for row in dataFrame.itertuples(False):
      list.append (ProductClass(str(row.id),str(row.name),float(row.price)))
    return list



"""
Function Read_CSV -> read a CSV file
Create a CSVFilemanager object and use the methode read to return
the information from file in a Dataframe    
Args:
   path (str) -> CSV file path (absolut) 
Returns:
   df (dataframe) -> DataFrame with the information from CSV file.   
"""
def Read_CSV (path: str) -> pd.DataFrame:
  df=CSVFileManager(path).read()
  return df

"""
cashiers_read_list : read the cashiers CSV file and convert the dataframe in a instance object list
Use "Read_CSV" function to have a dataframe with the cashiers information.
Create a obj cashierconverter -> Converts the dataframe to a list of cashier instances 
Use the methode convert to have a list of instances
Use the methode print to show the information from screen
Args:
    None
Returns:
    list_cashiers (list) : return a list of cashiers (instance). Every instance is a cashier object.  
"""
def cashiers_read_list () -> list:
     # Read CSV file
     df = Read_CSV ("data/cashiers.CSV")
     # Create object cashierconverter
     converter = CashierConverter ()
     # Use methode convert to have a list
     list_cashiers=converter.convert(df)
     # Use the methode print to show the information
     print ("Cashiers_List")
     converter.print(list_cashiers)
     # return the list of cashiers
     return list_cashiers

"""
customers_read_list : read the file customers CSV and convert the dataframe in a instance object list
Use the function Read_CSV to have a dataframe with the customer information.
Create a obj customerconverter -> Converts the dataframe to a list of customers instances 
Use the methode convert to have a list of instances
Use the methode print to show the information from screen
Args:
    None
Returns:
    list_customers (list) : return a list of customers (instance). Every instance is a customer object.  
"""
def customers_read_list () -> list:
    # Read CSV file    
     df = Read_CSV ("data/customers.csv")
     # Create object customerconverter
     converter = CustomerConverter ()
     # Use methode convert to have a list
     list_customers=converter.convert(df)
     # Use the methode print to show the information
     print ("Customer_List")
     converter.print(list_customers)
     # return the list of customer
     return list_customers


"""
products_read_list -> read all the products from CSV file and return a list of products
We have 4 kind of products to read from a 4 CSV and convert. To add or remove another file with more products
is just change deiccionary value. 
The products are define in a diccionary where key is the path and the value is the class of product
Use the function Read_CSV to have a dataframe with the product information.
Create a obj productconverter -> Converts the dataframe to a list of products instances 
Use the methode convert to have a list of instances
Use the methode print to show the information in screen
Args:
    None
Returns:
    list_products (list) : return a list of products (instance). Every instance is a product object.  
"""
def products_read_list () -> list:
     # define all the products available
     # key -> path  // value -> a class of product
     path_product = { "data/drinks.csv": Drink,
                      "data/hamburgers.csv": Hamburger,
                      "data/happyMeal.csv" : HappyMeal,
                      "data/sodas.csv" : Soda,
                     } 
     #Initialize the list where we put all the instances
     list_products=[]
     # Iterate through the diccionary keys 
     for path in path_product.keys():
        # Read CSV
        df = Read_CSV(path)
        # Create obj converter product
        converter = ProductConverter ()
        # Get the class for convert 
        product_class = path_product.get(path)
        # Use the methode with the correct class each iteration
        list_products += converter.convert(df,product_class)
     # Once all the files are read and convert
     # Print the information in screen
     print ("Product_List")
     converter.print(list_products)
     # Return the instance product list
     return list_products    

"""
print_list : prints information from a list of objects.
This function use the methode "describe" to get the information from object and print it
All the objects must have the methode "describe" as customer, cashier and all products 
Args:
    list (list) : a list with objects with the methode describe 
Returns:
    None
"""
def print_list (list: list):
     # Iteration through the list
     for item in list:
        # print the information from methode describe
        print(item.describe())


""" 
save_order_information_csv : save the information from order to a "orders_list.csv" file.
This function save the information from a list : dni_cashier, dni_customer, datetime, total price
Put the information with the headers in a dataframe.
Create a obj CSVFilemanager to use the methode write to save the information
Args:
    order_data (list) : a list with the information to save in file
Returns:    
    None
"""
def save_order_information_csv (order_data: list) :
    # define the headers for the file   
    headers = ["dni_cashier", "dni_customer",
               "datetime_order", "total_order" ]
    # Create the dataframe
    df = pd.DataFrame([order_data], columns=headers)
    # Create the obj CSVFilemanager with correct path
    csv_order = CSVFileManager ("data/Orders_list.csv")
    # Write the information
    csv_order.write (df)

 