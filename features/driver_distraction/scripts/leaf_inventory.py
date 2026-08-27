#!/usr/bin/env python3
"""T4 —— SWE1 28 leaf 之逐列清單（下放包 01 §五 T4）。

欄位形制沿 `bed_lowering`。**`_x000D_` 正規化於此步做並留原文欄** ——
正規化後之欄供比對，原文欄供追溯；只留其一即無從證明正規化沒改別的東西。
"""
import csv
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
A03 = ROOT / "inputs/DD_SWE1_0807_EN.xlsx"
OUT = ROOT / "data/leaf_inventory.tsv"
COLS = dict(req_id=0, source_req_id=1, title=2, description=3,
            categorization=14, sub_categorization=15, priority=16,
            verification_criteria=17, verification_method=18)


def norm(s):
    """`_x000D_` 為 Excel 匯出之 CR 殘留。正規化 = 轉真換行 ＋ 壓縮空白。

    **只碰 `_x000D_` 與空白**，不碰任何其他字元 —— 原文欄可證。
    """
    s = str(s or "").replace("_x000D_\n", "\n").replace("_x000D_", "\n")
    return re.sub(r"[ \t]+", " ", s).strip()


def main():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    rows = [r for r in wb["Analysis Report"].iter_rows(min_row=9, values_only=True)
            if r[0] not in (None, "")]
    hdr = ["req_id", "source_req_ids", "title", "description",
           "categorization", "sub_categorization", "priority",
           "verification_criteria", "verification_method",
           "description_raw", "vc_raw", "had_x000D"]
    n_x = 0
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
        w.writerow(hdr)
        for r in rows:
            raw_d, raw_v = str(r[3] or ""), str(r[17] or "")
            had = "_x000D_" in raw_d or "_x000D_" in raw_v
            n_x += had
            srcs = "; ".join(s.strip() for s in norm(r[1]).split("\n") if s.strip())
            w.writerow([
                str(r[0]).strip(), srcs, norm(r[2]), norm(r[3]).replace("\n", "\\n"),
                str(r[14] or "").strip(), str(r[15] or "").strip(),
                str(r[16] or "").strip(),
                norm(r[17]).replace("\n", "\\n"), norm(r[18]).replace("\n", "\\n"),
                raw_d.replace("\n", "\\n").replace("\t", " "),
                raw_v.replace("\n", "\\n").replace("\t", " "),
                "yes" if had else "no",
            ])
    print(f"{OUT.relative_to(ROOT)} —— {len(rows)} 列"
          f"（應 28 —— {'閉合 ✅' if len(rows) == 28 else '**不閉合 ❌**'}）")
    print(f"含 `_x000D_` 之列：{n_x} / {len(rows)}")
    # 正規化只動 _x000D_ 與空白之證明：把原文欄之 _x000D_ 與空白抹平後應相等
    bad = []
    for r in rows:
        a = re.sub(r"\s+", "", str(r[3] or "").replace("_x000D_", ""))
        b = re.sub(r"\s+", "", norm(r[3]))
        if a != b:
            bad.append(str(r[0]).strip())
    print(f"正規化未動其他字元：{'✅' if not bad else '**❌ ' + str(bad) + '**'}")


if __name__ == "__main__":
    main()
