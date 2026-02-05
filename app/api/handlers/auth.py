from fastapi import APIRouter, Depends, HTTPException

from app.api import get_auth_service
from app.core import WrongPassword, UserNotFound, logger, UserExists
from app.schemas import (
    UserScheme,
    UserSchemeResponse,
    UserLoginScheme,
    TokenResponse
)   
from app.services import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register", summary="Регистрация нового пользователя")
async def regitser(
    user: UserScheme,
    auth_service: AuthService = Depends(get_auth_service)
) -> UserSchemeResponse:
    try:
        return await auth_service.register_user(user)
    except UserExists as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=409,
            detail=e.detail
        )

@router.post("/login", summary="Авторизация и получение JWT-токена")
async def login(
    user: UserLoginScheme,
    auth_service: AuthService = Depends(get_auth_service)
) -> TokenResponse:
    try: 
        return await auth_service.login_user(user)
    except UserNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )
    except WrongPassword as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )