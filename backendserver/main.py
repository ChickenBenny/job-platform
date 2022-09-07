from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models.crawler_cakeresume import web_crawler_cake
from models.process_and_insert_cakeresume import preprocessing_cakeresume

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/init")
def init_db():
    crawler_de = web_crawler_cake('data-engineer', 'init')
    url_de = crawler_de.get_url_data()
    data_de = crawler_de.crawl_all_data(url_de)

    crawler_backend = web_crawler_cake('back-end-engineer', 'init')
    url_backend = crawler_backend.get_url_data()
    data_backend = crawler_de.crawl_all_data(url_backend)

    crawler_ds = web_crawler_cake('data-scientist', 'init')
    url_ds = crawler_ds.get_url_data()
    data_ds = crawler_de.crawl_all_data(url_ds)

    crawler_ml = web_crawler_cake('machine-learning-engineer', 'init')
    url_ml =crawler_ml.get_url_data()
    data_ml = crawler_de.crawl_all_data(url_ml)

    crawler_qa = web_crawler_cake('qa-test-engineer', 'init')
    url_qa = crawler_qa.get_url_data()
    data_qa = crawler_de.crawl_all_data(url_qa)

    data_processor = preprocessing_cakeresume()
    data_de = data_processor.process_with_pandas(data_de)
    data_backend = data_processor.process_with_pandas(data_backend)
    data_ds = data_processor.process_with_pandas(data_ds)
    data_ml = data_processor.process_with_pandas(data_ml)
    data_qa = data_processor.process_with_pandas(data_qa)

    data_processor.insert_into_db(data_de, 'data_engineer')
    data_processor.insert_into_db(data_backend, 'backend_engineer')
    data_processor.insert_into_db(data_ds, 'data_scientist')
    data_processor.insert_into_db(data_ml, 'ml_engineer')
    data_processor.insert_into_db(data_qa, 'qa_engineer')

    return {"message": "init_ok!"}