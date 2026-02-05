from datetime import datetime
import json

from app.core import BookingStatus, BookingUpdateField
from app.core.exception import BookingNotFound, TableNotFound
from app.repositories import BookingRepository
from app.schemas import BookingScheme, BookingSchemeResponse
from app.schemas.booking import BookingSchemeInput
from app.services.cache_service import CacheService
from app.services.table_service import TableService


class BookingService:
    def __init__(
        self, 
        booking_repository: BookingRepository,
        table_service: TableService,
        cache_service: CacheService
    ) -> None:
        self.booking_repository = booking_repository   
        self.table_service = table_service
        self.cache_service = cache_service
    
    async def create_booking(
        self, 
        booking_scheme: BookingSchemeInput,
        user_id: int
    ) -> BookingSchemeResponse:
        new_booking_scheme = BookingScheme(
            **booking_scheme.model_dump(), user_id=user_id
        )
        
        await self.table_service.get_table(booking_scheme.table_id)
        
        booking = await self.booking_repository.create(new_booking_scheme)
        
        return BookingSchemeResponse.model_validate(booking) 
    
    async def get_booking(self, booking_id: int) -> BookingSchemeResponse:
        booking = await self.booking_repository.get_one(booking_id)
        
        if not booking:
            raise BookingNotFound
        
        
        return BookingSchemeResponse.model_validate(booking) 
    
    async def get_bookings(self) -> list[BookingSchemeResponse]:
        if bookings := await self.cache_service.get_values("bookings"):
            data = json.loads(bookings)
            return [
                BookingSchemeResponse.model_validate(item) \
                    for item in data
            ]
        
        bookings = await self.booking_repository.get_all()
        if not bookings:
            raise BookingNotFound
        
        serialized_bookings = [BookingSchemeResponse.model_validate(booking) \
            for booking in bookings
        ]
        
        await self.cache_service.set_values(
            "bookings",
            serialized_bookings,
            BookingSchemeResponse
        )
        
        return serialized_bookings
    
    
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