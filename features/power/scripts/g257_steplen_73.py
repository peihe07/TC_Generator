"""G257 —— Procedure 步驟字數 lint（73 包 / R-P398(b)）。

IN §5.2 之字數限制**約束 Procedure**（ER 無字數上限，IN §6 / §6.1）：
  §5.2A 一般 setup／transition 步：**≤ 12 字**
  §5.2B 末步（§5.5 之驗證擁有者）：**≤ 18 字**（含 action ＋ check target）
  §5.2C 需意圖之 setup 步（帶 `to …` 子句）：**≤ 18 字**

⚠ 72 包站④-1 量之為 **ER 末步**，欄位量錯（R-P398(b)）。本閘量 Procedure。

用法：
    python features/power/scripts/g257_steplen_73.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "features/power/data/g257_steplen_73.md"
TO_CLAUSE = re.compile(r"\bto\s+\w", re.I)


def steps(s: str) -> list[str]:
    return [re.sub(r"^\s*\d+\.\s*", "", l).strip()
            for l in (s or "").splitlines() if re.match(r"^\s*\d+\.", l)]


CHECK = re.compile(r"\bcheck (?:that|whether|which|each)\b|\bto verify\b|\bto check\b", re.I)


def limit(step: str, is_last: bool) -> int:
    """⚠ **一項判準之明示假設（74 包，執行層，待分析層追認）**

    IN §5.2 只定義三種角色：**A** 一般 setup／transition（≤12，明載「Action + target
    only; **no purpose clause**」）、**B** Final Step（≤18，**須含驗證意圖**）、
    **C** 需意圖之 setup（帶 `to …`，≤18）。

    本 corpus 之慣例為**一 TC 多個 check 步**（ER 1:1 對齊之基礎，自早期各包既然），
    故存在**非末步而自帶 `check that`** 之步 —— 該形態**不在 §5.2 之三分類內**。

    §5.2A 之定義明言其為「無 purpose clause」之步，故**不涵蓋帶 check 之步**；
    本閘據此把「非末步但帶 `check that` / `to verify`」歸為**驗證步，取 18 字**。
    此為判準之分類假設，非內容判斷；**待分析層追認**（若裁為應取 12，
    則須先裁「一 TC 只能有一個 check 步」，那是 §5.5 之適用問題，非字數問題）。
    """
    if is_last:
        return 18                      # §5.2B
    if CHECK.search(step):
        return 18                      # 非末步之驗證步 —— 見上之假設
    if TO_CLAUSE.search(step):
        return 18                      # §5.2C（`to …` 例外）
    return 12                          # §5.2A（純 setup／transition）


def main() -> None:
    cur = rm.load_current()
    rows, tally = [], Counter()
    for tc in sorted(cur, key=lambda t: t["tc_id"]):
        st = steps(tc.get("test_procedure") or "")
        for i, s in enumerate(st):
            n, lim = len(s.split()), limit(s, i == len(st) - 1)
            if n > lim:
                kind = ("§5.2B 末步" if i == len(st) - 1
                        else ("§5.2C `to …`" if TO_CLAUSE.search(s) else "§5.2A 一般"))
                rows.append((tc["tc_id"], i + 1, len(st), n, lim, kind, s))
                tally[kind] += 1

    md = ["# G257 —— Procedure 步驟字數 lint（73 包 / R-P398(b)）", "",
          "> IN §5.2 之字數限制**約束 Procedure**；ER 無字數上限（IN §6 / §6.1）。",
          "> §5.2A 一般步 ≤12、§5.2B 末步 ≤18、§5.2C 帶 `to …` 之 setup 步 ≤18。",
          "",
          "> ⚠ 72 包站④-1 量之為 **ER 末步**，欄位量錯（R-P398(b)），已撤銷。",
          "",
          f"## 逾限步 **{len(rows)}** 步（涉 {len({r[0] for r in rows})} 條 TC）", ""]
    if rows:
        md += ["| 類 | 步數 |", "|---|---|"]
        for k, v in tally.most_common():
            md.append(f"| {k} | {v} |")
        md += ["", "| tc_id | 步 | 共 | 字 | 上限 | 類 | 步文 |",
               "|---|---|---|---|---|---|---|"]
        for tid, i, tot, n, lim, kind, s in sorted(rows, key=lambda r: -r[3]):
            md.append(f"| `{tid}` | {i} | {tot} | **{n}** | {lim} | {kind} | {s[:80]} |")
    else:
        md.append("**期望值 0，實測 0 —— PASS。**")
    md.append("")
    OUT.write_text("\n".join(md))
    print(f"G257 逾限步 {len(rows)}（涉 {len({r[0] for r in rows})} 條）"
          f" → {OUT.relative_to(ROOT)}")
    for k, v in tally.most_common():
        print(f"   {v:5d}  {k}")


if __name__ == "__main__":
    main()
