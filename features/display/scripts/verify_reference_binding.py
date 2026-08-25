#!/usr/bin/env python3
"""Verify feature.yaml's `reference:` bindings against the files (R-G23).

R-G15 made the binding visible. Visible is not checked: a declared sha256
that nothing ever compares fails exactly like no binding at all, except it
reads as though the material were protected. R-DM19's carry — the 26 rows of
signal resolution, the two LOOKUP_MISSES entries, and every signal field in
every TC after this — all rest on these four files being the ones that were
measured.

On mismatch this exits non-zero and prints BOTH values. It never rewrites
the declared value: doing that would silently adopt a database revision
nobody ruled on (R-G23).
"""
import hashlib
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[3]
FEATURE_YAML = Path(__file__).resolve().parents[1] / "feature.yaml"


def sha256_of(path):
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    cfg = yaml.safe_load(FEATURE_YAML.read_text(encoding="utf-8"))
    ref = cfg.get("reference") or {}
    if not ref:
        print(f"{FEATURE_YAML}: no `reference:` section — nothing to verify")
        return 0

    print("# reference binding check (R-G23)")
    print(f"feature.yaml: {FEATURE_YAML}")
    print(f"entries: {len(ref)}\n")
    print("| key | file | declared | actual | verdict |")
    print("|---|---|---|---|---|")

    bad = []
    for key in sorted(ref):
        entry = ref[key] or {}
        rel = entry.get("file", "")
        declared = str(entry.get("sha256", "")).strip().lower()
        path = ROOT / rel
        if not rel:
            verdict, actual = "**NO FILE DECLARED**", "—"
            bad.append((key, "no file declared"))
        elif not path.is_file():
            verdict, actual = "**MISSING**", "—"
            bad.append((key, f"file not found: {path}"))
        elif not declared:
            verdict, actual = "**NO SHA DECLARED**", sha256_of(path)[:16] + "…"
            bad.append((key, "no sha256 declared"))
        else:
            actual_full = sha256_of(path)
            actual = actual_full[:16] + "…"
            if actual_full == declared:
                verdict = "MATCH"
            else:
                verdict = "**MISMATCH**"
                bad.append((key, f"declared {declared} / actual {actual_full}"))
        print(f"| {key} | `{Path(rel).name if rel else '—'}` "
              f"| `{(declared[:16] + '…') if declared else '—'}` "
              f"| `{actual}` | {verdict} |")

    print()
    if bad:
        print(f"**{len(bad)} of {len(ref)} FAILED.** Full values:")
        for key, why in bad:
            print(f"  {key}: {why}")
        print("\nR-G23: stop and report. Do NOT update the declared value in "
              "feature.yaml — that would adopt an unruled revision of the "
              "reference database.")
        return 1
    print(f"**{len(ref)} of {len(ref)} match.**")
    return 0


if __name__ == "__main__":
    sys.exit(main())
