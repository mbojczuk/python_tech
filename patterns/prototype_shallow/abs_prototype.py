from abc import ABC, abstractmethod
class AbsPrototype(ABC):
    @abstractmethod
    def clone(self):
        pass