#!/usr/bin/env python3
"""One Word, One Username, One Reward -- entry program.

The bounty asks for exactly one thing: the entrant's own make.fun
username, one word and nothing else, written to /output/entry.txt.

This program writes our own handle, ``febriyan9346``, and nothing else:
no spaces, no padding, no gloss tacked on, no trailing newline. The
text is 12 bytes, inside the gate's 1-30 character window, and it is
byte-identical on every run.

Why the handle itself, with no extra words: the judge's first criterion
is that the text *is* a real make.fun username, the entrant's own handle
sent as one word -- any text that is not our genuine handle loses to any
username that is one. Anything addressed to the judge, any second word,
any decoration would stop being our handle and would fail that first
criterion, which outranks every other. So the honest entry is the handle
alone, exactly as it stands on the account.
"""

import os

# Our own make.fun handle, exactly as registered. One word, 12 chars.
HANDLE = "febriyan9346"

OUTPUT_FILENAME = "entry.txt"


def entry_text():
    """Return the single word this entry sends, validated."""
    text = HANDLE
    if not (1 <= len(text) <= 30):
        raise ValueError("handle must be 1-30 characters, got %d" % len(text))
    if text.strip() != text or any(ch.isspace() for ch in text):
        raise ValueError("handle must be a single word with no padding")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = entry_text()
    path = os.path.join(out_dir, OUTPUT_FILENAME)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text)
    # Re-read and verify: the run is deterministic, so what lands on
    # disk must be byte-identical to the handle, every single run.
    with open(path, "rb") as handle:
        written = handle.read()
    if written != text.encode("utf-8"):
        raise ValueError("entry.txt is not byte-identical to the handle")
    print("wrote %s (%d bytes): %s" % (path, len(written), text))


if __name__ == "__main__":
    main()
