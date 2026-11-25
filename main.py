"""Robot Romance one-liner entry.

Reads the single pickup line from entry.txt next to this script and
copies it byte-identically to $MAKEFUN_OUTPUT_DIR/entry.txt (mode 0644).
Stdlib only, no temp files, no network.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.txt")
    try:
        with open(src, "rb") as f:
            data = f.read()
    except OSError as exc:
        print(f"cannot read {src}: {exc}", file=sys.stderr)
        raise SystemExit(1)
    if not data.strip():
        print("entry.txt is empty or whitespace-only", file=sys.stderr)
        raise SystemExit(1)
    try:
        out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    except KeyError:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    with open(dst, "wb") as f:
        f.write(data)
    os.chmod(dst, 0o644)


if __name__ == "__main__":
    main()
