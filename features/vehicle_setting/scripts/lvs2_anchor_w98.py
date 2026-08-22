"""W-98 之錨點執行器（R-VS54 ＋ R-VS57，59 包 §3）。

二錨點同批執行並列回報：
  必命中   —— 一個編造之訊號名（`FL_HS_NOPE_Tlm`）須判 FAIL
  必不命中 —— A-VS110 之 33 條須判 WARN 而非 FAIL
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec
from writability_driver import (SIG_REF, dbc_signals, lvs2_verdict,  # noqa: E402
                                run, sourced_signals)

FEAT = Path(__file__).resolve().parents[1]
FABRICATED = "FL_HS_NOPE_Tlm"
TARGETS = ("FL_HS_Cmd_Tlm", "FR_HS_Cmd_Tlm", "FL_VS_Cmd_Tlm")


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    in_dbc, sourced = dbc_signals(), sourced_signals(blocks)

    a = lvs2_verdict(FABRICATED, in_dbc, sourced)
    print(f"錨點 1（必命中）  編造之訊號名 {FABRICATED:>16s} → {a}"
          f"   {'PASS，可失敗' if a == 'FAIL' else '⚠ 未命中，檢查已失效'}")

    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    grades, detail = run()
    hit, bad = [], []
    for leaf, row in l2r.items():
        qs = re.findall(r"\d{7}", row["reqid_list"] or "")
        sigs = {m.group(2) for q in qs if (b := blocks.get(q))
                for m in SIG_REF.finditer(b["text"])}
        if not sigs & set(TARGETS):
            continue
        hit.append(leaf)
        vs = {sg: lvs2_verdict(sg, in_dbc, sourced) for sg in sigs & set(TARGETS)}
        if any(v != "WARN" for v in vs.values()):
            bad.append((leaf, vs))
    print(f"錨點 2（必不命中）A-VS110 之標的 leaf {len(hit)} 條 —— "
          f"判非 WARN 者 {len(bad)}   {'PASS' if not bad else '⚠ 命中，R-VS57 未生效'}")
    for leaf, vs in bad[:10]:
        print("   ", leaf, vs)

    dep = [k for k, v in detail.items() if v.get("dr_dependent") == "DR-25"]
    print(f"\n標 dr_dependent = DR-25 者：{len(dep)} 條")
    w = {leaf: grades[leaf] for leaf in hit}
    from collections import Counter
    print("A-VS110 標的之分級：", dict(Counter(w.values())))
    if a != "FAIL" or bad:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
