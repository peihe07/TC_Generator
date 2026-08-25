#!/usr/bin/env python3
"""Transcribe a handoff's rulings and emit the check table (R-G20).

The table is printed as markdown so the upstream package can paste machine
output instead of retyping figures. Upstream 08 §1 had three hashes filled
in from memory; the comparison itself was always machine-run, but the
report was not — this script closes that gap.

Fence extraction uses `^```(\\w*)\\n` because handoff 07 introduced
info-string fences (```yaml); the plain `^```\\n` form mis-pairs them.
"""
import argparse
import hashlib
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FEAT = Path(__file__).resolve().parents[1]
HANDOFF = FEAT / "docs" / "handoff"
LEDGER = ROOT / "docs" / "fw036" / "RULINGS_LEDGER.md"
RULINGS = FEAT / "RULINGS.md"


def fences(path):
    return [b for _, b in re.findall(r"^```(\w*)\n(.*?)^```\n",
                                     path.read_text(encoding="utf-8"),
                                     re.S | re.M)]


def sha16(s):
    return hashlib.sha256(s.encode()).hexdigest()[:16]


def display_source_blocks():
    """Every R-DM block in handoff order — the order RULINGS.md holds."""
    out = fences(HANDOFF / "01_intake_recon.md")
    out += fences(HANDOFF / "02_source_correction.md")[1:]
    out += [b for b in fences(HANDOFF / "03_coverage_redo.md")
            if re.match(r"R-DM\d+（", b.strip())]
    for name in sorted(p.name for p in HANDOFF.glob("*.md"))[3:]:
        out += [b for b in fences(HANDOFF / name) if b.startswith("R-DM")]
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("handoff", help="e.g. 09_recon_crosscheck.md")
    ap.add_argument("--start", type=int, required=True,
                    help="running number of this package's first R-DM entry")
    args = ap.parse_args()

    blocks = fences(HANDOFF / args.handoff)
    dm = [b for b in blocks if b.startswith("R-DM")]
    g = [b for b in blocks if b.startswith("R-G")]

    print(f"## 抄錄核對表 — {args.handoff}（機器輸出，R-G20）\n")
    print("| # | 條號 | 去處 | 字元數 | SHA256（前 16 碼） | 逐字相符 |")
    print("|---|---|---|---|---|---|")
    got_dm = display_source_blocks()
    in_file = fences(RULINGS)
    for i, b in enumerate(dm, args.start):
        tag = b.strip().splitlines()[0].split("（")[0]
        ok = b in in_file
        print(f"| {i} | {tag} | `features/display/RULINGS.md` | {len(b)} "
              f"| `{sha16(b)}` | {'是' if ok else '**否**'} |")
    led = re.findall(r"^```text\n(.*?)^```\n", LEDGER.read_text(encoding="utf-8"),
                     re.S | re.M)
    for b in g:
        tag = b.strip().splitlines()[0].split("（")[0]
        ok = b in led
        print(f"| — | {tag} | `docs/fw036/RULINGS_LEDGER.md` | {len(b)} "
              f"| `{sha16(b)}` | {'是' if ok else '**否**'} |")

    same = got_dm == in_file
    print(f"\n累計：`RULINGS.md` 之 R-DM 區塊 **{len(in_file)}** 個，"
          f"與各下放包原檔逐字元比對 **{'全數相符' if same else '有不符'}**"
          f"（{len(got_dm)} vs {len(in_file)}）。")
    if not same:
        for i, (a, b) in enumerate(zip(got_dm, in_file)):
            if a != b:
                print(f"  第 {i} 個不符：{a.splitlines()[0][:40]}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
