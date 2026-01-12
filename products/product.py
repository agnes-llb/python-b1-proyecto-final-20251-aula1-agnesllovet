from abc import ABC, abstractmethod
# Import from module "food_package.py" the objects used in this module
from products.food_package import FoodPackage, Wrapping, Bottle, Glass, Box
"""
    Abstract base class that represents a generic Product of the system.
    This class defines common attributes and behavior by all products
    (hamburguer, drinks, happymeal, sodas).
"""
class Product(ABC):
    def __init__(self,id:str,name:str,price:float):
      self.id = id
      self.name = name
      self.price = price     
    
    def describe(self) -> str:
        return f"Product - Type: {self.type()}, Name: {self.name}, Id: {self.id} , Price: {self.price} , {self.foodPackage().describe()}."   
    
    @abstractmethod
    def type(self) -> str:
        pass
    @abstractmethod
    def foodPackage(self)->FoodPackage:
        pass  
"""
  Represents a hamburg product.
    Inherits from Products and adds specific attributes related to employment.
    Args:
        id (str): identification product.
        name (str): product name.
        price (int): price product. 
    methode type :
            str: description of product.
    methode foodPackage :
            Wrapping() -> a classe of food package      
"""
class Hamburger(Product):
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Hamburguer"
    def foodPackage(self) -> FoodPackage:
        return Wrapping()
"""
  Represents a soda product.
    Inherits from Products and adds specific attributes related to employment.
    Args:
        id (str): identification product.
        name (str): product name.
        price (int): price product. 
    methode type :
            str: description of product.
    methode foodPackage :
            Bottle() -> a classe of food package      
"""       
class Soda(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Soda"
    def foodPackage(self) -> FoodPackage:
        return Bottle()   
"""
  Represents a drink product.
    Inherits from Products and adds specific attributes related to employment.
    Args:
        id (str): identification product.
        name (str): product name.
        price (int): price product. 
    methode type :
            str: description of product.
    methode foodPackage :
            Glass() -> a classe of food package      
"""
class Drink(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "Drink"
    def foodPackage(self) -> FoodPackage:
        return Glass()
"""
  Represents a happy meal product.
    Inherits from Products and adds specific attributes related to employment.
    Args:
        id (str): identification product.
        name (str): product name.
        price (int): price product. 
    methode type :
            str: description of product.
    methode foodPackage :
            Box() -> a classe of food package      
"""
class HappyMeal(Product):
    #Write your code here
    def __init__(self,id:str,name:str,price:float):
        super().__init__(id,name,price)
    def type(self) -> str:
        return "HappyMeal"
    def foodPackage(self) -> FoodPackage:
        return Box()   
