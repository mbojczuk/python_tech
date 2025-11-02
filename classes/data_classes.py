from dataclasses import dataclass

# dataclass for composition example has all the boilerplate code automatically generated
# can still add methods, classmethods, slots, etc.
@dataclass(slots=True) # using slots for memory optimization 3.10+python
class Project:
    name: str
    payment: float
    client: str

class Employee:
    def __init__(self, name: str, age: int, salary: float, project: Project):
        self.name = name
        self.age = age
        self.salary = salary
        self.project = project # composition relationship not an is a relationship, this is has a relationship

    def __str__(self):
        return f"Employee(name={self.name}, age={self.age}, salary={self.salary}, project={self.project})"

p = Project("AI Development", 150000.0, "TechCorp")
e = Employee("Alice", 30, 90000.0, p)
print(e.project)  # Output: Project(name='AI Development', payment=150000.0, client='TechCorp')