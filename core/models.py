"""Data classes passed between the application layers."""
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class ChatMessage:
    """A text message from a public Telegram channel or chat."""

    chat_username: str
    message_id: int
    date: datetime
    text: str

    def build_link(self) -> str:
        return f"https://t.me/{self.chat_username}/{self.message_id}"
