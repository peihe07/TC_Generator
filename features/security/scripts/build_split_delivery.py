#!/usr/bin/env python3
"""交付形制六本（SEC-15 §2；R-SEC25）—— 一本 037 一本 workbook，本內依 SWE1 ID 升冪。

輸入為 v08 之 124 個 TC JSON（`sandbox/batch{1,2,3}/*.json`）；**TC 內容零變更**，
只改 (1) 列序、(2) TC ID（依新序重編）、(3) Remarks 內對他 TC ID 之引用（依對照表改寫）。
產出：六本交付 workbook ＋ `merged/security_v09_all.xlsx` ＋ `data/id_map_v08_v09.tsv`
＋ 共用五件之 v09 版（加 `workbook` 欄、TC ID 改新號）。
"""
from __future__ import annotations

import csv
import importlib.util
import os
import json
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from backend.xlsx_surgical import surgical_save          # noqa: E402

_s = importlib.util.spec_from_file_location("g1", Path(__file__).parent / "gen_batch1.py")
g1 = importlib.util.module_from_spec(_s)
_s.loader.exec_module(g1)

DATA = ROOT / "features" / "security" / "data"
SB = ROOT / "features" / "security" / "sandbox"
DELIVERY = SB / "delivery"
DATE = "20260917"
NAME_FMT = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification "
            "& Result_SWQT_Security_{comp}_{date}.xlsx")
C12_FMT = ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification "
           "& Result_SWQT_Security_{comp}")
# R-SEC25(a)(d)：037 本序 ＋ 檔名 token（＝ `trace_matrix.tsv` 之 `component`）
BOOK_ORDER = ["CertProvider", "KeyInstall", "SAM", "ECUCert", "SwdlSecureLib", "libLogEncrypt"]
# 封面填值（同 SEC-06 之量測；`C12` 依 R-SEC25(d) 逐本）
FILL = [("Cover 封面", "D6", "A"), ("Cover 封面", "G7", "2026-09-17"),
        ("Cover 封面", "D9", "PeiPYHsu"), ("Cover 封面", "G9", "2026-09-17"),
        ("Product Document 記錄封面頁", "B3", "NR1L"),
        ("Product Document 記錄封面頁", "B5", "V1.0"),
        ("Product Document 記錄封面頁", "B6", "SW Testing"),
        ("Product Document 記錄封面頁", "B7", "Confidential"),
        ("Product Document 記錄封面頁", "A13", "1"),
        ("Product Document 記錄封面頁", "B13", "初版發佈"),
        ("Product Document 記錄封面頁", "D13", "2026-09-17")]
RE_TC_REF = re.compile(r"NR1L-(?:CP|KI|SAM|ECUC|SWDL|LOGENC)-\d{3}")


def swe1_seq(swe1: str, tm_row: dict) -> int:
    """R-SEC25(b)：有 SWE1 ID 者取數字尾碼；ECUCert 取 037 `Analysis Report` 列號。"""
    m = re.search(r"(\d+)$", swe1)
    return int(m.group(1)) if m else int(tm_row["excel_row"])


def main() -> int:
    tm = {r["swe1_id"]: r for r in csv.DictReader(
        (DATA / "trace_matrix.tsv").open(encoding="utf-8"), delimiter="\t")}
    tcs = []
    for d in ("batch1", "batch2", "batch3"):
        for f in sorted((SB / d).glob("NR1L-*.json")):
            tcs.append(json.loads(f.read_text(encoding="utf-8")))
    # TC 總數以 `coverage.tsv` 之 tc_count 合計為準（SEC-20 起 134；原硬編 124）
    cov_total = sum(int(r["tc_count"]) for r in csv.DictReader(
        (DATA / "coverage.tsv").open(encoding="utf-8"), delimiter="\t"))
    assert len(tcs) == cov_total, f"JSON {len(tcs)} 筆 vs coverage 合計 {cov_total}"

    # 排序鍵：(037 本序, swe1_seq, 舊 TC 號)  —— 同 SWE1 內之舊號序即 sibling_no 序
    def key(t: dict):
        comp = tm[t["req_id"]]["component"]
        old_no = int(t["tc_id"].rsplit("-", 1)[1])
        return (BOOK_ORDER.index(comp), swe1_seq(t["req_id"], tm[t["req_id"]]), old_no)

    tcs.sort(key=key)
    # 重編號（各組自 001）
    counter: Counter = Counter()
    id_map: dict[str, tuple[str, str]] = {}
    for t in tcs:
        comp = tm[t["req_id"]]["component"]
        group = g1.GROUP[comp]
        counter[group] += 1
        id_map[t["tc_id"]] = (f"NR1L-{g1.ABBR[group]}-{counter[group]:03d}", comp)
    # Remarks 內之 TC ID 引用改寫
    rewritten = 0
    for t in tcs:
        def sub(m):
            nonlocal rewritten
            old = m.group(0)
            if old in id_map:
                rewritten += 1
                return id_map[old][0]
            return old
        t["remarks_new"] = RE_TC_REF.sub(sub, t["remarks"])
        t["tc_id_new"] = id_map[t["tc_id"]][0]
        t["workbook"] = id_map[t["tc_id"]][1]

    # ---- 六本 ＋ _all ----
    DELIVERY.mkdir(parents=True, exist_ok=True)
    (DELIVERY / "superseded").mkdir(exist_ok=True)
    reports: dict[str, dict] = {}
    shas: dict[str, str] = {}

    def write_book(rows: list[dict], out: Path, comp: str | None) -> dict:
        wb = openpyxl.load_workbook(g1.TEMPLATE)
        ws = wb[g1.SHEET]
        for n, t in enumerate(rows):
            row = g1.FIRST_ROW + n
            for k, col in g1.COLS.items():
                val = (t["tc_id_new"] if k == "tc_id"
                       else t["remarks_new"] if k == "remarks" else t[k])
                ws[f"{col}{row}"] = val
            for col, name in zip(g1.VM_COLS, g1.VM_NAMES):
                ws[f"{col}{row}"] = t["vehicle_model"][name]
        if comp:                                    # 交付本：封面填值
            for sheet, cell, value in FILL:
                wb[sheet][cell] = value
            wb["Cover 封面"]["C12"] = C12_FMT.format(comp=comp)
        return surgical_save(wb, g1.TEMPLATE, out)

    for comp in BOOK_ORDER:
        rows = [t for t in tcs if t["workbook"] == comp]
        out = DELIVERY / NAME_FMT.format(comp=comp, date=DATE)
        reports[comp] = write_book(rows, out, comp)
        shas[comp] = _sha16(out)
        print(f"  {comp:14s} {len(rows):3d} TC → {out.name}")
    all_out = SB / "merged" / f'security_{os.environ.get("SEC_VER", "v09")}_all.xlsx'
    reports["_all"] = write_book(tcs, all_out, None)
    shas["_all"] = _sha16(all_out)
    print(f"  {'_all':14s} {len(tcs):3d} TC → {all_out.relative_to(ROOT)}")

    # ---- id_map ----
    map_name = os.environ.get("ID_MAP", "id_map_v08_v09.tsv")
    with (DATA / map_name).open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["old_id", "new_id", "swe1_id", "workbook"])
        for t in sorted(tcs, key=lambda x: x["tc_id"]):
            w.writerow([t["tc_id"], t["tc_id_new"], t["req_id"], t["workbook"]])

    # ---- 共用件之 v09 版（加 workbook 欄、TC ID 改新號）----
    wb_of = {t["req_id"]: t["workbook"] for t in tcs}
    new_of = {t["tc_id"]: t["tc_id_new"] for t in tcs}
    cov = list(csv.DictReader((DATA / "coverage.tsv").open(encoding="utf-8"), delimiter="\t"))
    with (DATA / "coverage_v09.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "workbook", "disposition", "ccvr_batch", "tc_count", "tc_ids"])
        for r in cov:
            ids = [new_of[i] for i in r["tc_ids"].split(";") if i]
            w.writerow([r["swe1_id"], wb_of.get(r["swe1_id"], tm[r["swe1_id"]]["component"]),
                        r["disposition"], r["ccvr_batch"], r["tc_count"],
                        ";".join(sorted(ids))])
    ph = list(csv.DictReader((DATA / "placeholder_summary.tsv").open(encoding="utf-8"),
                             delimiter="\t"))
    with (DATA / "placeholder_summary_v09.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["workbook", "tc_id", "field", "line", "x_token", "original_pending",
                    "placeholder", "kind", "converted_to"])
        for r in ph:
            w.writerow([id_map[r["tc_id"]][1], new_of[r["tc_id"]], r["field"], r["line"],
                        r["x_token"], r["original_pending"], r["placeholder"], r["kind"],
                        r["converted_to"]])
    by_tok = defaultdict(list)
    for r in ph:
        by_tok[r["x_token"]].append(r)
    with (DATA / "placeholder_by_token_v09.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["token", "count", "workbooks", "tc_ids", "fields"])
        for k in sorted(by_tok):
            rs = by_tok[k]
            books = sorted({id_map[r["tc_id"]][1] for r in rs})
            ids = sorted({f'{id_map[r["tc_id"]][1]}/{new_of[r["tc_id"]]}' for r in rs})
            flds = Counter(r["field"] for r in rs)
            w.writerow([k, len(rs), ";".join(books), ";".join(ids),
                        " ".join(f"{a}={b}" for a, b in sorted(flds.items()))])
    for name in ("coverage_v09.tsv", "placeholder_summary_v09.tsv",
                 "placeholder_by_token_v09.tsv"):
        shutil.copy(DATA / name, DELIVERY / name.replace("_v09", ""))
    # 舊單本移入 superseded/
    old = DELIVERY / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
                      "Specification & Result_SWQT_Security_20260917.xlsx")
    if old.exists():
        shutil.move(str(old), str(DELIVERY / "superseded" / old.name))
        print(f"  單本移入 superseded/：{old.name}")

    print(f"  Remarks 內 TC ID 引用改寫 {rewritten} 處；id_map {len(id_map)} 列")
    print("  逐組:", dict(Counter(t["workbook"] for t in tcs)))
    for k, v in shas.items():
        print(f"  sha {k:14s} {v}")
    return 0


def _sha16(p: Path) -> str:
    import hashlib
    return hashlib.sha256(p.read_bytes()).hexdigest()[:16]


if __name__ == "__main__":
    sys.exit(main())
