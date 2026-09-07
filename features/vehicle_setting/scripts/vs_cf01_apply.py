#!/usr/bin/env python3
"""VS-CF-01 §2 —— CFTS044 工作簿 PENDING 甲類 13 列改寫（沙盒稿）。

來源：`docs/fw036/handoff/down/20260907_VS-CF-01.md`（Pei「是準」2026-09-07）。

**只寫 `features/vehicle_setting/sandbox/cfts044/`。不動母本、不動 `inputs/`、
不動 `output/` 之既有簿。** 寫入路徑一律 `backend/xlsx_surgical.surgical_save()`
（`Workbook.save()` 會毀 x14 dataValidation，R16／R-G3），全域無 `wb.save()`。

流程：
  1. 母本 → `sandbox/cfts044/cfts044_20260819.xlsx`（sha 須 = f39c03bd…）
  2. openpyxl 為計算層，逐列逐欄改（§2.1–§2.7）
  3. `surgical_save` 產 `cfts044_20260819_Revise1.xlsx`
  4. 落檔前 assert：觸及列之 L／M 步數相等；PENDING 列數 25 → 12
"""

from __future__ import annotations

import re
import shutil
import subprocess
import sys
import warnings
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "backend"))
from xlsx_surgical import surgical_save  # noqa: E402

warnings.filterwarnings("ignore")

MASTER = Path(
    "/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/"
    "Vehicle Settings/CFTS044/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_"
    "SWQT STLA Test Case Specification & Result_SWQT_CFTS044_Vehicle Controls_"
    "20260819.xlsx")
MASTER_SHA16 = "f39c03bd9cb0f1b3"
SB = ROOT / "features/vehicle_setting/sandbox/cfts044"
WORK = SB / "cfts044_20260819.xlsx"
OUT = SB / "cfts044_20260819_Revise1.xlsx"
SHEET = "Test Case Specification 測試用例規範"

C = {"F": 6, "I": 9, "J": 10, "K": 11, "L": 12, "M": 13,
     "N": 14, "P": 16, "R": 18, "AH": 34}

# --------------------------------------------------------------- §2.2 樣板

NOTGEN = ("NOT GENERATED: B7-no-invalid-raw —— {sig} 為 {n} bit，"
          "raw 全數已定義且皆在宣告有效集內，匯流排上無可送之無效值；"
          "R-VS102(2)；DR 草稿見 DATA_REQUESTS.md（未取號）")
NOTGEN_ROWS = {
    64: ("STATUS_CSWM.FL_HS_STATSts", 2),
    80: ("STATUS_CSWM.FR_HS_STATSts", 2),
    151: ("STATUS_CSWM.FL_VS_STATSts", 2),
    166: ("STATUS_CSWM.FR_VS_STATSts", 2),
    225: ("STATUS_CSWM.HSW_StatSts", 1),
}
NOTGEN_CLEAR = ("I", "J", "K", "L", "M", "P", "R")

AH_TWO_STATE = ("R-VS102(1): two-state vehicle (Off/Low/High); "
                "raw 2 lies outside the declared valid set")
AH_DR19_PAIR = ("dr_dependent = DR-19（R-VS102(3)）：$EngRun_Stat$ 非運轉態以 "
                "EngineSts = 0 對照，覆後複檢")
AH_DR19_SEED = ("dr_dependent = DR-19（R-VS102(3)）：$EngRun_Stat$ 以 EngineSts "
                "對照，覆後複檢")

TOUCHED = [10, 11, 12, 13, 14, 15, 16, 25, 26, 28, 44, 62, 63, 64, 68, 79, 80,
           84, 151, 155, 166, 170, 225]
# L／M 步數相等之硬規只對「仍有步驟」之列施行（§2.2 之 5 列已清空）
STEP_CHECK = [r for r in TOUCHED if r not in NOTGEN_ROWS
              and r not in (10, 11, 12, 13, 16, 68, 84, 155, 170)]


def sha16(p: Path) -> str:
    return subprocess.run(["shasum", "-a", "256", str(p)],
                          capture_output=True, text=True,
                          check=True).stdout[:16]


def steps(text) -> list[str]:
    """去序號之步驟清單。"""
    return [re.sub(r"^\s*\d+\.\s*", "", x).strip()
            for x in str(text or "").split("\n") if x.strip()]


def set_step(ws, row: int, col: str, idx: int, text: str) -> None:
    """改寫第 `idx` 步（1-based），其餘步逐字不動。"""
    cell = ws.cell(row, C[col])
    lines = [x for x in str(cell.value or "").split("\n") if x.strip()]
    assert len(lines) >= idx, f"r{row}{col} 只有 {len(lines)} 步，要改第 {idx} 步"
    assert lines[idx - 1].lstrip().startswith(f"{idx}."), \
        f"r{row}{col} 第 {idx} 行非 `{idx}.` 起首：{lines[idx - 1]!r}"
    lines[idx - 1] = text
    cell.value = "\n".join(lines)


def set_cell(ws, row: int, col: str, value) -> None:
    ws.cell(row, C[col]).value = value


def apply_all(ws) -> None:
    # ---------------------------------------------------- §2.1 兩態，補無效 raw
    for row, sig in ((63, "FL_HS_STATSts"), (79, "FR_HS_STATSts")):
        set_step(ws, row, "L", 2,
                 f"2. Send CAN: STATUS_CSWM.{sig} = 2 (Heated_seat_medium)")
        set_step(ws, row, "M", 2,
                 f"2. STATUS_CSWM.{sig} = 2 (Heated_seat_medium) is sent")
        set_cell(ws, row, "AH", AH_TWO_STATE)

    # ------------------------------------------- §2.2 全定義 → 不生成並具名
    for row, (sig, n) in NOTGEN_ROWS.items():
        for col in NOTGEN_CLEAR:
            set_cell(ws, row, col, None)
        set_cell(ws, row, "AH", NOTGEN.format(sig=sig, n=n))

    # ------------------------------------- §2.3 row 62 改對 PROXI Heated_Seat_Levels
    set_cell(ws, 62, "J",
             "1. The vehicle is equipped with the heated seat\n"
             "2. The Heated / Vented Seats screen is displayed")
    set_cell(ws, 62, "K", "NA")
    set_cell(ws, 62, "L",
             "1. PROXI Heated_Seat_Levels = 2 (3 Levels)\n"
             "2. Power cycle the HU and record the number of heated seat levels "
             "shown as Levels_valid\n"
             "3. PROXI Heated_Seat_Levels = 3\n"
             "4. Power cycle the HU and check that the number of heated seat "
             "levels shown is unchanged from Levels_valid")
    set_cell(ws, 62, "M",
             "1. PROXI Heated_Seat_Levels = 2 (3 Levels) is accepted\n"
             "2. Levels_valid is recorded\n"
             "3. PROXI Heated_Seat_Levels = 3 is accepted\n"
             "4. The number of heated seat levels shown is unchanged from "
             "Levels_valid")
    set_cell(ws, 62, "R", "負向測試 (Negative / Invalid)")
    set_cell(ws, 62, "AH",
             "R-VS102(1)：PROXI Heated_Seat_Levels raw 3 未定義（Format 列 760）；"
             "ER 依 invalid-ignored 範式；上游若覆無效 PROXI 之行為另有規定則複檢")

    # ------------------------------------------------------ §2.4 DR-19 對照
    set_step(ws, 14, "L", 3,
             "3. Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off)")
    set_step(ws, 14, "M", 3,
             "3. STATUS_CCAN3.EngineSts = 0 (Engine_Off) is sent")
    set_step(ws, 15, "L", 2,
             "2. Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off)")
    set_step(ws, 15, "M", 2,
             "2. STATUS_CCAN3.EngineSts = 0 (Engine_Off) is sent")
    for row in (14, 15):
        set_cell(ws, row, "AH", AH_DR19_PAIR)
    for row in (10, 11, 12, 13):
        assert ws.cell(row, C["AH"]).value is None, f"r{row} AH 非空，停手"
        set_cell(ws, row, "AH", AH_DR19_SEED)
    for row in (16, 68, 84, 155, 170):
        cur = str(ws.cell(row, C["AH"]).value or "")
        assert cur.startswith("BLOCKED: DR-19 —— "), f"r{row} AH 前綴不符：{cur[:40]!r}"
        set_cell(ws, row, "AH",
                 "dr_dependent = DR-19 —— " + cur[len("BLOCKED: DR-19 —— "):])

    # ---------------------------------------------------------- §2.5 DR-21
    set_step(ws, 26, "M", 2,
             "2. STATUS_BH_BCM2.CmdIgnSts = 5 (START) is sent")
    set_cell(ws, 26, "AH",
             "dr_dependent = DR-21（R-VS102(4)）：IGN_START 對照 5 (START)，覆後複檢")
    set_step(ws, 28, "L", 2, "2. PENDING: DR-21 IGN_OFF_ACC bus value")
    set_cell(ws, 28, "AH",
             "BLOCKED: DR-21 —— IGN_OFF_ACC 於 DBC 無對應；"
             "DR-21 逐實例條文尚未送出（台帳）")

    # ------------------------------------------------------ §2.6 別名（DR-22）
    set_step(ws, 25, "M", 2, "2. PROXI VC_HdRstPrsnt = 1 (Present) is accepted")
    set_cell(ws, 25, "AH",
             "alias（R-13／R-VS102(5)）：VC_HdRstPrsnt ≡ Headrest_Dump_Present"
             "（PROXI_HDCC27_R3 Format 列 780，0 Absent／1 Present；HDCC27 標 Not Used）")
    set_step(ws, 44, "M", 2, "2. PROXI DSP_SK_PRSNT = 1 (Present) is accepted")
    set_cell(ws, 44, "AH",
             "alias（R-13／R-VS102(5)）：DSP_SK_PRSNT ≡ Display_OFF_SoftKey"
             "（Format 列 692，0 Absent／1 Present；HDCC27 為 Set to 0）")

    # ------------------------------------- §2.7 順手：只限本包觸及之列之全形分號
    for row in TOUCHED:
        for col in ("L", "M"):
            cur = ws.cell(row, C[col]).value
            if cur and "；" in str(cur):
                set_cell(ws, row, col, str(cur).replace("；", ";"))


def assert_gates(ws) -> dict:
    for row in STEP_CHECK:
        a, b = len(steps(ws.cell(row, C["L"]).value)), len(steps(ws.cell(row, C["M"]).value))
        assert a == b, f"r{row} 步數不等：Test procedure {a} vs Expected Result {b}"
    pend = []
    for r in range(10, ws.max_row + 1):
        blob = (str(ws.cell(r, C["L"]).value or "") + "\n"
                + str(ws.cell(r, C["M"]).value or ""))
        if "PENDING" in blob:
            drs = sorted(set(re.findall(r"PENDING:\s*(DR-\d+)", blob)))
            pend.append((r, str(ws.cell(r, C["F"]).value), ",".join(drs) or "?"))
    assert len(pend) == 12, f"PENDING 應為 12 列，實得 {len(pend)}：{pend}"
    return {"pending": pend}


def main() -> int:
    assert MASTER.exists(), f"母本不存在：{MASTER}"
    got = sha16(MASTER)
    assert got == MASTER_SHA16, f"母本 sha16 {got} ≠ {MASTER_SHA16}，停手"
    SB.mkdir(parents=True, exist_ok=True)
    shutil.copy2(MASTER, WORK)
    assert sha16(WORK) == MASTER_SHA16, "沙盒副本 sha 不符，停手"

    wb = openpyxl.load_workbook(WORK)
    ws = wb[SHEET]
    apply_all(ws)
    res = assert_gates(ws)
    report = surgical_save(wb, WORK, OUT)      # **不呼叫 wb.save()**

    print(f"母本   sha16 {MASTER_SHA16}")
    print(f"沙盒本 {WORK.relative_to(ROOT)}  sha16 {sha16(WORK)}")
    print(f"Revise1 {OUT.relative_to(ROOT)}  sha16 {sha16(OUT)}")
    print(f"surgical_save: {report}")
    print(f"PENDING 25 → {len(res['pending'])}")
    for x in res["pending"]:
        print("   ", x)
    return 0


if __name__ == "__main__":
    sys.exit(main())
