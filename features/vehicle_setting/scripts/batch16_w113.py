"""W-113（63 包 §7）—— batch16，10 條。

自 W-111 後之池（**35**）依 R-VS58 選取；**`Fail_Present` 類優先納入**
（A-VS116 之標的，本輪因 R-VS59 首次入池）。同序內逐 Layer 2 輪流 ＋ reqid 升冪。

畫面層依 W-112 之對照表撰寫 —— **惟 Comfort 037 之 403 條 Functional 條文中，
含 heated／vented seat 者 20 條而其含 fail／error 者 0 條**，
故本批之畫面層斷言一律標 `PENDING: DR-5-B`（R-VS59(4)）。見上繳 35 §2.2。

**條文之訊號逐字轉錄，不更正**：5 個 leaf 於通風座椅／加熱方向盤之節內
引用加熱座椅之 `*_HS_STATFailSts`（A-VS138）。
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

OBJ = {"FL_HS_STATFailSts": "left front heated seat",
       "FR_HS_STATFailSts": "right front heated seat",
       "FL_VS_STATFailSts": "left front vented seat"}
STAGE = {"OneStageHeatedSeat": "one heated seat state",
         "TwoStagesHeatedSeat": "two heated seat states",
         "ThreeStagesHeatedSeat": "three heated seat states",
         "TwoStagesVentedSeatsManagement": "two vented seat states",
         "ThreeStagesVentedSeatsManagement": "three vented seat states",
         "HeatedSteeringWheelManagement": "a heated steering wheel"}

# 依 R-VS58：全 15 條 `Fail_Present` leaf 皆為 P0(b) 之標的；
# 同序內逐 Layer 2 輪流（Heated Seat／Vented Seat／Heated Steering Wheel）＋ reqid 升冪。
SEL = ["SWE1-VC-OneStageHeatedSeat-051",
       "SWE1-VC-TwoStagesVentedSeatsManagement-046",
       "SWE1-VC-HeatedSteeringWheelManagement-031",
       "SWE1-VC-OneStageHeatedSeat-052",
       "SWE1-VC-TwoStagesVentedSeatsManagement-047",
       "SWE1-VC-TwoStagesHeatedSeat-064",
       "SWE1-VC-TwoStagesVentedSeatsManagement-055",
       "SWE1-VC-TwoStagesHeatedSeat-065",
       "SWE1-VC-TwoStagesVentedSeatsManagement-056",
       "SWE1-VC-TwoStagesHeatedSeat-073"]


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
        sig = re.search(r"STATUS_CSWM\.(\w+)", flat).group(1)
        fam = "P" if "popup" in flat else "I"
        l2, l3 = gen[leaf]["layer2"], gen[leaf]["layer3"]
        obj = OBJ[sig]
        # 條文之訊號與其所在節之實體功能不符者，逐字轉錄並具名（A-VS138）
        if (l2 == "Vented Seat" and "_HS_" in sig) or (l2 == "Heated Steering Wheel"
                                                       and "_HS_" in sig):
            odd.append({"leaf": leaf, "layer2": l2, "signal": sig, "reqid": qid})
        # R-VS56 之 P0(b) 限熱源；`*_VS_STATFailSts` 為通風（非熱源）→ P1
        p0 = "_HS_" in sig
        prio = "P0" if p0 else "P1"
        why = ("P0(b)：加熱元件之失效狀態處置" if p0
               else "P1：通風座椅之失效狀態處置（非熱源，不入 P0(b)）")

        if fam == "P":
            title = f"Failure present blocks the {obj} request with a popup"
            lower = "(Failure present at request, informative popup)"
            step3 = (f"3. Press the {obj} icon and check that an informative popup "
                     f"relative to the failure is shown")
            method = "基礎故障注入 (Fault Injection Lite)"
            axis = f"本列為請求時之失效彈窗（式 P）；式 I 之列為失效時之圖示變更。"
        else:
            title = f"Failure present changes the {obj} icon"
            lower = "(Failure present, icon change regardless of level)"
            step3 = (f"3. Read the {obj} icon on the Heated / Vented Seats screen and "
                     f"check that it changes from the state shown before the failure")
            method = "基礎故障注入 (Fault Injection Lite)"
            axis = f"本列為失效時之圖示變更（式 I）；式 P 之列為請求時之彈窗。"

        proc = [f"1. Send CAN: STATUS_CSWM.{sig} = 0 (Fail_Not_Present)",
                f"2. Send CAN: STATUS_CSWM.{sig} = 1 (Fail_Present)", step3]
        er = [f"1. STATUS_CSWM.{sig} = 0 (Fail_Not_Present) is sent",
              f"2. STATUS_CSWM.{sig} = 1 (Fail_Present) is sent",
              "3. PENDING: DR-5-B"]

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
            "reasoning": (why + "；畫面層依 R-VS59(2) 取自 Comfort 素材，"
                          "而 Comfort 037 之 seat 相關 20 條中含 fail／error 者 **0**，"
                          "故依 R-VS59(4) 標 `PENDING: DR-5-B`"),
            "split_flag": False, "split_reason": "",
            "dr15_exposed": "no", "dr_dependent": "DR-5-B",
            "screen_source": scr.get(leaf, {}).get("status", ""),
            "distinguishing_axis": {"axis": "failure-mode", "delta": axis},
        })
    return {
        "batch": "batch16", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
        "generated_round": 40, "handoff": "docs/handoff/63_rulings_round39.md",
        "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
        "selection": "W-111 後之池 **35**（R-VS59 解除 delegate 之扣除）。"
                     "依 R-VS58／W-113：`Fail_Present` 類 **15 條**優先，取 **10**；"
                     "同序內逐 Layer 2 輪流（HS 5／VS 4／HSW 1）＋ reqid 升冪；兼取兩式（P 4／I 6）。",
        "signal_notation": "R-VS52 / SWC 0708（Send CAN: MSG.Sig = raw (label)；ER … is sent）",
        "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
        "revision": "W-113（40 輪）：batch16 首版",
        "screen_layer": "R-VS59(2) 之來源不足 —— 全 10 條之畫面層斷言標 `PENDING: DR-5-B`（R-VS59(4)）",
        "signal_section_mismatch": odd,
        "reasoning": "本批為本 feature **首批失效狀態 TC**（A-VS116 之標的，"
                     "自 R-VS59 撤回 `delegate = blocked` 之扣除後首次入池）。"
                     "條文之訊號逐字轉錄，**不更正**其與所在節之實體功能不符者（A-VS138）。",
        "tcs": tcs,
    }


if __name__ == "__main__":
    d = build()
    (FEAT / "generated/batch16.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch16：{len(d['tcs'])} 條")
    for tc in d["tcs"]:
        print(f"  {tc['priority']} {tc['leaf_id']:48s} {tc['tc_title']}")
    print(f"\n訊號與所在節不符者：{len(d['signal_section_mismatch'])}")
    for o in d["signal_section_mismatch"]:
        print("   ", o)
