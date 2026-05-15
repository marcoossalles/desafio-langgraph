from pathlib import Path

from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


BACKEND_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=BACKEND_DIR / ".env",
        env_file_encoding="utf-8",
    )

    APP_NAME: str = "Movie AI"

    API_VERSION: str = "/api/v1"

    LOG_LEVEL: str = "INFO"

    TMDB_API_TOKEN: str

    GROQ_API_KEY: str

    LLM_PROVIDER: str = "groq"

    LLM_MODEL: str = "llama3-8b-8192"

    LLM_TEMPERATURE: float = 0.7


settings = Settings()
