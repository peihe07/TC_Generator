#!/usr/bin/env python3
"""R-DM8 re-adjudication for SWE-DM-004/005 (handoff 03 §4.1 / step 9).

Puts SYS2's hot-behaviour rows (r31-r34, heading r30) next to the CFTS_020
clauses that carry the same subject, and asks ONE question per gap:
is the value still absent from the materials in hand?

Output is 缺/不缺 plus the evidence location. NO value is copied into any
conclusion field, and nothing is written back (R-DM8, canon §8.4.1).
"""
import re
from pathlib import Path

import docx
import openpyxl

ROOT = Path(__file__).resolve().parents[1]
SYS2 = ROOT / "inputs" / ("SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System"
                          "_Accepted & Released.xlsx")
CFTS = ROOT / "inputs" / ("R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 "
                          "ICS and DCSD _20260310-1533.docx")

SYS2_ROWS = [30, 31, 32, 33, 34]
CFTS_CLAUSES = ["1.11.2.2", "1.15.1.5", "1.15.2.5", "1.15.4.5"]


def norm(s):
    return " ".join(str(s or "").split())


def main():
    print("# SWE-DM-004 / 005 —— SYS2 與 CFTS 併讀")
    print("依 R-DM8：本輪只判「缺／不缺」與證據位置，不讀出、不回填任何值")

    wb = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
    grid = [list(r) for r in wb["Basic Report"].iter_rows(values_only=True)]
    wb.close()
    head = [norm(h) for h in grid[0]]
    c_fid = head.index("SYS2 Sys-RA-Feature-ID")
    c_cat = head.index("SYS2 分類 Category")
    c_desc = head.index("Description")

    print("\n## SYS2 `Basic Report` r30–r34（逐字，全文）")
    for rn in SYS2_ROWS:
        r = grid[rn - 1]
        print(f"\n### r{rn}  {norm(r[c_fid])}  [{norm(r[c_cat])}]")
        print(norm(r[c_desc]))

    d = docx.Document(CFTS)
    blocks, head_txt = [], "(前言)"
    for p in d.paragraphs:
        style = str(p.style.name).lower() if p.style is not None else ""
        txt = norm(p.text)
        if style.startswith("heading") and txt:
            head_txt = txt
        if txt:
            blocks.append((head_txt, txt))

    print("\n## CFTS_020 之對應章節（逐字，全文）")
    for clause in CFTS_CLAUSES:
        sel = [(h, t) for h, t in blocks if h.startswith(clause + " ")]
        if not sel:
            print(f"\n### {clause} —— 章節不存在")
            continue
        print(f"\n### {sel[0][0]}  （{len(sel)} 段）")
        for h, t in sel:
            print(f"  {t}")

    print("\n## 訊號／值 token 之兩側對照（逐字比對，非相似度）")
    sys2_txt = " ".join(norm(grid[rn - 1][c_desc]) for rn in SYS2_ROWS)
    cfts_txt = " ".join(t for h, t in blocks
                        if any(h.startswith(c + " ") for c in CFTS_CLAUSES))
    sig_s = set(re.findall(r"\$([A-Za-z0-9_]+)\$", sys2_txt))
    sig_c = set(re.findall(r"\$([A-Za-z0-9_]+)\$", cfts_txt))
    val_s = {v.strip() for v in re.findall(r"\[([A-Za-z0-9_%\s]+)\]", sys2_txt)}
    val_c = {v.strip() for v in re.findall(r"\[([A-Za-z0-9_%\s]+)\]", cfts_txt)}
    print(f"  訊號 僅 SYS2 有: {sorted(sig_s - sig_c)}")
    print(f"  訊號 僅 CFTS 有: {sorted(sig_c - sig_s)}")
    print(f"  訊號 兩側皆有  : {sorted(sig_s & sig_c)}")
    print(f"  值   僅 SYS2 有: {sorted(val_s - val_c)}")
    print(f"  值   僅 CFTS 有: {sorted(val_c - val_s)}")
    print(f"  值   兩側皆有  : {sorted(val_s & val_c)}")

    print("\n## 溫度門檻之出現位置（只報位置與是否存在）")
    temp = re.compile(r"\b\d+\s*(?:deg(?:rees)?\s*c|°\s*c)\b", re.I)
    print(f"  SYS2 r30–r34 含溫度數值+單位之列: "
          f"{[rn for rn in SYS2_ROWS if temp.search(norm(grid[rn-1][c_desc]))] or '無'}")
    hits = [(h, t) for h, t in blocks if temp.search(t)]
    print(f"  CFTS 全文含溫度數值+單位之段: {len(hits)}")
    for h, t in hits:
        print(f"    [{h}]")


if __name__ == "__main__":
    main()
