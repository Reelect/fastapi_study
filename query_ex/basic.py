from fastapi import FastAPI

app = FastAPI()

temp_item_db = [{"item_name": "Foo"},{"item_name": "Bar"}, {"item_name": "Baz"}]


# url example: http://127.0.0.1:8000/items/?skip=0&limit=2
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return temp_item_db[skip:skip+limit]