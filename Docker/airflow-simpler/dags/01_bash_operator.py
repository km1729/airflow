from airflow import DAG
from datetime import datetime, timedelta
# select an operator
from airflow.operators.bash import BashOperator

# 기본정보 (작성자, 대그를 다시 시도할 횟수 및 다시 시도를 위한 대기시간)
default_args = {
    'owner': 'kaycee',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

# dag 정보 (이름, 설명+기본정보, 시작날짜, 재시작 타이밍)
# dag id 를 변경하면서 기존의 대그는 두고 새로운 대그를 추가할 수 있다
with DAG(
    dag_id='first_dag_v4',
    default_args=default_args,
    description='my first dag for testing',
    start_date=datetime(2023,7,7,1),
    schedule_interval='@daily'

# 대그에서 실행하는 타스크
) as dag:
    task1 = BashOperator(
        task_id = 'first-task',
        bash_command="echo HELLO WORLD , this is my first task"
    )

    task2 = BashOperator(
        task_id='second-task',
        bash_command="echo HELLO WORLD  2"
    )

    task3 = BashOperator(
        task_id='third-task',
        bash_command="echo HELLO WORLD 3"
    )

# 종속성 설정
    # task1.set_downstream(task2)
    # task1.set_downstream(task3)

    # task1 >> task2
    # task1 >> task3

    task1 >> [task2, task3]
