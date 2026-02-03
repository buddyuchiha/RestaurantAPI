import uvicorn

from fastapi import FastAPI

from app.api.handlers import routers

app = FastAPI()

for router in routers:
    app.include_router(router)

@app.get("/")
async def default():
    return {"msg" : "hello"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        port=8000,
        host="127.0.0.1",
        reload=True
    )