import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd
import psycopg2


class crawler_yourator():
    def __init__(self):
        self.date = datetime.now().strftime("%Y%m%d")

    def get_data(self, job_type):
        url = f'https://www.yourator.co/api/v2/jobs?category[]={job_type}&tag[]=Python&sort=recent_updated'
        url_domain = 'https://www.yourator.co/'
        all_data = []
        response = requests.get(url)
        response = response.json()
        job_lists = response['jobs']
        for job in job_lists:
            job_url = url_domain + job['path']
            job_response = requests.get(job_url)
            soup = BeautifulSoup(job_response.text, 'html.parser')
            container = soup.find('div', {'class', 'container'})
            basic_info = container.find_all(
                'div', {'class': 'basic-info__title'})
            job_title = basic_info[0].h1.getText()
            job_company = basic_info[1].a.getText()
            job_type = job['job_type']
            job_address = job['city']
            salary = job['salary']
            tags = job['tags']
            skill_set = []
            if len(tags) != 0:
                for tag in tags:
                    skill_set.append(tag['name'])
            else:
                skill_set.append('None')
            tmp_data = [job_url, job_title, job_company,
                        skill_set, job_type, job_address, salary]
            all_data.append(tmp_data)
        return all_data

    def process_with_pandas(self, crawling_data):
        df = pd.DataFrame(crawling_data, columns=[
                          'job_link', 'job_title', 'job_company', 'skill', 'job_type', 'location', 'salary'])
        df['dt'] = self.date
        df.dropna()
        return df

    def insert(self, df, table):
        connection = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="postgres",
            host="job_database",
            port='5432'
        )
        cursor = connection.cursor()
        for i in range(df.shape[0]):
            try:
                query = f'''INSERT INTO {table}(url_link, title, company, skill, job_type, loc, salary, dt) \
                            VALUES(%s, %s, %s, %s, %s, %s, %s, %s);'''
                data = (df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3],
                        df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7])
                cursor.execute(query, data)
                connection.commit()
            except:
                cursor.close()
                connection.close()
                connection = psycopg2.connect(
                    database="postgres",
                    user="postgres",
                    password="postgres",
                    host="job_database",
                    port='5432'
                )
                cursor = connection.cursor()
        cursor.close()


if __name__ == '__main__':
    changer = {
        "data_engineer": "%E8%B3%87%E6%96%99%E5%B7%A5%E7%A8%8B%20%2F%20%E6%A9%9F%E5%99%A8%E5%AD%B8%E7%BF%92",
        "backend_engineer": "%E5%BE%8C%E7%AB%AF%E5%B7%A5%E7%A8%8B",
        "qa_engineer": "%E6%B8%AC%E8%A9%A6%E5%B7%A5%E7%A8%8B",
    }

    crawler = crawler_yourator()
    data = crawler.get_data(changer['data_engineer'])
    print(data)
