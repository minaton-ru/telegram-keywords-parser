"""Abstract contracts the search service depends on."""
from abc import ABC, abstractmethod
from collections.abc import AsyncIterator
from datetime import datetime

from core.models import ChatMessage


class MessageProvider(ABC):
    """Provides a chat's messages that are no older than the given moment."""

    @abstractmethod
    def fetch_messages(self, chat_username: str, since: datetime) -> AsyncIterator[ChatMessage]:
        pass


class Reporter(ABC):
    """Outputs a message that matched the keywords."""

    @abstractmethod
    def report_message(self, message: ChatMessage) -> None:
        pass
