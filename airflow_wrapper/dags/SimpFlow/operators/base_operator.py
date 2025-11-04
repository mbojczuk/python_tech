from abc import ABC, abstractmethod
from airflow.models import BaseOperator

# Base class with abstract method build that all classes need to implement
class BaseOperatorWrapper(ABC):

    @abstractmethod
    def build(self) -> BaseOperator:
        """Return a Airflow operator"""
        raise NotImplementedError
    
