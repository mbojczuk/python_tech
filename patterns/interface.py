from abc import ABC, abstractmethod # Import ABC and abstractmethod for creating interface
from dataclasses import dataclass

@dataclass
class MyClass(ABC):
    _myprop: int

    def do_something(self, value):
        self._myprop *= value
    
    # implement abstract method
    @property
    @abstractmethod
    def some_property(self):
        return self._myprop

# Example subclass implementing the interface
@dataclass
class AnotherClass(MyClass):

    @property
    def some_property(self):
        return self._myprop * 2  # override property to return double the value
    
    def __str__(self):
        return f"_myprop={self._myprop}"
    
if __name__ == "__main__":
    obj = AnotherClass(10)
    print(obj.some_property)  # Should print 20
    obj.do_something(3)
    print(obj.some_property)  # Should print 60
    print(str(obj))