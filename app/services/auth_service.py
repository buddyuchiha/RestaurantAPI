from app.core import (
    get_hashed_password,
    verify_hashed_password,
    WrongPassword
)
from app.schemas import UserScheme, UserSchemeResponse, UserLoginScheme
from app.services import UserService


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service
    
    async def register_user(self, user: UserScheme) -> UserSchemeResponse:
        hashed_password = get_hashed_password(user.password)
        user.password = hashed_password
        
        return await self.user_service.create_user(user)
    
    async def login_user(self, user: UserLoginScheme) -> bool:
        db_user = await self.user_service.get_user_by_login(user.login)
        
        if not verify_hashed_password(user.password, db_user.password):
            raise WrongPassword
        
        return True
    
    
    
    