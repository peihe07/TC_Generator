#!/usr/bin/env python3
"""並行防護 —— 分析層台帳之狀態檢查（下放包 03 作業 A、R-ICS17）。

功能限四項，不做他事；**不自動修復、不寫任何檔**。

1. 讀 `ANALYSIS_LOCK.md`，印 `holder`／`acquired`／`released`；
   `released` 非 null 而 `holder` 非 null 者報 INCONSISTENT。
2. grep `RULINGS.md` 之 `^## R-ICS`，印全部錨點與行號；同名錨點出現 ≥2 次
   且非 `vN` 形式者報 DUPLICATE（`R-ICS2 v1`／`v2` 為合法並存）。
3. 對 `ANOMALIES.md`／`DATA_REQUESTS.md` 之 `A-ICS{n}`／`DR-ICS{n}` 作同樣
   重號檢查，並印各自最大號。
4. 印五類 scope 檔之 sha256 與 mtime。

exit code：有 DUPLICATE 或 INCONSISTENT → 1，否則 0。

掃描條件（逐項揭露）：
  - 錨點：`RULINGS.md` 中 `^## (R-ICS\\d+)(?: (v\\d+))?\\s*$`，1-based 行號
  - A-／DR- 之登記列：`^\\| (A-ICS\\d+)`／`^\\| (DR-ICS\\d+)`（登記表之首格），
    **不掃內文引用** —— 內文提及同一編號屬正常，非重號
  - scope 檔清單自 `ANALYSIS_LOCK.md` 之 `scope:` 區塊讀出，glob 展開
"""
from __future__ import annotations

import glob
import hashlib
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parents[1]
LOCK = ROOT / "ANALYSIS_LOCK.md"

ANCHOR_RE = re.compile(r"^## (R-ICS\d+)(?: (v\d+))?\s*$")
problems: list[str] = []


def read_lock() -> dict[str, str]:
    txt = LOCK.read_text() if LOCK.exists() else ""
    out: dict[str, str] = {}
    for key in ("holder", "holder_session", "acquired", "released"):
        m = re.search(rf"^\s*{key}:\s*(\S+)", txt, re.M)
        if m:
            out[key] = m.group(1).split("#")[0].strip()
    scope = []
    # `scope:` 行可帶行尾註解，故不以行尾錨定
    m = re.search(r"^scope:[^\n]*((?:\n\s+- [^\n]+)+)", txt, re.M)
    if m:
        scope = [ln.strip()[2:].strip() for ln in m.group(1).strip("\n").split("\n")]
    out["_scope"] = scope
    return out


def check_lock() -> None:
    print("== 1. ANALYSIS_LOCK ==")
    if not LOCK.exists():
        print("  ANALYSIS_LOCK.md 不存在")
        problems.append("INCONSISTENT: ANALYSIS_LOCK.md 不存在")
        return
    lk = read_lock()
    for k in ("holder", "holder_session", "acquired", "released"):
        print(f"  {k:16} {lk.get(k, '(未載)')}")
    holder = lk.get("holder", "null")
    released = lk.get("released", "null")
    if released != "null" and holder != "null":
        problems.append(f"INCONSISTENT: released={released} 而 holder={holder}")
        print(f"  **INCONSISTENT** —— released 非 null 而 holder 非 null")
    else:
        print("  一致性：OK")


def check_anchors() -> None:
    print("\n== 2. RULINGS.md 錨點 ==")
    lines = (ROOT / "RULINGS.md").read_text().split("\n")
    seen: dict[str, list[tuple[int, str | None]]] = {}
    for i, ln in enumerate(lines, 1):
        m = ANCHOR_RE.match(ln)
        if m:
            seen.setdefault(m.group(1), []).append((i, m.group(2)))
    total = sum(len(v) for v in seen.values())
    for rid in sorted(seen, key=lambda s: int(s.split("R-ICS")[1])):
        for line, ver in seen[rid]:
            print(f"  {rid}{' ' + ver if ver else '':10} 行 {line}")
    print(f"  錨點總數 **{total}**（相異 ruling_id {len(seen)}）")
    for rid, occ in seen.items():
        if len(occ) >= 2:
            vers = [v for _, v in occ]
            if any(v is None for v in vers) and len(occ) > 1 and vers.count(None) > 1:
                problems.append(f"DUPLICATE: {rid} 出現 {len(occ)} 次且非 vN 形式")
                print(f"  **DUPLICATE** {rid} × {len(occ)}")
            elif all(v is None for v in vers):
                problems.append(f"DUPLICATE: {rid} 出現 {len(occ)} 次且非 vN 形式")
                print(f"  **DUPLICATE** {rid} × {len(occ)}")
            else:
                print(f"  並存（合法）：{rid} {[v or 'v1(隱)' for _, v in occ]}")


def check_series(fname: str, prefix: str) -> None:
    print(f"\n== 3. {fname} 之 {prefix}{{n}} ==")
    p = ROOT / fname
    if not p.exists():
        print("  檔不存在")
        problems.append(f"INCONSISTENT: {fname} 不存在")
        return
    ids = re.findall(rf"^\| ({prefix}\d+)", p.read_text(), re.M)
    counts: dict[str, int] = {}
    for i in ids:
        counts[i] = counts.get(i, 0) + 1
    nums = sorted(int(i.split("ICS")[1]) for i in counts)
    print(f"  登記列 {len(ids)} 列，相異 {len(counts)}，最大號 **{prefix}{max(nums) if nums else 0}**")
    gaps = [n for n in range(1, (max(nums) if nums else 0) + 1) if n not in nums]
    print(f"  號段缺口：{gaps or '無'}")
    for i, c in counts.items():
        if c >= 2:
            problems.append(f"DUPLICATE: {i} 於 {fname} 登記 {c} 次")
            print(f"  **DUPLICATE** {i} × {c}")


def check_scope_files() -> None:
    print("\n== 4. scope 檔之 sha256 / mtime ==")
    lk = read_lock()
    for pat in lk.get("_scope", []):
        for f in sorted(glob.glob(str(REPO / pat))):
            fp = Path(f)
            h = hashlib.sha256(fp.read_bytes()).hexdigest()[:16]
            mt = datetime.fromtimestamp(fp.stat().st_mtime).strftime("%Y-%m-%d %H:%M:%S")
            print(f"  {h}  {mt}  {fp.relative_to(REPO)}")


def main() -> int:
    check_lock()
    check_anchors()
    check_series("ANOMALIES.md", "A-ICS")
    check_series("DATA_REQUESTS.md", "DR-ICS")
    check_scope_files()
    print("\n總判：" + ("**FAIL** —— " + "；".join(problems) if problems else "OK（無 DUPLICATE／INCONSISTENT）"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
