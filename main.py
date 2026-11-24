#!/usr/bin/env python3
"""The Houseplant Out-of-Office — make.fun entry.

Writes one out-of-office auto-reply, as if a houseplant sent it, to
/output/entry.txt. Standard library only; fully deterministic: the same
bytes on every run.
"""

import os

LINE = (
    "Out of office: I died in March. "
    "This inbox is now a terrarium. "
    "Queries go to the cactus. "
    "It doesn't care either."
)


def main() -> None:
    # The gate allows 1 to 120 characters; fail loudly instead of
    # shipping a line the gate would refuse.
    assert 1 <= len(LINE) <= 120, f"entry is {len(LINE)} characters"
    assert "\n" not in LINE, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
