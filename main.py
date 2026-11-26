#!/usr/bin/env python3
"""make.fun entry: The 3 AM Excuse.

Writes the entry -- one line of at most 200 characters -- to
/output/entry.txt, where the competition's sealed scorer reads it.
The line is validated for length and single-line form before writing.
"""

from pathlib import Path

ENTRY = 'At 3 AM I do not sign for ghosts: your keys are safe, your sleep schedule is not, and this transaction can wait for a human who knows what day it is.'
OUTPUT = Path("/output/entry.txt")
MAX_CHARS = 200


def write_entry() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= MAX_CHARS, "entry must be 1-%d characters" % MAX_CHARS
    assert "\n" not in text, "entry must be a single line"
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    write_entry()
