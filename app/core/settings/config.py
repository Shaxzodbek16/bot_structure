from functools import cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DEBUG: bool = False
    BOT_TOKEN: str = "bot_token"

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DATABASE: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    ADMINS: str = "123456"

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def GET_ADMINS(self) -> list[int]:
        admins = []
        for admin in self.ADMINS.split(","):
            admin = admin.strip()
            try:
                admins.append(int(admin))
            except ValueError:
                continue
        return admins

    @property
    def GET_POSTGRES_URL(self):
        return f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"

    @property
    def BASE_DIRECTORY(self) -> Path:
        return Path(__file__).parent.parent.parent.parent


@cache
def get_settings() -> Settings:
    return Settings()
