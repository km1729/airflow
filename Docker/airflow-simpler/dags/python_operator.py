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
def greet(ti):
    first_name = ti.xcom_pull(task_ids='get_name', key='first_name')
    last_name= ti.xcom_pull(task_ids='get_name',key='last_name')
    age = ti.xcom_pull(task_ids='get_age', key='age')
    
    print(f"Hello world. I'm {first_name} {last_name} and {age} years old")

def get_name(ti):
    ti.xcom_push(key='first_name', value='Tom')
    ti.xcom_push(key='last_name', value='Friday')

def get_age(ti):
    ti.xcom_push(key='age', value=19)

with DAG(
    default_args=default_args,
    dag_id='python_operator_v6',
    description='python operator test',
    start_date=datetime(2023,7,7,1),
    schedule_interval='@daily'

) as dag:
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet #python function
        # op_kwargs={'age':15}
    )
    task2 = PythonOperator(
        task_id='get_name',
        python_callable=get_name,
    )
    task3 = PythonOperator(
        task_id='get_age',
        python_callable=get_age
    )

    #task2를 먼저 실행해서 이름을 얻고, 그 결과를 task1에 전달한다
    [task2,task3] >> task1