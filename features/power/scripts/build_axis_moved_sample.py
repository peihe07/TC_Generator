"""B5 —— 自 `input_data` 移出者之抽樣素材（R-P285）。

R-P285：重判後，凡其值**由 `input_data` 移出者**抽 **≥ 20%** 由分析層複核。

**⚠ 抽樣按群交錯排列**（41 §K 第 2 項）——
分析層依序讀取時若素材按群集中，讀前 N 條即全落於單一群；
本檔以**輪轉**方式交錯（`trigger_state` → `timing` → `mode` → `無對應` → …），
使依序讀取即自然跨群。

**本檔不作判定、不作摘要，逐字呈現。**

用法：
    python features/power/scripts/build_axis_moved_sample.py
"""

from __future__ import annotations

import collections
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SEED = 42

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

    moved: dict[str, list[tuple[dict, str, str]]] = collections.defaultdict(list)
    for t in sorted(tcs, key=lambda x: x["tc_id"]):
        d = t.get("distinguishing_axis")
        if d is None or d["axis"] != "input_data":
            continue
        prop, ev = propose(t, by_leaf[BASE.match(t["req_id"]).group(1)])
        if prop != "input_data":
            moved[prop].append((t, prop, ev))

    total = sum(len(v) for v in moved.values())
    rng = random.Random(SEED)
    # 各群按比例抽 ≥ 20%，至少 1 條
    picked: dict[str, list] = {}
    for g, v in moved.items():
        k = max(1, -(-len(v) * 20 // 100))
        picked[g] = sorted(rng.sample(v, min(k, len(v))), key=lambda x: x[0]["tc_id"])
    n = sum(len(v) for v in picked.values())

    # **輪轉交錯**（41 §K 第 2 項）
    order, pools = [], {g: list(v) for g, v in picked.items()}
    while any(pools.values()):
        for g in sorted(pools):
            if pools[g]:
                order.append(pools[g].pop(0))

    out = ["# B5 —— 自 `input_data` 移出者之抽樣素材（R-P285）\n",
           "\n> **本檔不作判定、不作摘要，逐字呈現。**\n",
           f"> 母體：自 `input_data` 移出者 **{total}** 條；"
           f"抽 **{n}** 條 = **{n / total * 100:.1f}%**（≥ 20%），"
           f"種子 `random.Random({SEED})`。\n",
           "> **⚠ 按群輪轉交錯排列**（41 §K 第 2 項）—— "
           "依序讀取即自然跨群，不致集中於單一群。\n",
           "\n| 移出至 | 母體 | 抽樣 | 率 |\n|---|---|---|---|\n"]
    for g in sorted(moved):
        out.append(f"| `{g}` | {len(moved[g])} | **{len(picked[g])}** | "
                   f"{len(picked[g]) / len(moved[g]) * 100:.0f}% |\n")
    out.append(f"\n**閱讀序（交錯）**："
               f"{'、'.join('`…-' + t['tc_id'][-3:] + '`(' + p + ')' for t, p, _ in order)}\n")
    out.append("\n**複核之問題**：該 TC 與其對照姊妹之區分，"
               "是否確為新值所指之語義框架（"
               "`input_data`＝餵入之資料值／`trigger_state`＝系統或車輛狀態／"
               "`mode`＝硬體或 bench 配置／`timing`＝事件時點）？\n\n---\n")

    for i, (t, prop, ev) in enumerate(order, 1):
        leaf = BASE.match(t["req_id"]).group(1)
        others = [p for p in by_leaf[leaf] if p["tc_id"] != t["tc_id"]]
        ref = min(others, key=lambda p: len(" ".join(diff_lines(t, p))))
        out.append(f"\n## {i} / {n} —— `{t['tc_id']}`（`{leaf}`）　"
                   f"`input_data` → **`{prop}`**\n\n"
                   f"**`tc_title`**：{t['tc_title']}\n\n"
                   f"**執行層之依據**：{ev}\n\n"
                   f"**對照條 `{ref['tc_id']}`**：{ref['tc_title']}\n\n"
                   f"**相異行（已排除觀察步驟）**：\n{fence(chr(10).join(diff_lines(t, ref)))}\n\n")
        for f in FIELDS:
            if str(t.get(f, "")) != str(ref.get(f, "")):
                out.append(f"**`{f}`**\n\n本條：\n{fence(t.get(f, ''))}\n\n"
                           f"對照：\n{fence(ref.get(f, ''))}\n\n")

    p = DATA / "axis_moved_sample_42.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)} — {p.stat().st_size} bytes")
    print(f"母體 {total}，抽 {n} = {n / total * 100:.1f}%，種子 {SEED}")
    for g in sorted(moved):
        print(f"  {g}: {len(moved[g])} → 抽 {len(picked[g])}")
    print(f"交錯序：{[t['tc_id'][-3:] for t, _, _ in order]}")


if __name__ == "__main__":
    main()
