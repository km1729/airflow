from airflow import DAG
from datetime import datetime, timedelta

from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'kaycee',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


with DAG(
    dag_id='catchup_backfill_v03',
    default_args=default_args,
    description='catchup and backfill function',
    start_date=datetime(2023,6,1,1),
    schedule_interval='@daily',
    # catchup 기능 True로 설정
    catchup=False

# 대그에서 실행하는 타스크
) as dag:
    task1 = BashOperator(
        task_id = 'catuchup',
        bash_command="echo HELLO WORLD , this is my catuch up"
    )

