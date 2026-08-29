#!/usr/bin/env python3
"""CFTS020 之「節前定義塊」全面掃查（下放包 07 作業 B 之第二半、R-ICS27(e)）。

**立此掃查之理由**（R-ICS27(e) 逐字之精神）：同一份 CFTS020 已用了五包，
而 `4819541`（§1.8.1 之 time-variables 定義塊）直到第五包才被讀到 ——
**不得假定只有這一塊**。前四包之誤不在讀錯，在只讀需求句而未讀節前之定義。

## 何謂「節前定義塊」（本檔之操作型定義，逐項揭露）

一個物件，其本文**不陳述某 ECU 於某條件下應為何**（＝不是行為需求），
而是**為其所在章節宣告一組符號、值域、預設值或列舉**，供該節之需求句引用。
以下五組型樣任一命中即列入候選（不分大小寫）：

  T1 宣告式引語：`the following ... shall be used`、`For this section`、
                 `within the scope of this section`、`shall be defined as`
  T2 符號賦值：  `<符號> =`（角括號內為識別字）
  T3 值域宣告：  `range of`、`valid values`、`shall be between`、
                 `minimum of`／`maximum of` 且同句帶數值
  T4 預設值：    `default value`、`default setting`、`initial value`
  T5 列舉宣告：  `one of the following`、`shall be set to one of`

**候選非結論**：型樣命中只表示「像定義塊」，逐筆仍須人讀。
本檔之輸出為清單，不是裁定（R-ICS27(e) 令「出清單」）。

適用性一律依 R-ICS2 v2(b)，判定取自 `cfts020_probe.py`（不另實作）。

輸出：docs/reports/07_predef_blocks.md
"""
from __future__ import annotations

import importlib.util
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("probe", ROOT / "scripts/cfts020_probe.py")
probe = importlib.util.module_from_spec(spec)
spec.loader.exec_module(probe)

PATTERNS = {
    "T1 宣告式引語": [r"the following[^.]{0,60}shall be used", r"for this section",
                  r"within the scope of this section", r"shall be defined as"],
    "T2 符號賦值": [r"<[A-Za-z_][A-Za-z0-9_]*>\s*="],
    "T3 值域宣告": [r"range of\s+\d", r"valid values", r"shall be between",
                r"minimum of\s+\d", r"maximum of\s+\d"],
    "T4 預設值": [r"default value", r"default setting", r"initial value"],
    "T5 列舉宣告": [r"one of the following", r"shall be set to one of"],
}


def hits(text: str) -> list[str]:
    out = []
    for name, pats in PATTERNS.items():
        for p in pats:
            if re.search(p, text, re.I):
                out.append(name)
                break
    return out


def symbols(text: str) -> list[str]:
    return sorted(set(re.findall(r"<([A-Za-z_][A-Za-z0-9_]*)>\s*=", text)))


def main() -> None:
    objs = probe.parse()
    cands = []
    for o in objs:
        h = hits(o["text"])
        if h:
            cands.append((o, h))

    L = ["# CFTS020 節前定義塊 — 全面掃查（2026-08-29）", "",
         "> 下放包 07 作業 B 之第二半，依 **R-ICS27(e)**。",
         "> 本檔由 `scripts/predef_sweep_07.py` 產生；**表格非人工謄寫**。",
         "> 操作型定義與五組型樣見該腳本檔頭。",
         "> **候選非結論** —— 型樣命中只表示「像定義塊」，逐筆仍須人讀。", "",
         f"## §0 母數與命中", "",
         f"- CFTS020 物件總數 **{len(objs)}**（屬性頭 `^\\d{{7}}: \\[`）",
         f"- 型樣命中之候選 **{len(cands)}** 個"
         f"（{len(cands) * 100 // len(objs)}%）",
         f"- 其中 R-ICS2 v2 判**適用**者 **{sum(1 for o, _ in cands if o['v2'] == '適用')}** 個",
         ""]

    c = Counter(t for _, hs in cands for t in hs)
    L += ["型樣分佈（一物件可命中多型）：", ""]
    for k in sorted(c):
        L.append(f"- {k}：{c[k]}")

    applic = [(o, h) for o, h in cands if o["v2"] == "適用"]
    L += ["", "## §1 **適用**之候選（逐筆；本節為須人讀之清單）", "",
          "| ObjectID | § | Artifact Type | 命中型樣 | 賦值符號 | 本文（前 160 字）|",
          "|---|---|---|---|---|---|"]
    for o, h in applic:
        syms = "、".join(symbols(o["text"])) or "—"
        body = o["text"][:160].replace("|", "\\|")
        L.append(f'| **{o["id"]}** | {o["section_no"]} | {o["artifact_type"]} | '
                 f'{"、".join(h)} | {syms} | {body} |')

    L += ["", "## §2 已錨定者（對照）", "",
          "`CFTS020-4819541` 為 R-ICS27(a) 所錨之 §1.8.1 定義塊。"
          "本掃查是否命中它，是本工具有效性之自檢：", ""]
    got = [o for o, _ in cands if o["id"] == "4819541"]
    L.append(f"- `4819541` 是否命中：**{'是' if got else '否 —— 工具失效，須查'}**")
    if got:
        L.append(f"- 其命中型樣：{'、'.join(hits(got[0]['text']))}")
        L.append(f"- 其賦值符號：{'、'.join(symbols(got[0]['text']))}")

    L += ["", "## §3 不適用之候選（僅列數與 ObjectID，供回溯）", "",
          f"共 **{len(cands) - len(applic)}** 個：",
          "", "```",
          "  ".join(o["id"] for o, _ in cands if o["v2"] != "適用"),
          "```", ""]

    L += ["## §4 全文之賦值符號總表（`<符號> =` 之相異識別字）", "",
          "| 符號 | 出現於幾個物件 | 其中判適用者 |", "|---|---|---|"]
    sym_map: dict[str, list] = {}
    for o in objs:
        for s in symbols(o["text"]):
            sym_map.setdefault(s, []).append(o)
    for s in sorted(sym_map):
        ap = sum(1 for o in sym_map[s] if o["v2"] == "適用")
        L.append(f"| `<{s}>` | {len(sym_map[s])} | {ap} |")

    Path(ROOT / "docs/reports/07_predef_blocks.md").write_text("\n".join(L) + "\n")
    print(f"寫入 docs/reports/07_predef_blocks.md")
    print(f"  物件 {len(objs)}／候選 {len(cands)}／適用之候選 {len(applic)}")
    print(f"  4819541 命中：{'是' if got else '否'}")
    print(f"  相異賦值符號 {len(sym_map)} 個")


if __name__ == "__main__":
    main()
