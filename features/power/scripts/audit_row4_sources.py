"""G187 —— 第 4 列代理判準之條件來源擴充（R-P267）。

R-P260(a) 判 `…-026` / `…-027` 為第 4 列（`LTM High` 是否存在 ＋ 所選之值），
而 `substantive_conditions` **只數到 1 項** ——
成因：其第二個條件（所選之值）**在 `test_procedure` 而非 `pre_conditions`**。
**條件不必然全數落於 `pre_conditions`。**

本檔將條件來源擴及 `test_procedure` 與 `input_test_data`，重跑代理判準。

**條件之計數方式（R-P250：先量再寫）**
`pre_conditions` 之實質條件沿用 `substantive_conditions`（扣除 bench 樣板列）。
`test_procedure` 之條件＝**設定或施加某具名參數之值**之步驟：
語料實測其措詞為 `Set … to`（37）、`Select "…" for`（12）、`Send … signal`（41）、
`Apply …`（6）、`Keep … at`（4）—— 取其**具名參數 ＋ 取值**者為一個條件。
`input_test_data` 之條件＝其非 `NA` 之每一列（每列為一個參數取值）。

**代理判準仍不得凌駕實質判準**（R-P236(b)）—— 其結果為提案。
**本檔不改值**（R-P267(d) / §I）。

用法：
    python features/power/scripts/audit_row4_sources.py
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
from rejudge_design_method import propose, substantive_conditions, STEP_RE  # noqa: E402

# `test_procedure` 中「設定／施加某具名參數之值」之步驟。
# 措詞取自語料實測，非自擬。
PROC_COND_RE = re.compile(
    r"\bSet\b.{0,60}?\bto\b|\bSelect\b\s*\"[^\"]+\"\s*for\b|"
    r"\bSend\b.{0,50}?\bsignal|\bApply\b\s+the\b|\bKeep\b.{0,40}?\bat\b|"
    r"\bHold\b.{0,40}?\bat\b", re.I)


def proc_conditions(proc: str) -> list[str]:
    out = []
    for ln in proc.split("\n"):
        if STEP_RE.match(ln) and PROC_COND_RE.search(ln):
            out.append(" ".join(ln.split()))
    return out


def data_conditions(data: str) -> list[str]:
    if str(data).strip().upper() in ("", "NA"):
        return []
    return [" ".join(ln.split()) for ln in str(data).split("\n") if ln.strip()]


def total_conditions(tc: dict) -> tuple[int, list[str]]:
    pre_n = substantive_conditions(tc["pre_conditions"])
    pc = proc_conditions(tc["test_procedure"])
    dc = data_conditions(tc.get("input_test_data", ""))
    return pre_n + len(pc) + len(dc), pc + dc


def load() -> list[dict]:
    tcs = []
    for f in sorted(glob.glob(str(ROOT / "features/power/generated/*.json"))):
        tcs += json.loads(Path(f).read_text(encoding="utf-8"))["tcs"]
    return tcs


def main() -> None:
    tcs = load()
    cur_row4 = {t["tc_id"] for t in tcs if propose(t)[0] == 4}

    # 擴充後：凡**第 1–3 列未命中**且總條件 ≥ 2 者即為第 4 列
    # （first-match 之序不變，只換第 4 列之判準）
    new_row4, added = set(), []
    for t in tcs:
        row = propose(t)[0]
        if row in (-1, 1, 2, 3):
            continue                       # 前列已命中者不受影響
        n, extra = total_conditions(t)
        if n >= 2:
            new_row4.add(t["tc_id"])
            if t["tc_id"] not in cur_row4:
                added.append((t, n, extra, row))

    out = ["# G187 —— 第 4 列代理判準之條件來源擴充（R-P267）\n",
           "\n> **本檔只出提案，不改值**（R-P267(d)）。\n",
           "> 代理判準仍不得凌駕實質判準（R-P236(b)）。\n",
           "\n## 一、條件之計數方式（先量語料）\n\n"
           "| 來源 | 計法 |\n|---|---|\n"
           "| `pre_conditions` | 實質條件項數（扣除 bench 樣板列），沿用 `substantive_conditions` |\n"
           "| `test_procedure` | **設定或施加某具名參數之值**之步驟數 —— 措詞實測："
           "`Set … to` / `Select \"…\" for` / `Send … signal` / `Apply …` / `Keep … at` |\n"
           "| `input_test_data` | 非 `NA` 之每一列（每列一個參數取值） |\n",
           f"\n## 二、影響面\n\n| | 條數 |\n|---|---|\n"
           f"| 現行第 4 列（只數 `pre_conditions`） | **{len(cur_row4)}** |\n"
           f"| 擴充後第 4 列 | **{len(new_row4)}** |\n"
           f"| **新增** | **{len(added)}** |\n",
           f"\n## 三、新增者逐條（{len(added)}）—— 供分析層抽樣複核\n\n"
           "| tc | 現落點 | 總條件 | 新增之條件（來自 procedure / data） |\n|---|---|---|---|\n"]
    for t, n, extra, row in sorted(added, key=lambda x: x[0]["tc_id"]):
        out.append(f"| `…-{t['tc_id'][-3:]}` | 第 {row} 列 | {n} | "
                   f"{'；'.join(x[:60] for x in extra)} |\n")

    p = DATA / "g187_row4_sources.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"第 4 列：{len(cur_row4)} → {len(new_row4)}（新增 {len(added)}）")
    print(f"新增者之現落點分布："
          f"{dict(collections.Counter(r for _, _, _, r in added))}")
    # R-P267 之二例應被納入
    for k in ("026", "027"):
        got = any(t["tc_id"].endswith(k) for t, _, _, _ in added)
        print(f"  R-P267 所舉之 `…-{k}` 是否被納入：{'是' if got else '**否**'}")


if __name__ == "__main__":
    main()
