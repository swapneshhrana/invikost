from functools import lru_cache
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# Dynamically calculate the path location profile by selecting parent index [4]
try:
    ENV_PATH = Path(__file__).resolve().parents[4] / ".env"
except IndexError:
    ENV_PATH = Path("/app/.env")


class Settings(BaseSettings):
    app_name: str = "invikost"
    app_version: str = "2.0.0"
    app_env: str = "development"

    database_url: str | None = Field(default=None)
    redis_url: str | None = Field(default=None)

    model_config = SettingsConfigDict(
        env_file=ENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    return Settings()
