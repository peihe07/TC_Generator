"""W-VF61 —— pilot #1 一次重生成（V23 §4）。

**取代 V19 版之 `vf230_pilot1.json`**（R-VF67：事故期間之產物一律重生）。
沿用檔名，不用 `batch01`。

逐項依 V23 §4.2：
  Pre-Condition            移除系統預設；menu 之開啟改為 procedure 步驟；
                           procedure ↔ ER 1:1
  priority／reasoning      依**實際所屬類別**（P0(a)／P0(c)）逐條具名，不套版
  specification_reference  R-VF68 之錨鏈 —— 037 `Source Requirement ID`
                           → 035 `Basic Report` 之「來源需求項目 ID」
  值域來源                 R-VF60 之 `0-CLAUSE`，引條文逐字片段
  tc_title                 區辨 token 為**實測值**（`Not Present` 而非 `absent`）
  LaneSenseWarning-014     A-VF18：以**結論句**為準，Remarks 具名不一致與 DR-35
"""
import csv
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
SYSRA = ("inputs/FM-WI-FSM-035-A02_VF230_HDCC_DT_STLA 技術安全需求分析報告_SYSRA "
         "STLA Technical Safety Requirement Analysis Report_SYSRA_VF230_V4_Released.xlsx")
EP = "等價劃分 (Equivalence Partitioning, EP)"

P0A = {"Power Liftgate/Tailgate Alert", "Suspension Service Mode"}
P0C = {"Blind Spot Alert", "Lane Sense Warning", "Park Sense",
       "Blind Spot with Trailer Detection"}
# P0(a)／P0(c) 之逐條理由（不套版 —— V23 §4.2、R-VF64）
WHY = {
    "Power Liftgate/Tailgate Alert":
        "P0(a) 實體致動：電動尾門之行程內可能有人；其警示設定之有無"
        "直接決定夾傷風險是否被提示",
    "Suspension Service Mode":
        "P0(a) 實體致動：維修模式之車身升降，作業者可能在車下；"
        "其設定之有無決定該模式能否被進入",
    "Blind Spot Alert":
        "P0(c) safety：其開關決定盲點警示**是否發出**；設定項不顯示即駕駛"
        "無從確認該警示之啟閉狀態",
    "Lane Sense Warning":
        "P0(c) safety：其開關決定車道偏離警示**是否發出**",
    "Park Sense":
        "P0(c) safety：其開關決定倒車／停車距離警示**是否發出**",
    "Blind Spot with Trailer Detection":
        "P0(c) safety：其決定拖車情境下盲點偵測範圍**是否延伸**；"
        "未延伸即拖車側之盲點無警示",
}

# 逐條：param（記法用）／pname（人讀）／val（實測值，用於 tc_title）／
# neg（True = 不顯示）／setting／item（條文逐字）／clause（0-CLAUSE 之逐字片段）／tag
SPEC = [
 ("SWE1-VC-PowerLiftgate/TailgateAlert-016", "Power Liftgate/Tailgate Alert",
  "CAN_Node_82_PTGM", "CAN node 82 (PTGM)", "Absent", True, "Power Tailgate Alert",
  "When the HMI receives the value Absent via signal, $CAN_Node_82_PTGM$, Then the "
  "HMI shall not display the Power Tailgate Alert customer setting in the Vehicle "
  "Settings menu.",
  "the value Absent via signal, $CAN_Node_82_PTGM$",
  "Absent partition; paired with seq 244, which covers the Present partition of "
  "the same node"),
 ("SWE1-VC-BlindSpotAlert-002", "Blind Spot Alert",
  "Blind_Spot_Monitoring", "Blind_Spot_Monitoring", "Absent", True, "Blind Spot Alert",
  "If $Blind_Spot_Monitoring$ = [Absent], the LTM or ETM shall not display the "
  "Blind Spot Alert customer setting.",
  "$Blind_Spot_Monitoring$ = [Absent]",
  "Absent partition; paired with seq 245 (Present) and distinct from seq 242, "
  "which reads Blindspot_Trailer_Detection"),
 ("SWE1-VC-LaneSenseWarning-014", "Lane Sense Warning",
  "Lane_Assist", "Lane_Assist", "Not Present", True, "Lane Sense Warning",
  "If $Lane_Assist$ = [Not Present] or [Lane Departure Warning], the LTM or ETM "
  "shall not display the Lane Sense Warning customer setting",
  "$Lane_Assist$ = [Not Present] or [Lane Departure Warning]",
  "Not-Present partition, first of the two suppressing values; paired with "
  "seq 246, which covers the two displaying values"),
 ("SWE1-VC-SuspensionServiceMode-002", "Suspension Service Mode",
  "CAN_Node_27_ASM_ASCM", "CAN node 27 (ASM / ASCM)", "Absent", True,
  "Suspension Service Mode",
  'HMI receives the value as "Absent" via signal, $CAN_Node_27(ASM / ASCM)$ Then '
  "HMI shall not display the Suspension Service Mode customer setting in the "
  "Vehicle Settings menu.",
  'the value as "Absent" via signal, $CAN_Node_27(ASM / ASCM)$',
  "Absent partition; paired with seq 247 (Present) of the same node"),
 ("SWE1-VC-Blind Spot with Trailer Detection-045", "Blind Spot with Trailer Detection",
  "Blindspot_Trailer_Detection", "Blindspot_Trailer_Detection", "Absent", True,
  "Blind Spot with Trailer Detection",
  "If Blindspot_Trailer_Detection = [Absent], the LTM or ETM shall not display the "
  "Blind Spot with Trailer Detection customer setting.",
  "Blindspot_Trailer_Detection = [Absent]",
  "Absent partition, trailer side; distinct from seq 239, which reads "
  "Blind_Spot_Monitoring"),
 ("SWE1-VC-ParkSense-084", "Park Sense",
  "CAN_Node_24_PAM_CVADAS", "CAN Node 24 (PAM/CVADAS)", "Absent", True, "Park Sense",
  "If CAN Node 24 (PAM/CVADAS) = [Absent], the LTM or ETM shall not display the "
  "Park Sense customer setting.",
  "CAN Node 24 (PAM/CVADAS) = [Absent]",
  "Absent partition; the Park Sense setting itself, not its front or rear volume "
  "settings"),
 ("SWE1-VC-PowerLiftgate/TailgateAlert-017", "Power Liftgate/Tailgate Alert",
  "CAN_Node_82_PTGM", "CAN node 82 (PTGM)", "Present", False, "Power Tailgate Alert",
  "When the HMI receives the value Present via signal, $CAN_Node_82_PTGM$, Then the "
  "HMI shall display the Power Tailgate Alert customer setting in the Vehicle "
  "Settings menu and allow the customer to modify the setting",
  "the value  Present via signal, $CAN_Node_82_PTGM$",
  "Present partition; paired with seq 238 (Absent). Modifiability is asserted as "
  "well as presence"),
 ("SWE1-VC-BlindSpotAlert-003", "Blind Spot Alert",
  "Blind_Spot_Monitoring", "Blind_Spot_Monitoring", "Present", False, "Blind Spot Alert",
  "If $Blind_Spot_Monitoring$ = [Present], the LTM or ETM shall display the Blind "
  "Spot Alert customer setting to allow the customer to modify it.",
  "$Blind_Spot_Monitoring$ = [Present]",
  "Present partition; paired with seq 239 (Absent)"),
 ("SWE1-VC-LaneSenseWarning-015", "Lane Sense Warning",
  "Lane_Assist", "Lane_Assist", "Active Lane Management", False, "Lane Sense Warning",
  "If $Lane_Assist$ = [Lane Departure Warning + Lane Keep Assist] or [Active Lane "
  "Management], the LTM or ETM shall display the Lane Sense Warning customer "
  "setting to allow the customer to modify it.",
  "$Lane_Assist$ = [Lane Departure Warning + Lane Keep Assist] or "
  "[Active Lane Management]",
  "Active-Lane-Management partition, one of the two displaying values; paired "
  "with seq 240, which covers the two suppressing values"),
 ("SWE1-VC-SuspensionServiceMode-003", "Suspension Service Mode",
  "CAN_Node_27_ASM_ASCM", "CAN node 27 (ASM / ASCM)", "Present", False,
  "Suspension Service Mode",
  'HMI receives the value as "Present" via signal, $CAN_Node_27(ASM / ASCM)$, The '
  'HMI shall display the "Suspension Service Mode" customer setting in the Vehicle '
  "Settings menu and allow the customer to modify the setting.",
  'the value as "Present" via signal, $CAN_Node_27(ASM / ASCM)$',
  "Present partition; paired with seq 241 (Absent)"),
]


def spec_refs() -> dict:
    """R-VF68 之錨鏈：037 `Source Requirement ID` → 035 之「來源需求項目 ID」。"""
    wb = openpyxl.load_workbook(ROOT / SYSRA, read_only=True, data_only=True)
    rows = list(wb["Basic Report"].iter_rows(values_only=True))
    h = rows[0]

    def col(sub):
        return next((j for j, v in enumerate(h) if sub in str(v or "")), None)

    cref, csrc = col("Sys-RA-Feature"), col("來源需求項目ID")
    out = {}
    for r in rows[1:]:
        k = str(r[cref] or "").strip()
        if k:
            out[k] = str(r[csrc] or "").strip()
    wb.close()
    return out


def main() -> None:
    lv = {r["swe_id"]: r for r in csv.DictReader(
        (ROOT / "data" / "vf230_leaves.tsv").open(encoding="utf-8"), delimiter="\t")}
    wr = {r["leaf_id"]: r for r in csv.DictReader(
        (ROOT / "docs" / "reports" / "vf230_writability.tsv").open(encoding="utf-8"),
        delimiter="\t")}
    refs = spec_refs()

    tcs = []
    for i, (leaf, l3, param, pname, val, neg, setting, item, clause, tag) in \
            enumerate(SPEC):
        seq, w = 238 + i, wr[leaf]
        src = lv[leaf]["src_ref"]
        ref = refs.get(src, "")
        if not ref:
            raise SystemExit(f"R-VF68 錨鏈斷：{leaf} 之 {src} 於 035 查無來源需求項目 ID")
        cls = "P0(a)" if l3 in P0A else "P0(c)"
        pend = "DR-34" if w["writable"] == "W1" else ""
        verb = "is not displayed" if neg else "is displayed and can be modified"
        # Pre-Condition：無系統預設、不以受測 feature 之可達性為前提（V20 §3）
        pre = ("1. The vehicle is powered and the HU has completed start-up\n"
               f"2. PROXI ${param}$ is set to \"{val}\"")
        proc = ("1. Power cycle the HU\n"
                "2. Open the Vehicle Settings menu and wait until it is fully "
                "rendered\n"
                f"3. Read the Vehicle Settings menu and check whether the "
                f"{setting} customer setting is listed"
                + ("" if neg else
                   f"\n4. Select the {setting} customer setting and change its value"))
        er = ("1. The HU completes start-up\n"
              "2. The Vehicle Settings menu is displayed\n"
              f"3. The {setting} customer setting is "
              + ("not displayed" if neg else "displayed")
              + (f" (PENDING: {pend} — the allowed values of ${param}$ are not "
                 f"in the PROXI table)" if pend else "")
              + ("" if neg else
                 f"\n4. The {setting} customer setting accepts the change and "
                 f"shows its new value"))
        remarks = []
        if leaf == "SWE1-VC-LaneSenseWarning-014":
            remarks.append(
                "A-VF18 / DR-35: the source clause is internally inconsistent — its "
                "fourth sentence names Cornering Lights feature availability while "
                "its concluding sentence acts on the Lane Sense Warning customer "
                "setting. Per V23 4.2 the concluding sentence governs; the two are "
                "not reconciled here.")
        if pend:
            remarks.append(f"PENDING {pend}: the allowed values of {param} are not "
                           f"in the PROXI table.")
        tcs.append({
            "leaf_id": leaf, "seq": seq, "test_set": w["test_set"], "layer3": l3,
            "tc_title": f"{setting} {verb} when {pname} is \"{val}\"",
            "test_item": item + "\n\n(" + tag + ")",
            "pre_conditions": pre,
            "input_test_data": "NA",
            "test_procedure": proc,
            "expected_result": er,
            "specification_reference": ref,
            "priority": "P0", "priority_class": cls,
            "design_method": EP,
            "writable": w["writable"], "dr_dependent": pend,
            "remarks": " ｜ ".join(remarks),
            "value_source": "0-CLAUSE",
            "reasoning": (f"{WHY[l3]}。"
                          f"值域來源 **0-CLAUSE**（R-VF60）—— 條文逐字："
                          f"「{clause}」。"
                          + (f"{param} 之允許值域不在 PROXI 表內，"
                             f"步驟 3 之 ER 標 PENDING：{pend}（DR-34）。"
                             if pend else "")),
        })

    out = {
        "batch": "vf230_pilot1", "line": "VF230",
        "feature": "vehicle_setting / VF230", "test_group": "Vehicle Setting",
        "handoff": "docs/handoff/V23_unblock.md", "work_order": "W-VF61",
        "supersedes": "V19 版之同名檔（R-VF67：事故期間之產物一律重生，不採用）",
        "selection": "R-VS58 之選池序，**P0 為外層分割**（R-VF64 甲案）。"
                     "池 621，取池首 10 —— 全為 P0（P0(a) 3 ／ P0(c) 7）。",
        "signal_notation": "R-1 v2：PROXI $Param$ = \"值\"；Input Test Data 為 NA",
        "spec_reference_source": "R-VF68：037 `Source Requirement ID` → 035 SYSRA "
                                 "`Basic Report` 之「來源需求項目 ID」。10/10 全解。",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "write_back": "**未寫回**（R-VF26）。`seq` 僅記於產出。",
        "b_column_start": "R-VF1（VF230 線）：238 起；本批 238–247",
        "delegation": "627 全數 `no`（W-VF46／W-VF50）",
        "tcs": tcs,
    }
    (ROOT / "generated" / "vf230_pilot1.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"寫入 generated/vf230_pilot1.json；{len(tcs)} 條，seq 238–247")
    for t in tcs:
        print(f"  {t['seq']} {t['priority_class']} {t['writable']:3} "
              f"{t['specification_reference']:26} {t['leaf_id'][:40]}")


if __name__ == "__main__":
    main()
