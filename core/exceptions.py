"""Application-level exceptions."""


class ChatUnavailableError(Exception):
    """The chat is missing, private or otherwise unavailable."""
