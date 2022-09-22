from bs4 import BeautifulSoup
import re

def get_job_link_and_title(search_item):
    url_domain = 'https://www.cakeresume.com'
    job_title = search_item.find(
        'div', {'class': re.compile(r'JobSearchItem_headerTitle__*')}).getText()
    job_link = url_domain + (search_item.find('div', {'class': re.compile(
        r'JobSearchItem_headerTitle__*')}).find('a', href=True))['href']
    return job_link, job_title

def get_company_name(search_item):
    company_name = search_item.find('div', class_=re.compile(
        r'JobSearchItem_headerSubtitle__*')).getText()
    return company_name

def get_job_skill(search_item):
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

def get_feature(search_item):
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

def get_job_data(search_item):
        job_link, job_title = get_job_link_and_title(search_item)
        company_name = get_company_name(search_item)
        skill_set = get_job_skill(search_item)
        feature = get_feature(search_item)
        try:
            data = [job_link, job_title, company_name, skill_set,
                    feature['user'], feature['map-marker-alt'], feature['dollar-sign']]
            return data
        except:
            return []    