from fastapi import Depends
from sqlalchemy.orm import Session 

from app.database import get_session
from app.repositories import TableRepository
from app.services import TableService


def get_table_repository(
    session: Session = Depends(get_session)
) -> TableRepository:
    return TableRepository(session)

def get_table_service(
    table_repository: TableRepository = Depends(get_table_repository)
) -> TableService:
    return TableService(table_repository)