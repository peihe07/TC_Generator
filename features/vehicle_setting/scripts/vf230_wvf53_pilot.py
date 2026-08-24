"""W-VF53 —— VF230 pilot 批（第 1 批，10 條）之生成。

依 V19 §5：
  - 範圍：R-VS58 選池序之池首 10 條（修正後全為 P0，見 A-VF17）
  - 寫回仍凍結（R-VF26）—— 產出落 `generated/`，不進工作簿
  - 訊號記法依 R-1 v2（V19 §5.3 二）：`PROXI $Param$ = "值"`／
    Input Test Data 為 `NA`
  - `not clear` 之 leaf 依 R-VF15 於 Remarks 逐字轉錄
  - W1 標 `PENDING: DR-34`
  - 每條之 `reasoning` 具名其值域來源（R-VF13 之鏈序）

輸出：generated/vf230_batch01.json
"""
import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC_REF_SRC = ("inputs/FM-WI-FSM-035-A02_VF230_HDCC_DT_STLA 技術安全需求分析報告"
                "_SYSRA STLA Technical Safety Requirement Analysis Report_SYSRA"
                "_VF230_V4_Released.xlsx")
EP = "等價劃分 (Equivalence Partitioning, EP)"

# 逐 leaf 之書寫參數。**每一欄之值皆取自 037 條文逐字**，不外加。
#   param      —— PROXI 參數名，逐字取自條文
#   absent/present —— 條文所列之值，逐字（含方括號內之字面）
#   setting    —— 條文所稱之 customer setting 名，逐字
#   axis       —— 手足之區辨軸（V19 §5.3 一：test_item 括號下半）
SPEC = {
 "SWE1-VC-PowerLiftgate/TailgateAlert-016": dict(
    param="CAN_Node_82_PTGM", val="Absent", shows=False,
    setting="Power Tailgate Alert",
    sib="Absent -> the setting is absent from the menu"),
 "SWE1-VC-PowerLiftgate/TailgateAlert-017": dict(
    param="CAN_Node_82_PTGM", val="Present", shows=True,
    setting="Power Tailgate Alert",
    sib="Present -> the setting is listed and modifiable"),
 "SWE1-VC-BlindSpotAlert-002": dict(
    param="Blind_Spot_Monitoring", val="Absent", shows=False,
    setting="Blind Spot Alert",
    sib="Absent -> the setting is absent from the menu"),
 "SWE1-VC-BlindSpotAlert-003": dict(
    param="Blind_Spot_Monitoring", val="Present", shows=True,
    setting="Blind Spot Alert",
    sib="Present -> the setting is listed and modifiable"),
 "SWE1-VC-LaneSenseWarning-014": dict(
    param="Lane_Assist", val="Not Present", shows=False,
    setting="Lane Sense Warning",
    alt="Lane Departure Warning",
    sib="Not Present / Lane Departure Warning -> the setting is absent"),
 "SWE1-VC-LaneSenseWarning-015": dict(
    param="Lane_Assist", val="Lane Departure Warning + Lane Keep Assist",
    shows=True, setting="Lane Sense Warning",
    alt="Active Lane Management",
    sib="LDW + LKA / Active Lane Management -> the setting is listed and modifiable"),
 "SWE1-VC-SuspensionServiceMode-002": dict(
    param="CAN_Node_27(ASM / ASCM)", val="Absent", shows=False,
    setting="Suspension Service Mode",
    sib="Absent -> the setting is absent from the menu"),
 "SWE1-VC-SuspensionServiceMode-003": dict(
    param="CAN_Node_27(ASM / ASCM)", val="Present", shows=True,
    setting="Suspension Service Mode",
    sib="Present -> the setting is listed and modifiable"),
 "SWE1-VC-Blind Spot with Trailer Detection-045": dict(
    param="Blindspot_Trailer_Detection", val="Absent", shows=False,
    setting="Blind Spot with Trailer Detection",
    sib="Absent -> the setting is absent from the menu"),
 "SWE1-VC-ParkSense-084": dict(
    param="CAN Node 24 (PAM/CVADAS)", val="Absent", shows=False,
    setting="Park Sense",
    sib="Absent -> the setting is absent from the menu"),
}


def build(leaf, s, wr, lv, specref, notclear):
    param, val, setting = s["param"], s["val"], s["setting"]
    shows, alt = s["shows"], s.get("alt")
    pending = wr["writable"] == "W1"
    dr = wr["dr_id"]

    # --- pre-conditions（R-1 v2：`PROXI $Param$ = "值"`）---
    pv = f'PROXI ${param}$ = "{val}"'
    if pending:
        pv += f" (PENDING: {dr})"
    pre = [f"1. {pv}",
           "2. The head unit has completed start-up after the PROXI "
           "configuration above was applied",
           "3. The LTM or ETM is the display under test"]
    if alt:
        pre.append(f'4. The equivalence class under test is represented by '
                   f'"{val}"; the other member of the same class is "{alt}"')

    # --- procedure / ER ---
    proc = ["1. Open the Vehicle Settings menu on the LTM or ETM",
            f"2. Check whether the {setting} customer setting is listed in the "
            "Vehicle Settings menu"]
    er = ["1. The Vehicle Settings menu is displayed",
          f"2. The {setting} customer setting is "
          + ("listed in the Vehicle Settings menu" if shows
             else "not listed in the Vehicle Settings menu")]
    if shows:
        proc.append(f"3. Select the {setting} customer setting and change it to "
                    "its other value")
        er.append(f"3. The {setting} customer setting accepts the change and "
                  "shows the changed value")

    # --- test_item：條文之條件→結果 ＋ 括號下半（區辨軸）---
    cond = f'If ${param}$ = [{val}]' + (f' or [{alt}]' if alt else '')
    body = (f"{cond}, the LTM or ETM shall "
            + ("display" if shows else "not display")
            + f" the {setting} customer setting"
            + (" to allow the customer to modify the setting." if shows else "."))
    item = f"{body}\n\n({s['sib']})"

    # --- reasoning：值域來源具名（R-VF13 鏈序 LID → DBC → PROXI → VC/VM）---
    reason = (f"P0（R-VF57 P0(c) safety／P0(a) 實體致動）—— 其開關決定該功能之"
              f"客戶設定是否存在，設定不存在即無從開啟。**值域來源：PROXI** —— "
              f"`{param}` 之值 `{val}` 逐字取自 037 條文之列舉，"
              f"非 LID、非 DBC、非 VC/VM。"
              f"**形態：可用性（availability）** —— 觸發為 PROXI 組態，"
              f"標的為 Vehicle Settings 選單中該設定之有無。"
              f"**設計方法 EP** —— PROXI 值域分為「顯示」與「不顯示」兩等價類，"
              f"每類取一代表值。")
    if alt:
        reason += (f" 本條之等價類含兩個列舉值（`{val}`／`{alt}`），"
                   f"取前者為代表值，後者具名於 pre-condition 4。")
    if pending:
        reason += (f" **{dr} 未覆**：`{param}` 之值編碼未確認，"
                   f"故其 pre-condition 標 `PENDING: {dr}`。")

    rm = []
    if pending:
        rm.append(f"PENDING: {dr} —— PROXI `{param}` 之值編碼待覆")
    if notclear:
        rm.append(f"Upstream Verification Criteria: {notclear}")
    if leaf == "SWE1-VC-LaneSenseWarning-014":
        rm.append("A-VF18 —— 條文內部不一致：其第 4 句稱評估 Lane_Assist 以決定 "
                  "`Cornering Lights` feature availability，而其結論句處置之對象為 "
                  "`Lane Sense Warning` customer setting。本 TC 依**結論句**書寫"
                  "（結論句為可觀察之結果），該不一致逐字登記")

    return {
        "leaf_id": leaf,
        "test_set": wr["test_set"],
        "tc_title": (f"{setting} setting "
                     + ("shown" if shows else "hidden")
                     + f" when {param} is {val}"),
        "test_item": item,
        "pre_conditions": "\n".join(pre),
        "input_test_data": "NA",
        "test_procedure": "\n".join(proc),
        "expected_result": "\n".join(er),
        "specification_reference": specref,
        "design_method": EP,
        "priority": "P0",
        "reasoning": reason,
        "form": "可用性型（PROXI → customer setting 之有無）",
        "value_source": "PROXI",
        "writable": wr["writable"],
        "dr_dependent": dr or "",
        "screen_pending": "no",
        "distinguishing_axis": {"axis": "PROXI value class", "delta": s["sib"]},
        "remarks": "; ".join(rm),
    }


def main() -> None:
    import openpyxl
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (ROOT / "docs" / "reports" / "vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    pool = json.loads((ROOT / "data" / "_vf230_priority.json")
                      .read_text(encoding="utf-8"))["pool"][:10]

    ws = openpyxl.load_workbook(ROOT / SPEC_REF_SRC, data_only=True,
                                read_only=True)["Basic Report"]
    sysra = {}
    for row in ws.iter_rows(min_row=2, values_only=True):
        if row and row[1]:
            sysra[str(row[1]).strip()] = str(row[4]).strip() if row[4] else ""

    # R-VF15 之逐字轉錄來源（037 之 VC 欄），只對 vcvm_not_clear == "1" 者
    NOTCLEAR = {
        "SWE1-VC-Blind Spot with Trailer Detection-045":
            "Scenario of checking PROXI parameter is not clear",
        "SWE1-VC-ParkSense-084":
            "Scenario of receiving signal is not clear",
    }

    tcs = []
    for leaf in pool:
        sr = sysra.get(lv[leaf]["src_ref"], "")
        if not sr:
            raise SystemExit(f"spec_reference 未解：{leaf}，停")
        tcs.append(build(leaf, SPEC[leaf], wr[leaf], lv[leaf], sr,
                         NOTCLEAR.get(leaf) if wr[leaf]["vcvm_not_clear"] == "1"
                         else None))

    # --- 自檢（V19 §5.3 之六項升級條件，逐項機器檢查）---
    fails = []
    for t in tcs:
        if "(" not in t["test_item"].split("\n")[-1]:
            fails.append((t["leaf_id"], "1 test_item 缺括號下半"))
        if t["input_test_data"] != "NA":
            fails.append((t["leaf_id"], "2 Input Test Data 非 NA"))
        for f in ("pre_conditions", "test_procedure", "expected_result",
                  "specification_reference", "design_method"):
            if not str(t[f]).strip():
                fails.append((t["leaf_id"], f"3 空欄：{f}"))
        if "NA" in t["expected_result"]:
            fails.append((t["leaf_id"], "3 ER 以 NA 充當未知"))
        if not re.fullmatch(r"VF230_V1_(PHDCC27|PDT27)_VF_\d+",
                            t["specification_reference"]):
            fails.append((t["leaf_id"], "4 spec_ref 格式"))
        if t["test_set"] not in {
                "Trailer and Signage", "Auxiliary Switches", "Driver Convenience",
                "Suspension and Comfort", "Units and Cameras",
                "Approach and Tailgate", "Lane and Lighting", "Measurement Units",
                "Daytime Lighting"}:
            fails.append((t["leaf_id"], "5 Test Set 不在已鎖 9 名內"))
        if "Vehicle Settings menu" not in t["test_procedure"]:
            fails.append((t["leaf_id"], "6 畫面層敘述無素材來源可指"))
    print("=== V19 §5.3 六項升級條件之自檢 ===")
    for l, m in fails:
        print(f"  ❌ {l}: {m}")
    print(f"  {'全部通過 ✅' if not fails else f'{len(fails)} 項未過'}")

    # 步驟數與 ER 步數一致（canon）
    for t in tcs:
        np_ = len([x for x in t["test_procedure"].split("\n") if x.strip()])
        ne = len([x for x in t["expected_result"].split("\n") if x.strip()])
        if np_ != ne:
            raise SystemExit(f"步數不一致 {t['leaf_id']}: {np_} vs {ne}")

    out = {
        "batch": "vf230_batch01",
        "line": "VF230 (Part 2)",
        "feature": "vehicle_setting",
        "test_group": "Vehicle Setting",
        "handoff": "docs/handoff/V19_pilot_start.md",
        "work_order": "W-VF53（pilot 批，本輪唯一生成工單）",
        "selection": ("R-VS58 選池序之池首 10 條。**選池序經 A-VF17 修正** —— "
                      "修正前池首為 6 P0 ＋ 4 P1，修正後 10 條全為 P0。"),
        "signal_notation": "R-1 v2（V19 §5.3 二）；SWC 0708 為風格權威",
        "spec_reference_source": ("R-VS33′ 之錨鏈，末端來源以 SYSRA "
                                  "`Basic Report` 之 `SYS2 來源需求項目ID` 代 SYS2 "
                                  "（DR-28 缺件，A-VS134 已認可其為同型來源）"),
        "design_method_domain": "VF230 交付本 `下拉選單` 分頁，9 值",
        "write_back": "凍結（R-VF26）—— 本批不進工作簿",
        "b_column_start": 238,
        "tcs": tcs,
    }
    p = ROOT / "generated" / "vf230_batch01.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nwrote {p}  ({len(tcs)} TC)")


if __name__ == "__main__":
    main()
