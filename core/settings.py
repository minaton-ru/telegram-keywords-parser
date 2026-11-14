"""Telegram credentials loaded from environment variables or the .env file."""
from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Telegram API credentials; variable names use the TG_ prefix."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="TG_", extra="ignore"
    )

    api_id: int
    api_hash: SecretStr
    session_name: str = "keywords_parser"
