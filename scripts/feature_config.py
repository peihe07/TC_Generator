#!/usr/bin/env python3
"""Shared feature.yaml loader for the FW036 pipeline scripts.

Column letters are converted to 0-based indices here; path globs resolve to
exactly one file — an ambiguous or missing input fails loud rather than
silently picking the first match.

`HomeHMI/scripts/feature_config.py` is the same loader, kept in place so the
Home pipeline's imports are untouched. New feature scripts import this one.
"""
from pathlib import Path

import yaml


def col_letter_to_idx(letter: str) -> int:
    """Excel column letter -> 0-based index."""
    n = 0
    for ch in letter.strip().upper():
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def idx_to_col_letter(idx: int) -> str:
    """0-based index -> Excel column letter."""
    s, n = "", idx + 1
    while n:
        n, r = divmod(n - 1, 26)
        s = chr(65 + r) + s
    return s


def load_feature_config(feature_dir: str | Path = ".") -> dict:
    """Read <feature_dir>/feature.yaml and add derived lookups."""
    root = Path(feature_dir)
    cfg = yaml.safe_load((root / "feature.yaml").read_text(encoding="utf-8"))
    cfg["root"] = root
    cfg["col"] = {k: col_letter_to_idx(v)
                  for k, v in cfg["workbook"]["columns"].items()}
    return cfg


def resolve_path(cfg: dict, key: str, override: str | None = None) -> Path:
    """CLI override wins; otherwise glob feature.yaml's `paths.<key>`."""
    if override:
        return Path(override)
    pattern = cfg["paths"].get(key)
    if not pattern:
        raise SystemExit(f"paths.{key} is null or absent in feature.yaml")
    hits = sorted(cfg["root"].glob(pattern))
    if len(hits) != 1:
        raise SystemExit(f"paths.{key} = {pattern!r} matched {len(hits)} files"
                         + (f": {[h.name for h in hits]}" if hits else ""))
    return hits[0]
