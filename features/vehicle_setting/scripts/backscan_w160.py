"""W-160（84 包 §5，R-VS77 之首次全母體回掃）。

**R-VS77**：凡新立或修訂之條文，其影響及於已產出之 TC 者，
須對**全母體**回掃 —— 「已通過 pilot」不豁免。

本檔對現行 225 條，逐一以**現行全部條文**重判。
§9 已涵蓋者（§5.5／R-VS39／R-VS52／R-VS56／L-VS2 等）不重複，
本檔只掃 **§9 未涵蓋而 84 包 §5 點名者**：

  R-VS6      `test_item` 上半段須逐字（**全母體**，非僅 `split_flag`）
  §4.5       欄位歸屬（pre_condition 與 procedure 不得重複設定同一配置）
  R-VS59(4)  最弱斷言（ER 為 PENDING 而該步驟之觀察可觀察者）
  R-VS61     值無對應者取逐字、不附 raw
  R-VS67′    欄組之能承載 → `impl_gap` 之標記
  R-VS69     `screen_pending` 之判準 ＝ AH 載有畫面層之 BLOCKED 註記
  R-VS71     值未解不阻塞（不得整條 PENDING 而其前置步驟本可寫）
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(FEAT / "scripts"))

from writeback_036 import latest_batches                      # noqa: E402
from defect_scan_w157 import steps_of, clause_of, d2, d3, d4  # noqa: E402
from rvs6_verdict_w163 import verdict as rvs6_verdict         # noqa: E402

WR = {r["leaf_id"]: r for r in csv.DictReader(
    (FEAT / "docs/reports/writability.tsv").open(encoding="utf-8"), delimiter="\t")}


def r_vs6(t: dict) -> str | None:
    """`test_item` 上半段須為條文逐字 —— **全母體**（R-VS77 之範圍）。

    **判準已定案（86 包 §1，57 輪 W-163）**：逐字之比較基準為
    **來源文件所顯示之字元**，非其儲存格式之編碼。三分中之 WARN
    （僅實體解碼／空白差異）**已收為 PASS**，其實作見
    `rvs6_verdict_w163.py`（該檔另附兩側錨點）。
    """
    return None if rvs6_verdict(t) == "PASS" else \
        "FAIL: test_item 上半段非條文逐字（字詞／標點之替換、或取自他句）"


def r_vs61(t: dict) -> str | None:
    """值於 LID 與 DBC 皆無來源者，須取條文逐字、**不附 raw**。"""
    body = f"{t.get('test_procedure', '')}\n{t.get('expected_result', '')}"
    for m in re.finditer(r"\b([A-Z][A-Z0-9_]{2,}\.\w{3,})\s*=\s*(\d+)\s*\(", body):
        sig = m.group(1)
        if sig.startswith("RADIO_B3."):        # 其 LID `fmt` 為空、DBC 亦無
            return f"{sig} 附 raw `{m.group(2)}` 而其值域無來源（R-VS61）"
    return None


def r_vs67p(t: dict) -> str | None:
    """取了非 `Atlantis High` 欄組者，須標 `impl_gap`（R-VS67′(2)／R-VS66(a)）。"""
    body = f"{t.get('test_procedure', '')}\n{t.get('expected_result', '')}"
    # **修正（本輪首跑所得）**：`impl_gap` 為 **TC 之欄位**（`impl_gap_w133.py` 所寫），
    # 非 `writability.tsv` 之欄 —— 初版讀後者，其恆為空致 28 項全為偽陽性。
    gap = str(t.get("impl_gap") or "").strip()
    if re.search(r"\bTELEMATIC_VEHICLE_SETUP\.\w+_Cmd_Tlm\b", body) and not gap:
        return "取 `Atlantis` 欄組之 `*_Cmd_Tlm` 而 writability 未標 `impl_gap`"
    return None


def r_vs69(t: dict) -> str | None:
    """`screen_pending` ＝ AH 載有畫面層之 BLOCKED 註記，與 ER 是否 PENDING 無關。"""
    ah = str(t.get("remarks", "") or "")
    # **收窄（本輪首跑所得）**：`DR-19`（`$EngRun_Stat$` 四值）與 `DR-22`
    # （訊號值域）為**訊號層**之待覆，非畫面層。R-VS69 之判準逐字為
    # 「AH 欄載有**畫面層**之 BLOCKED 註記」—— 只有 `DR-5-B`（HMI requirements）屬之。
    screen_block = bool(re.search(r"BLOCKED:\s*DR-5-B\b", ah))
    flag = str(t.get("screen_pending")) == "yes"
    if screen_block != flag:
        return (f"screen_pending = {t.get('screen_pending')} 而 AH "
                f"{'有' if screen_block else '無'}畫面層之 BLOCKED 註記（R-VS69）")
    return None


def r_vs71(t: dict) -> str | None:
    """值未解不阻塞 —— 不得整條 ER 皆 PENDING（其前置步驟本可寫）。"""
    er = steps_of(t.get("expected_result", ""))
    if er and all(e.startswith("PENDING") for e in er):
        return "全部 ER 皆 PENDING —— 前置步驟未照寫（R-VS71）"
    return None


RULES = [("R-VS6", r_vs6), ("§4.5", d2), ("R-VS59(4)-a", d3),
         ("R-VS59(4)-b", d4), ("R-VS61", r_vs61), ("R-VS67′", r_vs67p),
         ("R-VS69", r_vs69), ("R-VS71", r_vs71)]


def main() -> int:
    tcs = []
    for f in latest_batches():
        for t in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            tcs.append({**t, "_b": f.name})
    print(f"R-VS77 全母體回掃 —— {len(tcs)} 條 × {len(RULES)} 條文")
    total = 0
    for name, fn in RULES:
        hits = [(t["leaf_id"], t["_b"], fn(t)) for t in tcs if fn(t)]
        warn = [h for h in hits if h[2].startswith("WARN")]
        hits = [h for h in hits if not h[2].startswith("WARN")]
        total += len(hits)
        print(f"  {name:14s} {len(hits):3d}"
              + (f"   （另 WARN {len(warn)}）" if warn else ""))
        for leaf, b, why in hits[:6]:
            print(f"        {leaf}  [{b}]  {why}")
        if len(hits) > 6:
            print(f"        … 另 {len(hits) - 6} 條")
    print(f"  ── 不符總數 **{total}**")
    return 0 if total == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
