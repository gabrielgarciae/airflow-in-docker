# airflow_docker

### Para subir um container com o airflow faça:

1. Precisa criar um diretório, inseir o arquivo yaml do airflow.
2. Criar três pastas no mesmo diretório que serão os volumes: dags, logs e plugins
3. Depois no cmd, rodar: docker-compose up airflow-init, vai instalar a imagem.
4. Depois puxar um novo cmd, mesmo diretório e dar um docker-compose up
5. Puxar um browser localhost:8080, usuario e senha é airflow

yaml: https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml
