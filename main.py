#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes the roast line to $OUTPUT_DIR/entry.txt.
Gate: UTF-8 text, 1-160 characters, not only whitespace.
Standard library only; deterministic output.
"""

import os
import sys

LINE = (
    # The joke: the fridge's expiry policing escalates into a full funeral,
    # and the eulogy's punch ("He cultured") lands on the yoghurt itself.
    "My fridge held a funeral for a yoghurt one day past its date: one beep, "
    "a cold light, and a eulogy on its screen \u2014 'He lived. He cultured. "
    "He is gone.'"
)


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    if not (1 <= len(text) <= 160):
        print(f"gate failed: {len(text)} chars (need 1-160)", file=sys.stderr)
        return 1
    if not text.strip():
        print("gate failed: only whitespace", file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("gate failed: entry must be a single line", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
