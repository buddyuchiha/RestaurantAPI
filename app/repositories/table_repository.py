from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update

from app.core import TableStatus
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
        
    async def get_one(self, id: int) -> TableORM | None:
        async with self.session as session:
            query = select(TableORM).where(TableORM.id == id)
            result = await session.execute(query)
            
            return result.scalars().one_or_none()
    
    async def get_all(self) -> list[TableORM]:
        async with self.session as session:
            query = select(TableORM)
            result = await session.execute(query)
            
            return result.scalars().all() 
    
    async def update(self, id: int, status: str) -> TableORM:
        async with self.session as session:
            query = update(TableORM).where(TableORM.id == id).values(
                status=status
                ).returning(TableORM)
            result = await session.execute(query)
            await session.commit()
            
            table = result.scalars().one()
            await session.refresh(table)
            
            return table
            
    
    async def delete(self, id: int) -> bool:
        async with self.session as session:
            query = delete(TableORM).where(
                TableORM.id == id
                ).returning(TableORM)
            await session.execute(query)
            await session.commit()
            
            return True
        
    async def get_all_by_status(self, status: TableStatus) -> list[TableORM]:
        async with self.session as session:
            query = select(TableORM).where(TableORM.status==status)
            result = await session.execute(query)
            
            return result.scalars().all()
    