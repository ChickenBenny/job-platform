from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models.get_job_data import get_data

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
