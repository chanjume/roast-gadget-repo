#!/usr/bin/env python3
"""One-Line Roast: The Gadget You Use Every Day.

Writes a single original one-line roast to /output/entry.txt.
The gate requires 1-200 UTF-8 characters, not only white space.
The line roasts the phone: it warns storage is full, then tries to
sell cloud space for photos it already backed up twice — the phone
manufactures the problem, then sells the fix.
"""
import os

LINE = (
    "My phone says storage is full, then tries to sell me cloud "
    "space for the photos it already backed up twice."
)


def main():
    assert 1 <= len(LINE) <= 200, "entry must be 1-200 characters"
    assert LINE.strip() == LINE, "no leading/trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
