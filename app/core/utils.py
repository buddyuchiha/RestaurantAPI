from passlib.context import CryptContext

from app.core import settings

password_context = CryptContext(schemes=[settings.APP_HASH_ALGORITHM], deprecated="auto")


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_hashed_password(password: str, hashed_password: str) -> bool:
    return password_context.verify(password, hashed_password) 