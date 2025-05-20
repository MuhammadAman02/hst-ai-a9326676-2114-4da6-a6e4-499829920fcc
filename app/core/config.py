import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "Medical Chatbot"
    APP_VERSION: str = "1.0.0"
    APP_ENV: str = os.getenv("APP_ENV", "development")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")

    class Config:
        env_file = ".env"

settings = Settings()