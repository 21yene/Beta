from typing import Union
from fastapi import FastAPI
from app.utils.helper.logging import configure_logging, LogLevels

configure_logging(LogLevels.info)

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "again"}
