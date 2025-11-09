from airflow.operators.bash import BashOperator
from .base_operator import BaseOperatorWrapper
from dataclasses import dataclass, field

@dataclass
class BashOperatorWrapper(BaseOperatorWrapper):
    bash_command: str

    def __post_init__(self):
        super().__init__()

    def with_cmd(self) -> 'BashOperatorWrapper':
        return self.bash_command


    def build(self) -> BashOperator:
        operator_kwargs = {
            "name": self.task_id,
            "task_id": self.task_id
        }
        return BashOperator(
            task_id=self.task_id,
            bash_command=self.bash_command
        )