"""G171 —— 第 7 列與第 2 列之反向查（R-P244）。

第 2 列已證實其詞彙謂詞漏判真故障注入（`…-008` 之措詞為 `Stop the broadcast`，
不含 `disconnect` / `fault injection`）。第 7 列同型風險未排除 ——
其命中 0 係「無從判定」而非「已判為不適用」。

R-P244：改自**結構特徵**出發，不自詞彙出發。

  第 7 列（Combinatorial）之結構特徵：
    `input_test_data` ＋ `pre_conditions` 中列有**二個以上獨立參數**，
    且該組合於同一 leaf 內被**枚舉多次**（各參數取不同值）——
    組合測試之定義即為參數取值之組合枚舉。
    **單一參數變動而其餘固定者不算** —— 那是決策表之逐列，非組合。

  第 2 列（Fault Injection）之結構特徵：
    `test_procedure` 中含「**移除／中斷／停止某既有輸入**」之動作 ——
    即先有一個正常存在之輸入，步驟將其去除。
    不以「故障」二字為條件。

二者皆只產生**候選**，逐條之判定屬人工（本檔不判定）。

用法：
    python features/power/scripts/reverse_probe_rows.py
"""

from __future__ import annotations

import collections
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_design_method import STEP_RE  # noqa: E402
from confirm_row4 import substantive_lines  # noqa: E402

# 參數＝具名標的加一個取值。取自語料之實際書寫形態：
#   `STATUS_LIN.Batt_ST_Crit = [1h]` / `Timeout1 is at "00 min"` /
#   `$VC_MODEL_YEAR$ equal to "2025"` / `Rear_View_Camera reads "Present"`
PARAM_RE = re.compile(
    r"(\$?[A-Za-z][\w.]*\$?)\s*(?:=|==|is at|reads|equal to|is equal to|"
    r"greater than|carries)\s*[\"“\[]?([^\"”\[\]\n,;]{1,28})")

# 第 2 列之結構特徵：移除／中斷／停止一個既有輸入
REMOVE_RE = re.compile(
    r"\b(?:stop|stops|stopping|remove|removes|withhold|withholds|"
    r"interrupt|interrupts|cut|cuts|disconnect|disconnects|"
    r"cease|ceases|suppress|suppresses|disable|disables)\b.{0,60}"
    r"\b(?:broadcast|signal|signals|supply|power|transmission|message|messages|bus)\b",
    re.I)


def params(tc: dict) -> dict[str, str]:
    out = {}
    text = str(tc.get("input_test_data", "")) + "\n" + \
        "\n".join(substantive_lines(tc["pre_conditions"]))
    for name, val in PARAM_RE.findall(text):
        out.setdefault(name.strip(), val.strip())
    return out


def main() -> None:
    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]

    by_leaf: dict[str, list[dict]] = {}
    for t in tcs:
        by_leaf.setdefault(re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1), []).append(t)

    # ── 第 7 列 ──
    row7 = []
    for leaf, group in by_leaf.items():
        if len(group) < 2:
            continue
        pmaps = {t["tc_id"]: params(t) for t in group}
        # 該 leaf 內出現於 ≥ 2 條 TC 且取值不只一種之參數
        varying = collections.defaultdict(set)
        for pm in pmaps.values():
            for k, v in pm.items():
                varying[k].add(v)
        multi = {k for k, vs in varying.items() if len(vs) >= 2}
        if len(multi) < 2:
            continue
        # 組合枚舉之判準：存在二條 TC，其**二個以上**參數同時相異
        for i, a in enumerate(group):
            for b in group[i + 1:]:
                pa, pb = pmaps[a["tc_id"]], pmaps[b["tc_id"]]
                diff = {k for k in multi
                        if k in pa and k in pb and pa[k] != pb[k]}
                if len(diff) >= 2:
                    row7.append((leaf, a["tc_id"][-3:], b["tc_id"][-3:], sorted(diff)))

    # ── 第 2 列 ──
    row2 = [(t["tc_id"][-3:], re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1),
             m.group(0), t["design_method"])
            for t in tcs if (m := REMOVE_RE.search(str(t.get("test_procedure", ""))))]

    out = ["# G171 —— 第 7 / 2 列之反向查（R-P244）\n",
           "\n> 自**結構特徵**出發，不自詞彙出發。**本檔只出候選，判定屬人工。**\n",
           f"\n## 一、第 7 列（Combinatorial）候選 —— **{len(row7)}** 對\n\n",
           "判準：同一 leaf 內存在二條 TC，其**二個以上**獨立參數同時取不同值。\n"
           "單一參數變動而其餘固定者為決策表之逐列，不計。\n\n"]
    if row7:
        out.append("| leaf | TC 對 | 同時相異之參數 |\n|---|---|---|\n")
        for leaf, a, b, diff in row7:
            out.append(f"| `{leaf}` | `…-{a}` / `…-{b}` | {'、'.join('`'+d+'`' for d in diff)} |\n")
    else:
        out.append("**無候選。**\n")

    out.append(f"\n## 二、第 2 列（Fault Injection）候選 —— **{len(row2)}** 條\n\n"
               "判準：`test_procedure` 含「移除／中斷／停止某既有輸入」之動作。\n\n"
               "| tc | leaf | 命中之結構 | 現值 `design_method` |\n|---|---|---|---|\n")
    for tid, leaf, hit, dm in row2:
        out.append(f"| `…-{tid}` | `{leaf}` | `{hit}` | {dm} |\n")

    p = DATA / "g171_reverse_probe.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"第 7 列候選：{len(row7)} 對")
    for leaf, a, b, diff in row7[:10]:
        print(f"   {leaf}  …-{a}/…-{b}  {diff}")
    print(f"第 2 列候選：{len(row2)} 條")
    for tid, leaf, hit, dm in row2:
        print(f"   …-{tid}  {leaf}  「{hit}」  現值 {dm}")


if __name__ == "__main__":
    main()
