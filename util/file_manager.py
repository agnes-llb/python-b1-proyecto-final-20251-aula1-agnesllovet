import pandas as pd
import os

"""
    CSVFileManager provides basic functionality to read from and write 
    to CSV files using pandas DataFrames.
"""
class CSVFileManager:
  def __init__(self,path: str):
    # Use function for convert path to lowercase to avoid any mismatch
    self.path = path.lower()

  """
      Reads a CSV file and returns its contents as a pandas DataFrame.
      This method checks that the file has a '.csv' extension and that
      the file exists before reading it.
      Raises:
            ValueError: If the file does not have a '.csv' extension.
            FileNotFoundError: If the file does not exist.
      Returns:
            pd.DataFrame: Data read from the CSV file.
  """
  def read(self) -> pd.DataFrame:
        # Check that path contents the properly extension
        # If not create a exception
        if not self.path.endswith (".csv"):
            raise ValueError (f"The file : {self.path} is not a CSV")
        # Check file exist
        # If not create a exception
        if not os.path.exists (self.path):
            raise FileNotFoundError (f"The file : {self.path} not exist")
        # Read the file and retorn a dataframe
        return pd.read_csv(self.path) 


  """
      Writes a pandas DataFrame to a CSV file.
      If the file already exists, the data is appended.
      If the file does not exist, it is created and the header is written.
      Args:
         dataFrame (pd.DataFrame): DataFrame to be written to the CSV file.
      Raises:
          ValueError: If the file does not have a '.csv' extension.
  """
  def write(self,dataFrame: pd.DataFrame):
        # Check that path contents the properly extension
        # If not create a exception
        if not self.path.endswith (".csv"):
            raise ValueError (f"The file : {self.path} is not a CSV")
        # Check if the file exist to knos if we have to save header or not
        file_exist= os.path.exists(self.path)
        # save df to csv file with appropiate mode, not include index
        # save the column names(header) only first time  
        dataFrame.to_csv(self.path, mode="a",
                     index=False, header= not file_exist)




