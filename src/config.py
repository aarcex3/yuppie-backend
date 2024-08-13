"""
App dependecies
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """App settings"""

    DB_URL: str
    SECRET_KEY: str

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


SETTINGS = Settings()
