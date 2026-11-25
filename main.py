#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun one-liner entry."""
import os

TEXT = "Stuck at home this week: my nephew's GTA 6 pre-order needs an adult signature at delivery."
PATH = "/output/entry.txt"


MAX_WORDS = 20
MAX_CHARS = 140


def assure(text: str) -> str:
    n_words = len(text.split())
    n_chars = len(text)
    if n_words > MAX_WORDS:
        raise SystemExit(f"excuse runs {n_words} words, brief caps at {MAX_WORDS}")
    if n_chars > MAX_CHARS:
        raise SystemExit(f"excuse runs {n_chars} chars, gate caps at {MAX_CHARS}")
    return text


def write_entry() -> None:
    line = assure(TEXT)
    os.makedirs(os.path.dirname(PATH), exist_ok=True)
    with open(PATH, "w", encoding="utf-8") as fh:
        fh.write(line + "\n")
    os.chmod(PATH, 0o644)
    echoed = open(PATH, "r", encoding="utf-8").read().strip()
    print(f"excuse on disk: {len(echoed)} chars, {len(echoed.split())} words")


write_entry()
