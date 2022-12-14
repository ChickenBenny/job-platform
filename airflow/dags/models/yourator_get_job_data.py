import requests
from bs4 import BeautifulSoup

def get_job_data(url_datas):
    url_domain = 'https://www.yourator.co/'
    all_data = []
    for url in url_datas:
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
                    if tag['name'] == 'MachineLearning':
                        skill_set.append('機器學習')
                    elif tag['name'] == 'DeepLearning':
                        skill_set.append('深度學習')
                    else:
                        skill_set.append(tag['name'])
            else:
                skill_set.append('None')
            tmp_data = [job_url, job_title, job_company,
                        skill_set, job_type, job_address, salary]
            all_data.append(tmp_data)
    return all_data