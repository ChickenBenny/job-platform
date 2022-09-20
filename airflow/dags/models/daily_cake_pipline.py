from airflow.decorators import dag, task
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from models.cakeresume_get_job_data import get_job_data
from models.insert_into_db import insert_into_db

def daily_job_cakeresume(type, table):
    
    @task()
    def get_soup():
        url = f'https://www.cakeresume.com/jobs/python?profession%5B0%5D=it_{type}&order=latest'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        search_items = soup.find_all(
            'div', {'class': re.compile(r'JobSearchItem_wrapper__*')})
        data = []
        for search_item in search_items:
            job_data = get_job_data(search_item)
            data.append(job_data)   
        return {'content': data}

    @task
    def process_data(data):
        df = pd.DataFrame(data['content'], columns=[
                    'job_link', 'job_title', 'job_company', 'skill', 'job_type', 'location', 'salary'])
        df = df.dropna()
        df['job_type'] = df['job_type'].apply(lambda x: x.split('・')[1])
        df['location'] = df['location'].apply(lambda x: x.split('・')[0])
        return {'content': df.to_json()}

    @task
    def insert_data(processed_data):
        insert_into_db(processed_data, table)
        return {'status': 'daily_success'}

    insert_data(process_data(get_soup()))
