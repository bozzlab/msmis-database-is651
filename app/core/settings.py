from functools import lru_cache
from typing import Any, Optional
from urllib import parse

from pydantic import BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    DB_HOST: str
    DB_USER: str
    DB_PASS: str
    DB_NAME: str
    DB_PORT: str
    DATABASE_URI: Optional[PostgresDsn] = None

    PROJECT_NAME: str = "Pook Moo API"

    API_PATH_STR: str = "/api/v1"

    @validator("DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: dict[str, Any]) -> str:
        if isinstance(v, str):
            return v

        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("DB_USER"),
            password=parse.quote(values.get("DB_PASS")),
            host=values.get("DB_HOST"),
            port=values.get("DB_PORT"),
            path=f"/{values.get('DB_NAME') or ''}",
        )


settings = Settings()


@lru_cache
def get_settings() -> Settings:
    return Settings()
