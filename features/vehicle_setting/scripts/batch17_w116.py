"""W-116（64 包 §5）—— batch17，10 條。

自 W-114 重跑後之池（**26**）依 R-VS58 之優先序選取：
  第一序  `Fail_Present` 類 6 條（R-VS56 之 P0(b) 標的）
  第二序  P1，逐 Layer 2 輪流 ＋ reqid 升冪

畫面層依 **W-115(2) 之新對照表**（逐 leaf 行為層）；
查無者依 R-VS59(4) 標 `PENDING`。

**兩式**：
  式 F  失效 —— `IF <FailSts> passes to "Fail_Present" … icon shall change`
        ／`IF (<Req> … AND <FailSts> == "Fail_Present") THEN … popup`
  式 D  顯示／命令 —— `IF ($<disp>$ (==|passes to) "<階>" AND <FailSts> ==
        "Fail_Not_Present" [AND <Req> …]) THEN …`
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
OBJ_OF_FAIL = {"FL_HS_STATFailSts": "left front heated seat",
               "FR_HS_STATFailSts": "right front heated seat",
               "FL_VS_STATFailSts": "left front vented seat",
               "FR_VS_STATFailSts": "right front vented seat",
               "HSW_StatFailSts": "heated steering wheel"}
HS_LAB = {0: "Heated_seat_off", 1: "Heated_seat_low", 2: "Heated_seat_medium",
          3: "Heated_seat_high"}
VS_LAB = {0: "Vented_seat_off", 1: "Vented_seat_low", 2: "Vented_seat_medium",
          3: "Vented_seat_high"}
CMD_LAB = {"FR_VS_Cmd_Tlm": {0: "Vented_Seat_Off", 1: "Vented_Seat_Low",
                             2: "Vented_Seat_Medium", 3: "Vented_Seat_High"}}
RAW = {"off": 0, "low": 1, "medium": 2, "high": 3}
STAGE = {"OneStageHeatedSeat": "one heated seat state",
         "TwoStagesHeatedSeat": "two heated seat states",
         "ThreeStagesHeatedSeat": "three heated seat states",
         "TwoStagesVentedSeatsManagement": "two vented seat states",
         "ThreeStagesVentedSeatsManagement": "three vented seat states",
         "HeatedSteeringWheelManagement": "a heated steering wheel"}

SEL = [  # 第一序：`Fail_Present`（reqid 升冪）
    "SWE1-VC-TwoStagesHeatedSeat-074", "SWE1-VC-ThreeStagesHeatedSeat-098",
    "SWE1-VC-ThreeStagesHeatedSeat-099", "SWE1-VC-ThreeStagesVentedSeatsManagement-080",
    "SWE1-VC-ThreeStagesVentedSeatsManagement-081",
    "SWE1-VC-HeatedSteeringWheelManagement-035",
    # 第二序：P1，逐 Layer 2 輪流
    "SWE1-VC-OneStageHeatedSeat-047", "SWE1-VC-TwoStagesVentedSeatsManagement-043",
    "SWE1-VC-OneStageHeatedSeat-048", "SWE1-VC-TwoStagesVentedSeatsManagement-044",
]


def build() -> dict:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}
    scr = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/screen_source.tsv").open(encoding="utf-8"), delimiter="\t")}

    tcs, odd = [], []
    for leaf in SEL:
        row = l2r[leaf]
        qid = re.findall(r"\d{7}", row["reqid_list"])[0]
        source = "\n".join(blocks[qid]["text"].split("\n")[1:]).strip()
        flat = re.sub(r"\s+", " ", source)
        l2, l3 = gen[leaf]["layer2"], gen[leaf]["layer3"]
        fsig = re.search(r"STATUS_CSWM\.(\w*Fail\w*)", flat).group(1)
        fail = "Fail_Present" in flat
        screen = scr.get(leaf, {}).get("status", "PENDING")

        if (l2 == "Vented Seat" and "_HS_" in fsig) or (
                l2 == "Heated Steering Wheel" and "_HS_" in fsig):
            odd.append({"leaf": leaf, "layer2": l2, "signal": fsig, "reqid": qid})

        if fail:                                   # ── 式 F
            obj = OBJ_OF_FAIL[fsig]
            p0 = "_HS_" in fsig or fsig == "HSW_StatFailSts"
            title = f"Failure present changes the {obj} icon"
            lower = "(Failure present, icon change regardless of level)"
            proc = [f"1. Send CAN: STATUS_CSWM.{fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: STATUS_CSWM.{fsig} = 1 (Fail_Present)",
                    f"3. Read the {obj} icon on the Heated / Vented Seats screen and "
                    f"check that it changes from the state shown before the failure"]
            er = [f"1. STATUS_CSWM.{fsig} = 0 (Fail_Not_Present) is sent",
                  f"2. STATUS_CSWM.{fsig} = 1 (Fail_Present) is sent",
                  "3. PENDING: DR-5-B"]
            method = "基礎故障注入 (Fault Injection Lite)"
            prio = "P0" if p0 else "P1"
            why = ("P0(b)：加熱元件之失效狀態處置" if p0
                   else "P1：通風座椅之失效狀態處置（非熱源，不入 P0(b)）")
            axis = f"本列為失效時之圖示變更（式 F），失效訊號為 `{fsig}`。"
        else:                                      # ── 式 D
            m_if = re.search(r'IF \(?\$(\w+)\$ (==|passes to) "(\w+)"', flat)
            tok, init = m_if.group(1), m_if.group(3).rsplit("_", 1)[-1]
            dsig = DISP[tok]
            dlab = HS_LAB if "Heated" in tok else VS_LAB
            i_raw = RAW[init]
            obj = ("left front heated seat" if tok == "HeatedSeatFL" else
                   "right front heated seat" if tok == "HeatedSeatFR" else
                   "left front vented seat" if tok == "VentedSeatFL" else
                   "right front vented seat")
            m_cmd = re.search(r'set (\w+)\.(\w+) = "(\w+)"', flat)
            if m_cmd:                              # 命令型
                msg, cmd = m_cmd.group(1), m_cmd.group(2)
                c_raw = RAW[m_cmd.group(3).rsplit("_", 1)[-1]]
                c_lab = CMD_LAB[cmd][c_raw]
                title = f"{obj.capitalize()} at {init} plus request commands {m_cmd.group(3).rsplit('_', 1)[-1]}"
                lower = f"({STAGE[l3].capitalize()}, {init} plus press request)"
                step3 = (f"3. Press the {obj} icon and check that "
                         f"{msg}.{cmd} = {c_raw} ({c_lab}) is transmitted")
                er3 = f"3. {msg}.{cmd} = {c_raw} ({c_lab}) is sent"
                method = "決策表 (Decision Table Testing)"
                axis = f"本列為按壓請求下之命令送出（式 D／命令型），對象為 {tok}。"
            else:                                  # 顯示型
                title = f"{obj.capitalize()} display follows the status change to {init}"
                lower = f"({STAGE[l3].capitalize()}, status transition, no press)"
                step3 = (f"3. Read the displayed state of the {obj} and check that it "
                         f"changes to {init}")
                er3 = "3. PENDING: DR-5-B"
                method = "狀態轉換 (State Transition Testing)"
                axis = f"本列為顯示同步（式 D／顯示型），其畫面層依 R-VS59(4) 標 PENDING。"
            proc = [f"1. Send CAN: STATUS_CSWM.{fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: {dsig} = {i_raw} ({dlab[i_raw]})", step3]
            er = [f"1. STATUS_CSWM.{fsig} = 0 (Fail_Not_Present) is sent",
                  f"2. {dsig} = {i_raw} ({dlab[i_raw]}) is sent", er3]
            prio, why = "P1", "P1：主要功能邏輯"

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
            "reasoning": (why + f"；畫面層依 W-115(2) 之逐 leaf 行為層對照，"
                          f"本 leaf 判「{screen}」，"
                          + ("故依 R-VS59(4) 標 `PENDING: DR-5-B`"
                             if "PENDING" in er[-1] else "其畫面層斷言取自 Comfort 素材")),
            "split_flag": False, "split_reason": "", "dr15_exposed": "no",
            "dr_dependent": "DR-5-B" if "PENDING" in er[-1] else "DR-25",
            "screen_source": screen,
            "distinguishing_axis": {"axis": "failure-mode" if fail else "trigger",
                                    "delta": axis},
        })
    return {
        "batch": "batch17", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
        "generated_round": 41, "handoff": "docs/handoff/64_review_round40.md",
        "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
        "selection": "W-114 重跑後之池 **26**。依 R-VS58：第一序 `Fail_Present` **6** 條全取；"
                     "第二序 P1 逐 Layer 2 輪流取 **4**（HS 2／VS 2）。合計 **10**。",
        "signal_notation": "R-VS52 / SWC 0708（Send CAN: MSG.Sig = raw (label)；ER … is sent）",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "revision": "W-116（41 輪）：batch17 首版",
        "screen_layer": "依 W-115(2) 之逐 leaf 行為層對照；查無者標 `PENDING: DR-5-B`（R-VS59(4)）",
        "signal_section_mismatch": odd,
        "reasoning": "本批含 `HeatedSteeringWheelManagement-035` —— 其為 W-114(1) 補收 "
                     "`HSW_StatFailSts` 值域後**首次可寫**之 leaf（A-VS137）。"
                     "`FR_VS_Cmd_Tlm` 之二條為 R-VS60 跨列引入後首次可寫。",
        "tcs": tcs,
    }


if __name__ == "__main__":
    d = build()
    (FEAT / "generated/batch17.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch17：{len(d['tcs'])} 條")
    for tc in d["tcs"]:
        print(f"  {tc['priority']} {tc['leaf_id']:48s} {tc['tc_title'][:60]}")
    print(f"\n訊號與所在節不符者：{len(d['signal_section_mismatch'])}")
