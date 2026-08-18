"""B1 —— 第 4 列與第 8 列之分析層複核素材（R-P252）。

35 包之第 4 列 79 條與第 8 列 7 條皆為**執行層自判**，
依 R-P214 未經第二方複核。本檔備妥原始素材供分析層複核 ——
**不作判定、不作摘要，逐字呈現**（摘要會把複核者的判斷替換成執行層的）。

抽樣：第 4 列 79 條取 ≥ 16.7%，種子載明；第 8 列 7 條**全取**。

用法：
    python features/power/scripts/build_review_material_36.py
"""

from __future__ import annotations

import glob
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SEED = 36                      # 種子＝包號，載明於本檔與上繳包

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_design_method import propose  # noqa: E402
from confirm_row4 import cond_clauses, substantive_lines  # noqa: E402

# 35 包之人工判定：`…-099` 判不成立，已續判至第 9 列
REJECTED = {"099"}


def fence(text: str) -> str:
    return "```\n" + str(text).rstrip() + "\n```"


def main() -> None:
    tcs, clause_of = [], {}
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for l in d.get("leaves", []):
            clause_of[l["parent"]] = str(l.get("source_clause", ""))
        tcs += d["tcs"]

    row4 = [t for t in tcs
            if propose(t)[0] == 4 and t["tc_id"][-3:] not in REJECTED]
    row8 = [t for t in tcs if propose(t)[0] == 8]

    rng = random.Random(SEED)
    n = max(1, -(-len(row4) * 167 // 1000))          # ceil(79 * 16.7%) = 14
    sample = sorted(rng.sample(row4, n), key=lambda t: t["tc_id"])

    def block(t: dict, idx: int, total: int, label: str) -> str:
        base = re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)
        clause = clause_of.get(base, "")
        conds = cond_clauses(clause)
        subs = substantive_lines(t["pre_conditions"])
        return (
            f"\n### {label} {idx} / {total} —— `{t['tc_id']}`（`{base}`）\n\n"
            f"**`tc_title`**：{t['tc_title']}\n\n"
            f"**`source_clause` 逐字**（全文，未截斷）：\n{fence(clause)}\n\n"
            f"**clause 之條件子句**（`COND_RE` 所命中者，{len(conds)} 處）：\n"
            + ("".join(f"- `{c}`\n" for c in conds) or "- （無）\n")
            + f"\n**`pre_conditions` 逐字**：\n{fence(t['pre_conditions'])}\n\n"
            f"**實質前提**（扣除 bench 環境列，{len(subs)} 項）：\n"
            + "".join(f"- {s}\n" for s in subs)
            + f"\n**`input_test_data` 逐字**：\n{fence(t.get('input_test_data', ''))}\n\n"
            f"**`test_procedure` 逐字**：\n{fence(t['test_procedure'])}\n\n"
            f"**`expected_result` 逐字**：\n{fence(t['expected_result'])}\n\n"
            f"**執行層所判之「二個以上條件」**：{'；'.join(subs) or '（見上）'}\n\n"
            f"**現值 `design_method`**：{t['design_method']}\n")

    out = ["# B1 —— 第 4 / 8 列之分析層複核素材（R-P252）\n",
           "\n> **本檔不作判定、不作摘要，逐字呈現。**\n",
           f"> 第 4 列母體 **{len(row4)}** 條（79 條 = 80 − `…-099`）；"
           f"抽樣 **{n}** 條 = **{n / len(row4) * 100:.1f}%**，"
           f"種子 `random.Random({SEED})`。\n",
           f"> 第 8 列 **{len(row8)}** 條**全取**（其「跨功能」未機械化）。\n",
           f"\n**抽樣清單**：{'、'.join('`…-' + t['tc_id'][-3:] + '`' for t in sample)}\n",
           f"\n---\n\n## 一、第 4 列抽樣（{n} / {len(row4)}）\n\n"
           "複核之問題：**該 TC 之結果是否確由二個以上條件共同決定？**\n"]
    for i, t in enumerate(sample, 1):
        out.append(block(t, i, n, "第 4 列"))

    out.append(f"\n---\n\n## 二、第 8 列全 {len(row8)} 條\n\n"
               "複核之問題：**該 TC 之 ≥ 3 步是否確為「跨功能」？**\n"
               "（現行謂詞只驗步數，「跨功能」未機械化 —— 35 §7.3）\n")
    for i, t in enumerate(sorted(row8, key=lambda x: x["tc_id"]), 1):
        out.append(block(t, i, len(row8), "第 8 列"))

    p = DATA / "review_material_36.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)} — {p.stat().st_size} bytes")
    print(f"第 4 列母體 {len(row4)}，抽 {n} = {n / len(row4) * 100:.1f}%，種子 {SEED}")
    print(f"  {[t['tc_id'][-3:] for t in sample]}")
    print(f"第 8 列全 {len(row8)}：{[t['tc_id'][-3:] for t in row8]}")


if __name__ == "__main__":
    main()
