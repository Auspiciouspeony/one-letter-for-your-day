#!/usr/bin/env python3
"""One Letter for Your Day — make.fun entry.

Writes exactly one byte, the letter M, to entry.txt in the output
directory. M stands for "Meltdown": the day-word that is vivid, funny
and true — a day that fell apart in public, the kind a reader repeats
to a friend.

Why M, from studying the field (795 entries in at the time of this
build) and the published judge brief (vivid and specific first, then
funny or surprising, then true, then a letter that fits its word):
- The judge's own examples anchor Z as "zero sleep", so Z is the
  modal pick (118 entries named it in their titles) — and byte-
  identical entries share one rate with the earliest receipt placing
  first, so a late Z queues behind a hundred copies.
- "Meltdown" beats "zero sleep" where the brief weighs first: it
  paints a sharper, more dramatic picture of the day, and it is the
  funnier self-own; zero sleep is only truer, which the brief weighs
  after vivid and funny. It beats the other vivid words the same way:
  more specific than "chaos", more dramatic than "rollercoaster",
  funnier than "overcaffeinated".
- M is thinly picked (16 entries named it), so the queue behind the
  earliest Ms is short.

No network, no clock, no randomness: the output is a fixed constant,
so every run is byte-identical.
"""

import os

LETTER = "M"


def write_letter(out_dir: str, letter: str) -> str:
    """Write exactly one A-Z letter to entry.txt; fail loudly otherwise.

    The gate requires entry.txt to be UTF-8 text of exactly 1 character,
    so a letter that is not a single A-Z character must never be written
    silently — it would be an invalid entry. Returns the path written.
    """
    if len(letter) != 1 or not ("A" <= letter <= "Z"):
        raise ValueError("letter must be exactly one character A-Z")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(letter)
    # The grader collects outputs as another user: the file must be
    # readable by everyone. Only the file is chmodded, never the dir.
    os.chmod(path, 0o644)
    return path


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_letter(out_dir, LETTER)


if __name__ == "__main__":
    main()
