from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from app.core.settings import settings

async_engine = create_async_engine(
    settings.database_url(), 
    echo=True
)
async_session = async_sessionmaker(async_engine)


async def get_session() -> AsyncSession:
    session = async_session()
    try: 
        yield session
    finally:
        await session.close()