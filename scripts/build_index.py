#!/usr/bin/env python3
"""Regenerate index.json from the Markdown files in daily/ and monthly/.

Run from anywhere: python3 scripts/build_index.py
Each entry's title is the first "# " heading of the file (falls back to the filename).
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
SECTIONS = ("daily", "monthly")


def title_of(path: pathlib.Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^#\s+(.+)", line)
        if m:
            return m.group(1).strip()
    return path.stem


def main() -> None:
    index = {}
    for section in SECTIONS:
        folder = ROOT / section
        entries = []
        for f in sorted(folder.glob("*.md"), reverse=True):
            entries.append({"id": f.stem, "title": title_of(f), "path": f"{section}/{f.name}"})
        index[section] = entries
    (ROOT / "index.json").write_text(json.dumps(index, indent=2) + "\n", encoding="utf-8")
    print({k: len(v) for k, v in index.items()})


if __name__ == "__main__":
    main()
