from datetime import datetime, timedelta
from airflow.decorators import dag
from models.daily_yourator_pipline import daily_job_yourator

default_args = {
    'owner': 'Benny',
    'start_date': datetime(2022, 9, 22),
    'schedule_interval': '@daily',
    'retries': 5,
    'retry_delay': timedelta(minutes = 2)    
}

@dag(dag_id='yourator_daily_backend',
     default_args = default_args,    
)
def yourator_daily_backend():
    backend_daily = daily_job_yourator('backend_engineer', 'backend_engineer')

daily_job_backend = yourator_daily_backend()

@dag(dag_id='yourator_daily_data_engineer',
     default_args = default_args,    
)
def yourator_daily_data_engineer():
    data_engineer_daily = daily_job_yourator('data_engineer', 'data_engineer')

daily_job_data_engineer = yourator_daily_data_engineer()

@dag(dag_id='yourator_daily_qa_engineer',
     default_args = default_args,    
)
def yourator_daily_qa_engineer():
    data_qa_daily = daily_job_yourator('qa_engineer', 'qa_engineer')

daily_job_qa_engineer = yourator_daily_qa_engineer()