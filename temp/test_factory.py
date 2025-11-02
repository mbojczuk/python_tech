# Base Test Class
class BaseTest():
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

    def run(self) -> str:
        pass

    def __str__(self):
        return f"Test Name: {self.name}"


if __name__ == "__main__":
    test = BaseTest("Sample Test")  # This will raise an error since BaseTest is abstract
    print(test.name)
    print(test)