from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models.init_database import init_crawler
import psycopg2


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


def get_data():
    connection = psycopg2.connect(
                    database = "postgres",
                    user = "postgres",
                    password = "postgres",
                    host = "job_database",
                    port = '5432'
                )
    cursor = connection.cursor()
    query = f'SELECT * FROM backend_engineer LIMIT;'
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    return rows

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/init")
def init_db():
    init = init_crawler()
    init.init_database()

    return {"message": "init_ok!"}

@app.get("/backend")
def backend():
    data = get_data()
    return {"message": data}