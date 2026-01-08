from abc import ABC, abstractmethod
#Write your code here
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


'''Funcio Read_CSV 
Llegirà un fitxer csv indicat en el path 
retornarà in data frame'''
def Read_CSV (path: str):
  #obj_csv=CSVFileManager(path)
  df=CSVFileManager(path).read()
  return df

def cashiers_read_list () -> list:
     df = Read_CSV ("data/cashiers.CSV")
     converter = CashierConverter ()
     list=converter.convert(df)
     print ("Cashiers_List")
     converter.print(list)
     return list

def customers_read_list () -> list:
     df = Read_CSV ("data/customers.csv")
     converter = CustomerConverter ()
     list=converter.convert(df)
     print ("Customer_List")
     converter.print(list)
     return list



def products_read_list () -> list:
     
     path_product = { "data/drinks.csv": Drink,
                      "data/hamburgers.csv": Hamburger,
                      "data/happyMeal.csv" : HappyMeal,
                      "data/sodas.csv" : Soda,
                     } 
     list_products=[]
     for path in path_product.keys():
        df = Read_CSV(path)
        converter = ProductConverter ()
        product_class = path_product.get(path)
        list_products += converter.convert(df,product_class)
     print ("Product_List")
     converter.print(list_products)
     return list_products    

def print_list (list):
     #print(list)
     for item in list:
        print(item.describe())


def save_information_order_csv (order_data: list) :
    #    
    headers = ["dni_cashier", "dni_customer",
               "datetime_order", "total_order" ]
    df = pd.DataFrame([order_data], columns=headers)
    csv_order = CSVFileManager ("data/Orders_list.csv")
    csv_order.write (df)
    
    
''' comença el codi per provar els cashers 
pd_cash_obj=CSVFileManager("data/cashiers.csv")
print ("final funcio")
#pd=pd_cash_obj.read()
print (pd_cash_obj.read())
pd=pd_cash_obj.read()
print(type(pd))
'''
'''
list_Cashiers = []
for row in pd.itertuples(False):
  print (row)
  print(type(row))
  list_Cashiers.append (Cashier (str(row.dni),str(row.name),int(row.age),row.timetable,float(row.salary)))

print(list_Cashiers)
for list in list_Cashiers:
  print(list.describe())
'''
  
'''Posat els objectes en llista dels Customers '''
'''  llista de Customers
pd_customers=CSVFileManager("data/customers.csv")
print ("final funcio customers")
#pd=pd_cash_obj.read()
print (pd_customers.read())
pd1=pd_customers.read()

list_Customers =[]
#  def __init__(self,dni:str,name:str,age:int,email:str,postalCode:str):
for row in pd1.itertuples(False):
  print (row)
  print(type(row))
  list_Customers.append (Customer(str(row.dni),str(row.name),int(row.age), str(row.email),str(row.postalcode)))

print(list_Customers)
for list in list_Customers:
  print(list.describe())

llista de Customers '''

'''Posar els objectes en llista de productes - hamburguers '''
'''
pd_hamburgers=CSVFileManager("data/hamburgers.csv")
print ("funcio hamburgers")
#pd=pd_cash_obj.read()
print (pd_hamburgers.read())
pd=pd_hamburgers.read()

list_hamburgers =[]
#    def __init__(self,id:str,name:str,price:float):
for row in pd.itertuples(False):
  print (row)
  print(type(row))
  list_hamburgers.append (Hamburger(str(row.id),str(row.name),float(row.price)))

print(list_hamburgers)
for list in list_hamburgers:
  print(list.describe())
 '''

'''Posar els objectes en llista de productes - drinks '''
'''
pd_drinks=CSVFileManager("data/drinks.csv")
print ("funcio drinks")
#pd=pd_cash_obj.read()
print (pd_drinks.read())
pd=pd_drinks.read()

list_drinks =[]
#    def __init__(self,id:str,name:str,price:float):
for row in pd.itertuples(False):
  print (row)
  print(type(row))
  list_drinks.append (Drink(str(row.id),str(row.name),float(row.price)))

print(list_drinks)
for list in list_drinks:
  print(list.describe())
   '''

'''Posar els objectes en llista de productes - sodas '''
'''
pd_sodas=CSVFileManager("data/sodas.csv")
print ("funcio drinks")
#pd=pd_cash_obj.read()
print (pd_sodas.read())
pd=pd_sodas.read()

list_sodas =[]
#    def __init__(self,id:str,name:str,price:float):
for row in pd.itertuples(False):
  print (row)
  print(type(row))
  list_sodas.append (Soda(str(row.id),str(row.name),float(row.price)))

print(list_sodas)
for list in list_sodas:
  print(list.describe())

'''

'''Posar els objectes en llista de productes - happyMeal '''
'''
pd_happyMeal=CSVFileManager("data/happyMeal.csv")
print ("funcio happyMeal")
#pd=pd_cash_obj.read()
print (pd_happyMeal.read())
pd=pd_happyMeal.read()

list_happyMeal =[]
#    def __init__(self,id:str,name:str,price:float):
for row in pd.itertuples(False):
  print (row)
  print(type(row))
  list_happyMeal.append (HappyMeal(str(row.id),str(row.name),float(row.price)))

print(list_happyMeal)
for list in list_happyMeal:
  print(list.describe())

  '''