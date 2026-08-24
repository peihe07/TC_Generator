"""W-163（86 包 §1／§5）—— R-VS6 之三分判準，落檔並附兩側錨點。

**86 包 §1 之裁定**：R-VS6 之「逐字」，其比較基準為**來源文件所顯示之字元**，
非其儲存格式之編碼。

  PASS  上半段為條文之子字串；**或**僅差 XML 實體之還原
        （`&lt;` → `<`、`&amp;` → `&`、`&gt;` → `>`）、
        不斷行空白（`\\xa0` → 空白）、連續空白之壓縮
  FAIL  字詞之替換（`HU` → `HMI`、`When` → `If`、`Softkey button` → `softkey`）、
        **標點之替換（彎引號 → 直引號）**、取自條文之他句、或漏其前言

**彎引號屬 FAIL** —— 其為來源之顯示字元，非編碼。故正規化**不得**觸及引號。

**錨點（R-VS54，兩側皆須有標的）**
  必命中（須報 FAIL）：17 條之**修正前版**（`batch0{1,2,3,7}_v*`／`batch10_v5` 等）
  必不命中（須報 PASS）：27 條之實體解碼類（現行版）
"""
from __future__ import annotations

import html
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from writeback_036 import latest_batches      # noqa: E402
from defect_scan_w157 import clause_of        # noqa: E402

# 修正前之版本 —— FAIL 側錨點之標的（各為 `rvs6_restore_w160.py` 之輸入）
PRE_FIX = ["batch01_v8.json", "batch02_v6.json", "batch03_v5.json",
           "batch07_v6.json", "batch10_v5.json"]


def displayed(x: str) -> str:
    """來源文件**所顯示之字元** —— 實體還原 ＋ 空白正規化。

    **不觸及引號** —— 彎引號 `“”` 為顯示字元，其替換屬改寫（86 包 §1）。
    """
    return re.sub(r"\s+", " ", html.unescape(x).replace("\xa0", " ")).strip()


def verdict(t: dict) -> str:
    """PASS／FAIL —— 86 包 §1 之三分（WARN 已收為 PASS）。"""
    cl = clause_of(t["leaf_id"])
    upper = (t.get("test_item", "") or "").split("\n\n(")[0].strip()
    if not (cl and upper):
        return "PASS"
    if upper in cl or displayed(upper) in displayed(cl):
        return "PASS"
    return "FAIL"


def scan(files) -> tuple[int, int, list]:
    p = f = 0
    fails = []
    for path in files:
        for t in json.loads(Path(path).read_text(encoding="utf-8"))["tcs"]:
            if verdict(t) == "PASS":
                p += 1
            else:
                f += 1
                fails.append((t["leaf_id"], Path(path).name))
    return p, f, fails


def main() -> int:
    print("R-VS6 三分（86 包 §1）—— 逐字以所顯示之字元為準")

    ok = True
    # ── 必不命中側：現行全母體須全數 PASS ────────────────────────────
    p, f, fails = scan(latest_batches())
    print(f"  現行全母體      PASS {p}／FAIL {f}")
    for leaf, b in fails[:8]:
        print(f"        ⚠ {leaf} [{b}]")
    if f != 0:
        ok = False

    # ── 必命中側：修正前之版本須報出 FAIL ───────────────────────────
    pre = [FEAT / "generated" / n for n in PRE_FIX if (FEAT / "generated" / n).exists()]
    p2, f2, fails2 = scan(pre)
    print(f"  修正前之版本    PASS {p2}／**FAIL {f2}**   "
          f"（{len(pre)} 檔：{', '.join(x.name for x in pre)}）")
    for leaf, b in fails2[:20]:
        print(f"        · {leaf} [{b}]")
    if f2 == 0:
        ok = False

    # ── 27 條解碼類須落在 PASS 側（其於嚴格子字串比較下不相符）────────
    strict = 0
    for path in latest_batches():
        for t in json.loads(path.read_text(encoding="utf-8"))["tcs"]:
            cl = clause_of(t["leaf_id"])
            up = (t.get("test_item", "") or "").split("\n\n(")[0].strip()
            if cl and up and up not in cl and verdict(t) == "PASS":
                strict += 1
    print(f"  其中「僅解碼差異而判 PASS」者  **{strict}** 條"
          f"（86 包 §1 所收之 WARN）")
    if strict == 0:
        ok = False

    print("  錨點：", "**兩側皆有標的，PASS**" if ok else "**FAIL —— 有一側無標的**")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
