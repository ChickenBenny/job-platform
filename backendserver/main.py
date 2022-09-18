from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models.init_database import init_crawler
from models.get_job_data import get_data
from models.daily_job import daily_crawler

app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api")
async def home():
    return {"message": "Hello World"}


@app.get("/api/init")
def init_db():
    init = init_crawler()
    init.init_database()

    return {"message": "init_ok!"}


@app.get('/api/daily')
def daily():
    daily = daily_crawler()
    daily.crawl_daily()

    return {"message": "daily_ok"}


@app.get("/api/backend")
def backend():
    data = get_data("backend_engineer")
    return {"message": data}


@app.get("/api/dataEngineer")
def backend():
    data = get_data("data_engineer")
    return {"message": data}


@app.get("/api/dataScientist")
def backend():
    data = get_data("data_scientist")
    return {"message": data}


@app.get("/api/mlEngineer")
def backend():
    data = get_data("ml_engineer")
    return {"message": data}


@app.get("/api/qaEngineer")
def backend():
    data = get_data("qa_engineer")
    return {"message": data}
