"""W-152（81 包 §3）—— 餘 53 leaf 之生成。

四段：
  (a) **D 型 10** —— 依 `-014` 改寫後之形態：驗證目標為 DR-15 標的者，
      該步驟之 ER 寫 `PENDING: DR-15`，前置步驟照寫
  (b) **F 型 1**
  (c) **A 型補 2** —— `TELEMATIC_CLIMATE_SETUP` 為母體首見：
      LID 之 20 列該 message 下**無任何 `_HS_` 訊號**，
      而 `FL_HS_Cmd_Tlm` 於 LID 僅一列（列 764，message 為 `TELEMATIC_VEHICLE_SETUP`）。
      依 **R-VS9(1)′「message 歸屬以 LID 為第一權威」**取 LID；其不符具名（A-VS159）。
      值 `"Pressed"` 依 **R-VS67′** 之能承載判準 → `Atlantis High` 之
      `SETUP3.FL_HS_Tlm`（`0 = Not_Pressed`／`1 = Pressed`）能承載，取之。
  (d) **G 型 40 —— 逐條讀原文，不設樣板**；其形態分七類，各自具名：
      G1 適用性前言（**不生成**，A-VS141 之第六式）          5
      G2 值域宣告 ＋「其餘為無效」                            9
      G3 推進系統未啟動 → 開關灰階                            5
      G4 Stop-Start 之引用（未配備／已配備）                   6
      G5 follow-up 訊號（`shall follow this signal with … Not Pressed`） 7
      G6 `PowerMode`／`DriverSide` 之條件                      5
      G7 配置訊號 → 按鍵之顯示／啟用                          3
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
BLK = {b["id"]: b for b in blocks_with_sec()}
L2R = {r["swe_id"]: r for r in csv.DictReader(
    (FEAT / "data/leaf_to_reqid.tsv").open(encoding="utf-8"), delimiter="\t")}
GEN = {r["leaf_id"]: r for r in csv.DictReader(
    (FEAT / "docs/reports/generatable.tsv").open(encoding="utf-8"), delimiter="\t")}

PROP = "HYBRID_POWERTRAIN1.PropulsionSystemActive"
IGN = "STATUS_BH_BCM2.CmdIgnSts"
ENG = "STATUS_CCAN3.EngineSts"
HS_LAB = {0: "Heated_seat_off", 1: "Heated_seat_low", 2: "Heated_seat_medium",
          3: "Heated_seat_high"}
VS_LAB = {0: "Vented_seat_off", 1: "Vented_seat_low", 2: "Vented_seat_medium",
          3: "Vented_seat_high"}
HSW_LAB = {0: "Heated_steering_wheel_off", 1: "Heated_steering_wheel_low",
           2: "Heated_steering_wheel_medium", 3: "Heated_steering_wheel_high"}


def src(leaf: str) -> str:
    qs = re.findall(r"\d{7}", L2R[leaf]["reqid_list"])
    return "\n".join(BLK[qs[0]]["text"].split("\n")[1:]).strip()


def tc(leaf, title, lower, pre, proc, er, method, form, why, **kw) -> dict:
    d = {"leaf_id": leaf, "test_set": GEN[leaf]["layer2"], "tc_title": title,
         "test_item": src(leaf) + "\n\n(" + lower + ")",
         "pre_conditions": "\n".join(f"{i}. {x}" for i, x in enumerate(pre, 1)),
         "input_test_data": "NA",
         "test_procedure": "\n".join(f"{i}. {x}" for i, x in enumerate(proc, 1)),
         "expected_result": "\n".join(f"{i}. {x}" for i, x in enumerate(er, 1)),
         "specification_reference": L2R[leaf]["reqid_list"].replace(";", "\n"),
         "design_method": method, "priority": kw.pop("prio", "P1"),
         "reasoning": f"{kw.pop('p_why', 'P1：主要功能邏輯')}；**{form}** —— {why}",
         "split_flag": False, "split_reason": "", "dr15_exposed": kw.pop("dr15", "no"),
         "dr_dependent": kw.pop("dep", ""), "screen_pending": kw.pop("sp", "no"),
         "form": form, "distinguishing_axis": kw.pop("axis", {"axis": "form",
                                                              "delta": why})}
    if kw.get("remarks"):
        d["remarks"] = kw["remarks"]
    return d


SCREEN = "The Heated / Vented Seats screen is displayed"
BUS = "CAN-B is connected to the bus simulator"


def build() -> tuple[list[dict], list[dict]]:
    out, held = [], []

    # ── (a) D 型 10 —— 驗證目標為 DR-15 標的，ER 寫 PENDING: DR-15 ──────
    D = [("SWE1-VC-LeftFrontHeatedSeat-013", "left front heated seat", "FL_HS_Tlm"),
         ("SWE1-VC-LeftFrontHeatedSeat-015", "left front heated seat", "FL_HS_Tlm"),
         ("SWE1-VC-LeftFrontVentedSeat-011", "left front vented seat", "FL_VS_Tlm"),
         ("SWE1-VC-LeftFrontVentedSeat-013", "left front vented seat", "FL_VS_Tlm"),
         ("SWE1-VC-RightFrontHeatedSeat-030", "right front heated seat", "FR_HS_Tlm"),
         ("SWE1-VC-RightFrontHeatedSeat-032", "right front heated seat", "FR_HS_Tlm"),
         ("SWE1-VC-RightFrontVentedSeat-028", "right front vented seat", "FR_VS_Tlm"),
         ("SWE1-VC-RightFrontVentedSeat-030", "right front vented seat", "FR_VS_Tlm"),
         ("SWE1-VC-HeatedSteeringWheel-012", "heated steering wheel", "HSW_Tlm"),
         ("SWE1-VC-HeatedSteeringWheel-013", "heated steering wheel", "HSW_Tlm")]
    for leaf, obj, sig in D:
        if leaf not in GEN or leaf in {"SWE1-VC-HeatedSteeringWheel-012"}:
            continue      # `-012` 已於 batch21_probe 交付
        out.append(tc(
            leaf, f"{obj.capitalize()} press sends the request signal",
            "Press sends the on-change request",
            [f"The vehicle is equipped with the {obj}", SCREEN,
             f"{BUS} with signal tracing enabled"],
            ["Start a bus trace on CAN-B that captures the frames carrying "
             f"TELEMATIC_VEHICLE_SETUP3.{sig}",
             f"Press the {obj} icon",
             f"Read the CAN-B trace and check that the value sent on "
             f"TELEMATIC_VEHICLE_SETUP3.{sig} is the one specified for the current state"],
            ["The bus trace is running and is capturing the frames carrying "
             f"TELEMATIC_VEHICLE_SETUP3.{sig}",
             f"The {obj} icon registers the press", "PENDING: DR-15"],
            "功能測試 (Functional based ; no specific technique)",
            "D 型（送出）",
            "觸發為使用者按壓、標的為匯流排上之送出值。**其送出值為 DR-15 之 token 級標的**"
            "，於來源無逐字對應 —— 依 R-VS71 該步驟之 ER 寫 `PENDING: DR-15`、前置步驟照寫。"
            "**不以「有送出」代替「送出正確之值」**（80 包 §1，A-VS157）",
            dep="DR-15", dr15="yes",
            remarks="BLOCKED: DR-15 —— 請求訊號之編碼待覆；"
                    "BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆"))

    # ── (a′) D 型補 2 —— 第三排頭枕之送出（W-152 首次分型時漏列，A-VS160）──
    # 其與上列 8 條之別：條文之送出值為**逐字之 `[Pressed]`**（非 DR-15 之真值表），
    # 故 ER 得斷言該值；惟 `RADIO_B3.HDRstRelRq_3rdRow` 於 LID `fmt` 為空、
    # 基線 DBC 亦無 → 依 **R-VS61** 取來源逐字、**不附 raw**。
    # 二條之別在**接收端**（CBC／FSM），依 §8.2.2 為相異之控制實體，各一條。
    for leaf, rcv in (("SWE1-VC-ThirdRowHeadrestDump-033", "CBC"),
                      ("SWE1-VC-ThirdRowHeadrestDump-034", "FSM")):
        sg = "RADIO_B3.HDRstRelRq_3rdRow"
        out.append(tc(
            leaf, f"Third row headrest dump request is sent to the {rcv}",
            f"Selection sends the request to the {rcv}",
            ["The vehicle is equipped with a dumpable third row headrest",
             SCREEN, f"{BUS} with signal tracing enabled"],
            [f"Start a bus trace on CAN-B that captures the frames carrying {sg}",
             "Select the third row headrest dump control",
             f"Read the CAN-B trace and check that {sg} = Pressed is transmitted "
             f"to the {rcv}"],
            [f"The bus trace is running and is capturing the frames carrying {sg}",
             "The third row headrest dump control registers the selection",
             f"{sg} = Pressed is transmitted to the {rcv}"],
            "功能測試 (Functional based ; no specific technique)",
            "D 型（送出）",
            f"觸發為使用者選取、標的為送往 `{rcv}` 之送出值。**接收端為本條之區辨軸** —— "
            f"`-033` 之標的為 CBC、`-034` 為 FSM，依 §8.2.2 為相異之控制實體。"
            f"其值 `[Pressed]` 為條文逐字，非 DR-15 之標的，故 ER 得斷言之；"
            f"惟該訊號之值域於 LID 與 DBC 皆無來源，依 R-VS61 不附 raw",
            axis={"axis": "target", "delta": f"本列之接收端為 {rcv}；"
                  f"其對稱列之接收端為 {'FSM' if rcv == 'CBC' else 'CBC'}。"},
            remarks="BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆；"
                    "BLOCKED: DR-22 —— 該訊號之值域於 LID 與 DBC 皆無來源"))

    # ── (b) F 型 1 ────────────────────────────────────────────────────
    out.append(tc(
        "SWE1-VC-FeaturesEnableCriteria-023",
        "Hybrid pages disabled for other signal values",
        "Configuration outside the enabled set",
        ["The HU is in the Full-Operation state"],
        ["Set PROXI VC_VEH_LINE = 0 (Invalid)",
         "Set PROXI Hybrid_Type = 0 (Not Applicable)",
         "Power cycle the HU and check that the Hybrid Electric Pages access button "
         "is not displayed"],
        ["PROXI VC_VEH_LINE = 0 (Invalid) is accepted",
         "PROXI Hybrid_Type = 0 (Not Applicable) is accepted",
         "The Hybrid Electric Pages access button is not displayed"],
        "負向測試 (Negative / Invalid)", "F 型（啟用／停用）",
        "其為 `-021`／`-022` 之負向對偶 —— 條文逐字「for all other signal values」，"
        "故取二參數皆於啟用集合之外者。**值取 LID 之 `0 = Invalid`／`0 = Not Applicable`**"))

    # ── (c) A 型補 2 ──────────────────────────────────────────────────
    for leaf, obj, sig in (("SWE1-VC-OneStageHeatedSeat-042", "left front heated seat",
                            "FL_HS_Tlm"),
                           ("SWE1-VC-OneStageHeatedSeat-044", "right front heated seat",
                            "FR_HS_Tlm")):
        out.append(tc(
            leaf, f"{obj.capitalize()} request sets the command to pressed",
            "One stage configuration, press request",
            ["The vehicle is configured for one heated seat state", SCREEN,
             f"{BUS} with signal tracing enabled"],
            [f"Start a bus trace on CAN-B that captures the frames carrying "
             f"TELEMATIC_VEHICLE_SETUP3.{sig}",
             f"Press the {obj} icon",
             f"Read the CAN-B trace and check that "
             f"TELEMATIC_VEHICLE_SETUP3.{sig} = 1 (Pressed) is transmitted"],
            [f"The bus trace is running and is capturing the frames carrying "
             f"TELEMATIC_VEHICLE_SETUP3.{sig}",
             f"The {obj} icon registers the press",
             f"TELEMATIC_VEHICLE_SETUP3.{sig} = 1 (Pressed) is sent"],
            "決策表 (Decision Table Testing)", "A 型（命令）",
            "條文之 message 為 `TELEMATIC_CLIMATE_SETUP`，而 **LID 之該 message 下"
            "無任何 `_HS_` 訊號**；`FL_HS_Cmd_Tlm` 於 LID 僅列 764（message 為 "
            "`TELEMATIC_VEHICLE_SETUP`）。依 **R-VS9(1)′（message 歸屬以 LID 為第一權威）**"
            "取 LID，其不符具名於 A-VS159。值 `\"Pressed\"` 依 **R-VS67′** 之能承載判準 → "
            "`Atlantis High` 之 `SETUP3.*_Tlm`（`0 = Not_Pressed`／`1 = Pressed`）能承載"))

    # ── (d) G 型 ──────────────────────────────────────────────────────
    rest = json.loads((FEAT / "data/_w152_rest.json").read_text(encoding="utf-8"))
    Gs = [x for x in rest if x[0] in ("G", "E")]

    for _, leaf, _q, _l2, txt in Gs:
        flat = re.sub(r"\s+", " ", txt)

        # G1 適用性前言 —— 不生成
        if re.search(r"Also the requirements? are valid only if", flat, re.I):
            held.append({"leaf_id": leaf, "form": "G1 適用性前言",
                         "reason": "條文逐字為 `Also the requirements are valid only if …` "
                                   "—— **無觸發亦無可觀察之結果**，為 A-VS141 之第六式。"
                                   "W-121 之結構判準確判其為前言，惟該判準因升級條件而未套用，"
                                   "故其分級仍為 W0。**本層不生成並具名**"})
            continue

        # G2 值域宣告 ＋「其餘為無效」→ 負向 TC
        if "shall be considered invalid" in flat or "valid values are below" in flat.lower():
            # 取**其所宣告值域之 token**（`Valid values for the $X$ are shown below`），
            # 非條文首見之 `$…$`（首見者多為 `$Heated_Seat_Levels$` 等配置參數）。
            m = re.search(r"Valid values for the \$(\w+)\$", flat) or \
                re.search(r"\$(\w+)\$\s*=\s*\[Heated|\$(\w+)\$\s*=\s*\[Vented", flat)
            tok = (m.group(1) if m else "")
            if not tok:
                m2 = re.findall(r"\$(\w+)\$", flat)
                tok = next((x for x in m2 if x.endswith(("SeatFL", "SeatFR", "Stat",
                                                        "Stat_2"))), "")
            sig, lab = {"HeatedSeatFL": ("STATUS_CSWM.FL_HS_STATSts", HS_LAB),
                        "HeatedSeatFR": ("STATUS_CSWM.FR_HS_STATSts", HS_LAB),
                        "VentedSeatFL": ("STATUS_CSWM.FL_VS_STATSts", VS_LAB),
                        "VentedSeatFR": ("STATUS_CSWM.FR_VS_STATSts", VS_LAB),
                        "HSW_Stat": ("STATUS_CSWM.HSW_STATSts", {0: "OFF", 1: "ON"}),
                        "HSW_Stat_2": ("STATUS_CLIMATE8.Tri_Level_HSW_StatSts", HSW_LAB),
                        }.get(tok, ("STATUS_CSWM.FL_HS_STATSts", HS_LAB))
            obj = GEN[leaf]["layer2"].lower()
            # **無效值須為該訊號可表示而未定義之碼**。`*_STATSts` 為 2 bit，
            # 其 0–3 四碼皆已定義 → **無未用碼可注入**，依 §8.4.1 不得造值，
            # 該步驟依 R-VS71 寫 `PENDING`；`Tri_Level_HSW_StatSts` 有 `7 = SNA` 可用。
            spare = {"STATUS_CLIMATE8.Tri_Level_HSW_StatSts": (7, "SNA")}.get(sig)
            if spare:
                inj = f"{sig} = {spare[0]} ({spare[1]})"
                er2, why2 = f"{inj} is sent", (
                    f"故取其值域中之未用碼 `{spare[0]} ({spare[1]})` 為注入值（§7 之 unsupported 配對）")
                dep2, rem2 = "", ""
            else:
                inj = f"{sig} = a value outside the declared valid set"
                er2, why2 = "PENDING: DR-18", (
                    "而該訊號為 2 bit、其 0–3 四碼**皆已定義** —— "
                    "**無未用碼可注入**；依 §8.4.1 不得造值，"
                    "故該步驟之 ER 依 R-VS71 寫 `PENDING: DR-18`（無效碼之定義待覆）")
                dep2 = "DR-18"
                rem2 = "BLOCKED: DR-18 —— 該訊號 0–3 皆已定義，無效碼之定義待覆"
            out.append(tc(
                leaf, f"Invalid {obj} status value is ignored",
                "Value outside the declared valid set",
                [f"The vehicle is equipped with the {obj}", SCREEN, BUS],
                [f"Send CAN: {sig} = 0 ({lab[0]}) and record the displayed state "
                 f"as Display_valid",
                 f"Send CAN: {inj}",
                 f"Read the displayed state of the {obj} and check that it is unchanged "
                 f"from Display_valid"],
                [f"{sig} = 0 ({lab[0]}) is sent；Display_valid is recorded", er2,
                 f"The {obj} display is unchanged from Display_valid"],
                "負向測試 (Negative / Invalid)", "G2 值域宣告 ＋ 其餘為無效",
                f"條文列 `{tok}` 之合法值集並逐字宣告「All other states shall be considered "
                f"invalid by the HU」——**其可測內容即「非合法值不改變顯示」**，{why2}",
                dep=dep2, remarks=rem2))
            continue

        # G3 推進系統未啟動 → 開關灰階
        if "PrplsnSysAtv" in flat and "greyed-out" in flat:
            obj = ("left front heated seat" if "left front heated" in flat else
                   "right front heated seat" if "right front heated" in flat else
                   "left front vented seat" if "left front vented" in flat else
                   "right front vented seat" if "right front vented" in flat else
                   "heated steering wheel")
            out.append(tc(
                leaf, f"{obj.capitalize()} greyed out when propulsion is not active",
                "Propulsion inactive on an electrified vehicle",
                ["The vehicle is an electrified vehicle", SCREEN, BUS],
                ["Set PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle)",
                 f"Send CAN: {PROP} = 1 (Active)",
                 f"Send CAN: {PROP} = 0 (Not_Active) and check that the {obj} switch "
                 f"is greyed out"],
                ["PROXI Hybrid_Type = 3 (Plugin Hybrid Electric Vehicle) is accepted",
                 f"{PROP} = 1 (Active) is sent",
                 f"The {obj} switch is greyed out"],
                "決策表 (Decision Table Testing)", "G3 推進系統未啟動 → 灰階",
                f"條文之條件為 `$PrplsnSysAtv$ = [Not Active] && $Hybrid_Type$ = "
                f"[[PHEV] OR [BEV] …]` 之**合取** —— 二者皆須成立，"
                f"故 procedure 先設 Hybrid_Type 再切 PrplsnSysAtv。"
                f"`$PrplsnSysAtv$` 取 LID 之 `{PROP}`"))
            continue

        # G4 Stop-Start 之引用
        if "Stop-Start" in flat or "Stop Start" in flat:
            equipped = "not equipped" not in flat
            obj = ("left front heated seat" if "left front heated" in flat else
                   "right front heated seat" if "right front heated" in flat else
                   "left front vented seat" if "left front vented" in flat else
                   "right front vented seat" if "right front vented" in flat else
                   "heated steering wheel")
            if equipped and "please see" in flat.lower():
                held.append({"leaf_id": leaf, "form": "G4 Stop-Start 之轉指",
                             "reason": "條文逐字為「please see Stop-Start System Feature "
                                       "section for switch behavior」——**其為轉指，"
                                       "本身無可測內容**；所指之節已由 "
                                       "`Stop-StartSystem-002`～`-007` 覆蓋（§8.2.1 不得"
                                       "擴張至兄弟 Req）。**本層不生成並具名**"})
                continue
            out.append(tc(
                leaf, f"{obj.capitalize()} greyed out when the engine is not running",
                "Engine not running on a vehicle without stop-start",
                ["The vehicle is not equipped with the Stop-Start feature", SCREEN, BUS],
                ["Set PROXI Stop_And_Start_cfg = 0 (Absent)",
                 f"Send CAN: {ENG} = 2 (Engine_On)",
                 f"Send CAN: {ENG} = 0 (Engine_Off) and check that the {obj} switch "
                 f"is greyed out"],
                ["PROXI Stop_And_Start_cfg = 0 (Absent) is accepted",
                 f"{ENG} = 2 (Engine_On) is sent", "PENDING: DR-19"],
                "決策表 (Decision Table Testing)", "G4 Stop-Start 未配備 → 灰階",
                "條文之條件為 `$EngRun_Stat$ <> [IDLE_STBL//UNLIMITED//LIMITED//RUN]`；"
                "該四值於 LID 與 DBC 皆無對應（**DR-19 之標的**），"
                "依 R-VS71 該步驟之 ER 寫 `PENDING: DR-19`、前置步驟照寫",
                dep="DR-19", remarks="BLOCKED: DR-19 —— `$EngRun_Stat$` 之四值待覆"))
            continue

        # G5 follow-up 訊號
        if "follow this signal" in flat or "continue to send the periodic" in flat:
            m = re.search(r"\$?(\w*(?:RQ_TGW|RelRq|Cmd_Tlm))\$?", flat)
            tokn = m.group(1) if m else "HdRstRelRq"
            sig = {"HSW_RQ_TGW": "TELEMATIC_VEHICLE_SETUP3.HSW_Tlm",
                   "FL_VS_RQ_TGW": "TELEMATIC_VEHICLE_SETUP3.FL_VS_Tlm",
                   "FR_VS_RQ_TGW": "TELEMATIC_VEHICLE_SETUP3.FR_VS_Tlm",
                   "HdRstRelRq": "RADIO_B3.HDRstRelRq_3rdRow",
                   "FL_HS_Cmd_Tlm": "TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm",
                   "FR_HS_Cmd_Tlm": "TELEMATIC_VEHICLE_SETUP3.FR_HS_Tlm"}.get(
                       tokn, "TELEMATIC_VEHICLE_SETUP3.HSW_Tlm")
            obj = GEN[leaf]["layer2"].lower()
            # `RADIO_B3.HDRstRelRq_3rdRow` 於 LID 有列而**其 `fmt` 為空**、
            # 基線 DBC 亦無 —— **名有來源而值域無來源**（R-VS57(4) 之 B6 形態）。
            # 依 **R-VS61** 取來源逐字、**不附 raw**；不得推一個 raw 碼出來（§8.4.1）。
            no_dom = sig.startswith("RADIO_B3.")
            term = (f"{sig} = Not Pressed" if no_dom else f"{sig} = 0 (Not_Pressed)")
            extra = ("；其值域於 LID 與 DBC 皆無來源，依 R-VS61 取條文逐字 `[Not Pressed]`"
                     "、不附 raw" if no_dom else "")
            out.append(tc(
                leaf, f"Request returns to not pressed after the press",
                "On-change follow-up after release",
                [f"The vehicle is equipped with the {obj}", SCREEN,
                 f"{BUS} with signal tracing enabled"],
                [f"Start a bus trace on CAN-B that captures the frames carrying {sig}",
                 f"Press and release the {obj} control",
                 f"Read the CAN-B trace and check that {term} is "
                 f"transmitted after the release"],
                [f"The bus trace is running and is capturing the frames carrying {sig}",
                 f"The {obj} control registers the press and the release",
                 f"{term} is sent"],
                "狀態轉換 (State Transition Testing)", "G5 follow-up 訊號",
                f"條文逐字「shall follow this signal with an on change … = "
                f"[Not Pressed …] within <Tsend>」——**其驗證目標為釋放後之回歸值**，"
                f"非按壓本身。`{tokn}` 依 R-VS67′ 取 `Atlantis High` 之 `{sig}`{extra}",
                remarks="BLOCKED: DR-24′ —— `<Tsend>` 之上限值待覆，ER 只寫可觀察終態"))
            continue

        # G6 PowerMode／DriverSide 之條件
        if "PowerMode" in flat or "DriverSide" in flat:
            if "DriverSide" in flat:
                out.append(tc(
                    leaf, "Right hand drive modifies the seat control layout",
                    "Right hand drive configuration",
                    ["The HU is in the Full-Operation state", SCREEN],
                    ["Set PROXI Driver_Side = 0 (Left Side) and record the seat control "
                     "layout as Layout_LHD",
                     "Set PROXI Driver_Side = 1 (Right Side)",
                     "Power cycle the HU and check that the seat control layout differs "
                     "from Layout_LHD"],
                    ["PROXI Driver_Side = 0 (Left Side) is accepted；Layout_LHD is recorded",
                     "PROXI Driver_Side = 1 (Right Side) is accepted",
                     "PENDING: DR-5-B"],
                    "等價劃分 (Equivalence Partitioning, EP)", "G6 DriverSide 之條件",
                    "條文逐字「the HMI shall be modified as defined by HMI requirements」"
                    "——**其所指之 HMI requirements 不在本 feature 之範圍**（§8.4.2），"
                    "故只驗「有無變更」，其具體版面依 R-VS59(4) 標 PENDING",
                    sp="yes", dep="",
                    remarks="BLOCKED: DR-5-B —— 右駕版面之具體定義待 HMI requirements"))
                continue
            grey = "grey-out" in flat or "greyed" in flat
            val, lab = ((5, "START") if "IGN_START" in flat else
                        (1, "IGN_LK") if "IGN_OFF_ACC" in flat else (4, "RUN"))
            unresolved = "IGN_START" in flat or "IGN_OFF_ACC" in flat
            act = "greyed out" if grey else "selectable"
            out.append(tc(
                leaf, f"Headrest dump softkey {act} at the stated power mode",
                "Power mode condition",
                ["The vehicle is equipped with third row head restraints",
                 "The Controls screen is displayed", BUS],
                [f"Send CAN: {IGN} = 4 (RUN)",
                 f"Send CAN: {IGN} = {val} ({lab})",
                 f"Read the \"Headrest Dump\" softkey button and check that it is {act}"],
                [f"{IGN} = 4 (RUN) is sent",
                 (f"PENDING: DR-21" if unresolved else f"{IGN} = {val} ({lab}) is sent"),
                 f"The \"Headrest Dump\" softkey button is {act}"],
                "狀態轉換 (State Transition Testing)", "G6 PowerMode 之條件",
                f"條文之 `$PowerMode$` 值為 "
                f"`{'IGN_START' if 'IGN_START' in flat else 'IGN_OFF_ACC'}` —— "
                f"其於 LID 之 `{IGN}` 值域中**無逐字對應**（**DR-21 之標的**），"
                f"依 R-VS71 該步驟之 ER 寫 `PENDING: DR-21`、其餘照寫"
                if unresolved else "其值於 LID 有對應",
                dep="DR-21" if unresolved else "",
                remarks=("BLOCKED: DR-21 —— `$PowerMode$` 之 `IGN_START`／`IGN_OFF_ACC` "
                         "待覆" if unresolved else "")))
            continue

        # G7 配置訊號 → 按鍵之顯示／啟用
        if "receives" in flat and ("Present" in flat):
            m = re.search(r"\$?(\w*(?:PRSNT|Prsnt))\$?", flat)
            tokn = m.group(1) if m else "VC_HdRstPrsnt"
            btn = ("Screen Off" if "Screen Off" in flat else "Third Row Headrest Dump")
            act = "activated for user selection" if "activate" in flat else "displayed"
            out.append(tc(
                leaf, f"{btn} button {act.split()[0]} when configured present",
                "Configuration present versus absent",
                ["The HU is in the Full-Operation state",
                 "The Controls screen is displayed"],
                [f"Set PROXI {tokn} = 0 (Absent) and record whether the \"{btn}\" button "
                 f"is present as Button_absent",
                 f"Set PROXI {tokn} = 1 (Present)",
                 f"Power cycle the HU and check that the \"{btn}\" button is {act}"],
                [f"PROXI {tokn} = 0 (Absent) is accepted；Button_absent is recorded",
                 "PENDING: DR-22",
                 f"The \"{btn}\" button is {act}"],
                "等價劃分 (Equivalence Partitioning, EP)", "G7 配置訊號 → 按鍵",
                f"條文之觸發為**配置訊號**（`{tokn} = [Present]`），非狀態訊號 —— "
                f"其於 LID **無列**（`VC_HdRstPrsnt` 為 **DR-22 之 token 級標的**），"
                f"依 R-VS71 該步驟之 ER 寫 `PENDING: DR-22`、其餘照寫",
                dep="DR-22",
                remarks=f"BLOCKED: DR-22 —— `{tokn}` 之值域待覆"))
            continue

        # 其餘（G8）：允許啟用
        out.append(tc(
            leaf, "Engine running allows the seat and wheel switches",
            "Engine running condition",
            ["The vehicle is equipped with the Stop-Start feature", SCREEN, BUS],
            [f"Send CAN: {ENG} = 0 (Engine_Off)",
             f"Send CAN: {ENG} = 2 (Engine_On)",
             "Read the heated seat switch and check that it can be activated"],
            [f"{ENG} = 0 (Engine_Off) is sent", "PENDING: DR-19",
             "The heated seat switch can be activated"],
            "決策表 (Decision Table Testing)", "G8 引擎運轉 → 允許啟用",
            "條文之條件 `$EngRun_Stat$ = [IDLE_STBL//UNLIMITED//LIMITED//RUN]` 之四值"
            "於 LID 與 DBC 皆無對應（**DR-19 之標的**），依 R-VS71 該步驟寫 `PENDING: DR-19`",
            dep="DR-19", remarks="BLOCKED: DR-19 —— `$EngRun_Stat$` 之四值待覆"))
    return out, held


if __name__ == "__main__":
    tcs, held = build()
    d = {"batch": "batch23", "feature": "vehicle_setting", "test_group": "Vehicle Setting",
         "generated_round": 53, "handoff": "docs/handoff/81_scale_up.md",
         "profile": "docs/runtime/profiles/FW036_R1L_VehicleSetting_Profile.md",
         "selection": "W-152：餘 53 leaf 之生成，分四段（D 型／F 型／A 型補／G 型逐條）。",
         "signal_notation": "R-VS52 ＋ R-VS61 ＋ R-VS67′",
         "design_method_domain": "SWC 0708 交付本之 `下拉選單` 分頁，9 值",
         "revision": "W-152（53 輪）：batch23 首版",
         "held_out": held, "tcs": tcs}
    (FEAT / "generated/batch23.json").write_text(
        json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    import collections
    print(f"batch23：{len(tcs)} 條；held_out {len(held)}")
    print("形態分布：", dict(collections.Counter(t["form"] for t in tcs)))
    print("held_out：", dict(collections.Counter(h["form"] for h in held)))
