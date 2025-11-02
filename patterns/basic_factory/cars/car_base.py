from dataclasses import dataclass
from abc import ABC, abstractmethod
# This is the abstract base class defining the interface
@dataclass
class CarBase(ABC):
    make: str
    model: str

    @abstractmethod
    def start(self) -> str:
        raise NotImplementedError
    
    @abstractmethod
    def stop(self) -> str:
        raise NotImplementedError