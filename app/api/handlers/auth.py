from fastapi import APIRouter, Depends, HTTPException

from app.api import get_auth_service
from app.core import WrongPassword, UserNotFound
from app.schemas import UserScheme, UserSchemeResponse, UserLoginScheme
from app.services import AuthService


router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@router.post("/register")
async def regitser(
    user: UserScheme,
    auth_service: AuthService = Depends(get_auth_service)
) -> UserSchemeResponse:
    return await auth_service.register_user(user)

@router.post("/login")
async def login(
    user: UserLoginScheme,
    auth_service: AuthService = Depends(get_auth_service)
):
    try: 
        return await auth_service.login_user(user)
    except UserNotFound as e:
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )
    except WrongPassword as e:
        raise HTTPException(
            status_code=401,
            detail=e.detail
        )