#!/usr/bin/env python3
"""表 A（FROP 跨域揭露）之編製（下放包 27 T142）。

**承 REV-14** —— 母體標註為義務（R-VC15），且**不得沿用下放包 24 §3.1
之敘述**（該敘述為母體混用之產物）。本檔逐列重測，不引用任何既有數字。

「跨域」之定義：FROP ≠ 本 feature 之歸屬域。
本 feature 之歸屬域實測為 `Vehicle Settings`（117 leaf 中 104 筆），
故跨域者為 `Power Management` 與 `Audio Management`。
"""
import csv
import glob
import json
from collections import Counter
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / ("inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1"
              " STLA 報告.xlsx")
OUT = ROOT / "docs/TABLE_A_frop_crossdomain.md"
HOME = "Vehicle Settings"

rows = [r for r in list(openpyxl.load_workbook(A03, read_only=True,
                                               data_only=True)["Analysis Report"]
                        .iter_rows(values_only=True))[7:] if r[0] not in (None, "")]
frop = {str(r[0]).strip(): (str(r[7]).strip() if r[7] else "(空)") for r in rows}
title = {str(r[0]).strip(): str(r[3]).strip() for r in rows}

recon = {r["req_id"]: r for r in csv.DictReader(
    (ROOT / "data/recon_leaf_to_section.tsv").open(encoding="utf-8"), delimiter="\t")}
leaves = [r["req_id"] for r in csv.DictReader(
    (ROOT / "data/priority_final.tsv").open(encoding="utf-8"), delimiter="\t")]
prio = {r["req_id"]: r["final_p"] for r in csv.DictReader(
    (ROOT / "data/priority_final.tsv").open(encoding="utf-8"), delimiter="\t")}
tsmap = {r["section"]: r["test_set"] for r in csv.DictReader(
    (ROOT / "data/test_set_map.tsv").open(encoding="utf-8"), delimiter="\t")}

tcs = {}
for f in sorted(glob.glob(str(ROOT / "generated/*.json"))):
    d = json.loads(Path(f).read_text("utf-8"))
    for t in d["tcs"]:
        tcs.setdefault(t["leaf_id"], []).append((d["batch"], t["tc_title"]))

row_dist = Counter(frop[str(r[0]).strip()] for r in rows)
leaf_dist = Counter(frop[l] for l in leaves)
cross = [l for l in leaves if frop[l] not in (HOME, "(空)")]
cross_tc = sum(len(tcs.get(l, [])) for l in cross)
row_cross = [str(r[0]).strip() for r in rows if frop[str(r[0]).strip()] not in (HOME, "(空)")]
total_tc = sum(len(v) for v in tcs.values())

L = []
L.append("# 表 A —— FROP 跨域揭露（Vehicle Category）\n")
L.append("> **出貨門檻二表之一**（R-VC3）。缺之不得出貨。\n")
L.append(f"- 編製：`scripts/build_table_a.py`，下放包 27 T142\n"
         f"- 來源：`{A03.name}` 第 8 欄 `FROP (Feature Rollout Plan)`，"
         f"**逐列讀，非抽樣**\n"
         f"- **本表不引用任何既有敘述之數字** —— 承 REV-14，全部重測\n")
L.append("\n---\n\n## 0. 母體標註（R-VC15）\n")
L.append("本表涉及**二個母體**，其數字**不得互援**：\n")
L.append("| 母體 | 定義 | 大小 |\n|---|---|---|")
L.append(f"| **145 列** | 037 `Analysis Report` 之全部資料列（含 parent）| {len(rows)} |")
L.append(f"| **117 leaf** | 其中之 leaf（R-VC3 全取）| {len(leaves)} |")
L.append("\n### 0.1 FROP 分布 —— 二母體並列\n")
L.append("| FROP | 145 列母體 | 117 leaf 母體 |\n|---|---|---|")
for k in sorted(set(row_dist) | set(leaf_dist)):
    mark = "" if k == HOME else " **（跨域）**"
    L.append(f"| `{k}`{mark} | {row_dist.get(k, 0)} | {leaf_dist.get(k, 0)} |")
L.append(f"| **合計** | **{sum(row_dist.values())}** | **{sum(leaf_dist.values())}** |")
L.append(f"""
**歸屬域**：`{HOME}`（117 leaf 中 {leaf_dist[HOME]} 筆，
145 列中 {row_dist[HOME]} 筆）—— 本表之「跨域」即指 FROP ≠ 此值。

**FROP 欄無空值** —— 145 列全部有值，故跨域之判定不涉缺值處置。
""")
L.append(f"""### 0.2 ⚠ 兩個 17，落在不同母體（R-VC15／R-VC17）

| 量 | 母體 | 值 |
|---|---|---|
| 跨域**列**數 | 145 列 | **{len(row_cross)}** |
| 跨域 leaf 所產出之 **TC** 數 | {total_tc} TC（六批合計）| **{cross_tc}** |
| 跨域 **leaf** 數 | 117 leaf | {len(cross)} |

**前二者皆為 17，而它們不是同一件事** —— 一個是 037 的列、
一個是本專案產出的測試案例。**其相等為巧合，不得互援、不得據以主張對應。**

`DECISIONS.md` 簽署時所載之「145 列中之 17 列」即上表第一列，**該標註正確**。
本節之設立是因為第二個 17 是本輪新算出來的 —— **REV-11／REV-14 兩次教訓
都始於兩個相同的數字**，故在它們出現時即標明。
""")
L.append("\n---\n\n## 1. 跨域 leaf 逐筆（117 leaf 母體）\n")
L.append(f"**{len(cross)} leaf → {cross_tc} TC。**\n")
L.append("| req_id | section | FROP | Test Set | 批次 | P | TC 數 | TC 標題 |")
L.append("|---|---|---|---|---|---|---|---|")
for l in cross:
    ts = tsmap.get(recon[l]["outline"], "(未對應)")
    got = tcs.get(l, [])
    b = got[0][0] if got else "**(未生成)**"
    names = "<br>".join(f"{i}. {t}" for i, (_, t) in enumerate(got, 1)) or "—"
    L.append(f"| `{l.replace('SWE1-HMI-VC-', 'VC-')}` | {recon[l]['outline']} | "
             f"**{frop[l]}** | {ts} | `{b}` | {prio[l]} | {len(got)} | {names} |")

L.append("\n---\n\n## 2. 對照 —— 章 13 之 FROP 組成（REV-14 之標的）\n")
ch13 = [l for l in leaves if recon[l]["outline"].startswith("13")]
d13 = Counter(frop[l] for l in ch13)
row13 = [str(r[0]).strip() for r in rows
         if recon.get(str(r[0]).strip(), {}).get("outline", "").startswith("13")]
L.append(f"""下放包 24 §3.1 曾稱「章 13 之 FROP = Power Management **全批**」，
**實測不成立**。REV-11／REV-14 已記其成因（母體混用）。本節為表 A 之佐證欄。

| 母體 | 章 13 之組成 |
|---|---|
| 145 列 | {len(row13)} 列 —— {dict(Counter(frop[x] for x in row13))} |
| **117 leaf** | **{len(ch13)} leaf —— {dict(d13)}** |

**章 13 之 `{HOME}` 四筆逐筆具名**（即使其非跨域，仍列此以杜絕再次反推）：
""")
for l in ch13:
    if frop[l] == HOME:
        L.append(f"- `{l.replace('SWE1-HMI-VC-', 'VC-')}`（§{recon[l]['outline']}）"
                 f" —— {title[l][:64]}…")
L.append(f"""
**R-VC16(e) 之正確讀法**：`Power Management` 之 16 **列**全部落在章 13
（該命題在列母體上成立）；**其逆命題「章 13 全為 PM」在 leaf 母體上不成立**。
""")
L.append("\n---\n\n## 3. 已知限制（R-G8）\n")
L.append(f"""- **FROP 值取自 037 第 8 欄，未與任何 FROP 主檔核對** ——
  本表只能證明「037 這樣寫」，不能證明「FROP 計畫確實如此分派」。
  **DR-VC5（FROP 跨域 17 列之承接單位）仍未結**，其回覆可能改變本表之解讀。
- **`Test Set` 取自 `data/test_set_map.tsv`**（framework §2 之 8 組）——
  若 DR-VC3 回覆為「應補」，章 8／9 另立 `Cabrio Rooftop` 將使組數變 9，
  **本表之 `Test Set` 欄須重編**（R-VC16(c)）。
- **TC 數為本輪之實測**（六批 JSON 之 `tcs`）。尾段 6 leaf 未生成者標
  `(未生成)`，其 TC 數為 0 —— **非「該 leaf 不需 TC」**。
- 本表**未涵蓋 `{HOME}` 之 {leaf_dist[HOME]} 筆** —— 依定義它們非跨域。
""")
OUT.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"{OUT.relative_to(ROOT)} —— 跨域 {len(cross)} leaf / {cross_tc} TC；"
      f"跨域列 {len(row_cross)}")
