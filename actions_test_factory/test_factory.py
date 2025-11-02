import tests
from inspect import getmembers, isclass, isabstract
from typing import Dict
from tests.base_test import BaseTest

# The Factory class to create test instances
class TestFactory(object):
    # Registry of test name to test class mappings, name and base class
    _test_registry: Dict[str, type[BaseTest]] = {}

    def __init__(self):
        self._register_tests()

    # Property to access the test registry which is read only protected
    @property
    def registry(self) -> Dict[str, type[BaseTest]]:
        return dict(self._test_registry)

    @classmethod
    def _register_tests(cls) -> None:
        # Get all non-abstract classes from tests module
        classes = getmembers(tests, lambda m: isclass(m) and not isabstract(m))
        
        # Register classes that are subclasses of BaseTest
        for name, test_class in classes:
            if isclass(test_class) and issubclass(test_class, tests.BaseTest):
                test = getattr(test_class, "name", name)
                cls._test_registry[test] = test_class

    # Create test instance by name
    @classmethod
    def create_instance(cls, testname: str) -> BaseTest:
        if testname in cls._test_registry:
            return cls._test_registry[testname]()
        raise ValueError(f"Test '{testname}' not found in factory.")
    
    @classmethod
    def available(cls) -> list:
        return list(cls._test_registry.keys())