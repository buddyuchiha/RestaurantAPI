from fastapi import APIRouter, Depends

from app.api import get_user_service
from app.core import UserUpdateField
from app.schemas import UserScheme, UserSchemeResponse
from app.services import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/{user_id}")
async def get_one_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
) -> UserSchemeResponse:
    return await user_service.get_user(user_id)

@router.get("/")
async def get_users(
    user_service: UserService = Depends(get_user_service)
) -> list[UserSchemeResponse]:
    return await user_service.get_users()

@router.post("/")
async def create_user(
    user_scheme: UserScheme,
    user_service: UserService = Depends(get_user_service)
) -> UserSchemeResponse:
    return await user_service.create_user(user_scheme)

@router.put("/{user_id}")
async def update_user(
    user_id: int,
    update_field: UserUpdateField,
    data: str,
    user_service: UserService = Depends(get_user_service)
) -> UserSchemeResponse:
    return await user_service.update_user(user_id, update_field.value, data)

@router.delete("/{user_id}")
async def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
) -> bool:
    return await user_service.delete_user(user_id)