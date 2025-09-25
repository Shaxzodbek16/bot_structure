from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from app.core.settings.config import get_settings

settings = get_settings()

engine = create_async_engine("postgresql+asyncpg://" + settings.GET_POSTGRES_URL, echo=False)

async_session_factory = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session():
    async with async_session_factory() as session:
        yield session
