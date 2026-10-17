#!/usr/bin/env python3
"""Fail when a public source tree contains private paths, data or missing notices."""
from __future__ import annotations
from pathlib import Path
import hashlib
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKIP = {".git", ".pytest_cache", "__pycache__", "build", "dist", "release_checks"}
REQUIRED = ["README.md", "LICENSE", "CITATION.cff", "AUTHORS.md", "SECURITY.md",
            "CONTRIBUTING.md", "CHANGELOG.md", "environment.yml", "pyproject.toml"]
FORBIDDEN_SUFFIXES = {".mtz", ".pdb", ".cif", ".mmcif", ".npz"}
PRIVATE_PATTERNS = [r"/Volumes/", r"/Users/", r"[A-Za-z]:\\Users\\"]
EXPECTED_CLIPPER = "01276ebda309ece40a972560eec5a4f83b97ee37757675454ebe36083053e570"

errors = []
for name in REQUIRED:
    if not (ROOT / name).is_file():
        errors.append(f"missing required file: {name}")

files = []
for path in ROOT.rglob("*"):
    if any(part in SKIP or part.endswith(".egg-info") for part in path.parts):
        continue
    if path.is_file():
        files.append(path)
        rel = path.relative_to(ROOT)
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"private/scientific data file is not permitted: {rel}")
        if path.stat().st_size > 10 * 1024 * 1024:
            errors.append(f"unexpected file larger than 10 MiB: {rel}")
        if path != Path(__file__).resolve() and (path.suffix.lower() in {".py", ".md", ".toml", ".yml", ".yaml", ".json", ".txt", ".in"} or path.name in {"LICENSE"}):
            text = path.read_text(encoding="utf-8", errors="replace")
            for pattern in PRIVATE_PATTERNS:
                if re.search(pattern, text):
                    errors.append(f"local absolute path found in: {rel}")

archive = ROOT / "src/oasis_py/resources/clipper-2.1.20201109.tar.gz"
if not archive.is_file():
    errors.append("missing corresponding Clipper source archive")
elif hashlib.sha256(archive.read_bytes()).hexdigest() != EXPECTED_CLIPPER:
    errors.append("Clipper source archive checksum mismatch")

pyproject = (ROOT / "pyproject.toml").read_text(encoding="utf-8") if (ROOT / "pyproject.toml").is_file() else ""
for expected in ['name = "OASIS4.3-GUI"', 'version = "0.1"', 'license = "LGPL-2.1-or-later"']:
    if expected not in pyproject:
        errors.append(f"package metadata missing: {expected}")

if errors:
    print("Release audit failed:", file=sys.stderr)
    for error in sorted(set(errors)):
        print("-", error, file=sys.stderr)
    raise SystemExit(1)
print(f"Release audit passed: {len(files)} files; no target diffraction/structure files found")
