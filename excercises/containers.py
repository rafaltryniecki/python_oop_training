from abc import ABC, abstractmethod
from typing import List
from dependency_injector import containers, providers
from dependency_injector.wiring import inject, Provide

import pandas as pd


class FileReaderInterface(ABC):
    
    @abstractmethod
    def applies_to(self) -> List[str]:
        pass
    
    @abstractmethod
    def read(self, path: str) -> str:
        pass
    
    
class CsvReader(FileReaderInterface):

    def applies_to(self) -> List[str]:
        return ['csv']
    
    def read(self, file_location: str) -> pd.DataFrame:
        return pd.read_csv(file_location)


class ExcelReader(FileReaderInterface):
    
    def applies_to(self) -> List[str]:
        return ['xls', 'xlsx', 'xlsm']
    
    def read(self, file_location: str) -> pd.DataFrame:
        return pd.read_excel(file_location)
      
    
class FileReaderFactory():
    
    def __init__(self, readers: List[FileReaderInterface]):
        self.readers = readers


    def get_reader(self, readerType:str) -> FileReaderInterface:
        readers = [reader for reader in self.readers if readerType in reader.applies_to()]
        return readers[0]
    
class FilePathReader():
    
    def __init__(self, factory: FileReaderFactory):
        self.factory = factory
        
        
    def read_file_path(self, path: str):
        reader = self.factory.get_reader(path.split('.')[-1])
        return reader.read(path)



class Container(containers.DeclarativeContainer):
    
    csvReader = providers.Factory(CsvReader)
    excelReader = providers.Factory(ExcelReader)
    
    fileReaderFactory = providers.Factory(FileReaderFactory, readers=[csvReader(), excelReader()])
    filePathReader = providers.Factory(FilePathReader, factory=fileReaderFactory)
    
@inject
def main(filePathReader:FilePathReader = Provide[Container.filePathReader]):
    result = filePathReader.read_file_path('file.csv')

    
if __name__ == '_main_':
    container = Container()
    container.wire(modules=[__name__])
    main()