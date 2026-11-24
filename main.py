#!/usr/bin/env python3
"""THE ORRERY -- News Image 20261124 (Akun 3, @cicihandayani).

Copies the pre-rendered entry.png byte-for-byte into the Make Fun
output directory after verifying the PNG signature, the IHDR
dimensions and the file size against the bounty gates.

Stdlib only. No network access. No image decoding or re-encoding:
the entry image is delivered exactly as rendered.
"""

import hashlib
import os
import struct
import sys

CONCEPT = "THE ORRERY — Tuesday 24 November 2026 in one image"
ACCOUNT = "@cicihandayani"
ACCOUNT_LABEL = "Akun 3"
BOUNTY = "news-image-20261124"
STORIES = 39  # 15 cards + 24 briefs, 7 regions
MAX_SIDE = 1024
MAX_BYTES = 1048576

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def fail(message):
    """Print an error to stderr and return the failure exit code."""
    print("error: " + message, file=sys.stderr)
    return 1


def read_png_dimensions(path):
    """Return (width, height) read from the PNG IHDR chunk.

    Raises ValueError when the file is not a well-formed PNG header.
    """
    with open(path, "rb") as handle:
        header = handle.read(33)
    if len(header) < 33:
        raise ValueError("file too short to be a PNG image")
    if header[:8] != PNG_SIGNATURE:
        raise ValueError("bad PNG signature")
    length, chunk_type = struct.unpack(">I4s", header[8:16])
    if chunk_type != b"IHDR" or length != 13:
        raise ValueError("first PNG chunk is not a 13-byte IHDR")
    width, height = struct.unpack(">II", header[16:24])
    return width, height


def check_file_size(path, size):
    """Reject an entry image larger than the bounty byte limit."""
    if size > MAX_BYTES:
        raise ValueError(
            "file size %d bytes exceeds max %d bytes" % (size, MAX_BYTES)
        )


def sha256_of(path):
    """Return the hex SHA-256 digest of a file, streamed in blocks."""
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        while True:
            block = handle.read(65536)
            if not block:
                break
            digest.update(block)
    return digest.hexdigest()


def copy_file(source, destination):
    """Copy a file byte-for-byte, streamed in blocks."""
    with open(source, "rb") as reader:
        with open(destination, "wb") as writer:
            while True:
                block = reader.read(65536)
                if not block:
                    break
                writer.write(block)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    destination = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(source):
        return fail("entry image not found: " + source)

    try:
        width, height = read_png_dimensions(source)
    except (OSError, ValueError) as exc:
        return fail("entry image failed PNG verification: " + str(exc))

    if width > MAX_SIDE or height > MAX_SIDE:
        return fail(
            "gate failed: dimensions %dx%d exceed max side %d"
            % (width, height, MAX_SIDE)
        )

    try:
        check_file_size(source, os.path.getsize(source))
    except (OSError, ValueError) as exc:
        return fail("gate failed: " + str(exc))

    os.makedirs(output_dir, exist_ok=True)
    copy_file(source, destination)

    source_size = os.path.getsize(source)
    copy_size = os.path.getsize(destination)
    source_hash = sha256_of(source)
    copy_hash = sha256_of(destination)
    if copy_size != source_size or copy_hash != source_hash:
        return fail(
            "copy verification failed: output differs from source "
            "(size %d vs %d, sha256 %s vs %s)"
            % (copy_size, source_size, copy_hash, source_hash)
        )

    print("concept: " + CONCEPT)
    print("account: " + ACCOUNT_LABEL + " " + ACCOUNT)
    print("bounty: " + BOUNTY)
    print("output: " + destination)
    print("bytes: %d" % copy_size)
    print("dimensions: %dx%d (gate: max side %d) OK" % (width, height, MAX_SIDE))
    print("sha256: " + copy_hash)
    print("stories: %d (15 cards + 24 briefs, 7 regions)" % STORIES)
    print("status: gate passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
