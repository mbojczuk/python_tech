from abc import ABC, abstractmethod
class AbsComputer(ABC):
    @abstractmethod
    def display(self):
        pass