from datetime import datetime
from fastapi import APIRouter, Depends

from app.api import get_booking_service
from app.core import BookingStatus, BookingUpdateField
from app.schemas import BookingScheme, BookingSchemeResponse
from app.services import BookingService


router = APIRouter(
    prefix="/bookings",
    tags=["bookings"]    
)

@router.get("/{booking_id}")
async def get_one_booking(
    booking_id: int,
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingSchemeResponse:
    return await booking_service.get_booking(booking_id)

@router.get("/")
async def get_bookings(
    booking_service: BookingService = Depends(get_booking_service)
) -> list[BookingSchemeResponse]:
    return await booking_service.get_bookings()

@router.post("/")
async def create_booking(
    bookings_scheme: BookingScheme,
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingSchemeResponse:
    return await booking_service.create_booking(bookings_scheme)

@router.put("/info/{booking_id}")
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

@router.put("/status/{booking_id}")
async def update_booking_status(
    booking_id: int, 
    data: BookingStatus,
    booking_service: BookingService = Depends(get_booking_service)
) -> BookingSchemeResponse:
    return await booking_service.update_booking_status(
        booking_id,
        data
    )
    

@router.delete("/{booking_id}")
async def delete_booking(
    booking_id: int, 
    booking_service: BookingService = Depends(get_booking_service)
) -> bool:
    return await booking_service.delete_booking(booking_id)