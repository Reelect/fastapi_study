from typing import Union
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, query: Union[str, None] = None, short: bool = False):
    item = {"item_id": item_id}
    if query:
        # http://127.0.0.1:8000/items/1?query=this_is_revolution
        item.update({"query": query})
    if not short:
        # http://127.0.0.1:8000/items/1?query=this_is_revolution&short=Falase
        # on off, yes no, 1 0, True False(regardless of upper)
        item.update(
            {"description": "This is an amazing itme that has a long description"}
        )
    return item


# parameter category is detected by name
@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item