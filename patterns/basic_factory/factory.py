""" 
Factory pattern example:
 - Creational pattern
 - Defines interface for creating an object
 - Lets subclasses decide which object to build
 - Defers instance creation to subclasses
 - AKA Virtual Constructor
"""
import cars  # import cars package to register car classes
from inspect import getmembers, isclass, isabstract

# The Factory class to create car instances
class AutoFactory(object):
    cars = {}

    def __init__(self):
        self._register_cars()

    def _register_cars(self):
        classes = getmembers(cars, lambda m: isclass(m) and not isabstract(m))
        print(classes)
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, cars.CarBase):
                self.cars.update([[name, _type]])

    def create_instance(self, carname):
        if carname in self.cars:
            return self.cars[carname]()
        raise ValueError(f"Car '{carname}' not found in factory.")