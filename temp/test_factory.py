from dataclasses import dataclass
from abc import ABC, abstractmethod
# Base Test Class
@dataclass
class BaseTest(ABC):
    name: str
    # Property for name makes it like a read only data attribute

    @property
    def name(self) -> str:
        return self._name
    
    # Provide the setter functionality
    @name.setter
    def name(self, value: str) -> None:
        self._name = value

    @abstractmethod
    def run(self) -> str:
        raise NotImplementedError

class DBT_test(BaseTest):

    def run(self) -> str:
        return f"Running DBT test: {self.name}"

if __name__ == "__main__":
    test = DBT_test("SampleTest")
    print(f"Test Name: {test.name}")