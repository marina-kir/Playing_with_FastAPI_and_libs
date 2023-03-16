import uvicorn
from http import HTTPStatus
from typing import Union
import aiohttp
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()


@app.get("/ISBN/{isbn}")
def read_isbn(isbn: str):
    path = f"https://openlibrary.org/isbn/{isbn}.json"
    r = requests.get(path)
    return r.json()


if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)
