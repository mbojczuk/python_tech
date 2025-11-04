from typing import Dict, Type, Any

class SingletonBase:
    _instances: Dict[Type, Any] = {} # this way we can keep track of all new singleton instances

    # keeps track of all singleton references
    def __new__(cls, *args, **kwargs):
        # checks if singletong is already present if its not...
        if cls not in cls._instances:
            # Create and store the instance
            instance = super().__new__(cls)
            cls._instances[cls] = instance
        # return the instance
        return cls._instances[cls]