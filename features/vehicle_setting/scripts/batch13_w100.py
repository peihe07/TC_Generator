"""W-100（57 包 §5，自 32 輪順延四輪）—— batch13，10 條。

池：W-98 重跑後之 `generatable = yes` 扣已交付，得 **34**；
其中 33 條標 `dr_dependent = DR-25`（R-VS57 之 WARN 類），
1 條為 `FeaturesEnableCriteria-023`（A-VS112，DR-8 之跨條文依賴）。

選 10 條，**逐 Layer 2 輪流**（Heated Seat ／ Vented Seat 交替），
並兼取條文之兩式：
  式 A  `IF (<顯示值> == X AND <FailSts> == Fail_Not_Present AND <Req> passes to
        "Requested") THEN TLM shall set <Cmd_Tlm> = Y`   —— 按壓請求 → 命令
  式 B  `IF (<顯示值> passes to X AND <FailSts> == Fail_Not_Present)
        THEN TLM shall set <Cmd_Tlm> = X`                 —— 狀態鏡射 → 命令

`test_item` 上半段逐字取自 `blocks_with_sec()`（R-VS6），不改寫。
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

# 顯示值 token → 驅動其顯示之 DBC 訊號（LID CAN Mapping 列 915／916／2332）
DISPLAY_SIG = {"HeatedSeatFL": "STATUS_CSWM.FL_HS_STATSts",
               "HeatedSeatFR": "STATUS_CSWM.FR_HS_STATSts",
               "VentedSeatFL": "STATUS_CSWM.FL_VS_STATSts"}
FAIL_SIG = {"HeatedSeatFL": "STATUS_CSWM.FL_HS_STATFailSts",
            "HeatedSeatFR": "STATUS_CSWM.FR_HS_STATFailSts",
            "VentedSeatFL": "STATUS_CSWM.FL_VS_STATFailSts"}
# 命令訊號之 raw → label（LID `Atlantis` 欄組逐字；R-VS57 之 WARN 類）
CMD_LABEL = {
    "FL_HS_Cmd_Tlm": {0: "Heated_seat_off", 1: "Heated_seat_low",
                      2: "Heated_seat_medium", 3: "Heated_seat_high"},
    "FL_VS_Cmd_Tlm": {0: "Vented_Seat_Off", 1: "Vented_Seat_Low",
                      2: "Vented_Seat_Medium", 3: "Vented_Seat_High"},
}
# 顯示訊號之 raw → label（基線 DBC `VAL_` 逐字）
DISP_LABEL = {
    "STATUS_CSWM.FL_HS_STATSts": {0: "Heated_seat_off", 1: "Heated_seat_low",
                                  2: "Heated_seat_medium", 3: "Heated_seat_high"},
    "STATUS_CSWM.FL_VS_STATSts": {0: "Vented_seat_off", 1: "Vented_seat_low",
                                  2: "Vented_seat_medium", 3: "Vented_seat_high"},
}
LEVEL = {"off": 0, "low": 1, "medium": 2, "high": 3}

# (leaf, layer2, 式, 顯示 token, 初始階, 命令訊號, 命令訊息, 命令階)
SEL = [
    ("SWE1-VC-TwoStagesHeatedSeat-058", "Heated Seat", "A", "HeatedSeatFL", "off",
     "FL_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "high"),
    ("SWE1-VC-TwoStagesVentedSeatsManagement-040", "Vented Seat", "A", "VentedSeatFL", "off",
     "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "high"),
    ("SWE1-VC-TwoStagesHeatedSeat-059", "Heated Seat", "A", "HeatedSeatFL", "high",
     "FL_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "low"),
    ("SWE1-VC-TwoStagesVentedSeatsManagement-041", "Vented Seat", "A", "VentedSeatFL", "high",
     "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "low"),
    ("SWE1-VC-TwoStagesHeatedSeat-060", "Heated Seat", "A", "HeatedSeatFL", "low",
     "FL_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "off"),
    ("SWE1-VC-TwoStagesVentedSeatsManagement-042", "Vented Seat", "A", "VentedSeatFL", "low",
     "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "off"),
    ("SWE1-VC-TwoStagesHeatedSeat-067", "Heated Seat", "B", "HeatedSeatFL", "off",
     "FL_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "off"),
    ("SWE1-VC-TwoStagesVentedSeatsManagement-049", "Vented Seat", "B", "VentedSeatFL", "off",
     "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "off"),
    ("SWE1-VC-TwoStagesHeatedSeat-068", "Heated Seat", "B", "HeatedSeatFL", "low",
     "FL_HS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP", "low"),
    ("SWE1-VC-TwoStagesVentedSeatsManagement-050", "Vented Seat", "B", "VentedSeatFL", "low",
     "FL_VS_Cmd_Tlm", "TELEMATIC_VEHICLE_SETUP2", "low"),
]

KIND = {"Heated Seat": "heated seat", "Vented Seat": "vented seat"}
PRE = {"Heated Seat": "The vehicle is equipped with heated front seats",
       "Vented Seat": "The vehicle is equipped with vented front seats"}


def build() -> dict:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    tcs = []
    for leaf, l2, form, disp_tok, init, cmd, msg, cmd_lvl in SEL:
        row = l2r[leaf]
        qid = re.findall(r"\d{7}", row["reqid_list"])[0]
        source = "\n".join(blocks[qid]["text"].split("\n")[1:]).strip()   # R-VS6 上半段逐字
        kind, dsig, fsig = KIND[l2], DISPLAY_SIG[disp_tok], FAIL_SIG[disp_tok]
        i_raw, c_raw = LEVEL[init], LEVEL[cmd_lvl]
        i_lab, c_lab = DISP_LABEL[dsig][i_raw], CMD_LABEL[cmd][c_raw]

        if form == "A":
            title = f"{kind.capitalize()} at {init} plus request commands {cmd_lvl}"
            lower = f"({init.capitalize()} plus press request, no failure present)"
            proc = [f"1. Send CAN: {fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: {dsig} = {i_raw} ({i_lab})",
                    f"3. Press the left front {kind} icon and check that "
                    f"{msg}.{cmd} = {c_raw} ({c_lab}) is transmitted"]
            er = [f"1. {fsig} = 0 (Fail_Not_Present) is sent",
                  f"2. {dsig} = {i_raw} ({i_lab}) is sent",
                  f"3. {msg}.{cmd} = {c_raw} ({c_lab}) is sent"]
            method = "決策表 (Decision Table Testing)"
            axis = {"axis": "trigger",
                    "delta": f"本列之觸發為按壓請求（`DrvSeatHeating.Req passes to \"Requested\"`），"
                             f"自 {init} 起；式 B 之列為狀態鏡射，無按壓。"}
        else:
            title = f"{kind.capitalize()} status change mirrors {cmd_lvl} to the command"
            lower = f"(Status transition to {cmd_lvl} mirrored, no press)"
            proc = [f"1. Send CAN: {fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: {dsig} = {LEVEL['medium'] if i_raw != 2 else 3} "
                    f"({DISP_LABEL[dsig][LEVEL['medium'] if i_raw != 2 else 3]})",
                    f"3. Send CAN: {dsig} = {i_raw} ({i_lab}) without pressing any icon and "
                    f"check that {msg}.{cmd} = {c_raw} ({c_lab}) is transmitted"]
            er = [f"1. {fsig} = 0 (Fail_Not_Present) is sent",
                  f"2. {dsig} = {LEVEL['medium'] if i_raw != 2 else 3} "
                  f"({DISP_LABEL[dsig][LEVEL['medium'] if i_raw != 2 else 3]}) is sent",
                  f"3. {msg}.{cmd} = {c_raw} ({c_lab}) is sent"]
            method = "狀態轉換 (State Transition Testing)"
            axis = {"axis": "trigger",
                    "delta": f"本列之觸發為顯示值之轉換（`passes to`），無按壓；"
                             f"式 A 之列為按壓請求。"}

        tcs.append({
            "leaf_id": leaf,
            "test_set": l2,
            "tc_title": title,
            "test_item": f"{source}\n\n{lower}",
            "pre_conditions": "\n".join([
                f"1. {PRE[l2]}",
                "2. The Heated / Vented Seats screen is displayed",
                "3. CAN-B is connected to the bus simulator",
                "4. The vehicle architecture is Atlantis Mid"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join(proc),
            "expected_result": "\n".join(er),
            "specification_reference": row["reqid_list"].replace(";", "\n"),
            "design_method": method,
            # R-VS56 之 P0(b) 限「啟用」—— 即自 off 起之開啟；
            # 階數之升降（high→low／low→off）為階數切換，屬 P1。
            # 貫通座椅（vented）非熱源，不入 P0(b)。
            "priority": "P0" if (l2 == "Heated Seat" and form == "A" and init == "off")
                        else "P1",
            "reasoning": ("P0(b)：加熱座椅之按壓啟用"
                          if (l2 == "Heated Seat" and form == "A" and init == "off")
                          else "P1：主要功能邏輯"),
            "split_flag": False,
            "split_reason": "",
            "dr15_exposed": "no",
            "dr_dependent": "DR-25",
            "distinguishing_axis": axis,
        })
    return {
        "batch": "batch13",
        "feature": "vehicle_setting",
        "test_group": "Vehicle Setting",
        "generated_round": 36,
        "handoff": "docs/handoff/57_review_round35.md",
        "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
        "selection": "W-98 重跑後之池 34（33 標 dr_dependent = DR-25 ＋ 1 為 A-VS112 之標的）"
                     "→ 排除 A-VS112 之 `FeaturesEnableCriteria-023` → 33 → "
                     "逐 Layer 2 輪流取 10（Heated Seat 5／Vented Seat 5），兼取條文兩式",
        "signal_notation": "R-VS52 / SWC 0708（Send CAN: MSG.Sig = raw (label)；ER … is sent）",
        "revision": "W-100（36 輪）：batch13 首版",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "dr_dependency": "全 10 條之命令訊號（FL_HS_Cmd_Tlm／FL_VS_Cmd_Tlm）依 R-VS57 判 "
                         "L-VS2 WARN —— 其不在基線 DBC，訊號名與值域取 LID `Atlantis` 欄組之逐字。"
                         "**DR-25 覆後為 (b) 者，本批 10 條逐條撤回。**",
        "reasoning": "池 33 條全屬 `Atlantis Mid` 之 `*_Cmd_Tlm` 族。"
                     "`DrvSeatHeating.Req passes to \"Requested\"` 於 LID 無對映列，"
                     "本批以 HMI 按壓表述之 —— 其依據為同族已交付之 "
                     "`TwoStagesHeatedSeat-057`（按壓循環）與 `-066`（`without pressing any icon`），"
                     "二者已確立按壓為該請求之觸發。**列此供覆核。**",
        "tcs": tcs,
    }


if __name__ == "__main__":
    d = build()
    (FEAT / "generated/batch13.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch13：{len(d['tcs'])} 條")
    for tc in d["tcs"]:
        print(f"  {tc['priority']} {tc['leaf_id']:46s} {tc['tc_title']}")
