#!/usr/bin/env python3
"""R-C45 rows — the six leaves unblocked by an approved external document.

下放包 81 §2. Five of them had NO row at all and are appended with late
tc_ids (430–434), so nothing already in the workbook renumbers (65 §1 —
same mechanism as `splits.py`). The sixth (`11.5`) already HAS a row —
`NR1L-ComfortHMI-382`, a `[BLOCKED-SPEC]` marker — and is converted in
place, keeping its id.

Why the ids are written out rather than derived from a range: R-C43. A
literal id is an identity; `max(tc_id) + 1` is a boundary, and it moves
under you the next time a batch is added.

R-C45's three obligations, and where each is met here:
  一 具名並釘版  → profile §1.1 之表（本檔只引已列表者）
  二 版本無關    → 所引者為配置條件與選項名稱，非行為
  三 spec_ref    → EXT_REF() 另列該文件之 section，不併入 Comfort stem；
                   reasoning 具名其為外部出處
"""

TC_ID_FMT = "NR1L-ComfortHMI-{n:03d}"
STEM = ("SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_"
        "(September_25_2023)")
DM = "功能測試 (Functional based ; no specific technique)"

# --- 外部出處之引用字串（R-C45 第三項：不併入 Comfort stem）-----------------
#
# 88 §4 — 引用之對象**指向會被檢查的那一份位元組**，即 `inputs/` 之副本
# （每輪受 `shasum -c`）。客戶目錄之原始出處記在括號裡：來源可考，依據可驗。
# 下列字串本身是**文件名 ＋ 其內之 section**，不含路徑；路徑之權威在
# profile §1.1 之表。改字串即改 workbook 之 N 欄，故版本名一旦寫下，
# 換版就是換依據（88 §2 判準一），不是改一行常數。
#
#   EXT_CFTS043  → inputs/SYS1_CFTS043-…Tree view_R1L-R scope.xlsx
#   EXT_POPUP    → inputs/Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023).xlsx
#                  （原始出處：客戶目錄 26PI2.5/HMI/ 之同名檔）
#   EXT_SETTINGS → inputs/HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx
#                  **換版（89 §3）**：引用原發生於客戶目錄之 SR24 Post 2A
#                  (June 15 2023)。兩版之 30／31 節經**逐格比對完全相同**
#                  （各 7 列，2026-08-17 實測），落入 88 §2 判準二之第一分支，
#                  故改引 `inputs/` 現放之 SR25 版 —— 它在 BASELINE 保護內，
#                  判準三於此即已滿足。**換版依據是量測，不是「新版比較好」。**
EXT_CFTS043 = ("SYS1_CFTS043-HVAC Controls and Displays_Tree view_R1L-R "
               "scope_NEWR1L-53677")
EXT_POPUP = "Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023)_Main"
EXT_SETTINGS = "HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026)_Settings"

# CFTS043 之逐字配置條件 —— R-C28 第一問所要之明文。
# 標 `[ext-verbatim]`（非 `spec-verbatim`）：它是外部文件之原話，
# 不是本 spec 該節之原話 —— 兩者若共用一個標籤，讀者無從分辨（R-C45）。
PC_REAR_HVAC = ("[ext-verbatim] The below requirements shall be implemented "
                "when the PROXI parameter $Rear_HVAC_cfg$ = [Present] — the "
                "vehicle is equipped with rear climate (CFTS043 NEWR1L-53677)")

_WHY_REAR = (
    "本條之可觀察量在**後排**，而「車輛是否配備後排氣候」不在 profile §3.2 "
    "之軸內 —— 批次 9／12 因此停下。**依 R-C45 解封**：其配置條件由**外部文件**"
    "承載，CFTS043 之 R1L-R scope tree view 有 48 列逐字寫 `$Rear_HVAC_cfg$ = "
    "[Present]`，其 `Scope` 欄為 `Yes`、`Radio` 欄含 `R1L, R1L-R`，"
    "故 PC 逐字引之（R-C28 第一問）。**所引者為配置之存在而非行為**"
    "（R-C45 第二項），行為仍以本 spec 之條文為驗證對象。")

EXT_LEAVES_211 = ["SWE1-HVAC-015-04", "SWE1-HVAC-015-05"]

# --- 五條新列（tc_id 明寫，非自範圍導出）-----------------------------------
EXTERNAL = {
 "SWE1-HVAC-015-04": dict(
   tc_id=TC_ID_FMT.format(n=430), parent="SWE1-HVAC-015", outline="2.11",
   test_set="Climate Modes",
   title="Fan speed and Mode adjustments alter front and rear passengers",
   item=("Adjusting Fan speed and Mode shall alter the Front and Rear "
         "passengers (C12.)"),
   proc=["1. Turn \"SYNC\" on from the climate screen",
         "2. Change the fan speed from the climate screen",
         "3. Change the airflow mode from the climate screen"],
   er=["1. The \"SYNC\" button is highlighted",
       "2. The fan speed changes for the front and the rear passengers",
       "3. The airflow mode changes for the front and the rear passengers"],
   prio="P1", ext=EXT_CFTS043, why=_WHY_REAR),

 "SWE1-HVAC-015-05": dict(
   tc_id=TC_ID_FMT.format(n=431), parent="SWE1-HVAC-015", outline="2.11",
   test_set="Climate Modes",
   title="Rear climate adjustment breaks SYNC",
   item=("Adjusting the rear fan speed, mode or temperature from the "
         "touchscreen or the rear climate controls shall break SYNC and turn "
         "it off (C12.)"),
   proc=["1. Turn \"SYNC\" on from the climate screen",
         "2. Change the rear fan speed from the rear climate controls"],
   er=["1. The \"SYNC\" button is highlighted",
       "2. The \"SYNC\" button is no longer highlighted"],
   prio="P1", ext=EXT_CFTS043, why=_WHY_REAR),

 "SWE1-HVAC-116-03": dict(
   tc_id=TC_ID_FMT.format(n=432), parent="SWE1-HVAC-116", outline="16.11",
   test_set="EMEA ICS Interface",
   title="ICS fan and mode adjustments alter front and rear passengers",
   item=("Adjusting Fan speed and Mode on the ICS shall alter the Front and "
         "Rear passengers (ICE10.)"),
   proc=["1. Turn \"SYNC\" on from the ICS climate screen",
         "2. Change the fan speed on the ICS",
         "3. Change the airflow mode on the ICS"],
   er=["1. The \"SYNC\" button is highlighted",
       "2. The fan speed changes for the front and the rear passengers",
       "3. The airflow mode changes for the front and the rear passengers"],
   prio="P1", ext=EXT_CFTS043, why=_WHY_REAR),

 "SWE1-HVAC-116-04": dict(
   tc_id=TC_ID_FMT.format(n=433), parent="SWE1-HVAC-116", outline="16.11",
   test_set="EMEA ICS Interface",
   title="Rear climate adjustment breaks SYNC on the ICS",
   item=("Adjusting the rear fan speed, mode or temperature from the "
         "touchscreen or the rear climate controls shall break SYNC and turn "
         "it off (ICE10.)"),
   proc=["1. Turn \"SYNC\" on from the ICS climate screen",
         "2. Change the rear temperature from the rear climate controls"],
   er=["1. The \"SYNC\" button is highlighted",
       "2. The \"SYNC\" button is no longer highlighted"],
   prio="P1", ext=EXT_CFTS043, why=_WHY_REAR),

 "SWE1-HVAC-083": dict(
   tc_id=TC_ID_FMT.format(n=434), parent="SWE1-HVAC-083", outline="14.1",
   test_set="HVAC Pop-ups",
   title="HVAC pop-ups follow the pop-up list",
   item=("HVAC pop-ups shall follow the pop-up list (HVACP1.)"),
   proc=["1. Select the HVAC hard key for the driver temperature",
         "2. Set the climate off using the hard key while the head unit is "
         "not on the climate screen"],
   er=["1. The temperature pop-up listed for HVAC in the pop-up list is "
       "displayed",
       "2. The Climate Comfort pop-up listed for that condition in the "
       "pop-up list is displayed"],
   prio="P2", ext=EXT_POPUP,
   why=("`14.1`（HVACP1.）之全部內容委派予「the pop-up list」，該文件此前未在"
        "素材內，故停下（其搜尋範圍只到 `inputs/` 與 `spec-index/`）。"
        "**依 R-C45 解封**：`Pop Up List HMI R1 SR24 Post 2A` 已具名列於 "
        "profile §1.1，其 `Main` 工作表載 `HVAC — Pop-up when HVAC hard key "
        "for Passenger or Driver Temperature is selected` 與 `Climate "
        "Comfort — When Climate is set Off using Hard Key and the radio is "
        "not in climate screen`，**且該列之 Logic Reference 欄回指 Comfort "
        "HMI Logic and Flow** —— 兩份文件互指，是同一組需求之兩半。"
        "所引者為 popup 之識別（版本無關），其顯示行為仍以本 spec 為對象。")),
}

# --- 11.5：既有之 BLOCKED row 就地轉換（tc_id 不變）------------------------
UNBLOCK_382 = dict(
  tc_id=TC_ID_FMT.format(n=382),
  proc=["1. Open the Auto Comfort Settings for the heated and vented seats",
        "2. Read the options offered for the driver and for the passenger"],
  er=["1. The Auto Comfort Settings are displayed",
      "2. The options listed in the HMI Settings List for Auto-On Driver and "
      "Auto-On Passenger are offered"],
  ext=EXT_SETTINGS, prio="P2",
  remarks="",
  why=("`11.5`（HVS6.）將其全部內容委派予 **HMI Settings List**，"
       "故原為 `[BLOCKED-SPEC]` 之列（R-C24 第四項：扣除委派後無餘留）。"
       "**依 R-C45 解封並移出 marker 白名單**（R-C26：白名單之移除亦須裁定，"
       "下放包 81 §2.3 即其裁定）：該文件之 SR24 版已具名列於 profile §1.1，"
       "其 `Settings` 工作表載 `30 Auto-On Driver`（`30.1 Heated Seat`／"
       "`30.2 Heated Steering Wheel`／`30.3 Vented Seat`）與 "
       "`31 Auto-On Passenger`（`31.1`／`31.2`）—— **餘留不為空**。"
       "所引者為選項之名稱（版本無關），非其行為。"
       "**引用之版本（89 §3）**：原引客戶目錄之 SR24 Post 2A (June 15 2023)，"
       "今改引 `inputs/` 之 SR25 Post R1L-R (Feb 13 2026) —— "
       "兩版之 30／31 節經逐格比對**完全相同**（各 7 列，實測），"
       "而後者在 `BASELINE.sha256` 之保護內；"
       "**換版之依據是該量測，非版本之新舊**。"
       "**`12.6` 之對造仍為 BLOCKED** —— 其委派對象 `HMI Notes` 於客戶目錄"
       "查無此件，兩條之差別自此不再是同一句話（R-C40 之前件已不成立）。"))


def _row(req_id, spec, pre_conditions, spec_ref_outlines, emea):
    """Build one complete TC row for a leaf that had none."""
    refs = "; ".join(f"{STEM}_{o}" for o in dict.fromkeys(spec_ref_outlines))
    return {
        "req_id": req_id,
        "tc_id": spec["tc_id"],
        "tc_title": spec["title"],
        "test_group": "Comfort",
        "test_set": spec["test_set"],
        "test_item": spec["item"],
        "pre_conditions": pre_conditions,
        "input_test_data": "NA",
        "test_procedure": "\n".join(spec["proc"]),
        "expected_result": "\n".join(spec["er"]),
        # R-C45 三：外部出處另列，不併入 Comfort stem
        "specification_reference": f"{refs}; {spec['ext']}",
        "priority": spec["prio"],
        "design_method": DM,
        "split_flag": False,
        "split_reason": "",
        "functional_safety": "NA",
        "estimated_test_time": "",
        "remarks": "",
        "emea_ics_review": emea,
    }


def append_external(tcs: list, parent: str, pre_conditions_for: dict,
                    emea_for: dict, extra_outlines: dict) -> list:
    """Append this parent's R-C45 rows (if any) after its existing TCs."""
    out = list(tcs)
    for req_id, spec in sorted(EXTERNAL.items()):
        if spec["parent"] != parent:
            continue
        out.append(_row(req_id, spec, pre_conditions_for[req_id],
                        extra_outlines[req_id], emea_for.get(req_id, {})))
    return out


def unblock_11_5(tc: dict) -> dict:
    """Turn `NR1L-ComfortHMI-382` from a marker row into a real TC."""
    if tc["tc_id"] != UNBLOCK_382["tc_id"]:
        return tc
    row = dict(tc)
    row["test_procedure"] = "\n".join(UNBLOCK_382["proc"])
    row["expected_result"] = "\n".join(UNBLOCK_382["er"])
    row["remarks"] = UNBLOCK_382["remarks"]
    row["priority"] = UNBLOCK_382["prio"]
    row["specification_reference"] += f"; {UNBLOCK_382['ext']}"
    return row
