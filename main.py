"""Entry point: wires the dependencies and runs the keyword search."""
import asyncio
from datetime import datetime, timedelta, timezone

from telethon import TelegramClient

from core.adapters import ConsoleReporter, TelethonMessageProvider
from core.constants import CHATS_FILE, DAYS_BACK, KEYWORDS_FILE
from core.services import KeywordMatcher, KeywordSearchService
from core.settings import Settings
from core.utils import read_lines


async def run_parser() -> None:
    settings = Settings()
    chat_usernames = read_lines(CHATS_FILE)
    matcher = KeywordMatcher(read_lines(KEYWORDS_FILE))
    since = datetime.now(timezone.utc) - timedelta(days=DAYS_BACK)

    client = TelegramClient(
        settings.session_name, settings.api_id, settings.api_hash.get_secret_value()
    )
    async with client:  # the first run asks for phone and code; the session is saved to *.session
        service = KeywordSearchService(TelethonMessageProvider(client), matcher, ConsoleReporter())
        await service.run_search(chat_usernames, since)


if __name__ == "__main__":
    asyncio.run(run_parser())
