from abc import ABC, abstractmethod
from typing import TypeVar
from users import *

T = TypeVar("T")
class Converter(ABC):
  @abstractmethod
  def convert(self,dataFrame,*args) -> list:
      pass  
  def print(self, listaObjetos):
    for item in listaObjetos:
      print(item.describe())

class CashierConverter(Converter):
  def convert(self,dataFrame):    
    cashiers = []
    for index, row in dataFrame.iterrows():      
      cashier = Cashier(str(row['dni']),row['name'],row['age'],row['timetable'],row['salary'])
      cashiers.append(cashier)
    return cashiers

class CustomerConverter(Converter):
  #Write your code here
  pass

class ProductConverter(Converter):
  def convert(self,dataFrame,T):    
    products = []
    for index, row in dataFrame.iterrows():      
      product = T(row['id'],row['name'],row['price'])
      products.append(product)
    return products