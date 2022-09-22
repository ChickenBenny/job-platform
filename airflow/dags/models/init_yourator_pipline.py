from airflow.decorators import dag, task
import pandas as pd
import requests
from models.yourator_get_job_data import get_job_data
from models.insert_into_db import insert_into_db

POSTGRES_CONN_ID = 'job_database'

information = {
    "data_engineer": "%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%20%2F%20%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92",
    "backend_engineer": "%E5%BE%8C%E7%AB%AF%E5%B7%A5%E7%A8%8B",
    "qa_engineer": "%E6%B8%AC%E8%A9%A6%E5%B7%A5%E7%A8%8B"
}

def init_yourator(type, table):

    @task
    def get_url():
        url_datas = []
        url = f'https://www.yourator.co/api/v2/jobs?category[]={information[type]}&tag[]=Python&sort=recent_updated'
        url_datas.append(url)
        page = 2
        while True:
            url = f'https://www.yourator.co/api/v2/jobs?category[]={information[type]}&tag[]=Python&sort=recent_updated&page={page}'
            response = requests.get(url)
            response = response.json()
            if response['jobs']:
                url_datas.append(url)
                page += 1
            else:
                break
        return {'content': url_datas}    

    @task
    def get_data(url_datas):
        data = get_job_data(url_datas['content'])
        return {'content': data}
    
    @task
    def process_data(data):
        df = pd.DataFrame(data['content'], columns=[
                          'job_link', 'job_title', 'job_company', 'skill', 'job_type', 'location', 'salary'])
        df.dropna()
        return {'content': df.to_json()}

    @task
    def insert_data(processed_data):
        insert_into_db(processed_data, table)

    insert_data(process_data(get_data(get_url())))