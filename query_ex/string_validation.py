from typing import Union

from fastapi import FastAPI, Query
# validation check package
from typing_extensions import Annotated

app = FastAPI()


@app.get("/items/")
async def read_items(q: Annotated[Union[str, None], Query(max_length=50)] = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:  # q is limited 50 length string
        results.update({"q": q})
    return results
