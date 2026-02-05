import json

from app.core import UserNotFound
from app.repositories import UserRepository
from app.schemas import UserScheme, UserSchemeResponse
from app.schemas.user import UserCreateScheme
from app.services.cache_service import CacheService


class UserService:
    def __init__(
        self, 
        user_repository: UserRepository,
        cache_service: CacheService
    ) -> None:
        self.user_repository = user_repository
        self.cache_service = cache_service
        
    async def create_user(self, user_scheme: UserScheme) -> UserSchemeResponse:
        user = await self.user_repository.create(user_scheme)
        
        return UserSchemeResponse.model_validate(user)
    
    async def get_user(self, id: int) -> UserSchemeResponse:
        user = await self.user_repository.get_one(id)
        
        return UserSchemeResponse.model_validate(user)
    
    async def get_users(self) -> list[UserSchemeResponse]:
        if users := await self.cache_service.get_values("users"):
            return [
                UserSchemeResponse.model_validate(json.loads(user)) \
                    for user in users  
            ]
        
        users = await self.user_repository.get_all()
        serialazied_users = [
            UserSchemeResponse.model_validate(user) \
                for user in users
        ]
        
        await self.cache_service.set_values(
            "users",
            serialazied_users,
            UserSchemeResponse
        )
        
        return serialazied_users

    async def update_user(
        self,
        id: int,
        update_field: str,
        data: str
    ) -> UserSchemeResponse:
        user = await self.user_repository.update(id, update_field, data)
        
        return UserSchemeResponse.model_validate(user)
    
    async def delete_user(self, id: int) -> bool:
        return await self.user_repository.delete(id)
    
    async def get_user_by_login(self, user_login: str) -> UserCreateScheme:
        user = await self.user_repository.get_user_by_login(user_login)
    
        if not user:
            return False
           
        return UserCreateScheme.model_validate(user)
    
        