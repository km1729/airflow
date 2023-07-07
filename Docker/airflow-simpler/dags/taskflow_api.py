from airflow.decorators import dag, task
from datetime import datetime, timedelta

default_args = {
    'owner': 'kaycee',
    'retries': 5,
    'retry_delay': timedelta(minutes=5)
}

@dag(dag_id='taskflow_api_v02',
     default_args=default_args,
     start_date=datetime(2023, 7, 7),
     schedule_interval='@daily')
def hello_wrold_etl():

    @task(multiple_outputs=True)
    def get_name():
        return {
            'first_name':'Kaycee',
            'last_name':'Friday'
        }

    @task()
    def get_age():
        return 19
    
    @task()
    def greet(first_name, last_name, age):
        print(f"Hello World! I am {first_name} {last_name} and {age} years old")


    name_dict = get_name()
    age = get_age()
    greet(first_name=name_dict['first_name'],
          last_name=name_dict['last_name'],
          age=age)

greet_dag = hello_wrold_etl()