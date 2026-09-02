#!/usr/bin/env python3
"""VS-SL-03 §1 —— 綁別名後之 v3 報告（三本）。**唯讀，不寫回工作簿。**

與 v2 之別：Pei 2026-09-02 認可之 44 名 `manual` 已綁入（`vs_sl03_bind.py`），
故其列可產出 `path_proposed`／`control_proposed`，且 PROXI 之分支 (2) 可用其 FIP。
分支規則、正規化、自檢與 v2 同（VS-SL-02 §2.1／§2.4／§2.6）。
"""

from __future__ import annotations

import csv
import re
import sys
import warnings
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import vs_sl01_dryrun as v1  # noqa: E402
import vs_sl02_dryrun_v2 as v2  # noqa: E402
import vs_sl03_bind as bind  # noqa: E402
from settings_lookup import Lookup, format_proxi, resolve_raw  # noqa: E402

warnings.filterwarnings("ignore")
ROOT = v1.ROOT
DR_NO = v2.DR_NO
COLUMNS = v1.COLUMNS


def query_bound(lk: Lookup, name: str, item: dict | None, fip_no: str,
                req_text: str) -> dict:
    """以已綁之 Settings 項與 FIP No. 產出 path／control／proxi。"""
    flags: list[str] = []
    path = control = None
    if item:
        path = ["Settings", item["category"]] + \
               ([item["parent"]] if item["parent"] else []) + [item["name_plain"]]
        control = {"template": item["template"], "options": item["options"]}
    else:
        flags.append("ALIAS_MANUAL_NO_PATH")

    atl = [r for r in lk.atlantis if r["no"] == fip_no] if fip_no else []
    return {"name": name, "path": path, "control": control,
            "proxi": [], "flags": flags, "_atl": atl}


def proxi_bound(lk: Lookup, res: dict, item_text: str,
                proxi_now: str) -> tuple[list[dict], str, set[str]]:
    """分支 (1)(2)(3) —— 已綁之名不再落入 (4)。"""
    flags: set[str] = set()
    pairs = v1.PROXI_OLD_RE.findall(proxi_now)
    if pairs:
        out = []
        for param, label in pairs:
            raw = lab = None
            for one in re.split(r"\s+or\s+", label):
                raw, lab = resolve_raw(lk.values, param.strip(), one.strip())
                if raw is not None:
                    break
            if raw is None:
                flags.add("RAW_MISSING")
            out.append({"param": param.strip(), "raw": raw, "label": lab or label})
        return out, "(1) 形制改寫", flags

    for rec in res.get("_atl") or lk.atlantis_rows(res["name"]):
        if rec["parsed"]["terms"]:
            out = []
            for t in rec["parsed"]["terms"]:
                for label in t["labels"]:
                    raw, lab = resolve_raw(lk.values, t["param"], label)
                    if raw is None:
                        flags.add("RAW_MISSING")
                    out.append({"param": t["param"], "raw": raw, "label": lab or label})
                if len(t["labels"]) > 1:
                    flags.add("OR_VALUE")
            return out, f"(2) 总控表 No.{rec['no']}", flags
        if rec["parsed"]["kind"] == "ALWAYS_FALSE":
            flags.add("ALWAYS_FALSE")

    if v2.REQ_VAR_RE.search(item_text or ""):
        from settings_lookup import REQ_COND_RE, _dedup_terms
        terms = _dedup_terms([
            {"param": re.sub(r"^(?:if|and|or|when)\s+", "", p.strip(), flags=re.I).strip(),
             "labels": [l.strip()]} for p, l in REQ_COND_RE.findall(item_text)])
        if terms:
            out = []
            for t in terms:
                for label in t["labels"]:
                    raw, lab = resolve_raw(lk.values, t["param"], label)
                    if raw is None:
                        flags.add("RAW_MISSING")
                    out.append({"param": t["param"], "raw": raw, "label": lab or label})
                if len(t["labels"]) > 1:
                    flags.add("OR_VALUE")
            return out, "(2') 需求原文", flags

    flags.add("PROXI_PENDING")
    return [{"pending": f"PENDING: {DR_NO}"}], "(3) 二來源皆空", flags


def build_alias_v3(lk: Lookup, names, bound: dict) -> list[dict]:
    """`match_type`：44 名升為 `manual`；其餘沿 v2。evidence 保留。"""
    alias, tier2 = v2.merge_candidates(v1.build_alias(lk, names))
    for a in alias:
        b = bound.get(a["tc_name"])
        if not b:
            continue
        a["match_type"] = "manual"
        if b["item"]:
            a["hmi_name"] = b["item"]["name_plain"]
        if b["fip_no"]:
            hit = [r for r in lk.atlantis if r["no"] == b["fip_no"]]
            if hit:
                a["fip_name"] = hit[0]["name"]
        a["evidence"] = (a["evidence"] + "；Pei 2026-09-02 認可，綁定形式 "
                         + b["form"] + ("（無 path）" if not b["item"] else
                                        f"（Settings r{b['item']['row']}）"))
    return alias


def dryrun_vf230(lk: Lookup, alias_by_tc: dict, bound: dict):
    ws, g = v1.cells(ROOT / v1.VF230)
    out, branch3 = [], []
    for r in v1.data_rows(ws, g):
        item_text = g(r, 9)
        name = v2.setting_of_v2(g, r)
        alias = alias_by_tc.get(name, {"match_type": "UNRESOLVED", "hmi_name": ""})
        status = alias["match_type"]

        if name in bound:
            b = bound[name]
            res = query_bound(lk, name, b["item"], b["fip_no"], item_text)
            proposed, branch, flags = proxi_bound(lk, res, item_text, v1.proxi_now_of(g, r))
            flags |= set(res["flags"])
            flags.add("ALIAS_MANUAL")
        elif status == "exact":
            res = lk.query(alias.get("hmi_name") or name, item_text, DR_NO)
            proposed, branch, flags = v2.proxi_v2(lk, res, item_text,
                                                  v1.proxi_now_of(g, r), "exact")
            flags |= {f for f in res["flags"]
                      if f in ("VARIANT_UNRESOLVED", "BRAND_NAME_UNVERIFIED")}
        else:
            res = {"name": name, "path": None, "control": None, "proxi": [], "flags": []}
            proposed, branch, flags = v2.proxi_v2(lk, res, item_text,
                                                  v1.proxi_now_of(g, r), status)

        notes: list[str] = []
        if proposed and not proposed[0].get("pending"):
            proposed, notes = v1.propose_proxi(lk, {"proxi": proposed}, item_text,
                                               v1.proxi_now_of(g, r))
            if any(n.startswith("EP 兄弟") for n in notes):
                flags.add("EP_SIBLING")

        if not v2.needs_path(g(r, 12)):
            flags.add("BEHAVIOUR_ROW")
        elif not v1.STEP_RE.findall(g(r, 12)):
            flags.add("PATH_ABSENT")
        if "non-NAFTA" in item_text or "non-NAFTA" in g(r, 4):
            flags.add("NON_NAFTA")
        if v1._neg_contra(item_text, v1.proxi_now_of(g, r)):
            flags.add("NEG_CONTRA")

        out.append({
            "row": r, "tc_id": g(r, 6) or "(F 欄空)", "setting": name,
            "alias_status": status,
            "path_now": v1.path_now_of(g, r),
            "path_proposed": " > ".join(res["path"]) if res["path"] else "",
            "control_proposed": v2.control_text(res["control"]),
            "proxi_now": v1.proxi_now_of(g, r),
            "proxi_proposed": (format_proxi(proposed)
                               + ("｜" + "；".join(notes) if notes else "")
                               if proposed else ""),
            "flags": ";".join(sorted(flags)) + f"｜分支 {branch}",
        })
        if branch.startswith("(3)"):
            branch3.append({"row": r, "req_id": g(r, 4), "setting": name})
    return out, branch3


def main() -> int:
    lk, bound = bind.build(ROOT)
    ws, g = v1.cells(ROOT / v1.VF230)
    names = v1.collect_names(g, v1.data_rows(ws, g))
    alias = build_alias_v3(lk, names, bound)
    alias_by_tc = {a["tc_name"]: a for a in alias}

    cols = ["tc_name", "hmi_name", "fip_name", "match_type", "evidence",
            "tier2_proposal", "tier2_evidence"]
    (ROOT / "features/vehicle_setting/data/settings_alias.tsv").write_text(
        "\n".join(["\t".join(cols)] + ["\t".join(a[c] for c in cols) for a in alias]) + "\n",
        encoding="utf-8")

    vf, branch3 = dryrun_vf230(lk, alias_by_tc, bound)
    v1.write_tsv(ROOT / "features/vehicle_setting/reports/vf230_settings_dryrun_v3.tsv", vf)
    v1.write_tsv(ROOT / "features/bed_lowering/reports/bl_settings_dryrun_v3.tsv",
                 v2.dryrun_bl(lk))
    v1.write_tsv(ROOT / "features/vehicle_category/reports/vc_settings_dryrun_v3.tsv",
                 v2.dryrun_vc(lk))
    (ROOT / "features/vehicle_setting/reports/_v3_branch3.tsv").write_text(
        "\n".join(["row\treq_id\tsetting"] +
                  [f"{b['row']}\t{b['req_id']}\t{b['setting']}" for b in branch3]) + "\n",
        encoding="utf-8")

    fc = Counter(f for r in vf for f in r["flags"].split("｜")[0].split(";") if f)
    br = Counter(r["flags"].split("｜分支 ")[1].split(")")[0] + ")" for r in vf)
    print(f"vf230 {len(vf)} 列")
    print("  分支:", dict(br))
    print("  flags:", dict(fc))
    print("  path_proposed 非空:", sum(1 for r in vf if r["path_proposed"]))
    print("  (3) 之列數:", len(branch3))
    print("  別名:", dict(Counter(a["match_type"] for a in alias)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
