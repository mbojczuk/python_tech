from importlib import import_module
from inspect import getmembers, isclass, isabstract
from .car_factory import CarFactory

def load_factory(factory_name: str) -> CarFactory:
    try:
        factory_module = import_module('.' + factory_name, 'factories') # Import the factory module dynamically
    except ImportError as e:
        raise ImportError(f"Factory module '{factory_name}' could not be found.") from e
    
    # looks for  a class to return that is a subclass of CarFactory
    classes = getmembers(factory_module, lambda m: isclass(m) and not isabstract(m))
    
    # Find and return the factory class
    for _, _class in classes:
        if issubclass(_class, CarFactory):
            return _class()  # Instantiate and return the factory class