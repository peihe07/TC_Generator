"""63 包 §H 第 2 步 —— `-057` / `-065` 依 R-P376(b) 之丁案改寫入 corpus。

丁案（R-P374(c) / R-P376）：`RemStartFail` 為 HU 內部變數，
Procedure 改驅動 `CFTS009-4941504` 所載之上游 CAN 事件，
ER 改觀察同段落所載之下游效果（TLM 轉入 Standby）；
`RemStartFail` 自 Procedure / ER 移除，僅留 `test_item` 上半 verbatim。

R-P376(a) 之三要件（二條皆備）：
  (i)  上游事件與下游效果同載於 `4941504` 之同一段落
  (ii) 上游事件為 `$MESSAGE.Signal$`（BHCAN2 `VAL_ 854` / `VAL_ 1132`）
  (iii) 下游效果落 R-P353 白名單 (i)（`VAL_ 1470`）

⚠ R-P376(d)：本二條**不覆蓋 `RemStartFail` 內部值本身**，其代價入交付說明。

用法：
    python features/power/scripts/apply_r_p376_63.py [--dry-run]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
BATCHES = ROOT / "features/power/generated"

# 點火值取自 BHCAN2 `VAL_ 854 OperationalModeSts`
IGNITION = {
    "NR1L-PowerManagement-057": (2, "Ignition_Off"),
    "NR1L-PowerManagement-065": (10, "Ignition_Pre_Off"),
}

PRE = (
    "1. A LIN and CAN simulation tool is connected\n"
    "2. $STATUS_TELEMATIC.PowerSts_Telematic$ = 4 (Full_Operation)\n"
    "3. $STATUS_BH_BCM2.RemStActvSts$ = 1 (Remote Start Active)\n"
    "4. No phone call is in progress on the bench"
)
PROC = (
    "1. Send the signal $STATUS_BH_BCM1.OperationalModeSts$ = {raw} ({label})\n"
    "2. Send the signal $STATUS_BH_BCM2.RemStActvSts$ = 0 (Remote Start Not Active)\n"
    "3. Read the signal $STATUS_TELEMATIC.PowerSts_Telematic$ and check that it is 1 (Standby)"
)
ER = (
    "1. The signal value $STATUS_BH_BCM1.OperationalModeSts$ = {raw} ({label}) is received\n"
    "2. The signal value $STATUS_BH_BCM2.RemStActvSts$ = 0 (Remote Start Not Active) is received\n"
    "3. The signal value $STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby) is received"
)
BRACKET = ("(read $STATUS_TELEMATIC.PowerSts_Telematic$ "
           "-> The TLM passes to Standby)")
REMARK = ("(R-P376 丁案；原驗 RemStartFail 內部值，改驗其下游效果)")
NOTE = (
    "\n\n**R-P376 丁案改寫（63 包）**：`RemStartFail` 為 HU 內部變數，"
    "測試台無驅動與觀察方法（DR-PW23）。依 `CFTS009-4941504` 之同一段落，"
    "上游事件改以 `$STATUS_BH_BCM1.OperationalModeSts$` 與 "
    "`$STATUS_BH_BCM2.RemStActvSts$` 驅動，下游效果改觀察 "
    "`$STATUS_TELEMATIC.PowerSts_Telematic$ = 1 (Standby)`。"
    "**驗證對象由「內部變數之值」改為「其下游狀態轉移」**，"
    "本條不覆蓋 `RemStartFail` 內部值本身（R-P376(d)）。"
    "`test_item` 上半 verbatim 未改。"
)


def rewrite(tc: dict) -> dict:
    raw, label = IGNITION[tc["tc_id"]]
    item = tc["test_item"]
    head, sep, _ = item.rpartition("\n\n(")
    assert sep, f"{tc['tc_id']} 之 test_item 無括號下半"
    return {
        **tc,
        "test_item": f"{head}\n\n{BRACKET}",
        "pre_conditions": PRE,
        "input_test_data": "NA",
        "test_procedure": PROC.format(raw=raw, label=label),
        "expected_result": ER.format(raw=raw, label=label),
        "remarks": (tc.get("remarks") or "").strip() + (" " if tc.get("remarks") else "") + REMARK,
        "reasoning_note": (tc.get("reasoning_note") or "") + NOTE,
    }


def main() -> None:
    dry = "--dry-run" in sys.argv
    for path in sorted(BATCHES.glob("batch_*.json")):
        data = json.loads(path.read_text())
        hit = [t for t in data["tcs"] if t["tc_id"] in IGNITION]
        if not hit:
            continue
        data["tcs"] = [rewrite(t) if t["tc_id"] in IGNITION else t
                       for t in data["tcs"]]
        for t in data["tcs"]:
            if t["tc_id"] in IGNITION:
                print(f"### {t['tc_id']}")
                print("  PRE :", t["pre_conditions"].replace("\n", " | "))
                print("  ITD :", t["input_test_data"])
                print("  PROC:", t["test_procedure"].replace("\n", " | "))
                print("  ER  :", t["expected_result"].replace("\n", " | "))
                print("  括號:", t["test_item"].rsplit("\n\n", 1)[-1])
        if not dry:
            path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            print(f"→ 寫回 {path.relative_to(ROOT)}")
        else:
            print("（dry-run，未寫回）")


if __name__ == "__main__":
    main()
