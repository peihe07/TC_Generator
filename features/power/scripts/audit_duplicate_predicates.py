"""G192 —— 同型缺陷之全域搜尋（R-P273）。

39 §1.3：第 6 列之 `limit(\\b|±)` 命中裸詞 `limit`，
**與 37 包 `rejudge_axis` 所修者為同一缺陷，而 `rejudge_design_method` 未同步訂正**
—— 即「**同一缺陷修於一處而未及他處**」。

R-P273：缺陷經確認後，其修正**不得僅施於發現之處** ——
須以該缺陷之**特徵**全域搜尋其出現之全部位置，逐一修正或說明何以不修。

本檔查二事：

  **甲 同名謂詞之多處定義** —— 同一名稱於 ≥ 2 個模組各自定義者，
     其內容若相異即為「已分岔之副本」，一處修而他處不修之風險最高。
  **乙 裸英文常用詞** —— 正則中以裸詞（無 `_`、無大寫、非訊號名）
     比對之常用英文字。第 6 列之 `limit` 即屬此類；
     其風險為「該詞於語料中另有無關之用法」。

**本檔只查與呈**；修正與否逐項於上繳說明。

用法：
    python features/power/scripts/audit_duplicate_predicates.py
"""

from __future__ import annotations

import ast
import collections
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
SCRIPTS = Path(__file__).resolve().parent

# 乙型之候選：正則中之裸英文詞（小寫、無底線、長度 ≥ 3）
BARE_WORD_RE = re.compile(r"(?<![\\\w])[a-z]{3,}(?![\w])")
# 排除正則語法字與明確之技術詞
SKIP = {"noqa", "utf", "str", "int", "dict", "list", "tuple", "bool", "None",
        "re", "compile", "IGNORECASE"}


def collect_patterns() -> list[tuple[str, str, str]]:
    """回傳（模組, 謂詞名, 樣式字串）。"""
    out = []
    for path in sorted(SCRIPTS.glob("*.py")):
        src = path.read_text(encoding="utf-8")
        try:
            tree = ast.parse(src)
        except SyntaxError:
            continue
        for node in tree.body:
            if not isinstance(node, ast.Assign):
                continue
            tgt = node.targets[0]
            if not isinstance(tgt, ast.Name) or not tgt.id.endswith("_RE"):
                continue
            call = node.value
            if not (isinstance(call, ast.Call) and getattr(call.func, "attr", "") == "compile"):
                continue
            try:
                pat = ast.literal_eval(call.args[0])
            except Exception:
                continue
            out.append((path.stem, tgt.id, pat))
    return out


def main() -> None:
    pats = collect_patterns()

    # ── 甲：同名謂詞之多處定義 ──
    by_name: dict[str, list[tuple[str, str]]] = collections.defaultdict(list)
    for mod, name, pat in pats:
        by_name[name].append((mod, pat))
    dup = {n: v for n, v in by_name.items() if len(v) > 1}
    diverged = {n: v for n, v in dup.items() if len({p for _, p in v}) > 1}

    # ── 乙：裸英文常用詞 ──
    bare: list[tuple[str, str, list[str]]] = []
    for mod, name, pat in pats:
        words = sorted({w for w in BARE_WORD_RE.findall(pat)
                        if w not in SKIP and len(w) >= 4})
        if words:
            bare.append((mod, name, words))

    out = ["# G192 —— 同型缺陷之全域搜尋（R-P273）\n",
           "\n> 起點：第 6 列之 `limit(\\b|±)` 命中裸詞 `limit` ——\n",
           "> 37 包已於 `rejudge_axis` 修過同一缺陷而 `rejudge_design_method` 未同步。\n",
           "> **本檔只查與呈**；修正與否逐項於上繳說明。\n",
           f"\n## 一、彙總（掃描 {len(pats)} 個謂詞定義）\n\n| 項 | 數 |\n|---|---|\n",
           f"| **甲** 同名謂詞於 ≥ 2 模組各自定義 | **{len(dup)}** |\n",
           f"| 　其中內容**已分岔**（副本不一致） | **{len(diverged)}** |\n",
           f"| **乙** 含裸英文常用詞之謂詞 | **{len(bare)}** |\n",
           f"\n## 二、甲 —— 同名謂詞之多處定義（{len(dup)}）\n\n"
           "| 謂詞名 | 模組 | 內容一致 |\n|---|---|---|\n"]
    for n, v in sorted(dup.items()):
        same = len({p for _, p in v}) == 1
        out.append(f"| `{n}` | {'、'.join('`' + m + '`' for m, _ in v)} | "
                   f"{'是' if same else '**否 —— 已分岔**'} |\n")
    if diverged:
        out.append("\n### 已分岔者之逐一比對\n")
        for n, v in sorted(diverged.items()):
            out.append(f"\n**`{n}`**\n\n")
            for m, p in v:
                out.append(f"- `{m}`：`{p}`\n")

    out.append(f"\n## 三、乙 —— 含裸英文常用詞之謂詞（{len(bare)}）\n\n"
               "> **裸詞非必為缺陷** —— 其風險為「該詞於語料中另有無關之用法」，\n"
               "> 須逐一實測其命中組成方能判定。第 6 列之 `limit` 即經此法查出。\n\n"
               "| 模組 | 謂詞 | 裸詞 |\n|---|---|---|\n")
    for mod, name, words in bare:
        out.append(f"| `{mod}` | `{name}` | {'、'.join('`' + w + '`' for w in words[:12])} |\n")

    p = DATA / "g192_duplicate_predicates.md"
    p.write_text("".join(out), encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"掃描 {len(pats)} 個謂詞定義")
    print(f"  甲 同名多處定義 {len(dup)}；**已分岔 {len(diverged)}**")
    for n, v in sorted(diverged.items()):
        print(f"     `{n}`：{[m for m, _ in v]}")
    print(f"  乙 含裸英文詞 {len(bare)}")


if __name__ == "__main__":
    main()
