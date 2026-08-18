"""G151 —— R-P159 分層取樣備料（R-P224）。

R-P159 裁定分析層每批之覆核範圍為
「全部 leaf 之 `source_clause` 與 `reasoning`（全讀）＋ 反向涵蓋報告（全讀）
 ＋ TC 全文（**分層取樣：每 leaf 至少一條 ＋ 全部 P0**）」，
**該分層取樣至今未完整執行**（批次五、六之 TC 本體未讀）。

R-P224：**執行層備料，分析層讀。**

取樣規則（逐字依 R-P224）：
  （a）**全部 P0 之 TC**
  （b）**每 leaf 至少一條** —— P0 已涵蓋者不重複；
       未有 P0 之 leaf 取其 `split_index = 1` 者
  （c）取樣清單與其涵蓋率

**不得節錄欄位**（§I）—— 十六欄逐條全附。

用法：
    python features/power/scripts/build_review_sampling.py
"""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

# 十六欄 —— 依 workbook 之欄位順序，**不節錄**。
FIELDS = ["req_id", "tc_id", "tc_title", "test_group", "test_set", "test_item",
          "pre_conditions", "input_test_data", "test_procedure", "expected_result",
          "specification_reference", "priority", "design_method",
          "functional_safety", "split_reason", "reasoning_note"]

CHUNK = 8   # R-P224：每段不逾 8 條


def main() -> None:
    batches = [json.loads(p.read_text(encoding="utf-8"))
               for p in sorted(GENERATED.glob("*.json"))]
    all_tcs, leaves = [], []
    for b in batches:
        all_tcs += b["tcs"]
        leaves += [l["parent"] for l in b["leaves"]]

    p0 = [t for t in all_tcs if t.get("priority") == "P0"]
    covered = {t["req_id"] for t in p0}
    extra = []
    for leaf in leaves:
        if leaf in covered:
            continue
        cand = [t for t in all_tcs if t["req_id"] == leaf]
        pick = next((t for t in cand if t.get("split_index") == 1), cand[0] if cand else None)
        if pick:
            extra.append(pick)
            covered.add(leaf)

    sample = sorted(p0 + extra, key=lambda t: t["tc_id"])
    out = ["# G151 —— R-P159 分層取樣（R-P224 備料）\n",
           "\n> **執行層備料，分析層讀**（R-P224）。\n",
           "> 取樣規則：**全部 P0** ＋ **每 leaf 至少一條**"
           "（P0 已涵蓋者不重複；未有 P0 者取 `split_index = 1`）。\n",
           "> **十六欄逐條全附，未節錄任何欄位**（§I）。\n",
           f"\n## 涵蓋率\n\n| 項 | 數 |\n|---|---|\n"
           f"| 全部 P0 | **{len(p0)}** |\n"
           f"| 補足每 leaf 至少一條 | **{len(extra)}** |\n"
           f"| **取樣合計** | **{len(sample)}** / 264 = "
           f"**{len(sample)/len(all_tcs)*100:.1f}%** |\n"
           f"| **leaf 涵蓋** | **{len(covered)}** / {len(set(leaves))} = "
           f"**{len(covered)/len(set(leaves))*100:.1f}%** |\n"]

    未涵蓋 = sorted(set(leaves) - covered)
    if 未涵蓋:
        out.append(f"\n**未涵蓋之 leaf（{len(未涵蓋)}）**："
                   f"{'、'.join('`'+x+'`' for x in 未涵蓋)}\n")

    for i in range(0, len(sample), CHUNK):
        seg = sample[i:i + CHUNK]
        out.append(f"\n---\n\n## 段 {i//CHUNK + 1} —— {seg[0]['tc_id'][-3:]} ~ "
                   f"{seg[-1]['tc_id'][-3:]}（{len(seg)} 條）\n")
        for t in seg:
            out.append(f"\n### `{t['tc_id']}`\n\n")
            for f in FIELDS:
                v = str(t.get(f, ""))
                if "\n" in v:
                    out.append(f"- **{f}**：\n\n```\n{v}\n```\n")
                else:
                    out.append(f"- **{f}**：{v or '（空）'}\n")

    (DATA / "sampling_for_review.md").write_text("".join(out), encoding="utf-8")
    print(f"wrote {(DATA / 'sampling_for_review.md').relative_to(ROOT)}")
    print(f"  P0 {len(p0)} ＋ 補足 {len(extra)} = 取樣 {len(sample)} / {len(all_tcs)} "
          f"（{len(sample)/len(all_tcs)*100:.1f}%）")
    print(f"  leaf 涵蓋 {len(covered)} / {len(set(leaves))}"
          f"{'；**未涵蓋 ' + str(len(未涵蓋)) + '**' if 未涵蓋 else '（全涵蓋）'}")
    print(f"  分 {-(-len(sample)//CHUNK)} 段，每段 ≤ {CHUNK} 條")


if __name__ == "__main__":
    main()
