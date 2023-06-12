#Write your code here

class Container(ABC): 
    @abstractmethod
    def pack(self)  -> str:
        pass
    @abstractmethod
    def material(self) -> str:
        pass
    def describe(self):
        return f"Empaque: {self.pack()} , Material: {self.material()}"    
    
class Wrapping(Container):  
  #Write your code here
  pass

class Bottle(Container):  
  #Write your code here
  pass
      
class Glass(Container):  
  #Write your code here
  pass

class Box(Container):  
  #Write your code here
  pass