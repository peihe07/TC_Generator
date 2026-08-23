"""W-108(1) 之錨點（R-VS54 ＋ R-VS57(4)，61 包 §4）。

  必命中   —— `HSW_Cmd_Tlm` 之 4 leaf 須由 WARN 轉 **W2／B6-value-absent**
  必不命中 —— `FL_HS_Cmd_Tlm` 之 17 leaf 須維持 **WARN**（照寫，標 dr_dependent）
二錨點同批執行並列回報。
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec                            # noqa: E402
from writability_driver import (SIG_REF, dbc_signals, lid_column_domain,  # noqa: E402
                                lvs2_verdict, run, sourced_signals,
                                value_sourced, bus_domain)

FEAT = Path(__file__).resolve().parents[1]


def leaves_touching(sig: str, blocks: dict, l2r: dict) -> list[str]:
    out = []
    for leaf, row in l2r.items():
        qs = re.findall(r"\d{7}", row["reqid_list"] or "")
        sigs = {m.group(2) for q in qs if (b := blocks.get(q))
                for m in SIG_REF.finditer(b["text"])}
        if sig in sigs:
            out.append(leaf)
    return out


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    in_dbc, sourced = dbc_signals(), sourced_signals(blocks)
    mid, high = lid_column_domain(), bus_domain()
    grades, detail = run()

    for sig, want, label in (("HSW_Cmd_Tlm", "B6", "必命中"),
                             ("FL_HS_Cmd_Tlm", "WARN", "必不命中")):
        v = lvs2_verdict(sig, in_dbc, sourced, value_sourced(sig, in_dbc, mid, high))
        ls = leaves_touching(sig, blocks, l2r)
        if want == "B6":
            bad = [l for l in ls if detail.get(l, {}).get("blocker_class") != "B6-value-absent"]
            ok = v == "B6" and not bad
        else:
            bad = [l for l in ls if detail.get(l, {}).get("dr_dependent") != "DR-25"
                   and grades.get(l) in ("W0", "W1")]
            ok = v == "WARN" and not bad
        print(f"錨點（{label}）{sig:16s} → {v:5s}  leaf {len(ls):3d}  "
              f"不符 {len(bad):2d}   {'PASS' if ok else '⚠ 未命中'}")
        if bad:
            print("    ", bad[:8])

    dep = sum(1 for v in detail.values() if v.get("dr_dependent") == "DR-25")
    b6 = sum(1 for v in detail.values() if v.get("blocker_class") == "B6-value-absent")
    print(f"\n`dr_dependent = DR-25`：{dep} 條（61 包 §4 之預期 61）")
    print(f"`B6-value-absent`：{b6} 條（預期 4）")
    if dep != 61 or b6 != 4:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
