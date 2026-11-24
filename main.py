"""One-sentence absurd invention pitch.

Writes a single sentence pitching a ridiculous invention that fixes a
tiny everyday annoyance (the lonely sock that never finds its pair)
to /output/entry.txt. Deterministic, standard library only.
"""

import os

PITCH = (
    "Behold SockMatch: a washing machine with a tiny dating app that "
    "pairs up lonely socks before the spin cycle, so every sock leaves "
    "holding hands with its soulmate."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH.strip()
    assert text, "pitch must not be empty"
    assert len(text) <= 220, "pitch must be at most 220 characters"
    assert text.count(".") == 1 and text.endswith("."), "pitch must be one sentence"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")


if __name__ == "__main__":
    main()
