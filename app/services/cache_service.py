from typing import Any, Type
from pydantic import TypeAdapter
import redis

from app.core import settings


class CacheService:
    def __init__(self, cache_connection: redis.Redis) -> None:
        self.cache_connection = cache_connection
        
    async def get_values(self, key: str) -> list[any] | None:
        values_json = await self.cache_connection.get(key)
        
        return values_json 
    
    async def set_values(
        self,
        key: str,
        data: list[Any],
        scheme_type: Type[Any]
    ) -> None:
        adapter = TypeAdapter(scheme_type)
        serialized_data = adapter.dump_json(data)
        
        await self.cache_connection.set(
            key,
            serialized_data,
            ex=settings.REDIS_EXP
        )
        