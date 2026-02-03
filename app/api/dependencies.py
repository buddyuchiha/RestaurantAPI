from fastapi import Depends
from sqlalchemy.orm import Session 

from app.database import get_session
from app.repositories import TableRepository
from app.repositories import UserRepository
from app.services import TableService
from app.services import UserService


def get_table_repository(
    session: Session = Depends(get_session)
) -> TableRepository:
    return TableRepository(session)


def get_table_service(
    table_repository: TableRepository = Depends(get_table_repository)
) -> TableService:
    return TableService(table_repository)


def get_user_repository(
    session: Session = Depends(get_session)
) -> UserRepository:
    return UserRepository(session)


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository)
) -> UserService:
    return UserService(user_repository)