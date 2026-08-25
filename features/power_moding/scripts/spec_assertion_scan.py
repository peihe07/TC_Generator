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
HAS_MUST_HIT = True
MUST_HIT_NOTE = '`--cell-must-hit` 兩項（分類錯誤 → FAIL／無用詞者不誤報）—— R-PMH100 使偽陰自此可檢查；**惟逐行之 `LINE_VERDICT` 仍由人寫入，本錨點不驗其正確**'

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
    # --- 29 包步驟 3（R-PMH107(a)）：batch 2 之 `-009`／`-010` 之動畫斷言 ---
    # **既有檢查對新資料之適用，非新增檢查項** —— 判別法見 R-PMH107。
    "animation": (r"\b(animations?|start-?up\s+animation|shut-?down\s+animation)\b",
                  "`-009` ER3／ER5：`The start-up sound starts when the driver door is "
                  "closed`／`… is synchronised with the start-up animation`；"
                  "`-010` ER3～ER5：`The shut-down animation starts`／"
                  "`The goodbye sound starts at the start of the animation`"),
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
    "**粗篩之判準仍以詞為之**（R-PMH98 允許之兩層作法）—— 其與關鍵詞之差別在於"
    "**落選之格逐格具名其落選理由，非靜默略過**；**判準本身之偽陰仍在**",
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


# --- R-PMH98（26 包）：矩陣側之母體改為**全枚舉**，關鍵詞降為排序輔助 ---
# **母體 = 事件列之全部有值格（174，21 包 §3 已量）**，非關鍵詞命中之子集。
# 分兩層：機器以**謂詞域**粗篩，**落選者逐格具名其落選理由**（非靜默略過）。
#
# 謂詞域之定義 —— 每一格依其自身之動詞／名詞歸入零至多個域。
PREDICATE_DOMAIN = {
    "audio":   r"\b(mute[sd]?|unmute[sd]?|audio|sounds?|volume)\b",
    "display": r"\b(screen|VP|display(?:ed|s)?|pop-?ups?|shown|show|camera|GUI"
               r"|visibile|visible)\b",
    "power":   r"\b(power|wakes?\s+up|standby|powers?\s+on|remain\s+off"
               r"|turns?\s+off|stays?\s+on)\b",
    "state":   r"\b(event ignored|recall|return|end call|go back|reinstat\w*)\b",
    # 29 包：矩陣 174 格**無一含動畫用詞**（實測 0），故本域之加入
    # **不改變任何既有斷言之落選理由**（已以輸出逐 byte 比對驗證）。
    "animation": r"\b(animations?|outro|splash\s+screens?)\b",
}

# 各斷言之**入選謂詞**（粗篩之判準）。**其仍以詞為之，該限度已具名於 LIMITS。**

# --- 29 包步驟 3（R-PMH107(a)）：`animation` 斷言之規格側逐行記法 ---
# 母體 = 規格全文命中 `animation` 用詞之行（實測 23 行）。**四詞記法，逐行具名。**
# **矩陣側實測 0 格含動畫用詞** —— 174 格全部以「無共同謂詞」記 `未對照`（R-PMH100）。
ANIM_LINE_VERDICT: dict[int, tuple[str, str, str]] = {
    19: ("未對照",
         "素材參照 vs 動畫是否播放／是否同步",
         "**無共同謂詞**（R-PMH79）—— 其述「官方圖形與動畫範例參照 PDO release」，不斷言任何動畫之播放或同步。"),
    39: ("未對照",
         "圖／清單之標籤 vs 動畫是否播放",
         "**無共同謂詞** —— `Vehicle Start Up Animation,` 為圖說／清單項之標籤，**不含謂詞值**。"),
    91: ("未對照",
         "圖／清單之標籤 vs 動畫是否播放",
         "**無共同謂詞** —— `Vehicle Start Up Animation,` 為圖說／清單項之標籤，**不含謂詞值**。"),
    175: ("未對照",
         "圖／清單之標籤 vs 動畫是否播放",
         "**無共同謂詞** —— `Vehicle Start Up Animation,` 為圖說／清單項之標籤，**不含謂詞值**。"),
    224: ("未對照",
         "圖／清單之標籤 vs 動畫是否播放",
         "**無共同謂詞** —— `Vehicle Start Up Animation,` 為圖說／清單項之標籤，**不含謂詞值**。"),
    269: ("未對照",
         "圖／清單之標籤 vs 動畫是否播放",
         "**無共同謂詞** —— `Vehicle Start Up Animation,` 為圖說／清單項之標籤，**不含謂詞值**。"),
    282: ("印證",
         "門關閉 → 啟動動畫是否呈現",
         "**同謂詞同值** —— `SU1.)` 逐字載 `When the vehicle's driver door is closed a startup animation will be presented (3 sec)`，與 `-009` 之「門關閉引發啟動動畫」一致。⚠ 其 `(3 sec)` 為時長，**`-009` 未斷言任何秒數**（§8.4.1 不造值），故該部分不入對照。"),
    283: ("未對照",
         "動畫**之後**之畫面 vs 動畫是否播放／同步",
         "**謂詞不同** —— 其述動畫結束後 screen black／splash screen 之呈現，`-009`／`-010` 未斷言動畫之後之畫面。"),
    295: ("印證",
         "門關閉 → 啟動動畫開始；關機動畫開始",
         "**同謂詞同值** —— `SU4.)` 逐字載 `it shall start upon driver door close` 與 `If shut-down animation is supported, it shall begin playing`，分別印證 `-009` 與 `-010` 之觸發。**其 `conclude by 3 seconds`／`within 10s` 未入對照**（不造值）。"),
    296: ("未對照",
         "關機動畫之**觸發條件** vs `-010` 之「動畫已被觸發」",
         "**謂詞不同** —— 其載關機動畫之開始須 `KEY OFF` 與 `radio UI shut down` 之組合；`-010` 之步驟以 `Trigger the shut-down animation` **抽象該觸發**而不重述其條件（§8.5，其屬 `Startup Animation` 組之 `SU4.)`，已於 `-010` 之 reasoning 具名）。**二者不取相反值** —— 其為同一事之前置條件與其已成立。"),
    297: ("未對照",
         "延遲模式之 outro animation 之例 vs 本批之斷言",
         "**謂詞不同** —— 其為 `SU4.)` 之舉例（先 key off 後 Radio Shut Down），述關機動畫**於何時**被觸發，非其開始後聲音是否同步。"),
    298: ("未對照",
         "門被移除 → 不顯示啟動動畫",
         "**同謂詞相反值，惟條件互斥可證**（R-PMH84）—— 其條件為 `doors are removed/not present`；而 `-009` 之 PC3 為 `The driver door is open` 且其步驟為 `Close the driver door`，**「駕駛門開著並被關上」蘊含該門存在** —— 二條件不可同時成立。故非牴觸。"),
    299: ("牴觸",
         "同一 ignition cycle 內第二次觸發 → 啟動動畫是否播放",
         "**同謂詞相反值，條件互斥未證**（R-PMH84）—— `SU5.)` 逐字載 `If ignition cycle has not changed the animation should only be played once`，即同一 ignition cycle 內第二次門關閉**不再播放動畫**；而 `-009` 之 ER 斷言門關閉後啟動音**與啟動動畫同步**。**`-009` 之 pre_condition 未排除「本 ignition cycle 內動畫已播放過」** —— 該狀態非測試員之動作而是測試前既存之狀態，**不能以「程序不含該動作」排除**。**停止條件 7 觸發，上呈不自行調和（R-PMH79）。**"),
    300: ("牴觸",
         "同一 CAN BUS wake up 內重複門關閉 → 啟動動畫是否播放",
         "**同謂詞相反值，條件互斥未證** —— 逐字 `Animation should only play once per CAN BUS wake up upon closing the driver door.`。**與 L299 同形態而為另一句**（其計次之單位不同：L299 以 ignition cycle，本行以 CAN BUS wake up）—— **二者各自成立，不合併計數**。**停止條件 7 觸發。**"),
    301: ("牴觸",
         "門開著時點火轉 ACC/RUN/START → 啟動動畫是否播放",
         "**同謂詞相反值，條件互斥未證** —— 逐字 `If vehicle ignition is turned to ACC, RUN or START ON with the door open, the animation screen shall be skipped`。`-009` 之 PC3 為 `The driver door is open and the head unit is off`，**未言 ignition 之位置**；門開著時 ignition 已轉 ACC/RUN/START 之情形**未被排除**，而該情形下動畫被跳過，`-009` 之同步斷言即無所附麗。**停止條件 7 觸發。**"),
    302: ("印證",
         "最後狀態為 Radio OFF 時門關閉 → 播放啟動動畫",
         "**同謂詞同值** —— `SU6.)` 逐字載 `If last state is Radio OFF, play startup animation and show applicable splash screens when driver door closed`，與 `-009` 之「門關閉 → 啟動動畫」一致（其 PC3 之 `head unit is off` 落於此情形）。"),
    303: ("未對照",
         "按 Power Button 開機 → 不顯示啟動動畫",
         "**同謂詞相反值，惟條件互斥可證** —— 其條件為 `When Power Button is pressed On`，**該動作為測試員之動作且不在 `-009` 之 procedure 中**（其步驟只有門關閉與讀取）。⚠ **本判與 L299／L301 之差異須具名**：該二者之條件為**測試前既存之狀態**（本 cycle 內是否已播放／ignition 之位置），**不能以「程序不含該動作」排除**；本行之條件為一個動作，可以。"),
    304: ("印證",
         "啟動動畫於各螢幕間之同步",
         "**同謂詞同值** —— `SU7.)` 逐字載 `Start up animation should sync on start up with all capable screen's start up animation`，與 `-009` ER4 之「聲音於各支援螢幕間同步」**同向**（同一次啟動之跨螢幕一致性）。**其為動畫側之同步，聲音側之同步由 `SSND 1)` 承載。**"),
    305: ("未對照",
         "動畫被中斷時之行為 vs 未被中斷時之同步",
         "**謂詞不同** —— 其述 `Animations on all screens should stop … during any interruptions of animation (timeout, ignition button press)`，標的為**中斷情形下動畫如何停**；`-009`／`-010` 未斷言中斷情形。⚠ **中斷情形下聲音是否隨之停止，規格未言，本批亦未驗** —— 登記為限度，不造值。"),
    307: ("未對照",
         "動畫期間之硬鍵按壓之效果 vs 動畫是否播放",
         "**謂詞不同** —— `SU9.)` 述 `Screen Off`／`Power Off` 硬鍵於動畫期間無作用，其標的為按鍵之效果。**該二鍵不在 `-009`／`-010` 之 procedure 中。**"),
    311: ("印證",
         "門關閉 → 啟動音開始且與啟動動畫同步",
         "**同謂詞同值** —— `SSND 1)` 為 `-009` 之 `source_clause` 自身（R-PMH50）。"),
    312: ("印證",
         "告別音於關機動畫開始時同步；跨螢幕同步",
         "**同謂詞同值** —— `SSND 1)` 之後半，為 `-010` 之 `source_clause` 與 `-009` ER4 之依據。"),
    314: ("印證",
         "設定為 Always → 每次啟動動畫播放時皆播放聲音",
         "**同謂詞同值** —— `SSND 2.1)` 逐字載 `should be played everytime the startup animation is played`，與 `-009`／`-010` 之 PC2（設定為 `Always`）一致，**其亦為該 PC2 之來源**（29 §2.3）。"),
}

ASSERTION_DOMAIN = {
    "audio": ("audio", r"\b(mute[sd]?|unmute[sd]?|audio|sounds?|volume|background)\b"),
    "popup": ("display", r"pop\s*-?\s*ups?"),
    "popup_after": ("display", r"pop\s*-?\s*ups?"),
    "announcement": (None, r"\b(traffic\s+announcement|announcements?|received)\b"),
    "animation": ("animation",
                  r"\b(animations?|start-?up\s+animation|shut-?down\s+animation)\b"),
}


def enumerate_matrix(assertion: str) -> tuple[list, list, list]:
    """回傳（全部有值格, 入選格, 落選格及其理由）。"""
    import matrix_vs_chapter as mvc
    wb, ws = mvc.load_sheet()
    cells = [(lo, r, lbl, c, ax, v)
             for lo, r, lbl, cs in mvc.event_rows(ws) for c, ax, v in cs]
    wb.close()
    dom, rx = ASSERTION_DOMAIN[assertion]
    sel_re = re.compile(rx, re.I)
    sel, rej = [], []
    for cell in cells:
        v = cell[5]
        if sel_re.search(v):
            sel.append(cell)
        else:
            doms = sorted(d for d, dr in PREDICATE_DOMAIN.items()
                          if re.search(dr, v, re.I))
            rej.append((cell, doms))
    return cells, sel, rej


def print_enumeration(assertion: str) -> None:
    cells, sel, rej = enumerate_matrix(assertion)
    dom, rx = ASSERTION_DOMAIN[assertion]
    print(f"\n--- 矩陣側之**全枚舉**（R-PMH98）—— 斷言 `{assertion}` ---\n")
    print(f"  母體 = 事件列之**全部有值格 {len(cells)}**（非關鍵詞命中之子集）")
    print(f"  入選（謂詞域 `{dom}`，判準 `{rx}`）= **{len(sel)}** 格，"
          f"分布於 **{len({(a, b) for a, b, *_ in sel})}** 列")
    print(f"  落選 = **{len(rej)}** 格 —— **逐格具名其落選理由**：\n")
    from collections import Counter
    agg = Counter(tuple(d) for _, d in rej)
    for doms, n in agg.most_common():
        why = ("該格無任何謂詞域之詞" if not doms
               else f"該格之謂詞域為 {list(doms)}，與 `{dom}` 不交")
        print(f"    {n:>3} 格  {why}")
    vs = cell_verdicts(assertion)
    from collections import Counter as _C
    kc = _C(k for _, k, _, _ in vs)
    print(f"\n  **R-PMH100：{len(vs)} 格全部入判定表** —— 記法分布 {dict(kc)}")
    n_read = sum(1 for _, _, pr, _ in vs if "而其列未具名記法" in pr)
    print("  **「落選」類別已消滅** —— 關鍵詞自此只決定人讀之先後。")
    if n_read:
        print(f"  ⚠ 其中 **{n_read}** 格記 **`待定義`** —— "
              f"「**入選而列層未具名，判定尚未作成**」（28 包步驟 2(a)）。")
        print(f"     （`{assertion}` 之列層記法存於 `matrix_vs_chapter.VERDICT`"
              f" 之章別判定，非本檔）")
    au = domain_audit(assertion)
    print(f"  分類錯誤之稽核（`AUDIT_CORE`）：**{len(au)}** 格"
          + ("" if not au else f" ← **FAIL** {au[:3]}"))
    # 與關鍵詞篩選之對照（停止條件 8）
    kw = re.compile(ASSERTIONS[assertion][0], re.I)
    kw_cells = [c for c in cells if kw.search(c[5])]
    same_rows = {(a, b) for a, b, *_ in sel} == {(a, b) for a, b, *_ in kw_cells}
    print(f"\n  === 與關鍵詞篩選之對照（26 包停止條件 8）===")
    print(f"    關鍵詞篩選得 **{len(kw_cells)}** 格；全枚舉入選 **{len(sel)}** 格")
    print(f"    **其所在之列是否相同：{same_rows}**")
    if len(kw_cells) != len(sel):
        only_kw = [c for c in kw_cells if c not in sel]
        only_en = [c for c in sel if c not in kw_cells]
        for c in only_kw:
            print(f"    只在關鍵詞側：r{c[1]} c{c[3]} = {c[5][:70]}")
        for c in only_en:
            print(f"    只在全枚舉側：r{c[1]} c{c[3]} = {c[5][:70]}")



# --- R-PMH100（27 包）：**落選即判定** —— 消滅「落選」類別 ---
# 26 包之落選格其輸出已含具名理由（「該格之謂詞域為 `['state']`，與 `audio` 不交」）
# —— **該理由即一個 `未對照` 之判定**（R-PMH79：無共同謂詞），只是不在判定表內。
# 本輪將其入表：**174 格全部有記法**，關鍵詞自此**只決定人讀之先後**。
#
# **偽陰之性質隨之改變**：
#   改造前 —— 某格因用詞未被想到而**不存在於輸出**，**不可檢查**；
#   改造後 —— 某格因**謂詞域分類錯誤**而得 `未對照`，**可構造 must-hit**。
#
# 稽核用之核心關鍵詞（**不含 `background` 等歧義詞**）。
AUDIT_CORE = {
    "audio": r"\b(mute[sd]?|unmute[sd]?|audio|sounds?|volume)\b",
    "popup": r"pop\s*-?\s*ups?",
    "popup_after": r"pop\s*-?\s*ups?",
    "announcement": r"\b(traffic\s+announcement|announcements?)\b",
    "animation": r"\banimations?\b",
}


def cell_key(lo: int, r: int, c: int) -> str:
    return f"r{r}c{c}(blk{lo})"


def cell_verdicts(assertion: str, extra=None) -> list:
    """174 格**全部**之判定：(鍵, 記法, 謂詞, 依據)。**無「落選」類別。**"""
    cells, _, _ = enumerate_matrix(assertion)
    cells = list(cells) + list(extra or [])
    dom, rx = ASSERTION_DOMAIN[assertion]
    sel_re = re.compile(rx, re.I)
    out = []
    for lo, r, lbl, c, ax, v in cells:
        named = AUDIO_CELL_VERDICT.get((lo, r)) if assertion == "audio" else None
        if named and sel_re.search(v):
            kind, pred, why = named
            out.append((cell_key(lo, r, c), kind, pred, f"（列層已具名）{why}"))
        elif sel_re.search(v):
            # 28 包步驟 2(a)（27 §12 第 1 項）：其記法**不是 `未對照`** ——
            # `未對照` 為一個**已作成之判定**，而本格之判定**尚未作成**。
            # 記 `待定義`（R-PMH85 之第四詞），使統計不再把「待判定」算入「已判定」。
            out.append((cell_key(lo, r, c), "待定義",
                        f"本格含 `{assertion}` 之用詞而其列未具名記法",
                        "**入選而列層未具名 —— 判定尚未作成**。"
                        f"`{assertion}` 之列層記法存於 `matrix_vs_chapter.VERDICT` "
                        "之章別判定（如 ch7 之 `r48` 為牴觸），非本檔。**須人讀。**"))
        else:
            doms = sorted(d for d, dr in PREDICATE_DOMAIN.items()
                          if re.search(dr, v, re.I))
            why = ("該格無任何謂詞域之詞" if not doms
                   else f"該格之謂詞域為 {doms}，與 `{dom}` 不交")
            out.append((cell_key(lo, r, c), "未對照",
                        f"該格之謂詞域 vs 斷言 `{assertion}` 之謂詞域",
                        f"**無共同謂詞**（R-PMH79）—— {why}。（謂詞域粗篩，R-PMH100）"))
    return out


def domain_audit(assertion: str, extra=None) -> list:
    """**分類錯誤之稽核** —— 含核心關鍵詞而其謂詞域不含該域者。空清單為 PASS。"""
    cells, _, _ = enumerate_matrix(assertion)
    cells = list(cells) + list(extra or [])
    dom = ASSERTION_DOMAIN[assertion][0]
    core = re.compile(AUDIT_CORE[assertion], re.I)
    bad = []
    for lo, r, lbl, c, ax, v in cells:
        if not core.search(v):
            continue
        doms = {d for d, dr in PREDICATE_DOMAIN.items() if re.search(dr, v, re.I)}
        if dom and dom not in doms:
            bad.append((cell_key(lo, r, c), sorted(doms), v[:70]))
    return bad


def cell_must_hit() -> int:
    """R-PMH100 之 must-hit（27 包步驟 2）。"""
    print("=== R-PMH100 之 must-hit（27 包步驟 2）===")
    print("**改造前之偽陰不可檢查**（某格不存在於輸出）；"
          "**改造後可檢查**（某格分類錯誤而得 `未對照`）。\n")
    base = domain_audit("audio")
    print(f"  基線（現況 174 格）之分類錯誤 = **{len(base)}**")

    saved = PREDICATE_DOMAIN["audio"]
    PREDICATE_DOMAIN["audio"] = r"__never_matches__"
    a_bad = domain_audit("audio")
    PREDICATE_DOMAIN["audio"] = saved
    ok_a = len(a_bad) > len(base)
    print(f"\n  (a) 令 `audio` 之謂詞域失效（模擬分類錯誤）→ 稽核報 "
          f"**{len(a_bad)}** 格分類有誤：{ok_a}")
    for k, d, v in a_bad[:3]:
        print(f"        {k} 域={d} :: {v}")

    stub = [(99, 99, "測試替身", 1, "（替身軸）", "Event ignored")]
    b_bad = domain_audit("audio", stub)
    ok_b = len(b_bad) == len(base)
    print(f"\n  (b) 注入一格 `Event ignored`（確無 audio 用詞）→ "
          f"稽核仍為 **{len(b_bad)}** 格：{ok_b}")

    print("\n" + "=" * 62)
    print(f"(a) 分類錯誤被攔下: {ok_a}；(b) 無用詞者不誤報: {ok_b}；"
          f"現況分類錯誤: {len(base)}")
    return 0 if (ok_a and ok_b and not base) else 1



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


# --- R-PMH98 之規格側（27 包步驟 6）：**只界定母體並量其行數，本輪不做判定** ---
# 排除規則須**具名且逐行可查**。
SPEC_EXCLUDE = [
    ("空行", r"^\s*$"),
    ("純頁碼", r"^\s*\d{1,3}\s*$"),
    ("純標點或單字元", r"^\s*[\W_]\s*$"),
    ("封面／文件資訊（p1）", None),          # 以頁次判，非以字樣
    ("流程圖頁之標籤（p2–p7、p11）", None),  # 同上
]


def spec_population() -> None:
    """R-PMH98 之規格側母體界定與行數（**本輪只量，不判定**）。"""
    import yaml
    cfg = yaml.safe_load((ROOT / "feature.yaml").read_text(encoding="utf-8"))
    d = fitz.open(ROOT / cfg["paths"]["spec_pdf"])
    print("=== 規格側全枚舉之母體界定（R-PMH98，27 包步驟 6）===")
    print("**本輪只界定母體並量其行數，不做判定** —— 規模未知，先量再做。\n")
    tot = kept = 0
    per_page = []
    NARR_PAGES = {8, 9, 10, 11}   # 有 leaf 之章所在之頁（p8–p11）
    for i in range(d.page_count):
        lines = d[i].get_text().splitlines()
        tot += len(lines)
        n_blank = sum(1 for l in lines if not l.strip())
        n_num = sum(1 for l in lines if re.fullmatch(r"\s*\d{1,3}\s*", l))
        n_punct = sum(1 for l in lines if re.fullmatch(r"\s*[\W_]\s*", l))
        body = len(lines) - n_blank - n_num - n_punct
        in_scope = i + 1 in NARR_PAGES
        if in_scope:
            kept += body
        per_page.append((i + 1, len(lines), n_blank, n_num, n_punct, body, in_scope))
    print(f"{'頁':>3} {'總行':>5} {'空行':>5} {'頁碼':>5} {'標點':>5} {'敘述行':>6}  在範圍")
    for pg, n, b, num, pu, body, ins in per_page:
        print(f"{pg:>3} {n:>5} {b:>5} {num:>5} {pu:>5} {body:>6}  "
              f"{'✅' if ins else '—（圖／封面）'}")
    print(f"\n  PDF 全文行數 = **{tot}**")
    print(f"  **母體（p8–p11 之敘述行）= {kept}**")
    print(f"  排除規則（**逐行可查**）：{[n for n, _ in SPEC_EXCLUDE]}")
    print("\n  ⚠ **`p1–p7` 與 `p11` 之圖標籤以頁次排除，非以字樣** ——"
          "\n    其依據為 A-PMH04（2.1–6.1 為圖片佔位）與 12.4（`Please refer to the diagram`）。"
          "\n    **p11 之 `OFF1.)`～`OFF3.)` 在 p11 而 p11 在範圍內** —— 故該頁未被整頁排除。")
    print(f"\n  **每一斷言 × {kept} 行**之人讀規模已知；"
          "其分兩層（謂詞層粗篩 ＋ 落選即判定）之作法同矩陣側（R-PMH100）。")
    d.close()



def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--assertion", choices=sorted(ASSERTIONS), default="popup",
                    help="R-PMH93 —— 掃描之單位為**斷言**")
    ap.add_argument("--cell-must-hit", action="store_true",
                    help="R-PMH100 —— 分類錯誤之 must-hit")
    ap.add_argument("--spec-population", action="store_true",
                    help="R-PMH98 規格側 —— 母體界定與行數（只量不判）")
    a = ap.parse_args()
    if a.spec_population:
        spec_population()
        print_limits()
        sys.exit(0)
    if a.cell_must_hit:
        rc = cell_must_hit()
        print_limits()
        sys.exit(rc)
    rx, desc = ASSERTIONS[a.assertion]
    pat = re.compile(rx, re.I)
    lv = {"popup": LINE_VERDICT, "audio": AUDIO_LINE_VERDICT,
          "announcement": ANN_LINE_VERDICT, "popup_after": AFTER_LINE_VERDICT,
          "animation": ANIM_LINE_VERDICT}[a.assertion]
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
    if a.assertion in ASSERTION_DOMAIN:
        print_enumeration(a.assertion)
    if a.assertion in ("audio", "announcement"):
        print("\n--- 矩陣側之逐列記法（已具名者）---\n")
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
