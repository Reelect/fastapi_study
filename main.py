from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


# str input example
@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


# int input example
# should use same parameter to query
@app.get("/items/{item}")
async def read_item(item: int):  # : type makes convert to indicated type
    return {"item_id": item}


# order problem example
# case 1 : special case -> must be placed first
@app.get("/conflict/special")
async def take_special():
    return {"message": "you got the special"}


# case 2 : ordinary case -> must be last
@app.get("/conflict/{ordinary}")
async def take_special(ordinary):
    return {"message": "ordinary result-> "+ordinary}