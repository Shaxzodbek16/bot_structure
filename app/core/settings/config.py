from functools import cache
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    BOT_TOKEN: str = "bot_token"

    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = "postgres"
    POSTGRES_DATABASE: str = "postgres"
    POSTGRES_HOST: str = "localhost"
    POSTGRES_PORT: int = 5432

    ADMINS: str = "123456"

    # If you use sqlite, you can use this:
    SQLITE_DATABASE_NAME: str = "db.sqlite3"

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def admins(self):
        admins = []
        for admin in self.ADMINS.split(","):
            admin = admin.strip()
            admins.append(int(admin))
        return admins

    @property
    def get_postgres_url(self):
        return f"{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DATABASE}"

    @property
    def get_sqlite_url(self):
        return str(self.SQLITE_DATABASE_NAME)


@cache
def get_settings() -> Settings:
    return Settings()
