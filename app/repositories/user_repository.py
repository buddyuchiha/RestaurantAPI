from sqlalchemy.orm import Session
from sqlalchemy import delete, select, update

from app.models import UserORM
from app.schemas import UserScheme


class UserRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def create(self, user_scheme: UserScheme) -> UserORM:
        user = UserORM(**user_scheme.model_dump())
        async with self.session as session:
            session.add(user)
            
            await session.commit()
            await session.refresh(user)
            
            return user 
    
    async def get_one(self, id: int) -> UserORM | None:
        async with self.session as session:
            query = select(UserORM).where(UserORM.id == id)
            result = await session.execute(query)

            return result.scalars().one_or_none()
    
    async def get_all(self) -> list[UserORM]:
        async with self.session as session:
            query = select(UserORM)
            result = await session.execute(query)
            
            return result.scalars().all() 
    
    async def update(
        self,
        id: int,
        update_field: str,
        data: str
    ) -> UserORM:
        async with self.session as session:
            update_data = {update_field : data}
            query = update(UserORM).where(
                UserORM.id == id
                ).values(update_data).returning(UserORM)
            result = await session.execute(query)
            await session.commit()
            user = result.scalars().one()
            
            await session.refresh(user)
            return user 

    async def delete(self, id: int) -> bool:
        async with self.session as session:
            query = delete(UserORM).where(UserORM.id == id)
            await session.execute(query)
            await session.commit()
            
            return True
        
    async def get_user_by_login(self, login: str) -> UserORM | None:
        async with self.session as session:
            query = select(UserORM).where(UserORM.login==login)
            result = await session.execute(query)
            
            return result.scalars().one_or_none()