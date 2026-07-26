#!/usr/bin/env python3
"""Parse builders.md Overview table → JSON list of {name, handle, profile_url}."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROW_RE = re.compile(
    r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*`?@?([A-Za-z0-9_]+)`?\s*\|\s*"
    r"(?:[^|]*\|\s*)?(https://x\.com/[A-Za-z0-9_]+)\s*\|"
)
# Overview rows: | # | Name | Handle | Role | Profile |
ROW_RE_FULL = re.compile(
    r"^\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*`@?([A-Za-z0-9_]+)`\s*\|\s*[^|]*\|\s*"
    r"(https://x\.com/[A-Za-z0-9_]+)\s*\|"
)
# Fallback: handle + profile only
HANDLE_URL_RE = re.compile(
    r"`@([A-Za-z0-9_]+)`.*?(https://x\.com/[A-Za-z0-9_]+)"
)


def parse(text: str) -> list[dict[str, str]]:
    builders: list[dict[str, str]] = []
    seen: set[str] = set()

    for line in text.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|\s*#\s*\|", line) or re.match(r"^\|\s*-+", line):
            continue

        m = ROW_RE_FULL.match(line) or ROW_RE.match(line)
        if m:
            name, handle, url = m.group(1).strip(), m.group(2).strip(), m.group(3).strip()
        else:
            continue

        key = handle.lower()
        if key in seen:
            continue
        seen.add(key)
        # Prefer handle from URL if present
        url_handle = url.rstrip("/").split("/")[-1]
        if url_handle and url_handle.lower() == handle.lower():
            handle = url_handle
        builders.append(
            {"name": name, "handle": handle, "profile_url": url}
        )

    if not builders:
        # Last-resort: scan whole file for @handles with x.com links nearby
        for m in re.finditer(
            r"\|\s*\d+\s*\|\s*([^|]+?)\s*\|\s*`@([A-Za-z0-9_]+)`",
            text,
        ):
            name, handle = m.group(1).strip(), m.group(2).strip()
            key = handle.lower()
            if key in seen:
                continue
            seen.add(key)
            builders.append(
                {
                    "name": name,
                    "handle": handle,
                    "profile_url": f"https://x.com/{handle}",
                }
            )

    return builders


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "builders.md")
    if not path.is_file():
        print(f"error: file not found: {path}", file=sys.stderr)
        return 1
    data = parse(path.read_text(encoding="utf-8"))
    if not data:
        print("error: no builders parsed", file=sys.stderr)
        return 2
    json.dump(data, sys.stdout, ensure_ascii=False, indent=2)
    sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
