"""W-109（61 包 §5）—— 產能終局之盤點。

逐一列出**未交付 leaf** 之阻塞歸屬，並列**逐 DR 之解鎖量**
（某 DR 覆後可增加幾條可生成 leaf），**依解鎖量降冪排序**。

**該表即送 DR 之優先序依據，取代歷輪之估計。**

解鎖量之判準（R-VS50′：「有 N 個標的」與「N 個可作業之標的」須分列）：
  標的數     —— 該 DR 所涉之未交付 leaf 數（不問其他阻塞）
  可解鎖數   —— 該 DR **單獨**覆後即成為 `generatable = yes` 之未交付 leaf 數
                （即其餘阻塞因子皆已清）
"""
from __future__ import annotations

import collections
import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from dr_conflict import conflict                                   # noqa: E402
from inscope_w39 import blocks_with_sec                            # noqa: E402
from writability_driver import (SIG_REF, clause_pairs, dbc_signals,  # noqa: E402
                                lid_column_domain, run, sourced_signals,
                                value_sourced, bus_domain)

FEAT = Path(__file__).resolve().parents[1]


def delivered_leaves() -> set[str]:
    groups: dict[str, list] = collections.defaultdict(list)
    for f in (FEAT / "generated").glob("batch*.json"):
        m = re.match(r"(batch\d+)(?:_v(\d+))?\.json$", f.name)
        if m:
            groups[m.group(1)].append((int(m.group(2) or 1), f))
    out = set()
    for v in groups.values():
        out |= {tc["leaf_id"] for tc in
                json.loads(max(v)[1].read_text(encoding="utf-8"))["tcs"]}
    return out


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    grades, detail = run()
    in_dbc, sourced = dbc_signals(), sourced_signals(blocks)
    mid, high = lid_column_domain(), bus_domain()
    done = delivered_leaves()

    rows, target, unlock = [], collections.Counter(), collections.Counter()
    for leaf, g in gen.items():
        if leaf in done:
            continue
        det = detail.get(leaf, {})
        qs = re.findall(r"\d{7}", (l2r.get(leaf, {}).get("reqid_list") or ""))
        drs, b6 = set(), False
        for q in qs:
            blk = blocks.get(q)
            if not blk:
                continue
            for tok, vals in clause_pairs(blk["text"]).items():
                for v in vals:
                    if (dr := conflict(tok, v)):
                        drs.add(dr)
            for m in SIG_REF.finditer(blk["text"]):
                sg = m.group(2)
                if sg not in in_dbc and sg in sourced and not value_sourced(
                        sg, in_dbc, mid, high):
                    b6 = True
        blockers = []
        if g["delegate"] == "blocked":
            blockers.append(f"delegate=blocked{'/' + g['blocked_ref'] if g['blocked_ref'] else ''}")
        if g["delegate"] == "pending":
            blockers.append("delegate=pending")
        if det.get("blocker_class") == "B4-preamble":
            blockers.append("B4-preamble")
        if b6:
            blockers.append("B6-value-absent")
        blockers += sorted(drs)
        if det.get("dr_dependent"):
            blockers.append(f"dr_dependent={det['dr_dependent']}")
        # 其餘之 W2 —— 其阻塞為分級判準本身（R-VS47），無對應 DR。
        # 不列則「無阻塞因子」一欄會把它們與真正可作業者混為一談。
        if not blockers and grades.get(leaf) == "W2":
            blockers.append(f"W2：{det.get('理由', '（未載）')}")
        rows.append({"leaf": leaf, "w": grades.get(leaf, "?"), "gen": g["generatable"],
                     "delegate": g["delegate"], "blockers": blockers})

        # 標的數：該 DR 所涉之未交付 leaf
        keys = set(drs)
        if g["blocked_ref"]:
            keys.add(g["blocked_ref"])
        if b6:
            keys.add("（無 DR：HSW_Cmd_Tlm 值域無來源）")
        if det.get("dr_dependent"):
            keys.add(det["dr_dependent"] + "′")
        if not keys and grades.get(leaf) == "W2":
            keys.add(f"（無 DR：{det.get('理由', '（未載）')}）")
        for k in keys:
            target[k] += 1
        # 可解鎖數：該 DR 為其**唯一**阻塞因子者
        if len(keys) == 1 and g["delegate"] not in ("blocked", "pending") \
                and det.get("blocker_class") != "B4-preamble":
            unlock[next(iter(keys))] += 1

    print(f"已交付 **{len(done)}**；母體 {len(gen)}；**未交付 {len(rows)}**\n")
    print("## 逐 DR 之解鎖量（降冪）\n")
    print("| DR／阻塞因子 | 標的數（未交付） | **可解鎖數**（其為唯一阻塞） |")
    print("|---|---:|---:|")
    for k, n in sorted(target.items(), key=lambda x: (-unlock[x[0]], -x[1])):
        print(f"| {k} | {n} | **{unlock[k]}** |")
    print()
    nob = [r for r in rows if not r["blockers"]]
    print(f"**無任何阻塞因子而仍未交付者：{len(nob)}**（即池 —— 可作業而未取）")
    for r in nob:
        print("   ", r["leaf"], r["w"], r["gen"])
    print()
    print("## 未交付 leaf 之阻塞歸屬（前 40 列）\n")
    print("| leaf | W | gen | delegate | 阻塞因子 |")
    print("|---|---|---|---|---|")
    for r in sorted(rows, key=lambda x: x["leaf"])[:40]:
        print(f"| `{r['leaf']}` | {r['w']} | {r['gen']} | {r['delegate']} | "
              f"{'；'.join(r['blockers']) or '—'} |")
    (FEAT / "docs/reports/endgame_w109.json").write_text(
        json.dumps({"delivered": len(done), "undelivered": len(rows),
                    "target": dict(target), "unlock": dict(unlock),
                    "rows": rows}, ensure_ascii=False, indent=1), encoding="utf-8")


if __name__ == "__main__":
    main()
