# airflow_docker

6 SEÇÃO DOCKER COMPOSE

É uma ferramenta para rodar multiplos containers, para projetos de vários containers. Roda multiplos builds e runs 

#remover containers
docker-compose down
#Remover volumes
docker volume prune

Variavies de ambiente, quando você cria um arquivo env separado, geralmente para guardar senhas e passa o caminho do ambiente no seu código

docker-compose ps (lista)

Para rodar o airflow: 
1- Precisa criar um diretório, inseir o arquivo yaml do airflow. 
2- Criar três pastas no mesmo diretório que serão os volumes: dags, logs e plugins

yaml: https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml

Depois no cmd, rodar: docker-compose up airflow-init, vai instalar a imagem.
Depois puxar um novo cmd, mesmo diretório e dar um docker-compose up
Puxar um browser localhost:8080, usuario e senha é airflow
