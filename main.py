#!/usr/bin/env python3
"""THE COPPERPLATE - NI24 Wave 2 carrier (Akun 3, @cicihandayani).

Stdlib-only carrier: reads entry.png from this same directory, verifies
the server gate (PNG signature, IHDR 1024x1024, at most 1 MiB), then
writes the image bytes exactly, unchanged, to stdout.
"""
import struct
import sys
from pathlib import Path

MAX_BYTES = 1024 * 1024
EXPECTED_W = 1024
EXPECTED_H = 1024


def main() -> int:
    path = Path(__file__).resolve().parent / "entry.png"
    data = path.read_bytes()
    if len(data) > MAX_BYTES:
        print(f"gate fail: {len(data)} bytes > {MAX_BYTES}", file=sys.stderr)
        return 1
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        print("gate fail: not a PNG", file=sys.stderr)
        return 1
    if data[12:16] != b"IHDR":
        print("gate fail: missing IHDR", file=sys.stderr)
        return 1
    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_W, EXPECTED_H):
        print(f"gate fail: {width}x{height} != {EXPECTED_W}x{EXPECTED_H}", file=sys.stderr)
        return 1
    sys.stdout.buffer.write(data)
    sys.stdout.buffer.flush()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
