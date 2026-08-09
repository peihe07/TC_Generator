#!/usr/bin/env python3
"""Step 1 (AMFM) — sample Wilson's legacy rows as STYLE exemplars.

R4 froze the 158 `SWE-RAD-*` rows as a legacy region: they trace a superseded
requirement family, so their traceability is not adopted, but they remain this
workbook's only precedent for how a row is written. Style may be borrowed;
traceability may not.

That distinction has to survive into the generation context, because a
few-shot exemplar is the most persuasive thing in a prompt. So every exemplar
emitted here is stripped of the fields that would carry the old family into a
new row — `req_id`, `spec_reference`, `tc_id`, `test_group`, `test_set` — and
carries a `style_only` marker plus the reason. What is left is what style
actually means: how a Test Item is phrased, how a Pre-Condition is staged, the
step granularity of a procedure, how an Expected Result is numbered against it.

Sampling is by CFTS-section-free heuristics, since the legacy rows have no
section of their own under the ruled source: rows are grouped by their own
Test Set value (the band scheme `FM`/`AM`/`USB`), and within each group the
rows closest to the median procedure length are taken — a median row is
typical, whereas the longest and shortest are the ones a reader would call
unrepresentative.

Rows failing the current lint's structural expectations (single-step
procedures, blank priority — the 5 A-AM05/recon compliance notes) are excluded
from the pool, exactly as Home excluded Arif's blank-priority rows: a frozen
deviation must not be learned as style.

Output: `data/exemplars.json`

Usage:
    python AMFMHMI/scripts/extract_exemplars.py --feature-dir AMFMHMI
    python AMFMHMI/scripts/extract_exemplars.py --feature-dir AMFMHMI --per-group 3
"""
from __future__ import annotations

import argparse
import json
import re
import statistics
import sys
from pathlib import Path

import openpyxl

sys.path.insert(0, str(Path(__file__).resolve().parent.parent.parent / "scripts"))
from feature_config import load_feature_config, resolve_path  # noqa: E402

# Carried into the context because they ARE the style.
STYLE_FIELDS = ("test_item", "pre_conditions", "input_test_data",
                "test_procedure", "expected_result", "priority",
                "design_method")
# Withheld because they would import the superseded family's traceability,
# or a column convention R7 overrode for new rows.
WITHHELD = {
    "req_id": "legacy SWE-RAD-* family — new rows trace SWE-RA-RAD-* (R1/R4)",
    "spec_reference": "legacy CFTS024-<ReqIF.ForeignID> form — new rows use "
                      "{doc}-{stla_id} (R7-Q3)",
    "test_group": "legacy value 'Radio' — new rows write 'AMFM' (R7-Q1)",
    "test_set": "legacy band scheme FM/AM/USB — new rows use the capability "
                "scheme (R7-Q2)",
}


def numbered_steps(text: str) -> int:
    return len(re.findall(r"^\s*\d+[\.\)]", str(text or ""), flags=re.M))


def load_legacy_rows(cfg, wb_path: Path) -> list[dict]:
    col = cfg["col"]
    author = cfg["done_region"]["author_value"]
    ws = openpyxl.load_workbook(wb_path, read_only=True)[cfg["workbook"]["sheet"]]
    rows = list(ws.iter_rows(values_only=True))

    def cell(r, key):
        i = col.get(key)
        return "" if i is None or i >= len(r) or r[i] is None else str(r[i]).strip()

    out = []
    for n, r in enumerate(rows[cfg["workbook"]["header_row"]:],
                          start=cfg["workbook"]["header_row"] + 1):
        if cell(r, "author") != author:
            continue
        out.append({"row": n} | {k: cell(r, k) for k in
                                 (*STYLE_FIELDS, *WITHHELD, "author")})
    return out


def usable(row: dict) -> tuple[bool, str]:
    """Frozen deviations are recorded elsewhere; they are not style."""
    if numbered_steps(row["test_procedure"]) < 2:
        return False, "procedure has fewer than two numbered steps"
    if not row["priority"]:
        return False, "blank priority"
    if not row["expected_result"]:
        return False, "blank expected result"
    return True, ""


def pick(rows: list[dict], k: int) -> list[dict]:
    """The k rows closest to the group's median procedure length."""
    if len(rows) <= k:
        return rows
    lengths = [len(r["test_procedure"]) for r in rows]
    mid = statistics.median(lengths)
    return sorted(rows, key=lambda r: abs(len(r["test_procedure"]) - mid))[:k]


def run(args) -> int:
    cfg = load_feature_config(args.feature_dir)
    wb_path = resolve_path(cfg, "workbook")
    rows = load_legacy_rows(cfg, wb_path)
    if not rows:
        print(f"no rows authored by {cfg['done_region']['author_value']!r}",
              file=sys.stderr)
        return 1

    pool, excluded = [], []
    for r in rows:
        ok, why = usable(r)
        (pool if ok else excluded).append(r if ok else {"row": r["row"], "why": why})

    groups: dict[str, list[dict]] = {}
    for r in pool:
        groups.setdefault(r["test_set"] or "(blank)", []).append(r)

    exemplars = []
    for group, members in sorted(groups.items()):
        for r in pick(members, args.per_group):
            exemplars.append({
                "source_row": r["row"],
                "legacy_group": group,
                "style_only": True,
                "withheld": WITHHELD,
                "author": r["author"],
                **{k: r[k] for k in STYLE_FIELDS},
            })

    out = Path(args.feature_dir) / "data"
    out.mkdir(exist_ok=True)
    (out / "exemplars.json").write_text(json.dumps({
        "source": wb_path.name,
        "basis": "frozen legacy region (R4 option i) — STYLE ONLY, "
                 "traceability not adopted",
        "legacy_rows": len(rows), "usable_pool": len(pool),
        "excluded": excluded,
        "groups": {g: len(v) for g, v in sorted(groups.items())},
        "exemplars": exemplars,
    }, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"legacy rows : {len(rows)} (author {cfg['done_region']['author_value']})")
    print(f"excluded    : {len(excluded)} "
          f"({', '.join(sorted({e['why'] for e in excluded})) or '-'})")
    print(f"groups      : " + ", ".join(
        f"{g}={len(v)}" for g, v in sorted(groups.items())))
    print(f"exemplars   : {len(exemplars)} "
          f"({args.per_group} per group, median procedure length)")
    print(f"withheld    : {', '.join(WITHHELD)}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--feature-dir", default=".")
    ap.add_argument("--per-group", type=int, default=2)
    return run(ap.parse_args())


if __name__ == "__main__":
    sys.exit(main())
