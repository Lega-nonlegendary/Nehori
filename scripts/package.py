#!/usr/bin/env python3
"""Validate the public file set and create an upload archive (Python 3.10+)."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
from urllib.parse import unquote, urlsplit
import zipfile

FILES = (
    "README.md", "README.ja.md", "README.zh-CN.md", "LICENSE",
    "CHANGELOG.md", ".gitignore", "PUBLISHING.md", "scripts/package.py",
    "skills/nehori/SKILL.md",
    "skills/nehori/references/exploration.md",
    "skills/nehori/references/dialogue-patterns.md",
    "skills/nehori/references/conversation-map.md",
    "skills/nehori/references/research-notes.md",
)
IGNORED_DIRS = {".git", "__pycache__"}
LINK = re.compile(r"!?\[[^\]\n]*\]\(([^)\n]+)\)")
PRIVATE_PATTERNS = (
    ("absolute Windows path", re.compile(r"(?<!\w)[A-Za-z]:[\\/]")),
    ("absolute user-home path", re.compile(r"/(?:Users|home)/[^/\s]+")),
    ("private runtime URI", re.compile(r"\b(?:memory|agent|history|proc)://")),
    ("session identifier", re.compile(r"\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b", re.I)),
    ("possible API token", re.compile(r"\b(?:sk-|gh[pousr]_|github_pat_)[A-Za-z0-9_-]{20,}\b")),
)


class PackageError(Exception):
    pass


def is_link(path):
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, "st_file_attributes", 0) & 0x400)


def validate(root):
    """Return one validated byte snapshot; archives use these same bytes."""
    root = Path(root).resolve()
    expected = set(FILES)
    allowed_dirs = {str(parent.as_posix()) for name in FILES for parent in Path(name).parents}
    seen = set()
    for base, dirs, names in os.walk(root, followlinks=False):
        base = Path(base)
        for name in list(dirs):
            child = base / name
            if is_link(child):
                raise PackageError("Link/reparse-point directory is not distributable")
            if name in IGNORED_DIRS:
                dirs.remove(name)
            elif child.relative_to(root).as_posix() not in allowed_dirs:
                raise PackageError("Unexpected directory: " + child.relative_to(root).as_posix())
        for name in names:
            child = base / name
            rel = child.relative_to(root).as_posix()
            if is_link(child):
                raise PackageError("Link/reparse-point file is not distributable")
            if rel not in expected:
                raise PackageError("Unexpected file: " + rel)
            seen.add(rel)
    missing = expected - seen
    if missing:
        raise PackageError("Missing public files: " + ", ".join(sorted(missing)))

    snapshot = {}
    for rel in FILES:
        raw = (root / rel).read_bytes()
        try:
            text = raw.decode("utf-8")
        except UnicodeDecodeError:
            raise PackageError("File is not UTF-8: " + rel) from None
        for label, pattern in PRIVATE_PATTERNS:
            if pattern.search(text):
                raise PackageError("Possible private content (" + label + ") in " + rel)
        if rel.endswith(".md"):
            for match in LINK.finditer(text):
                link = match.group(1).strip().strip("<>")
                parsed = urlsplit(link)
                if parsed.scheme in {"http", "https", "mailto"}:
                    continue
                if not parsed.path and parsed.fragment:
                    continue
                if parsed.scheme or parsed.netloc or parsed.path.startswith("/") or "\\" in parsed.path:
                    raise PackageError("Non-portable link in " + rel)
                target = (root / rel).parent / unquote(parsed.path)
                target = target.resolve()
                try:
                    target_rel = target.relative_to(root).as_posix()
                except ValueError:
                    raise PackageError("Link escapes the public repository in " + rel) from None
                if target_rel not in expected:
                    raise PackageError("Missing or non-public link target in " + rel + ": " + parsed.path)
        snapshot[rel] = raw
    return snapshot


def package(root, output):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output == root or root in output.parents:
        raise PackageError("The archive must be outside the public repository")
    if output.exists():
        raise PackageError("Refusing to overwrite an existing archive")
    snapshot = validate(root)
    output.parent.mkdir(parents=True, exist_ok=True)
    created = False
    try:
        with output.open("xb") as stream:
            created = True
            with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
                for rel, data in snapshot.items():
                    info = zipfile.ZipInfo("nehori/" + rel)
                    info.compress_type = zipfile.ZIP_DEFLATED
                    info.external_attr = 0o100644 << 16
                    archive.writestr(info, data)
    except Exception:
        if created:
            output.unlink(missing_ok=True)
        raise
    return {
        "archive": output.name,
        "files": len(snapshot),
        "archive_sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
        "members": {"nehori/" + rel: hashlib.sha256(data).hexdigest() for rel, data in snapshot.items()},
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True, type=Path, help="New ZIP path outside this repository")
    args = parser.parse_args()
    try:
        manifest = package(Path(__file__).resolve().parents[1], args.output)
    except (PackageError, OSError) as error:
        print("Package rejected: " + str(error), file=sys.stderr)
        return 1
    print(json.dumps(manifest, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
