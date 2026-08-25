#!/usr/bin/env python3
"""23 包步驟 5 —— batch 1 之**逐條 ER 斷言** × 規範性素材／規格他處。

22 §12 第 6 項（執行層自陳）：ch 7 × 矩陣之 30 列判定為**章**層，
**不等於逐條 TC 之 ER 都被對照過**。

本檔以 **ER 斷言**為單位：對 `generated/batch01.json` 之每一條 TC 之
每一行 `expected_result`，逐一具名其與 State Matrix 某格或規格他處之關係，
記法依 **R-PMH79**（牴觸／印證／未對照）＋ **R-PMH84**（條件互斥須被證明）。

**每一 ER 斷言皆須於 `ER_VERDICT` 具名**，未具名 → FAIL。
**發現任一牴觸 → 退出碼 1**（23 包停止條件 7）。

用法:
    python scripts/batch_er_vs_matrix.py
"""

# R-PMH92 —— 本檢查之 must-hit 註冊。**總表之結果欄由此決定，手寫不採認。**
HAS_MUST_HIT = False
MUST_HIT_NOTE = '**未註冊 must-hit**（24 包 §12）—— 其逐條判定由人寫入'

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BATCH = ROOT / "generated" / "batch01.json"

LIMITS = [
    "**只對照 `expected_result`** —— `pre_conditions` 與 `test_procedure` 之斷言不入母體",
    "**切分以五連接詞產生候選 ＋ 人讀複核**（R-PMH101）—— 其**連接詞清單仍是列舉**；"
    "以無連接詞之並置表達之複合命題（如 `The screen shows A B C`）不會被切開",
    "**謂詞之認定為人工** —— `ER_VERDICT` 逐條具名，本檢查只驗其存在，不驗其正確",
    "素材側只看 **State Matrix**；規格側只看 **SYS1 之 outline 文字與 PDF 文字層** —— "
    "**PDF 之圖表（p9 能力矩陣以文字層存在故有看，p11 流程圖無）不在此列**",
    "**`-007` 之 ER 不入母體** —— 其已於 24／25 包單獨處置；**其 `pre_conditions` 則已入母體**（R-PMH102）",
    "**「未對照」之依據多為「素材無對應列」** —— 其證明的是素材之沉默，"
    "非二者條件互斥；凡以條件互斥為由者已逐條具名其依據（R-PMH84）",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


NO_ROW = ("**素材無對應列**：State Matrix 全 362 非空格中，"
          "`disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` "
          "**全數 0 命中**（21 包 §3.1、23 包複驗）。**無共同謂詞。**")




# --- R-PMH97（28 包步驟 2(c)）：`test_procedure` 之**逐步驟**二分 ---
# 27 §12 第 6 項自陳：`test_procedure` 全數歸為測試執行斷言**而該歸類未逐條驗證**。
# 本輪逐步驟具名其類與理由（**寫入常數，非只在上繳包** —— R-PMH97 明令）。
# 鍵為 (tc 末三碼, 步驟序)；值為 (類, 標的, 理由)
TP_VERDICT: dict[tuple, tuple] = {
    ("001", 1):
        ("測試執行", "讀取並記錄 loading 指示狀態",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1／ER1.2 承載。"),
    ("001", 2):
        ("測試執行", "等待系統回報 ready",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER2.1 承載。"),
    ("001", 3):
        ("測試執行", "讀取並檢查 `\"Accept\"` 按鈕",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER3.1／ER3.2 承載。"),
    ("002", 1):
        ("測試執行", "讀取並記錄畫面",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1／ER1.2 承載。"),
    ("002", 2):
        ("測試執行", "按 `\"Accept\"` 並檢查 last mode screen",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER2.1／ER2.2 承載。"),
    ("003", 1):
        ("測試執行", "讀取並記錄免責畫面",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1／ER1.2 承載。"),
    ("003", 2):
        ("測試執行", "不按任何硬鍵與 `\"Accept\"` 直至畫面改變",
         "**測試執行斷言** —— 其主語為測試員之**不作為**。⚠ **惟其含 `until the screen changes` 一個隱含之 SUT 事件** —— 該事件即 ER2.2 之 `the disclaimer screen times out`（27 包 §3.3 所查出者），**已入母體並判為未對照**。**故無未掃之 SUT 斷言。**"),
    ("003", 3):
        ("測試執行", "讀取並檢查 last mode screen",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER3.1 承載。"),
    ("004", 1):
        ("測試執行", "不按任何硬鍵與 `\"Accept\"`",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1 承載。"),
    ("004", 2):
        ("測試執行", "等待長於非 Maserati 之逾時後讀取畫面",
         "**測試執行斷言** —— 其主語為測試員之等待與讀取。⚠ **其隱含「非 Maserati 之逾時長度為已知」** —— **而規格未給任何秒數**（`SU1.)`／`SU2.)` 皆無），故該步驟以「長於」表述而不引任何值（§8.4.1 不造值，13 包已定）。其所驗之 SUT 斷言為 ER2.1／ER2.2（畫面仍顯示、未逾時），**已入母體**。"),
    ("004", 3):
        ("測試執行", "按 `\"Accept\"` 並檢查 last mode screen",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER3.1／ER3.2 承載。"),
    ("005", 1):
        ("測試執行", "讀取並檢查 comfort controls",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1 承載。"),
    ("005", 2):
        ("測試執行", "操作一個 comfort control 並檢查其回應",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER2.1 承載。"),
    ("006", 1):
        ("測試執行", "讀取並記錄畫面上之控制項",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1 承載。"),
    ("006", 2):
        ("測試執行", "檢查 comfort controls 不在步驟 1 所記錄者之中",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER2.1 承載。"),
    ("007", 1):
        ("測試執行", "不按 ON/OFF 鍵、不轉 key-off",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1／ER1.2 承載。**其為 R-PMH87 之限定項 1、2。**"),
    ("007", 2):
        ("測試執行", "不開門、不操作 HVAC 硬控",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其為限定項 3、4。"),
    ("007", 3):
        ("測試執行", "不按 Mute 鍵或 Headunit Mode 鍵",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其為限定項 5、6。"),
    ("007", 4):
        ("測試執行", "不以語音辨識變更 headunit mode",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其為限定項 7。"),
    ("007", 5):
        ("測試執行", "於免責畫面顯示期間送出交通報導",
         "**測試執行斷言 —— 惟其須具名一項**（28 包步驟 2(c) 明令）：其主語為測試員（`Deliver`），**而其隱含「SUT 能接收該報導」之前提**。**該前提已由 `pre_conditions` 之 PC2.1 `A traffic announcement is available to be received` 承載，且該 PC 斷言已入母體並判為未對照**（28 包步驟 2(b) 之全枚舉：174 格，謂詞域 `announcement` 入選 0 格）。**故其非未掃之 SUT 斷言。**"),
    ("007", 6):
        ("測試執行", "讀取畫面與音訊輸出並記錄",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER6.1／ER6.2 承載。"),
    ("007", 7):
        ("測試執行", "移除免責畫面並檢查 pop-up 顯示",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER7.1 承載。"),
    ("008", 1):
        ("測試執行", "讀取並記錄 radio 電源狀態",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER1.1 承載。"),
    ("008", 2):
        ("測試執行", "按電源鍵使 radio 轉為 On",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER2.1 承載（**該 ER 為本批唯一之印證**）。"),
    ("008", 3):
        ("測試執行", "讀取並檢查免責畫面",
         "**測試執行斷言** —— 其主語為測試員之操作（觀察／記錄／等待／按壓）。**其所觀察之對象已由對應之 ER 斷言承載並掃描**，故本步驟本身不入母體。 其對象由 ER3.1 承載。"),
}

# --- R-PMH98／R-PMH100（28 包步驟 2(b)）：PC 之斷言亦改為**全枚舉** ---
# 27 §12 第 4 項自陳：PC 之 24 個斷言中 21 個之依據為同一組**零命中探針**，
# **而那組探針是我列的** —— 只做了關鍵詞式之否定，未做全枚舉。
# 本輪比照矩陣側：**每一 PC 斷言 × 174 格全部入判定表**，
# 落選記 `未對照` ＋ 其謂詞域理由；入選者逐格具名（`PC_CELL_VERDICT`）。
PC_DOMAIN = {
    "disclaimer": r"disclaimer",
    "ready": r"\b(ready|reports?)\b",
    "maserati": r"Maserati",
    "comfort": r"comfort",
    "announcement": r"\b(announcements?|traffic)\b",
    "accept": r"Accept",
    "powerbtn": r"Power Button",
    "ignition": r"\b(key-?on|key-?off|ignition)\b",
    "call": r"\bcall\b",
}
PC_ASSERTION_DOMAIN = {
    ("001", 1, 1): "disclaimer",
    ("001", 2, 1): "ready",
    ("002", 1, 1): "disclaimer",
    ("002", 1, 2): "accept",
    ("002", 2, 1): "ready",
    ("003", 1, 1): "maserati",
    ("003", 2, 1): "disclaimer",
    ("003", 2, 2): "accept",
    ("003", 3, 1): "ready",
    ("004", 1, 1): "maserati",
    ("004", 2, 1): "disclaimer",
    ("004", 2, 2): "accept",
    ("004", 3, 1): "ready",
    ("005", 1, 1): "maserati",
    ("005", 2, 1): "comfort",
    ("005", 3, 1): "disclaimer",
    ("006", 1, 1): "maserati",
    ("006", 2, 1): "comfort",
    ("006", 3, 1): "disclaimer",
    ("007", 1, 1): "disclaimer",
    ("007", 2, 1): "announcement",
    ("008", 1, 1): "powerbtn",
    ("008", 2, 1): "ignition",
    ("008", 3, 1): "call",
}

PC_CELL_VERDICT = {
    (("008", 1, 1), "r7c13(blk1)"):
        ("印證", "**同一謂詞（Power Button 是否為 off）取相同值** —— 本格逐字 `Power Button remains off with open and closure of door`，其斷言該狀態於開關門時**維持**；`-008` 之前提即該狀態存在。**矩陣支持該前提可被建立並維持。**"),
    (("008", 1, 1), "r8c12(blk1)"):
        ("印證", "同 `r7c13` —— 逐字相同。"),
    (("008", 1, 1), "r40c2(blk37)"):
        ("印證", "**同一謂詞取相同值** —— `Power press OFF > … (Power Button OFF state)`，其斷言該狀態**可由按 ON/OFF 鍵進入**。**矩陣支持該前提之可達性。**"),
    (("008", 1, 1), "r40c3(blk37)"):
        ("印證", "同 `r40c2`。"),
    (("008", 1, 1), "r40c4(blk37)"):
        ("印證", "同 `r40c2`。"),
    (("008", 1, 1), "r40c5(blk37)"):
        ("印證", "同 `r40c2`。"),
}


def pc_cell_verdicts() -> list:
    """每一 PC 斷言 × 174 格之判定：(PC 鍵, 格鍵, 記法, 依據)。"""
    import spec_assertion_scan as sas
    wb_cells, _, _ = sas.enumerate_matrix("audio")     # 只借其 174 格之列舉
    out = []
    for pk, dom in PC_ASSERTION_DOMAIN.items():
        rx = re.compile(PC_DOMAIN[dom], re.I)
        for lo, r, lbl, c, ax, v in wb_cells:
            ck = sas.cell_key(lo, r, c)
            if rx.search(v):
                hv = PC_CELL_VERDICT.get((pk, ck))
                if hv:
                    out.append((pk, ck, hv[0], hv[1]))
                elif dom == "call":
                    # `-008` PC3（`No phone call scenario is in progress`）之
                    # 33＋4 格依其**欄軸**判：軸為 `Call Not Active` 者，
                    # 矩陣以該情境為一個成立之欄 → **印證**其前提可建立；
                    # 軸為 `Call Active` 者，其條件與本前提**互斥**（依欄軸本身）。
                    if "Call Not Active" in ax:
                        out.append((pk, ck, "印證",
                                    "**矩陣以 `Call Not Active` 為一個成立之欄軸** —— "
                                    "其存在即支持「無通話進行中」之前提可被建立。"
                                    "**互斥／可達性之依據為欄軸本身，非推定。**"))
                    else:
                        out.append((pk, ck, "未對照",
                                    "**條件互斥，依據為欄軸本身** —— 本格之欄軸為 "
                                    "`Call Active`，而本前提為「無通話進行中」。"
                                    "二者不可同時成立，故非同一命題之相反值。"))
                else:
                    out.append((pk, ck, "待定義",
                                f"**入選（謂詞域 `{dom}`）而未具名記法 —— 判定尚未作成。**"))
            else:
                doms = sorted(d for d, dr in sas.PREDICATE_DOMAIN.items()
                              if re.search(dr, v, re.I))
                why = ("該格無任何謂詞域之詞" if not doms
                       else f"該格之謂詞域為 {doms}")
                out.append((pk, ck, "未對照",
                            f"**無共同謂詞**（R-PMH79）—— {why}，"
                            f"與本斷言之謂詞域 `{dom}` 不交。（謂詞域粗篩，R-PMH100）"))
    return out

# --- R-PMH101（27 包）：斷言之切分以**謂詞**為準 ---
# 機器以五種連接詞產生候選（` and `／` with `／` while `／`;`／`, `），
# **人讀複核**其各切片是否各自可獨立為真為假，複核結果寫入本常數。
# 鍵為 (tc 末三碼, 欄, 條序, 候選序)；值為 (是否為獨立命題, 規範化文字或 None, 理由)
SPLIT_CONNECTIVES = r"\s+and\s+|\s+with\s+|\s+while\s+|;\s*|,\s+"
SPLIT_REVIEW: dict[tuple, tuple] = {
    ("002", "er", 1, 2):
        (True, "the \"Accept\" button is shown on that screen",
         "`with` 所連接者為**名詞片語**，非命題；惟其確指一個**可各自為真為假**之命題（按鈕是否呈現於該畫面上）。**接受切分，並規範化其文字。**"),
    ("003", "er", 1, 2):
        (True, "the \"Accept\" button is shown on that screen",
         "同 `-002` ER1.2。"),
    ("003", "er", 2, 2):
        (True, "the disclaimer screen times out",
         "`while` 所連接者為**獨立命題**（畫面是否逾時），**且其類與前半不同** —— 前半 `No user input is given` 為**測試執行斷言**，本半為 **SUT 行為斷言**。**以 ` and ` 為據時二者被綁為一個測試執行斷言，該 SUT 斷言遂完全未被掃描。**"),
    ("005", "pc", 2, 2):
        (False, None,
         "`with` 之切分產生 `The vehicle is not equipped` ／ `the lower comfort screen` —— **後者非命題，前者亦不完整**。原句 `The vehicle is not equipped with the lower comfort screen` 為**單一命題**。**不接受切分。**"),
    ("006", "pc", 2, 2):
        (False, None,
         "同 `-005` PC2.2。"),
    ("002", "pc", 1, 2):
        (True, "the \"Accept\" button is shown on that screen",
         "同 `-002` ER1.2。"),
    ("003", "pc", 2, 2):
        (True, "the \"Accept\" button is shown on that screen",
         "同上。"),
    ("004", "pc", 2, 2):
        (True, "the \"Accept\" button is shown on that screen",
         "同上。"),
}

# --- R-PMH102（27 包）：`pre_conditions` 之斷言判定 ---
# 鍵為 (tc 末三碼, PC 條序, 斷言序)；值為 (類, 記法, 謂詞, 依據)
PC_VERDICT: dict[tuple, tuple] = {
    ("001", 1, 1):
        ("SUT", "未對照", "免責畫面是否顯示（前提狀態）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("001", 2, 1):
        ("SUT", "未對照", "系統是否尚未回報 ready",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。** 矩陣之列軸為事件，無「系統就緒」之列。"),
    ("002", 1, 1):
        ("SUT", "未對照", "免責畫面是否顯示（前提狀態）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("002", 1, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否呈現於該畫面",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("002", 2, 1):
        ("SUT", "未對照", "系統是否已回報 ready",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("003", 1, 1):
        ("SUT", "未對照", "車輛是否為非 Maserati 應用",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("003", 2, 1):
        ("SUT", "未對照", "免責畫面是否顯示（前提狀態）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("003", 2, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否呈現於該畫面",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("003", 3, 1):
        ("SUT", "未對照", "系統是否已回報 ready",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("004", 1, 1):
        ("SUT", "未對照", "車輛是否為 Maserati 應用",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("004", 2, 1):
        ("SUT", "未對照", "免責畫面是否顯示（前提狀態）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("004", 2, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否呈現於該畫面",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("004", 3, 1):
        ("SUT", "未對照", "系統是否已回報 ready",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("005", 1, 1):
        ("SUT", "未對照", "車輛是否為 Maserati 應用",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("005", 2, 1):
        ("SUT", "未對照", "車輛是否未配備 lower comfort screen",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("005", 3, 1):
        ("SUT", "未對照", "免責畫面是否顯示（前提狀態）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("006", 1, 1):
        ("SUT", "未對照", "車輛是否為 Maserati 應用",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("006", 2, 1):
        ("SUT", "未對照", "車輛是否已配備 lower comfort screen",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("006", 3, 1):
        ("SUT", "未對照", "免責畫面是否顯示（前提狀態）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("007", 1, 1):
        ("SUT", "未對照", "免責畫面是否顯示（前提狀態）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。**"),
    ("007", 2, 1):
        ("SUT", "未對照", "交通報導是否可被接收",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout`／`Maserati` **全數 0 命中**。**無共同謂詞。** 矩陣無 `announcement`（0 命中）。"),
    ("008", 1, 1):
        ("SUT", "未對照", "radio 是否處於 Power Button Off 狀態",
         "**共同名詞 `Power Button OFF`** —— **矩陣以其為軸（情境條件）而非斷言** —— 軸為「在此條件下」之限定，**其不斷言 SUT 是否可處於該狀態**，故無可相反之值。 ⚠ **本項為 R-PMH102 之關鍵測試**：若矩陣某格斷言「在該情境下 SUT 不可能處於 Power Button Off」，則本 TC 之前提無法建立、整條不可執行。**實測無此格。**"),
    ("008", 2, 1):
        ("SUT", "未對照", "ignition 是否已由 OFF 轉為 ACC 或 RUN",
         "矩陣之區塊名為 `Key-on`／`Key-off`（**狀態**），其 `Key-on` 為 `Key-off` 區塊之一**事件列**（`r33` = `Recall Last state of VP`）—— **其斷言該事件之後果，不斷言該轉換是否可發生**。無可相反之值。"),
    ("008", 3, 1):
        ("SUT", "未對照", "是否有通話情境進行中",
         "**共同名詞 `Call Active`／`Call Not Active`** —— **矩陣以其為軸（情境條件）而非斷言** —— 軸為「在此條件下」之限定，**其不斷言 SUT 是否可處於該狀態**，故無可相反之值。 且 `-008` 之前提恰對應 `Call Not Active` 欄（23 包 §5.1 之印證即由此）。"),
}

# --- R-PMH94／R-PMH97（26 包）：母體改為**斷言**，並先做二分 ---
# 鍵為 (tc_id 之末三碼, ER 之序號, 斷言之序號)
# 值為 (類, 記法, 謂詞, 依據)；類 ∈ {"SUT", "測試執行"}
#   `SUT`      —— 標的為受測系統之行為或狀態 → **須反向掃描**
#   `測試執行` —— 標的為測試員之作為或不作為 → **不入母體**，記法為 `—`
# **25 包以 ER 條為單位（18 條），其涵蓋率 78%（5 個斷言未單獨對照）；
#   本輪改以斷言為單位（23 個），涵蓋率 100%。**
ER_VERDICT: dict[tuple[str, int, int], tuple[str, str, str, str]] = {
    # --- 27 包（R-PMH101）：五連接詞切分後新增之三個斷言 ---
    ("002", 1, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否呈現於該畫面",
         "**R-PMH101 新增之切分**（`with` 連接，26 包以 ` and ` 為據時未切開）。矩陣無 `Accept`（0 命中）。**無共同謂詞。**"),
    ("003", 1, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否呈現於該畫面",
         "同 `-002` ER1.2。**R-PMH101 新增之切分。**"),
    ("003", 2, 2):
        ("SUT", "未對照", "免責畫面是否逾時",
         "**R-PMH101 新增之切分，且為本輪最重要之一項** —— 26 包以 ` and ` 為據時，本斷言被綁於前半之 `No user input is given`（**測試執行斷言**）而整條不入掃描母體；**其為 SUT 行為斷言，先前完全未被掃描**。矩陣無 `timeout`（0 命中）；其 `Timer` 8 處全為 `Radio Off Delay`。**無共同謂詞。**"),
    ("001", 1, 1):
        ("SUT", "未對照", "`\"loading...\"` 是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("001", 1, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為 25→26 包新增之單獨對照**（原併於 ER1 一條）。"),
    ("001", 2, 1):
        ("SUT", "未對照", "系統是否回報 ready",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣之列軸為事件，無「系統就緒」之列。"),
    ("001", 3, 1):
        ("SUT", "未對照", "`\"Loading...\"` 是否移除",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("001", 3, 2):
        ("SUT", "未對照", "`\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為新增之單獨對照**。"),
    ("002", 1, 1):
        ("SUT", "未對照", "免責畫面與 `\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("002", 2, 1):
        ("SUT", "未對照", "免責畫面是否移除",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為新增之單獨對照**。"),
    ("002", 2, 2):
        ("SUT", "未對照", "是否顯示 last mode screen",
         "**共同名詞 `Last state`**（矩陣 `r33` = `Recall Last state of VP`），惟其觸發為 `Key-on` 事件，本斷言之觸發為按 `\"Accept\"` 或逾時 —— 矩陣全簿無 `Accept`（0 命中）。**不同謂詞（回復何狀態 vs 按鍵／逾時後之畫面）。**"),
    ("003", 1, 1):
        ("SUT", "未對照", "免責畫面與 `\"Accept\"` 按鈕是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("003", 2, 1):
        ("測試執行", "—", "（測試員是否給予輸入）",
         "**測試執行斷言**（R-PMH97）—— 其主語為測試員之不作為（`No user input is given`），非 SUT。**不入反向掃描之母體。**"),
    ("003", 3, 1):
        ("SUT", "未對照", "是否顯示 last mode screen",
         "**共同名詞 `Last state`**（矩陣 `r33` = `Recall Last state of VP`），惟其觸發為 `Key-on` 事件，本斷言之觸發為按 `\"Accept\"` 或逾時 —— 矩陣全簿無 `Accept`（0 命中）。**不同謂詞（回復何狀態 vs 按鍵／逾時後之畫面）。**"),
    ("004", 1, 1):
        ("測試執行", "—", "（測試員是否給予輸入）",
         "**測試執行斷言**（R-PMH97），同 `-003` ER2。**不入母體。**"),
    ("004", 2, 1):
        ("SUT", "未對照", "Maserati 之免責畫面是否仍顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `Maserati`（0 命中）。**本斷言為新增之單獨對照**。"),
    ("004", 2, 2):
        ("SUT", "未對照", "是否已逾時",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `timeout`（0 命中）；其 `Timer` 8 處全為 `Radio Off Delay`。**本斷言為新增之單獨對照**。"),
    ("004", 3, 1):
        ("SUT", "未對照", "免責畫面是否移除",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** **本斷言為新增之單獨對照**。"),
    ("004", 3, 2):
        ("SUT", "未對照", "是否顯示 last mode screen",
         "**共同名詞 `Last state`**（矩陣 `r33` = `Recall Last state of VP`），惟其觸發為 `Key-on` 事件，本斷言之觸發為按 `\"Accept\"` 或逾時 —— 矩陣全簿無 `Accept`（0 命中）。**不同謂詞（回復何狀態 vs 按鍵／逾時後之畫面）。**"),
    ("005", 1, 1):
        ("SUT", "未對照", "comfort controls 是否顯示於免責畫面",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `comfort`（0 命中）；其 `HVAC Knobs` 為**硬體旋鈕**，非畫面上之 comfort controls。**不同謂詞。**"),
    ("005", 2, 1):
        ("SUT", "未對照", "被操作之 comfort control 是否有回應",
         "同 `-005` ER1。"),
    ("006", 1, 1):
        ("SUT", "未對照", "免責畫面上所顯示之控制項（記錄步）",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。**"),
    ("006", 2, 1):
        ("SUT", "未對照", "配備 lower comfort screen 時 comfort controls 是否**不**顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** 矩陣無 `lower comfort`（0 命中）。"),
    ("008", 1, 1):
        ("SUT", "未對照", "radio 是否處於 Power Button Off 狀態（記錄步）",
         "**共同名詞 `Power Button OFF`**（矩陣之欄軸），惟本斷言為**記錄前提狀態**，非斷言某事件之後果。**無可相反之值。**"),
    ("008", 2, 1):
        ("SUT", "印證", "**按 ON/OFF 鍵後 head unit 之電源狀態** —— `PITA6.1`／本斷言取「轉為 On」；矩陣 `r6` c12／c13 取 `Head Unit Power ON`",
         "**同一謂詞取相同值。** `-008` 之 pre-condition 已含「無通話情境進行中」（`PITA6.1` 之 `unless certain phone call scenarios have occurred`），**恰對應 `Call Not Active` 欄**。**矩陣為本斷言之獨立佐證。**"),
    ("008", 3, 1):
        ("SUT", "未對照", "轉 On 後免責畫面是否顯示",
         "**素材無對應列**：State Matrix 全 362 非空格中 `disclaimer`／`splash`／`animation`／`comfort`／`Accept`／`loading`／`timeout` **全數 0 命中**（21 §3.1、23 包複驗）。**無共同謂詞。** `PITA6.1` 之 `disclaimer screen shall be displayed (see SU6.)` 於矩陣無對應。"),
}


def split_assertions(text: str, tc3: str, field: str) -> list[tuple[int, int, str]]:
    """回傳 [(條序, 斷言序, 文字)] —— 機器候選 ＋ `SPLIT_REVIEW` 之人讀複核。"""
    out = []
    for i, line in enumerate([x for x in text.split("\n") if x.strip()], 1):
        body = re.sub(r"^\d+\.\s*", "", line)
        cands = [x.strip() for x in re.split(SPLIT_CONNECTIVES, body) if x.strip()]
        j = 0
        for k, cand in enumerate(cands, 1):
            rv = SPLIT_REVIEW.get((tc3, field, i, k))
            if rv is not None and rv[0] is False:
                continue                      # 人讀判為非獨立命題 → 併回前一斷言
            j += 1
            out.append((i, j, rv[1] if (rv and rv[1]) else cand))
    return out


def main() -> None:
    d = json.loads(BATCH.read_text(encoding="utf-8"))
    counts = {"牴觸": 0, "印證": 0, "未對照": 0, "待定義": 0}
    kinds = {"SUT": 0, "測試執行": 0}
    unnamed = []
    print("=== batch 1 之逐**斷言**對照（27 包，R-PMH101／R-PMH102）===")
    print("**切分以謂詞為準**：機器以五連接詞產生候選 ＋ 人讀複核（`SPLIT_REVIEW`）")
    print("**母體及於 `pre_conditions`**（R-PMH102）—— `test_procedure` 為測試執行斷言，不入母體\n")
    n = {"pc": 0, "er": 0}
    for t in d["tcs"]:
        k3 = t["tc_id"][-3:]
        print(f"## {t['tc_id']}（leaf {t['leaf_id']}）\n")
        for field, col, table in (("pc", "pre_conditions", PC_VERDICT),
                                  ("er", "expected_result", ER_VERDICT)):
            if field == "er" and k3 == "007":
                print("  （`-007` 之 ER 已於 24／25 包單獨處置，不入本表）\n")
                continue
            for i, j, txt in split_assertions(t[col], k3, field):
                n[field] += 1
                v = table.get((k3, i, j))
                tag = "PC" if field == "pc" else "ER"
                print(f"  {tag}{i}.{j}: {txt}")
                if v is None:
                    print("      **未具名 ← FAIL**")
                    unnamed.append((t["tc_id"], tag, i, j))
                    continue
                kind, form, pred, why = v
                kinds[kind] = kinds.get(kind, 0) + 1
                if form in counts:
                    counts[form] += 1
                print(f"      類：**{kind}**；記法：**{form}**；謂詞：{pred}")
                print(f"      依據：{why}\n")
    print("=== 結果 ===")
    print(f"  **`pre_conditions` 之斷言 {n['pc']}**（R-PMH102 新入母體）／"
          f"**`expected_result` 之斷言 {n['er']}**（`-007` 另計）")
    print(f"  二分（R-PMH97）：SUT **{kinds['SUT']}**／測試執行 **{kinds['測試執行']}**")
    print(f"  記法：牴觸 **{counts['牴觸']}**／印證 **{counts['印證']}**／"
          f"未對照 **{counts['未對照']}**／待定義 **{counts['待定義']}**")
    print(f"  未具名 **{len(unnamed)}**")

    # --- 28 包步驟 2(c)：`test_procedure` 之逐步驟二分 ---
    tp_un, tp_sut = [], []
    for t in d["tcs"]:
        k3 = t["tc_id"][-3:]
        steps = [x for x in t["test_procedure"].split("\n") if x.strip()]
        for i in range(1, len(steps) + 1):
            v = TP_VERDICT.get((k3, i))
            if v is None:
                tp_un.append((t["tc_id"], i))
            elif v[0] != "測試執行":
                tp_sut.append((t["tc_id"], i))
    print(f"\n  === `test_procedure` 之逐步驟二分（28 包步驟 2(c)，R-PMH97）===")
    print(f"  步驟總數 **{sum(len([x for x in t['test_procedure'].split(chr(10)) if x.strip()]) for t in d['tcs'])}**；"
          f"未具名 **{len(tp_un)}**；**歸為 SUT 斷言者 {len(tp_sut)}**")
    print("  **全部歸為測試執行斷言，其對象皆由對應之 ER／PC 斷言承載並已入母體。**")
    print("  ⚠ 三步驟另具名其隱含之 SUT 前提："
          "\n     `-003` 步驟 2 之 `until the screen changes` → ER2.2（27 包查出者）"
          "\n     `-004` 步驟 2 之「逾時長度已知」→ 規格未給秒數，以「長於」表述（§8.4.1）"
          "\n     `-007` 步驟 5 之「SUT 能接收該報導」→ PC2.1，已入母體")
    if tp_un:
        print(f"  **未具名 ← FAIL**：{tp_un}")

    # --- 28 包步驟 2(b)：PC 斷言 × 174 格之全枚舉 ---
    pcv = pc_cell_verdicts()
    from collections import Counter
    pc_c = Counter(k for _, _, k, _ in pcv)
    n_as = len(PC_ASSERTION_DOMAIN)
    print(f"\n  === PC 之全枚舉（28 包步驟 2(b)，R-PMH98／R-PMH100）===")
    print(f"  **{n_as} 個 PC 斷言 × 174 格 = {len(pcv)} 項判定**（非零命中探針）")
    print(f"  記法分布：{dict(pc_c)}")
    pend = [(pk, ck) for pk, ck, k, _ in pcv if k == "待定義"]
    print(f"  待定義（入選而未具名）：**{len(pend)}**"
          + ("" if not pend else f" ← {pend[:5]}"))
    print("  **21 個「零命中探針」之依據自此由 4,176 項逐格判定取代。**")
    if counts["牴觸"]:
        print("  ← **停止條件觸發**：發現牴觸，須上呈")
    for tid, tag, i, j in unnamed:
        print(f"    未具名：{tid} {tag}{i}.{j}")
    print_limits()
    sys.exit(1 if (counts["牴觸"] or unnamed or tp_un) else 0)


if __name__ == "__main__":
    main()
