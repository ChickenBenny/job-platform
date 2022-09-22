from datetime import datetime, timedelta
from airflow.decorators import dag
from models.init_yourator_pipline import init_yourator

default_args = {
    'owner': 'Benny',
    'start_date': datetime(2022, 9, 22),
    'schedule_interval': '@once',
    'retries': 5,
    'retry_delay': timedelta(minutes = 2)    
}

@dag(dag_id='yourator_init_backend',
     default_args = default_args,    
)
def yourator_init_backend():
    backend_init = init_yourator('backend_engineer', 'backend_engineer')

init_job_backend = yourator_init_backend()

@dag(dag_id='yourator_init_data_engineer',
     default_args = default_args,    
)
def yourator_init_data_engineer():
    data_engineer_init = init_yourator('data_engineer', 'data_engineer')

init_job_data_engineer = yourator_init_data_engineer()

@dag(dag_id='yourator_init_qa_engineer',
     default_args = default_args,    
)
def yourator_init_qa_engineer():
    data_qa_init = init_yourator('qa_engineer', 'qa_engineer')

init_job_qa_engineer = yourator_init_qa_engineer()