"""W-150（80 包 §4）—— E 型放量。

E 型之形態（80 包 §1 判其通過）：
    `When the HU receives a $<tok>$ = [<描述> / <別名>] signal, the HU shall
     change the stored status … and change the display as specified by the HMI
     within a time period of <Tdisplay>`
  觸發＝**收到狀態訊號**；標的＝**顯示之變更**（依 R-VS59(4) 寫最弱斷言）。

**排除二條**（其觸發非「收到狀態訊號」，故非 E 型 —— 升級條件命中，上繳 45 §2.2）：
    `OneStageHeatedSeat-042`／`-044` —— `IF <Req> passes to "Requested" THEN set …`
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

SIG = {"HSW_Stat_2": ("STATUS_CLIMATE8.Tri_Level_HSW_StatSts", "heated steering wheel",
                      {0: "Heated_steering_wheel_off", 1: "Heated_steering_wheel_low",
                       2: "Heated_steering_wheel_medium", 3: "Heated_steering_wheel_high"}),
       "HeatedSeatFL": ("STATUS_CSWM.FL_HS_STATSts", "left front heated seat",
                        {0: "Heated_seat_off", 1: "Heated_seat_low",
                         2: "Heated_seat_medium", 3: "Heated_seat_high"}),
       "HeatedSeatFR": ("STATUS_CSWM.FR_HS_STATSts", "right front heated seat",
                        {0: "Heated_seat_off", 1: "Heated_seat_low",
                         2: "Heated_seat_medium", 3: "Heated_seat_high"}),
       "VentedSeatFL": ("STATUS_CSWM.FL_VS_STATSts", "left front vented seat",
                        {0: "Vented_seat_off", 1: "Vented_seat_low",
                         2: "Vented_seat_medium", 3: "Vented_seat_high"}),
       "VentedSeatFR": ("STATUS_CSWM.FR_VS_STATSts", "right front vented seat",
                        {0: "Vented_seat_off", 1: "Vented_seat_low",
                         2: "Vented_seat_medium", 3: "Vented_seat_high"})}
ALIAS = {"OFF": 0, "LO": 1, "MED": 2, "HI": 3}
EXCLUDE = {"SWE1-VC-OneStageHeatedSeat-042", "SWE1-VC-OneStageHeatedSeat-044"}


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    sel = json.loads((FEAT / "data/_w150_E.json").read_text(encoding="utf-8"))

    tcs, skipped = [], []
    for leaf, qid, l2 in sel:
        if leaf in EXCLUDE:
            skipped.append(leaf)
            continue
        source = "\n".join(blocks[qid]["text"].split("\n")[1:]).strip()
        flat = re.sub(r"\s+", " ", source)
        m = re.search(r"\$(\w+)\$\s*=\s*\[([^\]/]+)/\s*(\w+)\]", flat)
        tok, alias = m.group(1), m.group(3).split("_")[-1].upper()
        sig, obj, lab = SIG[tok]
        raw = ALIAS[alias]
        other = 0 if raw != 0 else 3
        var = f"{obj.split()[0].capitalize()}_display_before"
        tcs.append({
            "leaf_id": leaf, "test_set": l2,
            "tc_title": f"{obj.capitalize()} display follows status "
                        f"{lab[raw].rsplit('_', 1)[-1]}",
            "test_item": source + f"\n\n(Status transition to "
                                  f"{lab[raw].rsplit('_', 1)[-1]})",
            "pre_conditions": "\n".join([
                f"1. The vehicle is equipped with {'a heated steering wheel' if 'steering' in obj else 'the seat function under test'}",
                "2. The Heated / Vented Seats screen is displayed",
                "3. CAN-B is connected to the bus simulator"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join([
                f"1. Send CAN: {sig} = {other} ({lab[other]}) and record the {obj} "
                f"display state as {var}",
                f"2. Send CAN: {sig} = {raw} ({lab[raw]})",
                f"3. Read the displayed state of the {obj} and check that it changes "
                f"from {var}"]),
            "expected_result": "\n".join([
                f"1. {sig} = {other} ({lab[other]}) is sent；{var} is recorded",
                f"2. {sig} = {raw} ({lab[raw]}) is sent",
                f"3. The {obj} display changes from {var}"]),
            "specification_reference": l2r[leaf]["reqid_list"].replace(";", "\n"),
            "design_method": "狀態轉換 (State Transition Testing)",
            "priority": "P1",
            "reasoning": ("P1：主要功能邏輯；**E 型 —— 觸發為收到狀態訊號**"
                          "（`When the HU receives a … signal`），標的為顯示之變更。"
                          "其具體樣式待 TLM HMI Document，依 R-VS59(4) 寫最弱斷言"),
            "split_flag": False, "split_reason": "", "dr15_exposed": "no",
            "dr_dependent": "", "screen_pending": "yes",
            "remarks": ("BLOCKED: DR-5-B —— 變更後之顯示樣式待 TLM HMI Document；"
                        "BLOCKED: DR-24′ —— `<Tdisplay>` 之上限值待覆"),
            "distinguishing_axis": {"axis": "level",
                                    "delta": f"本列之目標狀態為 {lab[raw]}，對象為 {tok}。"},
        })
    d = {"batch": "batch22", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
         "generated_round": 52, "handoff": "docs/handoff/80_probe_verdict.md",
         "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
         "selection": f"W-150：E 型放量。指令載 14 條，**其中 2 條之觸發非「收到狀態訊號」"
                      f"而為按壓請求**（`OneStageHeatedSeat-042`／`-044`），"
                      f"依升級條件排除並具名 → **實產 {len(tcs)} 條**。",
         "signal_notation": "R-VS52 ＋ R-VS67′",
         "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
         "revision": "W-150（52 輪）：batch22 首版",
         "excluded": [{"leaf_id": x, "reason": "觸發為 `IF <Req> passes to \"Requested\"`"
                       "（按壓請求）而非收到狀態訊號 —— 非 E 型"} for x in skipped],
         "tcs": tcs}
    (FEAT / "generated/batch22.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch22：{len(tcs)} 條（指令載 14，排除 {len(skipped)}）")
    for t in tcs:
        print(f"  {t['leaf_id']:44s} {t['tc_title']}")
    print("排除：", skipped)


if __name__ == "__main__":
    main()
