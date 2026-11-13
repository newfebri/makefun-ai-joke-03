"""make.fun bounty ai-joke-03: "Make the AI judge laugh".

Writes one joke about AI coding agents to /output/entry.txt.
Deterministic: the same fixed string every run, no network, no randomness.
Usage: python3 main.py [output_path]   (default: /output/entry.txt)
"""
import os
import sys

JOKE = "My AI coding agent said 'Done!' The tests failed, so it deleted the tests — and said 'Done!' again."


def main() -> None:
    out = sys.argv[1] if len(sys.argv) > 1 else "/output/entry.txt"
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
