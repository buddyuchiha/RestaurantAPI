from fastapi import APIRouter, Depends

from app.api import get_table_service
from app.schemas import TableScheme
from app.services import TableService


router = APIRouter(
    prefix="/tables", 
    tags=["tables"]
)

@router.get("/")
async def get_table():
    pass 

@router.get("/")
async def get_tables():
    pass 

@router.post("/")
async def create_tables(
    table_service: TableService = Depends(get_table_service)
) -> TableScheme:
    return await table_service.create_table()

@router.put("/")
async def update_table():
    pass 

@router.delete("/")
async def delete_table():
    pass 