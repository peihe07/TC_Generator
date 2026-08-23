"""W-108(3)（61 包 §5）—— batch15，依 R-VS58 之優先序自重跑後之池取。

池 **14**，扣除 `FeaturesEnableCriteria-023`（A-VS112，DR-8 之跨條文依賴）
得 **13** —— **池不足 10 之反面：池只餘 13，全取並回報**。

參數自條文**解析而得**，不手寫：
    `IF ($<顯示 token>$ (==|passes to) "<階>" …) THEN … set <MSG>.<Cmd> = "<階>"`
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

DISP_SIG = {"HeatedSeatFL": "STATUS_CSWM.FL_HS_STATSts",
            "HeatedSeatFR": "STATUS_CSWM.FR_HS_STATSts",
            "VentedSeatFL": "STATUS_CSWM.FL_VS_STATSts"}
FAIL_SIG = {"HeatedSeatFL": "STATUS_CSWM.FL_HS_STATFailSts",
            "HeatedSeatFR": "STATUS_CSWM.FR_HS_STATFailSts",
            "VentedSeatFL": "STATUS_CSWM.FL_VS_STATFailSts"}
OBJ = {"HeatedSeatFL": "left front heated seat", "HeatedSeatFR": "right front heated seat",
       "VentedSeatFL": "left front vented seat"}
HS_LAB = {0: "Heated_seat_off", 1: "Heated_seat_low", 2: "Heated_seat_medium",
          3: "Heated_seat_high"}
VS_LAB = {0: "Vented_seat_off", 1: "Vented_seat_low", 2: "Vented_seat_medium",
          3: "Vented_seat_high"}
CMD_LAB = {"FL_HS_Cmd_Tlm": HS_LAB, "FR_HS_Cmd_Tlm": HS_LAB,
           "FL_VS_Cmd_Tlm": {0: "Vented_Seat_Off", 1: "Vented_Seat_Low",
                             2: "Vented_Seat_Medium", 3: "Vented_Seat_High"}}
RAW = {"off": 0, "low": 1, "medium": 2, "high": 3}
STAGE_PRE = {("Heated Seat", "two"): "The vehicle is configured for two heated seat states",
             ("Heated Seat", "three"): "The vehicle is configured for three heated seat states",
             ("Vented Seat", "two"): "The vehicle is configured for two vented seat states",
             ("Vented Seat", "three"): "The vehicle is configured for three vented seat states"}

# 依 R-VS58：本池預判 **P0 0／P1 13／P2 1**（P2 者為 A-VS112 之標的，排除）。
# 同序內逐 Layer 2 輪流 ＋ reqid 升冪。
ORDER = ["SWE1-VC-TwoStagesHeatedSeat-070", "SWE1-VC-TwoStagesVentedSeatsManagement-051",
         "SWE1-VC-TwoStagesHeatedSeat-071", "SWE1-VC-ThreeStagesVentedSeatsManagement-075",
         "SWE1-VC-TwoStagesHeatedSeat-072", "SWE1-VC-ThreeStagesHeatedSeat-084",
         "SWE1-VC-ThreeStagesHeatedSeat-088", "SWE1-VC-ThreeStagesHeatedSeat-090",
         "SWE1-VC-ThreeStagesHeatedSeat-091", "SWE1-VC-ThreeStagesHeatedSeat-093",
         "SWE1-VC-ThreeStagesHeatedSeat-094", "SWE1-VC-ThreeStagesHeatedSeat-095",
         "SWE1-VC-ThreeStagesHeatedSeat-097"]


def parse(text: str) -> dict:
    flat = re.sub(r"\s+", " ", text)
    m_if = re.search(r'IF \(\$(\w+)\$ (==|passes to) "(\w+)"', flat)
    m_then = re.search(r'set (\w+)\.(\w+) = "(\w+)"', flat)
    return {"tok": m_if.group(1), "form": "A" if m_if.group(2) == "==" else "B",
            "init": m_if.group(3).rsplit("_", 1)[-1], "msg": m_then.group(1),
            "cmd": m_then.group(2), "cmd_lvl": m_then.group(3).rsplit("_", 1)[-1]}


def build() -> dict:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    gen = {r["leaf_id"]: r for r in csv.DictReader(
        (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}

    tcs, mism = [], []
    for leaf in ORDER:
        row = l2r[leaf]
        qid = re.findall(r"\d{7}", row["reqid_list"])[0]
        source = "\n".join(blocks[qid]["text"].split("\n")[1:]).strip()
        p = parse(source)
        l2 = gen[leaf]["layer2"]
        stage = "three" if "ThreeStages" in leaf else "two"
        obj, dsig, fsig = OBJ[p["tok"]], DISP_SIG[p["tok"]], FAIL_SIG[p["tok"]]
        dlab = HS_LAB if "Heated" in p["tok"] else VS_LAB
        i_raw, c_raw = RAW[p["init"]], RAW[p["cmd_lvl"]]
        i_lab, c_lab = dlab[i_raw], CMD_LAB[p["cmd"]][c_raw]

        # R-VS56：P0(b) 限加熱元件自 off 起之啟用 —— 本池無此形態
        final_p = "P0" if (l2 == "Heated Seat" and p["form"] == "A"
                           and p["init"] == "off") else "P1"
        if final_p != "P1":
            mism.append((leaf, "P1", final_p))
        why = "P1：主要功能邏輯"

        if p["form"] == "A":
            title = f"{obj.capitalize()} at {p['init']} plus request commands {p['cmd_lvl']}"
            lower = f"({stage.capitalize()} stage configuration, {p['init']} plus press request)"
            proc = [f"1. Send CAN: {fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: {dsig} = {i_raw} ({i_lab})",
                    f"3. Press the {obj} icon and check that "
                    f"{p['msg']}.{p['cmd']} = {c_raw} ({c_lab}) is transmitted"]
            method = "決策表 (Decision Table Testing)"
            delta = (f"本列之階數配置為{stage}、顯示 token 為 {p['tok']}、初始階為 {p['init']}，"
                     f"觸發為按壓請求。")
        else:
            mid_raw = 2 if i_raw != 2 else 3
            title = f"{obj.capitalize()} status change mirrors {p['cmd_lvl']} to the command"
            lower = f"({stage.capitalize()} stage configuration, status transition, no press)"
            proc = [f"1. Send CAN: {fsig} = 0 (Fail_Not_Present)",
                    f"2. Send CAN: {dsig} = {mid_raw} ({dlab[mid_raw]})",
                    f"3. Send CAN: {dsig} = {i_raw} ({i_lab}) without pressing any icon and "
                    f"check that {p['msg']}.{p['cmd']} = {c_raw} ({c_lab}) is transmitted"]
            method = "狀態轉換 (State Transition Testing)"
            delta = (f"本列之階數配置為{stage}、顯示 token 為 {p['tok']}、"
                     f"轉換之目標階為 {p['init']}，無按壓。")
        er = [f"1. {fsig} = 0 (Fail_Not_Present) is sent",
              f"2. {proc[1].split('Send CAN: ')[1]} is sent",
              f"3. {p['msg']}.{p['cmd']} = {c_raw} ({c_lab}) is sent"]

        reasoning = why
        if p["tok"].endswith("FR") and p["form"] == "A":
            reasoning += ("；觸發表述依 `CFTS044-4859365`，其與駕駛側 `4859364` 逐字對稱，"
                          "駕駛側之觸發表述由 `4859508` 之 `or` 並列確立（61 包 §2）")
        elif p["form"] == "A":
            reasoning += "；觸發表述依 `CFTS044-4859508` 之 `or` 並列（60 包 §1）"

        tcs.append({
            "leaf_id": leaf, "test_set": l2, "tc_title": title,
            "test_item": f"{source}\n\n{lower}",
            "pre_conditions": "\n".join([
                f"1. {STAGE_PRE[(l2, stage)]}",
                "2. The Heated / Vented Seats screen is displayed",
                "3. CAN-B is connected to the bus simulator",
                "4. The vehicle architecture is Atlantis Mid"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join(proc), "expected_result": "\n".join(er),
            "specification_reference": row["reqid_list"].replace(";", "\n"),
            "design_method": method, "priority": final_p, "reasoning": reasoning,
            "priority_prejudged": "P1",
            "split_flag": False, "split_reason": "", "dr15_exposed": "no",
            "dr_dependent": "DR-25",
            "distinguishing_axis": {"axis": "configuration", "delta": delta},
        })
    return {
        "batch": "batch15", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
        "generated_round": 38, "handoff": "docs/handoff/61_review_round37.md",
        "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
        "selection": "W-108 重跑後之池 **14**，扣除 `FeaturesEnableCriteria-023`"
                     "（A-VS112，DR-8）得 **13** —— **全取**。"
                     "依 R-VS58 預判 P0 **0**／P1 13／P2 1；同序內逐 Layer 2 輪流 ＋ reqid 升冪。"
                     "**池於本批後見底（0）。**",
        "signal_notation": "R-VS52 / SWC 0708（Send CAN: MSG.Sig = raw (label)；ER … is sent）",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "revision": "W-108(3)（38 輪）：batch15 首版",
        "priority_prejudge_mismatch": mism,
        "dr_dependency": "全 13 條之命令訊號依 R-VS57 判 L-VS2 WARN，標 `dr_dependent = DR-25`（→ DR-25′）。",
        "reasoning": "本批參數自條文解析而得，不手寫（`parse()`）。"
                     "Sibling Rows：`-075`／`-051` 與 `-093`／`-072` 等組其可測內容相同，"
                     "**以 pre_conditions 之階數配置分辨**（R-VS59 前之既有慣例）。",
        "tcs": tcs,
    }


if __name__ == "__main__":
    d = build()
    (FEAT / "generated/batch15.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch15：{len(d['tcs'])} 條")
    for tc in d["tcs"]:
        print(f"  {tc['priority']} {tc['leaf_id']:46s} {tc['tc_title']}")
    print("預判與定稿不一致：", d["priority_prejudge_mismatch"])
