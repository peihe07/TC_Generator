#!/usr/bin/env python3
"""T18c（下放包 12 §6.2）—— 批次 B1 生成。

範圍依 T18b：`-003`~`-008` ＋ `-013`~`-016`（**10 leaf**）。
`-001`／`-002` 因 Body OFF 電源域觸發、profile §3 五項無對應而**剔除**。

`test_item` 上半自 037 **機器擷取**（逾 50 token 取 `Case`＋`Then` 連續摘句）。
拘束依 §6.2 一至六，形制承 pilot（R-DD9／R-DD15／R-DD16／R-DD17）。

**只生成，不寫回、不 git。** 產物：`generated/batch_b1.json`
"""
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
A03 = ROOT / "inputs" / "DD_SWE1_0807_EN.xlsx"
OUT = ROOT / "generated" / "batch_b1.json"

SPEED = "$STATUS_CCAN3.VehicleSpeedVSOSig$"
MSG = '"STATUS_CCAN3"'
LOCK, UNLOCK = "129 (8.0625 km/h)", "77 (4.8125 km/h)"
TOKEN_CAP = 50

# profile §1 —— SYS-RA → ObjectID
OBJ = {"114": "CFTS022-4915105", "115": "CFTS022-4915106", "116": "CFTS022-4915107",
       "120": "CFTS022-4915112", "121": "CFTS022-4915115"}

# 取樣 feature —— HMI spec p7 `Driver Lockout Tables`，**黃標與 NAV 系皆已排除**。
# 一個 Requirement 家族一個取樣，使該家族之 AC1／AC2 可對讀。
# `-013`／`-015` 之取樣與 pilot 相異（§6.2-3）。
FEAT = {
    "114": ('"Reconfigurable menu bar"', "p7 top=356（Menu Bar 列）"),
    "115": ('"Edit phone book (speller input)"', "p7 top=291（Phone 列）"),
    "116": ('"DND Customize auto reply message"', "p7 top=317（DND 列）"),
    "120": ('"Player Song, artist, title, etc. (speller search)"', "p7 top=330（Player 列）"),
    "121": ('"Pairing (1st time)"', "p7 top=304（Phone 列）"),
}

# leaf → (source, priority, 家族)
META = {
    "003": ("114", "P1"), "004": ("114", "P1"),
    "005": ("115", "P1"), "006": ("115", "P1"),
    "007": ("116", "P0"), "008": ("116", "P1"),
    "013": ("120", "P0"), "014": ("120", "P1"),
    "015": ("121", "P0"), "016": ("121", "P1"),
}
ROW = {"003": 11, "004": 12, "005": 13, "006": 14, "007": 15, "008": 16,
       "013": 21, "014": 22, "015": 23, "016": 24}


def upper_half(text):
    lines = text.split("\n")
    if len(text.split()) <= TOKEN_CAP:
        return text, "full", len(text.split())
    i = next(k for k, l in enumerate(lines) if l.startswith("Case"))
    j = next(k for k, l in enumerate(lines) if l.startswith("Then"))
    exc = "\n".join(lines[i:j + 1])
    return exc, "excerpt(Case..Then)", len(exc.split())


def sig_pc():
    """R-DD17：PC 之訊號源行只書訊號源本身。"""
    return f"1. The signal {SPEED} is transmitted on the bus at 0 (0.0000 km/h)"


def timeout_tc(leaf, feat, why):
    """AC2 逾時 fail-safe 之共同形（-004／-006／-008／-014／-016）。"""
    return {
        "pre_conditions": sig_pc(),
        "input_test_data": "NA",
        "test_procedure": (
            f"1. Open {feat}, then leave it\n"
            f"2. Stop transmitting the message {MSG} and let the signal timeout elapse\n"
            f"3. Open {feat} again and check that it does not open"),
        "expected_result": (
            f"1. {feat} is displayed and accepts input, and the previous screen is "
            "shown again after leaving it\n"
            f"2. The message {MSG} is no longer present on the bus and the signal "
            "timeout window has elapsed\n"
            f"3. {feat} does not open and the screen stays as it was before the attempt"),
        "design_method": "基礎故障注入 (Fault Injection Lite)",
        "reasoning": why,
    }


TCS = {}

# ── -003（-114 AC1）：5/3 MPH 規則之雙向 ──────────────────────────────
f, src = FEAT["114"][0], FEAT["114"][1]
TCS["003"] = {
    "pre_conditions": sig_pc(),
    "input_test_data": "NA",
    "test_procedure": (
        f"1. Send the signal {SPEED} = {LOCK}\n"
        f"2. Select {f} and check that it does not open\n"
        f"3. Send the signal {SPEED} = {UNLOCK}\n"
        f"4. Select {f} again and check that it opens"),
    "expected_result": (
        f"1. The vehicle-speed signal is carried on the bus at raw 129, which is "
        "8.0625 km/h [ASSUMPTION A-DD6]\n"
        f"2. {f} does not open and the screen stays as it was before the attempt\n"
        f"3. The vehicle-speed signal is carried on the bus at raw 77, which is "
        "4.8125 km/h [ASSUMPTION A-DD6]\n"
        f"4. {f} opens and its view is displayed"),
    "design_method": "狀態轉換 (State Transition Testing)",
    "reasoning": (
        "驗證目標：037 本列之 `5/3 MPH rule`。其 source `-114` 所命者為"
        "「**監看 `$Speedometer$` 以啟閉受限 feature**」之能力，驗證對象為**規則整體**。"
        "**5/3 之雙門檻即遲滯（hysteresis）** —— 遲滯之定義為「上行門檻 ≠ 下行門檻」，"
        "**任一單邊皆無法承載該性質**；故本則之驗證點為一，非二，"
        "步驟 2 與步驟 4 合為該單一驗證點之組成，不拆（`split_flag: false`）。"
        f"關鍵情境條件：raw 129 與 raw 77 皆取 profile §3.1（R-DD7(c)），標 [ASSUMPTION A-DD6]；"
        f"取樣 feature 取 {f}（{src}），非黃標、非 NAV 系。"
        "**未取「above 3 MPH」之任意中間值** —— profile §3.1 只給 129 與 77 二個 spec 溯源之格，"
        "另擇一值即造值（IN §8.4.1）；raw 129（5.0097 MPH）本身即在 3 MPH 之上，足以起算。"
        "刻意略過：BVA 之另一側（raw 128／78）037 未書，不擴入（IN §8.2.1）；"
        "個別方向之轉換分由 `-007`（`-116`，上鎖）與 `-005`（`-115`，解鎖）"
        "依其各自 source 承載 —— **拆本則即產出與該二者幾近重複之 TC，"
        "而 `-114` 所命之遲滯性質反而無人驗**。"),
}

# ── -005（-115 AC1）：解鎖方向 ────────────────────────────────────────
f, src = FEAT["115"][0], FEAT["115"][1]
TCS["005"] = {
    "pre_conditions": sig_pc(),
    "input_test_data": "NA",
    "test_procedure": (
        f"1. Send the signal {SPEED} = {LOCK}\n"
        f"2. Send the signal {SPEED} = {UNLOCK}\n"
        f"3. Select {f} and check that it opens"),
    "expected_result": (
        "1. The vehicle-speed signal is carried on the bus at raw 129, which is "
        "8.0625 km/h, above the 3 MPH threshold [ASSUMPTION A-DD6]\n"
        "2. The vehicle-speed signal is carried on the bus at raw 77, which is "
        "4.8125 km/h [ASSUMPTION A-DD6]\n"
        f"3. {f} opens and its view is displayed"),
    "design_method": "狀態轉換 (State Transition Testing)",
    "reasoning": (
        "驗證目標：車速自 3 MPH 之上降至 3 MPH 或以下時，受限解除 —— "
        f"斷言錨取 profile §2.1 觀察面 A，取樣 feature {f}（{src}）。"
        "關鍵情境條件：解鎖側取 raw **77**（4.8125 km/h＝2.9903 MPH），"
        "為 profile §3.1 依 R-DD7(c) 所定之 ≤3 MPH 側第一個可表示格，標 [ASSUMPTION A-DD6]。"
        "起始值取 raw 129 而非任意「3 MPH 以上」之值 —— 後者無 spec 來源，寫入即造值。"
        "一條 TC 即足：037 本列只有一條解鎖路徑。"
        "刻意略過：raw 78（不應解）為 BVA 之另一側，037 未書，不擴入（§8.2.1）；"
        "037 VC 第 2 項之 `\"Lock Out State\" variable to \"Unlocked\"` "
        "依 profile §2.3 不得入 ER，改以 HMI 之可及性承載。"),
}

# ── -007（-116 AC1）：上鎖方向 ────────────────────────────────────────
f, src = FEAT["116"][0], FEAT["116"][1]
TCS["007"] = {
    "pre_conditions": sig_pc(),
    "input_test_data": "NA",
    "test_procedure": (
        f"1. Send the signal {SPEED} = {UNLOCK}\n"
        f"2. Send the signal {SPEED} = {LOCK}\n"
        f"3. Select {f} and check that it does not open"),
    "expected_result": (
        "1. The vehicle-speed signal is carried on the bus at raw 77, which is "
        "4.8125 km/h, below the 5 MPH threshold [ASSUMPTION A-DD6]\n"
        "2. The vehicle-speed signal is carried on the bus at raw 129, which is "
        "8.0625 km/h [ASSUMPTION A-DD6]\n"
        f"3. {f} does not open and the screen stays as it was before the attempt"),
    "design_method": "狀態轉換 (State Transition Testing)",
    "reasoning": (
        "驗證目標：車速自 5 MPH 之下升至 5 MPH 或以上時，受限生效 —— "
        f"斷言錨取 profile §2.1 觀察面 A，取樣 feature {f}（{src}）。"
        "關鍵情境條件：上鎖側取 raw **129**（8.0625 km/h＝5.0097 MPH），"
        "為 profile §3.1 之 ≥5 MPH 側第一個可表示格，標 [ASSUMPTION A-DD6]；"
        "起始值取 raw 77（2.9903 MPH）—— 其為 profile §3.1 中唯一低於 5 MPH 之 spec 溯源格。"
        "一條 TC 即足：037 本列只有一條上鎖路徑。"
        "刻意略過：raw 128（不應鎖）037 未書，不擴入（§8.2.1）。"),
}

# ── -013／-015（-120／-121 AC1）：Lockout Table 之表列鎖定 ────────────
for lf, fam in (("013", "120"), ("015", "121")):
    f, src = FEAT[fam]
    TCS[lf] = {
        "pre_conditions": sig_pc(),
        "input_test_data": "NA",
        "test_procedure": (
            f"1. Send the signal {SPEED} = {LOCK}\n"
            f"2. Select {f} and check that it does not open"),
        "expected_result": (
            "1. The vehicle-speed signal is carried on the bus at raw 129, which is "
            "8.0625 km/h [ASSUMPTION A-DD6]\n"
            f"2. {f} does not open and the screen stays as it was before the attempt"),
        "design_method": "狀態轉換 (State Transition Testing)",
        "reasoning": (
            "驗證目標：受限態下，Lockout Table 標 `L/O` 之 feature 被鎖 —— "
            f"取樣 {f}，所據為 HMI spec {src}，"
            "**非黃標（黃標三項為 Player / RSE、Messaging、SRT Options，以 PDF 填色實測定位）、"
            "非 NAV 系（p7 註記逐字 `Embedded NAV for R1L is applicable to LATAM region only`）**。"
            "關鍵情境條件：037 本列之 Method 逐字 `send a speed above 5 MPH`，"
            "故取 profile §3.1 之上鎖側 raw 129，標 [ASSUMPTION A-DD6]。"
            "一條 TC 即足：037 本列只有一條常態路徑。"
            "刻意略過：**不逐一遍歷表列全部 feature** —— 037 本列未要求窮舉，"
            "以具名單一樣本承載（profile §2.1 禁泛稱，未禁單樣本）；"
            "解鎖方向與 BVA 另一側不擴入（§8.2.1）。"
            "**負向面（不在表內之 feature 仍可存取）本則未涵蓋** —— 見 `COVERAGE_GAPS.md` "
            "[CG-DD1]：該行為明載於 CFTS022 `-120`／`-121` 之驗證標準欄"
            "（`Features not listed in the table remain accessible`），"
            "**屬上游所有而非本層所造**；惟其樣本須具名一個「不在表內」之 feature，"
            "而 HMI spec p7 之 16 列**全部標 L/O**（表內無非 L/O 之列），"
            "CFTS022 之表本體又以圖片參照且該 xlsx 無任何嵌入物件（實測 0）——"
            "**權威表之內容於綁定來源中不存在，故無從確認任一 feature 不在表內**，"
            "具名即造值（§8.4.1）。表可機讀後即應於本則加該斷言（同一 trigger 之另一後果，§5.7）。"),
    }

# ── AC2 逾時族（-004／-006／-008／-014／-016）──────────────────────────
AC2_WHY = {
    "004": "`-114`", "006": "`-115`", "008": "`-116`",
    "014": "`-120`", "016": "`-121`",
}
for lf in ("004", "006", "008", "014", "016"):
    fam = META[lf][0]
    f, src = FEAT[fam]
    sibs = [f"`newR1L-DD-B{i:03d}`" for i in range(1, 1)]
    TCS[lf] = timeout_tc(lf, f, (
        "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— "
        f"斷言錨取 profile §2.1 觀察面 A，取樣 {f}（{src}）。"
        "關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 "
        "原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 "
        "`After the … signal timeout`，故為停送非送 SNA（raw 8191）。"
        "步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」"
        "分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。"
        "**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——"
        f"本列源自 {AC2_WHY[lf]}，其區別僅在取樣 feature 與追溯 ID，"
        "**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。"
        "刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"))


def main():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    rows = [list(r) for r in wb["Analysis Report"].iter_rows(values_only=True)]
    wb.close()

    order = ["003", "004", "005", "006", "007", "008", "013", "014", "015", "016"]
    lower = {
        "003": "(Both boundaries of the 5/3 MPH rule, exercised in one sequence)",
        "004": "(Fail-safe: the speed message is stopped and the menu-bar view is retried)",
        "005": "(Unlock at the 3 MPH boundary, approached from above)",
        "006": "(Fail-safe: the speed message is stopped and the phone book is retried)",
        "007": "(Lock at the 5 MPH boundary, approached from below)",
        "008": "(Fail-safe: the speed message is stopped and the auto reply editor is retried)",
        "013": "(Lockout of a table entry sampled from the Player row)",
        "014": "(Fail-safe: the speed message is stopped and the player search is retried)",
        "015": "(Lockout of a table entry sampled from the Phone row)",
        "016": "(Fail-safe: the speed message is stopped and pairing is retried)",
    }

    out = []
    for n, lf in enumerate(order, 1):
        src_row = rows[ROW[lf] - 1]
        half, mode, ntok = upper_half(src_row[3])
        assert half in src_row[3], lf
        assert ntok <= TOKEN_CAP, (lf, ntok)
        t = TCS[lf]
        out.append({
            "tc_id": f"newR1L-DD-B{n:03d}",
            "req_id": f"SWE1-RA-Driver_Distraction-{lf}",
            "test_group": "Driver Distraction",
            # framework.md Part II（Layer 2，經核准）—— 組 2 `Speed Monitoring`（003–008）、
            # 組 4 `Lockout Tables`（013–016）。**不以 TC 欄位既成事實變更之**（包 14 §二）。
            "test_set": "Speed Monitoring" if lf in
                        ("003", "004", "005", "006", "007", "008")
                        else "Lockout Tables",
            "test_item": half + "\n" + lower[lf],
            "pre_conditions": t["pre_conditions"],
            "input_test_data": t["input_test_data"],
            "test_procedure": t["test_procedure"],
            "expected_result": t["expected_result"],
            "spec_reference": OBJ[META[lf][0]],
            "tc_ref_id": "NEW",
            "priority": META[lf][1],
            "design_method": t["design_method"],
            "functional_safety": "NA",
            "author": "PeiPYHsu",
            "split_flag": False,
            "split_reason": "NA",
            "upper_half_provenance": {
                "source": f"037 Analysis Report r{ROW[lf]} c3 (Requirement Description)",
                "mode": mode, "tokens": ntok, "cap": TOKEN_CAP,
            },
            "reasoning": t["reasoning"],
        })

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", "utf-8")
    print(f"寫入 {OUT.name}：{len(out)} TC")
    for o in out:
        p = o["upper_half_provenance"]
        print(f"  {o['tc_id']}  {o['req_id']}  {o['priority']:<3} {o['test_set']:<24}"
              f"{p['mode']:<20} {p['tokens']}/{p['cap']}  {o['spec_reference']}")


if __name__ == "__main__":
    main()
