from datetime import date

class Employee:

    __slots__ = ("name", "age", "position", "_salary", "_annual_Salary")  # memory optimization by restricting attributes
    minimum_wage = 1500.0  # class variable shared across all instances

    # if we wanted to change the minimum wage at the class level instead of instance level we could use a class method
    # cls is short for class FYI
    # so this changes the minimum wage for all instances of the class
    @classmethod
    def set_minimum_wage(cls, new_wage: float) -> None:
        if new_wage  > 3000.0:
            raise ValueError("Minimum wage cannot exceed 3000.0")
        cls.minimum_wage = new_wage

    @classmethod
    def new_employee(cls, name: str, dob: date) -> 'Employee':
        now = date.today()
        age = now.year - dob.year - ((now.month, now.day) < (dob.month, dob.day))
        return cls(name, age, "Unknown", cls.minimum_wage)

    def __init__(self, name: str, age: int, position: str, salary: float):
        self.name = name
        self.age = age
        self.position = position
        # looks like a public attribute but it's actually protected using abstraction
        self.salary = salary
        self._annual_Salary = None  # private attribute for caching annual salary if needed

    def increase_salary(self, percent: int) -> None:
        self.salary += self.salary * (percent / 100)

    # print method for easy display when printing a class this will be called
    # think of it as toString in other languages and return a string representation of the object
    # like datetime's __str__ method will return the date in a readable format
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Position: {self.position}, Salary: ${self.salary}"
    
    # repr method for unambiguous representation of the object in order to recreate the object
    def __repr__(self):
        return f"Employee(name={repr(self.name)}, age={repr(self.age)}, position={repr(self.position)}, salary={repr(self.salary)})" #since salary is protected we access it via the property

    # makes it like a read only data attribute
    @property
    def salary(self) -> float:
        return self._salary
    
    # provide the functionality to set the salary with some validation
    @salary.setter
    def salary(self, new_salary: float) -> None:
        if new_salary < Employee.minimum_wage:
            raise ValueError(f"Salary must be at least {Employee.minimum_wage}")
        self._annual_Salary = None  # reset cached annual salary on salary change
        self._salary = new_salary
        
    # computed property to get annual salary which is calculated at runtime
    # also caches the value after first computation incase performance on subsequent accesses is needed
    @property
    def annual_salary(self) -> float:
        if self._annual_Salary is None:
            self._annual_Salary = self.salary * 12
        return self._annual_Salary


if __name__ == "__main__":
    emp = Employee("Alice", 30, "Developer", 70000)
    print(emp) # Display using __str__
    emp.increase_salary(10) # Increase salary by 10%
    print("After salary increase:") 
    print(emp) # Display using __str__
    print(repr(emp)) # Display using __repr__ which includes all details like how the constructor was called
    print(emp.salary)  # Accessing salary via property
    print(emp.annual_salary)  # Accessing annual salary via property computed attribute at runtime
    emp.salary = 2000  # Setting salary via property with validation
    print(emp.salary)
    print(emp.annual_salary)

    print(Employee.minimum_wage)  # Accessing class variable
    Employee.set_minimum_wage(2200.0)  # Changing class variable via class method
    print(Employee.minimum_wage)
    print(emp.minimum_wage)  # Accessing class variable via instance
    print(emp._annual_Salary)  # Accessing private attribute directly (not recommended)
    print(emp.salary)

    # factory function usage
    e = Employee.new_employee("Bob", date(1990, 5, 15))  # Creating new employee using alternative constructor
    print(e)