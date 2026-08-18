"""G188 —— 以 `source_clause` 逐字相同為條件之反向全批掃（R-P269）。

38 §九第 4 項：(b-2) 之形態（**錨點不同而內容相同**）全批未掃；
該次僅由 G178 之 13 組中辨出 2 組。
**若另有 clause 相同而 TC 不同者，現行無任何機制查之。**

G178 由 **TC 側**出發（四欄逐字全同）；本檔由 **規格側**出發（clause 逐字相同），
二者為互補之方向：

  G178  TC 相同 → 問其 leaf 是否應相同
  G188  clause 相同 → 問其 TC 是否應相同

**clause 相同而 TC 不同者為新形態** —— 同一規格文字產出不同之驗證，
或為刻意（不同錨點側重不同面向），或為不一致。

正規化：**僅空白與 NBSP**（比照 R-P125(a)，不得擴大）。

用法：
    python features/power/scripts/scan_clause_duplicates.py
"""

from __future__ import annotations

import collections
import glob
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

BODY = ("pre_conditions", "input_test_data", "test_procedure", "expected_result")


def norm(text: str) -> str:
    """R-P125(a)：僅空白與 NBSP。"""
    return " ".join(str(text).replace("\xa0", " ").replace(" ", " ").split())


def main() -> None:
    leaves: dict[str, dict] = {}
    tcs_by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for l in d.get("leaves", []):
            leaves[l["parent"]] = l
        for t in d["tcs"]:
            import re
            tcs_by_leaf[re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)].append(t)

    by_clause: dict[str, list[str]] = collections.defaultdict(list)
    for parent, l in leaves.items():
        by_clause[norm(l.get("source_clause", ""))].append(parent)

    groups = [(c, sorted(ps)) for c, ps in by_clause.items() if len(ps) > 1]
    groups.sort(key=lambda x: x[1])

    rows = []
    for clause, parents in groups:
        anchors = {leaves[p].get("source_anchor", "") for p in parents}
        sigs = {p: {tuple(norm(t.get(f, "")) for f in BODY)
                    for t in tcs_by_leaf[p]} for p in parents}
        all_sigs = [sigs[p] for p in parents]
        # TC 集合是否相同
        tc_same = all(s == all_sigs[0] for s in all_sigs)
        # 部分相同者：交集非空而不全等
        inter = set.intersection(*all_sigs) if all_sigs else set()
        rows.append({
            "parents": parents, "n_anchor": len(anchors),
            "anchor_same": len(anchors) == 1,
            "counts": [len(tcs_by_leaf[p]) for p in parents],
            "tc_same": tc_same,
            "n_common": len(inter),
            "clause": clause,
        })

    same = [r for r in rows if r["tc_same"]]
    diff = [r for r in rows if not r["tc_same"]]
    new_form = [r for r in diff]

    out = ["# G188 —— `source_clause` 逐字相同之反向全批掃（R-P269）\n",
           "\n> **本檔只掃與呈，不改值**（R-P269(d)）。\n",
           "> 正規化僅空白與 NBSP（比照 R-P125(a)）。\n",
           "> **與 G178 互補**：G178 由 TC 側出發（TC 相同 → 問 leaf）；"
           "本檔由規格側出發（clause 相同 → 問 TC）。\n",
           f"\n## 一、彙總\n\n| 項 | 數 |\n|---|---|\n"
           f"| `source_clause` 逐字相同之 leaf 群 | **{len(groups)}** |\n"
           f"| 　其 TC 集合**亦相同** | **{len(same)}** |\n"
           f"| 　其 TC 集合**不同 —— 新形態** | **{len(diff)}** |\n"
           f"| 　　其中**錨點亦相同**者 | {sum(1 for r in diff if r['anchor_same'])} |\n"
           f"| 　　其中**錨點相異**者 | {sum(1 for r in diff if not r['anchor_same'])} |\n",
           "\n## 二、逐群\n\n"
           "| leaf 群 | 錨點 | TC 數 | TC 集合 | 共同 TC 數 |\n|---|---|---|---|---|\n"]
    for r in rows:
        out.append(f"| {'、'.join('`' + p + '`' for p in r['parents'])} | "
                   f"{'**相同**' if r['anchor_same'] else '相異'} | "
                   f"{'／'.join(str(c) for c in r['counts'])} | "
                   f"{'相同' if r['tc_same'] else '**不同**'} | {r['n_common']} |\n")

    if new_form:
        out.append(f"\n## 三、新形態逐群 —— clause 相同而 TC 不同（**{len(new_form)}** 群）\n\n"
                   "> 意義：**同一規格文字產出不同之驗證** ——\n"
                   "> 或為刻意（不同錨點側重不同面向），或為不一致。**裁定於 40 包。**\n")
        for r in new_form:
            out.append(f"\n### {'、'.join('`' + p + '`' for p in r['parents'])}\n\n"
                       f"- 錨點：{'**相同**' if r['anchor_same'] else '相異'}"
                       f"（{r['n_anchor']} 組）\n"
                       f"- TC 數：{'／'.join(str(c) for c in r['counts'])}；"
                       f"**共同 TC {r['n_common']} 條**\n")
            for p in r["parents"]:
                ids = sorted(t["tc_id"][-3:] for t in tcs_by_leaf[p])
                out.append(f"- `{p}` 之 TC：{'、'.join('`…-' + i + '`' for i in ids)}\n")
            out.append(f"- `source_clause`（前 200 字元）：\n```\n{r['clause'][:200]}\n```\n")

    p = DATA / "g188_clause_duplicates.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"clause 逐字相同之 leaf 群：{len(groups)}")
    print(f"  TC 集合亦相同：{len(same)}")
    print(f"  **TC 集合不同（新形態）：{len(diff)}**")
    for r in diff:
        print(f"     {r['parents']}  錨點{'相同' if r['anchor_same'] else '相異'}  "
              f"TC 數 {r['counts']}  共同 {r['n_common']}")


if __name__ == "__main__":
    main()
