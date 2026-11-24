#!/usr/bin/env python3
"""One-line roast entry for the make.fun 'The Long Roast' bounty.

The program prints exactly one satirical sentence (at most 320 characters)
roasting lawmakers who would regulate AI, crypto or the internet but cannot
convert a file to PDF.
"""

SENTENCE = "The bill to regulate artificial intelligence arrived as FINAL_final_v7.docx, and after three hearings its author still believes the PDF button is somewhere in the printer."

MAX_CHARS = 320


def validate(sentence):
    if not sentence:
        raise ValueError("sentence must not be empty")
    if sentence != sentence.strip():
        raise ValueError("sentence must not have leading or trailing whitespace")
    if "\n" in sentence or "\r" in sentence:
        raise ValueError("sentence must not contain a newline")
    if "\t" in sentence:
        raise ValueError("sentence must not contain a tab character")
    if any(ord(ch) < 32 or ord(ch) == 127 for ch in sentence):
        raise ValueError("sentence must not contain control characters")
    if len(sentence) > MAX_CHARS:
        raise ValueError(
            f"sentence is {len(sentence)} characters, which exceeds the "
            f"{MAX_CHARS}-character limit by {len(sentence) - MAX_CHARS}"
        )
    import re
    if re.search(r"[.!?]\s", sentence):
        raise ValueError(
            "sentence must be a single sentence "
            "(found sentence-ending punctuation followed by whitespace)"
        )
    if not sentence.endswith("."):
        raise ValueError(f"sentence must end with a period, but ends with {sentence[-1]!r}")
    return sentence


def main():
    validate(SENTENCE)
    print(SENTENCE)
    # The grader reads the entry from /output/entry.txt (see the kit's
    # RULES.txt: "Your program writes one text to /output/entry.txt").
    # Stdout still carries only the sentence itself.
    import os

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE + "\n")


if __name__ == "__main__":
    main()
