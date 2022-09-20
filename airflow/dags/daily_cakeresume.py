from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from models.daily_cake_pipline import daily_job_cakeresume


default_args = {
    'owner': 'Benny',
    'start_date': datetime(2022, 9, 18),
    'schedule_interval': '@daily',
    'retries': 5,
    'retry_delay': timedelta(minutes = 2)    
}

@dag(dag_id='daily_update_backend',
     default_args = default_args,    
)
def daily_cakeresume_backend():
    backend_daily = daily_job_cakeresume('back-end-engineer', 'backend_engineer')

daily_job_backend = daily_cakeresume_backend()

@dag(dag_id='daily_update_data_engineer',
     default_args = default_args,    
)
def daily_cakeresume_data_engineer():
    data_engineer_daily = daily_job_cakeresume('data-engineer', 'data_engineer')

daily_job_data_engineer = daily_cakeresume_data_engineer()

@dag(dag_id='daily_update_data_scientist',
     default_args = default_args,    
)
def daily_cakeresume_data_scientist():
    data_scientist_daily = daily_job_cakeresume('data-scientist', 'data_scientist')

daily_job_data_scientist = daily_cakeresume_data_scientist()

@dag(dag_id='daily_update_ml_engineer',
     default_args = default_args,    
)
def daily_cakeresume_ml_engineer():
    data_ml_daily = daily_job_cakeresume('machine-learning-engineer', 'ml_engineer')

daily_job_ml_engineer = daily_cakeresume_ml_engineer()

@dag(dag_id='daily_update_qa_engineer',
     default_args = default_args,    
)
def daily_cakeresume_qa_engineer():
    data_qa_daily = daily_job_cakeresume('qa-test-engineer', 'qa_engineer')

daily_job_qa_engineer = daily_cakeresume_qa_engineer()