"""Small helpers."""
from pathlib import Path


def read_lines(path: Path) -> list[str]:
    """Return the file's non-empty lines, stripped of surrounding whitespace."""
    lines = path.read_text(encoding="utf-8").splitlines()
    return [line.strip() for line in lines if line.strip()]
