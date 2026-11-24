"""One-Line Robot Wedding Vows — make.fun entry.

Writes a single line of robot wedding vows to /output/entry.txt.
Python standard library only.
"""

import os
from pathlib import Path

ENTRY = (
    "I vow to love you in sickness and in low battery, to install every "
    "update beside you, and to never factory-reset us \u2014 even when you "
    "blue-screen at dinner."
)


MAX_CHARS = 160


def validate(text: str) -> None:
    """Check the entry against the competition gate before writing."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(ENTRY)
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
