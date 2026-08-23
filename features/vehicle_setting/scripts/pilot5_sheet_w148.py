"""W-148（78 包 §5）—— pilot #5 之抽樣準備。

  **必檢 7**：拆分產出之 7 條（`split_flag = true`，**首次出現之形態**）
  **分層 8**：batch20 之 12 條 × `impl_gap`（有／無）之交叉格取樣

每條含十六欄全文 ＋ `split_reason` ＋ 來源條文逐字節錄；**列抽樣之交叉格矩陣**。
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]
COLS = ["tc_title", "test_item", "pre_conditions", "input_test_data", "test_procedure",
        "expected_result", "specification_reference", "design_method", "priority",
        "split_flag", "split_reason", "dr_dependent", "impl_gap", "screen_pending",
        "dr15_exposed", "remarks"]


def latest():
    g: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            g[m.group(1)].append((int(m.group(2) or 1), f))
    return [(k, max(v)[1]) for k, v in sorted(g.items())]


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}

    splits, b20 = [], []
    for name, f in latest():
        for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]:
            if tc.get("split_flag"):
                splits.append((name, tc))
            if name == "batch20":
                b20.append((name, tc))

    cells = collections.defaultdict(list)
    for name, tc in b20:
        cells["有" if str(tc.get("impl_gap", "")).strip() else "無"].append((name, tc))
    strat = []
    for k in sorted(cells):
        for x in cells[k]:
            if len(strat) < 8 and x not in strat:
                strat.append(x)
    # 不足 8 時自最大格補足
    big = max(cells.values(), key=len) if cells else []
    for x in big:
        if len(strat) >= 8:
            break
        if x not in strat:
            strat.append(x)

    items = [(n, t, "必檢（拆分產出，首次出現之形態）") for n, t in splits] + \
            [(n, t, f"分層（batch20 × `impl_gap` "
                    f"{'有' if str(t.get('impl_gap','')).strip() else '無'}）")
             for n, t in strat[:8]]

    out = ["# pilot #5 review sheet", "",
           "執行層產出（W-148，51 輪）。依 78 包 §5 之抽樣。", "",
           "## 1. 抽樣之交叉格矩陣", "",
           "| 母體 | 條數 | 說明 |", "|---|---:|---|",
           f"| 拆分產出（`split_flag = true`） | {len(splits)} | **必檢，不抽樣** —— "
           "本 feature 首次出現之形態 |",
           f"| `batch20` | {len(b20)} | 分層母體 |", "",
           "| `batch20` ＼ `impl_gap` | 有 | 無 |", "|---|---:|---:|",
           f"| 條數 | {len(cells.get('有', []))} | {len(cells.get('無', []))} |", "",
           f"**必檢 {len(splits)} ＋ 分層 {len(strat[:8])} ＝ {len(items)} 條。**",
           "", "> `impl_gap` 之「無」格為 0 —— batch20 之 12 條全數帶 `impl_gap`",
           "> （其命令訊號 `*_Cmd_Tlm` 皆不在基線 DBC）。",
           "> **該維度於本母體為單值**，分層 8 條全自「有」格取（同 A-VS142 之形態）。",
           "", "---", ""]

    for i, (batch, tc, why) in enumerate(items, 1):
        leaf = tc["leaf_id"]
        row = l2r.get(leaf, {})
        out += [f"## {i}. `{leaf}`", "",
                "| 項 | 值 |", "|---|---|",
                f"| 來源批次 | `{batch}` |", f"| 納入理由 | {why} |",
                f"| `split_flag` | {tc.get('split_flag')} |",
                f"| `split_reason` | {tc.get('split_reason') or '（無）'} |",
                f"| `impl_gap` | {tc.get('impl_gap') or '（無）'} |",
                f"| `dr_dependent` | {tc.get('dr_dependent') or '（無）'} |", "",
                "**來源條文逐字**", ""]
        for rid in (row.get("reqid_list") or "").split(";"):
            blk = blocks.get(rid.strip().replace("CFTS044-", ""))
            if blk:
                body = "\n".join(blk["text"].split("\n")[1:]).strip()
                out += [f"`{rid.strip()}`：", "", "> " + body.replace("\n", "\n> "), ""]
        out += ["**十六欄全文**", ""]
        for c in COLS:
            v = tc.get(c, "")
            if isinstance(v, str) and "\n" in v:
                out += [f"**{c}**", "", "```", v, "```", ""]
            else:
                out.append(f"**{c}**：{v}")
        out += ["", "### 覆核欄（分析層填）", "", "| 項 | 建議分類 | 理由 |", "|---|---|---|",
                "| 內容正確性 | | |", "| 拆分之軸是否成立 | | |",
                "| `impl_gap` 之標記 | | |", "", "---", ""]

    (FEAT / "docs/reports/pilot5_sheet.md").write_text("\n".join(out), encoding="utf-8")
    print(f"pilot5_sheet.md：必檢 {len(splits)} ＋ 分層 {len(strat[:8])} = {len(items)} 條")
    print(f"交叉格：impl_gap 有 {len(cells.get('有', []))}／無 {len(cells.get('無', []))}")
    for b, t, w in items:
        print(f"  {b:10s} {t['leaf_id']:44s} {w[:22]}")


if __name__ == "__main__":
    main()
