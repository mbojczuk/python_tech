from abc import ABC, abstractmethod
# Base Test Class

class BaseTest(ABC):
    def __init__(self, name: str):
        self.name = name

    # Property for name makes it like a read only data attribute
    @property   
    def name(self) -> str:
        return self._name
    
    # Provide the setter functionality
    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @name.getter
    def name(self) -> str:
        return self._name
    
    # this is an abstract method that must be implemented by subclasses
    @abstractmethod
    def run(self) -> str:
        raise NotImplementedError