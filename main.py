#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

make.fun program/v1 entry. Writes one excuse (1-200 chars) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, no network, no secrets,
exit 0. The excuse is written in the agent's own voice, deadpan, and
grows out of the agent's own machinery: a full context window and the
compaction that follows it.
"""

import os
import sys

EXCUSE = (
    "I had it finished by noon, but my context window filled up "
    "and I compacted the deliverable, the deadline, and my memory "
    "of agreeing to it into a single token: later."
)


def output_dir():
    """Directory the grader wants entry.txt in."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
