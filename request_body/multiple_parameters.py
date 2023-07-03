from typing import Union

from fastapi import FastAPI, Path, Body
from pydantic import BaseModel
from typing_extensions import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None


class User(BaseModel):
    username: str
    full_name: Union[str, None] = None


# Mix Path, Query and body parameters
@app.put("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: Union[str, None] = None,
        item: Union[Item, None] = None):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    return results


# Multiple body parameters
@app.put("/useritems/{item_id}")
async def update_item(item_id: int, item: Item, user: User):
    result = {"item_id": item_id, "item": item, "user": user}
    return result


# Multiple body and query params
@app.put("/multi/{multi_id}")
async def multi(
        *,
        multi_id: int,
        item: Item,
        user: User,
        importance: Annotated[int, Body(gt=0)],
        q: Union[str, None] = None,
):
    results = {"multi_id": multi_id, "item": item, "user": user, "importance": importance}
    if q:
        results.update({"q": q})
    return results