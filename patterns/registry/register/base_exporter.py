from abc import ABC, abstractmethod
from .data_type import Data

class BaseExport(ABC):
    
    _format: str = "base"

    @property
    def format(self) -> str:
        return self._format  
          
    @abstractmethod
    def export_data(self, data: Data) -> None:
        pass
