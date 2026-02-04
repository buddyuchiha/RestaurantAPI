from datetime import datetime
from app.core import BookingStatus, BookingUpdateField
from app.repositories import BookingRepository
from app.schemas import BookingScheme, BookingSchemeResponse
from app.schemas.booking import BookingSchemeInput


class BookingService:
    def __init__(self, booking_repository: BookingRepository) -> None:
        self.booking_repository = booking_repository   
    
    async def create_booking(
        self, 
        booking_scheme: BookingSchemeInput,
        user_id: int
    ) -> BookingSchemeResponse:
        new_booking_scheme = BookingScheme(
            **booking_scheme.model_dump(), user_id=user_id
        )
        
        booking = await self.booking_repository.create(new_booking_scheme)
        
        return BookingSchemeResponse.model_validate(booking) 
    
    async def get_booking(self, booking_id: int) -> BookingSchemeResponse:
        booking = await self.booking_repository.get_one(booking_id)
        
        return BookingSchemeResponse.model_validate(booking) 
    
    async def get_bookings(self) -> list[BookingSchemeResponse]:
        bookings = await self.booking_repository.get_all()
        
        return [
            BookingSchemeResponse.model_validate(
                booking
                ) for booking in bookings
            ]
    
    async def update_booking_data(
        self,
        id: int,
        update_field: BookingUpdateField,
        data: int | datetime
    ) -> BookingSchemeResponse:
        return await self.booking_repository.update(
            id,
            str(update_field.value), 
            data
            )
    
    async def update_booking_status(
        self,
        id: int, 
        data: BookingStatus
        ) -> BookingSchemeResponse:
        booking = await self.booking_repository.update(id, "status", data)
        
        return BookingSchemeResponse.model_validate(booking)
    
    async def delete_booking(self, id: int) -> bool:
        return await self.booking_repository.delete(id)