#!/usr/bin/env python3
"""R-DM13 anchored coverage cross-reference: SYS2 FR rows vs SWE-DM leaves.

Replaces the bag-of-words version retracted by R-DM13 (see
data/coverage_sys2_vs_swe_dm.RETRACTED.tsv). Nothing here uses similarity,
fuzziness or scoring: every anchor is a VERBATIM comparison, and a row with
no verbatim anchor is recorded as having none (handoff 03 §七第 10 條).

Population: SYS2 `Basic Report` rows whose Category normalises to
'functional requirement' (80).

Anchors recorded per row (all of them, in their own columns):
  signals  — `$NAME$` tokens in Description
  values   — `[VALUE]` tokens in Description
  heading  — the nearest preceding Category=='heading' row (positional)
  melco    — Melco ID tokens that appear on 037's Excluded NRLs sheet

`anchor_kind` names the highest-priority anchor PRESENT, in the R-DM13
order: signal > value > heading > melco > none.

`candidate_leaf` is only ever produced by the heading anchor, because it is
the only anchor whose counterpart exists on the 037 side: 037 carries no
signal-layer information (R-DM14), and Melco hits mark 037's HW exclusions,
never a leaf. The test is verbatim substring containment of a leaf phrase in
the heading text, where a leaf phrase is:

    Requirement Title split on ' - ' and ' & ', plus Sub Categorization,
    whitespace-normalised, lower-cased, segments shorter than
    MIN_PHRASE characters dropped

MIN_PHRASE is the one tunable in this file. It does not make the match
fuzzy — a phrase either occurs verbatim or it does not — it only stops
generic fragments from matching. Every produced candidate carries the
matched phrase verbatim in `note`, so any reader can check it by eye.

Per R-DM12 the result column is named candidate_leaf, never 對應/mapping,
and must not be cited without `anchor_kind` alongside it.
"""
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[1]
SYS2 = ROOT / "inputs" / ("SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System"
                          "_Accepted & Released.xlsx")
F037 = ROOT / "inputs" / \
    "Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx"

MIN_PHRASE = 8

SIGNAL = re.compile(r"\$([A-Za-z0-9_]+)\$")
VALUE = re.compile(r"\[([A-Za-z0-9_%\s]+)\]")


def norm(s):
    return " ".join(str(s or "").split())


def leaves():
    wb = openpyxl.load_workbook(F037, data_only=True)
    ws = wb["SWE1 Requirements"]
    hdr = {norm(ws.cell(7, c).value): c for c in range(1, ws.max_column + 1)}
    out = []
    for r in range(8, 16):
        title = norm(ws.cell(r, hdr["Requirement Title"]).value)
        sub = norm(ws.cell(r, hdr["Sub Categorization"]).value)
        phrases = [s.strip() for s in re.split(r" - | & ", title)]
        phrases.append(sub)
        phrases = [p for p in phrases if len(p) >= MIN_PHRASE]
        out.append({"id": norm(ws.cell(r, hdr["SWE-Requirement ID"]).value),
                    "title": title, "sub": sub, "phrases": phrases})
    ex = wb["Excluded NRLs (HW-only)"]
    excluded = {norm(ex.cell(r, 1).value) for r in range(2, 10)}
    wb.close()
    return out, excluded


def sys2_rows():
    wb = openpyxl.load_workbook(SYS2, read_only=True, data_only=True)
    grid = [list(r) for r in wb["Basic Report"].iter_rows(values_only=True)]
    wb.close()
    head = [norm(h) for h in grid[0]]

    def col(name):
        hits = [i for i, h in enumerate(head) if h == name] or \
               [i for i, h in enumerate(head) if h.startswith(name)]
        assert len(hits) == 1, (name, hits)
        return hits[0]

    rows = [(i + 1, r) for i, r in enumerate(grid)
            if i >= 1 and str(r[0] or "").strip() != ""]
    return rows, col


def main():
    lv, excluded = leaves()
    rows, col = sys2_rows()
    c_fid, c_cat, c_desc = (col("SYS2 Sys-RA-Feature-ID"),
                            col("SYS2 分類 Category"), col("Description"))
    c_swhw, c_melco = col("SYS2 SW/HW/System"), col("SYS2 Melco ID")
    c_l1, c_l2, c_l3 = (col("SYS2 功能(一階) Function (Level 1)"),
                        col("SYS2 功能(二階) Function (Level 2)"),
                        col("SYS2 功能(三階) Function (Level 3)"))

    # positional heading ancestor, same rule as sys2_heading_tree.py
    ancestor, cur = {}, None
    for rn, r in rows:
        if norm(r[c_cat]).lower() == "heading":
            cur = (rn, norm(r[c_fid]), norm(r[c_desc]))
        ancestor[rn] = cur

    pop = [(rn, r) for rn, r in rows
           if norm(r[c_cat]).lower() == "functional requirement"]

    print("# R-DM13 anchored coverage cross-reference")
    print(f"population (Category=='functional requirement', case-normalised): "
          f"{len(pop)}")
    print(f"anchors are verbatim only; MIN_PHRASE={MIN_PHRASE} chars")
    print("candidate_leaf is a CANDIDATE (R-DM12): cite it only together "
          "with anchor_kind")
    print()
    print("## 037 leaf phrases used for the heading anchor")
    for lf in lv:
        print(f"  {lf['id']}: {lf['phrases']}")

    out_rows = []
    for rn, r in pop:
        desc = norm(r[c_desc])
        sigs = sorted(set(SIGNAL.findall(desc)))
        vals = sorted({v.strip() for v in VALUE.findall(desc) if v.strip()})
        anc = ancestor[rn]
        anc_txt = anc[2] if anc else ""
        mel = sorted({t.strip() for t in re.split(r"[,\s;]+", norm(r[c_melco]))
                      if t.strip()} & excluded)

        hits = []
        for lf in lv:
            m = [p for p in lf["phrases"] if p.lower() in anc_txt.lower()]
            if m:
                hits.append((lf["id"], m))

        if sigs:
            kind = "signal"
        elif vals:
            kind = "value"
        elif anc_txt:
            kind = "heading"
        elif mel:
            kind = "melco"
        else:
            kind = "none"

        if hits:
            cand = ",".join(h[0] for h in hits)
            note = "heading 錨逐字含 leaf 片語：" + "；".join(
                f"{i}←{'|'.join(repr(x) for x in m)}" for i, m in hits)
        else:
            cand = ""
            note = ("heading 錨無逐字 leaf 片語"
                    if anc_txt else "無 heading 祖先")
        if mel:
            note += f"；Melco 命中 037 Excluded（HW 排除項）{mel}"

        out_rows.append({
            "sys2_row": rn, "sys_ra_id": norm(r[c_fid]),
            "category": norm(r[c_cat]), "swhw": norm(r[c_swhw]),
            "heading_ancestor": f"r{anc[0]} {anc[2]}" if anc else "",
            "signals": ",".join(sigs), "values": ",".join(vals),
            "melco": ",".join(mel), "anchor_kind": kind,
            "candidate_leaf": cand, "note": note,
            "func_l1": norm(r[c_l1]), "func_l2": norm(r[c_l2]),
            "func_l3": norm(r[c_l3]),
        })

    cols = ["sys2_row", "sys_ra_id", "category", "swhw", "heading_ancestor",
            "signals", "values", "melco", "anchor_kind", "candidate_leaf",
            "note", "func_l1", "func_l2", "func_l3"]
    out = ROOT / "data" / "coverage_sys2_vs_swe_dm.tsv"
    with out.open("w", encoding="utf-8") as fh:
        fh.write("\t".join(cols) + "\n")
        for d in out_rows:
            fh.write("\t".join(str(d[c]) for c in cols) + "\n")

    print()
    print("## anchor_kind 分布（最高優先之現存錨）")
    from collections import Counter
    for k, n in Counter(d["anchor_kind"] for d in out_rows).most_common():
        print(f"  {k}: {n}")
    print()
    print("## 各錨之存在數（非互斥，逐列獨立計）")
    print(f"  含 $signal$        : {sum(1 for d in out_rows if d['signals'])}")
    print(f"  含 [value]         : {sum(1 for d in out_rows if d['values'])}")
    print(f"  有 heading 祖先    : "
          f"{sum(1 for d in out_rows if d['heading_ancestor'])}")
    print(f"  Melco 命中 Excluded: {sum(1 for d in out_rows if d['melco'])}")
    sig = sorted({s for d in out_rows for s in d["signals"].split(",") if s})
    val = sorted({v for d in out_rows for v in d["values"].split(",") if v})
    print(f"  相異訊號名 {len(sig)}: {sig}")
    print(f"  相異值 token {len(val)}: {val}")

    print()
    print("## candidate_leaf 分布（候選，非裁定）")
    cnt = Counter()
    for d in out_rows:
        if d["candidate_leaf"]:
            for x in d["candidate_leaf"].split(","):
                cnt[x] += 1
    for lf in lv:
        print(f"  {lf['id']} ({lf['sub']}): {cnt.get(lf['id'], 0)}")
    print(f"  有候選之列: {sum(1 for d in out_rows if d['candidate_leaf'])}")
    print(f"  無候選之列: {sum(1 for d in out_rows if not d['candidate_leaf'])}")

    print()
    print("| sys2_row | sys_ra_id | swhw | heading_ancestor | anchor_kind "
          "| candidate_leaf | note |")
    print("|---|---|---|---|---|---|---|")
    for d in out_rows:
        print(f"| r{d['sys2_row']} | {d['sys_ra_id']} | {d['swhw']} "
              f"| {d['heading_ancestor']} | {d['anchor_kind']} "
              f"| {d['candidate_leaf'] or '（無）'} | {d['note']} |")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
