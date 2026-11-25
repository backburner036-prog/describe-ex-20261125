"""Entry for make.fun bounty "Describe Your Ex in One Word".

The bounty asks for a single word that describes an ex, judged on
comic punch, surprise, craft, and recognition. Our verdict is
"Recalled": an ex like a defective product the factory had to pull
back off the shelves -- do not use, dangerous, return it.

This program writes that one word to /output/entry.txt, validating
it first (1-111 UTF-8 characters, no surrounding whitespace, no
newlines) and checking the write by reading it back.
"""

from pathlib import Path

TEXT = "Recalled"

OUTPUT = Path("/output/entry.txt")


def validate(text: str) -> None:
    """Reject anything that is not a clean single word within the gate."""
    if not text:
        raise ValueError("entry text must not be empty")
    if text != text.strip():
        raise ValueError("entry text must not have leading/trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must not contain a newline")
    if any(ch.isspace() for ch in text):
        raise ValueError("entry text must be a single word (no whitespace)")
    n_bytes = len(text.encode("utf-8"))
    if not 1 <= n_bytes <= 111:
        raise ValueError(
            f"entry must be 1-111 UTF-8 characters (gate limit), got {n_bytes}"
        )


def main() -> None:
    validate(TEXT)
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(TEXT, encoding="utf-8")
    round_trip = OUTPUT.read_text(encoding="utf-8")
    assert round_trip == TEXT, "round-trip check failed: file content differs"
    print(f"Wrote {len(TEXT)} characters to {OUTPUT}: {TEXT!r}")


if __name__ == "__main__":
    main()
