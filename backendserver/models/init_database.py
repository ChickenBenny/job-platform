from models.init_models.crawler_cakeresume import web_crawler_cake
from models.init_models.process_and_insert_cakeresume import preprocessing_cakeresume
from models.init_models.crawler_yourator import crawler_yourator
import json


def get_information(website):
    with open('/models/crawl_information.json', 'r') as fp:
        information = json.load(fp)[website]
        return information


class init_crawler():
    def __init__(self):
        self.cakeresume = get_information('cakeresume')
        self.yourator = get_information('yourator')

    def init_cakeresumse(self):
        data_processor = preprocessing_cakeresume()
        for key in self.cakeresume.keys():
            job_type = self.cakeresume[key]
            type = 'init'

            web_crawler = web_crawler_cake(job_type, type)
            url_data = web_crawler.get_url_data()
            data = web_crawler.crawl_all_data(url_data)

            data = data_processor.process_with_pandas(data)
            data_processor.insert_into_db(data, key)

    def init_yourator(self):
        crawler = crawler_yourator()
        for key in self.yourator.keys():
            url_data = crawler.get_url(self.yourator[key])
            data = crawler.get_data(url_data)
            data = crawler.process_with_pandas(data)
            crawler.insert(data, key)

    def init_database(self):
        self.init_cakeresumse()
        self.init_yourator()
