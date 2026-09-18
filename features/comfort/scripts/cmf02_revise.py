#!/usr/bin/env python3
"""CMF-02 §4 —— Comfort HMI Revise 候選本（0907 本之複本，xlsx_surgical 寫入）。

R-C46：母本為 `delivered/…_ComfortHMI_20260907.xlsx` 之複本；既有 466 列之
列位、F（TC ID）、E（TestRail ID）不變；C／E／O／AA 既有格不動；新增 sibling
接於尾端（row 476 起），不插列。

寫入內容：
  既有列 row 10–475   COLS 各欄（F 除外）依 `write_back.render()` 重算，只有
                      與 0907 本不同之格會被寫入（surgical 之 diff）
  row 116             019-03 之 [BLOCKED-SPEC] 列（R-C51），F = -466
  W／X（R-C48）       row 10–475 全列 `0`；T／U／V／Y／Z 既有列不動
  row 476 起          sibling：F＝JSON tc_id、O＝`NEW`、AA＝`PeiPYHsu`、
                      C＝0907 本同 req 既有列之 C、E 留空、T／U／V／Y／Z＝1、W／X＝0

ABORT 級 invariant：zip member 集合相同、DV 之 sqref（classic 與 x14）逐字相同。
寫後以**產出檔**逐格對帳 0907 本（全部工作表）：未列於本包之格須逐格相同，
不符數須為 0，否則 exit 1。

Usage:
    python3 features/comfort/scripts/cmf02_revise.py
"""

import csv
import hashlib
import re
import sys
import zipfile
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent))
import write_back as W                                           # noqa: E402
sys.path.insert(0, str(W.ROOT))
from backend.xlsx_surgical import StructureError, sheet_members, surgical_save  # noqa: E402

FEATURE = W.FEATURE
SRC = FEATURE / "delivered" / (
    "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
    "Specification & Result_SWQT_ComfortHMI_20260907.xlsx")
SRC_SHA = "3550d16d8bd319633d872856ae51ba63a7d2a928d22fab69bff6dd1963736aff"
OUT_DIR = FEATURE / "sandbox" / "revise_0918"
OUT = OUT_DIR / (
    "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case "
    "Specification & Result_SWQT_ComfortHMI_20260918.xlsx")
RECON_TSV = FEATURE / "docs" / "reports" / "cmf02_candidate_cell_recon.tsv"
CHANGE_LOG = FEATURE / "docs" / "reports" / "cmf02_json_change_log.tsv"

FIRST, LAST_EXISTING = 10, 475          # 0907 本之資料列（466 列）
ROW_019_03 = 116
NEW_ROW_FIRST = 476
AUTHOR, TC_REF = "PeiPYHsu", "NEW"
ZERO_COLS, ONE_COLS = ("W", "X"), ("T", "U", "V", "Y", "Z")
# JSON 欄 → 其改動之包內出處（change log 之 item）；N 欄另由 R-C49 整欄承擔
FIELD_OF_COL = {c: f for c, f in W.COLS.items() if c != "F"}


def sha256(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def norm(v):
    return "" if v is None else v


def dv_sqrefs(path: Path) -> list:
    with zipfile.ZipFile(path) as z:
        xml = z.read(sheet_members(path)[W.SHEET]).decode("utf-8")
    return (re.findall(r'<dataValidation[^>]*sqref="([^"]+)"', xml)
            + re.findall(r"<xm:sqref>([^<]+)</xm:sqref>", xml))


def main() -> int:
    if sha256(SRC) != SRC_SHA:
        raise SystemExit("母本 sha256 不符 ENTRY 036 —— 停")
    tcs = W.load_tcs()
    existing = [t for t in tcs if int(t["tc_id"][-3:]) <= 466]
    new_tcs = [t for t in tcs if int(t["tc_id"][-3:]) > 466]
    plan = W.row_plan(existing)                 # 466 列，019-03 已落 row 116
    if len(plan) != LAST_EXISTING - FIRST + 1 or any(p.get(W.BLANK) for p in plan):
        raise SystemExit(f"row plan is not 466 TC rows: {len(plan)}")

    src_wb = openpyxl.load_workbook(SRC)
    src = src_wb[W.SHEET]
    wb = openpyxl.load_workbook(SRC)
    ws = wb[W.SHEET]

    intended = {}                                # (row, col) -> value
    # ---- 既有 466 列 --------------------------------------------------------
    c_of_req = {}
    for i, t in enumerate(plan):
        r = FIRST + i
        if src[f"D{r}"].value != t["req_id"]:
            raise SystemExit(f"row {r}: D={src[f'D{r}'].value!r} != {t['req_id']}")
        c_of_req.setdefault(t["req_id"], src[f"C{r}"].value)
        for col, field in FIELD_OF_COL.items():
            v = W.render(field, t[field])
            intended[(r, col)] = v if v != "" else None
        if r == ROW_019_03:
            intended[(r, "F")] = t["tc_id"]      # R-C51：-466（F 此前為空）
        for col in ZERO_COLS:
            intended[(r, col)] = 0
    # ---- 尾端新列 -------------------------------------------------------------
    for j, t in enumerate(sorted(new_tcs, key=lambda x: int(x["tc_id"][-3:]))):
        r = NEW_ROW_FIRST + j
        if src[f"D{r}"].value is not None:
            raise SystemExit(f"row {r} is not empty in the source")
        for col, field in FIELD_OF_COL.items():
            v = W.render(field, t[field])
            intended[(r, col)] = v if v != "" else None
        intended[(r, "F")] = t["tc_id"]
        intended[(r, "C")] = c_of_req[t["req_id"]]
        intended[(r, "O")] = TC_REF
        intended[(r, "AA")] = AUTHOR
        for col in ONE_COLS:
            intended[(r, col)] = 1
        for col in ZERO_COLS:
            intended[(r, col)] = 0
    for (r, col), v in intended.items():
        ws[f"{col}{r}"] = v

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    try:
        report = surgical_save(wb, SRC, OUT)
    except StructureError as exc:
        print(f"ABORTED (structure invariant): {exc}", file=sys.stderr)
        return 1

    ok = True

    def g(name, passed, note=""):
        nonlocal ok
        ok &= passed
        print(f"- {'PASS' if passed else '**FAIL**'} — {name}" + (f" — {note}" if note else ""))

    print("## §4 候選本 —— invariant 與逐格對帳（自產出檔讀回）\n")
    with zipfile.ZipFile(SRC) as a, zipfile.ZipFile(OUT) as b:
        g("zip member 數與母本相同（ABORT 級）", len(a.namelist()) == len(b.namelist()),
          f"{len(a.namelist())} vs {len(b.namelist())}")
    g("差異僅限目標 sheet 之 xml", report["differing"] == [sheet_members(SRC)[W.SHEET]],
      str(report["differing"]))
    s_src, s_out = dv_sqrefs(SRC), dv_sqrefs(OUT)
    g("DV sqref（classic ＋ x14）逐字相同（ABORT 級）", s_src == s_out, f"{s_out}")

    out_wb = openpyxl.load_workbook(OUT)
    out = out_wb[W.SHEET]
    last_row = NEW_ROW_FIRST + len(new_tcs) - 1
    bad_b = [r for r in range(FIRST, 602)
             if out[f"B{r}"].value != f'=IF(ISBLANK($D{r}),"",ROW()-9)']
    g(f"B 欄公式 row {FIRST}–601 逐列原樣（涵蓋新列 {NEW_ROW_FIRST}–{last_row}）", not bad_b,
      str(bad_b[:5]))
    dv_rows = set()
    for sq in s_out:
        for part in sq.split():
            m = re.match(r"[A-Z]+(\d+)(?::[A-Z]+(\d+))?$", part)
            if m:
                dv_rows |= set(range(int(m.group(1)), int(m.group(2) or m.group(1)) + 1))
    g("新列皆在 DV 涵蓋範圍內", all(r in dv_rows for r in range(NEW_ROW_FIRST, last_row + 1)),
      f"rows {NEW_ROW_FIRST}–{last_row}")

    # ---- 逐格對帳：全部工作表 ---------------------------------------------------
    changed_fields = {}
    with CHANGE_LOG.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh, delimiter="\t"):
            changed_fields.setdefault((row["tc_id"], row["field"]), set()).add(row["item"])
    tc_at_row = {FIRST + i: t for i, t in enumerate(plan)}
    tc_at_row.update({NEW_ROW_FIRST + j: t for j, t in enumerate(
        sorted(new_tcs, key=lambda x: int(x["tc_id"][-3:])))})

    def attribution(r, col):
        if r >= NEW_ROW_FIRST:
            return "§3 sibling"
        if r == ROW_019_03:
            return "R-C51"
        if col in ZERO_COLS:
            return "R-C48"
        if col == "N":
            return "R-C49"
        t = tc_at_row[r]
        items = changed_fields.get((t["tc_id"], FIELD_OF_COL.get(col, "")), set())
        return "+".join(sorted(items))

    recon, mismatch, wrong, n_cells = [], [], [], 0
    for name in src_wb.sheetnames:
        a, b = src_wb[name], out_wb[name]
        rows = max(a.max_row, b.max_row)
        cols = max(a.max_column, b.max_column)
        for r in range(1, rows + 1):
            for c in range(1, cols + 1):
                n_cells += 1
                va, vb = a.cell(r, c).value, b.cell(r, c).value
                col = openpyxl.utils.get_column_letter(c)
                key = (r, col) if name == W.SHEET else None
                if key in intended:
                    if norm(vb) != norm(intended[key]):
                        wrong.append(f"{name}!{col}{r}")
                    if norm(va) != norm(vb):
                        item = attribution(r, col)
                        if not item:
                            mismatch.append(f"{name}!{col}{r} (unattributed)")
                        recon.append({"cell": f"{col}{r}", "tc_id": tc_at_row.get(r, {}).get("tc_id", ""),
                                      "item": item or "UNATTRIBUTED",
                                      "before": "" if va is None else str(va),
                                      "after": "" if vb is None else str(vb)})
                elif norm(va) != norm(vb):
                    mismatch.append(f"{name}!{col}{r}")
    g("寫入格讀回 == 意圖值", not wrong, f"{len(wrong)} 格不符 {wrong[:5]}")
    g("**未列於本包之格與 0907 本逐格相同**（全部工作表）", not mismatch,
      f"不符 {len(mismatch)} 格 {mismatch[:5]}；比對 {n_cells} 格")

    by_item = {}
    for x in recon:
        by_item[x["item"]] = by_item.get(x["item"], 0) + 1
    print(f"- MEASURED — 變更格 {len(recon)}：" +
          "、".join(f"{k} {v}" for k, v in sorted(by_item.items())))
    with RECON_TSV.open("w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=["cell", "tc_id", "item", "before", "after"],
                           delimiter="\t")
        w.writeheader()
        w.writerows(recon)
    print(f"- recon table: {RECON_TSV.relative_to(FEATURE)}")
    print(f"\noutput: {OUT.relative_to(FEATURE)}\nsha256: {sha256(OUT)}")
    print(f"MISMATCH_COUNT: {len(mismatch)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
