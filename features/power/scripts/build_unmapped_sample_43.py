"""B2 —— 「無對應」28 條之相異行逐字 ＋ 抽樣素材（R-P290）。

R-P290：**不設區辨機制**（任何區辨機制皆須先知何者為對，為循環），
改以**提供判斷素材** —— 逐條列出其**相異行逐字**，
使讀者得自行判斷該相異行是否應歸某值。分析層抽樣 ≥ 20% 複核。

母體為 36 條「無對應」扣除 R-P288 之 8 條（僅施加相同而觀察／ER 相異者）= **28 條**。

**本檔不作判定、不作摘要。**

用法：
    python features/power/scripts/build_unmapped_sample_43.py
"""

from __future__ import annotations

import collections
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SEED = 43

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_axis_positive import propose, diff_lines, BASE, FIELDS  # noqa: E402
from rejudge_axis import load  # noqa: E402


def fence(t: str) -> str:
    return "```\n" + str(t).rstrip() + "\n```"


def main() -> None:
    tcs = load()
    by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_leaf[BASE.match(t["req_id"]).group(1)].append(t)

    unmapped, er_only = [], []
    for t in sorted(tcs, key=lambda x: x["tc_id"]):
        if not t.get("distinguishing_axis"):
            continue
        p, ev = propose(t, by_leaf[BASE.match(t["req_id"]).group(1)])
        if p != "**無對應**":
            continue
        others = [x for x in by_leaf[BASE.match(t["req_id"]).group(1)]
                  if x["tc_id"] != t["tc_id"]]
        ref = min(others, key=lambda x: len(" ".join(diff_lines(t, x))))
        (er_only if not diff_lines(t, ref) else unmapped).append((t, ref))

    rng = random.Random(SEED)
    k = max(1, -(-len(unmapped) * 20 // 100))
    picked = sorted(rng.sample(unmapped, k), key=lambda x: x[0]["tc_id"])

    out = ["# B2 —— 「無對應」之相異行逐字與抽樣（R-P290）\n",
           "\n> **本檔不作判定、不作摘要，逐字呈現。**\n",
           f"> 母體：「無對應」**{len(unmapped) + len(er_only)}** 條，"
           f"扣除 R-P288 之 **{len(er_only)}** 條（施加相同而觀察／ER 相異）"
           f"= **{len(unmapped)}** 條。\n",
           f"> 抽樣 **{k}** 條 = **{k / len(unmapped) * 100:.1f}%**（≥ 20%），"
           f"種子 `random.Random({SEED})`。\n",
           "> **複核之問題**：該相異行是否應歸五值之某一"
           "（`boundary` / `timing` / `trigger_state` / `mode` / `input_data`）？\n",
           f"\n**抽樣清單**：{'、'.join('`…-' + t['tc_id'][-3:] + '`' for t, _ in picked)}\n",
           f"\n## 一、全 {len(unmapped)} 條之相異行逐字\n\n"
           "| tc | leaf | 對照 | 相異行 |\n|---|---|---|---|\n"]
    for t, ref in unmapped:
        dl = diff_lines(t, ref)
        out.append(f"| `…-{t['tc_id'][-3:]}` | `{BASE.match(t['req_id']).group(1)}` | "
                   f"`…-{ref['tc_id'][-3:]}` | "
                   f"{'<br>'.join(x[:76] for x in dl)} |\n")

    out.append(f"\n---\n\n## 二、抽樣 {k} 條之全欄逐字\n")
    for i, (t, ref) in enumerate(picked, 1):
        out.append(f"\n### {i} / {k} —— `{t['tc_id']}`"
                   f"（`{BASE.match(t['req_id']).group(1)}`）\n\n"
                   f"**`tc_title`**：{t['tc_title']}\n\n"
                   f"**對照條 `{ref['tc_id']}`**：{ref['tc_title']}\n\n"
                   f"**相異行**：\n{fence(chr(10).join(diff_lines(t, ref)))}\n\n")
        for f in FIELDS:
            if str(t.get(f, "")) != str(ref.get(f, "")):
                out.append(f"**`{f}`**\n\n本條：\n{fence(t.get(f, ''))}\n\n"
                           f"對照：\n{fence(ref.get(f, ''))}\n\n")

    p = DATA / "unmapped_sample_43.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)} — {p.stat().st_size} bytes")
    print(f"無對應 {len(unmapped) + len(er_only)} 條 = 相異行有內容 {len(unmapped)} "
          f"＋ R-P288 之 {len(er_only)}")
    print(f"抽 {k} 條 = {k / len(unmapped) * 100:.1f}%："
          f"{[t['tc_id'][-3:] for t, _ in picked]}")


if __name__ == "__main__":
    main()
