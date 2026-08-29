#!/usr/bin/env python3
"""T23a（下放包 17 §三）—— `Body Off Init` 生成：`-001`／`-002`（2 leaf）。

依 **R-DD20 v2**：
- (a) 同一性採定義級基礎（CFTS009 `4941238`），marker `A-DD10` 標於電源時序步驟
- (b) 施加式**以 power 線通稱式之風格新編**，條件與觀察錨定 CFTS009 逐字：
      Body OFF 定義 `4941028`／入眠 `4941238`／喚醒 `4941100`／醒後現象 `4941103`
- (c) `-002` 之終止步驟：業務行照 037 Method 逐字；**不附 `$` 指令行**（v3 改述）
- (f) `TLM_Status.Info`／`$Telematic_Power$` **不用於本二則**

**只生成，不寫回、不 git。** 產物：`generated/batch_body_off_init.json`
"""
import json
import re
from pathlib import Path

import openpyxl

ROOT = Path(__file__).resolve().parent.parent
A03 = ROOT / "inputs" / "DD_SWE1_0807_EN.xlsx"
OUT = ROOT / "generated" / "batch_body_off_init.json"
TOKEN_CAP = 50

SPEED = "$STATUS_CCAN3.VehicleSpeedVSOSig$"
OBJ = "CFTS022-4915104"                       # profile §1：`-113` 之 ObjectID
MK = "[ASSUMPTION A-DD10]"

# 取樣 feature —— HMI spec p7 `Driver Lockout Tables`，逐字。
# 可用列僅 5 個（黃標之 Player/RSE、Messaging、SRT Options 與 NAV 系皆排除，
# 見上繳 14 §三-3 之實測），故與他批共用；一則一個，使二則於 ER 可區辨。
FEAT = {
    "001": ('"Player Song, artist, title, etc. (speller search)"', "p7 top=330（Player 列）"),
    "002": ('"DND Customize auto reply message"', "p7 top=317（DND 列）"),
}

# 037 Method（c18）之逐字片語 —— `-002` 之業務行照此承載（R-DD20 v2(c)）
TERM_VERBATIM = "terminate the DD process in the test environment"

wb = openpyxl.load_workbook(A03, read_only=True, data_only=True)
_rows = [list(r) for r in wb["Analysis Report"].iter_rows(values_only=True)]
wb.close()
SRC = {"001": _rows[8], "002": _rows[9]}      # leaf → 037 列（1-based 9／10）


def upper_half(k):
    """test_item 上半：037 c3 逐字；逾 50 token 方摘句（本二則實測皆未逾）。"""
    full = str(SRC[k][3]).strip()
    n = len(full.split())
    assert n <= TOKEN_CAP, f"{k} 逾 {TOKEN_CAP} token（{n}）—— 須改摘句，勿逕截"
    return full, n


# ── 電源時序步驟（R-DD20 v2(b)）—— power 線通稱式之風格，條件錨定 CFTS009 ──
SLEEP_STEP = f"Bring the HU through the Body OFF power down {MK}"
SLEEP_ER = "The HU periodic messages are no longer present on the bus"
WAKE_STEP = f"Start CAN activity on Body CAN to wake the HU {MK}"
# 4941103 逐字：`Within 400 msec of wakeup mode, each module shall broadcast all
# periodic messages …` —— ER 不得含 modal（IN §6），故取其可觀察面，不取 `shall`
WAKE_ER = "The HU broadcasts all its periodic messages within 400 msec of wakeup"


def access(k):
    f, _ = FEAT[k]
    return (f"Open {f} and check that it opens",
            f"{f} opens and its view is displayed")


def build(k):
    up, ntok = upper_half(k)
    low = {
        "001": "(a normal wake-up from Body OFF leaves the locked-out features reachable)",
        "002": "(a cold start after the process was terminated during sleep leaves the locked-out features reachable)",
    }[k]
    acc_p, acc_e = access(k)
    if k == "001":
        proc = [SLEEP_STEP, WAKE_STEP, acc_p]
        er = [SLEEP_ER, WAKE_ER, acc_e]
    else:
        # **R-DD20 v3(c)（下放包 19 §二）：不附 `$` 指令行。**
        # 理由（條文逐字）：IN §5.4 之二行式適用於「步驟需 shell／adb／CAN 工具等
        # 外部指令」者；本步驟與同則之電源時序步驟（`Bring the HU through the
        # Body OFF power down`，亦不附指令）**同屬台架程序層級**，
        # 其可執行性屬台架程序，**非規格缺件** —— 故 IN §8.4.3 之佔位義務
        # 於本欄不發生，v1(c)／v2(c) 之 `PENDING: DR-DD9 <…>` 撤。
        term = TERM_VERBATIM[0].upper() + TERM_VERBATIM[1:]
        proc = [SLEEP_STEP, term, WAKE_STEP, acc_p]
        er = [SLEEP_ER,
              "The DD process is no longer running in the test environment",
              WAKE_ER, acc_e]
    numbered = lambda xs: "\n".join(f"{i}. {x}" for i, x in enumerate(xs, 1))
    return {
        # R-DD2：`newR1L-DD-{n:03d}`；n 取 leaf 號（Pei 2026-08-29 裁 leaf 升冪，
        # 24 leaf 為 001–024 連續，故 n 恆等於 leaf 號）
        "tc_id": f"newR1L-DD-{k}",
        "req_id": f"SWE1-RA-Driver_Distraction-{k}",
        "test_group": "Driver Distraction",
        "test_set": "Body Off Init",
        "test_item": up + "\n" + low,
        "pre_conditions": f"1. The signal {SPEED} is transmitted on the bus at 0 (0.0000 km/h)",
        "input_test_data": "NA",
        "test_procedure": numbered(proc),
        "expected_result": numbered(er),
        "spec_reference": OBJ,
        "tc_ref_id": "NEW",
        # profile §4 之 PR-c（解鎖方向常態、**初始化**、監看能力 → P1）；
        # 下放包 17 §三 書 `-001` = P0，與 profile §4 之 Pei 裁准列表相衝 ——
        # 見上繳 14 §三-1／§十 10-1，本輪照 profile §4 生成並提交裁定
        "priority": "P1",
        "design_method": None,          # §12 於 procedure 定稿後指派（下方機械判）
        "functional_safety": "NA",
        "author": "PeiPYHsu",
        "split_flag": False,
        "split_reason": "NA",
        "upper_half_provenance": {
            "source": f"037 Analysis Report r{9 if k == '001' else 10} c3 "
                      "(Requirement Description)",
            "mode": "full", "tokens": ntok, "cap": TOKEN_CAP,
        },
    }


TCS = [build("001"), build("002")]

# ── §12 first-match —— 與自檢同一機械判準（不由作者指定）──────────────
import importlib.util as _il
_spec = _il.spec_from_file_location("_sc", ROOT / "scripts" / "selfcheck_tcs.py")
MENU_ST = "狀態轉換 (State Transition Testing)"
NEG = re.compile(r"\b(no longer|not|never|absent|without)\b", re.I)
STOP = {"the", "a", "an", "is", "are", "on", "in", "of", "its", "it", "and",
        "to", "at", "from", "no", "longer", "not", "all", "any", "within"}
for tc in TCS:
    ers = tc["expected_result"].split("\n")
    bags = [(bool(NEG.search(e)),
             {w.lower().strip('".,') for w in re.sub(r"^\d+\.\s*", "", e).split()} - STOP)
            for e in ers]
    st = any(a != b and len(x & y) >= 3
             for i, (a, x) in enumerate(bags) for b, y in bags[i + 1:])
    tc["design_method"] = MENU_ST if st else "功能測試 (Functional based ; no specific technique)"

REASON = {
    "001": (
        "驗證目標：出眠後之 Lock Out State 初始化 —— 斷言錨取 profile §2.1 觀察面 A，"
        f"取樣 {FEAT['001'][0]}（{FEAT['001'][1]}，非黃標、非 NAV 系）。"
        "037 VC 之 `all Lock Out States are NOT_RESTRICTED` 依 profile §2.3 之四禁詞不入 ER，"
        "改以該 feature 之可及性承載。電源時序依 **R-DD20 v2(b)**：步驟以 power 線之通稱式風格新編"
        "（該線無本序列之施加步驟，上繳 13 §6.3 已實測），條件與觀察錨定 CFTS009 逐字 —— "
        "入眠 `4941238`（Body OFF → Standby → 無 CAN-I/CAN-C → Body Off HU System Sleep Mode）、"
        "喚醒 `4941100`（`With the Body Off mode and CAN bus activity is initiated by any CAN module, "
        "all modules shall wake up`）、醒後可觀察現象 `4941103`（`Within 400 msec of wakeup mode, "
        "each module shall broadcast all periodic messages`）；Body OFF 之定義為 `4941028` 之 "
        "`$PowerMode$` 五值 —— **該值以方括號書之，依 profile §2.5 不入四交付欄**，故錨定記於此。"
        "電源時序二步標 [ASSUMPTION A-DD10]（R-DD20 v2 之殘餘假設＝台架實現與 DR-DD9 回覆之一致性）。"
        "速度訊號源壓於 `0 (0.0000 km/h)` —— 使觀察可歸因於初始化值，非基準速度規則；0 非門檻值，"
        "**不掛 A-DD6**。PC 不含 Gear／PARK_BRK／Country_Code —— `-113` 未條件於市場與檔位，"
        "引入即擴入（IN §8.2.1）。**TLM_Status.Info 與 $Telematic_Power$ 不用**（R-DD20 v2(f)）。"),
    "002": (
        "驗證目標：sleep 中 DD process 被終止後之冷啟初始化 —— 斷言錨與取樣同 `-001` 之體例，"
        f"取樣改為 {FEAT['002'][0]}（{FEAT['002'][1]}）使二則於 ER 可區辨（IN §8.7）。"
        "終止步驟之**業務行照 037 Method（r10 c18）逐字承載** —— 原文 "
        f"`{TERM_VERBATIM}`（首字母大寫為步驟書寫之排版正規化，實詞未改）；"
        "**不附 `$` 指令行**（**R-DD20 v3(c)**）—— 本步驟與電源時序步驟同屬台架程序層級，其可執行性屬台架程序，**非規格缺件**，故 IN §8.4.3 之佔位義務不發生；v1(c)／v2(c) 之 `PENDING: DR-DD9 <…>` 已撤。"
        "**不得自 SYSAD 取服務名充之**（R-DD4：SYSAD 不入語料）。"
        "**本則自 R-DD20 v3(c) 起可出貨**（PENDING 已撤）；DR-DD9 降緩發，process 之具名為品質改善項。"
        "電源時序、marker、PC 之處置同 `-001`。"),
}
for tc in TCS:
    tc["reasoning"] = REASON[tc["req_id"][-3:]]

OUT.write_text(json.dumps(TCS, ensure_ascii=False, indent=2) + "\n", "utf-8")
print(f"寫入 {OUT.relative_to(ROOT.parent.parent)}：{len(TCS)} 則")
for tc in TCS:
    print(f"  {tc['tc_id']}  {tc['req_id']}  {tc['priority']}  {tc['design_method']}")
    print(f"    上半 {tc['upper_half_provenance']['tokens']} tok / cap {TOKEN_CAP}")
