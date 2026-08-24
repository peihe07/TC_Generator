#!/usr/bin/env python3
"""R-DM7 coverage cross-reference: SYS2 Functional Requirement -> SWE-DM leaf.

Population: every SYS2 `Basic Report` row whose Category normalises to
'functional requirement' (80 rows; case-normalised, so the one
'Functional requirement' variant is included).

For each row this reports WHICH EVIDENCE EXISTS, not a verdict:

  melco  — the row's Melco ID appears in 037. The only Melco IDs 037 carries
           are the 8 on the 'Excluded NRLs (HW-only)' sheet, so a melco hit
           means the row is one 037 explicitly EXCLUDED as HW-only. It links
           the row to 037, never to a SWE-DM leaf.
  id     — the row's Sys-RA-Feature-ID equals a `Sys-RA-Feature-ID(s)` value
           on 037's 'SYS2 Traceability' sheet. Measured, not assumed.
  text   — token overlap between the row's Description and a leaf's
           Title + Sub Categorization + Description.

The text score is a mechanical bag-of-words overlap over content tokens
(lowercased, stopworded, length>=4, de-duplicated). It is a SEARCH AID.
The DISPLAY_CUT below decides only what gets printed in the '對應依據'
column; it is not a ruling on scope, and rows under the cut are printed as
'無' with their best score still shown. Scope is Tier 2 (handoff 01 Q2).
"""
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
SYS2 = ROOT / "inputs" / \
    "SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx"
F037 = ROOT / "inputs" / \
    "Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx"

DISPLAY_CUT = 3          # distinct shared content tokens

STOP = set("""shall must with that this from have been will when then than into
onto over under after before while each such other than these those they them
their there where which whose used using use uses based upon also only both any
all not non the and for are was were its it's per via able about above across
against among around because been being between during either every however
into more most much must need needs same some still such upon very within
without would could should case cases state states value values type types
system systems supplier suppliers requirement requirements artifact approved
market model year years subsystem functional information display
""".split())


def norm(s):
    return " ".join(str(s or "").split())


def toks(s):
    return {t for t in re.split(r"[^a-z0-9]+", norm(s).lower())
            if len(t) >= 4 and t not in STOP}


def main():
    # ---- 037 leaves
    wb = openpyxl.load_workbook(F037, data_only=True)
    ws = wb["SWE1 Requirements"]
    hdr = {" ".join(str(ws.cell(7, c).value or "").split()): c
           for c in range(1, ws.max_column + 1)}
    leaves = []
    for r in range(8, 16):
        leaves.append({
            "id": norm(ws.cell(r, hdr["SWE-Requirement ID"]).value),
            "sub": norm(ws.cell(r, hdr["Sub Categorization"]).value),
            "title": norm(ws.cell(r, hdr["Requirement Title"]).value),
            "toks": toks(" ".join([
                str(ws.cell(r, hdr["Requirement Title"]).value or ""),
                str(ws.cell(r, hdr["Sub Categorization"]).value or ""),
                str(ws.cell(r, hdr["Requirement Description"]).value or ""),
            ])),
        })
    tr = wb["SYS2 Traceability"]
    trace_ids = {norm(tr.cell(r, 3).value) for r in range(2, 10)}
    ex = wb["Excluded NRLs (HW-only)"]
    excluded_melco = {norm(ex.cell(r, 1).value) for r in range(2, 10)}
    wb.close()

    # ---- SYS2 population
    wb2 = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
    grid = [list(r) for r in wb2["Basic Report"].iter_rows(values_only=True)]
    wb2.close()
    head = [norm(h) for h in grid[0]]

    def col(name):
        hits = [i for i, h in enumerate(head) if h == name] or \
               [i for i, h in enumerate(head) if h.startswith(name)]
        assert len(hits) == 1, (name, hits)
        return hits[0]

    c_fid, c_melco, c_desc, c_cat = (col("SYS2 Sys-RA-Feature-ID"),
                                     col("SYS2 Melco ID"), col("Description"),
                                     col("SYS2 分類 Category"))
    c_swhw = col("SYS2 SW/HW/System")

    pop = [(i + 1, r) for i, r in enumerate(grid)
           if i >= 1 and str(r[0] or "").strip() != ""
           and norm(r[c_cat]).lower() == "functional requirement"]

    print("# R-DM7 coverage cross-reference")
    print(f"population = SYS2 Category=='functional requirement' "
          f"(case-normalised): {len(pop)} rows")
    print(f"037 SYS2-Traceability Sys-RA-Feature-ID(s) values: "
          f"{sorted(trace_ids)}")
    print(f"id-basis hits (SYS2 id == one of the above): "
          f"{sum(1 for _, r in pop if norm(r[c_fid]) in trace_ids)}")
    print(f"text scoring: bag-of-words overlap, len>=4, stopworded, "
          f"display cut >= {DISPLAY_CUT} shared tokens")
    print()
    print("| SYS2 列 | Sys-RA-Feature-ID | Melco ID | SW/HW | 對應 SWE-DM | 對應依據 |")
    print("|---|---|---|---|---|---|")

    counts = {"melco": 0, "id": 0, "text": 0, "none": 0}
    rows_out = []
    for rn, r in pop:
        fid, melco = norm(r[c_fid]), norm(r[c_melco])
        d = toks(r[c_desc])
        scored = sorted(((len(d & lf["toks"]), lf) for lf in leaves),
                        key=lambda x: -x[0])
        best, lf = scored[0]
        mtoks = sorted(d & lf["toks"])
        melco_tokens = {t.strip() for t in re.split(r"[,\s;]+", melco) if t.strip()}
        if fid in trace_ids:
            hit, basis, counts_key = lf["id"], "id", "id"
        elif melco_tokens & excluded_melco:
            hit = "無"
            basis = ("Melco：037 Excluded NRLs (HW-only) 列有此 Melco ID "
                     f"（{sorted(melco_tokens & excluded_melco)}）—— 037 明列排除，非 leaf 對應")
            counts_key = "melco"
        elif best >= DISPLAY_CUT:
            hit = lf["id"]
            basis = f"Description 文字：共通 token {best} 個 {mtoks}"
            counts_key = "text"
        else:
            hit = "無"
            basis = (f"無（最佳文字分數 {best}"
                     + (f"，{lf['id']} {mtoks}" if best else "") + "）")
            counts_key = "none"
        counts[counts_key] += 1
        print(f"| r{rn} | {fid} | {melco or '—'} | {norm(r[c_swhw])} | {hit} | {basis} |")
        rows_out.append((rn, fid, melco, norm(r[c_swhw]), hit, basis))

    print()
    print("## 依據別統計")
    for k, v in counts.items():
        print(f"  {k}: {v}")
    print()
    print("## 無對應之列（列號 + Sys-RA-Feature-ID）")
    none_rows = [(rn, fid) for rn, fid, _, _, hit, _ in rows_out if hit == "無"]
    print(f"  count = {len(none_rows)}")
    print("  " + ", ".join(f"r{rn} {fid}" for rn, fid in none_rows))
    print()
    print("## 每個 SWE-DM leaf 被指到之列數（僅文字依據，非裁定）")
    for lf in leaves:
        n = sum(1 for *_x, hit, _b in rows_out if hit == lf["id"])
        print(f"  {lf['id']} ({lf['sub']}): {n}")

    out = ROOT / "data" / "coverage_sys2_vs_swe_dm.tsv"
    with out.open("w", encoding="utf-8") as fh:
        fh.write("sys2_row\tsys2_feature_id\tmelco_id\tsw_hw\tswe_dm\tbasis\n")
        for row in rows_out:
            fh.write("\t".join(str(x) for x in row) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
