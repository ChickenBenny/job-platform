from airflow.decorators import dag, task
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
from random import randint
import time
from models.cakeresume_get_job_data import get_job_data
from models.insert_into_db import insert_into_db


def init_cakeresume(type, table):
    
    def get_soup(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup:
            return soup
        else:
            return ""

    def find_next_page(soup):
        next_page = soup.find(
            'div', {'class': re.compile(r'Pagination_wrapper__*')})
        if not next_page:
            return ""
        next_page_link = next_page.find_all(
            'a', {'class': re.compile(r'Pagination_itemNavigation__*')}, href=True)
        if len(next_page_link) == 2:
            return next_page_link[1]['href']
        elif len(next_page_link) == 1:
            return next_page_link[0]['href']
        else:
            return ""

    @task
    def get_url():
        url_data = []
        url = f'https://www.cakeresume.com/jobs/python?profession%5B0%5D=it_{type}&order=latest'
        url_data.append(url)
        soup = get_soup(url)
        if soup:
            i = 0
            while True:
                time.sleep(randint(1, 3))
                if i > 15:
                    break
                next_page_link = find_next_page(soup)
                if next_page_link == "":
                    break
                if next_page_link in url_data:
                    break
                else:
                    url_data.append(next_page_link)
                    soup = get_soup(next_page_link)
                    i += 1
        return {'content': url_data}        

    @task
    def get_data(url_data):
        data = []
        for url in url_data['content']:
            soup = get_soup(url)
            if soup != "":
                search_items = soup.find_all(
                    'div', {'class': re.compile(r'JobSearchItem_wrapper__*')})
                for search_item in search_items:
                    job_data = get_job_data(search_item)
                    data.append(job_data)
            time.sleep(randint(1, 3)) 
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

    insert_data(process_data(get_data(get_url())))       