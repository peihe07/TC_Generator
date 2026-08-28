#!/usr/bin/env python3
"""T18b（下放包 12 §6.1）—— B1 之訊號涵蓋掃描。

掃 leaf `-001`~`-008`、`-013`~`-016`（12 leaf）之 037 **全欄**，
擷取全部 `$...$` token，與 profile §3 之五項比對。

**已涵蓋者**可逕用 profile §3 之寫法；**未涵蓋者**逐項列出其所在 leaf
與 037 原文脈絡。**掃出未涵蓋即剔除該 leaf，不臆造施加路徑。**

唯讀。
"""
import re
from collections import defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
A03 = ROOT / "inputs" / "DD_SWE1_0807_EN.xlsx"

SCOPE = [f"{n:03d}" for n in list(range(1, 9)) + list(range(13, 17))]

# profile §3 之五項（逐字，含其狀態）
PROFILE_S3 = {
    "Speedometer":        "解除 —— STATUS_CCAN3.VehicleSpeedVSOSig",
    "PresentGear":        "解除 —— PT_SYSTEM_FD_1.GearEngagedForDisplay_PT",
    "Country_Code":       "解除 —— PROXI Country_Code = 91（標 A-DD5）",
    "VC_Trans_Equipped":  "**SUSPENDED** —— DR-DD5／DR-DD6",
    "PARK_BRK_EGD":       "保留來源名 —— DR-DD2 未結",
}
RE_TOKEN = re.compile(r"\$([^$\s]+)\$")


def main():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    rows = [list(r) for r in wb["Analysis Report"].iter_rows(values_only=True)]
    wb.close()

    idx = {}
    for i, row in enumerate(rows, 1):
        m = re.match(r"SWE1-RA-Driver_Distraction-(\d+)$", str(row[0] or ""))
        if m:
            idx[m.group(1)] = (i, row)

    print("=" * 78)
    print("T18b —— 訊號涵蓋掃描（B1 前置）")
    print("=" * 78)
    print(f"母體：037 `Analysis Report` 之 leaf {SCOPE[0]}~{SCOPE[7]}、"
          f"{SCOPE[8]}~{SCOPE[-1]}（**12 leaf**），**全 20 欄**逐格掃 `$...$`。")
    print("比對標的：profile §3 之五項。\n")

    per_leaf = {}
    all_tok = defaultdict(list)          # token -> [(leaf, 欄, 脈絡)]
    for k in SCOPE:
        assert k in idx, f"037 無 leaf {k}"
        i, row = idx[k]
        toks = []
        for j, v in enumerate(row):
            if v is None:
                continue
            for m in RE_TOKEN.finditer(str(v)):
                tk = m.group(1)
                if tk not in toks:
                    toks.append(tk)
                s = str(v)
                a, b = max(0, m.start() - 55), min(len(s), m.end() + 55)
                all_tok[tk].append((k, j, re.sub(r"\s+", " ", s[a:b]).strip()))
        per_leaf[k] = toks

    print("-" * 78)
    print("逐 leaf 之 `$...$` token")
    print("-" * 78)
    for k in SCOPE:
        i, _ = idx[k]
        t = per_leaf[k]
        print(f"  -{k} (037 r{i}): {t if t else '（無 $…$ token）'}")

    covered = {t for t in all_tok if t in PROFILE_S3}
    uncovered = {t for t in all_tok if t not in PROFILE_S3}

    print()
    print("-" * 78)
    print(f"已涵蓋（profile §3 五項之內）：{len(covered)} 個")
    print("-" * 78)
    for t in sorted(covered):
        ls = sorted({x[0] for x in all_tok[t]})
        print(f"  ${t}$  —— profile §3：{PROFILE_S3[t]}")
        print(f"      出現於 leaf：{ls}")

    print()
    print("-" * 78)
    print(f"**未涵蓋**（profile §3 五項之外）：{len(uncovered)} 個")
    print("-" * 78)
    if not uncovered:
        print("  無")
    for t in sorted(uncovered):
        ls = sorted({x[0] for x in all_tok[t]})
        print(f"\n  **${t}$**  —— 出現於 leaf：{ls}")
        for k, j, ctx in all_tok[t]:
            print(f"      -{k} c{j}: …{ctx}…")

    # profile §3 中未被本輪 12 leaf 用及者
    unused = set(PROFILE_S3) - covered
    print()
    print("-" * 78)
    print(f"profile §3 五項中，本 12 leaf 未用及者：{sorted(unused) if unused else '無'}")

    # B1 範圍判定
    bad = sorted({k for t in uncovered for k, _, _ in all_tok[t]})
    susp = sorted({k for t in covered if "SUSPENDED" in PROFILE_S3[t]
                   for k, _, _ in all_tok[t]})
    drop = sorted(set(bad) | set(susp))
    keep = [k for k in SCOPE if k not in drop]
    print()
    print("=" * 78)
    print("B1 範圍判定（§6.2）")
    print("=" * 78)
    print(f"  因**未涵蓋訊號**而剔除：{bad or '無'}")
    print(f"  因**profile §3 標 SUSPENDED**而剔除：{susp or '無'}")
    print(f"  **剔除合計**：{drop or '無'}（{len(drop)} leaf）")
    print(f"  **B1 範圍**：{keep}（{len(keep)} leaf）")
    return keep, drop


if __name__ == "__main__":
    main()
