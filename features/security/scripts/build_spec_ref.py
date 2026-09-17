#!/usr/bin/env python3
"""`specification_reference` 之取號計畫（SEC-18 §2-1；R-SEC10(c) amend2）。

輸入：`data/trace_matrix.tsv`（`swe1_id`／`sys_ra_sec`／`nrl`／`match_kind`）
      ＋ CCVR `SYS2 traceability`（A=SYS-RA-SEC id、B=NRL、C=description、D=Source category）
      ＋ 037 `Verification Criteria`（關鍵字篩選用）。
輸出：`data/spec_ref_plan.tsv`
      （`swe1_id | candidates_all | candidates_after_filter | lines | status | preview`）。

取號：`CFTS084-{NRL 數字}`，升冪，一號一行（cell 內 `\n`）。
"""
from __future__ import annotations

import csv
import importlib.util
import re
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features" / "security" / "data"
CCVR = (ROOT / "sources" / "raw" / "ccvr_v27_sys2_mapped" /
        "21047_24_00081_Supplier_Cybesecurity_Component_Verification_Report-v2.7_SYS2_Mapped.xlsx")

_t = importlib.util.spec_from_file_location("btm", Path(__file__).parent / "build_trace_matrix.py")
btm = importlib.util.module_from_spec(_t)
_t.loader.exec_module(btm)

# SEC-18_A（Pei 2026-09-17「他寫幾個你就對回去」）：**不篩、不設上限**。
# `match_kind` exact 與 base 皆計；不依 SYS2 category 排除；無 REVIEW 狀態。
# 原 SEC-18 §1(c) 之 category 排除與關鍵字篩選規則作廢（保留常數僅為回報「若篩會如何」）。
DROP_CATEGORIES_HISTORICAL = {"information", "heading", "reference"}


def sys2_table() -> dict[str, tuple[str, str, str]]:
    """SYS-RA-SEC id → (NRL, description, category)。"""
    ws = openpyxl.load_workbook(CCVR, read_only=True, data_only=True)["SYS2 traceability"]
    out = {}
    for row in list(ws.iter_rows(values_only=True))[1:]:
        if not row or not row[0]:
            continue
        out[str(row[0]).strip()] = (str(row[1] or "").strip(),
                                    str(row[2] or "").strip(),
                                    str(row[3] or "").strip())
    return out


def vc_map() -> dict[str, str]:
    """037 之 `Verification Criteria`（無者取 Description）。"""
    out: dict[str, str] = {}
    for doc_id, _comp in btm.SWE1_BOOKS:
        wb = openpyxl.load_workbook(btm.only(doc_id, "*.xlsx"), read_only=True, data_only=True)
        grid = list(wb["Analysis Report"].iter_rows(values_only=True))
        hdr = {str(h).strip(): i for i, h in enumerate(grid[7]) if h}
        vcol = next((i for k, i in hdr.items() if k.startswith("Verification Criteria")), None)
        dcol = next((i for k, i in hdr.items() if k.startswith("Requirement  Desc")
                     or k.startswith("Requirement Desc")), 3)
        for row in grid[8:]:
            a = str(row[0] or "").strip()
            b = str(row[1] or "").strip()
            if not a and not b:
                continue
            key = a or btm.split_source_ids(b)[0].replace(" ", "")
            text = " ".join(str(row[c] or "") for c in (dcol, vcol) if c is not None)
            out[key] = text
        wb.close()
    return out


def tokens(text: str) -> set[str]:
    return {w for w in re.findall(r"[A-Za-z][A-Za-z0-9_.]{3,}", text.lower())
            if w not in STOP}


def main() -> int:
    tm = list(csv.DictReader((DATA / "trace_matrix.tsv").open(encoding="utf-8"), delimiter="\t"))
    sys2 = sys2_table()
    vcs = vc_map()
    missing_nrl: list[str] = []
    rows = []
    for r in tm:
        swe1 = r["swe1_id"]
        ids = [i.strip() for i in (r["sys_ra_sec"] or "").split(";") if i.strip()]
        exact = r["match_kind"] == "exact"
        kept = []
        for i in ids:
            meta = sys2.get(i)
            if meta is None:
                missing_nrl.append(f"{swe1}:{i}")
                continue
            nrl, desc, cat = meta
            if not nrl:
                missing_nrl.append(f"{swe1}:{i}(no NRL)")
                continue
            kept.append((i, nrl, desc, cat))
        status = "OK" if kept else "FALLBACK"
        lines = [f"CFTS084-{re.sub(r'[^0-9]', '', n)}" for _, n, _, _ in
                 sorted(kept, key=lambda k: int(re.sub(r"[^0-9]", "", k[1])))] or [swe1]
        dropped = sum(1 for _, _, _, c in kept
                      if c.strip().lower() in DROP_CATEGORIES_HISTORICAL)
        rows.append({"swe1_id": swe1, "candidates_all": len(ids), "lines": len(lines),
                     "status": status, "category_excluded_if_filtered": dropped,
                     "preview": " ⏎ ".join(lines[:5]) + (" …" if len(lines) > 5 else ""),
                     "_kept": kept})

    with (DATA / "spec_ref_plan.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "candidates_all", "lines", "status",
                    "category_excluded_if_filtered", "preview"])
        for r in rows:
            w.writerow([r["swe1_id"], r["candidates_all"], r["lines"], r["status"],
                        r["category_excluded_if_filtered"], r["preview"]])

    # 供生成器用：swe1_id → 逐行值（`\n` 分隔）
    with (DATA / "spec_ref_values.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "value"])
        for r in rows:
            val = ("\n".join(f"CFTS084-{re.sub(r'[^0-9]', '', n)}" for _, n, _, _ in
                             sorted(r["_kept"], key=lambda k: int(re.sub(r"[^0-9]", "", k[1]))))
                   if r["status"] == "OK" else r["swe1_id"])
            w.writerow([r["swe1_id"], val.replace("\n", "⏎")])

    from collections import Counter
    print("spec_ref_plan.tsv：", dict(Counter(r["status"] for r in rows)))
    ln = sorted(r["lines"] for r in rows if r["status"] == "OK")
    if ln:
        print(f"  OK 列之行數 min/median/max = {ln[0]}／{ln[len(ln)//2]}／{ln[-1]}")
    mx = max(rows, key=lambda r: r["lines"])
    print(f"  最大列：{mx['swe1_id']} {mx['lines']} 行")
    print("  NRL 不在 SYS2 traceability 者：", missing_nrl or "無")
    import collections
    grp = collections.defaultdict(list)
    for r in rows:
        grp[r["swe1_id"].split("-")[1] if r["swe1_id"].startswith("SWE1") else "ECUCert"
            ].append(r["lines"])
    for g, v in sorted(grp.items()):
        v.sort()
        print(f"  {g:16s} {len(v):2d} 列  行數 min/median/max = "
              f"{v[0]}／{v[len(v)//2]}／{v[-1]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
