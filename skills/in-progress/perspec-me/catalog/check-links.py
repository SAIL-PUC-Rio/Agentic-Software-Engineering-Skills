#!/usr/bin/env python3
"""Stdlib-only relative-link checker for the PerSpecML catalog.

Walks every Markdown file under this directory, extracts Markdown-style
relative links (``[text](target)``), and verifies each target resolves to a
real file or directory on disk. Absolute URLs (``http://``, ``https://``,
``mailto:``) are skipped, since only *relative* links are in scope. A
``#page=N`` (or any ``#...``) fragment is stripped before resolving the
target, so PDF page anchors like ``report.pdf#page=6`` are checked against
``report.pdf``.

Usage:
    python3 check-links.py

Run from anywhere; the catalog root is this script's own directory. Exits
with status 0 and prints "0 broken links" when every relative link resolves,
or exits with status 1 and lists each broken link otherwise.
"""

import pathlib
import re
import sys

CATALOG_ROOT = pathlib.Path(__file__).resolve().parent

# Matches Markdown links: [text](target)
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)]+)\)")


def is_external(target: str) -> bool:
    return bool(re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target))


def check_file(md_file: pathlib.Path):
    broken = []
    text = md_file.read_text(encoding="utf-8")
    for match in LINK_RE.finditer(text):
        target = match.group(1).strip()

        if not target or is_external(target):
            continue

        # Strip a fragment, e.g. "#page=6" or "#some-heading".
        path_part = target.split("#", 1)[0]
        if not path_part:
            # A pure in-page anchor (e.g. "#page=6" with no path) has
            # nothing to resolve on disk.
            continue

        resolved = (md_file.parent / path_part).resolve()
        if not resolved.exists():
            broken.append((md_file, target))
    return broken


def main():
    all_broken = []
    md_files = sorted(CATALOG_ROOT.rglob("*.md"))
    for md_file in md_files:
        all_broken.extend(check_file(md_file))

    if all_broken:
        print(f"{len(all_broken)} broken link(s) found:\n")
        for md_file, target in all_broken:
            rel = md_file.relative_to(CATALOG_ROOT)
            print(f"  {rel}: {target}")
        sys.exit(1)

    print(f"Checked {len(md_files)} Markdown files: 0 broken links.")
    sys.exit(0)


if __name__ == "__main__":
    main()
