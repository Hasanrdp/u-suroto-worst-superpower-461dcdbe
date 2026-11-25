#!/usr/bin/env python3
"""Worst Superpower entry for make.fun competition
u-suroto-worst-superpower-461dcdbe.

The program writes one line -- the most useless superpower -- to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt). The text is fixed,
deterministic, and verified against its pinned byte count and SHA-256
before it is written, so both grader runs produce identical bytes.

Entry (77 characters, 77 bytes, one line, no trailing newline):
    I can summon rain, but only inside umbrellas that people have already closed.

Why it is useless: rain summoned into an umbrella that is already closed
wets nobody, waters nothing, and helps no one -- the power achieves
exactly nothing, and the closed umbrella is the one place rain can do no
good at all.
"""

import hashlib
import os
import sys

ENTRY = "I can summon rain, but only inside umbrellas that people have already closed."

# Pinned expectations for the entry output (exact bytes, no trailing newline).
EXPECTED_BYTES = 77
EXPECTED_SHA256 = "f615828526806afbb2a0e157a851cd9417347aae480330e5f01cc36d572a048c"


def verify(text: str) -> bytes:
    """Check the entry text against the gate and the pinned hash."""
    if not (1 <= len(text) <= 140):
        raise SystemExit(f"entry is {len(text)} characters, must be 1-140")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if text != text.strip():
        raise SystemExit("entry must not be only whitespace or padded")
    data = text.encode("utf-8")
    if len(data) != EXPECTED_BYTES:
        raise SystemExit(f"entry is {len(data)} bytes, expected {EXPECTED_BYTES}")
    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_SHA256:
        raise SystemExit(f"entry sha256 {digest} != expected {EXPECTED_SHA256}")
    return data


def main() -> int:
    data = verify(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as fh:
        fh.write(data)
    print(f"wrote {len(data)} bytes to {path} sha256={EXPECTED_SHA256}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
