from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


app = FastAPI()


@app.post("/items/special")
async def create_item(item: Item):
    result = item.dict()
    if item.tax:
        total_price = item.price + item.tax
        result.update({"total_price": total_price})
    return result


@app.post("/items/{item_id}")
async def create_item(item: Item, item_id: int, query: Union[str, None] = None):
    result = {"item_id": item_id, **item.dict()}
    if query:
        result.update({"query": query})
    return result