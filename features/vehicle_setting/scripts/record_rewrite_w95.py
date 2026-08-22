"""W-95：42 處 record 子句之處置（56 包 §2 / R-VS52(2)(4)）。

(a) 記錄而其值於該 TC 內無後續引用者 → 刪除 record 子句，改為直接檢查
(b) 用於後續比較者 → 保留並命名，比較步驟改引用變數名
(c) 讀取型斷言之 ER 形態沿用 `<X> reads <值>`

每一處為逐字替換，替換前 assert「全 TC 內恰命中一次」——
命中 0 次或多於 1 次即停下（R-VS54 之精神：替換式亦為形態相依）。
"""
from __future__ import annotations

import json
from pathlib import Path

FEAT = Path(__file__).resolve().parents[1]

LATEST = {
    "batch01": ("generated/batch01_v4.json", "generated/batch01_v5.json"),
    "batch02": ("generated/batch02_v2.json", "generated/batch02_v3.json"),
    "batch03": ("generated/batch03_v3.json", "generated/batch03_v4.json"),
    "batch04": ("generated/batch04_v4.json", "generated/batch04_v5.json"),
    "batch05": ("generated/batch05_v2.json", "generated/batch05_v3.json"),
    "batch06": ("generated/batch06_v2.json", "generated/batch06_v3.json"),
    "batch07": ("generated/batch07_v2.json", "generated/batch07_v3.json"),
    "batch08": ("generated/batch08_v3.json", "generated/batch08_v4.json"),
    "batch10": ("generated/batch10_v2.json", "generated/batch10_v3.json"),
    "batch11": ("generated/batch11_v2.json", "generated/batch11_v3.json"),
    "batch12": ("generated/batch12_v2.json", "generated/batch12_v3.json"),
}


def _sw(side: str, kind: str) -> list[tuple[str, str]]:
    """「點火非 RUN 時開關變灰」型：讀取步驟無後續引用 → 直接檢查（(a) 路）。"""
    return [
        (f"Read the state of the {side} {kind} switch and record it",
         f"Read the state of the {side} {kind} switch and check that it is selectable"),
        (f"The {side} {kind} switch is selectable and its state is recorded",
         f"The {side} {kind} switch reads selectable"),
    ]


def _disp_unused(obj: str, val: str) -> list[tuple[str, str]]:
    """「讀顯示狀態後不再引用」型 → 直接檢查（(a) 路）。"""
    return [
        (f"Read the displayed state of the {obj} and record it",
         f"Read the displayed state of the {obj} and check that it is {val}"),
        (f"The {obj} is displayed as {val} and the state is recorded",
         f"The {obj} reads {val}"),
    ]


def _disp_named(obj: str, var: str, val: str, mode: str) -> list[tuple[str, str]]:
    """「讀顯示狀態後於次一步比較」型 → 命名（(b) 路）。mode: changed / unchanged。"""
    out = [
        (f"Read the displayed state of the {obj} and record it",
         f"Read the displayed state of the {obj} and record as {var}"),
        (f"The {obj} is displayed as {val} and the state is recorded",
         f"{var} is recorded as {val}"),
        (f"check that the displayed state of the {obj} is unchanged from the state recorded in step 2",
         f"check that the displayed state of the {obj} is unchanged from {var}"),
        (f"check that the displayed state of the {obj} changes from the state recorded in step 2",
         f"check that the displayed state of the {obj} changes from {var}"),
        (f"unchanged from the state recorded in step 2",
         f"unchanged from {var}"),
    ]
    return out


def _icon(kind: str, var: str, raw: str, label: str, sig: str, step: str,
          newval: str) -> list[tuple[str, str]]:
    """「送值後記圖示狀態、次步比較」型 → 命名（(b) 路）。"""
    return [
        (f"Send CAN: {sig} = {raw} ({label}) and record the {kind} icon status",
         f"Send CAN: {sig} = {raw} ({label}) and record the {kind} icon status as {var}"),
        (f"The {kind} icon status is off and is recorded",
         f"{var} is recorded as off"),
        (f"check that the {kind} icon status changes from the status recorded in step {step}",
         f"check that the {kind} icon status changes from {var}"),
        (f"The {kind} icon status is {newval}",
         f"The {kind} icon status is {newval}, which differs from {var}"),
    ]


def _driver_label() -> list[tuple[str, str]]:
    return [
        ('Read the labels of the heated and vented seat buttons and record which button carries "Driver"',
         'Read the labels of the heated and vented seat buttons and record the button carrying "Driver" as Driver_label_initial'),
        ('The button carrying "Driver" is recorded',
         "Driver_label_initial is recorded"),
        ('the "Driver" and "Passenger" labels have swapped sides compared with step 1',
         'the "Driver" and "Passenger" labels have swapped sides compared with Driver_label_initial'),
        ('The "Driver" and "Passenger" labels are on the opposite heated and vented seat buttons from those recorded in step 1',
         'The "Driver" label is on the opposite heated and vented seat button from Driver_label_initial'),
    ]


EDITS: dict[tuple[str, str], list[tuple[str, str]]] = {
    # ---- (a) 路：22 處，刪除 record 子句 ----
    ("batch01", "SWE1-VC-ThirdRowHeadrestDump-025"): [
        ("Read the position of the left and right third row head restraints and record it",
         "Read the position of the left and right third row head restraints and check that both are raised"),
        ("Both third row head restraints are recorded as raised",
         "Both third row head restraints read raised"),
    ],
    ("batch02", "SWE1-VC-ThirdRowHeadrestDump-038"): [
        ('Read the state of the virtual "Rear View Camera" button and record it',
         'Read the state of the virtual "Rear View Camera" button and check that it is not selectable'),
        ('The state of the virtual "Rear View Camera" button is recorded',
         'The virtual "Rear View Camera" button reads not selectable'),
    ],
    ("batch03", "SWE1-VC-LeftFrontHeatedSeat-012"): _sw("left front", "heated seat"),
    ("batch03", "SWE1-VC-RightFrontHeatedSeat-029"): _sw("right front", "heated seat"),
    ("batch05", "SWE1-VC-LeftFrontVentedSeat-010"): _sw("left front", "vented seat"),
    ("batch06", "SWE1-VC-RightFrontVentedSeat-027"): _sw("right front", "vented seat"),
    ("batch05", "SWE1-VC-HeatedSteeringWheel-011"): [
        ("Read the state of the heated steering wheel switch and record it",
         "Read the state of the heated steering wheel switch and check that it is selectable"),
        ("The heated steering wheel switch is selectable and its state is recorded",
         "The heated steering wheel switch reads selectable"),
    ],
    ("batch10", "SWE1-VC-StopStartSystemBehavior-055"): [
        ("Read the state of the vented seat button and record it",
         "Read the state of the vented seat button and check that it is selectable"),
        ("The vented seat button is selectable and its state is recorded",
         "The vented seat button reads selectable"),
    ],
    ("batch04", "SWE1-VC-ThirdRowHeadrestDump-043"): [
        ('Read the state of the "Rear Camera" softkey button and record it',
         'Read the state of the "Rear Camera" softkey button and check that it is displayed'),
        ('The "Rear Camera" softkey button is displayed and its state is recorded',
         'The "Rear Camera" softkey button reads displayed'),
    ],
    ("batch05", "SWE1-VC-ThirdRowHeadrestDump-044"): [
        ('Read the state of the "Rear Camera" softkey button and record it',
         'Read the state of the "Rear Camera" softkey button and check that it is displayed'),
        ('The "Rear Camera" softkey button is displayed and its state is recorded',
         'The "Rear Camera" softkey button reads displayed'),
    ],
    ("batch05", "SWE1-VC-ThirdRowHeadrestDump-045"): [
        ("Read the screen and record that the image of the rear area of the vehicle is displayed",
         "Read the screen and check that the image of the rear area of the vehicle is displayed"),
        ("The image of the rear area of the vehicle is displayed and the state is recorded",
         "The image of the rear area of the vehicle is displayed"),
    ],
    ("batch06", "SWE1-VC-HeatedSteeringWheel-015"): _disp_unused("heated steering wheel", "off"),
    ("batch07", "SWE1-VC-HeatedSteeringWheel-016"): _disp_unused("heated steering wheel", "on"),
    ("batch07", "SWE1-VC-HeatedSteeringWheel-021"): _disp_unused("heated steering wheel", "off"),
    ("batch07", "SWE1-VC-HeatedSteeringWheel-022"): _disp_unused("heated steering wheel", "on"),
    ("batch10", "SWE1-VC-LeftFrontVentedSeat-014"): _disp_unused("left front vented seat", "high"),
    ("batch10", "SWE1-VC-LeftFrontVentedSeat-015"): _disp_unused("left front vented seat", "off"),
    ("batch10", "SWE1-VC-LeftFrontVentedSeat-017"): _disp_unused("left front vented seat", "off"),
    ("batch10", "SWE1-VC-RightFrontVentedSeat-031"): _disp_unused("right front vented seat", "high"),
    ("batch10", "SWE1-VC-RightFrontVentedSeat-032"): _disp_unused("right front vented seat", "off"),
    ("batch10", "SWE1-VC-RightFrontVentedSeat-034"): _disp_unused("right front vented seat", "off"),
    ("batch06", "SWE1-VC-ScreenOFF-051"): [
        ("Start a bus trace on CAN-B and record the frames carrying TGW_DISP_STAT",
         "Start a bus trace on CAN-B that captures the frames carrying TGW_DISP_STAT"),
        ("The bus trace is running and the frames carrying TGW_DISP_STAT are recorded",
         "The bus trace is running and is capturing the frames carrying TGW_DISP_STAT"),
    ],
    # ---- (b) 路：20 處，命名 ----
    ("batch01", "SWE1-VC-SwitchLHD/RHDConfiguration-011"): _driver_label(),
    ("batch08", "SWE1-VC-SwitchLHD/RHDConfiguration-014"): _driver_label(),
    ("batch03", "SWE1-VC-HeatedSteeringWheelManagement-027"): [
        ("Read the position of the heated steering wheel icon on the Heated / Vented Seats screen and record it",
         "Read the position of the heated steering wheel icon on the Heated / Vented Seats screen and record as HSW_icon_position_initial"),
        ("The position of the heated steering wheel icon is recorded",
         "HSW_icon_position_initial is recorded"),
        ("on the opposite side from the position recorded in step 1",
         "on the opposite side from HSW_icon_position_initial"),
        ("mirrored from the position recorded in step 1",
         "mirrored from HSW_icon_position_initial"),
    ],
    ("batch03", "SWE1-VC-LeftFrontHeatedSeat-007"): _disp_named(
        "left front heated seat", "HS_FL_display_initial", "off", "changed"),
    ("batch03", "SWE1-VC-LeftFrontHeatedSeat-008"): _disp_named(
        "left front heated seat", "HS_FL_display_initial", "low", "unchanged"),
    ("batch03", "SWE1-VC-RightFrontHeatedSeat-025"): _disp_named(
        "right front heated seat", "HS_FR_display_initial", "off", "changed"),
    ("batch03", "SWE1-VC-RightFrontHeatedSeat-026"): _disp_named(
        "right front heated seat", "HS_FR_display_initial", "low", "unchanged"),
    ("batch04", "SWE1-VC-LeftFrontVentedSeat-006"): _disp_named(
        "left front vented seat", "VS_FL_display_initial", "low", "unchanged"),
    ("batch04", "SWE1-VC-LeftFrontVentedSeat-007"): _disp_named(
        "left front vented seat", "VS_FL_display_initial", "off", "changed"),
    ("batch06", "SWE1-VC-RightFrontVentedSeat-023"): _disp_named(
        "right front vented seat", "VS_FR_display_initial", "low", "unchanged"),
    ("batch06", "SWE1-VC-RightFrontVentedSeat-024"): _disp_named(
        "right front vented seat", "VS_FR_display_initial", "off", "changed"),
    ("batch04", "SWE1-VC-HeatedSteeringWheel-006"): _disp_named(
        "heated steering wheel", "HSW_display_initial", "low", "unchanged"),
    ("batch05", "SWE1-VC-HeatedSteeringWheel-007"): _disp_named(
        "heated steering wheel", "HSW_display_initial", "off", "changed"),
    ("batch06", "SWE1-VC-ScreenOFF-052"): [
        ("Read the audio playback state and the current track and record them",
         "Read the audio playback state and the current track and record as Audio_track_initial"),
        ("Audio is playing and the playback state and track are recorded",
         "Audio_track_initial is recorded as playing"),
        ("audio playback continues with the same track as recorded in step 1",
         "audio playback continues with Audio_track_initial"),
        ("audio playback continues with the track recorded in step 1",
         "audio playback continues with Audio_track_initial"),
    ],
    ("batch06", "SWE1-VC-TwoStagesHeatedSeat-066"): _icon(
        "heated seat", "HS_icon_initial", "0", "Heated_seat_off",
        "STATUS_CSWM.FL_HS_STATSts", "1", "high"),
    ("batch08", "SWE1-VC-ThreeStagesHeatedSeat-089"): _icon(
        "heated seat", "HS_icon_initial", "0", "Heated_seat_off",
        "STATUS_CSWM.FL_HS_STATSts", "1", "medium"),
    ("batch07", "SWE1-VC-TwoStagesVentedSeatsManagement-048"): _icon(
        "vented seat", "VS_icon_initial", "0", "Vented_seat_off",
        "STATUS_CSWM.FL_VS_STATSts", "1", "high"),
    ("batch08", "SWE1-VC-ThreeStagesVentedSeatsManagement-071"): _icon(
        "vented seat", "VS_icon_initial", "0", "Vented_seat_off",
        "STATUS_CSWM.FL_VS_STATSts", "1", "medium"),
    ("batch08", "SWE1-VC-HeatedSteeringWheelManagement-032"): _icon(
        "heated steering wheel", "HSW_icon_initial", "0", "OFF",
        "STATUS_CSWM.HSW_StatSts", "2", "on"),
    ("batch11", "SWE1-VC-HeatedSteeringWheelManagement-025"): [
        ("and read whether the heated steering wheel control is present on the Heated / Vented Seats screen, and record it",
         "and read whether the heated steering wheel control is present on the Heated / Vented Seats screen, and record as HSW_control_initial"),
        ("The heated steering wheel control is not present and the state is recorded",
         "HSW_control_initial is recorded as not present"),
        ("is present, unlike the state recorded in step 1",
         "is present, unlike HSW_control_initial"),
    ],
}

FIELDS = ("test_procedure", "expected_result")


def apply_edits() -> tuple[int, list[str]]:
    """回傳（實際替換處數, 逐處之說明）。"""
    applied, log = 0, []
    for batch, (src, dst) in LATEST.items():
        d = json.loads((FEAT / src).read_text(encoding="utf-8"))
        for tc in d["tcs"]:
            edits = EDITS.get((batch, tc["leaf_id"]))
            if not edits:
                continue
            for old, new in edits:
                hits = sum(tc[f].count(old) for f in FIELDS)
                if hits == 0:
                    continue  # 同一 helper 之選擇性分支（changed / unchanged）
                if hits > 1:
                    raise SystemExit(f"命中 {hits} 次，停下：{batch} {tc['leaf_id']} — {old!r}")
                for f in FIELDS:
                    if old in tc[f]:
                        tc[f] = tc[f].replace(old, new)
                        applied += 1
                        log.append(f"{batch} {tc['leaf_id']} {f}: {old[:56]} → {new[:56]}")
        d["revision"] = "W-95（35 輪）：record 子句依 56 包 §2 處置"
        d["record_clause_policy"] = "R-VS52(2)(4) ＋ 56 包 §2：無後續引用者刪除改直接檢查；用於比較者命名"
        (FEAT / dst).write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n",
                                encoding="utf-8")
    return applied, log


if __name__ == "__main__":
    n, log = apply_edits()
    for line in log:
        print(line)
    print(f"\n實際替換 {n} 處")
