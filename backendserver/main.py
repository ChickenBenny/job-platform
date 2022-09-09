from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from models.init_database import init_crawler

app = FastAPI()

@app.get("/")
async def home():
    return {"message": "Hello World"}

@app.get("/init")
def init_db():
    init = init_crawler()
    init.init_database()

    return {"message": "init_ok!"}