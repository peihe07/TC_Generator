"""G256 —— IN §11 引號規則之 lint（72 包 / R-P397(b)）。

R-P384(b) 之「具名不以引號為要件」為**抽取**判準；
**書寫**依 IN §11 —— Procedure／ER 中之具名 UI 元件須以 `"…"` 包覆。

本層於 67／68／71 三包連續三次漏此規則（皆事後補正），
分析層之字典亦同（72 包 §0）—— **故入 lint，由閘擋而非靠人記**。

判準（**以全案已加引號之名為字典**，避免泛稱誤判）：

  1. 先蒐集全案 Procedure／ER 中**已以 `"…"` 書寫之具名元件**，成為「已知名」集合；
  2. 再掃全案，凡**該集合中之名以未加引號之形式出現**者即違規。

此判準只認**同一名在同一 corpus 內時而加引號、時而未加**之不一致 ——
即 67／68／71 三包所犯之形態。**不判斷「某泛稱是否應為具名」**（那是分析層之事）。

排除：`PENDING:` 佔位句、`Apply FUNC_STATE_…` / `Apply ENTER_…` 之片段引用、
`test_item` 上半（verbatim 不得改，R-6）。

用法：
    python features/power/scripts/g256_quotes_72.py
"""

from __future__ import annotations

import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import remeasure_55 as rm  # noqa: E402

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "features/power/data/g256_quotes_72.md"

QUOTED = re.compile(r'"([^"]{2,48})"')
SKIP = re.compile(r"^\s*\d*\.?\s*PENDING:|Apply (?:FUNC_STATE|ENTER)_", re.I)
# 具名元件之特徵：含 R-P353(ii) 類名詞，或為多字專名
NOUNY = re.compile(
    r"\b(screens?|icons?|pop-?ups?|logos?|animations?|buttons?|menus?|fonts?"
    r"|graphics?|gauges?|avatars?|sound)\b", re.I)


def known_names(cur) -> set[str]:
    """全案已以 `\"…\"` 書寫之具名元件。"""
    names = set()
    for tc in cur:
        for f in ("test_procedure", "expected_result"):
            for m in QUOTED.finditer(tc.get(f) or ""):
                v = m.group(1).strip()
                if len(v.split()) >= 2 and NOUNY.search(v):
                    names.add(v)
    return names


def offenders(line: str, names: set[str]) -> list[str]:
    if SKIP.search(line):
        return []
    masked = QUOTED.sub(lambda m: " " * len(m.group(0)), line)
    return [n for n in names if re.search(r"\b" + re.escape(n) + r"\b", masked, re.I)]


def main() -> None:
    cur = rm.load_current()
    names = known_names(cur)
    print(f"已知具名元件 {len(names)} 個：{'、'.join(sorted(names)[:8])} …")
    rows, tally = [], Counter()
    for tc in sorted(cur, key=lambda t: t["tc_id"]):
        for f in ("test_procedure", "expected_result"):
            for line in (tc.get(f) or "").splitlines():
                bad = offenders(line, names)
                if not bad:
                    continue
                for b in bad:
                    tally[b.lower()] += 1
                rows.append((tc["tc_id"], f, line.strip(), bad))

    md = ["# G256 —— IN §11 引號 lint（72 包 / R-P397(b)）", "",
          "> 具名 UI 元件於 Procedure／ER 須以 `\"…\"` 包覆（IN §11）。",
          "> R-P384(b) 之「不以引號為要件」為**抽取**判準，非書寫。",
          "",
          "> 判準：**以全案已加引號之具名元件為字典**，凡該名以**未加引號**之形式",
          "> 出現者即違規 —— 只認同一名在同一 corpus 內之**書寫不一致**，",
          "> 不判斷「某泛稱是否應為具名」（那是分析層之事）。",
          "",
          f"> 已知具名元件 **{len(names)}** 個。",
          "",
          f"## 違規句 **{len(rows)}** 句（涉 {len({r[0] for r in rows})} 條 TC）",
          ""]
    if rows:
        md += ["| tc_id | 欄 | 未加引號之名詞 | 句 |", "|---|---|---|---|"]
        for tid, f, line, bad in rows[:200]:
            md.append(f"| `{tid}` | {f} | {'、'.join(f'`{b}`' for b in bad)} | "
                      f"{line[:90]} |")
        md.append("")
        md += ["## 名詞分布", "", "| 名詞 | 次 |", "|---|---|"]
        for k, v in tally.most_common():
            md.append(f"| `{k}` | {v} |")
    else:
        md.append("**期望值 0，實測 0 —— PASS。**")
    md.append("")
    OUT.write_text("\n".join(md))
    print(f"G256 違規句 {len(rows)}（涉 {len({r[0] for r in rows})} 條）"
          f" → {OUT.relative_to(ROOT)}")
    for k, v in tally.most_common(12):
        print(f"   {v:4d}  {k}")


if __name__ == "__main__":
    main()
