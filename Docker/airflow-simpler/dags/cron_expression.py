from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'kaycee',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='cron_expression_v02',
    default_args=default_args,
    description='catchup and backfill function',
    start_date=datetime(2023,7,1),
    # cron expression
    schedule_interval='1 2 * * *'

) as dag:
    task1 = BashOperator(
        task_id = 'task1',
        bash_command="echo 12:00 pm"
    )
    task1

