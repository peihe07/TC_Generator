#!/usr/bin/env python3
"""下放包 12 作業 B：87 個「軸層適用、變體不合、範圍隨變體層」之物件於 SYS2 之收錄面量測。

只量不裁。本腳本不作任何「應否納入」之判斷，只輸出實測數。

掃描條件（逐項揭露）：
  - CFTS020 物件與三層分列：以 `importlib` **唯讀載入** `cfts020_probe.py`，
    呼叫 `parse()`（判準 R-ICS2 v2(b)）。不修改該檔。
      * 87 個 = `verdict == "適用"` ∧ `variant_fits_dut is False` ∧ `scope == "隨變體層"`
      * 29 個 = `verdict == "適用"` ∧ `variant_fits_dut is False` ∧ `scope != "隨變體層"`
  - SYS2：`inputs/SYS2_..._All_HW_System_Accepted & Released.xlsx`
      * openpyxl，`data_only=True`、`read_only=True`
      * 分頁 `Basic Report`（另有 `Polarion`／`_polarion` 二分頁為工具用，不含需求列）
      * **表頭列 = 第 1 列**；資料列 = 第 2～334 列，共 333 列
      * 所取欄（以欄名引用）：
          `ID`
          `Description`
          `SYS2 來源需求項目ID  Source Requirement items`   ← ObjectID 比對欄
          `SYS2 分類 Category`
          `SYS2 子分類 Sub Category Function Name`
          `SYS2 SW/HW/System (如果是HW+SW，就選System) ( software, hardware, or system (both software and hardware).)`
          `SYS2 MD Feedback`
          `SYS2 文件識別碼 Document ID`
  - ObjectID 比對方式：來源欄之儲存格內容以 `re.findall(r"\\d{7}")` 取出**所有** 7 位數字，
    與 CFTS020 之 ObjectID 作**精確字串**比對（一列可含多個來源 ID；一個 ObjectID
    亦可能對到多列）。不作前綴／模糊比對。

用法：
  python3 features/ics_management/scripts/sys2_87_probe_12.py            # 摘要
  python3 features/ics_management/scripts/sys2_87_probe_12.py --table    # §1 逐一表
  python3 features/ics_management/scripts/sys2_87_probe_12.py --reverse  # §4 反向查核
"""
from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
PROBE = ROOT / "scripts" / "cfts020_probe.py"
SYS2 = ROOT / ("inputs/SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_"
               "Accepted & Released.xlsx")

SHEET = "Basic Report"
HEADER_ROW = 1
COL_ID = "ID"
COL_DESC = "Description"
COL_SRC = "SYS2 來源需求項目ID  Source Requirement items"
COL_CAT = "SYS2 分類 Category"
COL_SUB = "SYS2 子分類 Sub Category Function Name"
COL_SWHW = ("SYS2 SW/HW/System (如果是HW+SW，就選System) "
            "( software, hardware, or system (both software and hardware).)")
COL_MD = "SYS2 MD Feedback"
COL_DOC = "SYS2 文件識別碼 Document ID"
WANTED = [COL_ID, COL_DESC, COL_SRC, COL_CAT, COL_SUB, COL_SWHW, COL_MD, COL_DOC]

ID_RE = re.compile(r"\d{7}")


def load_probe():
    """以 importlib 唯讀載入既有 probe，不改其檔。"""
    spec = importlib.util.spec_from_file_location("cfts020_probe", PROBE)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def cfts_objects() -> list[dict]:
    return load_probe().parse()


def split_sets(objs: list[dict]) -> tuple[list[dict], list[dict], list[dict]]:
    """三層交叉分列：(138 合 DUT, 29 範圍層算數, 87 範圍隨變體層)。"""
    fit, ruled, follow = [], [], []
    for o in objs:
        if o["verdict"] != "適用":
            continue
        if o["variant_fits_dut"]:
            fit.append(o)
        elif o["scope"] != "隨變體層":
            ruled.append(o)
        else:
            follow.append(o)
    return fit, ruled, follow


def sys2_rows() -> list[dict]:
    """回傳 SYS2 `Basic Report` 之資料列（以欄名為鍵）。"""
    wb = openpyxl.load_workbook(SYS2, data_only=True, read_only=True)
    ws = wb[SHEET]
    rows = list(ws.iter_rows(values_only=True))
    header = [str(c) if c is not None else "" for c in rows[HEADER_ROW - 1]]
    for w in WANTED:
        if w not in header:
            raise SystemExit(f"表頭查無欄名：{w!r}")
    idx = {w: header.index(w) for w in WANTED}
    out = []
    for r in rows[HEADER_ROW:]:
        if all(c is None for c in r):
            continue
        rec = {w: (r[idx[w]] if idx[w] < len(r) else None) for w in WANTED}
        rec["_src_ids"] = ID_RE.findall(str(rec[COL_SRC] or ""))
        out.append(rec)
    return out


def build_index(rows: list[dict]) -> dict[str, list[dict]]:
    idx: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        for sid in r["_src_ids"]:
            idx[sid].append(r)
    return idx


def top_of(o: dict) -> str:
    return ".".join(o["section_no"].split(".")[:2]) if o["section_no"] else "(無節)"


def shape(rows: list[dict]) -> dict:
    """一組 SYS2 列之欄位形態摘要（§3 對照用）。"""
    return {
        "列數": len(rows),
        "Category": dict(Counter(str(r[COL_CAT]) for r in rows)),
        "子分類": dict(Counter(str(r[COL_SUB]) for r in rows)),
        "SW/HW/System": dict(Counter(str(r[COL_SWHW]) for r in rows)),
        "Document ID": dict(Counter(str(r[COL_DOC]) for r in rows)),
        "MD Feedback 非空": sum(1 for r in rows if r[COL_MD]),
    }


def group_report(name: str, objs: list[dict], idx: dict[str, list[dict]]) -> None:
    hit_objs = [o for o in objs if idx.get(o["id"])]
    hit_rows = [r for o in hit_objs for r in idx[o["id"]]]
    print(f"\n== {name}：物件 {len(objs)}，SYS2 有對應者 {len(hit_objs)}"
          f"，對應之 SYS2 列數 {len(hit_rows)}")
    for k, v in shape(hit_rows).items():
        print(f"   {k}: {v}")
    fr = [r for r in hit_rows if str(r[COL_CAT]).strip().lower()
          == "functional requirement"]
    print(f"   其中 Category == Functional Requirement 之列數: {len(fr)}")
    print(f"   對應到 FR 列之物件數: {len({o['id'] for o in hit_objs for r in idx[o['id']] if str(r[COL_CAT]).strip().lower()=='functional requirement'})}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--table", action="store_true", help="§1 87 個逐一之對應判")
    ap.add_argument("--reverse", action="store_true", help="§4 反向查核")
    a = ap.parse_args()

    objs = cfts_objects()
    fit, ruled, follow = split_sets(objs)
    rows = sys2_rows()
    idx = build_index(rows)

    print(f"# CFTS020 物件 {len(objs)}；三層交叉：合DUT {len(fit)}／"
          f"範圍層算數 {len(ruled)}／範圍隨變體層 {len(follow)}")
    print(f"# SYS2 `{SHEET}` 資料列 {len(rows)}；帶來源 ID 之列 "
          f"{sum(1 for r in rows if r['_src_ids'])}；相異來源 ID {len(idx)}")

    if a.table:
        print("\n| # | ObjectID | 頂層節 | 節號 | SYS2 對應 | SYS2 ID | Category | 子分類 | SW/HW/System |")
        print("|---|---|---|---|---|---|---|---|---|")
        for i, o in enumerate(sorted(follow, key=lambda x: x["id"]), 1):
            hits = idx.get(o["id"], [])
            if not hits:
                print(f"| {i} | `{o['id']}` | §{top_of(o)} | §{o['section_no']} | **無** | — | — | — | — |")
            for h in hits:
                print(f"| {i} | `{o['id']}` | §{top_of(o)} | §{o['section_no']} | **有** | "
                      f"{h[COL_ID]} | {h[COL_CAT]} | {h[COL_SUB]} | {h[COL_SWHW]} |")
        return 0

    if a.reverse:
        # §4 反向查核：以 SYS2 之 333 列為起點，逐列歸入互斥桶（不以 87 為起點）
        by_id = {o["id"]: o for o in objs}
        fs = {o["id"] for o in follow}
        rs = {o["id"] for o in ruled}
        ff = {o["id"] for o in fit}
        buckets: dict[str, list[tuple[dict, dict | None]]] = defaultdict(list)
        for r in rows:
            if not r["_src_ids"]:
                buckets["⑥ 來源欄空白（無 7 位 ID）"].append((r, None))
                continue
            for sid in r["_src_ids"]:
                o = by_id.get(sid)
                if o is None:
                    buckets["⑤ 來源 ID 不在 CFTS020 之 2180 物件內"].append((r, None))
                elif sid in fs:
                    buckets["① 來源在 87 之內"].append((r, o))
                elif sid in rs:
                    buckets["② 來源在 29 之內（§1.18，R-ICS39）"].append((r, o))
                elif sid in ff:
                    buckets["③ 來源在 138 之內（變體合 DUT）"].append((r, o))
                else:
                    buckets[f"④ 來源在 CFTS020 內但軸層判不適用"
                            f"（variant={o['variant']}）"].append((r, o))
        for k in sorted(buckets):
            v = buckets[k]
            print(f"\n== {k}：SYS2 列數 {len(v)}")
            print("   Category:", dict(Counter(str(r[COL_CAT]) for r, _ in v)))
            if v and v[0][1] is not None:
                print("   來源之頂層節:",
                      dict(Counter(top_of(o) for _, o in v if o)))
            fr = [(r, o) for r, o in v
                  if str(r[COL_CAT]).strip().lower() == "functional requirement"]
            print(f"   Functional Requirement 列數 {len(fr)}")
            for r, o in fr[:40]:
                print(f"     {r[COL_ID]}  src={','.join(r['_src_ids']) or '（空白）'}  "
                      f"§{o['section_no'] if o else '—'}  "
                      f"{str(r[COL_DESC])[:70]}")

        # Associated 分支之整體覆蓋（§4-2）
        assoc = [o for o in objs if o["variant"] == "Associated"]
        hit = [o for o in assoc if idx.get(o["id"])]
        print(f"\n== Associated 分支（§1.5／1.6／1.7／1.14／1.16／1.17／1.18）")
        print(f"   物件總數 {len(assoc)}；SYS2 有對應列者 {len(hit)}")
        print("   有對應者之頂層節:", dict(Counter(top_of(o) for o in hit)))
        print("   其中軸層不適用而 SYS2 仍有列者:",
              sum(1 for o in hit if o["verdict"] != "適用"))
        return 0

    group_report("87 個（範圍隨變體層）", follow, idx)
    group_report("29 個（§1.18，R-ICS39 裁定算數）", ruled, idx)
    group_report("138 個（變體合 DUT，對照）", fit, idx)

    print("\n-- 87 個依頂層節分組（實數）--")
    g = Counter(top_of(o) for o in follow)
    for k in sorted(g, key=lambda s: [int(x) for x in s.split(".")] if s[0].isdigit() else [999]):
        sub = [o for o in follow if top_of(o) == k]
        hit = [o for o in sub if idx.get(o["id"])]
        frobj = {o["id"] for o in sub for r in idx.get(o["id"], [])
                 if str(r[COL_CAT]).strip().lower() == "functional requirement"}
        print(f"  §{k}: 物件 {len(sub)}，SYS2 有對應 {len(hit)}，其中對到 FR 列者 {len(frobj)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
