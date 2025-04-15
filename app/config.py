from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:1234@localhost/auth_db"
    JWT_SECRET_KEY: str = "supersecret"
    JWT_ALGORITHM: str = "HS256"

    model_config = ConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()