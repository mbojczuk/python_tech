from base_operator import BaseOperatorWrapper
from airflow.providers.cncf.kubernetes.operators.pod import KubernetesPodOperator
from dataclasses import dataclass

@dataclass
class KubernetesPodWrapper(BaseOperatorWrapper):
    task_id: str
    namespace: str


def build(self) -> KubernetesPodOperator:
    return KubernetesPodOperator(
        task_id = self.task_id,
        namespace=self.namespace
    )