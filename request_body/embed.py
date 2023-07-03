from typing import Union

from fastapi import Body, FastAPI
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Annotated[Item, Body(embed=True)]):
    # expect a JSON with a key item and inside of it the model contents
    results = {"item_id": item_id, "item": item}
    return results