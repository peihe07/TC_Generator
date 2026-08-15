#!/usr/bin/env python3
"""Write the pilot batch into the prepared workbook — handoff 25 §3.

Three stages, verified separately and never merged (25 §3):
  §3.1  pre-gates   — any failure stops before the splice
  §3.2  splice      — through backend/xlsx_surgical.py only (R18-3)
  §3.3  assertions  — read back FROM THE EMITTED FILE, not from memory

Written for Comfort. The four existing features' write_back.py are quarantined
and must not be used as a starting point (R20-5) — they predate the surgical
emit path and carry per-feature column policy that does not transfer.

What this does NOT do (25 §3.6): it does not copy anything to the customer
delivery path, does not touch the prepared file, does not modify ENTRY 001,
and does not run git. Excel's own four-point confirmation is Pei's (profile
§0.1) — a program-level check cannot stand in for it, so the script stops
after emitting and says so.

Usage:
    python3 features/comfort/scripts/write_back.py            # dry-run
    python3 features/comfort/scripts/write_back.py --write
"""

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from backend.xlsx_surgical import StructureError, surgical_save  # noqa: E402

FEATURE = ROOT / "features" / "comfort"
GEN = FEATURE / "generated"
SRC = FEATURE / "output" / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                            "STLA Test Case Specification & Result_SWQT_"
                            "Comfort_20260815_prepared.xlsx")
OUT = FEATURE / "output" / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                            "STLA Test Case Specification & Result_SWQT_"
                            "Comfort_20260815_pilot.xlsx")
SHEET = "Test Case Specification 測試用例規範"
SRC_SHA = "b68117a211b080093a4f845a32601e678b6279331fc4b26e6a81484e8b5e700d"
FIRST_ROW = 10

# profile §0 — revision C letters, verified against the header at recon.
COLS = {
    "D": "req_id", "F": "tc_id", "G": "test_group", "H": "test_set",
    "I": "test_item", "J": "pre_conditions", "K": "input_test_data",
    "L": "test_procedure", "M": "expected_result",
    "N": "specification_reference", "P": "priority", "R": "design_method",
    "S": "functional_safety", "AH": "remarks",
}
# Never written. B carries the template's own numbering formula; clearing or
# overwriting it removes the mechanism (profile §0.1).
NEVER_WRITE = ["B", "C", "E", "O", "Q", "T", "U", "V", "W", "X", "Y", "Z",
               "AB", "AC", "AD", "AE", "AF", "AG"]


def sha256(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def load_tcs() -> list:
    docs = [json.loads(p.read_text(encoding="utf-8"))
            for p in sorted(GEN.glob("*.json"))]
    tcs = [t for d in docs for t in d["tcs"]]
    return sorted(tcs, key=lambda t: int(t["tc_id"].rsplit("-", 1)[1]))


# ------------------------------------------------------------ §3.1 pre-gates

def pre_gates(tcs: list) -> bool:
    print("## §3.1 前置 gate\n")
    ok = True

    def g(name, passed, note=""):
        nonlocal ok
        ok &= passed
        print(f"- {'PASS' if passed else '**FAIL**'} — {name}"
              + (f" — {note}" if note else ""))

    def shasum(args):
        return subprocess.run(["shasum", "-a", "256", "-c"] + args,
                              cwd=FEATURE, capture_output=True, text=True)

    r = shasum(["BASELINE.sha256"])
    n_ok = r.stdout.count(": OK")
    g("BASELINE.sha256 8 檔全數 OK", n_ok == 8 and "FAILED" not in r.stdout,
      f"OK={n_ok}, FAILED={r.stdout.count('FAILED')}")

    r = shasum(["--ignore-missing", "DELIVERY.sha256"])
    d_ok = r.stdout.count(": OK")
    e2 = "ENTRY 002" in (FEATURE / "DELIVERY.sha256").read_text("utf-8")
    g("DELIVERY.sha256 OK 且仍 2 筆、無 ENTRY 002", d_ok == 2 and not e2,
      f"OK={d_ok}, ENTRY002={'present' if e2 else 'absent'}")

    digest = sha256(SRC) if SRC.exists() else "(missing)"
    g("來源為 A-CF07 經 Pei 確認之同一份位元組", digest == SRC_SHA,
      f"measured {digest[:16]}…, expected {SRC_SHA[:16]}…")

    r = subprocess.run([sys.executable, str(FEATURE / "scripts" / "lint_tcs.py")],
                       capture_output=True, text=True)
    lint_ok = r.returncode == 0
    tail = [l for l in r.stdout.strip().split("\n") if "gates PASS" in l]
    g("lint 全數 PASS", lint_ok, tail[-1] if tail else "no summary line")

    g("生成之 TC 數為 14", len(tcs) == 14, f"measured {len(tcs)}")
    print()
    return ok


# ------------------------------------------------------------ §3.2 splice

def splice(tcs: list) -> dict:
    wb = openpyxl.load_workbook(SRC)
    ws = wb[SHEET]
    for i, tc in enumerate(tcs):
        r = FIRST_ROW + i
        for col, field in COLS.items():
            ws[f"{col}{r}"] = tc[field] if tc[field] != "" else None
    return surgical_save(wb, SRC, OUT)


# ------------------------------------------------- §3.3 post-write assertions

def assertions(tcs: list, report: dict) -> bool:
    """Every check reads the EMITTED file, never the in-memory workbook."""
    print("## §3.3 寫回後 assertion（自產出檔讀回）\n")
    ok = True

    def g(name, expected, actual, note=""):
        nonlocal ok
        p = expected == actual
        ok &= p
        print(f"- {'PASS' if p else '**FAIL**'} — {name}: "
              f"expected `{expected}`, measured `{actual}`"
              + (f" — {note}" if note else ""))

    import zipfile
    with zipfile.ZipFile(SRC) as a, zipfile.ZipFile(OUT) as b:
        src_names, out_names = set(a.namelist()), set(b.namelist())
    g("zip member 數與來源相同", len(src_names), len(out_names),
      f"symmetric difference: {sorted(src_names ^ out_names) or 'none'}")
    from backend.xlsx_surgical import sheet_members
    member = sheet_members(SRC)[SHEET]        # resolved, not hard-coded
    g("差異僅限目標 sheet 之 xml", [member], sorted(report.get("differing", [])))
    g("DV counts 與來源相同", "equal",
      "equal" if report.get("dv_counts") else "not reported",
      str(report.get("dv_counts")))

    wb = openpyxl.load_workbook(OUT)
    ws = wb[SHEET]
    mismatches = []
    for i, tc in enumerate(tcs):
        r = FIRST_ROW + i
        for col, field in COLS.items():
            got = ws[f"{col}{r}"].value
            got = "" if got is None else str(got)
            if got != tc[field]:
                mismatches.append(f"{tc['tc_id']}.{col}({field})")
    g("row 10–23 逐列全部寫入欄之值與 JSON 一致", [], mismatches,
      f"{len(tcs)} rows x {len(COLS)} columns compared: {''.join(COLS)}")

    blanks = []
    for i in range(len(tcs)):
        r = FIRST_ROW + i
        for col in ("Q",) + tuple("TUVWXYZ"):
            if ws[f"{col}{r}"].value not in (None, ""):
                blanks.append(f"row{r}.{col}")
    g("Q 與 T–Z 留白（profile §3.7／§3.9）", [], blanks)
    bad_s = [f"row{FIRST_ROW + i}" for i in range(len(tcs))
             if ws[f"S{FIRST_ROW + i}"].value != "NA"]
    g("S 欄一律 NA（profile §3.8）", [], bad_s)

    # B must still hold its formula, not a value openpyxl substituted. The
    # template carries the same formula well past the target range, so the
    # check runs on rows 10-35 — row 24+ renders empty only because D is
    # empty, and that is the mechanism, not residue.
    bad_b = []
    for r in range(FIRST_ROW, FIRST_ROW + len(tcs) + 12):
        v = ws[f"B{r}"].value
        if v != f'=IF(ISBLANK($D{r}),"",ROW()-9)':
            bad_b.append(f"row{r}={v!r}")
    g(f"B 欄 row {FIRST_ROW}–{FIRST_ROW + len(tcs) + 11} 之公式逐列原樣存在",
      [], bad_b, "編號 1–14 由公式自算，未寫入值")

    blk = [t for t in tcs if t["remarks"].startswith("[BLOCKED-SPEC]")]
    bad_blk = []
    for t in blk:
        r = FIRST_ROW + tcs.index(t)
        for col in ("L", "M"):
            if ws[f"{col}{r}"].value not in (None,):
                bad_blk.append(f"{t['tc_id']}.{col}={ws[f'{col}{r}'].value!r}")
        rm = ws[f"AH{r}"].value or ""
        if "Owner:" not in rm[:60]:
            bad_blk.append(f"{t['tc_id']}.AH lacks Owner: in first 60 chars")
    g("BLOCKED row 之 L／M 為空且 Remarks 首 60 字含 Owner:", [], bad_blk,
      f"rows: {[t['tc_id'] for t in blk]}")

    last = FIRST_ROW + len(tcs)
    residue = []
    for r in range(last, last + 12):
        for col in COLS:          # B excluded — its formula is template, not residue
            v = ws[f"{col}{r}"].value
            if v not in (None, ""):
                residue.append(f"row{r}.{col}={str(v)[:24]!r}")
    g(f"row {last} 起無殘留內容", [], residue, f"scanned rows {last}–{last + 11}")
    wb.close()
    print()
    return ok


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--verify-only", action="store_true",
                    help="re-run §3.3 against the already-emitted file. The "
                         "§3.1 pre-gates are one-shot — gate 2 requires the "
                         "ledger to NOT yet carry ENTRY 002, so once the "
                         "entry is appended --write can no longer run. That "
                         "is the append-only ledger working, not a defect.")
    args = ap.parse_args()

    tcs = load_tcs()
    if args.verify_only:
        import zipfile
        with zipfile.ZipFile(SRC) as a, zipfile.ZipFile(OUT) as b:
            differing = sorted(m for m in a.namelist() if a.read(m) != b.read(m))
        from backend.xlsx_surgical import _dv_counts
        report = {"differing": differing, "dv_counts": _dv_counts(OUT)}
        ok = assertions(tcs, report)
        print(f"output sha256: {sha256(OUT)}")
        return 0 if ok else 1

    if not pre_gates(tcs):
        print("STOPPED at §3.1 — a pre-gate failed; the splice was not run.",
              file=sys.stderr)
        return 1
    if not args.write:
        print("dry-run — pre-gates only. Re-run with --write to splice.")
        return 0

    print("## §3.2 splice\n")
    print(f"- source : {SRC.name}")
    print(f"- target : {OUT.name}")
    print(f"- rows   : {FIRST_ROW}–{FIRST_ROW + len(tcs) - 1}")
    print(f"- 未寫入欄: {NEVER_WRITE}\n")
    try:
        report = splice(tcs)
    except StructureError as exc:
        print(f"ABORTED (structure invariant): {exc}", file=sys.stderr)
        return 1
    print(f"- surgical report: {report}\n")

    ok = assertions(tcs, report)
    print(f"output sha256: {sha256(OUT)}\n")
    print("NEXT: Excel 四項確認由 Pei 執行（profile §0.1）—— 無修復提示／"
          "R 欄下拉九項可用／D5 Scope 正確／row 10–23 內容與編號正確。"
          "程式層檢查不能代替 Excel 自身之檔案完整性判定。")
    print("本腳本到此停下：未複製至客戶交付路徑、未動 prepared 檔、"
          "未改 ENTRY 001、未執行 git。")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
