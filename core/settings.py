"""Telegram credentials and run parameters loaded from environment variables or the .env file."""
from pathlib import Path

from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Telegram API credentials and run parameters; variable names use the TG_ prefix."""

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", env_prefix="TG_"
    )

    api_id: int
    api_hash: SecretStr
    session_name: str = "keywords_parser"
    days_back: int = 2
    chats_file: Path = Path("chats.txt")
    keywords_file: Path = Path("keywords.txt")
