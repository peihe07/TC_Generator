"""B4 —— `axis` 映射提案之分析層複核素材（R-P262(a)）。

36 §九：`axis` 264 條提案僅 16 條經實讀驗證。
37 §G179：31 條已改者，其判準所依之描述欄**與內文出自同一次撰寫** ——
若當初即誤解區分軸，二者會一致地錯。

故其餘映射不逕改。本檔備料供分析層複核 ——
**不作判定、不作摘要，逐字呈現 token 差**。

抽樣：`input_data` / `trigger_state` / `mode` 三大群各 ≥ 16.7%，種子 38（＝包號）。

用法：
    python features/power/scripts/build_axis_review_38.py
"""

from __future__ import annotations

import collections
import glob
import json
import random
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SEED = 38

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_axis import propose_axis, diff_text, load, FIELDS  # noqa: E402

GROUPS = ("input_data", "trigger_state", "mode")


def main() -> None:
    tcs = load()
    by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_leaf[re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)].append(t)

    pools: dict[str, list[tuple[dict, str]]] = collections.defaultdict(list)
    unmapped = []
    for t in tcs:
        leaf = re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)
        ax, ev = propose_axis(t, by_leaf[leaf])
        if ax is None:
            unmapped.append((t["tc_id"], leaf))
        elif ax in GROUPS:
            pools[ax].append((t, ev))

    rng = random.Random(SEED)
    out = ["# B4 —— `axis` 映射提案之複核素材（R-P262(a)）\n",
           "\n> **本檔不作判定、不作摘要，逐字呈現。**\n",
           f"> 三大群各抽 ≥ 16.7%，種子 `random.Random({SEED})`。\n",
           "\n| 群 | 母體 | 抽樣 | 率 |\n|---|---|---|---|\n"]
    samples: dict[str, list] = {}
    for g in GROUPS:
        pool = sorted(pools[g], key=lambda x: x[0]["tc_id"])
        k = max(1, -(-len(pool) * 167 // 1000))
        samples[g] = sorted(rng.sample(pool, k), key=lambda x: x[0]["tc_id"])
        out.append(f"| `{g}` | {len(pool)} | **{k}** | {k / len(pool) * 100:.1f}% |\n")

    for g in GROUPS:
        out.append(f"\n---\n\n## 群 `{g}`（{len(samples[g])} 條）\n\n"
                   "複核之問題：**該 TC 與其對照姊妹之區分軸，是否確為本群之軸？**\n")
        for i, (t, ev) in enumerate(samples[g], 1):
            leaf = re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)
            ref_id = re.search(r"對照 `([^`]+)`", ev)
            ref = next((p for p in by_leaf[leaf]
                        if ref_id and p["tc_id"].endswith(ref_id.group(1))), None)
            out.append(f"\n### {i} / {len(samples[g])} —— `{t['tc_id']}`（`{leaf}`）\n\n"
                       f"**`tc_title`**：{t['tc_title']}\n\n"
                       f"**執行層之依據**：{ev}\n\n")
            if ref is not None:
                out.append(f"**對照條 `{ref['tc_id']}`**：{ref['tc_title']}\n\n"
                           f"**四欄 token 差（逐字）**：\n```\n"
                           f"{diff_text(t, ref)}\n```\n\n")
                for f in FIELDS:
                    if str(t.get(f, "")) != str(ref.get(f, "")):
                        out.append(f"**`{f}`**\n\n本條：\n```\n{t.get(f, '')}\n```\n\n"
                                   f"對照：\n```\n{ref.get(f, '')}\n```\n\n")
            else:
                out.append("**無對照條**（本檔取自 `propose_axis` 之依據字串）\n\n")

    out.append(f"\n---\n\n## 「無對應」{len(unmapped)} 條之三個選項與其後果（R-P262(b)）\n\n"
               "> 其 leaf 僅產出 1 條 TC，無他條可區分；§4.6 之六值皆預設「與他條之區分」。\n"
               "> **本檔只呈選項與後果，不裁。**\n\n"
               "| 選項 | 後果 |\n|---|---|\n"
               "| 新增列舉值（如 `single`） | 須改 §4.6，**屬 canon 層**，影響全部 feature；"
               "其利為語義正確、不需犧牲既有契約 |\n"
               "| 以 `none` 表之 | **與 §4.6 之 `none` ⇔ `duplicate_of` 雙向契約衝突**（G174 之 C4 / C7）"
               "—— 該 40 條並非重複，設 `duplicate_of` 即為不實；不設則 C4 觸發 40 次 |\n"
               "| 留空 | 違反 G168 之 C2（`axis` 非空字串），全批 40 條觸發；"
               "且「留空」與「未填」無從分辨 |\n"
               "\n**逐條**\n\n| tc | leaf |\n|---|---|\n")
    for tid, leaf in unmapped:
        out.append(f"| `…-{tid[-3:]}` | `{leaf}` |\n")

    p = DATA / "axis_review_38.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)} — {p.stat().st_size} bytes")
    for g in GROUPS:
        print(f"  {g}: 母體 {len(pools[g])}、抽 {len(samples[g])} "
              f"= {len(samples[g]) / len(pools[g]) * 100:.1f}%  "
              f"{[t['tc_id'][-3:] for t, _ in samples[g]]}")
    print(f"  無對應 {len(unmapped)} 條")


if __name__ == "__main__":
    main()
