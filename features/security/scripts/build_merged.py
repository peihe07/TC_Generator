#!/usr/bin/env python3
"""合併本（SEC-05 §5）—— batch1 v02 ＋ batch2 v01，依 framework Layer 2 順序、D 欄升冪。

另產 `data/coverage.tsv`（70 列 × disposition/batch/tc_count/tc_ids）與更新
`data/pending_summary.tsv`（合併本口徑）。交付本不載內部狀態（D 群不入）。
"""
from __future__ import annotations

import csv
import importlib.util
import json
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
OUT_XLSX = SB / "merged" / "security_v01.xlsx"


def main() -> int:
    OUT_XLSX.parent.mkdir(parents=True, exist_ok=True)
    tcs = []
    for d in (SB / "batch1", SB / "batch2"):
        for f in d.glob("NR1L-*.json"):
            tcs.append(json.loads(f.read_text(encoding="utf-8")))

    l2 = list(csv.DictReader((DATA / "layer2_assign.tsv").open(encoding="utf-8"), delimiter="\t"))
    # framework Layer 2 順序：Test Set 之首見序；其內以 SWE1 之 layer2 列序、再以 TC ID
    ts_order, seen = [], set()
    for r in l2:
        k = (r["test_group"], r["test_set"])
        if k not in seen:
            seen.add(k)
            ts_order.append(k)
    ts_rank = {k: i for i, k in enumerate(ts_order)}
    swe_rank = {r["swe1_id"]: i for i, r in enumerate(l2)}
    tcs.sort(key=lambda t: (ts_rank[(t["test_group"], t["test_set"])],
                            swe_rank[t["req_id"]], t["tc_id"]))

    wb = openpyxl.load_workbook(g1.TEMPLATE)
    ws = wb[g1.SHEET]
    for n, t in enumerate(tcs):
        row = g1.FIRST_ROW + n
        for key, col in g1.COLS.items():
            ws[f"{col}{row}"] = t[key]
        for col, name in zip(g1.VM_COLS, g1.VM_NAMES):
            ws[f"{col}{row}"] = t["vehicle_model"][name]
    report = surgical_save(wb, g1.TEMPLATE, OUT_XLSX)

    # coverage.tsv —— 70 列全覆蓋
    bo = {r["swe1_id"]: r for r in csv.DictReader(
        (DATA / "batch_order.tsv").open(encoding="utf-8"), delimiter="\t")}
    by_swe = defaultdict(list)
    for t in tcs:
        by_swe[t["req_id"]].append(t["tc_id"])
    with (DATA / "coverage.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["swe1_id", "disposition", "ccvr_batch", "tc_count", "tc_ids"])
        for r in l2:
            s = r["swe1_id"]
            ids = sorted(by_swe.get(s, []))
            w.writerow([s, "D" if bo[s]["disposition"] == "D" else "PRODUCED",
                        bo[s]["ccvr_batch"], len(ids), ";".join(ids)])

    # pending_summary.tsv —— 合併本口徑
    import re
    agg = defaultdict(list)
    for t in tcs:
        for line in (t["proc"] + "\n" + t["er"]).splitlines():
            m = re.match(r"^\s*(?:\d+\.\s*)?PENDING:\s*(\S+)", line)
            if m:
                agg[m.group(1)].append(t["tc_id"])
    with (DATA / "pending_summary.tsv").open("w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh, delimiter="\t")
        w.writerow(["token", "count", "tc_ids"])
        for k in sorted(agg):
            w.writerow([k, len(agg[k]), ";".join(sorted(set(agg[k])))])

    cov = list(csv.DictReader((DATA / "coverage.tsv").open(encoding="utf-8"), delimiter="\t"))
    produced = [c for c in cov if int(c["tc_count"]) > 0]
    print(f"合併本：{len(tcs)} TC → {OUT_XLSX.relative_to(ROOT)}")
    print("  逐組:", dict(Counter(t["test_group"] for t in tcs)))
    print("  priority:", dict(Counter(t["priority"] for t in tcs)))
    print(f"  coverage.tsv {len(cov)} 列；tc_count>0 = {len(produced)}；D 群 = "
          f"{sum(1 for c in cov if c['disposition'] == 'D')}")
    print(f"  PENDING token 群 {len(agg)}；行 {sum(len(v) for v in agg.values())}")
    print("  surgical:", {k: v for k, v in report.items() if k != "members_patched"})
    return 0


if __name__ == "__main__":
    sys.exit(main())
