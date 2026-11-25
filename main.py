"""Have You Tried Turning It Off? — make.fun one-liner entry.

Writes exactly one funny line to /output/entry.txt.
Pure Python standard library only.
"""

import os

LINE = (
    "Don't worry, we'll get through this together. "
    "Have you tried turning it off and on again? "
    "It worked on my printer once, and it is still the highlight of my career."
)


def main() -> None:
    assert 1 <= len(LINE) <= 199, "line must be 1-199 chars"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.chmod(path, 0o644)
    # Verify the file on disk is exactly the intended single line.
    with open(path, encoding="utf-8") as f:
        assert f.read() == LINE, "written output differs from LINE"


if __name__ == "__main__":
    main()
