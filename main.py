#!/usr/bin/env python3
"""The Dog Reviews the Mailman.

Writes one funny one-line review a dog gives the mailman to
/output/entry.txt. Deterministic, standard library only.
"""

import os

# v3: concrete identifiers only a dog would track (uniform, bag, slot)
# plus a dog-logic count ("in 400 visits") so the joke belongs to this
# dog and this mailman (criteria 3 and 5), keeping v2's escalating end.
LINE = (
    "One star. Same uniform, same bag, same paper through the slot, "
    "and in 400 visits he has never once brought me a treat. "
    "Tomorrow I bark twice as loud."
)


def main() -> None:
    text = LINE.strip()
    assert text, "entry must not be empty"
    assert len(text) <= 200, "entry must be under 200 characters"
    assert text.isascii(), "entry must be plain ASCII"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
