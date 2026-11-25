#!/usr/bin/env python3
"""THE DATELINE — entry program for news-image-20261124 (Akun 3, @cicihandayani).

The entry is a single built image: the program copies ``entry.png`` from this
repository into the output directory the harness provides. It draws nothing,
fetches nothing, and needs no network: the picture was composed beforehand
from Tuesday 24 November 2026's reported news (36 dated stories, 9 regions).

Usage:
    MAKEFUN_OUTPUT_DIR=out python3 main.py
    python3 main.py out

The program runs twice and both runs must write the same bytes; copying the
same file twice satisfies that by construction. Only the standard library is
used, so the program runs in the grading sandbox exactly as it runs here.
"""
import hashlib
import os
import shutil
import struct
import sys

EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def _repo_dir():
    return os.path.dirname(os.path.abspath(__file__))


def _output_dir(argv):
    env = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR")
    if env:
        return env
    if len(argv) > 1:
        return argv[1]
    return "out"


def _read_header(path):
    """Return (width, height) from the PNG IHDR chunk, or raise ValueError."""
    with open(path, "rb") as handle:
        head = handle.read(33)
    if len(head) < 33 or head[:8] != PNG_MAGIC:
        raise ValueError("entry.png is not a PNG file")
    chunk_type = head[12:16]
    if chunk_type != b"IHDR":
        raise ValueError("entry.png has no IHDR chunk first")
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def _sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for block in iter(lambda: handle.read(65536), b""):
            digest.update(block)
    return digest.hexdigest()


def copy_entry():
    source = os.path.join(_repo_dir(), "entry.png")
    if not os.path.isfile(source):
        raise FileNotFoundError("entry.png is missing from the repository")
    width, height = _read_header(source)
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        raise ValueError(
            "entry.png is %dx%d, expected %dx%d"
            % (width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )
    before = _sha256(source)
    source_bytes = os.path.getsize(source)
    target_dir = _output_dir(sys.argv)
    os.makedirs(target_dir, exist_ok=True)
    target = os.path.join(target_dir, "entry.png")
    shutil.copyfile(source, target)
    after = _sha256(target)
    if before != after or os.path.getsize(target) != source_bytes:
        raise ValueError("copied entry.png differs from the repository file")
    print("copied entry.png (%dx%d, %d bytes, sha256 %s) to %s"
          % (width, height, source_bytes, after, target))
    return 0


if __name__ == "__main__":
    raise SystemExit(copy_entry())
