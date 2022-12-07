# from airflow.decorators import dag, task
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import random
import time
from models.jobbank104_get_job_data import get_job_data
from models.insert_into_db import insert_into_db

POSTGRES_CONN_ID = 'job_database'

def init_jobbank104(type, table):
    
    def search_job(keyword:str, max_mun=100, filter_params=None, sort_type='日期', is_sort_asc=False):
        '''search for vacancies'''
        jobs = []
        total_count = 0

        url = 'https://www.104.com.tw/jobs/search/list'
        query = f'ro=0&kwop=7&keyword={keyword}&expansionType=area,spec,com,job,wf,wktm&mode=s&jobsource=2018indexpoc'
        if filter_params:
            query += ''.join([f'&{key}={value}' for key, value, in filter_params.items()])
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
            'Referer': 'https://www.104.com.tw/jobs/search/',
        }
        sort_dict = {
            '符合度': '1',
            '日期': '2',
            '經歷': '3',
            '學歷': '4',
            '應徵人數': '7',
            '待遇': '13',
        }
        sort_params = f"&order={sort_dict.get(sort_type, '1')}"
        sort_params += '&asc=1' if is_sort_asc else '&asc=0'
        query += sort_params

        page = 1
        while len(jobs) < max_mun:
            params = f'{query}&page={page}'
            r = requests.get(url, params=params, headers=headers)

            if r.status_code != requests.codes.ok:
                print('request failed', r.status_code)
                data = r.json()
                print(data['status'], data['statusMsg'], data['errorMsg'])
                break
            print(r.text)

            data = r.json()
            total_count = data['data']['totalCount']
            jobs.extend(data['data']['list'])

            if (page == data['data']['totalPage']) or (data['data']['totalPage'] == 0):
                break
            page += 1
            time.sleep(random.uniform(1, 3))
        
        data = []
        for i in jobs[:max_mun]:
            job_url = f"https:{i['link']['job']}"
            data.append(job_url)
        return data

    def get_data(job_type):
        job_urls = search_job(job_type, max_mun=100, filter_params={})
        data = []
        for url in job_urls:
            job_info = get_job_data(url, job_type)
            print(job_info)
            if job_info != []:
                data.append(job_info)
        return {'content': data}
    
    def process_data(data):
        df = pd.DataFrame(data['content'], columns=[
                    'job_link', 'job_title', 'job_company', 'skill', 'job_type', 'location', 'salary'])
        df = df.dropna()
        return {'content': df.to_json()}
    
    def insert_data(processed_data):
        insert_into_db(processed_data, table)

    insert_data(process_data(get_data(type)))