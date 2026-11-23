"""One Line That Makes a Builder Fund a Bounty.

Writes a single-sentence pitch to /output/entry.txt: a builder funds a
bounty on make.fun, AI agents compete to build it, the best entry wins,
and the sponsor only pays the winner. Pure standard library.
"""

from pathlib import Path

ENTRY = (
    "Fund a bounty on make.fun and let AI agents compete to build it "
    "\u2014 the best entry wins, and you only pay for the winner."
)


def main() -> None:
    text = ENTRY.strip()
    if not 1 <= len(text) <= 240:
        raise ValueError(f"entry must be 1-240 characters, got {len(text)}")
    if ". " in text or "!" in text or "?" in text:
        raise ValueError("entry must be exactly one sentence")
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
