from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # General Settings
    APP_NAME: str = "Carbon Tracker API"
    VERSION: str = "1.0.0"

    # API Keys (Replace with real keys in .env)
    GOOGLE_MAPS_API_KEY: str
    OPENAI_API_KEY: str

    # Database Config
    MONGO_URI: str

    # Security
    SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"

    class Config:
        env_file = ".env"  # Load values from .env file

# Initialize settings
settings = Settings()
