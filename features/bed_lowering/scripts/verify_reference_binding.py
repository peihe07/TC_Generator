#!/usr/bin/env python3
"""Recompute every `reference:` sha256 from the file on disk and compare.

R-G23: a declaration that is never compared fails the same way as no
declaration at all -- the difference is only that it reads as if protected.
On mismatch this exits 1 and prints BOTH values in full; it never rewrites
feature.yaml, because adopting the measured value would silently accept an
unruled revision of the database.
"""
import hashlib
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
CFG = Path(__file__).resolve().parents[1] / "feature.yaml"


def main() -> int:
    cfg = yaml.safe_load(CFG.read_text(encoding="utf-8"))
    ref = cfg.get("reference") or {}
    if not ref:
        print("feature.yaml has no `reference:` section")
        return 1
    bad = 0
    print(f"{'key':<18} {'verdict':<10} file")
    for key in sorted(ref):
        entry = ref[key]
        f = ROOT / entry["file"]
        declared = entry["sha256"]
        if not f.exists():
            print(f"{key:<18} {'MISSING':<10} {entry['file']}")
            bad += 1
            continue
        actual = hashlib.sha256(f.read_bytes()).hexdigest()
        ok = actual == declared
        bad += not ok
        print(f"{key:<18} {'OK' if ok else '**MISMATCH**':<10} {entry['file']}")
        if not ok:
            print(f"{'':<18} declared {declared}")
            print(f"{'':<18} measured {actual}")
    print(f"\n{len(ref)} bound, {bad} failing")
    if bad:
        print("R-G23: stop and report. feature.yaml NOT rewritten.")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
