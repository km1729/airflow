This procedure can be useful for learning and exploration.  
이 도커파일은 포스트그래스, 웹서버, 스케쥴러, 익스큐터(로컬익스큐터)를 사용하며, 셀러리와 레디스는 사용하지 않는다.   

# docker-commpose.yaml 파일 수정
1. (Line 59) CeleryExecutor >> LocalExecutor  
2. comment out  
    - (Line 107-117) redis
    - (Line 151-171) Celery Worker

# Folder 생성 하고 Docker 실행 
```bash
mkdir ./dags ./logs ./plungs
echo -e "AIRFLOW_UID=$(id -u)" > .env #for linux

docker compose up airflow-init
docker compose up -d
```

# Airflow webserver 
- go to a web browser 
- http://localhost:8080/  
- id: airflow  
- pw: airflow  

> 여기까지 실행하면 예제가 설치되어 있는 에어플로우 컨테이너가 작동되는 것을 확인 할 수 있다

# Example dags 삭제
- 컨테이너들을 닫고 & 연결된 볼륨 제거
- `docker-compose down -v`
``` bash
[+] Running 7/7
 ✔ Container airflow-simpler-airflow-scheduler-1  Removed  3.2s 
 ✔ Container airflow-simpler-airflow-webserver-1  Removed  7.0s 
 ✔ Container airflow-simpler-airflow-triggerer-1  Removed  5.0s 
 ✔ Container airflow-simpler-airflow-init-1       Removed  0.2s 
 ✔ Container airflow-simpler-postgres-1           Removed  0.6s 
 ✔ Volume airflow-simpler_postgres-db-volume      Removed  0.1s 
 ✔ Network airflow-simpler_default                Removed  0.7s
 ```
- yaml 파일 수정 line 68 in docker-compose.yaml file  
`AIRFLOW__CORE__LOAD_EXAMPLES: 'true' >> 'false'`  
- docker run again by
``` bash
docker-compose up airflow-init
docker-compose up -d
```

# Reference  
- [Running Airflow in Docker](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html)
- [coder2j - Airflow Tutorial for Beginner 10:44](https://youtu.be/K9AnJ9_ZAXE)