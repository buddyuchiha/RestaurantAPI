from typing import AsyncGenerator

from fastapi import Depends, HTTPException, Request, Security, security
import redis
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
    AuthService,
    CacheService
)
from cache.accessor import get_cache_session


def get_cache_service(
    cache_session = Depends(get_cache_session)
) -> redis.Redis:
    return CacheService(cache_session) 


def get_table_repository(
    session: Session = Depends(get_session)
) -> TableRepository:
    return TableRepository(session)


def get_table_service(
    table_repository: TableRepository = Depends(get_table_repository),
    cache_service: CacheService = Depends(get_cache_service)
) -> TableService:
    return TableService(table_repository, cache_service)


def get_user_repository(
    session: Session = Depends(get_session)
) -> UserRepository:
    return UserRepository(session)


def get_user_service(
    user_repository: UserRepository = Depends(get_user_repository),
    cache_service: CacheService = Depends(get_cache_service)
) -> UserService:
    return UserService(user_repository, cache_service)


def get_booking_repository(
    session: Session = Depends(get_session)
) -> BookingRepository:
    return BookingRepository(session)


def get_booking_service(
    booking_repository: BookingRepository = Depends(get_booking_repository),
    table_service: TableService = Depends(get_table_service),
    cache_service: CacheService = Depends(get_cache_service)
) -> BookingService:
    return BookingService(booking_repository, table_service, cache_service)


def get_auth_service(
    user_service: UserService = Depends(get_user_service)
) -> AuthService:
    return AuthService(user_service)


reusable_oauth2 = security.HTTPBearer()

def get_request_user_id(
    request: Request, 
    auth_service: AuthService = Depends(get_auth_service),
    token: security.HTTPAuthorizationCredentials = Security(
        reusable_oauth2
    )
) -> int | None: 
    try: 
        user_id = auth_service.get_user_id_from_access_token(
            token.credentials
        )
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