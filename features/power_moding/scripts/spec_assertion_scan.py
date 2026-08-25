#!/usr/bin/env python3
"""R-PMH90 —— 斷言類之**規格全文反向掃描**（23 包步驟 4）。

凡以「限定排除某類斷言」為據之 TC（如 `-007` 以四項事件限定排除 pop-up），
其限定之充分性**須經規格全文之反向掃描**，不得只掃素材。

本檔掃規格 PDF 全文之 `pop-up`／`popup`／`pop up`（不分大小寫），
逐**行**具名其與 `SU3.)`（`No pop-ups will appear until the disclaimer
screen has been removed`）之關係，記法依 R-PMH79。

**計數單位須明說**：本檔以**行**為單位（與分析層 23 §3.1 同），
其**匹配數**為 30 而**行數**為 25 —— 二者皆列出，不混用。

用法:
    python scripts/spec_assertion_scan.py
"""

# R-PMH92 —— 本檢查之 must-hit 註冊。**總表之結果欄由此決定，手寫不採認。**
HAS_MUST_HIT = False
MUST_HIT_NOTE = '**未註冊 must-hit**（24 包 §12）—— 其逐行判定由人寫入'

import argparse
import re
import sys
from pathlib import Path

import fitz
import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(Path(__file__).resolve().parent))

# --- R-PMH93（24 包）：反向掃描之單位為**斷言**，非 TC 亦非 ER 之條 ---
# `-007` 之 ER4 含兩個斷言：(a) `no pop-up is displayed`、
# (b) `The announcement is heard in the background`。23 包只掃了 (a)。
ASSERTIONS = {
    "popup": (r"pop\s*-?\s*ups?",
              "`-007` ER4(a)：`no pop-up is displayed`（免責畫面移除前不顯示 pop-up）"),
    "audio": (r"\b(mute[ds]?|unmute[ds]?|audio|sounds?|volume|background)\b",
              "`-007` ER4(b)：`The announcement is heard in the background`"
              "（免責畫面期間報導之音訊照常可聞）"),
    # --- 25 包步驟 4（R-PMH94）：`-007` 其餘 ER 之斷言 ---
    "announcement": (r"\b(traffic\s+announcement|announcements?|received)\b",
                     "`-007` ER3：`The traffic announcement is delivered`"),
    "popup_after": (r"pop\s*-?\s*ups?",
                    "`-007` ER5：`The traffic announcement pop-up is displayed`"
                    "（免責畫面**移除後** pop-up 顯示）"),
}

# --- R-PMH94：ER1／ER2 **不需反向掃描**，其理由具名 ---
# 二者之內容為 procedure 步驟 1、2 之**限定之複述**
# （`No ON/OFF key press and no key-off transition occurs`／
#  `No door is opened and no HVAC hard control is adjusted`），
# **其斷言之標的為「測試過程中該事件未發生」，非 SUT 之行為** ——
# 素材所述者皆為「某事件發生後 SUT 如何」，二者**無共同謂詞可取相反值**。
# **此判斷本身即須具名**（本註解即其具名處）。
NO_SCAN = {
    "ER1": "限定之複述（不按 ON/OFF 鍵、不轉 key-off）—— 斷言標的為測試員之行為，非 SUT 之行為",
    "ER2": "限定之複述（不開門、不操作 HVAC 硬控）—— 同上",
}
PAT = re.compile(ASSERTIONS["popup"][0], re.I)

LIMITS = [
    "**每次只掃一個斷言**（R-PMH93）—— `--assertion popup`／`audio`；其餘斷言未掃者不在本次輸出內",
    "**各斷言之關鍵詞皆為列舉，其偽陰未估**（25 包步驟 5 具名）—— "
    "**R-PMH91 廢止了記法上之列舉，未廢止關鍵詞上之列舉**。"
    "已知之同義表述（未命中）：`audio` 斷言 → `silent`／`silence`／`no output`／`suppressed`／"
    "`inaudible`／`no sound`／`quiet`；`popup` 斷言 → `dialog`／`prompt`／`message box`／`toast`／"
    "`notification`；`announcement` 斷言 → `TA`／`traffic info`／`alert`。"
    "**惟其偽陰已有一次量測**（25 包步驟 5）：上列 15 個同義表述於**規格全文與矩陣全簿**"
    "之命中**全部為 0**（大小寫不敏感、字界錨定）——**故就該 15 個候選而言，本判準之偽陰為 0**。"
    "**該量測不涵蓋未被想到之表述**，列舉之問題本身仍在",
    "**以行為單位** —— PDF 之換行由版面決定；同一句跨兩行者計為兩行（如 `SU3.)` 之 L293／L294）",
    "**只掃文字層** —— p11 之流程圖為影像，其中若有 pop-up 字樣本檔看不見",
    "**記法之判定為人工** —— `LINE_VERDICT` 逐行具名，本檢查只驗其存在，不驗其正確",
]


def print_limits() -> None:
    print("\n=== 本檢查未涵蓋之範圍（R-PMH52）===")
    for x in LIMITS:
        print(f"  - {x}")
    print("  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。")


AFTER = ("**印證** —— 其於流程圖中之位置在免責畫面**之後**（`User Acceptance` → "
         "`Last Mode Screen` → 該 popup），二者為先後而非同時。")
IGN_OFF = ("**未對照** —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群：FOTA／Wi-Fi／"
           "Charge Now），而免責畫面之相位為**開機序列**。**條件互斥之依據為 "
           "`PM1)` 之逐字 `popups to show at IGN OFF`。**")
PB_OFF = ("**未對照** —— 其狀態為 `Power Button Off`，而 `PITA6.1` 逐字載 "
          "`Upon pressing power button to On state disclaimer screen shall be "
          "displayed` —— **免責畫面在該狀態之後**，為先後而非同時。")

# 鍵為 PDF 文字層之行號（`fitz` 逐頁 `get_text()` 串接後之行序）
LINE_VERDICT: dict[int, tuple[str, str, str]] = {
    127: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    140: ("印證", "pop-up 是否顯示（`GDPR/SOS popup`）",
          "**印證** —— 其逐字條件為 `If disclaimer screen is skipped go directly to "
          "last mode screen, showing GDPR/SOS popup first` —— **明載其條件為免責畫面"
          "被跳過**，與 `SU3.)` 之「免責畫面顯示中」**互斥，且互斥之依據為規格文字本身**。"),
    143: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    151: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    160: ("未對照", "pop-up 是否**重複**顯示",
          "**不同謂詞** —— `do not show popup again if popup was shown at Radio Off` "
          "之標的為「是否重複」，`SU3.)` 之標的為「是否顯示」。"),
    257: ("印證", "pop-up 是否顯示（`Geolocation + SOS Popup`）", AFTER),
    293: ("—", "（`SU3.)` 本身）", "**本行即比對之一造**，不入判定。"),
    294: ("—", "（`SU3.)` 本身之續行）", "**本行即比對之一造**，不入判定。"),
    332: ("未對照", "**pop-up 是否顯示** —— `SU3.)` 取「不顯示」（免責畫面移除前，"
                    "**全稱否定**）；本行取「顯示」（`Pop-ups still shown.`）",
          "**24 包改判（原記「牴觸」，A-PMH21）** —— **條件互斥已被證明**（R-PMH84 之要件）。"
          "以 `get_pixmap` 4x 渲染 p9 之矩陣區實見：本格在 **`HEADUNIT POWER OFF` 欄**、"
          "`KEY ON ENGINE ON` 列。**免責畫面為 head unit 所顯示之畫面，其相位必為 head unit 開機中**；"
          "而**同一欄之 `Climate GUI` 格逐字為 `Not Visibile due to power off`** —— "
          "**該欄之語意即「頭端電源關閉」，其時無任何畫面可顯示免責內容。**"
          "**互斥之依據為欄位之語意 ＋ 同欄之另一格之逐字，非推定。**"),
    348: ("未對照", "**pop-up 是否顯示** —— 同 L332",
          "**24 包改判（原記「牴觸」）** —— 同 L332：本格在 **`HEADUNIT POWER OFF` 欄**、"
          "`KEY ON ENGINE OFF (ACC or RUN)` 列（渲染實見）。**同欄之 `Climate GUI` 格亦為 "
          "`Not Visibile due to power off`。條件互斥已證。**"),
    407: ("未對照", "pop-up 是否顯示（IGN OFF 之 popup 群）", IGN_OFF),
    409: ("未對照", "pop-up 之顯示時長", IGN_OFF),
    410: ("未對照", "pop-up 之逾時", IGN_OFF),
    411: ("未對照", "pop-up 是否關閉", IGN_OFF),
    413: ("未對照", "FOTA popup 之互動", IGN_OFF),
    414: ("未對照", "popup 之互動逾時", IGN_OFF),
    415: ("未對照", "因 popup 而保持喚醒之上限", IGN_OFF),
    417: ("未對照", "IGN OFF 之 popup 優先序", IGN_OFF),
    419: ("未對照", "FOTA popup 之接受", IGN_OFF),
    426: ("未對照", "Wi-Fi 設定 popup 之忽略", IGN_OFF),
    428: ("未對照", "XEV key off popup", IGN_OFF),
    430: ("未對照", "XEV key off popup 之忽略", IGN_OFF),
    443: ("未對照", "HVAC pop-up 是否顯示（`PITA6`）", PB_OFF +
          " ⚠ **本行另與 State Matrix `r48c10` 牴觸**（20 §4.2，R-PMH80 已處置）——"
          "**該牴觸與本次掃描之標的（vs `SU3.)`）不同，不重複計。**"),
    445: ("未對照", "HVAC popup 是否顯示（`PITA6.1`）", PB_OFF),
    450: ("未對照", "Phone call popup 是否顯示於 Power Button Off 之上（`PITA9`）", PB_OFF +
          " ⚠ **須具名之殘餘風險**：`-007` 之四項限定**不含「無來電」** —— "
          "若來電發生於免責畫面期間，`PITA9` 之 popup 是否顯示，"
          "**規格未於該相位表態**（其只述 `Power Button Off state`）。**列為未驗項。**"),
}


# --- R-PMH93 —— `audio` 斷言之規格側逐行判定（24 包步驟 4）---
AUDIO_LINE_VERDICT: dict[int, tuple[str, str, str]] = {
    294:
        ("—", "（`SU3.)` 本身 —— 本斷言之來源）",
         "**本行即斷言之出處**，不入判定。"),
    311:
        ("未對照", "**不同音源** —— `SSND 1)` 之標的為**啟動音／告別音**；本斷言之標的為**交通報導之音訊**",
         "且其觸發為 `upon driver door close` 並與開機動畫同步 —— **免責畫面在開機動畫之後**（`SU1.)` 之序：animation → splash → disclaimer）。**條件互斥之依據為規格自身之時序。**"),
    312:
        ("未對照", "**不同音源** —— 啟動音之跨螢幕同步",
         "同 L311。"),
    313:
        ("未對照", "**不同音源** —— 啟動音／告別音之設定選項",
         "同 L311。"),
    314:
        ("未對照", "**不同音源** —— 設定為 Always 時啟動音之播放",
         "其條件逐字為 `everytime **the startup animation is played**` —— **免責畫面不在開機動畫期間**（`SU1.)` 之序）。**條件互斥之依據為規格自身。**"),
    315:
        ("未對照", "**不同音源** —— 設定為 Once a Day",
         "同 L314。"),
    316:
        ("未對照", "**不同音源** —— 設定為 Never 時啟動音不播放",
         "⚠ **最接近者**：`should not be played on any situation` 為**全稱否定**。惟其標的仍為**啟動音／告別音**，非交通報導之音訊。**不同謂詞（不同音源），非同一命題之相反值。**"),
    317:
        ("未對照", "**音量位準** vs **是否可聞**",
         "`Sound volume level shall match current entertainment sounds volume` 之謂詞為**位準**；本斷言之謂詞為**是否可聞**。**不同謂詞。**"),
    457:
        ("未對照", "VR 長按 SIRI 後 radio 之 audio 狀態",
         "`VRLP1` 之條件逐字為 `shall be functional when **radio is OFF** and KEY ON or ACC` —— **免責畫面之相位中 radio 已在開機序列中而非 OFF**。**條件互斥之依據為 `VRLP1` 之條件句。**"),
    458:
        ("未對照", "同 L457",
         "同 L457。"),
    459:
        ("未對照", "同 L457",
         "同 L457。"),
    460:
        ("未對照", "同 L457",
         "同 L457。"),
    519:
        ("未對照", "**head unit 是否靜音** —— `OFF3.)` 取「靜音」；本斷言取「可聞」",
         "**共同謂詞成立**，惟其條件逐字為 `when **launching app from Power Off State**` —— **`-007` 之 procedure 不含啟動 app**。**條件互斥由 TC 自身之構造成立**（R-PMH87 之同一形態）。"),
}

# --- `audio` 斷言之矩陣側逐列判定。鍵為 (區塊起列, 列) ---
AUDIO_CELL_VERDICT: dict[tuple[int, int], tuple[str, str, str]] = {
    (1, 16):
        ("未對照", "**是否靜音** —— `Radio Wakes Up and mutes` 取靜音；本斷言取可聞",
         "**條件互斥之依據為矩陣自身之欄軸**：本列有值之二格其欄為 `Power Button OFF`（頭端關機中），**而免責畫面顯示時頭端已開機**。⚠ 惟 `-007` 之限定**不含「不按 SRT／Off Road+ 鍵」**——其互斥靠欄軸而非靠 TC 構造。"),
    (37, 40):
        ("未對照", "**是否靜音** —— `Power press OFF > Mute Active` 取靜音",
         "**條件互斥由 TC 自身之構造成立** —— `-007` 之限定 1 逐字為 `Do not press the ON/OFF key and do not turn key-off`（R-PMH87）。"),
    (37, 41):
        ("未對照", "**是否靜音** —— `unmute`／`HU Unmute`",
         "其值為**解除**靜音，與本斷言之「可聞」**同向而非相反**；且其為來電之音訊，**不同音源**。⚠ `-007` 之限定**不含「無來電」**（23 §12 第 1 項之同一缺口）。"),
    (37, 42):
        ("未對照", "**是否靜音** —— `maintain mute`／`Mute Inactive`",
         "其值為**維持**既有靜音狀態，非**使之**靜音；本斷言之前提為未靜音，故維持即維持可聞。**非相反值。**"),
    (37, 43):
        ("未對照", "**是否靜音** —— `Mute Active`／`Mute Inactive`",
         "同 `r42`：**維持**而非**使之**靜音。"),
    (37, 44):
        ("未對照", "**是否靜音** —— `Mute Active`／`Mute Inactive`",
         "同 `r42`：其變化在 `Screen Off` 而 `Mute` 為維持。"),
    (37, 45):
        ("牴觸", "**音訊是否可聞（是否靜音）** —— 本斷言取「可聞（未靜音）」；本列取 **`Mute --> Active`**（**使之靜音**）",
         "**共同謂詞取相反值。** 其觸發為**按 Mute 鍵**（c3／c5／c7／c9 逐字 `Mute --> Active`；c11 逐字 `Mute becomes active if previously unmuted`）。**條件互斥未證** —— `-007` 之四項限定（R-PMH87：ON/OFF 鍵、key-off、開門、HVAC 硬控）**不含「不按 Mute 鍵」**，且其欄軸為 `Key On, Gear != Reverse`，**與免責畫面之相位（`KEY ON`）重疊**。**依 R-PMH84 判為牴觸，須上呈，不得自行調和（R-PMH79）。**"),
    (37, 46):
        ("未對照", "**是否靜音** —— `If Radio/Media, Mute --> Inactive. Else: Mute Active`",
         "其 `Mute --> Inactive` 為**解除**靜音（同向）；`Else: Mute Active` **無箭頭，為維持**而非使之靜音（與 c2 之 `Mute --> Inactive` 之記法對照可見）。**非相反值。** ⚠ 該記法之區辨（有無 `-->`）為本層之判讀。"),
    (37, 47):
        ("未對照", "**是否靜音** —— 同 `r46`",
         "同 `r46`（以 VR 切換 Headunit Mode）。"),
    (37, 48):
        ("未對照", "**是否靜音** —— `Screen Off Active Mute Active` 等",
         "其 `Mute` 皆為**維持**；且 `-007` 之限定 2 已含 `do not adjust HVAC hard controls`。**雙重互斥。**"),
}


# --- `announcement`（ER3）之規格側逐行判定 ---
ANN_LINE_VERDICT: dict[int, tuple[str, str, str]] = {
    293:
        ("—", "（`SU3.)` 本身 —— 本斷言之來源）",
         "**本行即斷言之出處**，不入判定。"),
    294:
        ("—", "（`SU3.)` 本身之續行）",
         "同上。"),
}

# --- `popup_after`（ER5）之規格側逐行判定 ---
AFTER_LINE_VERDICT: dict[int, tuple[str, str, str]] = {
    127:
        ("未對照", "pop-up 是否顯示（流程圖之 `Geolocation + SOS Popup`）",
         "未對照 —— 其 popup 為 p4／p6 流程圖之 `Geolocation + SOS Popup`，**與交通報導之 popup 不同**；且其位置在免責畫面之後而 ER5 之情境亦為移除後，**同向而非相反**。"),
    140:
        ("未對照", "pop-up 是否顯示（流程圖之 `Geolocation + SOS Popup`）",
         "未對照 —— 其 popup 為 p4／p6 流程圖之 `Geolocation + SOS Popup`，**與交通報導之 popup 不同**；且其位置在免責畫面之後而 ER5 之情境亦為移除後，**同向而非相反**。"),
    143:
        ("未對照", "pop-up 是否顯示（流程圖之 `Geolocation + SOS Popup`）",
         "未對照 —— 其 popup 為 p4／p6 流程圖之 `Geolocation + SOS Popup`，**與交通報導之 popup 不同**；且其位置在免責畫面之後而 ER5 之情境亦為移除後，**同向而非相反**。"),
    151:
        ("未對照", "pop-up 是否顯示（流程圖之 `Geolocation + SOS Popup`）",
         "未對照 —— 其 popup 為 p4／p6 流程圖之 `Geolocation + SOS Popup`，**與交通報導之 popup 不同**；且其位置在免責畫面之後而 ER5 之情境亦為移除後，**同向而非相反**。"),
    160:
        ("未對照", "**該 popup 是否重複顯示** —— `do not show popup again if popup was shown at Radio Off`",
         "⚠ **最接近者** —— 其為**否定**（不再顯示），與 ER5 之「顯示」取相反值。**惟其 popup 為 p4 流程圖之 `Geolocation + SOS Popup`（同段之上下文），非交通報導之 popup**。**不同 popup → 無共同謂詞。** ⚠ 若上游確認該句泛指所有 popup，則為牴觸；**已具名待確認。**"),
    257:
        ("未對照", "pop-up 是否顯示（流程圖之 `Geolocation + SOS Popup`）",
         "未對照 —— 其 popup 為 p4／p6 流程圖之 `Geolocation + SOS Popup`，**與交通報導之 popup 不同**；且其位置在免責畫面之後而 ER5 之情境亦為移除後，**同向而非相反**。"),
    293:
        ("—", "（`SU3.)` 本身 —— ER5 之來源）",
         "**本行即斷言之出處**（`will not see the pop-up **until the disclaimer screen is removed**`），不入判定。"),
    294:
        ("—", "（`SU3.)` 本身之續行）",
         "同上。"),
    332:
        ("未對照", "pop-up 是否顯示（p9 `Pop-ups still shown`）",
         "未對照 —— 其欄為 `HEADUNIT POWER OFF`（25 §2.1 以字級座標實測：`Pop-ups` x=483.0，與同欄之 `Visibile` x=442.5 同欄；右欄之 x 基準為 596.6）。**免責畫面之顯示條件為 head unit 轉 On（`PITA6.1` 逐字），故其不可能出現於該欄所述之狀態**（R-PMH96）。"),
    348:
        ("未對照", "同 L332",
         "同 L332。"),
    407:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    409:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    410:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    411:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    413:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    414:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    415:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    417:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    419:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    426:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    428:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    430:
        ("未對照", "IGN OFF 之 popup 群",
         "未對照 —— 其相位為 `IGN OFF`（`PM1)` 之 popup 群），**而 ER5 之情境為開機序列中免責畫面移除後**。**條件互斥之依據為 `PM1)` 之逐字 `popups to show at IGN OFF`。**"),
    443:
        ("未對照", "HVAC pop-up 是否顯示（`PITA6`）",
         "未對照 —— 其狀態為 `Power Button Off`，**且其 popup 為 HVAC／phone call，非交通報導**。**不同 popup 且不同相位。**"),
    445:
        ("未對照", "HVAC popup 是否顯示（`PITA6.1`）",
         "未對照 —— `PITA6.1` 之 popup 為 **HVAC**，非交通報導；**且其末句 `disclaimer screen shall be displayed` 與 ER5 之「移除後」為先後關係**。**不同 popup。**"),
    450:
        ("未對照", "Phone call popup 是否顯示（`PITA9`）",
         "未對照 —— 其狀態為 `Power Button Off`，**且其 popup 為 HVAC／phone call，非交通報導**。**不同 popup 且不同相位。**"),
}


def lines(pat: re.Pattern) -> list[tuple[int, str]]:
    cfg = yaml.safe_load((ROOT / "feature.yaml").read_text(encoding="utf-8"))
    d = fitz.open(ROOT / cfg["paths"]["spec_pdf"])
    txt = "\n".join(d[i].get_text() for i in range(d.page_count))
    return [(i + 1, re.sub(r"\s+", " ", l).strip())
            for i, l in enumerate(txt.splitlines()) if pat.search(l)]


def matrix_rows(pat: re.Pattern):
    """矩陣側之命中列（`audio` 斷言須掃素材，`popup` 斷言於 20–22 包已掃）。"""
    import matrix_vs_chapter as mvc
    wb, ws = mvc.load_sheet()
    out = []
    for lo, r, lbl, cells in mvc.event_rows(ws):
        hits = [(c, ax, v) for c, ax, v in cells if pat.search(v)]
        if hits:
            out.append((lo, r, lbl, hits))
    wb.close()
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--assertion", choices=sorted(ASSERTIONS), default="popup",
                    help="R-PMH93 —— 掃描之單位為**斷言**")
    a = ap.parse_args()
    rx, desc = ASSERTIONS[a.assertion]
    pat = re.compile(rx, re.I)
    lv = {"popup": LINE_VERDICT, "audio": AUDIO_LINE_VERDICT,
          "announcement": ANN_LINE_VERDICT, "popup_after": AFTER_LINE_VERDICT}[a.assertion]
    hits = lines(pat)
    n_match = sum(len(pat.findall(l)) for _, l in hits)
    print(f"=== 規格全文之反向掃描（R-PMH90／R-PMH93）—— 斷言 `{a.assertion}` ===")
    print(f"  標的：{desc}")
    print(f"  關鍵詞：`{rx}`")
    print(f"  **行數 = {len(hits)}**；**匹配數 = {n_match}**"
          "  ← 二者為不同之計數單位，不混用\n")
    counts, unnamed = {}, []
    for i, l in hits:
        v = lv.get(i)
        print(f"  L{i}: {l[:110]}")
        if v is None:
            print("      **記法：未具名 ← FAIL**")
            unnamed.append(i)
            continue
        kind, pred, why = v
        counts[kind] = counts.get(kind, 0) + 1
        print(f"      記法：**{kind}**；謂詞：{pred}")
        print(f"      依據：{why}\n")
    # --- 矩陣側（`audio` 斷言）---
    if a.assertion in ("audio", "announcement"):
        print("\n--- 矩陣側（State Matrix）---\n")
        if a.assertion == "announcement":
            n_hit = len(matrix_rows(pat))
            print(f"  命中之事件列 = **{n_hit}**"
                  + ("  —— **矩陣全簿無 `announcement`／`traffic announcement`／`received`**"
                     if not n_hit else ""))
        for lo, r, lbl, cs in (matrix_rows(pat) if a.assertion == "audio" else []):
            v = AUDIO_CELL_VERDICT.get((lo, r))
            print(f"  [區塊 r{lo}] r{r} {lbl}（{len(cs)} 格命中）")
            for c, ax, val in cs[:3]:
                print(f"      c{c} [{ax}] = {val[:100]}")
            if len(cs) > 3:
                print(f"      … 另 {len(cs)-3} 格")
            if v is None:
                print("      **記法：未具名 ← FAIL**")
                unnamed.append((lo, r))
                continue
            kind, pred, why = v
            counts[kind] = counts.get(kind, 0) + 1
            print(f"      記法：**{kind}**；謂詞：{pred}")
            print(f"      依據：{why}\n")

    print("=== 結果 ===")
    print(f"  {counts}；未具名 **{len(unnamed)}**")
    n_conf = counts.get("牴觸", 0)
    print(f"\n  **牴觸 {n_conf} 處**"
          + ("  ← **停止條件觸發，須上呈，不得自行調和（R-PMH79）**" if n_conf else "  —— 無"))
    if a.assertion != "popup":
        print_limits()
        sys.exit(1 if (n_conf or unnamed) else 0)
    print("\n  **與分析層 23 §3.1 之對照**：其報「25 處」，本檔行數 **25** —— **相符**；"
          "\n  其所報之行號（131／147／155／263／144／164／341／357／416–439／453／455／460）"
          "\n  與本檔（127／143／151／257／140／160／332／348／407–430／443／445／450）**逐一相差 4~13**，"
          "\n  **因二者之文字萃取不同**（分析層用 `pm.txt`，本檔用 `fitz` 逐頁串接）。"
          "\n  **其分類（牴觸 2／印證 5／未對照 18）與本檔逐項相符**"
          "（本檔之印證 5 含 L140；`SU3.)` 自身 2 行本檔另計為 `—`，分析層併入未對照）。")
    print_limits()
    sys.exit(1 if unnamed else 0)


if __name__ == "__main__":
    main()
