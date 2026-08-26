#!/usr/bin/env python3
"""T105(c) —— Title 越界之全批檢查（下放包 19 §2.2）。

形態：037 作者改寫 `Title` 時，把**他 leaf 之 Description 內容**併入了
本 leaf 之敘述。實例：`VC-025-02` 之 Title 含 `Aux 1, Aux 2`，
而該二項在 `-03` 之 Description，不在 `-02`。

**危害異於 A-VC10 之前三面**：前三面影響單筆之正確性，
本面影響**批次之追溯結構** —— 若上半取 Title，該 TC 即涵蓋 sibling
所擁有之行為，違 IN §8.2.1 並產生重複追溯。

⚠ **初版漏抓下放包 §2.2 已點名之 `VC-025-02`** —— Title 寫 `Aux 1`／`Aux 2`，
而 `-03` 之 Description 寫 `Aux Camera 1`／`Aux Camera 2`：**簡寫對不上全稱**，
逐字子串比對失效。此即下放包 §五.3 所預告之偽陰性
（「Title 之改寫若為同義而非逐字挪用，字串比對看不到」）。
已補**詞集包含**之第二段判準。

**這是第三次「掃描器漏抓它被造出來要抓的那一筆」**（T52／T79／本次）。
PLAYBOOK §7.1(b) 正是為此而設，而本次之已知標的就寫在下放包裡 ——
**我應該先跑它再看結果，順序反了。**

判準（保守，寧可多報）：
  對每個 leaf，取其 `Title` 中之**專有名詞短語**（連續 Title-Case 詞組
  與引號／括號內字串），逐一檢查：
    (1) 該詞是否出現於**本 leaf 之 Description**（出現則無越界）
    (2) 否則是否出現於**同節他 leaf 之 Description**（是則為越界候選）
  其餘（二者皆無）另列 —— 那是 Title 獨有之改寫用語，非越界。

母體：本批之 leaf（預設 `Controls` 17 筆）。只回報，不處置。
"""
import re
import sys
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"

# 專有名詞短語：連續之 Title-Case 詞（允許數字與 &/-），長度 ≥ 2 詞，
# 或引號／括號內之字串。單詞者噪音過大，不取。
PHRASE = re.compile(r"\b(?:[A-Z][A-Za-z0-9&/-]*)(?:\s+(?:[A-Z][A-Za-z0-9&/-]*|\d+)){1,5}\b")
STOP = {"The", "This", "That", "When", "If", "On", "In", "For", "Map", "Adopt",
        "Items", "Settings", "Controls", "Expose", "Reflect", "Require"}


def phrases(s: str):
    out = set()
    for m in PHRASE.finditer(s):
        p = m.group(0).strip()
        w = p.split()
        while w and w[0] in STOP:
            w = w[1:]
        if len(w) >= 2:
            out.add(" ".join(w))
    return out


def main(test_set="Controls"):
    sys.path.insert(0, str(Path(__file__).parent))
    from partn import load
    leaves = [r for r in load()[0] if r["test_set"] == test_set]
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    raw = list(wb["Analysis Report"].iter_rows(values_only=True))
    desc = {str(r[0]).strip(): str(r[4]).strip() for r in raw[7:] if r[0]}

    by_sec = defaultdict(list)
    for r in leaves:
        by_sec[r["section"]].append(r["req_id"])

    cross, titleonly = [], []
    for r in sorted(leaves, key=lambda x: x["req_id"]):
        rid, sec = r["req_id"], r["section"]
        own = desc.get(rid, "")
        sibs = [s for s in by_sec[sec] if s != rid]
        for p in sorted(phrases(r["title"])):
            if p.lower() in own.lower():
                continue
            hit = [s for s in sibs if p.lower() in desc.get(s, "").lower()]
            if not hit:
                # 第二段：**詞集包含** —— 簡寫對全稱（`Aux 1` ⊂ `Aux Camera 1`）。
                # 於 sibling 之 Description 上滑動 2–6 詞之窗，
                # 若本詞之詞集為某窗詞集之子集，即為越界候選。
                pt = {w.lower() for w in p.split()}
                for s in sibs:
                    dw = re.findall(r"[A-Za-z0-9]+", desc.get(s, ""))
                    for n in range(len(pt), 7):
                        if any(pt <= {x.lower() for x in dw[i:i + n]}
                               for i in range(max(0, len(dw) - n + 1))):
                            hit.append(s)
                            break
                    if s in hit:
                        continue
            if hit:
                cross.append((rid, p, sorted(set(hit))))
            else:
                titleonly.append((rid, p))

    print(f"Test Set: {test_set}；leaf {len(leaves)} 筆")
    print(f"\n=== A. **越界候選** —— Title 之詞不在本 leaf 之 Description，"
          f"卻在同節他 leaf 之 Description：{len(cross)} 處")
    for rid, p, hit in cross:
        print(f"  {rid.replace('SWE1-HMI-VC-', ''):<10} {p!r:<34} "
              f"→ 屬 {[h.replace('SWE1-HMI-VC-', '') for h in hit]}")
    print(f"\n=== B. Title 獨有之詞（非越界，改寫用語）：{len(titleonly)} 處")
    for rid, p in titleonly[:24]:
        print(f"  {rid.replace('SWE1-HMI-VC-', ''):<10} {p!r}")
    if len(titleonly) > 24:
        print(f"  …（共 {len(titleonly)} 處）")
    return cross


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "Controls")
    sys.exit(0)
