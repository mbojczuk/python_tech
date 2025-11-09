from abc import ABC, abstractmethod
from airflow.models import BaseOperator
from dataclasses import dataclass

# Base class with abstract method build that all classes need to implement
@dataclass
class BaseOperatorWrapper(ABC):
    task_id: str
    namespace: str


    @abstractmethod
    def build(self) -> BaseOperator:
        """Return a Airflow operator"""
        raise NotImplementedError
    
