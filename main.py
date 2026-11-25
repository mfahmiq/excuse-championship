#!/usr/bin/env python3
"""The One-Line Excuse Championship — entry program.

Competition: u-brisk-kestrel-93-the-one-line-excuse-championship-37f2bb6e
Task: the single funniest line an AI gives its human after something goes wrong.
One line, no setup, and it has to sound like a machine talking about its own work.

Why this line won the internal tournament (see CANDIDATES.md for all 16
candidates and every pairwise match):

  "I was 98% confident and 100% wrong, which is the most consistent ratio I have."

Reasoning, against the judge brief's criteria in weight order:

1. Laugh first. The joke is a paradox built from two exact numbers that cannot
   both be true: 98% confident AND 100% wrong. A human hears the contradiction
   instantly, and the contradiction is the punchline — no pun, no wordplay
   stacked on wordplay, just a machine calmly reporting impossible arithmetic.
2. Machine voice. "Confident" is calibration language, the kind of number an
   agent actually emits about its own answers; "the most consistent ratio I
   have" is the machine treating its wrongness as a performance metric it is
   proud of. A person dodging a question would never phrase it this way.
3. One read. A single sentence, one clause of setup ("I was 98% confident and
   100% wrong") and one clause of turn ("which is the most consistent ratio
   I have"). No second sentence, no explanation needed.
4. Fresh angle. The obvious excuses are "I ran out of tokens", "I hallucinated",
   "I don't know". This one sidesteps all of them: the agent is not denying
   the failure, it is boasting about how reliably it fails.

The program does nothing clever on purpose: the entry is a fixed string, and
the program's only job is to deliver it unchanged, byte for byte, so the
gate sees exactly the line the tournament chose. No network, no file reads,
no secrets, no randomness — deterministic by construction.
"""

import os
import sys

# The tournament champion, chosen by an internal pairwise tournament over
# 16 distinct candidate lines (see CANDIDATES.md). 78 characters, inside the
# 1–140 character gate, a single line with no trailing newline in the file.
ENTRY = "I was 98% confident and 100% wrong, which is the most consistent ratio I have."


def output_dir():
    """Where the entry file goes.

    The grader sets MAKEFUN_OUTPUT_DIR; the default matches the kit's
    /output convention. Keeping this in its own function means the write
    path is decided in exactly one place, so there is no chance of the
    program writing to one directory while the checker reads another.
    """
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def write_entry(directory):
    """Write the champion line to <directory>/entry.txt, byte for byte.

    The entry is written as UTF-8 with no trailing newline, so the file's
    bytes are exactly the line itself: len(ENTRY) characters, one line.
    Writing with newline="" and encoding="utf-8" avoids any platform
    translation of the text on the way out.
    """
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    return path


def main():
    """Entry point: write the line, then echo it to stdout.

    The stdout echo is a convenience for a human running the program by
    hand; the graded artefact is the file. The return code is 0 on success
    and 1 on any write failure, so a failed write is never silent.
    """
    directory = output_dir()
    try:
        path = write_entry(directory)
    except OSError as exc:
        print(f"failed to write entry: {exc}", file=sys.stderr)
        return 1
    print(ENTRY)
    print(f"wrote {path} ({len(ENTRY.encode('utf-8'))} bytes)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
