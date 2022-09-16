from models.daily_models.cakeresume import *
from models.daily_models.yourator import crawler_yourator
import json


def get_information(website):
    with open('/models/crawl_information.json', 'r') as fp:
        information = json.load(fp)[website]
        return information


class daily_crawler():
    def __init__(self):
        self.cakeresume = get_information('cakeresume')
        self.yourator = get_information('yourator')

    def crawl_cakeresume(self):
        data_processor = preprocessing_cakeresume()
        for key in self.cakeresume.keys():
            job_type = self.cakeresume[key]

            web_crawler = web_crawler_cake(job_type)
            soup = web_crawler.get_soup()
            data = web_crawler.crawl_all_data(soup)
            data = data_processor.process_with_pandas(data)
            data_processor.insert_into_db(data, key)

    def crawl_yourator(self):
        crawler = crawler_yourator()
        for key in self.yourator.keys():
            data = crawler.get_data(self.yourator[key])
            data = crawler.process_with_pandas(data)
            crawler.insert(data, key)

    def crawl_daily(self):
        self.crawl_cakeresume()
        self.crawl_yourator()
