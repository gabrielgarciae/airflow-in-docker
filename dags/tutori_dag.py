from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import requests
import json

def captura_conta_dados():
    url = "https://data.cityofnewyork.us/resource/rc75-m7u3.json"
    response = requests.get(url, verify=False)
    df = pd.DataFrame(json.loads(response.content))
    qtd = len(df.index)
    return qtd

def e_valida(ti): #se a quantidade tiver ok vai para task valida, se não estiver vai para nvalida
    qtd = ti.xcom_pull(task_ids = 'captura_conta_dados') #essa linha, pega informação da task captura_conta_dados (usa para comunicar informações entre tasks)
    if (qtd > 1000):
        return 'valido'
    return 'nvalido'


# a patir da meia noite do startdate mais 30 segundos do schedule, é que a dag será executada 
with DAG('tutori_dag', start_date = datetime(2023,3,6),
        schedule_interval = '30 * * * *', catchup=False)  as dag:
    
    #primeira task
    captura_conta_dados = PythonOperator(
        task_id = 'captura_conta_dados',
        python_callable = captura_conta_dados
    )

    #segunda task
    e_valida = BranchPythonOperator(
        task_id = 'e_valida',
        python_callable = e_valida
    )

    #terceira task
    valido = BashOperator(
        task_id = 'valido',
        bash_command = "echo, 'Quantidade OK'"
    )

    #quarta task
    nvalido = BashOperator(
        task_id = 'nvalido',
        bash_command = "echo, 'Quantidade nOK'"
    )
captura_conta_dados >> e_valida >> [valido, nvalido]
# mostrar a direção a seguir ao airflow, o que está em [] é como se fosse um if, seguir na direção de um id ou de outro