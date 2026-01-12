from abc import ABC, abstractmethod

"""
    Abstract base class that represents a generic user of the system.
    This class defines common attributes and behavior shared by all users
    (such as Cashier and Customer).
"""
class User(ABC):
  def __init__(self,dni:str,name:str,age:int):
    self.dni = dni
    self.name = name
    self.age = age    
   
  @abstractmethod
  def describe(self):
      pass

"""
  Represents a cashier user.
    Inherits from User and adds specific attributes related to employment.
    Args:
        dni (str): National identification number.
        name (str): Cashier name.
        age (int): Cashier age.
        timeTable (str): Working timetable.
        salary (float): Cashier salary.    
    methode describe :
            str: Cashier description.
"""
class Cashier(User): 
  def __init__(self,dni:str,name:str,age:int,timeTable:str,salary:float):
    #Use the constructor for atributs commons from parent class
    super().__init__(dni,name,age)
    #Define the especific atributs for this class
    self.timeTable = timeTable
    self.salary = salary
  def describe(self)-> str:
        return (f"Cashier - Name: {self.name}, DNI: {self.dni}, Timetable: {self.timeTable}, Salary: {self.salary}.")


"""
  Represents a customer user.
    Inherits from User and adds specific attributes related to employment.
    Args:
        dni (str): National identification number.
        name (str): Cashier name.
        age (int): Cashier age.
        email (str): Customer email address.
        postalCode (str): Customer postal code.   
    methode describe :
            str: Cashier description.
"""
class Customer(User):
  def __init__(self,dni:str,name:str,age:int,email:str,postalCode:str):
    #Use the constructor for atributs commons from parent class
    super().__init__(dni,name,age)
    #Define the especific atributs for this class
    self.email = email
    self.postalCode = postalCode
  def describe(self)->str:
        return (f"Customer - Name: {self.name}, DNI: {self.dni} , Age: {self.age}, Email: {self.email}, Postal Code: {self.postalCode}")