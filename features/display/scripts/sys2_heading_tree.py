#!/usr/bin/env python3
"""SYS2 Basic Report section tree (handoff 03 §3.4).

Nodes are the rows whose Category normalises to 'heading' (45 of them).
A node's children are the subsequent non-Heading data rows up to the next
Heading row. No similarity is involved: membership is positional, taken
from the export's own row order.
"""
import re
from pathlib import Path

import openpyxl

from tsv_meta import write_meta

ROOT = Path(__file__).resolve().parents[1]
SYS2 = ROOT / "inputs" / ("SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System"
                          "_Accepted & Released.xlsx")


def norm(s):
    return " ".join(str(s or "").split())


def load():
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


def build():
    rows, col = load()
    c_fid, c_cat, c_desc = (col("SYS2 Sys-RA-Feature-ID"),
                            col("SYS2 分類 Category"), col("Description"))
    nodes, cur = [], None
    orphans = []
    for rn, r in rows:
        cat = norm(r[c_cat]).lower()
        if cat == "heading":
            cur = {"row": rn, "fid": norm(r[c_fid]),
                   "text": norm(r[c_desc]), "children": [], "fr": []}
            nodes.append(cur)
        elif cur is None:
            orphans.append(rn)
        else:
            cur["children"].append(rn)
            if cat == "functional requirement":
                cur["fr"].append(rn)
    return nodes, orphans, rows


def main():
    nodes, orphans, rows = build()
    print("# SYS2 Basic Report — section tree")
    print("node = Category normalises to 'heading'; children = following "
          "non-Heading data rows until the next Heading row (positional, "
          "from the export's own order)")
    print(f"data rows {len(rows)} | heading nodes {len(nodes)} | "
          f"rows before the first heading (orphans) {len(orphans)}"
          + (f" -> {orphans}" if orphans else ""))
    covered = sum(len(n["children"]) for n in nodes) + len(nodes) + len(orphans)
    print(f"accounting: {covered} == {len(rows)} : {covered == len(rows)}")
    print()
    print("| heading_row | sys_ra_id | heading_text | child_rows | child_FR_count |")
    print("|---|---|---|---|---|")
    for n in nodes:
        ch = n["children"]
        span = f"r{ch[0]}–r{ch[-1]} ({len(ch)})" if ch else "（無）"
        print(f"| r{n['row']} | {n['fid']} | {n['text']} | {span} "
              f"| {len(n['fr'])} |")

    out = ROOT / "data" / "sys2_heading_tree.tsv"
    with out.open("w", encoding="utf-8") as fh:
        fh.write("heading_row\tsys_ra_id\theading_text\tchild_rows\t"
                 "child_FR_count\n")
        for n in nodes:
            fh.write(f"{n['row']}\t{n['fid']}\t{n['text']}\t"
                     f"{' ¦ '.join(str(c) for c in n['children'])}\t"
                     f"{len(n['fr'])}\n")
    write_meta(out, ["heading_row", "sys_ra_id", "heading_text", "child_rows", "child_FR_count"], len(nodes),
               generated_by="features/display/scripts/sys2_heading_tree.py",
               rulings=[],
               measurement_conditions="節點＝Category 正規化為 heading 之列；子＝其後之非 Heading 資料列至下一個 Heading 為止（位置性）",
               notes="45 節點；r72 一節點下掛 48 個 FR。")
    print(f"\nwrote {out}")
    print(f"FR rows under a heading: {sum(len(n['fr']) for n in nodes)}")
    print(f"headings with 0 FR children: "
          f"{sum(1 for n in nodes if not n['fr'])}")


if __name__ == "__main__":
    main()
