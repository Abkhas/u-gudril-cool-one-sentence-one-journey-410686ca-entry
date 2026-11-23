"""One Sentence, One Journey — entry program.

Writes a single complete story about a journey, told in exactly one
sentence, to the output file the gate reads. The sentence is embedded
here as a literal: 254 characters, one terminal full stop, no title,
no second sentence.
"""

import os
import re
import sys

SENTENCE = (
    "The ferry left the harbour at first light with her wedding ring "
    "still in her pocket and her husband's voice still in her ears, "
    "and when the island rose out of the mist she threw the ring into "
    "the grey water and laughed for the first time in eleven years."
)

GATE_MIN_CHARS = 1
GATE_MAX_CHARS = 300


def fail(message):
    print("entry rejected: " + message, file=sys.stderr)
    raise SystemExit(1)


def main():
    text = SENTENCE.strip()

    if not (GATE_MIN_CHARS <= len(text) <= GATE_MAX_CHARS):
        fail("entry is %d chars, gate needs %d-%d" % (len(text), GATE_MIN_CHARS, GATE_MAX_CHARS))

    stops = re.findall(r"[.!?]", text)
    if len(stops) != 1 or not text.endswith(stops[0]):
        fail("entry must be exactly one sentence ending in its only stop")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(text)

    print("wrote %s (%d chars, 1 sentence)" % (out_path, len(text)))


if __name__ == "__main__":
    main()
