#!/usr/bin/env python3
"""T21b（下放包 15 §三）—— 批次 B2 生成：`-017`~`-024`（8 leaf）。

乙案（R-DD19）解凍：`$VC_Trans_Equipped$` 依 A-DD8 之施加路徑、
A-DD9 之兩極代表值生成。**R-DD19(c) 硬邊界：MTA(2)／DDCT(3) 不入任何 TC。**

`test_item` 上半自 037 機器擷取（逾 50 token 取 `Case`＋`Then` 連續摘句）。
**只生成，不寫回、不 git。** 產物：`generated/batch_b2.json`
"""
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
A03 = ROOT / "inputs" / "DD_SWE1_0807_EN.xlsx"
OUT = ROOT / "generated" / "batch_b2.json"
TOKEN_CAP = 50

SPEED = "$STATUS_CCAN3.VehicleSpeedVSOSig$"
GEAR = "$PT_SYSTEM_FD_1.GearEngagedForDisplay_PT$"
BRAKE = "$BCM_FD_9.ParkBrakeSts$"
GEAR_MSG, BRAKE_MSG = '"PT_SYSTEM_FD_1"', '"BCM_FD_9"'

# profile §1 —— HK 章閘 ＋ 條文 ObjectID（升冪，一行一 ID）
GATE = "CFTS022-4915120"
OBJ = {"126": "CFTS022-4915121", "127": "CFTS022-4915122",
       "128": "CFTS022-4915123", "129": "CFTS022-4915124"}

# 取樣 feature —— HMI spec p7，黃標與 NAV 系皆已排除；一個 Requirement 家族一個
FEAT = {
    "126": ('"Pairing (1st time)"', "p7 top=304（Phone 列）"),
    "127": ('"Reconfigurable menu bar"', "p7 top=356（Menu Bar 列）"),
    "128": ('"Edit phone book (speller input)"', "p7 top=291（Phone 列）"),
    "129": ('"DND Customize auto reply message"', "p7 top=317（DND 列）"),
}
# leaf → (source 條文, priority, AC)
META = {
    "017": ("126", "P1", 1), "018": ("126", "P1", 2),
    "019": ("127", "P0", 1), "020": ("127", "P1", 2),
    "021": ("128", "P1", 1), "022": ("128", "P1", 2),
    "023": ("129", "P0", 1), "024": ("129", "P1", 2),
}
ROW = {f"{n:03d}": 8 + n for n in range(17, 25)}

# A-DD9 之兩極（R-DD19(b)）；**2/3 為硬邊界，本表刻意不含**
AUTO = "PROXI Gear_Box_Type = 4 (ATX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]"
MANU = "PROXI Gear_Box_Type = 1 (MTX) [ASSUMPTION A-DD8] [ASSUMPTION A-DD9]"
PARK, NONPARK = "12 (Park)", "15 (Drive)"          # 非 P 代表值：T21a


def upper_half(text):
    lines = text.split("\n")
    if len(text.split()) <= TOKEN_CAP:
        return text, "full", len(text.split())
    i = next(k for k, l in enumerate(lines) if l.startswith("Case"))
    j = next(k for k, l in enumerate(lines) if l.startswith("Then"))
    exc = "\n".join(lines[i:j + 1])
    return exc, "excerpt(Case..Then)", len(exc.split())


def pc(trans):
    return ("1. The signal " + SPEED + " is transmitted on the bus at 0 (0.0000 km/h)\n"
            "2. PROXI Country_Code = 91\n"
            "3. " + trans)


AC2_WHY = (
    "關鍵情境條件：失效形態取**匯流排逾時**（停送承載訊息），"
    "依 profile §3.2「逐 leaf 依 037 AC2 原文定」——本列 AC2 逐字書 "
    "`cannot obtain valid … input`，其 Method 逐字書 `Stop or suppress … updates` 與 "
    "`After the agreed input timeout`。**所停之訊號取該 source AC1 所條件之訊號**"
    "（下放包 15 §3.4）—— 判定所需之訊號即 AC1 之條件訊號。"
    "**PROXI 參數不作失效標的**（其為組態非訊號，停送無從施加）——"
    "故 037 Method 所列之另一選項（`make VC_Trans_Equipped unavailable`）不取。"
    "步驟 2 先確認訊號正常時該 feature 可用，否則末步之「不可用」"
    "分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。"
    "**基準態取該 source 家族之「可解除」側** —— AC2 之原文**未條件於檔位或手煞之值**"
    "（其僅書 `required … input is unavailable`），故基準之選定為測試佈置，"
    "非對需求之主張，不構成擴入 sibling（IN §8.2.1）。"
)

TCS = {}

# ── AC1 四則 ────────────────────────────────────────────────────────
AC1 = {
    "017": ("126", AUTO, "自排", GEAR, PARK, True),
    "019": ("127", AUTO, "自排", GEAR, NONPARK, False),
    "021": ("128", MANU, "手排", BRAKE, "1 (ON)", True),
    "023": ("129", MANU, "手排", BRAKE, "0 (OFF)", False),
}
for lf, (fam, trans, kind, sig, val, unlocked) in AC1.items():
    f, src = FEAT[fam]
    mk = " [ASSUMPTION A-DD2]" if sig == BRAKE else ""
    TCS[lf] = {
        "pre_conditions": pc(trans),
        "input_test_data": "NA",
        "test_procedure": (
            "1. Send the signal " + sig + " = " + val + mk + "\n"
            "2. Open " + f + " and check that it "
            + ("opens" if unlocked else "does not open")),
        "expected_result": (
            "1. The signal " + sig + " is carried on the bus at " + val + mk + "\n"
            + ("2. " + f + " opens and its view is displayed"
               if unlocked else
               "2. " + f + " does not open and the screen stays as it was before the attempt")),
        "design_method": "決策表 (Decision Table Testing)",
        "reasoning": (
            "驗證目標：香港市場條件下，" + kind + "車之"
            + ("解除" if unlocked else "受限") + "判定 —— 斷言錨取 profile §2.1 觀察面 A，"
            "取樣 " + f + "（" + src + "，非黃標、非 NAV 系）。"
            "037 VC 之 `Listener receives a … notification` 依 profile §2.3 不入 ER，"
            "改以該 feature 之可及性承載。"
            "關鍵情境條件：市場 `PROXI Country_Code = 91`（確定值，A-DD5 已撤，不掛 marker）；"
            "變速箱型式依 **R-DD19** 之乙案，施加路徑掛 [ASSUMPTION A-DD8]、"
            "代表值掛 [ASSUMPTION A-DD9]"
            + ("（`4 (ATX)`）" if trans is AUTO else "（`1 (MTX)`）") + "；"
            + ("手煞訊號名依 **R-DD18** 採認上游書面回覆之 `PARK_BRK_EDG`，"
               "其 CAN 對應為 T19c 實測所得，規範欄未更正故掛 [ASSUMPTION A-DD2]。"
               if sig == BRAKE else
               ("檔位取 `12 (Park)`（DBC `VAL_` 逐字）。"
                if val == PARK else
                "檔位取 **`15 (Drive)`** —— 037 書 `<> [P]` 為一**類**，"
                "類內任一成員皆合法；於非 P 之 17 個成員中取行車常態檔位，"
                "`0 (Initialize)` 與 `31 (SNA)` 不取（前者為初始化態、後者為訊號不可用，"
                "取之會把「檔位非 P」與「檔位未知」混為一談），"
                "`13 (Neutral)`／`14 (Reverse)` 亦合法而未取。**類內取樣非假設，不掛 marker**（T21a）。"))
            + "速度訊號源壓於 `0 (0.0000 km/h)` —— **排除基準速度規則之干擾**，"
            "使觀察可歸因於"
            + ("檔位" if sig == GEAR else "手煞") + "；0 非門檻值，**不掛 A-DD6**。"
            "一條 TC 即足：037 本列只有一條常態路徑。"
            "刻意略過：**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位** —— "
            "其歸屬為 DR-DD6 之未決問題，R-DD19(c) 定為硬邊界；"
            "fail-safe 面由同 source 之 AC2 列承載。"),
    }

# ── AC2 四則 ────────────────────────────────────────────────────────
AC2 = {
    "018": ("126", AUTO, GEAR, PARK, GEAR_MSG, "gear"),
    "020": ("127", AUTO, GEAR, PARK, GEAR_MSG, "gear"),
    "022": ("128", MANU, BRAKE, "1 (ON)", BRAKE_MSG, "brake"),
    "024": ("129", MANU, BRAKE, "1 (ON)", BRAKE_MSG, "brake"),
}
SIB = {"018": "`newR1L-DD-C004`（`-020`）", "020": "`newR1L-DD-C002`（`-018`）",
       "022": "`newR1L-DD-C008`（`-024`）", "024": "`newR1L-DD-C006`（`-022`）"}
GRP = {"018": "組 3（`-018`／`-020`）", "020": "組 3（`-018`／`-020`）",
       "022": "組 4（`-022`／`-024`）", "024": "組 4（`-022`／`-024`）"}
for lf, (fam, trans, sig, val, msg, kind) in AC2.items():
    f, src = FEAT[fam]
    mk = " [ASSUMPTION A-DD2]" if sig == BRAKE else ""
    TCS[lf] = {
        "pre_conditions": pc(trans),
        "input_test_data": "NA",
        "test_procedure": (
            "1. Send the signal " + sig + " = " + val + mk + "\n"
            "2. Open " + f + ", then leave it\n"
            "3. Stop transmitting the message " + msg + " and let the input timeout elapse\n"
            "4. Open " + f + " again and check that it does not open"),
        "expected_result": (
            "1. The signal " + sig + " is carried on the bus at " + val + mk + "\n"
            "2. " + f + " opens and its view is displayed, and the previous screen "
            "is shown again after leaving it\n"
            "3. The message " + msg + " is no longer present on the bus and the input "
            "timeout window has elapsed\n"
            "4. " + f + " does not open and the screen stays as it was before the attempt"),
        "design_method": "基礎故障注入 (Fault Injection Lite)",
        "reasoning": (
            "驗證目標：香港市場條件下，判定所需之車輛訊號消失時，fail-safe 使受限 feature "
            "不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 " + f + "（" + src + "）。"
            + AC2_WHY +
            "本列所停者為" + ("檔位訊息 " + msg if kind == "gear" else "手煞訊息 " + msg) + "。"
            "市場 `PROXI Country_Code = 91`（確定值）；變速箱型式依 R-DD19 掛 "
            "[ASSUMPTION A-DD8]／[ASSUMPTION A-DD9]"
            + ("；手煞訊號名依 R-DD18 掛 [ASSUMPTION A-DD2]。" if sig == BRAKE else "。")
            + "速度訊號源壓於 `0`，排除基準速度規則之干擾，不掛 A-DD6。"
            "**本列之 037 原文與 " + SIB[lf] + " 逐字全等**（A-DD7 " + GRP[lf] + "）——"
            "其區別僅在取樣 feature 與追溯 ID，**不得以取樣之不同偽稱為不同之驗證目標**"
            "（下放包 10 §四）。"
            "刻意略過：SNA 路徑 037 本列未書，寫入即造值；"
            "**`MTA`(2)／`DDCT`(3) 不入本則之任何欄位**（R-DD19(c) 硬邊界）。"),
    }


def main():
    wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
    rows = [list(r) for r in wb["Analysis Report"].iter_rows(values_only=True)]
    wb.close()

    lower = {
        "017": "(Automatic transmission with the gear selector in Park)",
        "018": "(Fail-safe: the gear message is stopped and pairing is retried)",
        "019": "(Automatic transmission with the gear selector away from Park)",
        "020": "(Fail-safe: the gear message is stopped and the menu-bar view is retried)",
        "021": "(Manual transmission with the parking brake applied)",
        "022": "(Fail-safe: the parking-brake message is stopped and the phone book is retried)",
        "023": "(Manual transmission with the parking brake released)",
        "024": "(Fail-safe: the parking-brake message is stopped and the auto reply editor is retried)",
    }
    out = []
    for n, lf in enumerate(sorted(META), 1):
        src_row = rows[ROW[lf] - 1]
        half, mode, ntok = upper_half(src_row[3])
        assert half in src_row[3], lf
        assert ntok <= TOKEN_CAP, (lf, ntok)
        fam, prio, _ = META[lf]
        t = TCS[lf]
        # R-DD19(c) 硬邊界之生成端自檢 —— 其所禁者為「作 Pre-Condition 或輸入」，
        # 故掃**四個交付欄**；`reasoning` 得載明其被排除（紀錄非輸入）。
        deliver = " ".join(t[k] for k in ("pre_conditions", "input_test_data",
                                          "test_procedure", "expected_result"))
        for bad in (r"Gear_Box_Type\s*=\s*[23]\b", r"\bMTA\b", r"\bDDCT\b"):
            assert not re.search(bad, deliver), (lf, bad)
        out.append({
            "tc_id": f"newR1L-DD-C{n:03d}",
            "req_id": f"SWE1-RA-Driver_Distraction-{lf}",
            "test_group": "Driver Distraction",
            "test_set": "Hong Kong Market",
            "test_item": half + "\n" + lower[lf],
            "pre_conditions": t["pre_conditions"],
            "input_test_data": t["input_test_data"],
            "test_procedure": t["test_procedure"],
            "expected_result": t["expected_result"],
            "spec_reference": GATE + "\n" + OBJ[fam],
            "tc_ref_id": "NEW",
            "priority": prio,
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
        print(f"  {o['tc_id']}  {o['req_id']}  {o['priority']:<3} "
              f"{p['mode']:<20} {p['tokens']}/{p['cap']}  "
              f"{o['spec_reference'].replace(chr(10), '+')}  {o['design_method'][:6]}")


if __name__ == "__main__":
    main()
