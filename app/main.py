import uvicorn

from fastapi import FastAPI

from app.api.handlers import routers
from app.core import settings


app = FastAPI()

for router in routers:
    app.include_router(router)

@app.get("/")
async def default():
    return {"msg" : "hello"}


if __name__ == "__main__":
    uvicorn.run(
        "app.main:app", 
        port=settings.APP_PORT,
        host=settings.APP_HOST,
        reload=True
    )