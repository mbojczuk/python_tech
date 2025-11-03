from .base_test import BaseTest
from typing import Dict, Type

class TestRegister:
    _registery: Dict[str, Type[BaseTest]] = {}

    @classmethod
    def register(cls, test_cls: Type[BaseTest]) -> Type[BaseTest]:
        name = getattr(test_cls, "name", test_cls.__name__)
        if name in cls._registery:
            raise KeyError(f"Test already registered with name: {name}")
        cls._registery[name] = test_cls
        return test_cls