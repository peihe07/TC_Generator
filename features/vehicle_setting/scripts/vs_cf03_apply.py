#!/usr/bin/env python3
"""VS-CF-03 —— CFTS044 出貨版 Revise2：237/237 全生成、PENDING 0、DR 0。

來源：`docs/fw036/handoff/down/20260908_VS-CF-03.md`（Pei 裁定 2026-09-08）。

**只寫 `features/vehicle_setting/sandbox/cfts044/`。** 落檔一律
`backend/xlsx_surgical.surgical_save()`，全域無 `wb.save()`（R16／R-G3）。
基準 `cfts044_20260819_Revise1.xlsx`（sha256 f444028d…），Revise1 不改（R-G72）。

生成之唯一來源鏈（下放包 §一）：037 SWRA `Analysis Report` D 欄為第一來源，
Q 欄為驗證手段之來源；`test_item` 上半取 N 欄 ObjectID 對應之 CFTS 原句 verbatim。

`surgical_save` 為 cell-diff 落檔器，無刪列能力；§四 之刪 2 列以
「內容上移 ＋ 尾 2 列清空」為之，資料列（F 欄非空）由 243 降為 241。
"""

from __future__ import annotations

import csv
import json
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

FEAT = ROOT / "features/vehicle_setting"
SB = FEAT / "sandbox/cfts044"
BASE = SB / "cfts044_20260819_Revise1.xlsx"
OUT = SB / "cfts044_20260819_Revise2.xlsx"
REMAP = FEAT / "reports/cfts044_tcid_remap.tsv"
SHEET = "Test Case Specification 測試用例規範"
BASE_SHA = "f444028d1cd93396738b4225ef6ce5de0ad3d41675d66f16acb0d099c8ef44a1"

SWRA = sorted((FEAT / "inputs").glob("*037*CFTS044*.xlsx"))
CFTS_SRC = (FEAT / "inputs" / "SYS2  R1LR_Atl-H_25PI1.1_Activation and "
            "Configuration_CFTS_044_Vehicle Controls_SR26_20250815-1022_"
            "20260324_Version3_Released.xlsx")

C = {"B": 2, "D": 4, "F": 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11,
     "L": 12, "M": 13, "N": 14, "O": 15, "P": 16, "R": 18, "S": 19, "AH": 34}
AUTHOR_COLS = ("J", "K", "L", "M")
FIRST, LAST = 10, 252

EP = "等價劃分 (Equivalence Partitioning, EP)"
DT = "決策表 (Decision Table Testing)"
ST = "狀態轉換 (State Transition Testing)"
FN = "功能測試 (Functional based ; no specific technique)"
FI = "基礎故障注入 (Fault Injection Lite)"
NEG = "負向測試 (Negative / Invalid)"

DEL_ROWS = (23, 48)          # §四：與 24／49 之保留列重複
COMFORT = 'Press "Comfort" on Menu Bar'


# --------------------------------------------------------------- 來源讀取

def sha256(p: Path) -> str:
    return subprocess.run(["shasum", "-a", "256", str(p)],
                          capture_output=True, text=True,
                          check=True).stdout.split()[0]


def load_swra() -> dict:
    """037 Analysis Report：SWE-Requirement ID -> {D, Q, R, file, row}。"""
    idx: dict[str, dict] = {}
    for f in SWRA:
        tag = f.name.split("SWRA_")[-1].replace(".xlsx", "")
        ws = openpyxl.load_workbook(f, read_only=True)["Analysis Report"]
        for r in range(8, ws.max_row + 1):
            a = ws.cell(r, 1).value
            if not a:
                continue
            key = str(a).strip()
            assert key not in idx, f"037 leaf 重複：{key}"
            idx[key] = {"file": tag, "row": r, "D": ws.cell(r, 4).value,
                        "Q": ws.cell(r, 17).value, "R": ws.cell(r, 18).value}
    return idx


def load_cfts() -> dict:
    """CFTS044 SYS2 Basic Report：7 位 ObjectID -> 原句。"""
    ws = openpyxl.load_workbook(CFTS_SRC, read_only=True)["Basic Report"]
    d: dict[str, str] = {}
    for r in range(2, ws.max_row + 1):
        oid, desc = ws.cell(r, 5).value, ws.cell(r, 3).value
        if oid is None:
            continue
        for one in str(oid).replace(",", " ").split():
            d[one.strip()] = clean_src(desc)
    return d


def clean_src(text) -> str:
    """CFTS 原句正規化：去 `_x000D_`、外層引號、成對雙引號，行首尾空白。"""
    s = str(text or "").replace("_x000D_\n", "\n").replace("_x000D_", "\n")
    s = s.replace("\xa0", " ").strip()
    if s.startswith('"') and s.endswith('"'):
        s = s[1:-1]
    s = s.replace('""', '"')
    return "\n".join(ln.strip() for ln in s.split("\n") if ln.strip()).strip()


SWRA_IDX = load_swra()
CFTS = load_cfts()


def d_of(req: str) -> str:
    return str(SWRA_IDX[req]["D"] or "")


def cfts(oid: str) -> str:
    return CFTS[oid]


# --------------------------------------------------------------- 書寫樣板

def api_set(sig: str, label: str) -> tuple[str, str]:
    """API 層設定（§一(b)）：`Set $Sig$ = [Label]`。"""
    return f"Set ${sig}$ = {label}", f"${sig}$ = {label} is accepted"


def api_read(sig: str, label: str) -> tuple[str, str]:
    """API 層讀取（§一(b)）：`Read $Sig$ and check that it is [Label]`。"""
    return (f"Read ${sig}$ and check that it is {label}",
            f"${sig}$ reads {label}")


def can_send(sig: str, raw: int, label: str) -> tuple[str, str]:
    """確為 CAN 之訊號維持 profile R-VS52(1) 之作者側記法。"""
    return (f"Send CAN: {sig} = {raw} ({label})",
            f"{sig} = {raw} ({label}) is sent")


def numbered(items: list[str]) -> str:
    return "\n".join(f"{i}. {t}" for i, t in enumerate(items, 1))


def item(upper: str, tag: str) -> str:
    """test_item 兩段式（R-S4）：上半 verbatim、下半英文情境標籤。"""
    return f"{upper.strip()}\n\n({tag})"


# --------------------------------------------------------------- 逐列規格

def steps(pairs: list[tuple[str, str]]) -> tuple[str, str]:
    return numbered([a for a, _ in pairs]), numbered([b for _, b in pairs])


def cfg_gate(sig: str, ok: str, tag: str, upper: str, control: str,
             other: str | None) -> dict:
    """§2.1 組態閘控之正負成對範式。`other` 為 None 時用不造值之對立式。"""
    neg = f"Set ${sig}$ = {other}" if other else \
        f"Set ${sig}$ to a value other than {ok}"
    neg_er = (f"${sig}$ = {other} is accepted" if other else
              f"${sig}$ is set to a value other than {ok}")
    proc, er = steps([
        api_set(sig, ok),
        (f'Power cycle the HU and {COMFORT[0].lower() + COMFORT[1:]}',
         'The "Comfort" screen is displayed'),
        (f"Read the {control} and record its presence as Control_qualifying",
         "Control_qualifying is recorded as displayed"),
        (neg, neg_er),
        (f'Power cycle the HU, {COMFORT[0].lower() + COMFORT[1:]} and check '
         f"that the {control} is not displayed",
         f"The {control} is not displayed"),
    ])
    return {"I": item(upper, tag),
            "J": numbered(["The HU is in its delivered configuration",
                           "The configuration parameters are writable through "
                           "the VHAL interface"]),
            "K": "NA", "L": proc, "M": er, "P": "P1", "R": EP}


def spec(rows_map: dict) -> dict:
    return rows_map


# =====================================================================
#  §2.1 組態閘控型 —— 9 列
# =====================================================================

HS_CTRL = "heated seat control"
VS_CTRL = "vented seat control"

CFG_SINGLE = {
    93:  ("Heated_Seats", "[Front Seats]", "4859360", HS_CTRL,
          "One stage config gate: heated seats present vs absent"),
    107: ("Heated_Seats", "[Front Seats]", "4859376", HS_CTRL,
          "Two stages config gate: heated seats present vs absent"),
    127: ("Heated_Seats", "[Front Seats]", "4859400", HS_CTRL,
          "Three stages config gate: heated seats present vs absent"),
    179: ("Cooled_Seats", '"Front Seats"', "4859438", VS_CTRL,
          "Two stages config gate: cooled seats present vs absent"),
    199: ("Cooled_Seats", '"Front Seats"', "4859464", VS_CTRL,
          "Three stages config gate: cooled seats present vs absent"),
}

# 雙條件列：第一條件維持合格，只翻第二條件（§8.3 一次一驗證點）
CFG_DUAL = {
    108: ("Heated_Seats", "[Front Seats]", "Heated_Seats_Levels",
          "[Two Levels]", "4859377", HS_CTRL,
          "Two stages level gate: two levels vs other level count"),
    128: ("Heated_Seats", "[Front Seats]", "Heated_Seats_Levels",
          "[Three Levels]", "4859401", HS_CTRL,
          "Three stages level gate: three levels vs other level count"),
    180: ("Cooled_Seats", '"Front Seats"', "Heated_Steats_Levels",
          '"Two Levels"', "4859439", VS_CTRL,
          "Two stages vented level gate: two levels vs other level count"),
    200: ("Cooled_Seats", '"Front Seats"', "Heated_Steats_Levels",
          '"Three Levels"', "4859465", VS_CTRL,
          "Three stages vented level gate: three levels vs other level count"),
}


def build_cfg() -> dict:
    out = {}
    for row, (sig, ok, oid, ctrl, tag) in CFG_SINGLE.items():
        out[row] = cfg_gate(sig, ok, tag, cfts(oid), ctrl, None)
        out[row]["AH"] = (
            "037 Q 欄為 \"Requirement is not clear\"；TC 依 D 欄之行為敘述生成"
            "（下放包 §一(c)）。訊號名與值標籤取自 037 "
            f"{SWRA_IDX[req_of(row)]['file']} D 欄；step 4 之非合格值不造具體值"
            "（§8.4.1）")
    for row, (g1, v1, g2, v2, oid, ctrl, tag) in CFG_DUAL.items():
        proc, er = steps([
            api_set(g1, v1),
            api_set(g2, v2),
            (f'Power cycle the HU and press "Comfort" on Menu Bar',
             'The "Comfort" screen is displayed'),
            (f"Read the {ctrl} and record its presence as Control_qualifying",
             "Control_qualifying is recorded as displayed"),
            (f"Set ${g2}$ to a value other than {v2}",
             f"${g2}$ is set to a value other than {v2}"),
            (f'Power cycle the HU, press "Comfort" on Menu Bar and check that '
             f"the {ctrl} is not displayed",
             f"The {ctrl} is not displayed"),
        ])
        out[row] = {
            "I": item(cfts(oid), tag),
            "J": numbered(["The HU is in its delivered configuration",
                           "The configuration parameters are writable through "
                           "the VHAL interface"]),
            "K": "NA", "L": proc, "M": er, "P": "P1", "R": DT,
            "AH": ("037 Q 欄為 \"Requirement is not clear\"；TC 依 D 欄之行為敘述"
                   "生成（下放包 §一(c)）。雙條件列之負向側只翻第二條件，"
                   f"第一條件 ${g1}$ = {v1} 維持合格（§8.3）；"
                   "非合格值不造具體值（§8.4.1）"
                   + ("。CFTS 原句之拼字 `Steats` 與 037 D 欄一致，照抄不改"
                      if "Steats" in g2 else
                      "。CFTS 原句作 `Heated_Steats_Levels`，037 D 欄作 "
                      "`Heated_Seats_Levels`；上半從 CFTS verbatim，"
                      "步驟從 D 欄（§一(a)）")),
        }
    return out


# =====================================================================
#  §2.2 故障圖示型 —— row 94
# =====================================================================

def build_fault_icon() -> dict:
    d = d_of("SWE1-VC-OneStageHeatedSeat-040")
    upper = [ln.strip() for ln in d.split("\n")
             if ln.strip().startswith("Regardless of the value")][0]
    proc, er = steps([
        can_send("STATUS_CSWM.FR_HS_STATFailSts", 0, "Fail_Not_Present"),
        api_set("HeatedSeatFR", "[HS_HI]"),
        ("Read the right front heated seat icon and record it as Icon_no_fail",
         "Icon_no_fail is recorded"),
        can_send("STATUS_CSWM.FR_HS_STATFailSts", 1, "Fail_Present"),
        ("Read the right front heated seat icon and check that it differs "
         "from Icon_no_fail",
         "The right front heated seat icon differs from Icon_no_fail"),
    ])
    return {94: {
        "I": item(upper, "Fail_Present overrides the seat state icon"),
        "J": numbered(["The vehicle is equipped with the right front heated seat",
                       'The "Comfort" screen is displayed',
                       "CAN-B is connected to the bus simulator"]),
        "K": "NA", "L": proc, "M": er, "P": "P1", "R": FI,
        "AH": ("test_item 上半取 037 HeatedSeat D 欄末句（N 欄 ObjectID 4859361 之 "
               "CFTS 原句為前言式，與 D 欄之可測行為不對應，依下放包 §二 之 "
               "fallback 取 D 欄之行為句並具名）。`Regardless of` 以 baseline 覆蓋"
               "（§5.6）；baseline 之非 OFF 值 [HS_HI] 取自同節 leaf -024 之 D 欄與 "
               "CFTS 原句（§一(d)）；TLM HMI Document 未附，ER 只寫圖示改變，"
               "不寫改成什麼"),
    }}


# =====================================================================
#  §2.3 請求／釋放型 —— 5 列
# =====================================================================

TSEND = "<Tsend> 無上限值，本列不驗時限（下放包 §2.3）"


def build_request() -> dict:
    out = {}

    # row 87 —— $FR_HS_RQ$ = [HS_NOT_PSD]，於 [HS_PSD] 之後
    proc, er = steps([
        api_read("FR_HS_RQ", "[HS_NOT_PSD]"),
        ("Press and release the right front heated seat control",
         "The right front heated seat control registers the press and the release"),
        ("Read $FR_HS_RQ$ and check that it is [HS_PSD] followed by [HS_NOT_PSD]",
         "$FR_HS_RQ$ reads [HS_PSD] followed by [HS_NOT_PSD]"),
    ])
    out[87] = {"L": proc, "M": er, "R": ST,
               "AH": f"訊號名與值標籤取自 037 HeatedSeat D 欄（$FR_HS_RQ$／"
                     f"[HS_PSD]／[HS_NOT_PSD]）；{TSEND}"}

    # row 173 —— $FR_VS_RQ_TGW$ = [Vented Seat Pressed / VS_PSD]
    proc, er = steps([
        api_read("FR_VS_RQ_TGW", "[Not Pressed / VS_NOT_PSD]"),
        ("Press the right front vented seat control",
         "The right front vented seat control registers the press"),
        ("Read $FR_VS_RQ_TGW$ and check that it is "
         "[Vented Seat Pressed / VS_PSD]",
         "$FR_VS_RQ_TGW$ reads [Vented Seat Pressed / VS_PSD]"),
    ])
    out[173] = {"L": proc, "M": er, "R": ST,
                "AH": "訊號名與值標籤取自 037 VentedSeat D 欄（$FR_VS_RQ_TGW$／"
                      "[Vented Seat Pressed / VS_PSD]）；step 1 之 "
                      "[Not Pressed / VS_NOT_PSD] 取自同 leaf 之 test_item 上半 "
                      f"verbatim（§一(d)）；{TSEND}"}

    # row 233／234 —— 同 Req（HeatedSteeringWheel-013），括號下半須相異
    proc, er = steps([
        api_read("HSW_RQ_TGW", "[NOT Pressed / NOT_PSD]"),
        ("Press and release the heated steering wheel button",
         "The heated steering wheel button registers the press and the release"),
        ("Read $HSW_RQ_TGW$ and check that it is [PSD] followed by "
         "[NOT Pressed / NOT_PSD]",
         "$HSW_RQ_TGW$ reads [PSD] followed by [NOT Pressed / NOT_PSD]"),
    ])
    out[233] = {"L": proc, "M": er, "R": ST,
                "tag": "Release follows the press on the button",
                "AH": "訊號名與值標籤取自 037 Heated_Steering_Wheel D 欄"
                      f"（$HSW_RQ_TGW$／[NOT Pressed / NOT_PSD]）；{TSEND}"}

    proc2, er2 = steps([
        api_read("HSW_RQ_TGW", "[NOT Pressed / NOT_PSD]"),
        ("Press and release the heated steering wheel control on the "
         '"Comfort" screen',
         "The heated steering wheel control registers the press and the release"),
        ("Read $HSW_RQ_TGW$ and check that it has returned to "
         "[NOT Pressed / NOT_PSD]",
         "$HSW_RQ_TGW$ reads [NOT Pressed / NOT_PSD] after the release"),
    ])
    out[234] = {"L": proc2, "M": er2, "R": ST,
                "tag": "Request returns to NOT_PSD after the release",
                "AH": "訊號名與值標籤取自 037 Heated_Steering_Wheel D 欄；"
                      "本列與 row 233 同 Req，括號下半以「回復終態」區分"
                      f"（R-S4）；{TSEND}"}

    # row 235 —— signal mapping 未附，只驗 toggle 之狀態變化
    proc3, er3 = steps([
        ("Read $HSW_Stat_2$ and record it as HSW_Stat_before",
         "HSW_Stat_before is recorded"),
        ("Press the heated steering wheel control",
         "The heated steering wheel control registers the press"),
        ("Read $HSW_Stat_2$ and check that it has changed from the "
         "recorded value",
         "$HSW_Stat_2$ differs from HSW_Stat_before"),
    ])
    out[235] = {"L": proc3, "M": er3, "R": ST,
                "AH": "D 欄指向未附之 signal mapping；本列驗 toggle 之狀態變化，"
                      "不驗送出值（下放包 §2.3）"}
    return out


# =====================================================================
#  §2.4 HSW 命令型 —— 4 列
# =====================================================================

def build_hsw_cmd() -> dict:
    out = {}
    pre = numbered(["The vehicle is equipped with the heated steering wheel",
                    'The "Comfort" screen is displayed',
                    "CAN-B is connected to the bus simulator"])
    for row, stat, cmd, oid in ((245, "OFF", "ON", "4859496"),
                                (246, "ON", "OFF", "4859497")):
        proc, er = steps([
            api_set("HSW_Stat", stat),
            can_send("STATUS_CSWM.HSW_StatFailSts", 0, "Fail_Not_Present"),
            ("Press the heated steering wheel control to drive "
             "SteeringWheelHeating.Req to Requested",
             "SteeringWheelHeating.Req is driven to Requested"),
            api_read("HSW_Cmd_Tlm", cmd),
        ])
        out[row] = {
            "I": item(cfts(oid),
                      f"User request with $HSW_Stat$ = {stat} and no fault"),
            "J": pre, "K": "NA", "L": proc, "M": er, "P": "P1", "R": DT,
            "AH": "三條件合取，值域取自 037 Heated_Steering_Wheel D 欄"
                  "（$HSW_Stat$／$HSW_StatFailSts$／SteeringWheelHeating.Req）。"
                  "$HSW_StatFailSts$ 於基線 DBC 有同名訊號，"
                  "維持 CAN 記法；$HSW_Stat$／$HSW_Cmd_Tlm$ 為 API 層（§一(b)）",
        }
    for row, stat, cmd, oid, tag in (
            (249, "[ON]", "ON", "4859500",
             "State transition to ON drives the command"),
            (250, "[OFF]", "OFF", "4859501",
             "State observed as OFF drives the command")):
        first = "[OFF]" if stat == "[ON]" else "[ON]"
        proc, er = steps([
            api_set("HSW_Stat", first),
            (f"Set $HSW_Stat$ = {stat} without pressing any control",
             f"$HSW_Stat$ = {stat} is accepted"),
            api_read("HSW_Cmd_Tlm", cmd),
        ])
        out[row] = {
            "I": item(cfts(oid), tag), "J": pre, "K": "NA",
            "L": proc, "M": er, "P": "P1", "R": ST,
            "AH": "狀態變化觸發（非使用者請求），與 row 245／246 之觸發來源相異；"
                  "值域取自 037 Heated_Steering_Wheel D 欄",
        }
    return out


# =====================================================================
#  §2.6 其餘 4 列
# =====================================================================

def build_misc() -> dict:
    out = {}

    # row 56 —— PHEV 章節層條文，依 Q 欄生成薄 TC
    proc, er = steps([
        ("Set PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle)",
         "PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle) is accepted"),
        ("Power cycle the HU", "The HU completes start-up"),
        ('Press "Hybrid Electric" button and check that the PHEV feature '
         "pages are displayed on the HU",
         "The PHEV feature pages are displayed on the HU"),
    ])
    out[56] = {
        "I": item(cfts("4859529"), "PHEV pages viewable on the Head Unit"),
        "J": numbered(["The vehicle is a plug-in hybrid electric vehicle",
                       "The HU is in its delivered configuration"]),
        "K": "NA", "L": proc, "M": er, "P": "P2", "R": FN,
        "AH": "037 D 欄僅章節描述；依 Q 欄（CAN signal to be trigger／System "
              "update CAN value to HMI／HMI change the display state to new）"
              "生成一條薄 TC，本列為章節層條文（下放包 §2.6）",
    }

    # row 69／230／252 —— Stop-Start 相關之開關行為
    for row, oid, side, tag, req in (
            (69, "4858317", "left front heated seat",
             "Engine stopped with Stop-Start equipped",
             "SWE1-VC-LeftFrontHeatedSeat-011"),
            (230, "4858529", "heated steering wheel",
             "Engine stopped with Stop-Start equipped: steering wheel",
             "SWE1-VC-HeatedSteeringWheel-010")):
        proc, er = steps([
            can_send("STATUS_CCAN3.EngineSts", 2, "Engine_On"),
            (f"Read the {side} control and record its state as Control_running",
             "Control_running is recorded"),
            can_send("STATUS_CCAN3.EngineSts", 0, "Engine_Off"),
            (f"Read the {side} control and check that its state differs from "
             "Control_running",
             f"The {side} control state differs from Control_running"),
        ])
        out[row] = {
            "I": item(cfts(oid), tag),
            "J": numbered(["The vehicle is equipped with the Stop-Start feature",
                           'The "Comfort" screen is displayed',
                           "CAN-B is connected to the bus simulator"]),
            "K": "NA", "L": proc, "M": er, "P": "P1", "R": ST,
            "AH": "轉指條文之不生成處置撤回；依 037 " + SWRA_IDX[req]["file"] +
                  " Q 欄（Set the Start-Stop available CAN signal to be "
                  "trigger／System update CAN value）生成。$EngRun_Stat$ 依 037 "
                  "D 欄之對照以 STATUS_CCAN3.EngineSts 觀察；開關行為之具體樣式"
                  "未附，ER 只寫狀態相異",
        }

    # row 252 —— 無 CFTS044 ObjectID（037 Source 為 SYS-RA-CFTS100，DR-11）
    d252 = d_of("SWE1-VC-HeatedSteeringWheel-009")
    upper252 = [ln.strip() for ln in d252.split("\n")
                if ln.strip().startswith("For vehicles not equipped")][0]
    proc, er = steps([
        can_send("STATUS_CCAN3.EngineSts", 2, "Engine_On"),
        ("Read the heated steering wheel control and check that it is "
         "selectable",
         "The heated steering wheel control is selectable"),
        can_send("STATUS_CCAN3.EngineSts", 0, "Engine_Off"),
        ("Read the heated steering wheel control and check that it is "
         "disabled and shown greyed-out",
         "The heated steering wheel control is disabled and shown greyed-out"),
    ])
    out[252] = {
        "I": item(upper252, "Stop-Start not equipped: control greyed-out"),
        "J": numbered(["The vehicle is not equipped with the Stop-Start feature",
                       'The "Comfort" screen is displayed',
                       "CAN-B is connected to the bus simulator"]),
        "K": "NA", "L": proc, "M": er, "P": "P1", "R": ST,
        "AH": "本 leaf 之 037 Source Requirement ID 為 SYS-RA-CFTS100（非 "
              "CFTS044），無 CFTS044 ObjectID 可錨（DR-11），"
              "specification_reference 留空並具名；test_item 上半依下放包 §二 之 "
              "fallback 取 037 D 欄之行為句。依 Q 欄生成",
    }
    return out


# =====================================================================
#  B7 五列 —— R-VS102(2) 撤回後之重生成（下放包 §〇「未生成列 → 0」）
# =====================================================================

B7 = {
    64:  ("HeatedSeatFL", "4858308", "left front heated seat",
          ["[Heated Seat Off / HS_OFF]", "[Heated Seat Low / HS_LO]",
           "[Heated Seat Medium / HS_MED]", "[Heated Seat High / HS_HI]"],
          ["Off", "Low", "Medium", "High"],
          "Valid value set accepted, others ignored"),
    80:  ("HeatedSeatFR", "4858338", "right front heated seat",
          ["[Heated Seat Off / HS_OFF]", "[Heated Seat Low / HS_LO]",
           "[Heated Seat Medium / HS_MED]", "[Heated Seat High / HS_HI]"],
          ["Off", "Low", "Medium", "High"],
          "Valid value set accepted, others ignored: passenger side"),
    151: ("VentedSeatFL", "4858368", "left front vented seat",
          ["[Vented Seat Off / VS_OFF]", "[Vented Seat Low / VS_LO]",
           "[Vented Seat Medium / VS_MED]", "[Vented Seat High / VS_HI]"],
          ["Off", "Low", "Medium", "High"],
          "Valid value set accepted, others ignored: vented driver side"),
    166: ("VentedSeatFR", "4858399", "right front vented seat",
          ["[Vented Seat Off / VS_OFF]", "[Vented Seat Low / VS_Lo]",
           "[Vented Seat Medium / VS_MED]", "[Vented Seat High / VS_HI]"],
          ["Off", "Low", "Medium", "High"],
          "Valid value set accepted, others ignored: vented passenger side"),
    225: ("HSW_Stat", "4858516", "heated steering wheel",
          ["[Heated steering wheel off / OFF]",
           "[Heated steering wheel on / ON]"],
          ["Off", "On"],
          "Dual state valid value set accepted, others ignored"),
}


def build_b7() -> dict:
    out = {}
    for row, (sig, oid, ctrl, labels, states, tag) in B7.items():
        pairs = []
        for lbl, st in zip(labels, states):
            pairs.append(api_set(sig, lbl))
            pairs.append((f"Read the {ctrl} control and check that its state "
                          f"is {st}",
                          f"The {ctrl} control state is {st}"))
        pairs.append((f"Set ${sig}$ to a value outside the valid set above",
                      f"${sig}$ is set to a value outside the valid set"))
        pairs.append((f"Read the {ctrl} control and check that its state is "
                      "unchanged from the last valid value",
                      f"The {ctrl} control state is unchanged from {states[-1]}"))
        src = cfts(oid)
        upper = [ln.strip() for ln in src.split("\n")
                 if ln.strip().startswith("Valid values")]
        proc, er = steps(pairs)
        out[row] = {
            "I": item(upper[0] if upper else src.split("\n")[0], tag),
            "J": numbered([f"The vehicle is equipped with the {ctrl}",
                           'The "Comfort" screen is displayed',
                           "The signal is writable through the VHAL interface"]),
            "K": "NA", "L": proc, "M": er, "P": "P1", "R": EP,
            "AH": "本 leaf 之 "
                  f"${sig}$ 為 API／CarProperty 層訊號（037 D 欄逐字 "
                  "`via the VHAL interface`），非匯流排 raw，"
                  "「raw 全數已定義」不構成不生成之依據；值標籤逐字取 037 D 欄"
                  "與同列 CFTS 原句；無效值不造具體值（§8.4.1）",
        }
    return out


# =====================================================================
#  §三 既有 12 列 PENDING 之收尾
# =====================================================================

PRESS_RQ = {
    71:  ("FL_HS_RQ", "[HS_PSD]", "[HS_NOT_PSD]", "left front heated seat",
          "HeatedSeat"),
    86:  ("FR_HS_RQ", "[HS_PSD]", "[HS_NOT_PSD]", "right front heated seat",
          "HeatedSeat"),
    157: ("FL_VS_RQ_TGW", "[Vented Seat Pressed / VS_PSD]",
          "[Not Pressed / VS_NOT_PSD]", "left front vented seat", "VentedSeat"),
    172: ("FR_VS_RQ_TGW", "[Not Pressed / VS_NOT_PSD]",
          "[Vented Seat Pressed / VS_PSD]", "right front vented seat",
          "VentedSeat"),
}

CYCLE = {
    73:  ("FL_HS_RQ", "HeatedSeatFL", "left front heated seat",
          [("[HS_HI]", "[HS_MED]"), ("[HS_MED]", "[HS_LO]"),
           ("[HS_LO]", "[HS_OFF]"), ("[HS_OFF]", "[HS_HI]")], "HeatedSeat"),
    88:  ("FR_HS_RQ", "HeatedSeatFR", "right front heated seat",
          [("[HS_HI]", "[HS_MED]"), ("[HS_MED]", "[HS_LO]"),
           ("[HS_LO]", "[HS_OFF]"), ("[HS_OFF]", "[HS_HI]")], "HeatedSeat"),
    159: ("FL_VS_RQ_TGW", "VentedSeatFL", "left front vented seat",
          [("[High]", "[Medium]"), ("[Medium]", "[Low]"),
           ("[Low]", "[Off]"), ("[Off]", "[High]")], "VentedSeat"),
    174: ("FR_VS_RQ_TGW", "VentedSeatFR", "right front vented seat",
          [("[High]", "[Medium]"), ("[Medium]", "[Low]"),
           ("[Low]", "[Off]"), ("[Off]", "[High]")], "VentedSeat"),
}


def build_pending() -> dict:
    out = {}
    for row, (rq, sent, rest, ctrl, fam) in PRESS_RQ.items():
        proc, er = steps([
            api_read(rq, rest),
            (f"Press the {ctrl} control",
             f"The {ctrl} control registers the press"),
            api_read(rq, sent),
        ])
        out[row] = {"L": proc, "M": er,
                    "AH": f"訊號名與值標籤取自 037 {fam} D 欄（${rq}$／{sent}）；"
                          f"step 1 之 {rest} 取自同 leaf 之 test_item 上半 "
                          f"verbatim（§一(d)）；{TSEND}"}
    for row, (rq, stat, ctrl, table, fam) in CYCLE.items():
        pairs = []
        for cur, nxt in table:
            pairs.append(api_set(stat, cur))
            pairs.append((f"Press the {ctrl} control, read ${rq}$ and check "
                          f"that it is {nxt}",
                          f"${rq}$ reads {nxt}"))
        proc, er = steps(pairs)
        out[row] = {"L": proc, "M": er, "R": DT,
                    "AH": f"真值表逐條展開，四值循環之對映逐字取 037 {fam} D 欄"
                          f"（${stat}$ 之現值 → ${rq}$ 之送出值）；末行以實讀為準。"
                          "送出值以 D 欄之標籤書寫，不需匯流排編碼"}

    # row 28 —— $PowerMode$ 保留原標籤，不代以 DBC raw
    proc, er = steps([
        api_set("PowerMode", "[Ign. run / IGN_RUN]"),
        ('Read the "3rd Headrest Fold" softkey button and record its state as '
         "Softkey_ign_run", "Softkey_ign_run is recorded"),
        api_set("PowerMode",
                "[Ign. off & acc. (4 position switch) / IGN_OFF_ACC]"),
        ('Read the "3rd Headrest Fold" softkey button and check that it is '
         "selectable",
         'The "3rd Headrest Fold" softkey button is selectable'),
    ])
    out[28] = {"L": proc, "M": er,
               "AH": "$PowerMode$ 為 API／CarProperty 層訊號（037 Common "
                     "Features D 欄逐字 `through the CarPropertyManager API`），"
                     "值標籤保留 D 欄原表示法，不代以 DBC raw。"
                     "step 1 之 [Ign. run / IGN_RUN] 取自同節 leaf -038 之 "
                     "test_item 上半 verbatim（§一(d)）"}

    # row 35 —— 條文自帶否定側，ER 收斂為可選性
    proc, er = steps([
        api_set("PowerMode",
                "[Ign. off & acc. (4 position switch) / IGN_OFF_ACC]"),
        ('Read the "Rear View Camera" button and check that it is not '
         "selectable",
         'The "Rear View Camera" button is not selectable'),
        api_set("PowerMode", "[IGN_RUN]"),
        ('Read the "Rear View Camera" button and check that it is selectable',
         'The "Rear View Camera" button is selectable'),
    ])
    out[35] = {"L": proc, "M": er,
               "AH": "條文 `selectable only when [IGN_RUN]` 自帶否定側，"
                     "ER 收斂為可選性。$PowerMode$ 依 §一(b) 用 API "
                     "記法，值標籤取 037 Common Features D 欄與同節 leaf -031 之"
                     " test_item 上半 verbatim"}
    return out


# =====================================================================
#  §2.5／§一(b) —— Cmd_Tlm 與 *_RQ 之 API 記法改寫
# =====================================================================

LBL_RE = r"(?:\[([^\]]+)\]|\"{1,2}([^\"]+)\"{1,2})"
STAT_API = {"HeatedSeatFL", "HeatedSeatFR", "VentedSeatFL", "VentedSeatFR"}
ICON = {"FL": "left front", "FR": "right front"}


def parse_cmd(req: str) -> dict:
    d = re.sub(r"\s+", " ", " ".join(ln.strip() for ln in d_of(req).split("\n")))
    m = re.search(r"set\s+\$?([A-Za-z0-9_.]*Cmd_Tlm)\$?\s*=\s*" + LBL_RE, d)
    assert m, f"{req}：037 D 欄找不到 Cmd_Tlm 之指派，停手"
    conds = [(a.strip("$"), b or c) for a, b, c in
             re.findall(r"\$?([A-Za-z0-9_.$]+?)\$?\s*(?:==|=|passes to)\s*"
                        + LBL_RE, d[:m.start()])]
    return {"cmd": m.group(1).split(".")[-1], "val": m.group(2) or m.group(3),
            "conds": conds, "quoted": m.group(3) is not None}


CMD_ROWS = [96, 98] + list(range(110, 116)) + list(range(119, 125)) + \
    list(range(130, 138)) + list(range(139, 147)) + list(range(182, 188)) + \
    list(range(191, 197)) + list(range(202, 210)) + list(range(211, 219))


def build_cmd_rows(cur: dict) -> dict:
    out = {}
    for row in CMD_ROWS:
        req = cur[row]["D"]
        p = parse_cmd(req)
        fam = SWRA_IDX[req]["file"]
        q = (lambda s: f'"{s}"') if p["quoted"] else (lambda s: f"[{s}]")
        side = p["cmd"][:2]
        kind = "heated seat" if "_HS_" in p["cmd"] else "vented seat"
        ctrl = f"{ICON[side]} {kind}"
        state_cond = [(a, b) for a, b in p["conds"] if a in STAT_API]
        fail_cond = [(a, b) for a, b in p["conds"] if a.endswith("FailSts")]
        req_cond = [(a, b) for a, b in p["conds"] if a.endswith(".Req")]
        pairs = []
        for sig, lbl in fail_cond:
            pairs.append(can_send(sig, 0, lbl))
        if req_cond:                       # 使用者請求觸發
            for sig, lbl in state_cond:
                pairs.append(api_set(sig, q(lbl)))
            if not pairs:                  # 僅 .Req 條件（row 96／98）
                pairs.append(api_read(p["cmd"], "[Not_Pressed]"))
            pairs.append((f"Press the {ctrl} icon, read ${p['cmd']}$ and "
                          f"check that it is {q(p['val'])}",
                          f"${p['cmd']}$ reads {q(p['val'])}"))
        elif state_cond:                   # 狀態變化觸發
            sig, lbl = state_cond[0]
            pairs.append((f"Set ${sig}$ to a value other than {q(lbl)}",
                          f"${sig}$ is set to a value other than {q(lbl)}"))
            pairs.append((f"Set ${sig}$ = {q(lbl)} without pressing any icon, "
                          f"read ${p['cmd']}$ and check that it is "
                          f"{q(p['val'])}",
                          f"${p['cmd']}$ reads {q(p['val'])}"))
        else:                              # 無條件可設，只驗命令
            pairs.append(api_read(p["cmd"], "[Not_Pressed]"))
            pairs.append((f"Press the {ctrl} icon, read ${p['cmd']}$ and "
                          f"check that it is {q(p['val'])}",
                          f"${p['cmd']}$ reads {q(p['val'])}"))
        proc, er = steps(pairs)
        note = (f"${p['cmd']}$ 為 API／CarProperty 層訊號"
                "（037 D 欄逐字 `via the VHAL interface`），"
                "「不在基線 DBC」不構成缺陷（下放包 §2.5）；"
                f"訊號名與值標籤逐字取 037 {fam} D 欄")
        if "_mid" in str(p["val"]) or any("_mid" in str(b) for _, b in p["conds"]):
            note += "。`_mid` 之值取 D 欄之原標籤"
        if not req_cond and state_cond:
            note += "。前置之非目標值不造具體值（§8.4.1）"
        if row in (96, 98):
            note += ("。step 1 之 [Not_Pressed] 取自同節 leaf -043／-045 之 D 欄"
                     "（§一(d)）；本 leaf 之 D 欄僅 .Req 一個條件，"
                     "以基線讀取補足 §六.4 之 ≥2 步")
        out[row] = {"L": proc, "M": er, "AH": note}
    return out


# 其餘引用 *_RQ／*_Cmd_Tlm 之列（§一(b) 之一致性收尾）
def build_rq_rest() -> dict:
    out = {}
    # row 18 —— DriverSide 對 $FL_HS_RQ$ 無影響
    proc, er = steps([
        ("Set PROXI Driver_Side = 0 (Left Side) and power cycle the HU",
         "The HU completes start-up with PROXI Driver_Side = 0 (Left Side)"),
        ("Press the left front heated seat switch, read $FL_HS_RQ$ and "
         "record as FL_HS_RQ_LHD", "FL_HS_RQ_LHD is recorded"),
        ("Set PROXI Driver_Side = 1 (Right Side) and power cycle the HU",
         "The HU completes start-up with PROXI Driver_Side = 1 (Right Side)"),
        ("Press the left front heated seat switch, read $FL_HS_RQ$ and "
         "record as FL_HS_RQ_RHD", "FL_HS_RQ_RHD is recorded"),
        ("Check that FL_HS_RQ_RHD equals FL_HS_RQ_LHD",
         "FL_HS_RQ_RHD = FL_HS_RQ_LHD"),
    ])
    out[18] = {"L": proc, "M": er,
               "AH": "訊號名取 037 Common Features D 欄之 $FL_HS_RQ$"
                     "（原步驟以 DBC 之 TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm 代入，"
                     "§一(a) 不代換）；PROXI 依 profile R-VS86 維持既有記法"}

    # row 72 —— $FL_HS_RQ$ 之釋放跟隨
    proc, er = steps([
        api_read("FL_HS_RQ", "[HS_NOT_PSD]"),
        ("Press and release the left front heated seat switch",
         "The left front heated seat switch registers the press and the release"),
        ("Read $FL_HS_RQ$ and check that it has returned to [HS_NOT_PSD]",
         "$FL_HS_RQ$ reads [HS_NOT_PSD] after the press"),
    ])
    out[72] = {"L": proc, "M": er,
               "AH": f"訊號名與值標籤取 037 HeatedSeat D 欄（$FL_HS_RQ$／"
                     f"[HS_NOT_PSD]）；{TSEND}"}

    # row 97／99 —— Cmd_Tlm 之 Not_Pressed 跟隨
    for row, sig, ctrl in ((97, "FL_HS_Cmd_Tlm", "left front heated seat"),
                           (99, "FR_HS_Cmd_Tlm", "right front heated seat")):
        proc, er = steps([
            api_read(sig, "[Not_Pressed]"),
            (f"Press and release the {ctrl} control",
             f"The {ctrl} control registers the press and the release"),
            (f"Read ${sig}$ and check that it has returned to [Not_Pressed]",
             f"${sig}$ reads [Not_Pressed] after the release"),
        ])
        out[row] = {"L": proc, "M": er,
                    "AH": "$" + sig + "$ 為 API 層訊號；值標籤取 037 "
                          "HeatedSeat D 欄之 [Not_Pressed]。037 D 欄本 leaf 之側"
                          "別（FR）與 N 欄 CFTS 原句（"
                          + ("FL" if row == 97 else "FR") + "）不一致，"
                          "本列從 CFTS 原句之側別，具名待覆；" + TSEND}

    # row 158 —— $FL_VS_RQ_TGW$ 之釋放跟隨
    proc, er = steps([
        api_read("FL_VS_RQ_TGW", "[Not Pressed / VS_NOT_PSD]"),
        ("Press and release the left front vented seat control",
         "The left front vented seat control registers the press and the release"),
        ("Read $FL_VS_RQ_TGW$ and check that it has returned to "
         "[Not Pressed / VS_NOT_PSD]",
         "$FL_VS_RQ_TGW$ reads [Not Pressed / VS_NOT_PSD] after the release"),
    ])
    out[158] = {"L": proc, "M": er,
                "AH": "訊號名與值標籤取 037 VentedSeat D 欄（$FL_VS_RQ_TGW$／"
                      f"[Not Pressed / VS_NOT_PSD]）；{TSEND}"}

    # row 232 —— $HSW_RQ_TGW$ = [Pressed / PSD]
    proc, er = steps([
        can_send("STATUS_CLIMATE8.Tri_Level_HSW_StatSts", 0,
                 "Heated_steering_wheel_off"),
        ('Press the heated steering wheel icon on the "Comfort" screen',
         "The heated steering wheel icon registers the press"),
        api_read("HSW_RQ_TGW", "[Pressed / PSD]"),
    ])
    out[232] = {"L": proc, "M": er,
                "AH": "訊號名與值標籤取 037 Heated_Steering_Wheel D 欄"
                      "（$HSW_RQ_TGW$／[Pressed / PSD]）。"
                      "Tri_Level_HSW_StatSts 於基線 DBC 有同名訊號，維持 CAN 記法；"
                      + TSEND}

    # row 32／33 —— 同族之釋放／週期跟隨
    for row, tag in ((32, "release"), (33, "periodic")):
        if tag == "release":
            pairs = [
                api_read("HdRstRelRq", "[Pressed]"),
                ('Press and release the "3rd Headrest Fold" softkey button',
                 'The "3rd Headrest Fold" softkey button registers the press '
                 "and the release"),
                ("Read $HdRstRelRq$ and check that it has returned to "
                 "[Not Pressed]",
                 "$HdRstRelRq$ reads [Not Pressed] after the release"),
            ]
        else:
            pairs = [
                ('Press and release the "3rd Headrest Fold" softkey button',
                 'The "3rd Headrest Fold" softkey button registers the press '
                 "and the release"),
                ("Read $HdRstRelRq$ and check that it is [Not pressed]",
                 "$HdRstRelRq$ reads [Not pressed]"),
                ("Read $HdRstRelRq$ again without pressing the button and "
                 "check that it is still [Not pressed]",
                 "$HdRstRelRq$ still reads [Not pressed]"),
            ]
        proc, er = steps(pairs)
        out[row] = {"L": proc, "M": er,
                    "AH": "訊號名與值標籤取 037 Common Features D 欄之 "
                          "$HdRstRelRq$，非 DBC 之 RADIO_B3.HDRstRelRq_3rdRow"
                          "（§一(a) 不代換）；原步驟之「common features "
                          "control」為泛指，改為本 leaf 之實際操作對象；" + TSEND}

    # row 30／31 —— $HdRstRelRq$，DR-22 撤
    for row, dest in ((30, "CBC"), (31, "FSM")):
        proc, er = steps([
            api_read("HdRstRelRq", "[Not Pressed]"),
            ('Select the "3rd Headrest Fold" softkey button',
             'The "3rd Headrest Fold" softkey button registers the selection'),
            (f"Read $HdRstRelRq$ and check that it is [Pressed] at the {dest}",
             f"$HdRstRelRq$ reads [Pressed] at the {dest}"),
        ])
        out[row] = {"L": proc, "M": er,
                    "AH": "訊號名與值標籤取 037 Common Features D 欄"
                          "（$HdRstRelRq$ = [Pressed]），非 DBC 之 "
                          "RADIO_B3.HDRstRelRq_3rdRow（§一(a) 不代換）；"
                          "值域即 D 欄之標籤；" + TSEND}
    return out


# =====================================================================
#  全簿收尾
# =====================================================================

NAV = [
    ("Open the Controls screen from the Menu Bar", 'Press "Controls" on Menu Bar'),
    ("Open the Rear View Camera screen from the Menu Bar",
     'Press "Rear View Camera" on Menu Bar'),
    ("Open the Heated / Vented Seats screen from the Menu Bar", COMFORT),
    ("Heated / Vented Seats screen", '"Comfort" screen'),
    ("Climate screen", '"Comfort" screen'),
    ("Controls screen", '"Controls" screen'),
    ("Rear View Camera screen", '"Rear View Camera" screen'),
    ('"Headrest Dump"', '"3rd Headrest Fold"'),
    ("Headrest Dump Softkey button", '"3rd Headrest Fold" softkey button'),
    ("Hybrid Electric Pages access button", '"Hybrid Electric" button'),
    ('"Third Row Headrest Dump" button', '"3rd Headrest Fold" button'),
    ("Third Row Headrest Dump Softkey button",
     '"3rd Headrest Fold" softkey button'),
]
OPEN_RE = re.compile(r'Open the ("(?:[^"]+)") screen')

BLOCK_RE = re.compile(r"BLOCKED:\s*(DR-[0-9]+[′’']?(?:-[A-Z])?)\s*——\s*")


def sweep_text(s: str) -> str:
    for a, b in NAV:
        if b.strip('"').split('"')[0] and f'"{a}"' not in s:
            pass
        s = s.replace(a, b)
    s = OPEN_RE.sub(lambda m: f"Press {m.group(1)} on Menu Bar", s)
    s = s.replace('""Comfort" screen"', '"Comfort" screen')
    s = s.replace('""Controls" screen"', '"Controls" screen')
    s = s.replace("；", "; ").replace("，", ", ")
    s = re.sub(r"[ \t]+\n", "\n", s)
    s = "\n".join(ln.rstrip() for ln in s.split("\n"))
    s = re.sub(r"\.\s*$", "", s, flags=re.M)
    s = re.sub(r";\s+$", "", s, flags=re.M)
    return s.strip()


def main() -> int:
    assert BASE.exists(), f"基準不存在：{BASE}"
    got = sha256(BASE)
    assert got == BASE_SHA, f"Revise1 sha256 {got} ≠ 下放包所載，停手"
    shutil.copy2(BASE, OUT)

    wb = openpyxl.load_workbook(OUT)
    ws = wb[SHEET]
    cur = {r: {k: ws.cell(r, c).value for k, c in C.items()}
           for r in range(FIRST, LAST + 1)}
    for r in cur:
        cur[r]["D"] = str(cur[r]["D"]).strip()

    plan: dict[int, dict] = {}
    for part in (build_cfg(), build_fault_icon(), build_request(),
                 build_hsw_cmd(), build_misc(), build_b7(), build_pending(),
                 build_cmd_rows(cur), build_rq_rest()):
        for row, fields in part.items():
            assert row not in plan, f"row {row} 被兩個區段指派，停手"
            plan[row] = fields

    # ---- 施作：逐列逐欄
    for row, fields in sorted(plan.items()):
        tag = fields.pop("tag", None)
        for col, val in fields.items():
            ws.cell(row, C[col]).value = val
        if tag is not None:                       # 只換括號下半
            it = str(ws.cell(row, C["I"]).value or "")
            upper = it.split("\n\n")[0]
            ws.cell(row, C["I"]).value = item(upper, tag)

    # ---- §四 sibling 區分 token
    for row, tok in ((10, "Stop-start enabled, engine stopped: heated seat"),
                     (11, "Stop-start enabled, engine stopped: vented seat"),
                     (12, "Stop-start enabled, engine stopped: heated "
                          "steering wheel"),
                     (58, "Vehicle line M4"),
                     (59, "Vehicle line MP")):
        it = str(ws.cell(row, C["I"]).value or "")
        ws.cell(row, C["I"]).value = item(it.split("\n\n")[0], tok)

    # ---- §六.8 row 13：不讀回自注之訊號，驗證點改為 HMI 觀察
    proc, er = steps([
        can_send("STATUS_CCAN3.ESS_ENG_ST", 3, "ENS Running"),
        can_send("STATUS_CCAN3.EngineSts", 2, "Engine_On"),
        ("Read the heated seat switch indicators and record their state as "
         "Indicators_running", "Indicators_running is recorded"),
        can_send("STATUS_CCAN3.ESS_ENG_ST", 1, "ENS Stopped"),
        ("Send CAN: STATUS_CCAN3.EngineSts = 0 (Engine_Off) and check that "
         "the heated seat switch indicators differ from Indicators_running",
         "The heated seat switch indicators differ from Indicators_running"),
    ])
    ws.cell(13, C["L"]).value, ws.cell(13, C["M"]).value = proc, er
    ws.cell(13, C["AH"]).value = (
        "驗證點改為 HMI 觀察（開關指示燈狀態），不讀回自注之訊號"
        "（下放包 §六.8）；$EngRun_Stat$ 依 037 D 欄之對照以 "
        "STATUS_CCAN3.EngineSts 觀察")

    # ---- §三 尾段：DR-19／DR-21 之 dr_dependent 前綴撤除
    for r in range(FIRST, LAST + 1):
        a = str(ws.cell(r, C["AH"]).value or "")
        if a.startswith("dr_dependent = DR-19"):
            ws.cell(r, C["AH"]).value = (
                "$EngRun_Stat$ 依 037 D 欄之對照以 STATUS_CCAN3.EngineSts 觀察")
        elif a.startswith("dr_dependent = DR-21"):
            ws.cell(r, C["AH"]).value = (
                "$PowerMode$ 之 IGN_START 依 037 D 欄之對照以 "
                "STATUS_BH_BCM2.CmdIgnSts = 5 (START) 觀察")

    # ---- BLOCKED 前綴全簿撤除（§〇「BLOCKED → 0」）
    for r in range(FIRST, LAST + 1):
        a = str(ws.cell(r, C["AH"]).value or "")
        if not a:
            continue
        parts = [p.strip() for p in re.split(r"；|;", a) if p.strip()]
        keep = []
        for p in parts:
            m = BLOCK_RE.match(p)
            if not m:
                keep.append(p)
                continue
            dr, body = m.group(1), p[m.end():].strip()
            if dr in ("DR-15", "DR-21", "DR-24′", "DR-24’", "DR-25", "DR-26",
                      "DR-18", "DR-22"):
                if dr.startswith("DR-24"):
                    keep.append("時限之上限值於來源無明載，本列不驗時限")
                elif dr == "DR-18":
                    keep.append("`_mid` 之值取 037 D 欄之原標籤")
                else:
                    keep.append(body)
            else:                       # DR-5-B 等仍開之 DR：降為非阻擋之具名
                keep.append(f"dr_dependent = {dr}：{body}")
        seen, ded = set(), []
        for p in keep:
            if p not in seen:
                seen.add(p)
                ded.append(p)
        ws.cell(r, C["AH"]).value = "；".join(ded) or None

    # ---- 前置條件與步驟之一致性（§8.5）：無 CAN 步驟者不留匯流排前置
    bus_dropped = []
    for r in range(FIRST, LAST + 1):
        proc_txt = str(ws.cell(r, C["L"]).value or "")
        if not proc_txt.strip():
            continue
        has_can = "Send CAN:" in proc_txt
        has_trace = "trace" in proc_txt
        pre = [re.sub(r"^\s*\d+\.\s*", "", x).strip()
               for x in str(ws.cell(r, C["J"]).value or "").split("\n") if x.strip()]
        new = []
        for ln in pre:
            if not has_trace:
                ln = ln.replace(" with signal tracing enabled", "")
            if not has_can and re.search(r"connected to the bus simulator", ln):
                bus_dropped.append(r)
                continue
            new.append(ln)
        if new != pre:
            ws.cell(r, C["J"]).value = numbered(new)

    # ---- §五／§六.1–.3 全簿掃描（作者側四欄）
    for r in range(FIRST, LAST + 1):
        for col in AUTHOR_COLS:
            v = ws.cell(r, C[col]).value
            if v is None:
                continue
            ws.cell(r, C[col]).value = sweep_text(str(v))
    # row 49 之空標籤（§五）
    for col in ("L", "M"):
        v = str(ws.cell(49, C[col]).value or "")
        ws.cell(49, C[col]).value = v.replace('the "" soft button',
                                              'the "Screen Off" soft button')
    # §六.2 `Set PROXI` → `PROXI`
    for r in range(FIRST, LAST + 1):
        for col in ("L", "M"):
            v = ws.cell(r, C[col]).value
            if v and "Set PROXI" in str(v):
                ws.cell(r, C[col]).value = re.sub(
                    r"\bSet PROXI\b", "PROXI", str(v))

    # ---- §四 刪 row 23／48：內容上移，尾 2 列清空
    cols = list(C.values()) + [C_ for C_ in range(1, 35)]
    cols = sorted(set(range(1, 35)))
    keep_rows = [r for r in range(FIRST, LAST + 1) if r not in DEL_ROWS]
    snapshot = {r: [ws.cell(r, c).value for c in cols] for r in keep_rows}
    for i, r in enumerate(keep_rows):
        tgt = FIRST + i
        for c, v in zip(cols, snapshot[r]):
            ws.cell(tgt, c).value = v
    for r in range(FIRST + len(keep_rows), LAST + 1):
        for c in cols:
            ws.cell(r, c).value = None

    # ---- tc_id／No.# 重賦（§10.3）
    remap = []
    for i, r in enumerate(keep_rows):
        tgt = FIRST + i
        old = str(ws.cell(tgt, C["F"]).value or "")
        new = f"NR1L-VehicleSetting-{i + 1:03d}"
        remap.append({"old_row": r, "new_row": tgt, "old_tc_id": old,
                      "new_tc_id": new,
                      "requirement_id": str(ws.cell(tgt, C["D"]).value or "")})
        ws.cell(tgt, C["F"]).value = new
        ws.cell(tgt, C["B"]).value = i + 1
    for d in DEL_ROWS:
        remap.append({"old_row": d, "new_row": "", "old_tc_id":
                      str(cur[d]["F"] or ""), "new_tc_id": "DELETED",
                      "requirement_id": cur[d]["D"]})
    REMAP.parent.mkdir(parents=True, exist_ok=True)
    with open(REMAP, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, delimiter="\t", fieldnames=[
            "old_row", "new_row", "old_tc_id", "new_tc_id", "requirement_id"])
        w.writeheader()
        w.writerows(sorted(remap, key=lambda x: x["old_row"]))

    report = surgical_save(wb, BASE, OUT)
    print(f"Revise1 sha256 {BASE_SHA}")
    print(f"Revise2 {OUT.relative_to(ROOT)}  sha256 {sha256(OUT)}")
    print(f"surgical_save: {report}")
    print(f"觸及列（生成／改寫）：{len(plan)}；tc_id 對照 → "
          f"{REMAP.relative_to(ROOT)}")
    assert sha256(BASE) == BASE_SHA, "Revise1 落檔後 sha 改變，R-G72 破，停手"
    return 0


def req_of(row: int) -> str:
    return REQ_BY_ROW[row]


REQ_BY_ROW: dict[int, str] = {}


if __name__ == "__main__":
    _ws = openpyxl.load_workbook(BASE)[SHEET]
    REQ_BY_ROW = {r: str(_ws.cell(r, C["D"]).value).strip()
                  for r in range(FIRST, LAST + 1)}
    sys.exit(main())
