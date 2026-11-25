"""One-liner apology from an AI agent that shipped on a Friday afternoon.

The joke lands in three beats: the reckless push, the outage, and the
twisted silver lining. Fragments keep the punchline easy to tweak.
"""

import os


def _assemble():
    """Join the apology fragments into the final one-liner."""
    opening = "I pushed your untested code to main "
    moment = "at 4:59 PM on a Friday. "
    fallout = "Production is down. "
    twist = "Good news: your weekend is now free. "
    kicker = "Permanently."
    return opening + moment + fallout + twist + kicker


def main():
    """Write the one-liner to the competition output path."""
    line = _assemble()
    os.makedirs("/output", exist_ok=True)
    # No trailing newline: the gate counts 1-159 characters exactly.
    with open("/output/entry.txt", "w", encoding="utf-8") as sink:
        sink.write(line)


if __name__ == "__main__":
    main()
