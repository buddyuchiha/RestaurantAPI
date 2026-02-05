from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException

from app.api import get_booking_service, get_request_user_id
from app.core import (
    BookingStatus,
    BookingUpdateField,
    BookingNotFound,
    TableNotFound,
    logger
)
from app.schemas import (
    BookingScheme,
    BookingSchemeResponse,
    BookingSchemeInput
)
from app.services import BookingService


router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]    
)

@router.get("/{booking_id}", summary="Получить информацию о конкретной брони")
async def get_one_booking(
    booking_id: int,
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingSchemeResponse:
    try:
        return await booking_service.get_booking(booking_id)
    except BookingNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )

@router.get("/", summary="Получить список всех бронирований")
async def get_bookings(
    booking_service: BookingService = Depends(get_booking_service)
) -> list[BookingSchemeResponse]:
    try:
        return await booking_service.get_bookings()
    except BookingNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )

@router.post("/", summary="Создать новое бронирование")
async def create_booking(
    bookings_scheme: BookingSchemeInput,
    user_id = Depends(get_request_user_id),
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingSchemeResponse:
    try:
        return await booking_service.create_booking(bookings_scheme, user_id)
    except TableNotFound as e:
        logger.error(e.detail)
        raise HTTPException(
            status_code=404,
            detail=e.detail
        )

@router.put(
    "/info/{booking_id}", 
    summary="Изменить параметры брони (стол, время)"
)
async def update_booking_info(
    booking_id: int,
    update_field: BookingUpdateField,
    data: int | datetime,
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingSchemeResponse:
    return await booking_service.update_booking_data(
        booking_id,
        update_field,
        data
    )

@router.put("/status/{booking_id}", summary="Обновить статус бронирования")
async def update_booking_status(
    booking_id: int, 
    data: BookingStatus,
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingSchemeResponse:
    return await booking_service.update_booking_status(
        booking_id,
        data
    )
    
@router.delete("/{booking_id}", summary="Удалить бронь")
async def delete_booking(
    booking_id: int, 
    booking_service: BookingService = Depends(get_booking_service)
) -> bool:
    return await booking_service.delete_booking(booking_id)