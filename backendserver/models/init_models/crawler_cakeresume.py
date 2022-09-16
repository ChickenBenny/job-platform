import requests
from bs4 import BeautifulSoup
import re
from random import randint
import time


class web_crawler_cake():
    def __init__(self, job_type, crawling_type):
        self.job_type = job_type
        self.crawling_type = crawling_type

    def get_soup(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if soup:
            return soup
        else:
            return ""

    def find_next_page(self, soup):
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

    def get_url_data(self):
        url_data = []
        url = f'https://www.cakeresume.com/jobs/python?profession%5B0%5D=it_{self.job_type}&order=latest'
        url_data.append(url)
        if self.crawling_type == 'init':
            soup = self.get_soup(url)
            if soup:
                i = 0
                while True:
                    time.sleep(randint(1, 6))
                    if i > 15:
                        break
                    next_page_link = self.find_next_page(soup)
                    if next_page_link == "":
                        break
                    if next_page_link in url_data:
                        break
                    else:
                        url_data.append(next_page_link)
                        soup = self.get_soup(next_page_link)
                        i += 1
        return url_data

    def get_search_item(self, soup):
        search_item = soup.find_all(
            'div', {'class': re.compile(r'JobSearchItem_wrapper__*')})
        return search_item

    def get_job_link_and_title(self, search_item):
        url_domain = 'https://www.cakeresume.com'
        job_title = search_item.find(
            'div', {'class': re.compile(r'JobSearchItem_headerTitle__*')}).getText()
        job_link = url_domain + (search_item.find('div', {'class': re.compile(
            r'JobSearchItem_headerTitle__*')}).find('a', href=True))['href']
        return job_link, job_title

    def get_company_name(self, search_item):
        company_name = search_item.find('div', class_=re.compile(
            r'JobSearchItem_headerSubtitle__*')).getText()
        return company_name

    def get_job_skill(self, search_item):
        skill_set = []
        if search_item.find('div', {'class': re.compile(r'JobSearchItem_tags__*')}):
            tags = search_item.find('div', {'class': re.compile(
                r'JobSearchItem_tags__*')}).find_all('div', {'class': re.compile(r'Tags_item__*')})
            for tag in tags:
                if tag.text != '':
                    skill_set.append(tag.text)
        else:
            skill_set.append('None')
        return skill_set

    def get_feature(self, search_item):
        job_features = search_item.find(
            'div', class_=re.compile(r'JobSearchItem_features__*'))
        inline_messages_type = job_features.find_all(
            'div', class_=re.compile(r'InlineMessage_icon__*'))
        inline_messages = job_features.find_all(
            'div', class_=re.compile(r'InlineMessage_label__*'))
        feature = {}
        if len(inline_messages) == len(inline_messages_type):
            for i in range(len(inline_messages)):
                type = (inline_messages_type[i].find('div', class_=re.compile(
                    r'Tooltip_handle__*')).find('i', class_=True)['class'])[1][3:]
                label = inline_messages[i].text
                feature[type] = label
        return feature

    def get_job_data(self, search_item):
        job_link, job_title = self.get_job_link_and_title(search_item)
        company_name = self.get_company_name(search_item)
        skill_set = self.get_job_skill(search_item)
        feature = self.get_feature(search_item)
        try:
            data = [job_link, job_title, company_name, skill_set,
                    feature['user'], feature['map-marker-alt'], feature['dollar-sign']]
            return data
        except:
            return []

    def crawl_all_data(self, url_datas):
        data = []
        for url in url_datas:
            soup = self.get_soup(url)
            if soup != "":
                search_items = self.get_search_item(soup)
                for search_item in search_items:
                    job_data = self.get_job_data(search_item)
                    data.append(job_data)
            time.sleep(randint(1, 6))

        return data
