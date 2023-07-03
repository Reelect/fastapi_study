from fastapi import FastAPI

app = FastAPI()


# :path는 매개변수가 경로와 일치해야함을 알려줍니다
@app.get("/files/{file_path:path}")
async def read_file(file_path: str):
    return {"file_path": file_path}
