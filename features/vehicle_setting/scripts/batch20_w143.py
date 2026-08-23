"""W-143(1)（77 包 §2）—— batch20：依 **R-VS71** 補寫 A 型 12 條。

A 型＝`IF ($<disp>$ (==|passes to) "<階>" AND <FailSts> == "Fail_Not_Present"
[AND <Req> passes to "Requested"]) THEN TLM shall set <MSG>.<Cmd> = "<階>"`。

**十二條之值皆含 `_mid`** —— A-VS104 已裁其**不可對映**至 `_medium`
（變母音之縮寫，無結構性判準；併 DR-18；禁區禁止擴充 R-VS48(a)）。

依 **R-VS71**：值之未解**不阻塞生成** ——
  可解者 → `= <raw> (<label>)`
  `_mid` → **取來源逐字、不附 raw**（R-VS61），標 `dr_dependent = DR-18`
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
DISP = {"HeatedSeatFL": "STATUS_CSWM.FL_HS_STATSts", "HeatedSeatFR": "STATUS_CSWM.FR_HS_STATSts",
        "VentedSeatFL": "STATUS_CSWM.FL_VS_STATSts", "VentedSeatFR": "STATUS_CSWM.FR_VS_STATSts"}
FAIL = {"HeatedSeatFL": "STATUS_CSWM.FL_HS_STATFailSts", "HeatedSeatFR": "STATUS_CSWM.FR_HS_STATFailSts",
        "VentedSeatFL": "STATUS_CSWM.FL_VS_STATFailSts", "VentedSeatFR": "STATUS_CSWM.FR_VS_STATFailSts"}
OBJ = {"HeatedSeatFL": "left front heated seat", "HeatedSeatFR": "right front heated seat",
       "VentedSeatFL": "left front vented seat", "VentedSeatFR": "right front vented seat"}
RAW = {"off": 0, "low": 1, "medium": 2, "high": 3}
# 標籤逐字：**顯示訊號**取 DBC `VAL_`（`Vented_seat_*` 小寫 s），
# **命令訊號**取 LID `Atlantis` 欄組（`Vented_Seat_*` 大寫 S，52 包 §3 之 typo 裁定）。
# 二者形態不同，混用即 R-VS39 違規（50 輪 W-143 實測 4 項）。
LAB = {"Heated": {0: "Heated_seat_off", 1: "Heated_seat_low", 2: "Heated_seat_medium",
                  3: "Heated_seat_high"},
       "Vented": {0: "Vented_seat_off", 1: "Vented_seat_low", 2: "Vented_seat_medium",
                  3: "Vented_seat_high"}}
CMD_LAB = {"Heated": LAB["Heated"],
           "Vented": {0: "Vented_Seat_Off", 1: "Vented_Seat_Low",
                      2: "Vented_Seat_Medium", 3: "Vented_Seat_High"}}


def term(sig: str, val: str, fam: str, cmd: bool = False) -> tuple[str, bool]:
    """回傳（書寫形式, 是否未解）。`_mid` 為未解（A-VS104）。"""
    lvl = val.rsplit("_", 1)[-1]
    tbl = CMD_LAB[fam] if cmd else LAB[fam]
    if lvl in RAW:
        return f"{sig} = {RAW[lvl]} ({tbl[RAW[lvl]]})", False
    return f"{sig} = {val}", True          # R-VS61：來源逐字，不附 raw


def main() -> None:
    blocks = {b["id"]: b for b in blocks_with_sec()}
    l2r = {r["swe_id"]: r for r in csv.DictReader(
        (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
    A = json.loads((FEAT / "data/_w143_A.json").read_text(encoding="utf-8"))
    tcs = []
    for leaf, l2, l3, qid, tok, op, init, msg, cmd, out in A:
        source = "\n".join(blocks[qid]["text"].split("\n")[1:]).strip()
        fam = "Heated" if "Heated" in tok else "Vented"
        dsig, fsig, obj = DISP[tok], FAIL[tok], OBJ[tok]
        press = op == "=="
        d_term, d_open = term(dsig, init, fam)
        c_term, c_open = term(f"{msg}.{cmd}", out, fam, cmd=True)
        stage = ("three heated seat states" if fam == "Heated"
                 else "three vented seat states")
        step3 = (f"3. Press the {obj} icon and check that {c_term} is transmitted"
                 if press else
                 f"3. Send CAN: {d_term} without pressing any icon and check that "
                 f"{c_term} is transmitted")
        proc = [f"1. Send CAN: {fsig} = 0 (Fail_Not_Present)",
                (f"2. Send CAN: {d_term}" if press
                 else f"2. Send CAN: {dsig} = 0 ({LAB[fam][0]})"), step3]
        er = [f"1. {fsig} = 0 (Fail_Not_Present) is sent",
              (f"2. {d_term} is sent" if press
               else f"2. {dsig} = 0 ({LAB[fam][0]}) is sent"),
              f"3. {c_term} is sent"]
        lvl_out = out.rsplit("_", 1)[-1]
        tcs.append({
            "leaf_id": leaf, "test_set": l2,
            "tc_title": (f"{obj.capitalize()} at {init.rsplit('_', 1)[-1]} commands "
                         f"{lvl_out}"),
            "test_item": f"{source}\n\n(Three stage configuration, "
                         f"{'press request' if press else 'status transition'})",
            "pre_conditions": "\n".join([
                f"1. The vehicle is configured for {stage}",
                "2. The Heated / Vented Seats screen is displayed",
                "3. CAN-B is connected to the bus simulator"]),
            "input_test_data": "NA",
            "test_procedure": "\n".join(proc), "expected_result": "\n".join(er),
            "specification_reference": l2r[leaf]["reqid_list"].replace(";", "\n"),
            "design_method": ("決策表 (Decision Table Testing)" if press
                              else "狀態轉換 (State Transition Testing)"),
            "priority": "P1", "reasoning": (
                "P1：主要功能邏輯；本條之 `_mid` 值依 **A-VS104** 不可對映至 `_medium`"
                "（變母音之縮寫，無結構性判準，併 DR-18），"
                "依 **R-VS71** 值之未解不阻塞生成、依 **R-VS61** 取來源逐字不附 raw"),
            "split_flag": False, "split_reason": "", "dr15_exposed": "no",
            "dr_dependent": "DR-18" if (d_open or c_open) else "",
            "impl_gap": f"{msg}.{cmd}",
            "screen_pending": "no",
            "remarks": (f"BLOCKED: DR-18 —— `_mid` 之對映未解，其值取條文逐字；"
                        f"IMPL_GAP: {msg}.{cmd} —— 依 R-VS66(a) 開 issue 予 RD"),
            "distinguishing_axis": {"axis": "level",
                                    "delta": f"本列之初始階為 {init}、命令階為 {out}，"
                                             f"對象為 {tok}。"},
        })
    d = {"batch": "batch20", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
         "generated_round": 50, "handoff": "docs/handoff/77_split_and_full.md",
         "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
         "selection": "W-142 之池 83 中之 **A 型（IF/THEN 命令型）12 條** —— "
                      "其值皆含 `_mid`，依 R-VS71 照寫。",
         "signal_notation": "R-VS52 ＋ R-VS61（未解值取來源逐字，不附 raw）",
         "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
         "revision": "W-143(1)（50 輪）：batch20 首版",
         "tcs": tcs}
    (FEAT / "generated/batch20.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"batch20：{len(tcs)} 條")
    for t in tcs:
        print(f"  {t['priority']} {t['leaf_id']:46s} {t['tc_title']}")


if __name__ == "__main__":
    main()
