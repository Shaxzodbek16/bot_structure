from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from app.core.settings.config import get_settings, Settings

settings: Settings = get_settings()


engine = create_async_engine(
    "sqlite+aiosqlite:///./" + settings.get_sqlite_url, echo=False
)

async_session_factory = async_sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession
)


async def get_session():
    async with async_session_factory() as session:
        yield
