#!/usr/bin/env python3
"""T15 —— pilot 生成：組 3 `Lockout Enforcement`（leaf 009–012）。

下放包 09 §六 之規格。**只生成，不寫回工作簿、不 git。**
`test_item` 上半自 037 `Analysis Report` **機器擷取**（不手打），
逾 50 token 者取其 `Case`＋`Then` 二行之連續摘句（R-S4）。

輸出：`features/driver_distraction/generated/pilot_group3.json`
"""
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
A03 = ROOT / "inputs" / "DD_SWE1_0807_EN.xlsx"
OUT = ROOT / "generated" / "pilot_group3.json"

ROW = {"009": 17, "010": 18, "011": 19, "012": 20}
TOKEN_CAP = 50

SPEED = "$STATUS_CCAN3.VehicleSpeedVSOSig$"
POPUP = 'Feature not available while the vehicle is in motion.'
# profile §2.1 之取樣：p7 `Driver Lockout Tables`，黃標三項
# （Player / RSE、Messaging、SRT Options）已排除；二者皆非 NAV，
# 不受「Embedded NAV 僅 LATAM」之拘束。
FEAT_117 = 'Pairing (1st time)'
FEAT_118 = 'Reconfigurable menu bar'


def upper_half(text):
    """037 Requirement Description → test_item 上半。

    ≤ TOKEN_CAP token 者全文照錄；逾限者取 `Case`／`Then` 二行之
    **連續**摘句 —— 該二行為條文之操作性內容，且為同源二列之相異處。
    """
    lines = text.split("\n")
    if len(text.split()) <= TOKEN_CAP:
        return text, "full", len(text.split())
    i = next(k for k, l in enumerate(lines) if l.startswith("Case"))
    j = next(k for k, l in enumerate(lines) if l.startswith("Then"))
    exc = "\n".join(lines[i:j + 1])
    return exc, "excerpt(Case..Then)", len(exc.split())


def main():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    rows = [list(r) for r in wb["Analysis Report"].iter_rows(values_only=True)]
    wb.close()
    src = {k: rows[v - 1] for k, v in ROW.items()}

    halves = {}
    for k, row in src.items():
        halves[k] = upper_half(row[3])
        assert halves[k][2] <= TOKEN_CAP, (k, halves[k][2])
        assert halves[k][0] in row[3], f"{k} 摘句非原文子串"

    lower = {
        "009": '(Access attempt on "Pairing (1st time)" with the speed signal held at the lock threshold)',
        "010": '(Fail-safe: the speed message is stopped and "Pairing (1st time)" is retried after the timeout)',
        "011": '(Lockout notification raised while "Reconfigurable menu bar" is being edited)',
        "012": '(Fail-safe: the speed message is stopped and "Reconfigurable menu bar" is retried after the timeout)',
    }

    tcs = [
        {
            "leaf": "009",
            "test_set": "Lockout Enforcement",
            "pre_conditions": (
                "1. The signal " + SPEED + " is transmitted on the bus at 0 (0.0000 km/h)"
            ),
            "input_test_data": "NA",
            "test_procedure": (
                "1. Send the signal " + SPEED + " = 129 (8.0625 km/h)\n"
                '2. Open the Phone screen and select "Pairing (1st time)"\n'
                "3. Read the Phone screen and check that the pairing flow has not started"
            ),
            "expected_result": (
                "1. The vehicle-speed signal is carried on the bus at raw 129, which is "
                "8.0625 km/h [ASSUMPTION A-DD6]\n"
                '2. The Phone screen is displayed and the "Pairing (1st time)" entry is selected\n'
                "3. The pairing flow does not start and the Phone screen stays as it was "
                "before the attempt"
            ),
            "priority": "P0",
            "design_method": "狀態轉換 (State Transition Testing)",
            "reasoning": (
                "驗證目標：速度達上鎖門檻時，Lockout Table 所列之受限 feature 其存取被阻 —— "
                "斷言錨取 profile §2.1 觀察面 A（存取阻擋），取樣 feature 具名為 "
                '"Pairing (1st time)"。關鍵情境條件：'
                + SPEED + " 由 0 送至 raw 129（8.0625 km/h＝5.0097 MPH），"
                "該值為 profile §3.1 依 R-DD7(c) 所定之上鎖側第一個可表示格，標 [ASSUMPTION A-DD6]。"
                "一條 TC 即足：037 之 AC1 只有一條常態路徑（施加受限狀態 → 存取被阻），"
                "無獨立可分之部分失效（IN §8.2.2 未成立）。"
                "刻意略過：解鎖方向（raw 77／78）屬 -013／-015，門檻下側 raw 128 之不應鎖屬 BVA 之另一半，"
                "本列不擴入（IN §8.2.1）；p7 黃標三項（Player / RSE、Messaging、SRT Options）不取樣，"
                "Embedded NAV 系（含 Destination Entry）因僅適用 LATAM 亦不取。"
                "設計方法依 IN §12 首合原則取狀態轉換 —— 觸發為車速由 0 跨越門檻之 A→B 轉換，"
                "於 Scenario 之前命中；且 §12 tie-break 之 Scenario 判準為「≥3 steps crossing features」，"
                "本列為單一 feature 之存取嘗試，不合。"
            ),
        },
        {
            "leaf": "010",
            "test_set": "Lockout Enforcement",
            "pre_conditions": (
                "1. The signal " + SPEED + " is transmitted on the bus at 0 (0.0000 km/h)"
            ),
            "input_test_data": "NA",
            "test_procedure": (
                '1. Start "Pairing (1st time)" from the Phone screen, then leave it\n'
                '2. Stop transmitting the message "STATUS_CCAN3" and let the signal timeout elapse\n'
                '3. Select "Pairing (1st time)" again and check that the pairing flow does not start'
            ),
            "expected_result": (
                '1. The "Pairing (1st time)" pairing screen is shown, and the Phone screen is '
                "displayed again after leaving it\n"
                '2. The message "STATUS_CCAN3" is no longer present on the bus and the signal '
                "timeout window has elapsed\n"
                '3. The "Pairing (1st time)" pairing flow does not start and the Phone screen '
                "stays as it was before the attempt"
            ),
            "priority": "P1",
            "design_method": "基礎故障注入 (Fault Injection Lite)",
            "reasoning": (
                "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取，"
                "斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：失效形態取「匯流排逾時」而非 SNA —— "
                "profile §3.2 明定逐 leaf 依 037 AC2 原文定，而本列 AC2 逐字為 "
                "`the signal simulation tool stops transmitting a vehicle message`，"
                "其驗證方法欄亦書 `After the signal timeout`，故為停送非送 SNA。"
                "步驟 1 先確認該 feature 在訊號正常時可啟動，"
                "否則步驟 3 之「不可啟動」分不出「fail-safe 生效」與「本來就不可用」（IN §5.6 基準）。"
                "刻意略過：SNA（raw 8191）之路徑本列不涵蓋 —— 037 本列未書該形態，寫入即造值。"
                "另：本列與 newR1L-DD-004 之驗證目標實質相同（見該列 reasoning 與 A-DD7／DR-DD7）。"
            ),
        },
        {
            "leaf": "011",
            "test_set": "Lockout Enforcement",
            "pre_conditions": (
                "1. The signal " + SPEED + " is transmitted on the bus at 0 (0.0000 km/h)"
            ),
            "input_test_data": "NA",
            "test_procedure": (
                '1. Open the menu-bar configuration view for "Reconfigurable menu bar"\n'
                "2. Send the signal " + SPEED + " = 129 (8.0625 km/h)\n"
                "3. Read the screen and check that the Standard Lockout Popup is displayed"
            ),
            "expected_result": (
                '1. The menu-bar configuration view for "Reconfigurable menu bar" is displayed '
                "and accepts editing input\n"
                "2. The vehicle-speed signal is carried on the bus at raw 129, which is "
                "8.0625 km/h [ASSUMPTION A-DD6]\n"
                '3. The Standard Lockout Popup is displayed, showing "' + POPUP + '"'
            ),
            "priority": "P0",
            "design_method": "狀態轉換 (State Transition Testing)",
            "reasoning": (
                "驗證目標：受限 feature 使用中而車速跨越門檻時，HMI 呈現 lockout 通知 —— "
                "斷言錨取 profile §2.2 觀察面 B，字串逐字取 HMI spec p4。"
                "關鍵情境條件：與 -009 之別在於**施加順序** —— 本列先進入 feature 再跨門檻，"
                "故設計方法取狀態轉換；raw 129 同 profile §3.1，標 [ASSUMPTION A-DD6]。"
                "一條 TC 即足：037 之 AC1 只有一條轉換路徑，無獨立可分之部分失效。"
                "刻意略過：通知關閉後之後續行為、以及 popup 之逾時形態，037 本列未書，不擴入；"
                '取樣 feature 取 "Reconfigurable menu bar"（Menu Bar 列，非黃標、非 NAV 系），'
                "與同源之 -012 一致，使 -118 家族之二列可對讀。"
            ),
        },
        {
            "leaf": "012",
            "test_set": "Lockout Enforcement",
            "pre_conditions": (
                "1. The signal " + SPEED + " is transmitted on the bus at 0 (0.0000 km/h)"
            ),
            "input_test_data": "NA",
            "test_procedure": (
                '1. Open the "Reconfigurable menu bar" configuration view, then leave it\n'
                '2. Stop transmitting the message "STATUS_CCAN3" and let the signal timeout elapse\n'
                "3. Open the menu-bar configuration view again and check that it does not open"
            ),
            "expected_result": (
                '1. The menu-bar configuration view for "Reconfigurable menu bar" is displayed '
                "and accepts editing input, and the previous screen is shown again after leaving it\n"
                '2. The message "STATUS_CCAN3" is no longer present on the bus and the signal '
                "timeout window has elapsed\n"
                "3. The menu-bar configuration view does not open and the screen stays as it was "
                "before the attempt"
            ),
            "priority": "P1",
            "design_method": "基礎故障注入 (Fault Injection Lite)",
            "reasoning": (
                "驗證目標：訊號逾時之 fail-safe 對 -118 家族之取樣 feature 同樣使其不可存取，"
                "斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：形態同 -010 取匯流排逾時，"
                "依 profile §3.2 逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書停送與 signal timeout。"
                "**本列之 037 Requirement Description 與 -010 逐字全等**（見 A-DD7），"
                "其 Then 句書 `HMI keeps the corresponding feature locked` 而非 -118 之通知面；"
                "本 TC 依原文斷言存取阻擋，**不代上游改寫為通知**（IN §8.4.2）。"
                "區別二列者為取樣 feature 與 spec_reference，非斷言內容。"
                "**本列與 newR1L-DD-002 之驗證目標實質相同** —— 依 IN §4.6 之等價判準"
                "（same trigger + outcome + input + verification target）四者皆同，"
                "其區別僅在取樣 feature 與追溯 ID，而取樣 feature 係作者所選、非 spec 所定。"
                "二列皆保留係追溯要求（每 leaf 須有 TC），"
                "**不得以取樣 feature 之不同偽稱為不同之驗證目標**；成因見 A-DD7／DR-DD7。"
            ),
        },
    ]

    spec = {"009": "CFTS022-4915108", "010": "CFTS022-4915108",
            "011": "CFTS022-4915109", "012": "CFTS022-4915109"}

    out = []
    for n, tc in enumerate(tcs, 1):
        k = tc["leaf"]
        half, mode, ntok = halves[k]
        out.append({
            "tc_id": f"newR1L-DD-{n:03d}",
            "req_id": f"SWE1-RA-Driver_Distraction-{k}",
            "test_group": "Driver Distraction",
            "test_set": tc["test_set"],
            "test_item": half + "\n" + lower[k],
            "pre_conditions": tc["pre_conditions"],
            "input_test_data": tc["input_test_data"],
            "test_procedure": tc["test_procedure"],
            "expected_result": tc["expected_result"],
            "spec_reference": spec[k],
            "tc_ref_id": "NEW",
            "priority": tc["priority"],
            "design_method": tc["design_method"],
            "functional_safety": "NA",
            "author": "PeiPYHsu",
            "split_flag": False,
            "split_reason": "NA",
            "upper_half_provenance": {
                "source": f"037 Analysis Report r{ROW[k]} c3 (Requirement Description)",
                "mode": mode,
                "tokens": ntok,
                "cap": TOKEN_CAP,
            },
            "reasoning": tc["reasoning"],
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"寫入 {OUT.relative_to(ROOT.parent.parent)}：{len(out)} TC")
    for o in out:
        p = o["upper_half_provenance"]
        print(f"  {o['tc_id']}  {o['req_id']}  {o['priority']:<3} "
              f"上半 {p['mode']} {p['tokens']}/{p['cap']} token  {o['spec_reference']}")


if __name__ == "__main__":
    main()
