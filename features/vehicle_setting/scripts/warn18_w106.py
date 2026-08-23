"""W-106（60 包 §6）—— `FR_VS_Cmd_Tlm`／`HSW_Cmd_Tlm` 之 WARN 類 leaf 可寫性實測。

該二訊號之 leaf 從未取用，其可寫性未實測（36 輪 §3.3 未驗第四項）。
逐 leaf 列其分級、阻塞因子、值域來源與其是否可解。

**不得跨列引入 `FR_VS_Cmd_Tlm` 之值域**（禁區；A-VS103）。
"""
from __future__ import annotations

import csv
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from dr_conflict import conflict                              # noqa: E402
from inscope_w39 import blocks_with_sec                       # noqa: E402
from writability_driver import (SIG_REF, clause_pairs, dbc_signals,  # noqa: E402
                                lid_column_domain, run, sourced_signals)

FEAT = Path(__file__).resolve().parents[1]
TARGETS = ("FR_VS_Cmd_Tlm", "HSW_Cmd_Tlm")


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    in_dbc, sourced = dbc_signals(), sourced_signals(blocks)
    mid = lid_column_domain()
    grades, detail = run()
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    delivered = set()
    for f in sorted((FEAT / "generated").glob("batch*.json")):
        delivered |= {tc["leaf_id"] for tc in json.loads(f.read_text(encoding="utf-8"))["tcs"]}

    rows = []
    for leaf, row in l2r.items():
        qs = re.findall(r"\d{7}", row["reqid_list"] or "")
        sigs, drs = set(), set()
        for q in qs:
            blk = blocks.get(q)
            if not blk:
                continue
            sigs |= {m.group(2) for m in SIG_REF.finditer(blk["text"])}
            for tok, vals in clause_pairs(blk["text"]).items():
                for val in vals:
                    if (dr := conflict(tok, val)):
                        drs.add(dr)
        tgt = sigs & set(TARGETS)
        if not tgt:
            continue
        g = gen.get(leaf, {})
        rows.append({
            "leaf": leaf, "layer2": g.get("layer2", ""), "sig": ";".join(sorted(tgt)),
            "writable": grades.get(leaf, "?"), "generatable": g.get("generatable", ""),
            "delegate": g.get("delegate", ""), "已交付": leaf in delivered,
            "blocker": detail.get(leaf, {}).get("blocker_class", ""),
            "reason": str(detail.get(leaf, {}).get("理由", "")),
            "dr": ";".join(sorted(drs)),
            "值域": "可解" if all(mid.get(s) for s in tgt) else "未解",
            "值域來源": {s: sorted(mid.get(s, [])) for s in sorted(tgt)},
        })

    print(f"標的 leaf 合計 {len(rows)}（`FR_VS_Cmd_Tlm` ＋ `HSW_Cmd_Tlm` 之 WARN 類）\n")
    hdr = f"{'leaf':46s} {'L2':22s} {'訊號':28s} {'W':3s} {'gen':4s} {'交付':4s} {'值域':4s} {'DR':10s} 阻塞"
    print(hdr)
    print("-" * len(hdr))
    for r in sorted(rows, key=lambda x: (x["sig"], x["leaf"])):
        print(f"{r['leaf']:46s} {r['layer2']:22s} {r['sig']:28s} {r['writable']:3s} "
              f"{r['generatable']:4s} {'已' if r['已交付'] else '未':4s} {r['值域']:4s} "
              f"{r['dr']:10s} {r['blocker'] or r['reason'][:26]}")

    print("\n分級分布：", dict(Counter(r["writable"] for r in rows)))
    print("generatable：", dict(Counter(r["generatable"] for r in rows)))
    print("值域：", dict(Counter(r["值域"] for r in rows)))
    for s in TARGETS:
        print(f"  {s} 之 LID `Atlantis` 欄組值域：{sorted(mid.get(s, [])) or '（無）'}")
    pool = [r for r in rows if r["generatable"] == "yes" and not r["已交付"]]
    print(f"\n**可寫且未交付者：{len(pool)}**")
    for r in pool:
        print("   ", r["leaf"], r["sig"])


if __name__ == "__main__":
    main()
