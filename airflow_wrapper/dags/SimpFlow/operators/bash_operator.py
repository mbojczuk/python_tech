from airflow.operators.bash import BashOperator
from .base_operator import BaseOperatorWrapper
from dataclasses import dataclass, field

@dataclass
class BashOperatorWrapper(BaseOperatorWrapper):
    task_id: str
    bash_command: str

    def build(self) -> BashOperator:
        return BashOperator(
            task_id=self.task_id,
            bash_command=self.bash_command
        )