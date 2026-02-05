from fastapi import APIRouter, Depends, HTTPException

from app.api import get_table_service
from app.core import logger
from app.core.enum import TableStatus
from app.core.exception import TableNotFound
from app.schemas import TableScheme
from app.services import TableService


router = APIRouter(
    prefix="/tables", 
    tags=["tables"]
)

@router.get("/status")
async def get_tables_by_status(
    table_status: TableStatus,
    table_service: TableService = Depends(get_table_service)
) -> list[TableScheme]:
    return await table_service.get_tables_by_status(table_status)

@router.get("/{table_id}")
async def get_one_table(
    table_id: int,
    table_service: TableService = Depends(get_table_service)
) -> TableScheme:
    try: 
        return await table_service.get_table(table_id)
    except TableNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )

@router.get("/")
async def get_tables(
    table_service: TableService = Depends(get_table_service)
) -> list[TableScheme]:
    try: 
        logger.info("get_tables")
        return await table_service.get_tables() 
    except TableNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )

@router.post("/")
async def create_table(
    table_service: TableService = Depends(get_table_service)
) -> TableScheme:
    return await table_service.create_table()

@router.put("/{table_id}")
async def update_table(
    table_id: int, 
    table_status: TableStatus,
    table_service: TableService = Depends(get_table_service)
) -> TableScheme:
    return await table_service.update_table(table_id, table_status)  

@router.delete("/{table_id}")
async def delete_table(
    table_id: int,
    table_service: TableService = Depends(get_table_service)
) -> bool:
    return await table_service.delete_table(table_id)
