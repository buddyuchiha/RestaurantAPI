import uvicorn

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def default():
    return {"msg" : "hello"}


if __name__ == "__main__":
    uvicorn.run(app)