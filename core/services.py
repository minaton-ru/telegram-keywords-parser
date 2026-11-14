"""Search logic; depends only on the abstract contracts."""
import re
import sys
from collections.abc import Iterable
from datetime import datetime

from core.exceptions import ChatUnavailableError
from core.interfaces import MessageProvider, Reporter


class KeywordMatcher:
    """Checks whether a text contains at least one keyword (whole word, case-insensitive)."""

    _WORD_RE = re.compile(r"[\w-]+")

    def __init__(self, keywords: Iterable[str]) -> None:
        self._keywords = frozenset(keyword.lower() for keyword in keywords)

    def match_text(self, text: str) -> bool:
        words = self._WORD_RE.findall(text.lower())
        return any(word in self._keywords for word in words)


class KeywordSearchService:
    """Walks the chats and passes messages containing keywords to the reporter."""

    def __init__(
        self, provider: MessageProvider, matcher: KeywordMatcher, reporter: Reporter
    ) -> None:
        self._provider = provider
        self._matcher = matcher
        self._reporter = reporter

    async def run_search(self, chat_usernames: Iterable[str], since: datetime) -> None:
        for chat_username in chat_usernames:
            try:
                async for message in self._provider.fetch_messages(chat_username, since):
                    if self._matcher.match_text(message.text):
                        self._reporter.report_message(message)
            except ChatUnavailableError as error:
                print(f"[{chat_username}] skipped: {error}", file=sys.stderr)
