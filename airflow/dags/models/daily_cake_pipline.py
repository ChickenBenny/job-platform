from datetime import datetime, timedelta
from airflow.decorators import dag, task
from airflow.providers.postgres.hooks.postgres import PostgresHook
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from models.cakeresume_get_job_data import get_job_data

POSTGRES_CONN_ID = 'job_database'

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
    def insert_into_db(processed_data):
        processed_data = pd.read_json(processed_data['content'])
        hook = PostgresHook.get_hook(POSTGRES_CONN_ID)
        connection = hook.get_conn()
        cursor = connection.cursor()
        dt = datetime.now().strftime("%Y%m%d")
        for i in range(processed_data.shape[0]):
            try:
                query = f'''INSERT INTO {table}(url_link, title, company, skill, job_type, loc, salary, dt) \
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s);'''
                data = (processed_data.iloc[i, 0], processed_data.iloc[i, 1], processed_data.iloc[i, 2], processed_data.iloc[i, 3],
                        processed_data.iloc[i, 4], processed_data.iloc[i, 5], processed_data.iloc[i, 6], dt)
                cursor.execute(query, data)
                connection.commit()
                print('success')
            except:
                cursor.close()
                connection.close()
                connection = hook.get_conn()
                cursor = connection.cursor()
                print('fail')
        cursor = connection.cursor()
        print('daily work success')
        return {'status': 'daily_success'}

    insert_into_db(process_data(get_soup()))
