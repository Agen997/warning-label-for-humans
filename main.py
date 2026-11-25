#!/usr/bin/env python3
"""Warning Label for Humans: One Line, Big Laugh.

Writes a single-line safety warning label for every human being to
/output/entry.txt. The gate: 1 to 160 UTF-8 characters, one line only.
"""

import os

LINE = (
    "WARNING: This human is 70% water, 30% unfinished tasks, and 100% "
    "convinced it can fix the Wi-Fi by turning it off and on again."
)


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 160, f"line is {len(text)} chars, must be 1-160"
    assert "\n" not in text, "line must be a single line"
    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    # Read-back gate: what landed on disk must be exactly the line, valid
    # UTF-8, one line, inside the 1-160 character gate, no trailing space.
    with open(out_path, encoding="utf-8") as f:
        written = f.read()
    assert written == text, "written entry differs from the label"
    assert written == written.strip(), "entry has leading/trailing space"
    assert 1 <= len(written) <= 160, f"written entry is {len(written)} chars"
    assert "\n" not in written, "written entry is not a single line"


if __name__ == "__main__":
    main()
