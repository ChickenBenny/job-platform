from datetime import datetime, timedelta
from airflow.decorators import dag
from models.init_cake_pipline import init_cakeresume


default_args = {
    'owner': 'Benny',
    'start_date': datetime(2022, 9, 22),
    'schedule_interval': '@once',
    'retries': 5,
    'retry_delay': timedelta(minutes = 2)    
}

@dag(dag_id='cakeresume_init_backend',
     default_args = default_args,    
)
def cakeresume_init_backend():
    backend_init = init_cakeresume('back-end-engineer', 'backend_engineer')

init_job_backend = cakeresume_init_backend()

@dag(dag_id='cakeresume_init_data_engineer',
     default_args = default_args,    
)
def cakeresume_init_data_engineer():
    data_engineer_init = init_cakeresume('data-engineer', 'data_engineer')

init_job_data_engineer = cakeresume_init_data_engineer()

@dag(dag_id='cakeresume_init_data_scientist',
     default_args = default_args,    
)
def cakeresume_init_data_scientist():
    data_scientist_init = init_cakeresume('data-scientist', 'data_scientist')

init_job_data_scientist = cakeresume_init_data_scientist()

@dag(dag_id='cakeresume_init_ml_engineer',
     default_args = default_args,    
)
def cakeresume_init_ml_engineer():
    data_ml_init = init_cakeresume('machine-learning-engineer', 'ml_engineer')

init_job_ml_engineer = cakeresume_init_ml_engineer()

@dag(dag_id='cakeresume_init_qa_engineer',
     default_args = default_args,    
)
def cakeresume_init_qa_engineer():
    data_qa_init = init_cakeresume('qa-test-engineer', 'qa_engineer')

init_job_qa_engineer = cakeresume_init_qa_engineer()