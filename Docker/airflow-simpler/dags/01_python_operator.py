from airflow import DAG
from datetime import datetime, timedelta
# select an operator
from airflow.operators.python import PythonOperator


default_args = {
    'owner': 'kaycee',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

#python code
def greet(name, age):
    print(f"Hello world. I'm {name} and {age} years old")

with DAG(
    default_args=default_args,
    dag_id='python_operator_v2',
    description='python operator test',
    start_date=datetime(2023,7,7,1),
    schedule_interval='@daily'

) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet, #python function
        op_kwargs={'name':'tom', 'age':15}
    )