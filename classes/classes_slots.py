import sys

# Without slots
class EmployeeNoSlots:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# With slots
class EmployeeWithSlots:
    __slots__ = ('name', 'age', 'salary')
    
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

# Create instances
emp1 = EmployeeNoSlots("John", 30, 50000)
emp2 = EmployeeWithSlots("John", 30, 50000)

# Compare memory usage
print(f"Without slots: {sys.getsizeof(emp1.__dict__)} bytes")
print(f"With slots: {sys.getsizeof(emp2)} bytes")



# timing of __slots__ vs normal attribute access
import timeit

def access_with_slots():
    dev = EmployeeWithSlots("Charlie", 32, 80000)
    return dev.salary

def access_without_slots():
    emp = EmployeeNoSlots("Charlie", 32, 80000)
    return emp.salary

# Measure access times
slots_time = timeit.timeit(access_with_slots, number=1000000)
no_slots_time = timeit.timeit(access_without_slots, number=1000000)

print(f"Access time with slots: {slots_time:.6f} seconds") #0.08
print(f"Access time without slots: {no_slots_time:.6f} seconds") #0.09


# Use __slots__ when:

# You need to create many instances of a class
# The attributes are fixed and known
# Memory usage is a concern
# You want to prevent accidental attribute addition