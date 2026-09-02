#!/usr/bin/env python3
"""VS-SL-02 §2 —— dry-run v2。**唯讀，不寫回。**

與 v1（`vs_sl01_dryrun.py`）之別：

  2.1 PROXI 提議改為四分支
      (1) proxi_now 非空 → 形制改寫；label 查無 raw → RAW_MISSING（**不 PENDING**）
      (2) proxi_now 空、alias 已解、总控表有條件 → 依总控表
      (3) proxi_now 空、alias 已解、总控表無條件、需求原文無 $var$ → PENDING: DR-49
      (4) alias UNRESOLVED → 只掛 ALIAS_UNRESOLVED，**不掛 PROXI_PENDING、不 PENDING**
  2.2 只以 `exact` 之別名跑；`manual` 未經 Pei 認可不綁入，另計「若認可將解鎖之列數」
  2.3 PATH_ABSENT 分流：行為型（`Send CAN:` 而不操作設定項）移除該 flag
  2.4 Options 正規化：`/`、`,`、`+` 兩側各一空格，字詞逐字不動
  2.5 BL 之 Body_Types 行 PENDING（待 §1 之裁定）；DT 相關列掛 DT_APPLICABILITY
      VC 之 Specialty／螢幕方向列保留散文並移除 NO_MAPPING
"""

from __future__ import annotations

import re
import sys
import warnings
from collections import Counter, OrderedDict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import vs_sl01_dryrun as v1  # noqa: E402
from settings_lookup import Lookup, _norm, format_proxi  # noqa: E402

warnings.filterwarnings("ignore")

ROOT = v1.ROOT
DR_NO = "DR（未取號，依審閱 §2.2：未送出前不佔號）"
COLUMNS = v1.COLUMNS
REQ_VAR_RE = re.compile(r"\$[A-Za-z][A-Za-z0-9_]*\$|\b[A-Za-z][A-Za-z0-9_]{2,}\s*=\s*\[")
BEHAVIOUR_RE = re.compile(r"^\s*\d*\.?\s*Send CAN:", re.M)
# 92+3 列把設定項名寫成不加引號（`… check that the X setting is displayed …`），
# v1 之 `"X" customer setting` 抽取式整批漏掉。本輪補此 fallback。
SETTING_FALLBACK_RE = re.compile(r"check that the (.+?) setting is displayed", re.I)


def setting_of_v2(g, r) -> str:
    """設定項名。主抽取式未中時改用不加引號之形制。"""
    name = v1.setting_of(g, r)
    if name:
        return name
    m = SETTING_FALLBACK_RE.search(g(r, 12))
    return m.group(1).strip().strip('"') if m else ""


def normalize_option(text: str) -> str:
    """`/`、`,`、`+` 兩側各一空格；字詞逐字不動（VS-SL-02 §2.4）。"""
    s = re.sub(r"\s*([/,+])\s*", r" \1 ", text)
    return " ".join(s.split())


def control_text(control: dict | None) -> str:
    if not control:
        return ""
    opts = " / ".join(f'"{normalize_option(o)}"' for o in control["options"])
    return f"{control['template']} {opts}".strip() if opts else control["template"]


def needs_path(procedure: str) -> bool:
    """該列是否操作某設定項（需路徑）。行為型（只送 CAN 訊號）不需。"""
    if re.search(r"customer setting|Vehicle Settings menu|Settings screen", procedure, re.I):
        return True
    return not BEHAVIOUR_RE.search(procedure)


def proxi_v2(lk: Lookup, res: dict, item: str, proxi_now: str,
             alias_status: str) -> tuple[list[dict], str, set[str]]:
    """四分支之 PROXI 提議。回 (清單, 分支代號, flags)。"""
    flags: set[str] = set()

    # (1) 既有 PROXI → 形制改寫
    pairs = v1.PROXI_OLD_RE.findall(proxi_now)
    if pairs:
        out = []
        for param, label in pairs:
            raw, lab = None, None
            for one in re.split(r"\s+or\s+", label):
                raw, lab = _resolve(lk, param.strip(), one.strip())
                if raw is not None:
                    break
            if raw is None:
                flags.add("RAW_MISSING")
            out.append({"param": param.strip(), "raw": raw, "label": lab or label})
        return out, "(1) 形制改寫", flags

    # (4) 別名未解 → 不提議、不 PENDING
    if alias_status != "exact":
        flags.add("ALIAS_UNRESOLVED")
        return [], "(4) 別名未解", flags

    # (2) 总控表有條件
    for rec in lk.atlantis_rows(res["name"]):
        if rec["parsed"]["terms"]:
            out = []
            for t in rec["parsed"]["terms"]:
                for label in t["labels"]:
                    raw, lab = _resolve(lk, t["param"], label)
                    if raw is None:
                        flags.add("RAW_MISSING")
                    out.append({"param": t["param"], "raw": raw, "label": lab or label})
                if len(t["labels"]) > 1:
                    flags.add("OR_VALUE")
            return out, f"(2) 总控表 No.{rec['no']}", flags
        if rec["parsed"]["kind"] == "ALWAYS_FALSE":
            flags.add("ALWAYS_FALSE")

    # 需求原文有 $var$ → 用之（(3) 之條件含「需求原文無 $var$」）
    if REQ_VAR_RE.search(item or ""):
        from settings_lookup import REQ_COND_RE, _dedup_terms
        terms = _dedup_terms([
            {"param": re.sub(r"^(?:if|and|or|when)\s+", "", p.strip(), flags=re.I).strip(),
             "labels": [l.strip()]} for p, l in REQ_COND_RE.findall(item)])
        if terms:
            out = []
            for t in terms:
                for label in t["labels"]:
                    raw, lab = _resolve(lk, t["param"], label)
                    if raw is None:
                        flags.add("RAW_MISSING")
                    out.append({"param": t["param"], "raw": raw, "label": lab or label})
                if len(t["labels"]) > 1:
                    flags.add("OR_VALUE")
            return out, "(2') 需求原文", flags

    # (3) 皆無 → PENDING
    flags.add("PROXI_PENDING")
    return [{"pending": f"PENDING: {DR_NO}"}], "(3) 二來源皆空", flags


def _resolve(lk: Lookup, param: str, label: str):
    from settings_lookup import resolve_raw
    return resolve_raw(lk.values, param, label)


def dryrun_vf230(lk: Lookup, alias_by_tc: dict) -> tuple[list[dict], list[dict]]:
    ws, g = v1.cells(ROOT / v1.VF230)
    out, branch3 = [], []
    for r in v1.data_rows(ws, g):
        item = g(r, 9)
        name = setting_of_v2(g, r)
        alias = alias_by_tc.get(name, {"match_type": "UNRESOLVED", "hmi_name": ""})
        status = alias["match_type"]
        target = alias.get("hmi_name") or name
        res = lk.query(target, item, DR_NO) if (status == "exact" and target) else {
            "name": target, "path": None, "control": None, "proxi": [], "flags": []}

        proposed, branch, flags = proxi_v2(lk, res, item, v1.proxi_now_of(g, r), status)
        proposed, pnotes = (v1.propose_proxi(lk, {"proxi": proposed}, item, v1.proxi_now_of(g, r))
                            if proposed and not proposed[0].get("pending") else (proposed, []))
        if any(n.startswith("EP 兄弟") for n in pnotes):
            flags.add("EP_SIBLING")

        if status == "manual":
            flags.add("ALIAS_MANUAL")
        if not needs_path(g(r, 12)):
            flags.add("BEHAVIOUR_ROW")          # §2.3：行為型，不需路徑
        elif not v1.STEP_RE.findall(g(r, 12)):
            flags.add("PATH_ABSENT")
        if "non-NAFTA" in item or "non-NAFTA" in g(r, 4):
            flags.add("NON_NAFTA")
        if v1._neg_contra(item, v1.proxi_now_of(g, r)):
            flags.add("NEG_CONTRA")
        flags |= {f for f in res.get("flags", []) if f in ("VARIANT_UNRESOLVED", "BRAND_NAME_UNVERIFIED")}

        row = {
            "row": r, "tc_id": g(r, 6) or "(F 欄空)", "setting": name,
            "alias_status": status,
            "path_now": v1.path_now_of(g, r),
            "path_proposed": " > ".join(res["path"]) if res["path"] else "",
            "control_proposed": control_text(res["control"]),
            "proxi_now": v1.proxi_now_of(g, r),
            "proxi_proposed": (format_proxi(proposed) + ("｜" + "；".join(pnotes) if pnotes else "")
                               if proposed else ""),
            "flags": ";".join(sorted(flags)) + f"｜分支 {branch}",
        }
        out.append(row)
        if branch.startswith("(3)"):
            branch3.append({"row": r, "req_id": g(r, 4), "setting": name})
    return out, branch3


DT_ONLY = "the vehicle is a dt configuration"
DT_OR = "the vehicle configuration is either dt or dj/d2"


def dryrun_bl(lk: Lookup) -> list[dict]:
    ws, g = v1.cells(ROOT / v1.BL)
    out = []
    for r in v1.data_rows(ws, g):
        lines = [re.sub(r"^\s*\d+\.\s*", "", x).strip()
                 for x in g(r, 10).split("\n") if x.strip()]
        low = [" ".join(x.lower().split()).rstrip(".") for x in lines]
        proposed = ["PROXI CAN node 27 (ASM/ASCM) = 1 (Present)",
                    "PROXI Body_Types = PENDING（待 VS-SL-02 §1 之裁定）"]
        flags = {"PROSE_PRECOND"}
        # 包內 §2.5：只有 DT 專屬（7）與「DT 或 DJ/D2」（16）掛旗；DJ/D2 專屬之 8 列不掛
        if DT_ONLY in low or DT_OR in low:
            flags.add("DT_APPLICABILITY")
        elif "the vehicle is a dj/d2 configuration" in low:
            flags.add("DJD2_ONLY")
        out.append({
            "row": r, "tc_id": g(r, 6) or "(F 欄空)", "setting": g(r, 8) or g(r, 7),
            "alias_status": "n/a（不走 Settings List）",
            "path_now": v1.path_now_of(g, r), "path_proposed": "（本 feature 不套 path 段）",
            "control_proposed": "", "proxi_now": v1.proxi_now_of(g, r) or "（無 PROXI）",
            "proxi_proposed": " ; ".join(proposed),
            "flags": ";".join(sorted(flags)),
        })
    return out


KEEP_PROSE = ("specialty features", "portrait display", "landscape display",
              "controls buttons under test")


def dryrun_vc(lk: Lookup) -> list[dict]:
    ws, g = v1.cells(ROOT / v1.VC)
    out = []
    for r in v1.data_rows(ws, g):
        lines = [re.sub(r"^\s*\d+\.\s*", "", x).strip()
                 for x in g(r, 10).split("\n") if x.strip()]
        proposed, flags = [], set()
        for ln in lines:
            key = " ".join(ln.lower().split()).rstrip(".")
            hit = v1.PROSE_MAP.get(key)
            if hit:
                ref, prop, flag = hit
                proposed.append(prop)
                if flag:
                    flags.add(flag)
                flags.add("PROSE_PRECOND")
            elif any(k in key for k in KEEP_PROSE):
                flags.add("PROSE_PRECOND")
                flags.add("PROSE_KEPT")          # §2.5：保留散文，移除 NO_MAPPING
                proposed.append(f"保留散文：{ln}")
            elif re.search(r"\bequipped with\b|\bconfiguration is\b", ln, re.I):
                flags.add("PROSE_PRECOND")
                flags.add("NO_MAPPING")
                proposed.append(f"NO_MAPPING: {ln}")
        out.append({
            "row": r, "tc_id": g(r, 6) or "(F 欄空)", "setting": g(r, 8) or g(r, 7),
            "alias_status": "n/a（不走 Settings List）",
            "path_now": v1.path_now_of(g, r), "path_proposed": "（本 feature 不套 path 段）",
            "control_proposed": "", "proxi_now": v1.proxi_now_of(g, r) or "（無 PROXI）",
            "proxi_proposed": " ; ".join(dict.fromkeys(proposed)),
            "flags": ";".join(sorted(flags)),
        })
    return out


CANDIDATES = "docs/fw036/handoff/down/20260902_VS-SL-02_alias_candidates.tsv"


def merge_candidates(alias: list[dict]) -> tuple[list[dict], dict[str, str]]:
    """併入 Tier 2 之 `tier2_proposal`／`tier2_evidence` 兩欄（VS-SL-02 §2.2）。

    Tier 2 之提議**不改** `match_type` —— 未經 Pei 逐條認可前不綁入查找。
    """
    import csv as _csv
    src = {r["tc_name"]: r for r in
           _csv.DictReader(open(ROOT / CANDIDATES), delimiter="\t")}
    for a in alias:
        c = src.get(a["tc_name"])
        a["tier2_proposal"] = c["tier2_proposal"] if c else ""
        a["tier2_evidence"] = c["tier2_evidence"] if c else ""
    return alias, {k: v["tier2_proposal"] for k, v in src.items()}


def main() -> int:
    lk = Lookup(ROOT)
    ws, g = v1.cells(ROOT / v1.VF230)
    names = v1.collect_names(g, v1.data_rows(ws, g))
    alias, tier2 = merge_candidates(v1.build_alias(lk, names))
    alias_by_tc = {a["tc_name"]: a for a in alias}
    cols = ["tc_name", "hmi_name", "fip_name", "match_type", "evidence",
            "tier2_proposal", "tier2_evidence"]
    (ROOT / "features/vehicle_setting/data/settings_alias.tsv").write_text(
        "\n".join(["\t".join(cols)] + ["\t".join(a[c] for c in cols) for a in alias]) + "\n",
        encoding="utf-8")

    vf, branch3 = dryrun_vf230(lk, alias_by_tc)
    v1.write_tsv(ROOT / "features/vehicle_setting/reports/vf230_settings_dryrun_v2.tsv", vf)
    v1.write_tsv(ROOT / "features/bed_lowering/reports/bl_settings_dryrun_v2.tsv", dryrun_bl(lk))
    v1.write_tsv(ROOT / "features/vehicle_category/reports/vc_settings_dryrun_v2.tsv", dryrun_vc(lk))

    # 若 Tier 2 之 manual 44 名獲認可，將解鎖之列數
    t2_manual = {k for k, v in tier2.items() if v == "manual"}
    t2_dr = {k for k, v in tier2.items() if v == "DR"}
    t2_drop = {k for k, v in tier2.items() if v == "drop"}
    unlock = sum(1 for row in vf if row["setting"] in t2_manual)
    dr_rows = sum(1 for row in vf if row["setting"] in t2_dr)
    drop_rows = sum(1 for row in vf if row["setting"] in t2_drop)

    (ROOT / "features/vehicle_setting/reports/_v2_branch3.tsv").write_text(
        "\n".join(["row\treq_id\tsetting"] +
                  [f"{b['row']}\t{b['req_id']}\t{b['setting']}" for b in branch3]) + "\n",
        encoding="utf-8")

    fc = Counter(f for r in vf for f in r["flags"].split("｜")[0].split(";") if f)
    br = Counter(r["flags"].split("｜分支 ")[1] for r in vf)
    print(f"vf230 {len(vf)} 列")
    print("  分支:", dict(br))
    print("  flags:", dict(fc))
    print(f"  (3) 之列數 = {len(branch3)}")
    print(f"  Tier2 manual {len(t2_manual)} 名 → 若認可解鎖 {unlock} 列")
    print(f"  Tier2 DR     {len(t2_dr)} 名 → {dr_rows} 列")
    print(f"  Tier2 drop   {len(t2_drop)} 名 → {drop_rows} 列")
    return 0


if __name__ == "__main__":
    sys.exit(main())
