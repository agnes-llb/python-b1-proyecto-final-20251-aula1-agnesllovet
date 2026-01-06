import pandas as pd
import os

class CSVFileManager:
  def __init__(self,path: str):
    self.path = path.lower()

  def read(self) -> pd.DataFrame:
    if not self.path.endswith (".csv") :
        raise ValueError (f"The file : {self.path} is not a CSV")
    if not os.path.exists (self.path):
        raise FileNotFoundError (f"The file : {self.path} not exist")
    return pd.read_csv(self.path) 


  def write(self,dataFrame: pd.DataFrame):
    if not self.path.endswith (".csv") :
        raise ValueError (f"The file : {self.path} is not a CSV")
    if not os.path.exists (self.path):
        raise FileNotFoundError (f"The file : {self.path} not exist")    
    dataFrame.to_csv(self.path, index=False)




