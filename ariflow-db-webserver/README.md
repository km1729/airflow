# airflow

Install airflow with Docker-compose

Requirements:

- docker
- docker-compose

```bash
# 1. create a project folder
mkdir ./airflow

# 2. Docker-compose file download
curl -o docker-compose.yaml https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml


# 3. Create folders
mkdir ./dags ./plugins ./logs

# 4. create .env file
echo -e "AIRFLOW_UID=$(id -u)\nAIRFLOW_GID=0" > .env

# 5. Run airflow init
docker-compose up airflow-init

# 6. Run docker-compose
docker-compose up

# 7. Close running system
docker-compose down
```

Open a new terminal

```bash
# see  currently running containers
docker ps
'''
CONTAINER ID   IMAGE                  COMMAND                  CREATED          STATUS                    PORTS                                       NAMES
939a73031a3d   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   45 minutes ago   Up 45 minutes (healthy)   8080/tcp                                    airflow-docker_airflow-scheduler_1
54f8831bbb53   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   45 minutes ago   Up 45 minutes (healthy)   0.0.0.0:8080->8080/tcp, :::8080->8080/tcp   airflow-docker_airflow-webserver_1
80cf7c41e8e5   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   45 minutes ago   Up 45 minutes (healthy)   8080/tcp                                    airflow-docker_airflow-worker_1
e92cac8391d5   apache/airflow:2.5.1   "/usr/bin/dumb-init …"   45 minutes ago   Up 45 minutes (healthy)   8080/tcp                                    airflow-docker_airflow-triggerer_1
e53b40c01cbf   redis:latest           "docker-entrypoint.s…"   50 minutes ago   Up 50 minutes (healthy)   6379/tcp                                    airflow-docker_redis_1
45731cc22358   postgres:13            "docker-entrypoint.s…"   50 minutes ago   Up 50 minutes (healthy)   5432/tcp                                    airflow-docker_postgres_1
'''

# see airflow version
docker exec container_ID airflow version
2.5.0

```

Open a browser and type localhost:8080

![sbrowser](/docs/locahost.png)

Youtube tutorial  
[Running Airflow 2.0 with Docker in 5mins - Data with Marc](https://www.youtube.com/watch?v=ataytcxy2ck&ab_channel=datawithmarc)
