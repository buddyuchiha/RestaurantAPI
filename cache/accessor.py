from typing import AsyncGenerator
from redis import asyncio as redis

from app.core import settings


async def get_cache_session() -> AsyncGenerator[redis.Redis]:
    cache_session = redis.Redis(
       host=settings.REDIS_HOST,
       port=settings.REDIS_PORT,
       password=settings.REDIS_PASSWORD
    )
    try:
        yield cache_session
    finally:
        await cache_session.close()