class Employee:
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
        if new_salary < 1000.0:
            raise ValueError("Salary must be at least 1000.0")
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