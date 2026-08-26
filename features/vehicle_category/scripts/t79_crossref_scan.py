#!/usr/bin/env python3
"""T79 —— 純交叉引用型 leaf 之全表掃描（下放包 14 §四，承 A-VC17）。

A-VC17 之形態：037 之某 leaf，其 `Title` 與 `Description` **皆僅為交叉引用**
而無可測內容 —— 即該 leaf 不指向任何可觀察之行為，只指向另一份文件或另一節。
實例：`VC-013-04`（Description 逐字為 `Refer to PDO graphics.`）。

母體：**117 leaf**（母體標註依 R-VC15）。

判準三段，逐段收窄：

  A 段（引用詞）—— `Description` 命中引用詞（refer to／see／per／
      as defined in／according to／表頭形態）。
  B 段（可測內容之殘餘）—— 去掉引用片語後，該欄是否仍有動詞性內容。
      殘餘 token 數 < 門檻者列為候選。
  C 段（人工）—— 候選逐筆判讀 `Title` 是否**另行補入**可測內容。
      A-VC10 已證 037 之 Title 常多載於 Description，故不得只看 Description。

**只回報，不處置**（下放包 14 §四 T79 之明文）。偽陰性見上繳包 14。
"""
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"

# ⚠ 初版含裸 `per`，命中 `one radio button per line` 之 `per` ——
# 那是「每」不是「依據」。已移除裸 `per`，只留 `as per`。
REF = re.compile(
    r"\b(refer(?:\s+to)?|see|as\s+per|as\s+defined\s+in|according\s+to|"
    r"as\s+described\s+in|for\s+complete\s+logic)\b", re.I)
# 引用片語：引用詞 + 其標的（至句末或右括號）
REF_PHRASE = re.compile(
    r"\(?\s*\b(?:refer(?:\s+to)?|see|as\s+per|as\s+defined\s+in|"
    r"according\s+to|as\s+described\s+in)\b[^.)]*[.)]?", re.I)
# 動詞性內容之近似：祈使／宣告動詞
VERB = re.compile(
    r"\b(display|show|render|present|remove|hide|grey|appear|contain|"
    r"return|open|close|play|enable|disable|block|allow|order|filter|"
    r"restore|reset|clear|move|position|follow|continue|is|are|will|shall)\b",
    re.I)
RESIDUE_TOKENS = 6

# ⚠ 表頭之判定不得只靠「無動詞」——
# 初版以 VERB 未命中為條件，而 `Vehicle Tab Labels and Order.` 之
# `Order` 是名詞卻命中了動詞表，**掃描器因而漏掉 VC-007-01**
# （分析層 §2.3(a) 已點名之其中一筆）。
# 改以**題名形態**判定：去掉 `Cn.)` 之條號前綴後，
# 其字母 token 多數為 Title-Case 且無小寫功能詞連接成句者，判為表頭。
HEADNUM = re.compile(r"^\s*[A-Z]*\d[\d.]*\s*\)\s*")
FUNC = re.compile(r"\b(the|a|an|is|are|will|shall|if|when|that|to|of|in|on|"
                  r"with|for|not|do|does)\b", re.I)


def looks_like_heading(text: str) -> bool:
    s = HEADNUM.sub("", text).strip().rstrip(".")
    toks = [w for w in re.findall(r"[A-Za-z][A-Za-z\'-]*", s)]
    if not toks or len(toks) > 8:
        return False
    if FUNC.search(s):
        return False                      # 有功能詞即已成句，非題名
    caps = sum(1 for w in toks if w[:1].isupper())
    return caps >= max(2, len(toks) - 1)   # 幾乎全為 Title-Case


def main():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    raw = list(wb["Analysis Report"].iter_rows(values_only=True))
    rows = [r for r in raw[7:] if r[0] not in (None, "")]
    P = re.compile(r"^SWE1-HMI-VC-(\d{3})$")
    C = re.compile(r"^SWE1-HMI-VC-(\d{3})-(\d{2})$")
    ids = [str(r[0]).strip() for r in rows]
    pc = {C.match(i).group(1) for i in ids if C.match(i)}
    leaves = [r for r in rows
              if C.match(str(r[0]).strip())
              or (P.match(str(r[0]).strip())
                  and P.match(str(r[0]).strip()).group(1) not in pc)]

    a_hits, cand = [], []
    for r in leaves:
        rid, title, desc = str(r[0]).strip(), str(r[3]).strip(), str(r[4]).strip()
        if not REF.search(desc):
            # 表頭形態：無引用詞、無動詞、短
            if looks_like_heading(desc):
                cand.append((rid, "表頭形態", title, desc, desc))
            continue
        a_hits.append(rid)
        residue = REF_PHRASE.sub(" ", desc)
        residue = re.sub(r"^[\W\d]+|[\W]+$", "", residue).strip()
        if len(residue.split()) < RESIDUE_TOKENS or not VERB.search(residue):
            cand.append((rid, "引用後殘餘不足", title, desc, residue))

    print(f"母體: {len(leaves)} leaf（117 leaf 母體）")
    print(f"A 段 — Description 命中引用詞: {len(a_hits)} leaf")
    print(f"B 段 — 候選（引用後殘餘不足／表頭形態）: {len(cand)} leaf\n")
    print("=== C 段候選（須人工判讀 Title 是否另行補入可測內容）")
    for rid, why, title, desc, res in cand:
        print(f"\n--- {rid}  [{why}]")
        print(f"    D  : {desc[:150]}")
        print(f"    殘餘: {res[:100]!r}")
        print(f"    T  : {title[:150]}")
    return cand


if __name__ == "__main__":
    main()
    sys.exit(0)
