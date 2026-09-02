#!/usr/bin/env python3
"""VS-SL-04 §1 —— 對 v3 (3) 分支 105 列之二次查找。

依 `down/20260902_VS-SL-03_review.md` §2 之 R1／R2／R3；本層另加一值 **R1b**
（見下），並於上繳具名回報。

  R1   家族閘 —— 設定名自身無总控表列，但其家族列為變體數閘。
       实测 No.267 `AUX SWITCH Type`：
         `If AUX_Switch_Types is [Type1]), return value is 4.
          Else if AUX_Switch_Types is [Type2]), return value is 6. Else 0.`
       故 `SWITCH 1–4` 取 `= 1 (Type 1)`、`SWITCH 5–6` 取 `= 2 (Type 2)`；
       label 依 `_vf230_proxi_values.json` 逐字（`Type 1` 含空格），非 FIP 文面之 `Type1`。

  R1b  **本層新增**：FIP 列存在且條件明確，惟 v3 之條件式解析器抽不出 term
       （形制為 `is "Present"` 之引號式而非中括號式），故 v3 誤判為「兩來源皆空」。
       證據充分者於此補值；**不足者一律落 R3，不猜**。

  R2   FIP 列存在但為常數 → 不加 PROXI 行、不 PENDING、掛登記旗。
         `FIP_ALWAYS_OFF`：`Always false`／`Always return value is 0`
         `FIP_ALWAYS_ON` ：`Always true`（恆顯示，本無條件可加）

  R3   維持 `PENDING`，供 DR 第四節。三種成因分記於 `subcase`。
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
import vs_sl03_bind as bind  # noqa: E402
from settings_lookup import resolve_raw  # noqa: E402

warnings.filterwarnings("ignore")
ROOT = v1.ROOT
BRANCH3 = "features/vehicle_setting/reports/_v3_branch3.tsv"
OUT = "features/vehicle_setting/reports/_v4_branch3_resolution.tsv"

SWITCH_RE = re.compile(r"^SWITCH ([1-6]) ")
CONST_OFF = re.compile(r"^alwa\w*\s+(false|return value is\s*0)\s*$", re.I)
CONST_ON = re.compile(r"^alwa\w*\s+true\s*$", re.I)
NEGATED = re.compile(r"\bis\s+not\b", re.I)
QUOTED_TERM = re.compile(r'"([A-Za-z][A-Za-z0-9_]*)"\s+is\s+"([^"]+)"')

FAMILY_NO = "267"
FAMILY_PARAM = "AUX_Switch_Types"
# 審閱 §2 R2 明指之二列。`Phone Repetition` 之 FIP 名為 `Phone Information on Cluster`
# —— 與設定名不同字，其綁定來自審閱之裁示而非該名自身之 tier2_evidence。
REVIEW_FIP = {"Suspension Default Ride Height": "274", "Phone Repetition": "215"}

COLUMNS = ["row", "tc_id", "setting", "resolution", "subcase", "proxi_added", "evidence"]


def fip_row(lk, bound: dict, name: str):
    """該設定名之 FIP 列：綁定 > 審閱明指 > 以名查。回 (rec, 來源說明)。"""
    b = bound.get(name)
    if b and b["fip_no"]:
        rec = [x for x in lk.atlantis if x["no"] == b["fip_no"]]
        if rec:
            return rec[0], f"別名 evidence 指 No.{b['fip_no']}"
    if name in REVIEW_FIP:
        rec = [x for x in lk.atlantis if x["no"] == REVIEW_FIP[name]]
        if rec:
            return rec[0], f"審閱 §2 R2 明指 No.{REVIEW_FIP[name]}"
    rec = lk.atlantis_rows(name)
    if rec:
        return rec[0], f"以設定名逐字查得 No.{rec[0]['no']}"
    return None, ""


def hmi_state(lk, bound: dict, alias: dict, name: str) -> str:
    """該名於 HMI Settings List 之現況（供 DR 據實書寫，不得以「兩表皆無」一語帶過）。"""
    b = bound.get(name)
    if b and b["item"]:
        it = b["item"]
        return f"HMI 已綁 Settings r{it['row']}（{it['category']} > {it['name_plain']}）"
    a = alias.get(name, {})
    if a.get("hmi_name"):
        rows = [str(x["row"]) for x in lk.hmi_rows(a["hmi_name"])]
        return f"HMI 逐字命中 {a['hmi_name']!r}（Settings r{'/'.join(rows)}）"
    return "HMI Settings List 517 項逐字比對零命中"


def classify(lk, bound: dict, alias: dict, name: str) -> dict:
    m = SWITCH_RE.match(name)
    if m:
        n = int(m.group(1))
        label = "Type 1" if n <= 4 else "Type 2"
        raw, lab = resolve_raw(lk.values, FAMILY_PARAM, label)
        return {"resolution": "R1", "subcase": "FAMILY_GATE",
                "proxi_added": f"PROXI {FAMILY_PARAM} = {raw} ({lab})",
                "evidence": (f"总控表 No.{FAMILY_NO} AUX SWITCH Type（Type1→4／Type2→6）；"
                             f"proxi_values['{FAMILY_PARAM}']['{raw}'] = '{lab}'")}

    rec, src = fip_row(lk, bound, name)
    if rec is None:
        hmi = hmi_state(lk, bound, alias, name)
        both = hmi.startswith("HMI Settings List")
        return {"resolution": "R3",
                "subcase": "NO_MATCH_EITHER" if both else "NO_FIP_ROW",
                "proxi_added": "",
                "evidence": f"{hmi}；总控表 278 列逐字比對零命中"}

    expr = " ".join(rec["expr"].split())
    if CONST_OFF.match(expr):
        return {"resolution": "R2", "subcase": "FIP_ALWAYS_OFF", "proxi_added": "",
                "evidence": f"{src}；Atlantis 逐字 `{expr}`"}
    if CONST_ON.match(expr):
        return {"resolution": "R2", "subcase": "FIP_ALWAYS_ON", "proxi_added": "",
                "evidence": f"{src}；Atlantis 逐字 `{expr}`（恆顯示，無條件可加）"}
    if NEGATED.search(expr):
        return {"resolution": "R3", "subcase": "NEGATED_CONDITION", "proxi_added": "",
                "evidence": (f"{src}；Atlantis 逐字 `{expr[:90]}` —— 否定式，"
                             "其補集之應取值本層無據，不猜")}

    q = QUOTED_TERM.search(expr)
    if q:
        param, label = q.group(1), q.group(2)
        raw, lab = resolve_raw(lk.values, param, label)
        if raw is not None:
            return {"resolution": "R1b", "subcase": "PARSER_GAP_FIXED",
                    "proxi_added": f"PROXI {param} = {raw} ({lab})",
                    "evidence": (f"{src}；Atlantis 逐字 `{expr[:80]}`（引號式，v3 解析器漏抽）；"
                                 f"proxi_values['{param}']['{raw}'] = '{lab}'")}

    br = re.search(r"([A-Za-z][A-Za-z0-9_À-ɏ]*)\s+is\s+\[([^\]]+)\]", expr)
    if br:
        param, label = br.group(1), br.group(2)
        raw, lab = resolve_raw(lk.values, param, label)
        if raw is not None:
            return {"resolution": "R1b", "subcase": "PARSER_GAP_FIXED",
                    "proxi_added": f"PROXI {param} = {raw} ({lab})",
                    "evidence": (f"{src}；Atlantis 逐字 `{expr[:80]}`；"
                                 f"proxi_values['{param}']['{raw}'] = '{lab}'")}
        return {"resolution": "R3", "subcase": "FIP_PARAM_NOT_IN_VALUES",
                "proxi_added": "",
                "evidence": (f"{src}；Atlantis 逐字 `{expr[:80]}`；"
                             f"`{param}` 於 proxi_values 查無（近似鍵存在與否見上繳 §5），"
                             "依 R-13 不代入")}

    return {"resolution": "R3", "subcase": "UNPARSED_CONDITION", "proxi_added": "",
            "evidence": f"{src}；Atlantis 逐字 `{expr[:90]}` —— 本層無法確判，不猜"}


def main() -> int:
    lk, bound = bind.build(ROOT)
    alias = {r["tc_name"]: r for r in csv.DictReader(
        open(ROOT / "features/vehicle_setting/data/settings_alias.tsv"), delimiter="\t")}
    rows = list(csv.DictReader(open(ROOT / BRANCH3), delimiter="\t"))
    ws, g = v1.cells(ROOT / v1.VF230)

    out = []
    for r in rows:
        res = classify(lk, bound, alias, r["setting"])
        out.append({"row": r["row"],
                    "tc_id": g(int(r["row"]), 6) or "(F 欄空)",
                    "setting": r["setting"], **res})

    p = ROOT / OUT
    with open(p, "w", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=COLUMNS, delimiter="\t")
        w.writeheader()
        w.writerows(out)

    c = Counter(x["resolution"] for x in out)
    sub = Counter(x["subcase"] for x in out)
    total = sum(c.values())
    assert total == 105, f"合計 {total} ≠ 105"
    r1 = [x for x in out if x["resolution"] == "R1"]
    assert len(r1) == 54, f"R1 為 {len(r1)} 列，非 54"
    assert all(x["proxi_added"] for x in r1), "R1 有列未帶 proxi_added"
    assert all(x["proxi_added"] for x in out if x["resolution"] == "R1b")

    print(f"105 列之判：{dict(c)}  （assert 合計 = 105 PASS）")
    print("subcase:", dict(sub))
    for k in ("R1", "R1b", "R2", "R3"):
        names = sorted({x["setting"] for x in out if x["resolution"] == k})
        print(f"  {k:<4} {c.get(k, 0):>3} 列 / {len(names):>2} 名")
    return 0


if __name__ == "__main__":
    sys.exit(main())
