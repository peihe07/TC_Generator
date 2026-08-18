"""B1(b) —— 第 4 列新增 61 條之抽樣素材（R-P272(b)）。

39 §三：代理判準擴及 `test_procedure` 與 `input_test_data` 後，
第 4 列由 80 增至 141，新增 61 條。
執行層自陳其判準（「何謂一個條件」）**未經第二方確認**。

R-P272(b)：自新增 61 條抽 **12 條（≥ 19.7%）**，
逐條列出其二條件之**逐字出處**（來自 `pre_conditions` / `test_procedure` /
`input_test_data` 之何處），置於上繳最前。

**本檔不作判定、不作摘要** —— 逐字呈現其出處，供分析層複核。

用法：
    python features/power/scripts/build_row4_sample_40.py
"""

from __future__ import annotations

import glob
import json
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SEED = 40                       # 種子＝包號

sys.path.insert(0, str(Path(__file__).resolve().parent))
from audit_row4_sources import (proc_conditions, data_conditions,  # noqa: E402
                                total_conditions, load)
from rejudge_design_method import propose, substantive_conditions, BENCH_RE, STEP_RE  # noqa: E402


def pre_lines(pre: str) -> list[str]:
    return [" ".join(ln.split()) for ln in pre.split("\n")
            if STEP_RE.match(ln) and not BENCH_RE.search(ln)]


def fence(t: str) -> str:
    return "```\n" + str(t).rstrip() + "\n```"


def main() -> None:
    tcs = load()
    cur = {t["tc_id"] for t in tcs if propose(t)[0] == 4}
    added = []
    for t in tcs:
        row = propose(t)[0]
        if row in (-1, 1, 2, 3):
            continue
        n, _ = total_conditions(t)
        if n >= 2 and t["tc_id"] not in cur:
            added.append((t, row, n))

    rng = random.Random(SEED)
    k = max(1, -(-len(added) * 197 // 1000))       # ceil(61 * 19.7%) = 13
    sample = sorted(rng.sample(added, k), key=lambda x: x[0]["tc_id"])

    out = ["# B1(b) —— 第 4 列新增 61 條之抽樣素材（R-P272(b)）\n",
           "\n> **本檔不作判定、不作摘要，逐字呈現。**\n",
           f"> 母體 **{len(added)}** 條（第 4 列 80 → 141 之新增部分）；"
           f"抽 **{k}** 條 = **{k / len(added) * 100:.1f}%**，"
           f"種子 `random.Random({SEED})`。\n",
           "> 複核之問題：**該 TC 之結果是否確由所列之二個以上條件共同決定？**\n",
           f"\n**抽樣清單**：{'、'.join('`…-' + t['tc_id'][-3:] + '`' for t, _, _ in sample)}\n",
           "\n---\n"]
    for i, (t, row, n) in enumerate(sample, 1):
        pl = pre_lines(t["pre_conditions"])
        pc = proc_conditions(t["test_procedure"])
        dc = data_conditions(t.get("input_test_data", ""))
        out.append(f"\n## {i} / {k} —— `{t['tc_id']}`（`{t['req_id']}`）\n\n"
                   f"**`tc_title`**：{t['tc_title']}\n\n"
                   f"**現落點**：第 {row} 列　**擴充後之總條件數**：{n}\n\n"
                   f"### 條件之逐字出處\n\n"
                   f"| # | 來源欄位 | 逐字 |\n|---|---|---|\n")
        j = 0
        for s in pl:
            j += 1
            out.append(f"| {j} | `pre_conditions` | {s} |\n")
        for s in pc:
            j += 1
            out.append(f"| {j} | `test_procedure` | {s} |\n")
        for s in dc:
            j += 1
            out.append(f"| {j} | `input_test_data` | {s} |\n")
        out.append(f"\n### 四欄逐字\n\n"
                   f"**`pre_conditions`**：\n{fence(t['pre_conditions'])}\n\n"
                   f"**`input_test_data`**：\n{fence(t.get('input_test_data', ''))}\n\n"
                   f"**`test_procedure`**：\n{fence(t['test_procedure'])}\n\n"
                   f"**`expected_result`**：\n{fence(t['expected_result'])}\n")

    p = DATA / "row4_sample_40.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)} — {p.stat().st_size} bytes")
    print(f"母體 {len(added)}，抽 {k} = {k / len(added) * 100:.1f}%，種子 {SEED}")
    print(f"  {[t['tc_id'][-3:] for t, _, _ in sample]}")


if __name__ == "__main__":
    main()
