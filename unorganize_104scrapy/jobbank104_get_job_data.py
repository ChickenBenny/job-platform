import requests
from bs4 import BeautifulSoup
import time
import random
def get_job_location(soup):
    try:
        job_location = soup.findAll('div',{'class','t3 mb-0'})
        job_location = job_location[3].text
        job_location = job_location.replace(' ', '')
    except:
        try:
            job_location = soup.findAll('div',{'class','col p-0 list-row__data'})
            job_location = job_location[3].text
            job_location = job_location.replace(' ', '')
        except:
            job_location = ''
    return job_location

def get_job_time(soup):
    try:
        job_time = soup.findAll('div',{'class','t3 mb-0'})
        job_time = job_time[2].text
        job_time = job_time.replace(' ','')
    except:
        try:
            job_time = soup.findAll('div',{'class','col p-0 list-row__data'})
            job_time = job_time[2].text
            job_time = job_time.replace(' ','')
        except:
            job_time = ''
    return 'Full-time' if '全職' in job_time else 'Part-time'

def get_job_skill(soup):
    job_skill = soup.findAll('a',{'class','tools text-gray-deep-dark d-inline-block'})
    try:
        job_skill = [i.u.text for i in job_skill]
    except:
        job_skill = []
    return job_skill

def get_job_company(soup):
    company_info = soup.findAll('div',{'class','text-truncate d-inline-block align-bottom'})
    try:
        job_company = company_info[1].text
    except:
        job_company = ''
    return job_company

def get_job_title(soup):
    company_info = soup.findAll('div',{'class','text-truncate d-inline-block align-bottom'})
    try:
        job_title = company_info[2].text
    except:
        job_title = ''
    return job_title

def get_job_salary(soup):
    job_salary = soup.findAll('p',{'class','t3 mb-0 mr-2 text-primary font-weight-bold align-top d-inline-block'})
    try:
        job_salary = job_salary[0].text
        job_salary = job_salary.replace(' ','')
    except:
        job_salary = ''
    return job_salary

def get_soup(url:str):
    time.sleep(random.uniform(0.1, 1))
    x = requests.get(url)
    if x.status_code != requests.codes.ok:
        print('requests error', x.status_code)
        return ''
    soup = BeautifulSoup(x.text,'html.parser')
    return soup

def get_job_data(url, job_type):
    soup = get_soup(url)
    job_link = url
    job_title = get_job_title(soup)
    job_company = get_job_company(soup)
    job_location = get_job_location(soup)
    job_salary = get_job_salary(soup)
    job_time = get_job_time(soup)
    job_skill = get_job_skill(soup)

    try:
        data = [job_link, job_title, job_company, job_skill,
                job_type, job_location, job_salary, job_time]
        return data
    except:
        return []