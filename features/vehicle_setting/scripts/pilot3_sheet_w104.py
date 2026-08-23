"""W-104（60 包 §5／§6）—— pilot #3 之 review sheet。

母體：`batch13_v2` 之 **10 條全數**（新形態，不抽樣）
    ＋ W-101 之 Priority 變動 24 條中取 **3**
      （P0 之 6 條取 2 —— P0(a)／P0(b) 各一；由 P2 升 P1 者取 1）
合計 **13 條**。

每條含十欄全文 ＋ `dr_dependent`／`priority` 及其所依類別 ＋ 來源條文逐字節錄。
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

EXTRA = [
    ("generated/batch01_v6.json", "SWE1-VC-ThirdRowHeadrestDump-025",
     "P0(a) 之唯一一條 —— 實體致動；驗 R-VS56 之 P0(a) 是否可覆核"),
    ("generated/batch05_v4.json", "SWE1-VC-TwoStagesHeatedSeat-057",
     "P0(b) 之代表 —— 加熱座椅之按壓啟用；驗「啟用」與「階數切換」之界線"),
    ("generated/batch02_v4.json", "SWE1-VC-ThirdRowHeadrestDump-030",
     "由 P2 升 P1 者 —— 軟鍵之可選性；驗 R-VS56 之 P1 涵蓋範圍"),
]
COLS = ["tc_title", "test_item", "pre_conditions", "input_test_data", "test_procedure",
        "expected_result", "specification_reference", "design_method", "priority",
        "split_flag"]


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}

    items = []
    for tc in json.loads((FEAT / "generated/batch13_v2.json").read_text(encoding="utf-8"))["tcs"]:
        items.append((tc, "batch13_v2", "新形態全數納入 —— 標的訊號不在基線 DBC"))
    for f, leaf, why in EXTRA:
        for tc in json.loads((FEAT / f).read_text(encoding="utf-8"))["tcs"]:
            if tc["leaf_id"] == leaf:
                items.append((tc, Path(f).stem, why))

    out = ["# pilot #3 review sheet —— 13 條",
           "",
           "執行層產出（W-104，37 輪）。依 60 包 §5 之抽樣裁定。",
           "",
           "| 母體 | 條數 | 理由 |",
           "|---|---:|---|",
           "| `batch13_v2` 全數 | 10 | 首批「標的訊號不在基線 DBC」之 TC，形態與前 76 條皆不同，"
           "pilot #1／#2 之結論不涵蓋 |",
           "| W-101 之 Priority 變動 | 3 | P0(a) 1／P0(b) 1／由 P2 升 P1 1 —— 驗 R-VS56 之判定可覆核性 |",
           "",
           "**分析層先讀並附建議分類，Pei 覆核分類（60 包 §5）。**",
           "", "---", ""]

    for i, (tc, src, why) in enumerate(items, 1):
        leaf = tc["leaf_id"]
        row = l2r.get(leaf, {})
        out += [f"## {i}. `{leaf}`", "",
                f"| 項 | 值 |", "|---|---|",
                f"| 來源批次 | `{src}` |",
                f"| 納入理由 | {why} |",
                f"| `priority` | **{tc['priority']}** |",
                f"| Priority 所依類別（R-VS56） | {tc.get('reasoning', '（未記）')} |",
                f"| `dr_dependent` | {tc.get('dr_dependent') or '（無）'} |",
                f"| `design_method` | {tc['design_method']} |",
                f"| 章節 | {row.get('section', '')} |", ""]
        out.append("### 來源條文逐字")
        out.append("")
        for rid in (row.get("reqid_list") or "").split(";"):
            blk = blocks.get(rid.strip().replace("CFTS044-", ""))
            if not blk:
                continue
            body = "\n".join(blk["text"].split("\n")[1:]).strip()
            out += [f"`{rid.strip()}`（`EE Architecture: "
                    f"{blk['attrs'].get('EE Architecture', '?')}`）：", "",
                    "> " + body.replace("\n", "\n> "), ""]
        out.append("### 十欄全文")
        out.append("")
        for c in COLS:
            v = tc[c]
            if isinstance(v, str) and "\n" in v:
                out += [f"**{c}**", "", "```", v, "```", ""]
            else:
                out.append(f"**{c}**：{v}")
        out += ["", "### 覆核欄（分析層填）", "",
                "| 項 | 建議分類 | 理由 |", "|---|---|---|",
                "| 內容正確性 | | |", "| Priority 判定 | | |",
                "| `dr_dependent` 標記 | | |", "", "---", ""]

    (FEAT / "docs/reports/pilot3_sheet.md").write_text("\n".join(out), encoding="utf-8")
    print(f"pilot3_sheet.md：{len(items)} 條")
    for tc, src, _ in items:
        print(f"  {tc['priority']} {src:14s} {tc['leaf_id']}")


if __name__ == "__main__":
    main()
