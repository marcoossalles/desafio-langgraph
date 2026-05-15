from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    APP_NAME: str = "Movie AI"

    API_VERSION: str = "/api/v1"

    LOG_LEVEL: str = "INFO"

    TMDB_API_TOKEN: str

    GROQ_API_KEY: str

    LLM_PROVIDER: str = "groq"

    LLM_MODEL: str = "llama3-8b-8192"

    LLM_TEMPERATURE: float = 0.7

    class Config:

        env_file = ".env"


settings = Settings()