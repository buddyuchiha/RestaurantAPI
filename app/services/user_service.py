from app.core import UserNotFound
from app.repositories import UserRepository
from app.schemas import UserScheme, UserSchemeResponse


class UserService:
    def __init__(self, user_repository: UserRepository) -> None:
        self.user_repository = user_repository
        
    async def create_user(self, user_scheme: UserScheme) -> UserSchemeResponse:
        user = await self.user_repository.create(user_scheme)
        
        return UserSchemeResponse.model_validate(user)
    
    async def get_user(self, id: int) -> UserSchemeResponse:
        user = await self.user_repository.get_one(id)
        
        return UserSchemeResponse.model_validate(user)
    
    async def get_users(self) -> list[UserSchemeResponse]:
        users = await self.user_repository.get_all()
        
        return [UserSchemeResponse.model_validate(user) for user in users]

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
    
    async def get_user_by_login(self, user_login: str) -> UserScheme:
        user = await self.user_repository.get_user_by_login(user_login)
    
        if not user:
            raise UserNotFound
           
        return UserScheme.model_validate(user)
        