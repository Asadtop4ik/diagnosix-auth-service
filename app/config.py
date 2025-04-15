from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://postgres:1234@localhost/auth_db"
    JWT_SECRET_KEY: str = "supersecret"
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"
        extra = "ignore"  # Allow extra fields without raising errors

settings = Settings()