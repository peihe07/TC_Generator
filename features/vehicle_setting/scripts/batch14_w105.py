"""W-105（60 包 §6）—— batch14，10 條，依 **R-VS58** 之優先序。

(1) 先以來源條文預判全池之 Priority，列 P0／P1／P2 三數
(2) 依 R-VS58 選 leaf：P0 優先，同序內逐 Layer 2 輪流 ＋ reqid 升冪
(3) `*_STATFailSts` 之 `Fail_Present` 類須優先納入 —— **池中命中 0**，見上繳 33 §2
(4) 預判與定稿後之判定不一致者具名

**Sibling Rows**：batch13 之 10 條與本批之 ThreeStages 各列，其來源條文逐字相同
而僅節號（`1.3.3.3.2.1` vs `1.3.3.3.3.1`）與階數配置相異 ——
故 pre_conditions **須逐條指明階數配置**，否則二者不可分辨。
本批依此撰寫；batch13 之同一缺陷另產 `batch13_v2`（見 `sibling_fix_w105.py`）。
"""
from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from inscope_w39 import blocks_with_sec  # noqa: E402

FEAT = Path(__file__).resolve().parents[1]

DISP = {"FL_HS": "STATUS_CSWM.FL_HS_STATSts", "FR_HS": "STATUS_CSWM.FR_HS_STATSts",
        "FL_VS": "STATUS_CSWM.FL_VS_STATSts"}
FAIL = {"FL_HS": "STATUS_CSWM.FL_HS_STATFailSts", "FR_HS": "STATUS_CSWM.FR_HS_STATFailSts",
        "FL_VS": "STATUS_CSWM.FL_VS_STATFailSts"}
HS_LAB = {0: "Heated_seat_off", 1: "Heated_seat_low", 2: "Heated_seat_medium",
          3: "Heated_seat_high"}
VS_LAB = {0: "Vented_seat_off", 1: "Vented_seat_low", 2: "Vented_seat_medium",
          3: "Vented_seat_high"}
# 命令訊號之標籤取 LID `Atlantis` 欄組逐字（R-VS57 之 WARN 類）
CMD_LAB = {"FL_HS_Cmd_Tlm": HS_LAB, "FR_HS_Cmd_Tlm": HS_LAB,
           "FL_VS_Cmd_Tlm": {0: "Vented_Seat_Off", 1: "Vented_Seat_Low",
                             2: "Vented_Seat_Medium", 3: "Vented_Seat_High"}}
LEVEL = {"off": 0, "low": 1, "medium": 2, "high": 3}

# (leaf, layer2, 階數配置, 式, 側, 初始階, 命令訊號, 命令訊息, 命令階, 預判 Priority)
SEL = [
    # ── 第一序：R-VS56 之 P0(b)（加熱元件之啟用 —— 自 off 起）──────────
    ("SWE1-VC-TwoStagesHeatedSeat-061", "Heated Seat", "two", "A", "FR_HS", "off",
     "FR_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "high", "P0"),
    ("SWE1-VC-ThreeStagesHeatedSeat-081", "Heated Seat", "three", "A", "FL_HS", "off",
     "FL_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "high", "P0"),
    ("SWE1-VC-ThreeStagesHeatedSeat-085", "Heated Seat", "three", "A", "FR_HS", "off",
     "FR_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "high", "P0"),
    # ── 第二序：P1，逐 Layer 2 輪流 ＋ reqid 升冪 ──────────────────────
    ("SWE1-VC-ThreeStagesVentedSeatsManagement-063", "Vented Seat", "three", "A", "FL_VS",
     "off", "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "high", "P1"),
    ("SWE1-VC-TwoStagesHeatedSeat-062", "Heated Seat", "two", "A", "FR_HS", "high",
     "FR_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "low", "P1"),
    ("SWE1-VC-ThreeStagesVentedSeatsManagement-066", "Vented Seat", "three", "A", "FL_VS",
     "low", "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "off", "P1"),
    ("SWE1-VC-TwoStagesHeatedSeat-063", "Heated Seat", "two", "A", "FR_HS", "low",
     "FR_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "off", "P1"),
    ("SWE1-VC-ThreeStagesVentedSeatsManagement-072", "Vented Seat", "three", "B", "FL_VS",
     "off", "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "off", "P1"),
    ("SWE1-VC-TwoStagesHeatedSeat-069", "Heated Seat", "two", "B", "FL_HS", "high",
     "FL_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "high", "P1"),
    ("SWE1-VC-ThreeStagesVentedSeatsManagement-073", "Vented Seat", "three", "B", "FL_VS",
     "low", "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "low", "P1"),
]

STAGE_PRE = {("Heated Seat", "two"): "The vehicle is configured for two heated seat states",
             ("Heated Seat", "three"): "The vehicle is configured for three heated seat states",
             ("Vented Seat", "three"): "The vehicle is configured for three vented seat states"}
SIDE_WORD = {"FL_HS": "left front heated seat", "FR_HS": "right front heated seat",
             "FL_VS": "left front vented seat"}


def build() -> dict:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    tcs, mismatch = [], []
    for leaf, l2, stage, form, side, init, cmd, msg, cmd_lvl, pre_p in SEL:
        row = l2r[leaf]
        qid = re.findall(r"\d{7}", row["reqid_list"])[0]
        source = "\n".join(blocks[qid]["text"].split("\n")[1:]).strip()
        dsig, fsig = DISP[side], FAIL[side]
        dlab = HS_LAB if side.endswith("HS") else VS_LAB
        i_raw, c_raw = LEVEL[init], LEVEL[cmd_lvl]
        i_lab, c_lab = dlab[i_raw], CMD_LAB[cmd][c_raw]
        obj = SIDE_WORD[side]

        # 定稿後之判定（R-VS56）：P0(b) 限加熱元件自 off 起之啟用
        final_p = "P0" if (l2 == "Heated Seat" and form == "A" and init == "off") else "P1"
        why = ("P0(b)：加熱座椅之按壓啟用" if final_p == "P0" else "P1：主要功能邏輯")
        if final_p != pre_p:
            mismatch.append((leaf, pre_p, final_p))

        if form == "A":
            title = f"{obj.capitalize()} at {init} plus request commands {cmd_lvl}"
            lower = f"({stage.capitalize()} stage configuration, {init} plus press request)"
            proc = [f"1. Send CAN: {fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: {dsig} = {i_raw} ({i_lab})",
                    f"3. Press the {obj} icon and check that "
                    f"{msg}.{cmd} = {c_raw} ({c_lab}) is transmitted"]
            er = [f"1. {fsig} = 0 (Fail_Not_Present) is sent",
                  f"2. {dsig} = {i_raw} ({i_lab}) is sent",
                  f"3. {msg}.{cmd} = {c_raw} ({c_lab}) is sent"]
            method = "決策表 (Decision Table Testing)"
            delta = (f"本列之階數配置為{stage}、側為 {side}、初始階為 {init}，"
                     f"觸發為按壓請求（`4859508` 之 `or` 並列，60 包 §1）。")
        else:
            mid_raw = 2 if i_raw != 2 else 3
            title = f"{obj.capitalize()} status change mirrors {cmd_lvl} to the command"
            lower = f"({stage.capitalize()} stage configuration, status transition, no press)"
            proc = [f"1. Send CAN: {fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: {dsig} = {mid_raw} ({dlab[mid_raw]})",
                    f"3. Send CAN: {dsig} = {i_raw} ({i_lab}) without pressing any icon and "
                    f"check that {msg}.{cmd} = {c_raw} ({c_lab}) is transmitted"]
            er = [f"1. {fsig} = 0 (Fail_Not_Present) is sent",
                  f"2. {dsig} = {mid_raw} ({dlab[mid_raw]}) is sent",
                  f"3. {msg}.{cmd} = {c_raw} ({c_lab}) is sent"]
            method = "狀態轉換 (State Transition Testing)"
            delta = (f"本列之階數配置為{stage}、側為 {side}，"
                     f"觸發為顯示值之轉換（`passes to`），無按壓。")

        tcs.append({
            "leaf_id": leaf, "test_set": l2, "tc_title": title,
            "test_item": f"{source}\n\n{lower}",
            "pre_conditions": "\n".join([
                f"1. {STAGE_PRE[(l2, stage)]}",
                "2. The Heated / Vented Seats screen is displayed",
                "3. CAN-B is connected to the bus simulator",
                "4. The vehicle architecture is Atlantis Mid"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join(proc),
            "expected_result": "\n".join(er),
            "specification_reference": row["reqid_list"].replace(";", "\n"),
            "design_method": method, "priority": final_p, "reasoning": why,
            "priority_prejudged": pre_p,
            "split_flag": False, "split_reason": "", "dr15_exposed": "no",
            "dr_dependent": "DR-25",
            "distinguishing_axis": {"axis": "configuration", "delta": delta},
        })
    return {
        "batch": "batch14", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
        "generated_round": 37, "handoff": "docs/handoff/60_review_round36.md",
        "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
        "selection": "依 R-VS58：預判 P0 3／P1 20／P2 1（池 24，含 A-VS112 之 1）。"
                     "第一序取 P0 全 3 條（皆 Heated Seat，同序內 reqid 升冪）；"
                     "第二序 P1 逐 Layer 2 輪流取 7（Vented Seat 4／Heated Seat 3）。"
                     "**`Fail_Present` 類於池中命中 0** —— 全 16 條皆 `delegate = blocked`，見上繳 33 §2.1",
        "signal_notation": "R-VS52 / SWC 0708（Send CAN: MSG.Sig = raw (label)；ER … is sent）",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "revision": "W-105（37 輪）：batch14 首版",
        "priority_prejudge_mismatch": mismatch,
        "dr_dependency": "全 10 條之命令訊號依 R-VS57 判 L-VS2 WARN，標 `dr_dependent = DR-25`（→ DR-25′）。",
        "reasoning": "`DrvSeatHeating.Req`／`PsngrSeatHeating.Req` 以按壓表述，"
                     "依 60 包 §1 之裁定（`4859508` 之 `or` 並列自證），非推論。"
                     "Sibling Rows：本批 ThreeStages 各列與 batch13 之 TwoStages 各列"
                     "來源條文逐字相同，**以 pre_conditions 之階數配置分辨**。",
        "tcs": tcs,
    }


if __name__ == "__main__":
    d = build()
    (FEAT / "generated/batch14.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch14：{len(d['tcs'])} 條")
    for tc in d["tcs"]:
        print(f"  {tc['priority']} (預判 {tc['priority_prejudged']}) "
              f"{tc['leaf_id']:46s} {tc['tc_title']}")
    print(f"\n預判與定稿不一致：{d['priority_prejudge_mismatch']}")
