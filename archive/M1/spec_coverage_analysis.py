"""L2 SPEC coverage analysis (deterministic, no AI).

Cross-references SPEC behaviours (PC rules from the Media HMI PDF) against the
SWE1 requirements and the TC workbook, combining TWO signals so the result is
trustworthy (token-Jaccard alone over/under-flags templated wording):

  1. Explicit citation  — a requirement that cites "PCx.y" in the SWRA covers it
                          (high confidence, deterministic).
  2. Content match      — token Jaccard between the PC text and a req / TC.

A PC rule is a confident SPEC-only gap only when it is NEITHER cited NOR
content-matched by any requirement. Output: a 3-layer table (PC ↔ req ↔ TC).

Run: python archive/M1/spec_coverage_analysis.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "backend"))

import fitz  # pymupdf
import openpyxl

from spec_matcher import _tokenize, _jaccard
from req_tracer import load_swe1_reqs
from parser import parse_tc_xlsx

ROOT = Path(__file__).resolve().parent.parent
HMI_PDF = ROOT / "docs/test/Player/SPEC/Media HMI Logic and Flow R1 SR24 Post 2A (July 25th, 2023).pdf"
SWRA = ROOT / "docs/test/Player/SWE1/FM-WI-SW-PLA-SWRA-A04.xlsx"
SWE1_REQS = ROOT / "archive/M1/swe1_pla_reqs.json"
TC_GLOB = "docs/test/Player/Review/*PlayerFunctions*done*.xlsx"

CONTENT_TH = 0.12  # below this, no content coverage
_PC_DEF = re.compile(r"(PC\d[\d.]*)\)\s*(.+)")
_PC_CITE = re.compile(r"\bPC\d[\d.]*")
_RID = re.compile(r"SWE1-PLA-[\d-]+")


def extract_pc_rules() -> list[tuple[str, str]]:
    """Return [(pc_id, text)] for each PC rule, first occurrence (its definition)."""
    doc = fitz.open(HMI_PDF)
    txt = "".join(doc[i].get_text() for i in range(doc.page_count))
    rules: dict[str, str] = {}
    for seg in re.split(r"(?=PC\d[\d.]*\))", txt):
        m = _PC_DEF.match(seg.replace("\n", " "))
        if m and len(m.group(2).strip()) > 12:
            rules.setdefault(m.group(1), m.group(2).strip()[:240])
    # natural PC ordering
    def key(pid):
        return [int(x) for x in pid[2:].split(".")]
    return sorted(rules.items(), key=lambda kv: key(kv[0]))


def citation_map() -> dict[str, set[str]]:
    """PC id -> set of requirement ids that cite it (from the SWRA)."""
    wb = openpyxl.load_workbook(SWRA, read_only=True, data_only=True)
    out: dict[str, set[str]] = {}
    for ws in wb.worksheets:
        for row in ws.iter_rows(values_only=True):
            line = " | ".join(str(c) for c in row if c)
            rids = _RID.findall(line)
            pcs = _PC_CITE.findall(line)
            if rids and pcs:
                for p in set(pcs):
                    out.setdefault(p, set()).add(rids[0])
    return out


def main() -> None:
    pcs = extract_pc_rules()
    cites = citation_map()
    reqs = load_swe1_reqs(str(SWE1_REQS))
    req_tok = [(r["id"], _tokenize(f"{r.get('title','')} {r.get('desc','')}")) for r in reqs]
    tc_path = next(ROOT.glob(TC_GLOB))
    tcs = parse_tc_xlsx(str(tc_path))["rows"]
    tc_tok = [(t.get("tc_id"), _tokenize(f"{t.get('test_item','')} {t.get('expected_result','')}"))
              for t in tcs]

    rows = []
    for pid, ptxt in pcs:
        pt = _tokenize(ptxt)
        cited = sorted(cites.get(pid, []))
        rid, rscore = max(((i, _jaccard(pt, tk)) for i, tk in req_tok),
                          key=lambda x: x[1], default=(None, 0))
        tid, tscore = max(((i, _jaccard(pt, tk)) for i, tk in tc_tok),
                          key=lambda x: x[1], default=(None, 0))
        req_covered = bool(cited) or rscore >= CONTENT_TH
        tc_covered = tscore >= CONTENT_TH
        rows.append({
            "pc": pid, "text": ptxt, "cited_by": cited,
            "best_req": rid, "req_score": round(rscore, 2),
            "best_tc": tid, "tc_score": round(tscore, 2),
            "req_covered": req_covered, "tc_covered": tc_covered,
        })

    spec_only = [r for r in rows if not r["req_covered"]]
    untested = [r for r in rows if not r["tc_covered"]]
    json.dump(rows, open(ROOT / "archive/M1/spec_coverage_player.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=2)

    print(f"SPEC PC 規則: {len(rows)}")
    print(f"需求覆蓋(引用 OR 內文): {len(rows)-len(spec_only)}/{len(rows)} "
          f"= {(len(rows)-len(spec_only))/len(rows):.0%}")
    print(f"TC 覆蓋(內文): {len(rows)-len(untested)}/{len(rows)} "
          f"= {(len(rows)-len(untested))/len(rows):.0%}")
    print(f"\n=== 高信心 SPEC-only(既沒引用、也沒內文匹配需求)= {len(spec_only)} 條 ===")
    for r in spec_only:
        print(f"  [{r['pc']}] (best req {r['best_req']} {r['req_score']}) {r['text'][:78]}")


if __name__ == "__main__":
    main()
