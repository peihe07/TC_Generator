#!/usr/bin/env python3
"""T62 —— R-VC19(c)：保留之來源記法須對得上所引之來源列。

profile §1(c) 要求「保留之 token 確實逐字出現於該 leaf 之 `Title` 或
`Description`」。lint036 無法承載該項（見 profile §2），故由本腳本
以人工流程承擔，並逐輪明列於上繳包。

母體：本輪 pilot 之 **12 TC**（其 leaf 取自 **117 leaf 母體**之
Test Set `Glove Box`）。

判準：對每一筆之 `test_item` 上半，抽出其**非 `"..."` 之引號 token**
（`'...'` 與 `«...»`），逐一檢查該 token 是否為該 leaf 之
`Title` 或 `Description` 之**子字串**（逐字，不正規化）。

只讀不寫。
"""
import json
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
A03 = ROOT / "inputs/FM-WI-FSM-037-A03-N1L-SWE1-VehicleCategory-HMI-V0.1 STLA 報告.xlsx"

# 非 "..." 之來源記法：'...' 與 «...»
TOKEN = re.compile(r"«[^»]*»|(?<![A-Za-z])'[^']+'(?![A-Za-z])")


def source_rows():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    raw = list(wb["Analysis Report"].iter_rows(values_only=True))
    return {str(r[0]).strip(): (str(r[3]).strip(), str(r[4]).strip())
            for r in raw[7:] if r[0] not in (None, "")}


def main():
    src = source_rows()
    tcs = json.loads((ROOT / "generated" / "pilot_glovebox.json")
                     .read_text("utf-8"))["tcs"]
    rows, bad = [], []
    for t in tcs:
        lid = t["leaf_id"]
        top = t["test_item"].split("\n\n")[0]
        toks = TOKEN.findall(top)
        if not toks:
            continue
        title, desc = src[lid]
        for tok in toks:
            in_t = tok in title
            in_d = tok in desc
            ok = in_t or in_d
            where = ("Title" if in_t else "") + ("/Description" if in_d else "")
            rows.append((lid, tok, where.strip("/") or "—", ok))
            if not ok:
                bad.append((lid, tok))

    print("T62 — R-VC19(c) 保留記法之來源驗證")
    print(f"母體: {len(tcs)} TC（Glove Box，12 leaf ⊂ 117 leaf 母體）")
    print(f"帶非 \"...\" 記法之 TC: {len({r[0] for r in rows})}")
    print(f"token 數: {len(rows)}\n")
    print(f"{'leaf':<22}{'token':<28}{'出處':<18}判")
    print("-" * 74)
    for lid, tok, where, ok in rows:
        print(f"{lid:<22}{tok:<28}{where:<18}{'PASS' if ok else '**FAIL**'}")
    print("-" * 74)
    print(f"{len(rows)} tokens / {len(bad)} 未對上來源")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
