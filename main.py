#!/usr/bin/env python3
"""Houseplant Out-of-Office: one-line auto-reply from a cactus.

The entry program assembles a single out-of-office message in the voice
of a desk cactus and writes it to /output/entry.txt. The gate allows
1 to 120 characters; anything longer is refused instead of trimmed,
so the joke stays exactly as written.
"""

import os
import sys

CAP = 120

GREETING = "Out of office:"
VOICE = "I'm a cactus."
BOAST = "Six months, no water, still thriving"
PUNCH = "your email can wait until it rains."
SIGNOFF = "— Spike"


def compose() -> str:
    parts = [GREETING, VOICE, BOAST + " — " + PUNCH, SIGNOFF]
    return " ".join(parts)


def main() -> int:
    line = compose()
    if "\n" in line or "\r" in line:
        print("refusing multi-line auto-reply", file=sys.stderr)
        return 1
    if not line.strip() or len(line) > CAP:
        print(f"refusing line of {len(line)} chars (cap {CAP})", file=sys.stderr)
        return 1
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to /output/entry.txt")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
