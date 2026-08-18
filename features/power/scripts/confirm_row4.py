"""G170 —— 第 4 列 80 條之逐條確認證據（R-P243）。

R-P236(b) 之代理判準（`pre_conditions` 之實質條件項數 ≥ 2）僅產生**提案**；
R-P243(a) 要求逐條確認「該 TC 之結果是否**確由二個以上條件共同決定**」。

本檔**不作判定**，只蒐證 —— 判定由人工依本檔之三項證據為之：

  證據甲 **規格層**：`source_clause` 中管轄該行為之條件子句數
          （`When` / `While` / `If` / `Under` / `Unless` / `in case` 起首者）。
          條件子句 ≥ 2 者，規格本身即為多條件結構。
  證據乙 **姊妹層**：同一 leaf 內是否存在「僅差一個實質前提而 ER 不同」之姊妹 TC。
          此為決策表之結構特徵 —— 決策表之各列即為條件組合之枚舉。
          有姊妹者，該條件確實**改變結果**，非僅情境背景。
  證據丙 **輸入層**：`input_test_data` 之獨立參數數。

**證據乙之反面亦有意義**：無姊妹且規格僅一個條件子句者，
其「實質條件 ≥ 2」多為情境建構（如 bench 模式設定），代理判準即為偽陽性。

用法：
    python features/power/scripts/confirm_row4.py
"""

from __future__ import annotations

import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from rejudge_design_method import propose  # noqa: E402
from rejudge_design_method import substantive_conditions, BENCH_RE, STEP_RE  # noqa: E402

# 條件子句之起首詞（證據甲）。取自規格語料之實際措詞。
#
# **v1 → v2 之訂正（R-P187 / R-P182，並陳兩版）**
#   v1 未加 `re.I`，而語料之主要條件措詞為 **`IF`（全大寫，42 次）**
#   與小寫 `if`（35）/ `when`（14）/ `while`（5）—— v1 僅抓到首字大寫之
#   `If` / `When` / `While`，**證據甲幾近全失**。
#   v1：二證據皆無者 **37 / 80**；v2 見報表。
#   **偏誤方向：膨脹「疑似偽陽性」**，即誇大本層之發現，且會把 TC 推回落底、
#   抵銷 R-P236 之效果 —— 對執行層有利之方向，故依 R-P187 明載。
#   結構性理由：規格以 `IF … THEN` 之全大寫形式書寫（見 `SWE-PM-044`），
#   條件詞之大小寫與其是否為條件無關。
COND_RE = re.compile(
    r"\b(?:When|While|If|Under|Unless|In case|Once|As long as|"
    r"in the following .{0,12}conditions?)\b", re.I)


def cond_clauses(clause: str) -> list[str]:
    """`source_clause` 中管轄行為之條件子句（去重）。"""
    out = []
    for m in COND_RE.finditer(clause):
        seg = clause[m.start():m.start() + 90].replace("\n", " ")
        out.append(" ".join(seg.split()))
    return out


def substantive_lines(pre: str) -> list[str]:
    return [" ".join(ln.split()) for ln in pre.split("\n")
            if STEP_RE.match(ln) and not BENCH_RE.search(ln)]


def sibling(tc: dict, peers: list[dict]) -> dict | None:
    """同 leaf 內僅差一個實質前提、而 ER 不同者。"""
    mine = set(substantive_lines(tc["pre_conditions"]))
    for p in peers:
        if p["tc_id"] == tc["tc_id"]:
            continue
        theirs = set(substantive_lines(p["pre_conditions"]))
        if len(mine ^ theirs) == 2 and mine != theirs:
            if p["expected_result"] != tc["expected_result"]:
                return p
    return None


def main() -> None:
    tcs, leaf_clause = [], {}
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        d = json.loads(Path(f).read_text(encoding="utf-8"))
        for l in d.get("leaves", []):
            leaf_clause[l["parent"]] = str(l.get("source_clause", ""))
        tcs += d["tcs"]

    by_leaf: dict[str, list[dict]] = {}
    for t in tcs:
        by_leaf.setdefault(t["req_id"], []).append(t)

    row4 = [t for t in tcs if propose(t)[0] == 4]
    rows = []
    for t in sorted(row4, key=lambda x: x["tc_id"]):
        base = re.match(r"(SWE-PM-\d+)", t["req_id"]).group(1)
        conds = cond_clauses(leaf_clause.get(base, ""))
        sib = sibling(t, by_leaf[t["req_id"]])
        params = [ln for ln in str(t.get("input_test_data", "")).split("\n")
                  if ln.strip() and ln.strip() != "NA"]
        rows.append({
            "tc": t["tc_id"], "leaf": base,
            "pre": substantive_lines(t["pre_conditions"]),
            "k": substantive_conditions(t["pre_conditions"]),
            "n_cond": len(conds), "conds": conds[:3],
            "sib": sib["tc_id"][-3:] if sib else None,
            "n_param": len(params),
        })

    both = [r for r in rows if r["n_cond"] >= 2 and r["sib"]]
    spec_only = [r for r in rows if r["n_cond"] >= 2 and not r["sib"]]
    sib_only = [r for r in rows if r["n_cond"] < 2 and r["sib"]]
    neither = [r for r in rows if r["n_cond"] < 2 and not r["sib"]]

    out = ["# G170 —— 第 4 列 80 條之逐條確認證據（R-P243）\n",
           "\n> **本檔不作判定，只蒐證。** 判定見上繳 §三。\n",
           "> 證據甲＝`source_clause` 之條件子句數；"
           "證據乙＝同 leaf 內僅差一前提而 ER 不同之姊妹 TC；"
           "證據丙＝`input_test_data` 之獨立參數數。\n",
           f"\n## 一、證據交叉分布（{len(rows)} 條）\n\n"
           "| 證據甲 規格條件子句 ≥ 2 | 證據乙 有姊妹 | 條數 | 意義 |\n|---|---|---|---|\n",
           f"| 是 | 是 | **{len(both)}** | 規格為多條件結構，且該條件確實改變結果 |\n",
           f"| 是 | 否 | **{len(spec_only)}** | 規格為多條件，惟未以姊妹枚舉 |\n",
           f"| 否 | 是 | **{len(sib_only)}** | 規格僅一條件子句，惟姊妹顯示條件改變結果 |\n",
           f"| 否 | 否 | **{len(neither)}** | 二證據皆無 —— 代理判準之疑似偽陽性 |\n",
           "\n## 二、逐條\n\n"
           "| tc | leaf | 實質前提 | 甲 | 乙 姊妹 | 丙 參數 |\n|---|---|---|---|---|---|\n"]
    for r in rows:
        out.append(f"| `{r['tc'][-3:]}` | `{r['leaf']}` | "
                   f"{'；'.join(r['pre'])[:96]} | {r['n_cond']} | "
                   f"{'`…-' + r['sib'] + '`' if r['sib'] else '**無**'} | {r['n_param']} |\n")
    out.append("\n## 三、二證據皆無者（逐條，供人工判偽陽性）\n\n")
    for r in neither:
        out.append(f"- `…-{r['tc'][-3:]}`（`{r['leaf']}`）：實質前提 "
                   f"{'；'.join(r['pre'])}；規格條件子句 {r['n_cond']}\n")

    p = DATA / "g170_row4_confirmation.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"第 4 列 {len(rows)} 條")
    print(f"  甲＋乙皆有   {len(both)}")
    print(f"  僅甲（規格） {len(spec_only)}")
    print(f"  僅乙（姊妹） {len(sib_only)}")
    print(f"  二者皆無     {len(neither)}  ← 疑似偽陽性")
    for r in neither:
        print(f"     …-{r['tc'][-3:]} {r['leaf']}  前提={r['pre']}  甲={r['n_cond']}")


if __name__ == "__main__":
    main()
