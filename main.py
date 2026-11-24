#!/usr/bin/env python3
"""Make the Judge Smile — make.fun text-bounty entry.

Writes one original line (148 characters, at most 200) about a small good
thing that happened today to /output/entry.txt.

Deterministic, standard library only, no network, no randomness.
"""

import os

ENTRY = (
    "The stray cat that never lets anyone near fell asleep on my shoe "
    "this morning, and for ten whole minutes I was the most trusted "
    "person in the world."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} characters"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
