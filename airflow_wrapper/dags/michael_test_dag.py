from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

def _my_python_task_callable(name):
    """A simple Python function to be called by PythonOperator."""
    print(f"Hello from Python, {name}!")

with DAG(
    dag_id='sample_test_dag',
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['boj'],
) as dag:
    start_task = BashOperator(
        task_id='start_task',
        bash_command='echo "Starting the DAG!"',
    )

    python_task = PythonOperator(
        task_id='python_task',
        python_callable=_my_python_task_callable,
        op_kwargs={'name': 'Airflow User'},
    )

    end_task = BashOperator(
        task_id='end_task',
        bash_command='echo "DAG finished successfully!"',
    )

    start_task >> python_task >> end_task