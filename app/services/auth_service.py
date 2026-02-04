from datetime import datetime, timedelta
from jose import JWTError, jwt

from app.core import (
    get_hashed_password,
    settings,
    verify_hashed_password,
    WrongPassword
)
from app.core.exception import TokenExpired, TokenNotCorrect
from app.schemas import (
    UserScheme,
    UserSchemeResponse,
    UserLoginScheme,
    TokenResponse
)
from app.services import UserService


class AuthService:
    def __init__(self, user_service: UserService) -> None:
        self.user_service = user_service
    
    async def register_user(self, user: UserScheme) -> UserSchemeResponse:
        hashed_password = get_hashed_password(user.password)
        user.password = hashed_password
        
        return await self.user_service.create_user(user)
    
    async def login_user(self, user: UserLoginScheme) -> TokenResponse:
        db_user = await self.user_service.get_user_by_login(user.login)
        
        if not verify_hashed_password(user.password, db_user.password):
            raise WrongPassword
        
        token = self.generate_access_token(db_user.id)
        
        return TokenResponse(
            access_token=token,
            user_id=db_user.id,
            user_login=db_user.login
        )
    
    def generate_access_token(self, user_id: int) -> str:
        expires_date_unix = (
            datetime.now() + timedelta(
                minutes=settings.APP_ACCESS_TOKEN_EXPIRE_MINUTES
                )
            ).timestamp()
        to_encode = {"user_id" : user_id, "exp" : expires_date_unix}
        
        token = jwt.encode(
            to_encode,
            settings.APP_SECRET_KEY,
            settings.APP_ENCODE_ALGORITHM
        )
        
        return token
    
    def get_user_id_from_access_token(self, access_token: str) -> int: 
        try: 
            payload = jwt.decode(
                access_token,
                settings.APP_SECRET_KEY, 
                algorithms=[settings.APP_ENCODE_ALGORITHM]
            )
        except JWTError:        
            raise TokenNotCorrect
        if payload['exp'] < datetime.now().timestamp():
            raise TokenExpired
        return payload['user_id']
    
    