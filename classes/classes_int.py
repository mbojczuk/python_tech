class Employee:

    __slots__ = ("name", "age", "salary")  # memory optimization by restricting attributes

    def __init__(self, name: str, age: int, salary: float):
        self.name = name
        self.age = age
        self.salary = salary

    def increase_salary(self, percent: float) -> None:
        self.salary += self.salary * (percent / 100)

class Tester(Employee):
    
    def _run_test(self):
        print(f"Running tests for {self.name}")

class SlotsInspectorMixin:
    def has_slots(self):
        return hasattr(self, '__slots__')

class Developer(Employee, SlotsInspectorMixin): # now with multiple inheritance

    # storing only specific attributes in memory for optimization
    # reduced memory overhead by preventing the creation of __dict__ for each instance
    __slots__ = ("framework")  # memory optimization by restricting attributes

    def __init__(self, name: str, age: int, salary: float, framework: str):
        super().__init__(name, age, salary)
        self.framework = framework

    # method overriding with additional bonus parameter which overides the method from the base class aka polymorphism
    # all you need to do is name the method the same as the base/parent class method
    def increase_salary(self, percent: float, bonus: float = 0.0) -> None:
        super().increase_salary(percent) # call the base class method to increase salary by percent
        # this way we can add extra functionality to the derived class method
        self.salary += bonus

if __name__ == "__main__":
    tester = Tester("Bob", 28, 60000)
    print(f"Before salary increase: Name: {tester.name}, Age: {tester.age}, Salary: {tester.salary}")
    tester.increase_salary(15)
    tester._run_test()

    developer = Developer("Charlie", 32, 80000, "Django")
    print(f"Before salary increase: Name: {developer.name}, Age: {developer.age}, Salary: {developer.salary}, Framework: {developer.framework}")
    developer.increase_salary(10, bonus=5000)
    print(f"After salary increase: Name: {developer.name}, Age: {developer.age}, Salary: {developer.salary}, Framework: {developer.framework}")

    print(developer.__slots__)

    print(developer.has_slots())  # True

    # print (repr(tester))
    # print (repr(developer))

    # print(isinstance(tester, Employee))  # True
    # print(isinstance(developer, Employee))  # True

    # print(issubclass(Tester, Employee))  # True
    # print(issubclass(Developer, Employee))  # True
    # # all classes in python inherit from object class implicitly
    # print(issubclass(Tester, object))  # True
    # print(issubclass(Developer, object))  # True


