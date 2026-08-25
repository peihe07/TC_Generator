#!/usr/bin/env python3
"""batch 4 —— `Startup Animation`(9 leaf) ＋ `Splash Screen`(3 leaf)（32 包步驟 5）。

**本批為第一個含兩個 Test Set 之批次**（R-PMH120 之收尾計畫）。

**四項特別拘束**（32 包 §4.2／§4.4）：
  (a) `source_clause` **一律取自 PDF**（R-PMH50；9.1 之反轉不及於章 7），
      且 `-001-01`／`-001-02` 之 `source_clause` **須含 A-PMH03 所查出、
      SYS1 0 命中之子句** `after the animation (3 sec) a splash screen is
      presented timeout (1.5 each).`；
  (b) `-007` 之 marker 照原文抄 **`DS4.1)`**，不得代以 `SU4.1)`（A-PMH11）；
  (c) 每條標其 `test_set`（**兩值**），lint 之讀法隨之一般化；
  (d) 事件層限定依 **R-PMH55(c)** 自 `SU9.1)` 導出（見 `LIMIT_TOKENS_B4`）。

**`tc_id` 續為 provisional**；**零寫回工作簿**。

**R-PMH53 註（本批首次遇到）**：lint 之「交叉引用存在且語意相容」以
**兩條之 `distinguishing_axis` 是否共用詞**為判準。故**跨軸之指涉**
（如「動畫之 3 秒屬另一條之標的」——其軸為「動畫別」而本條之軸為「路徑」）
**必被判為不相容**。本批之三處跨軸指涉因而**以描述指名而不用 tc_id**。
**其代價**：該三處失去機器可追之指標。**該限度於上繳具名。**
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
EP = "等價劃分 (Equivalence Partitioning, EP)"

SA, SS = "Startup Animation", "Splash Screen"

# --- R-PMH50：逐字取自 PDF p8（非 SYS1）---
PDF = {
 "SU1_splash": ("SU1.) When the vehicle's driver door is closed a startup animation will be "
                "presented (3 sec), after the animation (3 sec) a splash screen is presented "
                "timeout (1.5 each)."),
 "SU1_black": "If ignition remains off after animation, screen is black.",
 "SU1_ignon": ("If ignition is turned on during animation, splash screen(s) are presented "
               "(1.5 sec timeout each)."),
 "SU4_start": ("SU4.) If start-up animation is supported, it shall start upon driver door "
               "close, and conclude by 3 seconds."),
 "SU4_shut": ("If shut-down animation is supported, it shall begin playing and conclude "
              "within 10s."),
 "SU4_trig": ("Begin shut down animation only when you have the combination of a KEY OFF and "
              "radio UI shut down."),
 "DS4_1": ("DS4.1) If doors are removed/not present and ignition is turned to ACC, RUN, or "
           "START, do not show Start Up Animation and jump directly to Splash screen."),
 "SU5_once": "SU5.) If ignition cycle has not changed the animation should only be played once.",
 "SU5_skip": ("-- If vehicle ignition is turned to ACC, RUN or START ON with the door open, the "
              "animation screen shall be skipped and start from applicable splash screen."),
 "SU6_radiooff": ("SU6.) If last state is Radio OFF, play startup animation and show applicable "
                  "splash screens when driver door closed then screen remains black."),
 "SU6_power": "When Power Button is pressed On do not show Start Up Animation.",
 "SU7_sync": ("SU7.) Start up animation should sync on start up with all capable screen's start "
              "up animation."),
 "SU7_stop": ("Animations on all screens should stop (refer to logic for specific behavior) "
              "during any interruptions of animation (timeout, ignition button press)."),
 "SU8": "SU8.) Show the splash screen and disclaimer screen once per CAN BUS cycle",
}

# --- 事件層限定（R-PMH55(c)／R-PMH87 形態：**測試員之動作** → procedure）---
# 其來源為 `SU9.)`／`SU9.1)`（他 leaf，且依 R-PMH74 不入 leaf 母體）：
#   SU9.)   Pressing "Screen Off" or "Power Off" hard key will not do anything
#           when pressed during animation.
#   SU9.1)  Pressing Power Off or Screen Off hard keys during the splash screen(s)
#           or disclaimer will reset the timeout …
# **不加此限定，凡斷言 splash 之 1.5 秒逾時者皆可能因逾時被重設而誤判。**
LIMIT_TOKENS_B4 = ["press the Power Off or Screen Off hard key"]
PC_LIMIT = "Do not press the Power Off or Screen Off hard key"

def r55(er_ref: str, why: str) -> str:
    """R-PMH126 —— 限定之依據**逐條**產生，具名該條之**哪一個** ER 斷言。"""
    return ("⚠ **事件層限定一項（R-PMH55(c)／R-PMH126）** —— 其所對之斷言為 "
            f"**{er_ref}**：{why}，而二者之條件**未證互斥**（R-PMH84）。"
            "**其為測試員之動作，故置於 procedure**（canon §4.5；對照 R-PMH113 之"
            "狀態型限定置於 pre_condition）。其來源 `SU9.)`／`SU9.1)` 為**他 leaf** 且依 "
            "R-PMH74 不入 leaf 母體，**故其只出現於步驟之限定子句，不擴入本條之斷言**"
            "（R-PMH55 之三判準）。")


_OLD_R55 = ("⚠ **事件層限定一項（R-PMH55(c)）**：`SU9.1)` 逐字載「於 splash 畫面或免責畫面期間按 "
       "Power Off／Screen Off 硬鍵**會重設逾時**」，與本條之逾時斷言**同謂詞取相反值**，"
       "而二者之條件**未證互斥**（R-PMH84）。**其為測試員之動作，故置於 procedure**"
       "（canon §4.5；對照 R-PMH113 之狀態型限定置於 pre_condition）。"
       "其來源 `SU9.)`／`SU9.1)` 為**他 leaf**且依 R-PMH74 不入 leaf 母體，"
       "**故其只出現於步驟之限定子句，不擴入本條之斷言**（R-PMH55 之三判準）。")

DIAG = ("⚠ **流程圖之未涵蓋項（A-PMH28；34a 之 R-PMH131 已定案）**：p3–p7 之流程圖文字層逐字載 "
        "`If vehicle supports more than 1 Splash screen, toggle them one after another with a "
        "1.5 timeout each`，**`toggle them one after another` 於散文 0 命中**。"
        "**本條不斷言其輪替順序**（§8.4.1 不造值）。"
        "**R-PMH131（34a）已裁：該五類不寫 TC、登記缺口、併入 `DR-PMH8` Q7** —— "
        "**本條之「不斷言」自此為裁定而非暫置**。"
        "⚠ **流程圖之規範性本身仍未決** —— R-PMH131 只裁「不為其撰寫 TC」；"
        "其繫於 `DR-PMH8` Q7，已登記於 `PENDING-ON-DR` 第 12 筆。")

TCS = [
 # ===== Splash Screen（3 leaf → 4 條）=====
 # ⚠ **R-PMH129（34 包）：本條撤除，不寫入交付工作簿。**
 #   `SU1.)` 之「動畫後呈現 splash，1.5 each」一句於 SYS1 匯出 **0 命中**（A-PMH03），
 #   037 因而無對應 outline、**無 leaf**；依 R-PMH55(b) 不得為其撰寫 TC。
 #   **32 包 §4.2(a)（令其 `source_clause` 須含該子句）已撤回。**
 #   **其定義保留於此（R-PMH44 原文不刪），以 `dropped=True` 排除於輸出**，
 #   使其後各條之 tc_id 位次不變（provisional，末次統一指派）。
 dict(dropped=True,
   leaf="SWE1-HMI-PM-001-01", outline="7.1", ts=SS, src="SU1_splash", dm=STATE, pri="P1",
   lim=("ER3 `Each splash screen times out after 1.5 seconds`",
        "`SU9.1)` 逐字載按該硬鍵**會重設 splash 畫面之逾時**，與本 ER 之「1.5 秒逾時」**同謂詞取相反值**"),
   title="Splash screen is presented after the startup animation",
   item="(正常路徑：門關閉 → 動畫 → splash；與 -025 之點火維持關閉路徑成對)",
   pre=["Start-up animation and splash screen are supported on this vehicle",
        "The driver door is open and the ignition is on"],
   proc=["Close the driver door and record the animation start",
         "Read the display and record the splash screen",
         "Check that the splash screen is presented after the animation"],
   er=["The startup animation is presented when the driver door is closed",
       "The splash screen is presented after the animation",
       "Each splash screen times out after 1.5 seconds"],
   reason=("**P1 —— 主要功能邏輯**（非 P0）：splash 未呈現不阻斷開機，其後仍到 last mode。"
     "設計方法 STATE —— 標的為門關閉所引發之畫面序列。"
     "⚠ **`source_clause` 含 A-PMH03 之漏句子句** —— `after the animation (3 sec) a splash "
     "screen is presented timeout (1.5 each).` **於 SYS1 匯出 0 命中**（13 包查出），"
     "**故本批一律取自 PDF**（R-PMH50；R-PMH75 之反轉只及於 9.1）。"
     "⚠ **§8.4.1 不造值：動畫之 `(3 sec)` 本條不斷言** —— 其屬**本批啟動動畫時序條**之標的（`SU4.)`）"
     "——**此處不以 tc_id 指涉**，理由見檔頭之 R-PMH53 註；"
     "本條只斷言其**序**（動畫之後）與 splash 之 `1.5` 逾時。" + DIAG),
   axis="路徑：點火開啟下之正常序列（對 -025 之點火維持關閉）"),

 dict(leaf="SWE1-HMI-PM-001-01", outline="7.1", ts=SS, src="SU1_black", dm=EP, pri="P1",
   title="Screen is black when the ignition remains off after the animation",
   item="(等價類：點火維持關閉 —— 與 -026 之動畫期間點火開啟成對)",
   pre=["Start-up animation is supported on this vehicle",
        "The driver door is open and the ignition is off"],
   proc=["Close the driver door and let the animation finish",
         "Check that the screen is black after the animation"],
   er=["The startup animation finishes with the ignition still off",
       "The screen is black"],
   reason=("**P1 —— 主要功能邏輯**：其失效使車輛於熄火狀態下螢幕不熄，為電池耗損。"
     "**設計方法 EP** —— `ignition remains off` 與 `ignition is turned on during animation` "
     "為同一條件之兩個等價類（依 **R-PMH118**，一條只含一類者其技術仍為 EP）。"
     "⚠ **與 -026 拆分之理由（canon §8.2.2）**：二者之預期結果相反（黑螢幕 vs splash），"
     "**併為一條則「其一失效」之 pass/fail 判定不明確**。"),
   axis="等價類：點火於動畫後維持關閉（對 -026 之動畫期間開啟）"),

 dict(leaf="SWE1-HMI-PM-001-02", outline="7.1", ts=SS, src="SU1_ignon", dm=EP, pri="P1",
   lim=("ER3 `Each splash screen times out after 1.5 seconds`",
        "同 -024 —— `SU9.1)` 之逾時重設與本 ER 之「1.5 秒逾時」**同謂詞取相反值**"),
   title="Splash screens are presented when the ignition is turned on during the animation",
   item="(等價類：點火於動畫期間開啟 —— 與 -025 之維持關閉成對)",
   pre=["Start-up animation and splash screen are supported on this vehicle",
        "The driver door is open and the ignition is off"],
   proc=["Close the driver door and turn the ignition on during the animation",
         "Read the display and record whether the animation continues",
         "Read the display and record each splash screen and its duration",
         "Read the display after the splash screens",
         "Check that the splash screens are presented with a 1.5 second timeout"],
   er=["The ignition is turned on while the animation is playing",
       "The animation is interrupted",
       "The splash screens are presented",
       "The disclaimer screen is displayed after the splash screens",
       "Each splash screen times out after 1.5 seconds"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 EP（同 -025 之依據，R-PMH118）。"
     "⚠ **35 包 §3（R-PMH133）之修正**：本 leaf 之 DESC 逐字為 `If ignition is turned ON "
     "during the startup animation, the system **interrupts the animation** and plays splash "
     "screens (1.5 sec each), **then proceeds to Disclaimer**.` —— **二項原未斷言，今補為 ER2／ER4**。"
     "⚠ **`splash screen(s)` 之括號複數本條照抄而不判讀其數** —— "
     "ER3 斷言「各 splash 皆呈現」而不斷言其張數。" + DIAG),
   axis="等價類：點火於動畫期間開啟（對 -025 之維持關閉）"),

 dict(leaf="SWE1-HMI-PM-011", outline="7.9", ts=SS, src="SU8", dm=STATE, pri="P1",
   lim=("ER3 `Neither the splash screen nor the disclaimer screen is shown again`",
        "`SU9.1)` 之**後半句**逐字為 `the radio shall display the screen the next time the screen turns on` —— **其令該畫面再次顯示**，與本 ER 之「不再顯示」**同謂詞取相反值**。⚠ **本條之依據為 `SU9.1)` 之後半句，非其逾時前半句**"),
   title="Splash and disclaimer screens are shown once per CAN BUS cycle",
   item="(每 CAN BUS cycle 各一次 —— 其計次單位為 CAN BUS cycle，非點火週期)",
   pre=["Splash screen and disclaimer screen are supported on this vehicle",
        "The CAN BUS has just woken up and neither screen has been shown yet"],
   proc=["Close the driver door and record the screens shown",
         "Reopen and close the driver door in the same CAN BUS cycle",
         "Check that neither screen is shown a second time"],
   er=["The splash screen and the disclaimer screen are shown once",
       "The second door closure occurs within the same CAN BUS cycle",
       "Neither the splash screen nor the disclaimer screen is shown again"],
   reason=("**P1 —— 主要功能邏輯**：其失效使畫面重複出現，干擾使用者。設計方法 STATE。"
     "⚠ **計次單位為 `CAN BUS cycle`，與**本批動畫計次條**所用之 `ignition cycle`／`CAN BUS wake up` 不同（**不以 tc_id 指涉**，見 R-PMH53 註）** —— "
     "**規格未言三者之關係**，本條照原文用 `CAN BUS cycle` 而不換算（§8.4.1 不造值）。"
     "⚠ **本條之標的含免責畫面而其 leaf 屬 `Splash Screen` 組** —— "
     "`SU8.)` 一句同時管二者，**其歸組依 R-PMH36 之 Layer 2 定版，本條不改**。"),
   axis="計次單位：CAN BUS cycle（對 -032 之 ignition cycle）"),

 # ===== Startup Animation（9 leaf → 10 條）=====
 dict(leaf="SWE1-HMI-PM-006-01", outline="7.5", ts=SA, src="SU4_start", dm=STATE, pri="P1",
   title="Start-up animation starts on driver door close and concludes by three seconds",
   item="(啟動動畫之時序 —— 與 -029 之關機動畫時序成對)",
   pre=["Start-up animation is supported on this vehicle",
        "The driver door is open"],
   proc=["Close the driver door and record the animation start time",
         "Record the animation end time",
         "Check that the animation concluded within three seconds"],
   er=["The start-up animation starts when the driver door is closed",
       "The animation end time is recorded",
       "The animation concludes by three seconds"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE —— 標的為門關閉所引發之轉換及其時限。"
     "⚠ **`conclude by 3 seconds` 為權威文本所給之值，得斷言**（非造值）。"),
   axis="動畫別：啟動動畫之時序（對 -029 之關機動畫）"),

 dict(leaf="SWE1-HMI-PM-006-02", outline="7.5", ts=SA, src="SU4_shut", dm=STATE, pri="P1",
   title="Shut-down animation begins playing and concludes within ten seconds",
   item="(關機動畫之時序 —— 與 -028 之啟動動畫時序成對)",
   pre=["Shut-down animation is supported on this vehicle",
        "The head unit is on"],
   proc=["Trigger the shut-down animation and record its start time",
         "Record the animation end time",
         "Check that the animation concluded within ten seconds"],
   er=["The shut-down animation begins playing",
       "The animation end time is recorded",
       "The animation concludes within ten seconds"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE。"
     "⚠ **關機動畫之觸發條件不在本條射程** —— 其由**本批之關機動畫觸發組合條**承載（`SU4.)` 之第三句；**不以 tc_id 指涉**，見 R-PMH53 註）；"
     "本條之步驟 2 只說 `Trigger the shut-down animation`（§8.5，不重述他條之條件）。"
     "⚠ **本條與 batch 2 之告別音條（告別音與關機動畫同步）不同謂詞** —— "
     "該條驗聲音之同步，本條驗動畫自身之時長。"),
   axis="動畫別：關機動畫之時序（對 -028 之啟動動畫）"),

 dict(leaf="SWE1-HMI-PM-006-03", outline="7.5", ts=SA, src="SU4_trig", dm=FUNC, pri="P1",
   title="Shut-down animation begins only on key off combined with radio UI shut down",
   item="(關機動畫之觸發組合 —— 與 -028／-029 之時序為不同謂詞)",
   pre=["Shut-down animation is supported on this vehicle",
        "The ignition is on and the radio UI is running"],
   proc=["Turn the key off without shutting the radio UI down",
         "Shut the radio UI down and read the display",
         "Check that the animation began only after both had occurred"],
   er=["The shut-down animation does not begin on key off alone",
       "The shut-down animation begins after the radio UI shuts down",
       "The animation began only once both conditions had occurred"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 FUNC —— 標的為一個具名之條件組合，"
     "**其輸入未被劃分為等價類**（權威文本只給該組合成立之一側），故非 EP（R-PMH118 之界線）。"
     "⚠ **`even not simulteneously` 之處置** —— 權威文本逐字含該拼字（原文如此），"
     "其舉例為 `First key off, later Radio Shut Down (delayed mode): show outro animation`；"
     "**本條之步驟 2／3 即依該例之順序**，故其為順序之一例而非全部順序之窮舉。"
     "⚠ **反向順序（先關 radio UI 後 key off）本條未驗** —— 規格以 `even not simulteneously` "
     "涵蓋之而未舉其例，**據實記載為限度**。"),
   axis="謂詞：關機動畫之觸發組合（對 -028／-029 之時序）"),

 dict(leaf="SWE1-HMI-PM-007", outline="7.5.1", ts=SA, src="DS4_1", dm=EP, pri="P1",
   title="No start-up animation is shown when the doors are removed",
   item="(門不存在之等價類 —— 其 marker 於原文為 DS4.1) 而非 SU4.1)，照原文抄)",
   pre=["Start-up animation and splash screen are supported on this vehicle",
        "The doors are removed or not present"],
   proc=["Turn the ignition to ACC, RUN or START and read the display",
         "Check that the display went directly to the splash screen"],
   er=["No start-up animation is shown",
       "The display goes directly to the splash screen"],
   reason=("**P1 —— 主要功能邏輯**：其失效使無門車輛卡在動畫。"
     "**設計方法 EP** —— `doors removed/not present` 為門之狀態之一個等價類"
     "（**其對立類（門存在且正常關閉）本批無專條** —— 各動畫條皆以門正常關閉為前提而不驗其為一個等價類；**該不對稱據實記載**）。"
     "⚠ **marker 之前綴照原文抄 `DS4.1)`** —— 其父項為 `SU4.)`（7.5）而前綴由 `SU` 變 `DS`，"
     "**極可能為規格原文之筆誤**（A-PMH11，依 R-PMH26 只登記不開 DR）；"
     "**canon §4.3.1 要求逐字，故不得代以 `SU4.1)`**。"
     "⚠ **`ACC, RUN, or START` 三值本條以一條涵蓋** —— 其為同一等價類之三個成員"
     "（權威文本以 `or` 並列而給同一結果），非三個獨立分支，故不依 §8.2.2 拆分。"),
   axis="等價類：門被移除／不存在（其對立類無專條，見 reasoning）"),

 dict(leaf="SWE1-HMI-PM-008-01", outline="7.6", ts=SA, src="SU5_once", dm=STATE, pri="P1",
   title="Animation is played only once while the ignition cycle has not changed",
   item="(計次：ignition cycle 與 CAN BUS wake up —— 與 -033 之跳過路徑成對)",
   pre=["Start-up animation is supported on this vehicle",
        "The ignition cycle has not changed since the animation was last played",
        "The animation has already been played once in this CAN BUS wake-up"],
   proc=["Reopen and close the driver door in the same CAN BUS wake-up",
         "Check that the animation is not played a second time"],
   er=["The driver door is closed again in the same CAN BUS wake-up",
       "The animation is not played a second time"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE。"
     "⚠ **35 包 §4（R-PMH134 之維度三：單位）之修正** —— 本 leaf 之 DESC 逐字為 "
     "`If the ignition cycle has not changed, the system shall play the animation only once "
     "**per CAN BUS wake-up** upon closing the driver door.` —— "
     "**其計次單位為 `CAN BUS wake-up`，而 `ignition cycle` 是其前提**。"
     "本條原以 `ignition cycle` 為計次基準，**今改依 DESC**：`ignition cycle` 降為 pre_condition 2，"
     "計次基準為 pre_condition 3 與 ER1 之 `CAN BUS wake-up`。"
     "**二者之關係規格仍未言，本條不斷言其等價**（§8.4.1）。"
     "⚠ **本行（L299／L300）於 29 包曾對 batch 2 之啟動音條判為牴觸** —— "
     "**對本批而言其為來源** —— 同一行對不同斷言得有不同記法（R-PMH93）。"),
   axis="路徑：同週期內重複觸發（對 -033 之點火轉 ACC/RUN/START）"),

 dict(leaf="SWE1-HMI-PM-008-02", outline="7.6", ts=SA, src="SU5_skip", dm=EP, pri="P1",
   title="Animation is skipped when the ignition is turned on with the door open",
   item="(等價類：門開著時點火轉 ACC/RUN/START —— 與 -032 之同週期重複成對)",
   pre=["Start-up animation and splash screen are supported on this vehicle",
        "The driver door is open"],
   proc=["Turn the ignition to ACC, RUN or START with the door open",
         "Check that the display starts from the applicable splash screen"],
   er=["The animation screen is skipped",
       "The display starts from the applicable splash screen"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 EP（門開／門關為同一條件之兩類，R-PMH118）。"
     "⚠ **`applicable splash screen` 之 `applicable` 本條不判讀** —— "
     "規格未言其判準（哪一張為 applicable），ER3 照原文用該詞而不指定張數（§8.4.1）。" + DIAG),
   axis="等價類：門開著時點火開啟（對 -032 之同週期重複門關閉）"),

 dict(leaf="SWE1-HMI-PM-009-01", outline="7.7", ts=SA, src="SU6_radiooff", dm=STATE, pri="P1",
   title="Animation and splash play with the screen black when the last state is Radio OFF",
   item="(最後狀態為 Radio OFF 之路徑 —— 與 -035 之電源鍵開機路徑成對)",
   pre=["Start-up animation and splash screen are supported on this vehicle",
        "The last state of the radio is OFF and the driver door is open"],
   proc=["Close the driver door and record the animation and splash screens",
         "Check that the screen remains black afterwards"],
   er=["The startup animation plays and the applicable splash screens are shown",
       "The screen remains black"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE。"
     "⚠ **本條之三個後果（播動畫／顯示 splash／螢幕維持黑）為同一觸發之必然序列**，"
     "依 canon §5.7 不拆（對照 §8.2.2 之 bundling —— 該條所禁者為**獨立分支**，"
     "**本處為同一分支之連續後果**，二者不同）。" + DIAG),
   axis="路徑：最後狀態為 Radio OFF（對 -035 之按電源鍵開機）"),

 dict(leaf="SWE1-HMI-PM-009-02", outline="7.7", ts=SA, src="SU6_power", dm=EP, pri="P1",
   title="No start-up animation is shown when the power button is pressed on",
   item="(等價類：按電源鍵開機 —— 與 -034 之門關閉路徑成對)",
   pre=["Start-up animation is supported on this vehicle",
        "The head unit is off"],
   proc=["Press the power button to turn the head unit on",
         "Check that no start-up animation is shown"],
   er=["The head unit turns on",
       "No start-up animation is shown"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 EP —— 開機來源之兩個等價類"
     "（門關閉 vs 電源鍵），其預期結果相反。"
     "⚠ **本條之限定與其動作看似衝突，實不衝突** —— 步驟 1 禁的是 **Power Off／Screen Off** "
     "硬鍵，步驟 2 按的是**電源鍵之 On**；`SU9.1)` 之標的為前者。**該區別於此具名。**"),
   axis="等價類：按電源鍵開機（對 -034 之門關閉）"),

 dict(leaf="SWE1-HMI-PM-010", outline="7.8", ts=SA, src="SU7_sync", dm=STATE, pri="P1",
   title="Start-up animation syncs across all capable screens",
   item="(跨螢幕同步 —— 與 -037 之中斷時停止為不同觸發)",
   pre=["Start-up animation is supported on more than one screen in this vehicle",
        "The driver door is open"],
   proc=["Close the driver door and record each screen's animation start",
         "Check that the animations started in sync with each other"],
   er=["The start-up animation starts on every capable screen",
       "The animations on all capable screens are in sync on start up"],
   reason=("**P1 —— 主要功能邏輯**。設計方法 STATE。"
     "⚠ **§8.4.1 不造值：規格未給任何允差** —— `sync` 無秒數，故 ER3 只斷言「同步」。"
     "⚠ **與 batch 2 之啟動音條（聲音之跨螢幕同步）不同謂詞** —— 該條驗聲音，本條驗動畫。"),
   axis="觸發：開機時之跨螢幕同步（對 -037 之中斷）"),

 dict(leaf="SWE1-HMI-PM-010", outline="7.8", ts=SA, src="SU7_stop", dm=STATE, pri="P1",
   title="Animations on all screens stop when the animation is interrupted",
   item="(中斷時之停止 —— 與 -036 之開機同步為不同觸發；同 leaf 之第二條，profile §4)",
   pre=["Start-up animation is supported on more than one screen in this vehicle",
        "The start-up animation is playing on every capable screen"],
   proc=["Interrupt the animation with an ignition button press",
         "Check that the animations stopped on all screens"],
   er=["The animation is interrupted by the ignition button press",
       "The animations on all screens stop"],
   reason=("**P1 —— 主要功能邏輯**。**同 leaf 之第二條**（profile §4：中斷為另一觸發）。"
     "⚠ **與 -036 拆分之理由（canon §8.2.2）** —— 開機同步與中斷停止為**兩個獨立分支**，"
     "併為一條則其一失效時 pass/fail 不明確。"
     "⚠ **`(refer to logic for specific behavior)` 本條不驗** —— "
     "**該 `logic` 未指明為何份文件**（32 包步驟 3 記 L305 為 `待定義`），"
     "故本條只斷言其**停止**，不斷言停止後之行為（§8.4.1 不造值）。"
     "⚠ **`timeout` 之中斷本條未驗** —— 權威文本舉二例（`timeout, ignition button press`），"
     "本條取後者；**前者未驗，據實記載為限度**。"),
   axis="觸發：動畫被中斷（對 -036 之開機同步）"),
]

BASE = 23        # batch 1–3 用 001–023，本批續 024 起（R-PMH16）


def norm_item(s: str) -> str:
    """canon §11 之正規化 —— **只用於 `test_item`，不用於 `source_clause`**（A-PMH26）。"""
    s = s.replace("‘", "'").replace("’", "'")
    s = re.sub(r"\s*\[CR\d+\]", "", s)
    return re.sub(r"  +", " ", s)


def main() -> None:
    out = []
    for n, t in enumerate(TCS, BASE + 1):
        # R-PMH129：撤除之條**不入輸出而其位次保留** —— tc_id 不重編。
        if t.get("dropped"):
            continue
        # R-PMH126：限定**逐條導出**。有 `lim` 者方插入其步驟與 ER，
        # **編號由此處產生** —— 使增刪一項不必手動重編十四條。
        proc, er = list(t["proc"]), list(t["er"])
        if t.get("lim"):
            proc.insert(0, PC_LIMIT)
            er.insert(0, "No Power Off or Screen Off hard key press occurs")
        proc = [f"{i}. {x}" for i, x in enumerate(proc, 1)]
        er = [f"{i}. {x}" for i, x in enumerate(er, 1)]
        out.append({
            "tc_id": f"NR1L-DisclaimerScreen-{n:03d}",
            "leaf_id": t["leaf"],
            "test_group": "Disclaimer screen",
            "test_set": t["ts"],
            "tc_title": t["title"],
            "test_item": norm_item(f"{PDF[t['src']]}\n\n{t['item']}"),
            "pre_conditions": "\n".join(f"{i}. {x}" for i, x in enumerate(t["pre"], 1)),
            # 33 包 §2.3：canon §4.5 逐字為 `set Input Test Data to NA`；
            # 前三批皆 `NA`，本批原為 `N/A` —— 四批一致化。
            "input_test_data": "NA",
            "test_procedure": "\n".join(proc),
            "expected_result": "\n".join(er),
            "specification_reference": f"{SPEC}_{t['outline']}",
            "design_method": t["dm"],
            "priority": t["pri"],
            "functional_safety": "NA",
            "estimated_test_time": "",
            "vehicle_models": "",
            "remarks": f"Test Set: {t['ts']}",
            "reasoning": t["reason"] + (r55(*t["lim"]) if t.get("lim") else ""),
            "distinguishing_axis": t["axis"],
            "source_clause": PDF[t["src"]],
            "source_clause_origin": "spec_pdf p8",
        })
    doc = {
        "batch": "batch04",
        "feature": "power_moding",
        "test_group": "Disclaimer screen",
        # **本批為兩個 Test Set** —— lint 之讀法隨之一般化（32 §4.4(c)）
        "test_sets": sorted({t["ts"] for t in TCS if not t.get("dropped")}),
        "handoff": "docs/handoff/32_batch4.md",
        "profile": "docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md",
        "selection": ("Test Set `Startup Animation`(9 leaf) ＋ `Splash Screen`(3 leaf)，"
                      "共 **12 leaf**（R-PMH120 之收尾計畫第一批）。**14 條 TC** —— "
                      "`-001-01` 拆 2（點火開啟／維持關閉）、`-010` 拆 2（開機同步／中斷停止），"
                      "皆依 profile §4 與 canon §8.2.2。"),
        "tc_id_status": "provisional",
        "leaf_scope": sorted({t["leaf"] for t in TCS if not t.get("dropped")}),
        "source_clause_basis": ("R-PMH50 —— **一律取自 spec_pdf p8**（R-PMH75 之反轉只及於 9.1）。"
                                "`-024`／`-026` 之 `source_clause` **含 A-PMH03 所查出、"
                                "SYS1 0 命中之子句**。"),
        "write_back": "凍結 —— 本批只產出 JSON，不寫回工作簿",
        # R-PMH126：**十四筆減為實際導出者** —— 無 `lim` 者不入。
        "limits": {f"NR1L-DisclaimerScreen-{BASE + 1 + i:03d}": LIMIT_TOKENS_B4
                   for i, x in enumerate(TCS)
                   if x.get("lim") and not x.get("dropped")},
        "tcs": out,
    }
    p = ROOT / "generated" / "batch04.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {p} — {len(out)} TC（自 {len(doc['leaf_scope'])} leaf，"
          f"{len(doc['test_sets'])} 個 Test Set）")


if __name__ == "__main__":
    main()
