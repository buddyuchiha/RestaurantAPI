from datetime import datetime

from sqlalchemy import delete, select, update

from app.models import BookingORM
from app.repositories import BaseRepository
from app.schemas import BookingScheme 


class BookingRepository(BaseRepository):
    def __init__(self, session) -> None:
        self.session = session
        
    async def create(
        self, 
        booking_scheme: BookingScheme
    ) -> BookingORM:
        booking = BookingORM(**booking_scheme.model_dump())
        async with self.session as session:
            session.add(booking)
            await session.commit()
            await session.refresh(booking)
            
            return booking
            
            
    async def get_one(self, id: int) -> BookingORM | None:
        async with self.session as session:
            query = select(BookingORM).where(BookingORM.id == id)
            result = await session.execute(query)
            
            return result.scalars().one_or_none()
             
    
    async def get_all(self) -> list[BookingORM]:
        async with self.session as session:
            query = select(BookingORM)
            result = await session.execute(query)
            
            return result.scalars().all()
    
    async def update(
        self,
        id: int,
        update_field: str,
        data: int | datetime
    ) -> BookingORM:
        update_data = {update_field : data}
        async with self.session as session:
            query = update(BookingORM).where(
                BookingORM.id == id
                ).values(update_data).returning(BookingORM)
            result = await session.execute(query)
            await session.commit()
            booking = result.scalars().one()
            
            await session.refresh(booking)
            return booking
            
    async def delete(self, id: int) -> bool:
        async with self.session as session:
            query = delete(BookingORM).where(BookingORM.id == id)
            await session.execute(query)
            await session.commit()
            
            return True 
        