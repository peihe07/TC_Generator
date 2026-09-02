#!/usr/bin/env python3
"""VS-SL-03 §1 —— 將 Pei 認可之 44 名 `manual` 別名綁入查找。

綁定一律**取自 `tier2_evidence` 之明指**，不以名稱相似度推算：

  形式 A  `HMI r311 [4.] …`          → Settings 第 311 列
  形式 B  `… Power Source（r583）`    → Settings 第 583 列
  形式 C  `HMI r566/r570/… > Aux n > Type`
          → 以（parent = `Aux n`、item = `Type`）綁；`Aux n` 之 n 取自 tc_name 之
            `SWITCH n`。18 個 Aux 家族名皆走此形。
  形式 D  無明指之 Settings 列（只給分類或只給 FIP）
          → **不綁 path**，只綁 FIP（供 PROXI），並記 `ALIAS_MANUAL_NO_PATH`

FIP 一律取 `tier2_evidence` 內 `FIP No.<n>` 之第一個；無則不綁。
"""

from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from settings_lookup import Lookup, _norm  # noqa: E402

CANDIDATES = "docs/fw036/handoff/down/20260902_VS-SL-02_alias_candidates.tsv"

ROW_AFTER_HMI = re.compile(r"HMI\s+r(\d+)(?![\d/–-])")
ROW_IN_PARENS = re.compile(r"[（(]r(\d+)[）)]")
AUX_PATH = re.compile(r"Aux\s+n\s*>\s*([A-Za-z][A-Za-z ]*?)\s*[（(]")
AUX_PATH2 = re.compile(r"Aux\s+n\s*>\s*([A-Za-z][A-Za-z ]*)$")
SWITCH_N = re.compile(r"SWITCH\s+(\d)", re.I)
FIP_NO = re.compile(r"FIP\s+No\.(\d+)")


def parse_binding(tc_name: str, evidence: str) -> dict:
    """回 {hmi_row | (parent,item) | None, fip_no, form}。"""
    fip = FIP_NO.search(evidence)
    out = {"fip_no": fip.group(1) if fip else "", "hmi_row": None,
           "hmi_parent_item": None, "form": ""}

    m = ROW_AFTER_HMI.search(evidence)
    if m:
        out["hmi_row"] = int(m.group(1))
        out["form"] = "A"
        return out
    m = ROW_IN_PARENS.search(evidence)
    if m:
        out["hmi_row"] = int(m.group(1))
        out["form"] = "B"
        return out
    sw = SWITCH_N.search(tc_name)
    item = AUX_PATH.search(evidence) or AUX_PATH2.search(evidence)
    if sw and item:
        out["hmi_parent_item"] = (f"Aux {sw.group(1)}", item.group(1).strip())
        out["form"] = "C"
        return out
    out["form"] = "D"
    return out


def resolve(lk: Lookup, b: dict) -> dict | None:
    """把綁定解成 Settings 之一項。"""
    if b["hmi_row"] is not None:
        for it in lk.settings:
            if it["row"] == b["hmi_row"]:
                return it
        return None
    if b["hmi_parent_item"]:
        parent, name = b["hmi_parent_item"]
        for it in lk.settings:
            if it["parent"] == parent and _norm(it["name_plain"]) == _norm(name):
                return it
    return None


def build(root: Path) -> tuple[Lookup, dict]:
    """回 (lookup, {tc_name: {item, fip_no, form}})。"""
    lk = Lookup(root)
    bound: dict[str, dict] = {}
    for row in csv.DictReader(open(root / CANDIDATES), delimiter="\t"):
        if row["tier2_proposal"] != "manual":
            continue
        b = parse_binding(row["tc_name"], row["tier2_evidence"])
        item = resolve(lk, b)
        bound[row["tc_name"]] = {"item": item, "fip_no": b["fip_no"],
                                 "form": b["form"], "evidence": row["tier2_evidence"]}
    return lk, bound


def main() -> int:
    root = Path(__file__).resolve().parents[3]
    lk, bound = build(root)
    ok = miss = 0
    print(f"{'tc_name':<58} {'形':<3} {'HMI 綁定':<52} FIP")
    for name, b in bound.items():
        it = b["item"]
        if it:
            path = " > ".join(["Settings", it["category"]]
                              + ([it["parent"]] if it["parent"] else [])
                              + [it["name_plain"]])
            ok += 1
        else:
            path = "—（不綁 path）"
            miss += 1
        print(f"{name[:57]:<58} {b['form']:<3} r{it['row'] if it else '---':<5} "
              f"{path[:46]:<47} {b['fip_no'] or '—'}")
    print(f"\n綁定成功 {ok}／{len(bound)}；不綁 path {miss}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
