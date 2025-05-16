# ABC package enables us to create blueprints for classes. 
# Classes that inherit from ABC cannot be directily instatiated 
# - instead, they tell other classes that inherit from them, which methods must be implemented
import pandas as pd
from abc import ABC, abstractmethod


class ReaderClass(ABC):
    @abstractmethod
    def read_file(self,):
        pass

# In the example above, ReaderClass is a blueprint for other classes, and each class that inherits from it
# must implement reader_file method. For example, below we will define excel reader

class ExcelReader(ReaderClass):
    def read_file(self, file_location: str) -> pd.DataFrame:
        return pd.read_excel(file_location)
    
# Now, in similar fashion define CSVReader, for reading data from csvs. Pandas method you'll need is pd.read_csv
        