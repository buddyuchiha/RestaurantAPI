from sqlalchemy.orm import Session
from sqlalchemy import select

from app.repositories import BaseRepository
from app.models import TableORM


class TableRepository(BaseRepository):
    def __init__(self, session: Session) -> None:
        self.session = session
        
    async def create(self) -> TableORM:
        async with self.session as session:
            table = TableORM()
            session.add(table)
            
            await session.commit()
            await session.refresh(table)
            
            return table
        
    async def get_one(self):
        pass 
    
    async def get_all(self):
        pass 
    
    async def update(self):
        pass 
    
    async def delete(self):
        pass