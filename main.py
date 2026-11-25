#!/usr/bin/env python3
"""Delete 'moist' from the dictionary.

The single word this entry would erase forever, written to /output/entry.txt
with no trailing newline and nothing else attached.
"""

import os

WORD = "moist"


def chosen_word() -> str:
    """The single word this entry would erase from the dictionary forever."""
    return WORD


def validate(word: str) -> str:
    """Gate: one token, 1-77 chars, no whitespace inside or around."""
    if not (1 <= len(word) <= 77):
        raise ValueError("word must be 1-77 characters")
    if word.split() != [word]:
        raise ValueError("entry must be a single word with no spaces")
    return word


def main() -> None:
    word = validate(chosen_word())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(word)


if __name__ == "__main__":
    main()
