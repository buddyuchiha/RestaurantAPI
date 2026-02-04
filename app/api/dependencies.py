from fastapi import Depends, HTTPException, Request, Security, security
from sqlalchemy.orm import Session 

from app.core import TokenExpired, TokenNotCorrect
from app.database import get_session
from app.repositories import (
    TableRepository,
    UserRepository,
    BookingRepository
)
from app.services import (
    TableService,
    UserService,
    BookingService,
    AuthService
)


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


def get_booking_repository(
    session: Session = Depends(get_session)
) -> BookingRepository:
    return BookingRepository(session)


def get_booking_service(
    booking_repository: BookingRepository = Depends(get_booking_repository)
) -> BookingService:
    return BookingService(booking_repository)


def get_auth_service(
    user_service: UserService = Depends(get_user_service)
) -> AuthService:
    return AuthService(user_service)


reusable_oauth2 = security.HTTPBearer()

def get_request_user_id(
    request: Request, 
    auth_service: AuthService = Depends(get_auth_service),
    token: security.HTTPAuthorizationCredentials = Security(reusable_oauth2)
) -> int | None: 
    try: 
        user_id = auth_service.get_user_id_from_access_token(token.credentials)
    except TokenExpired as e:
        raise HTTPException(
            status_code=401, 
            detail=e.detail
        )
    except TokenNotCorrect as e:
        raise HTTPException(
            status_code=401, 
            detail=e.detail
        )
    return user_id