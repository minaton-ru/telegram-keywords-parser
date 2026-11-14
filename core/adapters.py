"""Implementations of the contracts that talk to the outside world."""
from collections.abc import AsyncIterator
from datetime import datetime

from telethon import TelegramClient
from telethon.errors import RPCError

from core.exceptions import ChatUnavailableError
from core.interfaces import MessageProvider, Reporter
from core.models import ChatMessage


class TelethonMessageProvider(MessageProvider):
    """Telethon adapter: yields a chat's text messages, newest first."""

    def __init__(self, client: TelegramClient) -> None:
        self._client = client

    async def fetch_messages(
        self, chat_username: str, since: datetime
    ) -> AsyncIterator[ChatMessage]:
        try:
            async for message in self._client.iter_messages(chat_username):
                if message.date < since:
                    break
                if message.raw_text:  # text or media caption; service messages are skipped
                    yield ChatMessage(chat_username, message.id, message.date, message.raw_text)
        except (ValueError, RPCError) as error:
            raise ChatUnavailableError(str(error)) from error


class ConsoleReporter(Reporter):
    """Prints the local date and the link of a message to the terminal."""

    def report_message(self, message: ChatMessage) -> None:
        print(f"{message.date.astimezone():%Y-%m-%d %H:%M}  {message.build_link()}")
