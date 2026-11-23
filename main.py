"""One-Line Laugh Sprint entry.

Writes one original funny line (<=200 chars) to entry.txt and prints it.
Stdlib only, no network, no randomness, fully deterministic.
"""

import os
import sys

LINE = "My plants have a group chat now. I watered them once in March and they've been gossiping about my commitment issues ever since."


def main():
    # Gate: the entry must be UTF-8 text of 1 to 200 characters, not only whitespace.
    text = LINE.encode("utf-8").decode("utf-8")
    if not (1 <= len(text) <= 200) or not text.strip():
        print("entry line fails the 1-200 character gate", file=sys.stderr)
        return 2
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
