from fastapi import APIRouter, Depends, HTTPException

from app.api import get_user_service
from app.core import UserUpdateField, UserNotFound, logger
from app.schemas import UserScheme, UserSchemeResponse
from app.services import UserService


router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/{user_id}", summary="Получить информацию о пользователе по ID")
async def get_one_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
) -> UserSchemeResponse:
    try:
        return await user_service.get_user(user_id)
    except UserNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail 
        )

@router.get(
    "/",
    summary="Получить список всех зарегистрированных пользователей"
)
async def get_users(
    user_service: UserService = Depends(get_user_service)
) -> list[UserSchemeResponse]:
    try:
        return await user_service.get_users()
    except UserNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )

@router.post("/", summary="Создать новый профиль пользователя")
async def create_user(
    user_scheme: UserScheme,
    user_service: UserService = Depends(get_user_service)
) -> UserSchemeResponse:
    return await user_service.create_user(user_scheme)

@router.put(
    "/{user_id}",
    summary="Изменить конкретное поле в профиле пользователя"
)
async def update_user(
    user_id: int,
    update_field: UserUpdateField,
    data: str,
    user_service: UserService = Depends(get_user_service)
) -> UserSchemeResponse:
    return await user_service.update_user(user_id, update_field.value, data)

@router.delete(
    "/{user_id}",
    summary="Полностью удалить пользователя из системы"
)
async def delete_user(
    user_id: int,
    user_service: UserService = Depends(get_user_service)
) -> bool:
    return await user_service.delete_user(user_id)