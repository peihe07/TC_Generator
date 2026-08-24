#!/usr/bin/env python3
"""IN §9 自查表之機檢對映（R-G21@`1230e795`）。

R-G21 令 §9 自查表**逐項標註其保證來源**：有對應 lint 閘者記閘 id
（入 `GATES.tsv`），無者標「人工項」。其目的是
**使「機器保證」與「人力承擔」在紙上分得開**（G-D、G-E 之精神）。

**對映之三態**（不是二態 —— 這是本表最重要之設計）：

| 覆蓋 | 意義 |
|---|---|
| `full` | 該項之判準全部由所列閘承擔 |
| `partial` | 閘只覆蓋該項之一部分，**其餘仍為人力** |
| `manual` | 無閘，全由人讀承擔 |

**`partial` 不得記為 `full`。** 自查第 1 項要求 Test Set 為
capability-level 名詞片語且與 `framework.md` 一致，而閘 `G` 只驗其**非空**
—— 記 `full` 會使「G 綠」被讀成「第 1 項已保證」，
**而那正是 G-E 所指之形態：可測範圍到底之後，品質由人讀承擔。**

`residual_manual` 欄逐項寫出**閘接不住的那一半是什麼** ——
只標 `partial` 而不說殘餘為何，人讀時不知道自己要看什麼。

輸出 `docs/runtime/SELFCHECK_MAP.tsv`；`gates_tsv.py` 由此回填
`GATES.tsv` 之 `selfcheck_items` 欄（反向索引）。
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

IN_CANON = "docs/runtime/ASPICE_SWE6_AI_Instruction.md"
OUT_DEFAULT = "docs/runtime/SELFCHECK_MAP.tsv"
COLUMNS = ["item", "coverage", "gate_ids", "in_sections", "residual_manual", "summary"]

# 對映表 —— item → (coverage, gates, 殘餘人力之內容)
# 判定依據逐項見上繳 26 §六；`partial` 之殘餘不得留空。
MAPPING: dict[int, tuple[str, list[str], str]] = {
    1:  ("partial", ["G"],
         "G 只驗 Test Set 非空；名詞片語／capability-level／與 framework.md 一致／"
         "無 Test Group 前綴／拼寫一致／非 Unclassified 或 Misc —— 六項皆人讀"),
    2:  ("manual", [],
         "tc_title 之三種形態、2–14 字、sibling token 可見、無情態詞 —— "
         "lint036 無 tc_title 閘（feature 級 vf230_selfcheck_wvf62 有字數檢查，未入本簿）"),
    3:  ("partial", ["D", "R"],
         "D 驗 Pre-Condition 之違規詞、R 驗其版面（未編號行／多條件並列）；"
         "「每一條是 spec 觸發條件而非環境穩定前提」（§8.5）為語意判斷，人讀"),
    4:  ("partial", ["M"],
         "M 只驗空欄三態；欄位歸屬是否正確、重複資料是否已移入 PC／Procedure —— 人讀"),
    5:  ("partial", ["A"],
         "A 驗禁用動詞；「步驟可執行」與「末步驟擁有驗證」（§5.5）為人讀"),
    6:  ("manual", [], "步驟長度與意圖層級之三分類 —— 無可測判準"),
    7:  ("manual", [], "標準 setup 片語是否逐字重用 —— 無片語清單可比對"),
    8:  ("manual", [], "CLI／工具步驟之 description + `$` 格式 —— 無閘"),
    9:  ("manual", [], "需要前後比較時是否取 baseline —— 需判斷「是否需要」，無閘"),
    10: ("partial", ["E", "B", "H"],
         "E 驗 proc/er 編號行數對齊、B 驗 ER 情態詞、H 驗 ER 模糊語；"
         "「ER 可觀察」「結果涵蓋完整」「多階段版面之適用時機」為人讀"),
    11: ("manual", [],
         "無 False Pass／False Fail；supported 須配負向 —— 配對之完整性需跨 TC 判斷"),
    12: ("partial", ["U", "F"],
         "U 計 PENDING 佔位、F 攔方括號佔位；追溯至 Req/SWRA、RD 分解不越界、"
         "無造值、無範圍造作 —— 皆人讀（其中造值為 IN §8.4.1／§8.4.2）"),
    13: ("manual", [], "Design Method 是否於 procedure 定稿後才指派 —— 順序不可由產物觀察"),
    14: ("full", ["N"], ""),
    15: ("full", ["F"], ""),
    16: ("manual", [],
         "specification_reference 是否列出**每一個**直接驗證之 spec 節 —— "
         "G17／G18 型之雙向閘在 feature 級存在，lint036 無"),
    17: ("manual", [],
         "來源 spec 優先於索引匯出、門檻取自 spec 之具體值、相似操作於 ER 消歧、"
         "變體標籤一致、styled 元素不臆測為不可操作 —— 五項皆人讀"),
}


def parse_items(root: Path) -> dict[int, tuple[str, str]]:
    """自 IN §9 逐項抽出（編號 → (摘要, 所引 IN 節號)）。"""
    text = (root / IN_CANON).read_text(encoding="utf-8").splitlines()
    start = next(i for i, l in enumerate(text) if l.startswith("## 9. Self-Check"))
    end = next(i for i, l in enumerate(text[start + 1:], start + 1) if l.startswith("## "))
    out: dict[int, tuple[str, str]] = {}
    for line in text[start:end]:
        m = re.match(r"^(\d+)\.\s+(.*)$", line.strip())
        if not m:
            continue
        n, body = int(m.group(1)), m.group(2)
        secs = sorted(set(re.findall(r"§[0-9]+(?:\.[0-9]+){0,2}", body)))
        summary = re.sub(r"\s*\(§[^)]*\)", "", body).strip()
        out[n] = (summary, "／".join(secs))
    return out


def rows(root: Path) -> list[dict]:
    items = parse_items(root)
    missing = sorted(set(items) ^ set(MAPPING))
    if missing:
        raise SystemExit(f"對映表與 IN §9 之項目不一致：{missing}（R-G21 令 17 項全數分類）")
    out = []
    for n in sorted(items):
        coverage, gates, residual = MAPPING[n]
        summary, secs = items[n]
        if coverage == "partial" and not residual:
            raise SystemExit(f"第 {n} 項標 partial 而未寫殘餘人力 —— 不得留空")
        out.append({
            "item": str(n), "coverage": coverage,
            "gate_ids": ",".join(gates) if gates else "人工項",
            "in_sections": secs, "residual_manual": residual,
            "summary": summary[:140],
        })
    return out


def reverse_index(root: Path) -> dict[str, list[str]]:
    """gate_id → 其所保證之自查項編號（供 GATES.tsv 之 `selfcheck_items` 欄）。"""
    idx: dict[str, list[str]] = {}
    for n, (_, gates, _) in MAPPING.items():
        for g in gates:
            idx.setdefault(g, []).append(str(n))
    return {g: sorted(v, key=int) for g, v in idx.items()}


def main() -> int:
    ap = argparse.ArgumentParser(description="自查表機檢對映（R-G21）")
    ap.add_argument("--root", default=".")
    ap.add_argument("--out", default=OUT_DEFAULT)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    root = Path(args.root).resolve()
    data = rows(root)
    body = "\n".join(["\t".join(COLUMNS)]
                     + ["\t".join(r[c] for c in COLUMNS) for r in data]) + "\n"
    out = root / args.out
    if args.check:
        if not out.exists() or out.read_text(encoding="utf-8") != body:
            print(f"FAIL: {args.out} 與現行對映不符", file=sys.stderr)
            return 1
        print(f"OK: {args.out} 相符（{len(data)} 項）")
        return 0

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    tally: dict[str, int] = {}
    for r in data:
        tally[r["coverage"]] = tally.get(r["coverage"], 0) + 1
    print(f"寫入 {args.out}：{len(data)} 項")
    for k in ("full", "partial", "manual"):
        print(f"    {k:<9}{tally.get(k, 0):>3}")
    covered = {g for _, gs, _ in MAPPING.values() for g in gs}
    print(f"  對映到之閘 {len(covered)} 支：{','.join(sorted(covered))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
