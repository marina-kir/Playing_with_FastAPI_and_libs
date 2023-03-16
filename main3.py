import uvicorn
from http import HTTPStatus
from typing import Union
import aiohttp
import asyncio
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

global_items = {}

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    if item_id not in global_items.keys():
        raise HTTPException(status_code=HTTPStatus.NOT_FOUND)
    return {"item_id": item_id, "q": global_items[item_id]}


@app.put("/items/{item_id}", status_code=HTTPStatus.CREATED)
async def update_item(item_id: int, item: Item):
    global_items.update({item_id: item})
    return {"item_name": item.name, "item_id": item_id}


@app.get("/ISBN/{isbn}")
async def read_isbn(isbn: str):
    async with aiohttp.ClientSession() as session:
        path = f"https://openlibrary.org/isbn/{isbn}.json"
        async with session.get(path) as response:
            json = await response.json()
            return json

from pymongo import MongoClient
client = MongoClient()
db = client.local
col = db.marina
import pprint
from bson.objectid import ObjectId

content = pprint.pprint(col.find_one({"q": 5}))

pass



@app.get("/ISBN/{isbn}")
async def read_isbn(isbn: str):
    if (content == None):
        print("in if")
    else:
        print("not in if")
    async with aiohttp.ClientSession() as session:
        path = f"https://openlibrary.org/isbn/{isbn}.json"
        async with session.get(path) as response:
            json = await response.json()
            return json

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8001)