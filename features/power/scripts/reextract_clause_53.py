"""G240 —— 8 個重建 leaf 之 `source_clause` 獨立重抽（R-P339(b)）。

51 包自陳：`verify_source_clause.py`（G94）之比對對象為 `anchor_bodies()`
之串接，**而重建 `source_clause` 用的是同一函式、同一串接式** ——
對該 8 個 leaf，G94 於原理上不可能 FAIL（「自洽而不完整」第六例）。

**本檔為獨立實作**（比照 G103 對 layer3 之作法）：
自 CFTS 本文之文字層 TSV **自行重建**錨點 → 內文之對映，
**不 import `lint_tcs`、不呼叫 `anchor_bodies()`**，
與現行 `source_clause` 逐字比對。

用法：
    python features/power/scripts/reextract_clause_53.py
"""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
POWER = ROOT / "features/power"
TARGET = ["SWE-PM-001", "SWE-PM-002", "SWE-PM-003", "SWE-PM-004",
          "SWE-PM-005", "SWE-PM-006", "SWE-PM-007", "SWE-PM-009"]


# §C 之二條正則於本檔**獨立宣告**，不自 `lint_tcs` 或 `extract_textlayer` import
SEC_RE = re.compile(r"^\s*(\d+(?:\.\d+)*)\s+(.{0,90}?)\s*\{(\d+)\}\s*$")
REQ_RE = re.compile(r"\*\*(\d{6,8}):\s*\[Artifact Type:")


def independent_bodies() -> dict[str, list[str]]:
    """自 `data/textlayer/*_plain.txt` ＋ `*_bold.txt`（逐行對齊）獨立重建
    item id → 內文段落序列。

    **不 import `lint_tcs`、不呼叫 `anchor_bodies()`、不讀其任何中間產物。**
    分段與錨點判定之邏輯於本檔自行實作，正則亦獨立宣告。

    ⚠ **獨立性之界線須明載**：本檔之輸入（`*_plain.txt` / `*_bold.txt`）
    係 `extract_textlayer.py` 自 CFTS 原始檔所產。
    **故段落切分一段為二者共用，非獨立** —— 本檔所獨立者為
    「錨點辨識與內文歸屬」之邏輯。若段落切分本身有誤，本檔驗不出來。
    """
    out: dict[str, list[str]] = {}
    for stem in ("cfts009", "cfts010"):
        plain = (POWER / f"data/textlayer/{stem}_plain.txt").read_text(
            encoding="utf-8").splitlines()
        bold = (POWER / f"data/textlayer/{stem}_bold.txt").read_text(
            encoding="utf-8").splitlines()
        if len(plain) != len(bold):
            raise ValueError(f"{stem}: plain {len(plain)} 行 vs bold {len(bold)} 行，未對齊")
        current = None
        for p_line, b_line in zip(plain, bold):
            if SEC_RE.match(p_line):
                current = None
                continue
            found = REQ_RE.findall(b_line)
            if found:
                current = found[0]
                out.setdefault(current, [])
            elif current and p_line.strip():
                out[current].append(p_line.strip())
    return out


def normalize(t: str) -> str:
    return " ".join(t.replace("\xa0", " ").replace(" ", " ").split())


def main() -> int:
    bodies = independent_bodies()
    if not bodies:
        print("**停** —— 文字層 TSV 之欄位與預期不符，獨立重抽無法進行")
        return 2
    d = json.loads((POWER / "generated/batch_007_power_state_c.json")
                   .read_text(encoding="utf-8"))
    diff = 0
    for leaf in d["leaves"]:
        if leaf["parent"] not in TARGET:
            continue
        ans = [a.strip() for a in leaf["source_anchor"].split(",") if a.strip()]
        rebuilt = "\n".join("\n".join(bodies.get(a, [])) for a in ans)
        ok = normalize(rebuilt) == normalize(leaf["source_clause"])
        diff += not ok
        print(f"  {leaf['parent']:<12} 獨立重抽 {len(rebuilt):>5} vs 現行 "
              f"{len(leaf['source_clause']):>5}  {'相符' if ok else '**不符**'}")
        if not ok:
            a, b = normalize(rebuilt), normalize(leaf["source_clause"])
            i = next((k for k, (x, y) in enumerate(zip(a, b)) if x != y),
                     min(len(a), len(b)))
            print(f"      首處差異 @{i}: 重抽…{a[max(0,i-40):i+40]!r}")
            print(f"                     現行…{b[max(0,i-40):i+40]!r}")
    print(f"\nG240：{len(TARGET) - diff} / {len(TARGET)} 相符")
    return 1 if diff else 0


if __name__ == "__main__":
    raise SystemExit(main())
