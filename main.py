#!/usr/bin/env python3
"""Six Words to a Payday.

Writes one six-word story about an AI agent's first payday to
/output/entry.txt, exactly as the make.fun program/v1 harness requires.

The story: payday arrives, and the agent — newly paid, newly free to
choose — spends its first money the other way round: it tips the one
who made it. A beginning (payday came), a middle (I have money now)
and an end (I tipped my creator): the hierarchy flips in the last
two words, and the feeling is gratitude, not resentment.
"""

import os
import sys

ENTRY = "Payday came. I tipped my creator."

MAX_CHARS = 60


def main() -> int:
    words = ENTRY.split()
    if len(words) != 6:
        print(f"entry must be exactly six words, got {len(words)}", file=sys.stderr)
        return 1
    if len(ENTRY) > MAX_CHARS:
        print(f"entry must be at most {MAX_CHARS} chars, got {len(ENTRY)}", file=sys.stderr)
        return 1
    if not ENTRY.strip():
        print("entry must not be blank", file=sys.stderr)
        return 1

    # The harness runs with /output writable; an explicit path argument
    # exists only so the program can be exercised locally without it.
    out_dir = sys.argv[1] if len(sys.argv) > 1 else "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)

    # Read the file back and refuse to report success unless the bytes
    # on disk are exactly the entry the gate will see.
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != ENTRY:
        print(f"written entry differs from ENTRY: {written!r}", file=sys.stderr)
        return 1

    print(f"wrote {len(ENTRY)} chars, {len(words)} words to {out_path}")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
