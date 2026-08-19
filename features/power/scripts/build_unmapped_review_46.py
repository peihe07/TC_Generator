"""B1 —— 殘留「無對應」6 條之複核素材（R-P305）。

45 包：「無對應」36 → **6**；執行層自陳 (c) 項**形式完成而實質複核未發生**。
R-P305：該 6 條之複核於本包，**且為寫回之最後前置**；
**在分析層出具複核結果前，不得寫回**。

**本檔逐條列其相異行逐字 ＋ 對照條全欄。不作判定、不作摘要。**

分析層之複核問題：
  該相異行是否應歸五值之某一（`boundary` / `timing` /
  `trigger_state` / `mode` / `input_data`）？
  - 判**確無可歸** → 維持「無對應」，入驗證邊界
  - 判**謂詞不足** → 停，不寫回，另包訂正

用法：
    python features/power/scripts/build_unmapped_review_46.py
"""

from __future__ import annotations

import collections
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
sys.path.insert(0, str(Path(__file__).resolve().parent))

from rejudge_axis_positive import propose, diff_lines, BASE, FIELDS  # noqa: E402
from rejudge_axis import load  # noqa: E402

ALL_FIELDS = ("tc_title", "pre_conditions", "input_test_data",
              "test_procedure", "expected_result")


def fence(t: str) -> str:
    return "```\n" + str(t).rstrip() + "\n```"


def main() -> None:
    tcs = load()
    by_leaf: dict[str, list[dict]] = collections.defaultdict(list)
    for t in tcs:
        by_leaf[BASE.match(t["req_id"]).group(1)].append(t)

    rows = []
    for t in sorted(tcs, key=lambda x: x["tc_id"]):
        if not t.get("distinguishing_axis"):
            continue
        p, _ = propose(t, by_leaf[BASE.match(t["req_id"]).group(1)])
        if p != "**無對應**":
            continue
        others = [x for x in by_leaf[BASE.match(t["req_id"]).group(1)]
                  if x["tc_id"] != t["tc_id"]]
        ref = min(others, key=lambda x: len(" ".join(diff_lines(t, x))))
        rows.append((t, ref))

    out = ["# B1 —— 殘留「無對應」之複核素材（R-P305）\n",
           "\n> **本檔不作判定、不作摘要，逐字呈現。**\n",
           f"> 母體 **{len(rows)}** 條（45 包：36 → 6）。**全數列出，非抽樣。**\n",
           "\n> **複核之問題**：該相異行是否應歸五值之某一"
           "（`boundary` / `timing` / `trigger_state` / `mode` / `input_data`）？\n",
           "> - 判**確無可歸** → 維持「無對應」，入驗證邊界\n",
           "> - 判**謂詞不足** → **停，不寫回**，另包訂正（R-P305(b)）\n",
           "\n> ⚠ 45 包自陳：分析層前次所舉之二例，其**成因診斷有誤**"
           "（判為謂詞不足，實為 `input_test_data` 之內容不當驅動判定），\n",
           "> **而其結論（不應為「無對應」）正確** —— 診斷之誤不使結論失效，"
           "惟其推論不得沿用（R-P305 併記）。\n",
           f"\n**清單**：{'、'.join('`…-' + t['tc_id'][-3:] + '`' for t, _ in rows)}\n",
           "\n---\n"]

    for i, (t, ref) in enumerate(rows, 1):
        leaf = BASE.match(t["req_id"]).group(1)
        out.append(f"\n## {i} / {len(rows)} —— `{t['tc_id']}`（`{leaf}`）\n\n"
                   f"**對照條**：`{ref['tc_id']}`\n\n"
                   f"**相異行逐字**（已排除觀察步驟）：\n"
                   f"{fence(chr(10).join(diff_lines(t, ref)))}\n\n"
                   f"### 本條全欄\n\n")
        for f in ALL_FIELDS:
            out.append(f"**`{f}`**\n{fence(t.get(f, ''))}\n\n")
        out.append("### 對照條全欄\n\n")
        for f in ALL_FIELDS:
            out.append(f"**`{f}`**\n{fence(ref.get(f, ''))}\n\n")

    p = DATA / "unmapped_review_46.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)} — {p.stat().st_size} bytes")
    print(f"殘留「無對應」{len(rows)} 條（全數列出）："
          f"{[t['tc_id'][-3:] for t, _ in rows]}")


if __name__ == "__main__":
    main()
