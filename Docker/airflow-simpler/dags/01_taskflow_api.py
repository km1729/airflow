from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'kaycee',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='taskflow_api_v01',
     default_args=default_args,
     start_date=datetime(2023, 7, 7),
     schedule_interval='@daily')
def hello_wrold_etl():
    @task()
    def get_name():
        return 'Kaycee'

    @task()
    def get_age():
        return 19
    
    @task()
    def greet(name, age):
        print(f"Hello World! I am {name} and {age} years old")


    name = get_name()
    age = get_age()
    greet(name=name,age=age)

greet_dag = hello_wrold_etl()