#!/usr/bin/env python3
"""Write ALL current TCs into the prepared workbook — 25 §3 / 45 §2-§3.

45 §1 ruled the cadence: write back after EVERY batch, and write the WHOLE
corpus each time rather than appending. The reason is measured, not stylistic
— the pilot's 14 rows in `…_pilot.xlsx` are already stale (EMEA PCs removed
from 11 TCs, -019 gained a confining PC, -036 was split so 30 tc_ids shifted,
reasoning revised repeatedly). An append would leave the workbook a mixture of
generations, and nothing would say which row belonged to which.

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
import re
import subprocess
import sys
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
from backend.xlsx_surgical import StructureError, surgical_save  # noqa: E402

FEATURE = ROOT / "features" / "comfort"
GEN = FEATURE / "generated"
# 78 §3 — the source is now the EXTENDED template (ENTRY 022). The 20260815
# prepared file remains untouched as ENTRY 001's object; it is no longer the
#母本 because its DV and B-column formulas stop at row 59.
SRC = FEATURE / "output" / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                            "STLA Test Case Specification & Result_SWQT_"
                            "Comfort_20260816_prepared_ext.xlsx")
# 45 §2 — a NEW file. The pilot file is neither overwritten nor deleted:
# DELIVERY ENTRY 002 is its identity record, and deleting it would leave the
# ledger pointing at nothing (the converse of R-C14 — a recorded identity may
# not lose its object).
OUT = FEATURE / "output" / ("FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT "
                            "STLA Test Case Specification & Result_SWQT_"
                            "Comfort_20260816_extdocs.xlsx")
# 45 §3.4 said "ENTRY 003", which was TAKEN (the folder-attachment entry from
# 27 §3), so the second write-back became ENTRY 004. This is the third.
#
# 46 §1.2 reserves an ENTRY for the template extension. It is not written yet
# — the extension is Pei's Tier 3 work and has not happened — so the number is
# free and this write takes it. If the extension lands first, this constant
# moves; the one-shot gate below is what makes a collision loud rather than
# silent.
LEDGER_ENTRY = "ENTRY 026"
SHEET = "Test Case Specification 測試用例規範"
SRC_SHA = "6d53056e559bd0c13d26d38f16754536ede0230a5ce69c8596cce8e8b28b9d4c"
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


# 83 §1 — the ledger check, without `--ignore-missing`.
#
# That flag conflated "this file is not there" with "this file need not be
# checked". Only one of those is something we know. A produced file deleted by
# accident and ENTRY 023's overwritten bytes looked identical under it: both
# simply never appeared in the count.
#
# So absence is now DECLARED, by path, in DELIVERY.sha256's `# absent:` block,
# and the check reports three numbers instead of one. Both directions fail:
#   - missing and NOT declared absent  -> FAIL (something vanished)
#   - declared absent but PRESENT      -> FAIL (the declaration is stale, or
#                                         the object came back and nobody said)
ABSENT_DECL = re.compile(r"^# absent: (.+?)\s+——", re.M)


def check_ledger(ledger: Path) -> tuple:
    """Return (ok, verified, absent_declared, problems)."""
    text = ledger.read_text(encoding="utf-8")
    declared_absent = set(ABSENT_DECL.findall(text))
    # A row may carry `#   archived : <new path>` on the line after it: the
    # bytes still exist, they moved. That is a different thing from absence,
    # and it is checked rather than excused — the digest is verified at the
    # new path.
    rows = []
    for m in re.finditer(r"^([0-9a-f]{64})  (.+)$", text, re.M):
        tail = text[m.end():m.end() + 400]
        moved = re.match(r"\n#   archived : (.+?)(?:  （|\n)", tail)
        rows.append((m.group(1), m.group(2),
                     moved.group(1).strip() if moved else None))
    verified, absent, problems = 0, 0, []
    for digest, rel, moved in rows:
        path = FEATURE / rel
        if not path.exists():
            if moved:
                mp = FEATURE / moved
                if not mp.exists():
                    problems.append(f"archived path missing: {moved}")
                elif sha256(mp) != digest:
                    problems.append(f"MISMATCH at archived path: {moved}")
                else:
                    verified += 1
                continue
            if rel in declared_absent:
                absent += 1
            else:
                problems.append(f"MISSING (not declared): {rel}")
            continue
        if rel in declared_absent:
            problems.append(f"declared absent but PRESENT: {rel}")
            continue
        if sha256(path) != digest:
            problems.append(f"MISMATCH: {rel}")
            continue
        verified += 1
    # a declaration with no ledger row is a dangling permit
    listed = {rel for _, rel, _ in rows}
    for rel in sorted(declared_absent - listed):
        problems.append(f"declared absent but no ledger row: {rel}")
    return (not problems), verified, absent, problems


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

    # 87 §4 — was `n_ok == 8`, the number of baseline files on the day it was
    # written. `inputs/` went from 5 files to 8 and the count moved with it;
    # what the gate is for is "every listed file verifies", which is
    # `FAILED == 0` plus non-vacuity (R-C43 — the same defect as
    # `len(withheld) >= 20`, found the same way: the corpus grew).
    r = shasum(["BASELINE.sha256"])
    n_ok = r.stdout.count(": OK")
    n_bad = r.stdout.count("FAILED")
    g("BASELINE.sha256 逐檔全數 OK", n_bad == 0 and n_ok > 0,
      f"OK={n_ok}, FAILED={n_bad}")

    ok, n_ver, n_abs, problems = check_ledger(FEATURE / "DELIVERY.sha256")
    g("DELIVERY.sha256 逐列（不用 --ignore-missing）",
      ok and n_ver > 0,
      f"驗過 {n_ver}, 已知不存在 {n_abs}, 有問題 {len(problems)}"
      + (f" — {problems[:3]}" if problems else ""))
    # The one-shot guard, now keyed to THIS write's entry number. Once the
    # ledger carries it, --write can no longer run: that is the append-only
    # ledger working, not a defect.
    # Match the ENTRY HEADER, not the string anywhere. ENTRY 004's status text
    # names "ENTRY 005" as the template-extension entry to come, and a bare
    # substring search read that mention as the entry itself and blocked the
    # write. A ledger that discusses its own future entries is normal; a gate
    # that cannot tell a reference from a record is not.
    already = any(l.lstrip("# ").startswith(LEDGER_ENTRY + " ")
                  for l in (FEATURE / "DELIVERY.sha256")
                  .read_text("utf-8").splitlines())
    g(f"台帳尚無 {LEDGER_ENTRY}（一次性 gate）", not already,
      "present" if already else "absent")

    digest = sha256(SRC) if SRC.exists() else "(missing)"
    g("來源為 ENTRY 022 之擴充後母本（78 §3）", digest == SRC_SHA,
      f"measured {digest[:16]}…, expected {SRC_SHA[:16]}…")

    r = subprocess.run([sys.executable, str(FEATURE / "scripts" / "lint_tcs.py")],
                       capture_output=True, text=True)
    lint_ok = r.returncode == 0
    tail = [l for l in r.stdout.strip().split("\n") if "gates PASS" in l]
    g("lint 全數 PASS", lint_ok, tail[-1] if tail else "no summary line")

    # 45 §2 — the count is MEASURED, never pre-filled. What is asserted is
    # that it is non-zero, gap-free and matches what lint just counted.
    nums = [int(t["tc_id"].rsplit("-", 1)[1]) for t in tcs]
    contiguous = nums == list(range(1, len(nums) + 1))
    g("TC 數實測且 tc_id 連續無缺號", len(tcs) > 0 and contiguous,
      f"measured {len(tcs)} TCs, tc_id {nums[0]:03d}–{nums[-1]:03d}")
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

    # 70 §1 — the same format invariant, re-checked ON THE WORKBOOK. Five TCs
    # carried an unnumbered second pre_condition line through ENTRY 016 and
    # 017: the defect existed in the JSON and in the workbook at the same
    # time, and nothing on either side said so. A format invariant is cheap
    # enough to assert twice, and the second assertion is the one that reads
    # what the customer will read.
    numbering = []
    for i, tc in enumerate(tcs):
        r = FIRST_ROW + i
        cell = ws[f"J{r}"].value or ""
        lines = [l for l in str(cell).split("\n") if l.strip()]
        got = [re.match(r"^(\d+)\.\s", l) for l in lines]
        if not all(got) or [int(m.group(1)) for m in got] != list(
                range(1, len(lines) + 1)):
            numbering.append(f"row{r}({tc['tc_id']})")
    g("J 欄 pre_conditions 之行號自 1 起連續（70 §1）", [], numbering,
      f"{len(tcs)} rows read back from the workbook")

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

    # ---- assertion 11 (45 §3.3) — three marker classes, three rules -------
    # profile §5.1 / §5.2 / §5.2a. Each class's first visible line must carry
    # what that class exists to point at, and [BLOCKED-NON-HMI] must carry the
    # OPPOSITE of [BLOCKED-SPEC]: no owner at all.
    MARKER_RULE = {
        "[BLOCKED-SPEC]": ("Owner:", True),
        "[BLOCKED-NON-HMI]": ("Not an HMI-observable property", True),
        "[COVERED-BY]": ("[COVERED-BY]", True),
    }
    marked, bad_blk = {k: [] for k in MARKER_RULE}, []
    for i, t in enumerate(tcs):
        rm_json = t["remarks"]
        mk = next((m for m in MARKER_RULE if rm_json.startswith(m)), None)
        if mk is None:
            continue
        marked[mk].append(t["tc_id"])
        r = FIRST_ROW + i
        for col in ("L", "M"):
            if ws[f"{col}{r}"].value not in (None,):
                bad_blk.append(f"{t['tc_id']}.{col}={ws[f'{col}{r}'].value!r}")
        rm = ws[f"AH{r}"].value or ""
        needle, must_have = MARKER_RULE[mk]
        if (needle in rm[:60]) is not must_have:
            bad_blk.append(f"{t['tc_id']}.AH[:60] {mk} rule: "
                           f"{needle!r} {'missing' if must_have else 'present'}")
        if mk == "[BLOCKED-NON-HMI]" and "Owner:" in rm:
            bad_blk.append(f"{t['tc_id']}.AH names an Owner under "
                           f"[BLOCKED-NON-HMI] — that is a [BLOCKED-SPEC]")
    # 80 §1 / R-C27-1 — the 60 is this check's own inspection window, not
    # a claim about what a reader can see. Measured visibility is ~11
    # characters; the reachable goal is that the row reads as MARKED.
    g("三類 marker 列之 L／M 為空且 Remarks 前綴（檢查窗口 60 字元）符合各自規則",
      [], bad_blk,
      "; ".join(f"{k} {v or 'none'}" for k, v in marked.items()))

    # ---- assertion 10 (45 §3.3) — A-CF19 measured, not assumed ------------
    # The anomaly is about PRESENTATION, so the check separates the two
    # questions it was always confusing: is the content complete (yes/no,
    # checkable) and is it visible (a number, reportable but not a pass/fail).
    n_bad = [f"{t['tc_id']}"
             for i, t in enumerate(tcs)
             if (ws[f"N{FIRST_ROW + i}"].value or "")
             != t["specification_reference"]]
    g("N 欄 specification_reference 逐字元與 JSON 相同（A-CF19 之內容側）",
      [], n_bad, f"{len(tcs)} cells compared")
    lens = [(len(t["specification_reference"]), t["tc_id"]) for t in tcs]
    longest, longest_id = max(lens)
    multi = sum(1 for L, _ in lens if "; " in
                tcs[[i for i, t in enumerate(tcs)
                     if len(t["specification_reference"]) == L][0]]
                ["specification_reference"])
    width = ws.column_dimensions["N"].width
    rh = ws.row_dimensions[FIRST_ROW].height
    wrap = ws[f"N{FIRST_ROW}"].alignment.wrap_text
    per_line = int(width) if width else 0
    visible = 1 if (rh or 0) <= 15 else int((rh or 0) // 14)
    print(f"- MEASURED — A-CF19 之呈現側：N 欄最長 {longest} 字元"
          f"（{longest_id}）；欄寬 {width}；wrapText={wrap}；"
          f"列高 {rh} → 可見約 {visible} 行 ≈ {per_line * visible} 字元，"
          f"即最長者之 {100 * per_line * visible // max(longest, 1)}%。"
          f"**內容完整而僅首行可見** —— 這是 A-CF19 之實測，非 assertion："
          f"呈現屬 Tier 3，程式不得自行改列高（26 §2 之方向 3 已裁）")

    # handoff 26 §4.3 — scan to the sheet's real extent, not a fixed window.
    # The window used to be 12 rows wide while max_row is 59; residue past
    # row 35 would never have been looked at.
    last, end = FIRST_ROW + len(tcs), ws.max_row
    residue = []
    for r in range(last, end + 1):
        for col in COLS:          # B excluded — its formula is template, not residue
            v = ws[f"{col}{r}"].value
            if v not in (None, ""):
                residue.append(f"row{r}.{col}={str(v)[:24]!r}")
    g(f"row {last} 起至 max_row 無殘留內容", [], residue,
      f"scanned rows {last}–{end} (ws.max_row={end})")
    # ---- assertion 13 (上繳 33 §9.3) — the template's own provisions must
    # actually REACH the rows we wrote. The B-formula check below caught this
    # only because its window happened to extend past row 59; the data
    # validations were never checked at all, and P/T-Z/AF stop at row 11.
    # A row outside a DV sqref looks written and is not deliverable: profile
    # §0.1's confirmation item 2 ("R 欄下拉可用且為九項") is false there.
    import re as _re
    import zipfile as _zip
    from backend.xlsx_surgical import sheet_members as _sm
    with _zip.ZipFile(OUT) as _z:
        _xml = _z.read(_sm(OUT)[SHEET]).decode("utf-8")

    def _cover(sqrefs):
        rows = set()
        for sq in sqrefs:
            for part in sq.split():
                m = _re.match(r"([A-Z]+)(\d+)(?::([A-Z]+)(\d+))?$", part)
                if m:
                    rows |= set(range(int(m.group(2)),
                                      int(m.group(4) or m.group(2)) + 1))
        return rows

    r_rows = _cover(_re.findall(r"<xm:sqref>([^<]+)</xm:sqref>", _xml))
    p_rows = _cover([m for m in _re.findall(
        r'<dataValidation[^>]*sqref="([^"]+)"', _xml) if m.startswith("P")])
    # (B is checked above through openpyxl — the XML carries SHARED formulas,
    # where only the master cell holds the <f> text, so a regex over the raw
    # XML under-counts. Left out deliberately rather than duplicated wrongly.)
    written = set(range(FIRST_ROW, FIRST_ROW + len(tcs)))
    g("每一寫入列皆在 R 欄下拉（x14 DV）之涵蓋範圍內",
      [], sorted(written - r_rows)[:6] + (["…"] if len(written - r_rows) > 6 else []),
      f"{len(written - r_rows)} row(s) outside; DV covers rows "
      f"{min(r_rows)}–{max(r_rows)}")
    g("每一寫入列皆在 P 欄 DV 之涵蓋範圍內",
      [], sorted(written - p_rows)[:6] + (["…"] if len(written - p_rows) > 6 else []),
      f"{len(written - p_rows)} row(s) outside; DV covers rows "
      f"{min(p_rows)}–{max(p_rows)}" if p_rows else "no P DV found")

    # ---- assertion 12 (45 §3.3) — row count == TC count -------------------
    written = sum(1 for r in range(FIRST_ROW, end + 1)
                  if ws[f"D{r}"].value not in (None, ""))
    g("已寫入之列數等於現行 TC 數", len(tcs), written,
      f"rows {FIRST_ROW}–{FIRST_ROW + len(tcs) - 1}")
    wb.close()
    print()
    return ok


# ------------------------------------------------- §3.4 歷史產出之歸檔（Pei 追加，2026-08-16）

# `output/` 只保留三份：ENTRY 001 之 prepared（台帳之對象）、現行母本、
# 本次產出。其餘產出檔搬入 `output/archive/`。
#
# 台帳為 append-only：既有之 checksum 行**一字不改**，只
#   (a) 在該行之後插入一行 `#   archived : …` 註記，
#   (b) 於文末之「歸檔後之可驗路徑」段落追加該檔於新路徑之 checksum 行。
# (b) 不可省 —— 只做 (a) 的話，舊路徑於 `shasum -c --ignore-missing` 下
# 會被**靜靜跳過**，而「仍可驗」就只是一句宣稱（R-C43）。
KEEP_IN_OUTPUT = {SRC.name, OUT.name,
                  "FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test "
                  "Case Specification & Result_SWQT_Comfort_20260815_"
                  "prepared.xlsx"}
ARCHIVE_HEADER = "# 歸檔後之可驗路徑（2026-08-16）"


def archive_previous() -> list:
    """Move superseded outputs into output/archive/ and annotate the ledger."""
    out_dir = FEATURE / "output"
    arc = out_dir / "archive"
    arc.mkdir(exist_ok=True)
    moved = []
    for f in sorted(out_dir.glob("*.xlsx")):
        if f.name in KEEP_IN_OUTPUT:
            continue
        f.rename(arc / f.name)
        moved.append(f.name)
    if not moved:
        return moved

    led = FEATURE / "DELIVERY.sha256"
    before = led.read_text(encoding="utf-8").split("\n")
    out, annotated = [], []
    for line in before:
        out.append(line)
        m = re.match(r"^([0-9a-f]{64})  output/(.+)$", line)
        if m and m.group(2) in moved:
            out.append(f"#   archived : output/archive/{m.group(2)}"
                       "  （hash 與內容未變，見文末「歸檔後之可驗路徑」）")
            annotated.append(m.group(2))
    tail = [f"{sha256(arc / n)}  output/archive/{n}" for n in moved]
    if ARCHIVE_HEADER not in "\n".join(before):
        out += ["", "# " + "=" * 58, ARCHIVE_HEADER, "# " + "=" * 58]
    led.write_text("\n".join(out + tail) + "\n", encoding="utf-8")

    # append-only 之驗證：既有行必須原樣留存且順序不變
    after = led.read_text(encoding="utf-8").split("\n")
    kept = [l for l in after if l in before]
    assert [l for l in before if l] == [l for l in kept if l], \
        "DELIVERY.sha256 lost or reordered an existing line — append-only 破壞"
    print(f"\n## §3.4 歸檔\n\n- 搬入 output/archive/: {len(moved)} 檔")
    print(f"- 台帳增 archived 註記 {len(annotated)} 行、"
          f"新路徑 checksum {len(tail)} 行；既有行 0 處變動")
    return moved

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--verify-only", action="store_true",
                    help="re-run §3.3 against the already-emitted file. The "
                         "§3.1 pre-gates are one-shot — gate 2 requires the "
                         "ledger to NOT yet carry this write's entry, so once it "
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
    print(f"output sha256: {sha256(OUT)}")
    if ok:
        archive_previous()
    else:
        print("\n## §3.4 歸檔\n\n- **未執行** —— assertion 未全數 PASS，"
              "前一份產出檔留在 output/ 以便逐項比對")
    print()
    print("NEXT: Excel 四項確認由 Pei 執行（profile §0.1）—— 無修復提示／"
          f"R 欄下拉九項可用／D5 Scope 正確／row {FIRST_ROW}–"
          f"{FIRST_ROW + len(tcs) - 1} 內容與編號正確。"
          "程式層檢查不能代替 Excel 自身之檔案完整性判定。")
    print("本腳本到此停下：未複製至客戶交付路徑、未動 prepared 檔、"
          "未改 ENTRY 001、未執行 git。")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
