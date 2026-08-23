"""W-119（67 包）—— batch18，10 條 ＋ A-VS138 之 4 條更正。

池 **16**，取 **10**，餘 6。依 R-VS58 之優先序；同序內逐 Layer 2 輪流。

**held_out（4 條，具名）**：
  `OneStageHeatedSeat-040`      —— 適用性前言，W-87 之五式未涵蓋其形態（A-VS141）
  `FeaturesEnableCriteria-023`  —— 跨條文依賴（A-VS112）
  `ThreeStagesVentedSeatsManagement-070`／`-076`／`-077`／`-079` 等 —— 本輪未取，池餘

**併**：A-VS138 之 4 條已交付未更正者 —— 其為**條文本身**之訊號與所在節不符，
依 A-VS138 之處置「逐字轉錄，不更正」，**本輪之更正限於 `reasoning` 之具名**，
不動 procedure／ER 之訊號名。見上繳 37 §2。
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

DISP = {"HeatedSeatFL": "STATUS_CSWM.FL_HS_STATSts",
        "HeatedSeatFR": "STATUS_CSWM.FR_HS_STATSts",
        "VentedSeatFL": "STATUS_CSWM.FL_VS_STATSts",
        "VentedSeatFR": "STATUS_CSWM.FR_VS_STATSts"}
OBJ = {"HeatedSeatFL": "left front heated seat", "HeatedSeatFR": "right front heated seat",
       "VentedSeatFL": "left front vented seat", "VentedSeatFR": "right front vented seat"}
HS_LAB = {0: "Heated_seat_off", 1: "Heated_seat_low", 2: "Heated_seat_medium",
          3: "Heated_seat_high"}
VS_LAB = {0: "Vented_seat_off", 1: "Vented_seat_low", 2: "Vented_seat_medium",
          3: "Vented_seat_high"}
CMD_LAB = {"FR_VS_Cmd_Tlm": {0: "Vented_Seat_Off", 1: "Vented_Seat_Low",
                             2: "Vented_Seat_Medium", 3: "Vented_Seat_High"}}
RAW = {"off": 0, "low": 1, "medium": 2, "high": 3}
STAGE = {"OneStageHeatedSeat": "one heated seat state",
         "TwoStagesVentedSeatsManagement": "two vented seat states",
         "ThreeStagesVentedSeatsManagement": "three vented seat states",
         "HeatedSteeringWheelManagement": "a heated steering wheel"}

SEL = ["SWE1-VC-OneStageHeatedSeat-041", "SWE1-VC-TwoStagesVentedSeatsManagement-045",
       "SWE1-VC-OneStageHeatedSeat-046", "SWE1-VC-TwoStagesVentedSeatsManagement-052",
       "SWE1-VC-OneStageHeatedSeat-049", "SWE1-VC-TwoStagesVentedSeatsManagement-053",
       "SWE1-VC-HeatedSteeringWheelManagement-026",
       "SWE1-VC-TwoStagesVentedSeatsManagement-054",
       "SWE1-VC-OneStageHeatedSeat-050",
       "SWE1-VC-ThreeStagesVentedSeatsManagement-067"]

HELD = [
    ("SWE1-VC-OneStageHeatedSeat-040", "適用性前言 —— `Also the requirements are valid "
     "only if $Heated_Seat_Levels$ == \"One Level\"`；W-87 之五式未涵蓋 "
     "`Also the requirements are valid only if` 之形態（**A-VS141**）"),
    ("SWE1-VC-FeaturesEnableCriteria-023", "其「all other signal values」須跨條文取值"
     "（A-VS112），跨條文引入屬裁定事項"),
]


def build() -> dict:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    scr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/screen_source.tsv").open(encoding="utf-8"), delimiter="\t")}

    tcs = []
    for leaf in SEL:
        row = l2r[leaf]
        qid = re.findall(r"\d{7}", row["reqid_list"])[0]
        source = "\n".join(blocks[qid]["text"].split("\n")[1:]).strip()
        flat = re.sub(r"\s+", " ", source)
        l2, l3 = gen[leaf]["layer2"], gen[leaf]["layer3"]
        screen = scr.get(leaf, {}).get("status", "PENDING")
        fs = re.search(r"STATUS_CSWM\.(\w*Fail\w*)", flat)
        fsig = fs.group(1) if fs else None
        prio, why, dep = "P1", "P1：主要功能邏輯", "DR-25"

        if leaf.endswith("OneStageHeatedSeat-041"):          # 式 C：按壓循環
            obj, dsig = "left front heated seat", "STATUS_CSWM.FL_HS_STATSts"
            title = "One stage heated seat icon cycles off to high to off"
            lower = "(One stage configuration, press cycle)"
            proc = [f"1. Send CAN: {dsig} = 0 (Heated_seat_off)",
                    f"2. Press the {obj} icon and read the icon status",
                    f"3. Press the {obj} icon again and check that the icon status "
                    f"returns to off"]
            er = [f"1. {dsig} = 0 (Heated_seat_off) is sent",
                  "2. PENDING: DR-5-B", "3. PENDING: DR-5-B"]
            method = "狀態轉換 (State Transition Testing)"
            prio, why = "P0", "P0(b)：加熱座椅之按壓啟用"
            dep, axis = "DR-5-B", "本列為按壓循環（式 C），一階配置之 off → high → off。"
        elif leaf.endswith("OneStageHeatedSeat-046"):        # 式 S：無按壓之同步
            obj, dsig = "left front heated seat", "STATUS_CSWM.FL_HS_STATSts"
            title = "One stage heated seat icon follows status without a press"
            lower = "(One stage configuration, status change without press)"
            proc = [f"1. Send CAN: {dsig} = 0 (Heated_seat_off)",
                    f"2. Send CAN: {dsig} = 3 (Heated_seat_high) without pressing any icon",
                    f"3. Read the {obj} icon status and check that it follows the status"]
            er = [f"1. {dsig} = 0 (Heated_seat_off) is sent",
                  f"2. {dsig} = 3 (Heated_seat_high) is sent", "3. PENDING: DR-5-B"]
            method = "狀態轉換 (State Transition Testing)"
            dep, axis = "DR-5-B", "本列之觸發為狀態訊號變更而非按壓（式 S）。"
        elif leaf.endswith("HeatedSteeringWheelManagement-026"):   # 式 L：側位圖示
            title = "Left hand drive shows the heated steering wheel icon on the left"
            lower = "(Left hand drive configuration, icon side)"
            proc = ["1. Set PROXI Driver_Side = 0 (Left Side)",
                    "2. Power cycle the HU so that the configuration is applied",
                    "3. Open the Heated / Vented Seats screen and check that the "
                    "heated steering wheel icon is shown on the left side"]
            er = ["1. PROXI Driver_Side = 0 (Left Side) is accepted",
                  "2. The HU completes start-up", "3. PENDING: DR-5-B"]
            method = "等價劃分 (Equivalence Partitioning, EP)"
            dep, axis = "DR-5-B", "本列驗左駕配置下圖示之側位（式 L），來源另指 PDO graphics。"
        else:                                                # 式 D／M：解析式
            m_if = re.search(r'IF \(?\$(\w+)\$ (==|passes to) "(\w+)"', flat)
            tok, init = m_if.group(1), m_if.group(3).rsplit("_", 1)[-1]
            dsig, obj = DISP[tok], OBJ[tok]
            dlab = HS_LAB if "Heated" in tok else VS_LAB
            i_raw = RAW[init]
            m_cmd = re.search(r'set (\w+)\.(\w+) = "(\w+)"', flat)
            if m_cmd:
                msg, cmd = m_cmd.group(1), m_cmd.group(2)
                c_raw = RAW[m_cmd.group(3).rsplit("_", 1)[-1]]
                c_lab = CMD_LAB[cmd][c_raw]
                press = "passes to" not in m_if.group(2)
                title = (f"{obj.capitalize()} at {init} plus request commands "
                         f"{m_cmd.group(3).rsplit('_', 1)[-1]}" if press else
                         f"{obj.capitalize()} status change mirrors "
                         f"{m_cmd.group(3).rsplit('_', 1)[-1]} to the command")
                lower = (f"({STAGE[l3].capitalize()}, {init} plus press request)" if press
                         else f"({STAGE[l3].capitalize()}, status transition, no press)")
                step3 = ((f"3. Press the {obj} icon and check that " if press else
                          f"3. Send CAN: {dsig} = {i_raw} ({dlab[i_raw]}) without pressing "
                          f"any icon and check that ")
                         + f"{msg}.{cmd} = {c_raw} ({c_lab}) is transmitted")
                er3 = f"3. {msg}.{cmd} = {c_raw} ({c_lab}) is sent"
                method = ("決策表 (Decision Table Testing)" if press
                          else "狀態轉換 (State Transition Testing)")
                axis = (f"本列之觸發為{'按壓請求' if press else '狀態轉換'}，"
                        f"對象為 {tok}，初始階為 {init}。")
                mid = 2 if i_raw != 2 else 3
                proc = [f"1. Send CAN: STATUS_CSWM.{fsig} = 0 (Fail_Not_Present)",
                        (f"2. Send CAN: {dsig} = {i_raw} ({dlab[i_raw]})" if press else
                         f"2. Send CAN: {dsig} = {mid} ({dlab[mid]})"), step3]
                er = [f"1. STATUS_CSWM.{fsig} = 0 (Fail_Not_Present) is sent",
                      (f"2. {dsig} = {i_raw} ({dlab[i_raw]}) is sent" if press else
                       f"2. {dsig} = {mid} ({dlab[mid]}) is sent"), er3]
            else:                                            # 顯示型
                title = f"{obj.capitalize()} display follows the status change to {init}"
                lower = f"({STAGE[l3].capitalize()}, status transition, no press)"
                mid = 2 if i_raw != 2 else 3
                proc = [f"1. Send CAN: STATUS_CSWM.{fsig} = 0 (Fail_Not_Present)",
                        f"2. Send CAN: {dsig} = {mid} ({dlab[mid]})",
                        f"3. Send CAN: {dsig} = {i_raw} ({dlab[i_raw]}) and check that "
                        f"the displayed state of the {obj} changes to {init}"]
                er = [f"1. STATUS_CSWM.{fsig} = 0 (Fail_Not_Present) is sent",
                      f"2. {dsig} = {mid} ({dlab[mid]}) is sent", "3. PENDING: DR-5-B"]
                method = "狀態轉換 (State Transition Testing)"
                dep = "DR-5-B"
                axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"

        tcs.append({
            "leaf_id": leaf, "test_set": l2, "tc_title": title,
            "test_item": f"{source}\n\n{lower}",
            "pre_conditions": "\n".join([
                f"1. The vehicle is configured for {STAGE[l3]}",
                "2. The Heated / Vented Seats screen is displayed",
                "3. CAN-B is connected to the bus simulator",
                "4. The vehicle architecture is Atlantis Mid"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join(proc), "expected_result": "\n".join(er),
            "specification_reference": row["reqid_list"].replace(";", "\n"),
            "design_method": method, "priority": prio,
            "reasoning": (why + f"；畫面層依 W-115(2) 之逐 leaf 行為層對照判「{screen}」"
                          + ("，故依 R-VS59(4) 標 `PENDING: DR-5-B`"
                             if "PENDING" in "".join(er) else "")),
            "split_flag": False, "split_reason": "", "dr15_exposed": "no",
            "dr_dependent": dep, "screen_source": screen,
            "distinguishing_axis": {"axis": "trigger", "delta": axis},
        })

    return {
        "batch": "batch18", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
        "generated_round": 42, "handoff": "docs/handoff/67_round42.md",
        "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
        "selection": "池 **16**（W-114 重跑後扣已交付 129）。依 R-VS58 取 **10**，**餘 6**。"
                     "同序內逐 Layer 2 輪流（HS 4／VS 5／HSW 1）—— "
                     "**輪流不均**：池中 Heated Seat 僅 5 條而 Vented Seat 有 9 條，見上繳 37 §2。",
        "signal_notation": "R-VS52 / SWC 0708（Send CAN: MSG.Sig = raw (label)；ER … is sent）",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "revision": "W-119（42 輪）：batch18 首版",
        "held_out": [{"leaf_id": l, "reason": r} for l, r in HELD],
        "screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-5-B`（R-VS59(4)）",
        "tcs": tcs,
    }


if __name__ == "__main__":
    d = build()
    (FEAT / "generated/batch18.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch18：{len(d['tcs'])} 條")
    for tc in d["tcs"]:
        print(f"  {tc['priority']} {tc['leaf_id']:48s} {tc['tc_title'][:58]}")
    print("\nheld_out：")
    for h in d["held_out"]:
        print("  ", h["leaf_id"], "——", h["reason"][:70])
