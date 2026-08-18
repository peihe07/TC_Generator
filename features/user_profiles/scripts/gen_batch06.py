#!/usr/bin/env python3
"""第六批之生成器（41 包）—— ch7 Welcome Flow ＋ ch8 Setup Flow，tc_id 157–189。

## 批界

**第六批 ＝ ch7 之 `PRWEL` 10 leaf ＋ ch8 之 `NEWPR` 23 leaf ＝ 33 leaf。**
本批完成後，037 之 **180 leaf 全覆蓋**。

## 撰寫順序（41 包 §五之要求）

**ch8 沿用「同節多 leaf 併寫」之順序** —— 8.4（`069-01`／`069-02`）、
8.7（`073-02`／`073-03`）、8.8（`076-01`／`-02`／`-03`）三處各自一次寫完。
該順序逼人把該節逐字讀完；RD #8 即由此在第五批之生成當下被發現。

**本批由該順序得到的三件事**（皆記於各該 remarks）：
1. 8.4 之 `069-01`（過濾已用）與 `069-02`（自動 highlight）**共用一個畫面**，
   而 8.8.1（`077`）之「使用中者不顯示」**與 `069-01` 是同一句話的兩處出現** ——
   故 `077` 只驗數目，隱藏一側具名委派
2. 8.7 之兩個 leaf 是**同一個上限之兩端**（下界 1 字元、上界 12 字元含空格），
   兩者皆為 BVA，而其**界前值不同**
3. 8.8 之 `076-02`／`076-03` 為**同一句所切之兩個螢幕尺寸**，
   互為 §7 之列舉配對，非變體覆寫（後者見 `audit_variant_pairs` 之判準）

## 條數：**33 條，額外造者 0**

無 §7 之另立配對：本批之列舉（8.8 之兩個尺寸、8.7 之兩端）
皆已由 037 切成獨立 leaf，**不需我方再造**。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
from gen_pilot import (steps, FUNCTIONAL, STATE, BVA,  # noqa: E402
                       NEGATIVE, SCENARIO)
from gen_batch01 import _rec                           # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"
TC_START = 157

SAMPLE = [
    # ── ch7 / PRWEL
    "SWE1-HMI-PROF-056", "SWE1-HMI-PROF-057", "SWE1-HMI-PROF-058",
    "SWE1-HMI-PROF-060", "SWE1-HMI-PROF-061",
    "SWE1-HMI-PROF-062-01", "SWE1-HMI-PROF-062-03", "SWE1-HMI-PROF-062-04",
    "SWE1-HMI-PROF-063", "SWE1-HMI-PROF-064",
    # ── ch8 / NEWPR
    "SWE1-HMI-PROF-065", "SWE1-HMI-PROF-066", "SWE1-HMI-PROF-067",
    "SWE1-HMI-PROF-068",
    "SWE1-HMI-PROF-069-01", "SWE1-HMI-PROF-069-02",
    "SWE1-HMI-PROF-071", "SWE1-HMI-PROF-072",
    "SWE1-HMI-PROF-073-02", "SWE1-HMI-PROF-073-03",
    "SWE1-HMI-PROF-074", "SWE1-HMI-PROF-075",
    "SWE1-HMI-PROF-076-01", "SWE1-HMI-PROF-076-02", "SWE1-HMI-PROF-076-03",
    "SWE1-HMI-PROF-077", "SWE1-HMI-PROF-078", "SWE1-HMI-PROF-079",
    "SWE1-HMI-PROF-080", "SWE1-HMI-PROF-081", "SWE1-HMI-PROF-082",
    "SWE1-HMI-PROF-083", "SWE1-HMI-PROF-084",
]

PRIORITY = {
    "SWE1-HMI-PROF-056": ("P1", "welcome popup 之兩個觸發；ch7 之入口條文"),
    "SWE1-HMI-PROF-057": ("P2", "未完成 Tutorials 時之 PU0841 與其 X 之後續"),
    "SWE1-HMI-PROF-058": ("P2", "小版 welcome popup 之內容與兩個選項"),
    "SWE1-HMI-PROF-060": ("P3", "自訂 popup 關閉時不再詢問；罕見分支"),
    "SWE1-HMI-PROF-061": ("P2", "welcome popup 之兩個導向入口"),
    "SWE1-HMI-PROF-062-01": ("P0", "行車中 welcome popup 須自動清除 —— "
                                   "**遮蔽駕駛視野之防線本身**（§10.2 safety）"),
    "SWE1-HMI-PROF-062-03": ("P2", "使用者互動時之立即清除"),
    "SWE1-HMI-PROF-062-04": ("P2", "清除後於本 session 內不再返回"),
    "SWE1-HMI-PROF-063": ("P3", "遙控起動期間不計入 30 秒；計時之排除條件"),
    "SWE1-HMI-PROF-064": ("P2", "Valet Mode welcome popup 之清除行為同型"),
    "SWE1-HMI-PROF-065": ("P1", "R1 High 之流程分歧 —— 誤啟 CPA 即為錯誤變體行為"),
    "SWE1-HMI-PROF-066": ("P1", "New Profile Setup 之起始；ch8 之入口"),
    "SWE1-HMI-PROF-067": ("P2", "設定流程以 popup 串接之形態"),
    "SWE1-HMI-PROF-068": ("P2", "設定中按他鍵視同取消並詢問；避免誤丟輸入"),
    "SWE1-HMI-PROF-069-01": ("P1", "avatar 不得重複 —— 清單須濾掉已用者"),
    "SWE1-HMI-PROF-069-02": ("P2", "預設 avatar 之自動 highlight"),
    "SWE1-HMI-PROF-071": ("P3", "同名 username 之允許；罕用但明文"),
    "SWE1-HMI-PROF-072": ("P2", "連網車輛之第一步兩個選項"),
    "SWE1-HMI-PROF-073-02": ("P1", "username 下界 1 字元；Next 之啟用條件"),
    "SWE1-HMI-PROF-073-03": ("P2", "空格計入 12 字元上限"),
    "SWE1-HMI-PROF-074": ("P2", "username 步驟之三個選項與其去向"),
    "SWE1-HMI-PROF-075": ("P1", "特殊字元不得輸入 —— **輸入驗證之防線本身**"),
    "SWE1-HMI-PROF-076-01": ("P3", "highlight 隨選取移動；呈現層"),
    "SWE1-HMI-PROF-076-02": ("P2", "8.4 吋以上之 avatar 位置與按鈕字樣"),
    "SWE1-HMI-PROF-076-03": ("P2", "7 吋之 avatar 位置與按鈕字樣"),
    "SWE1-HMI-PROF-077": ("P1", "初始 avatar 數目下界；選擇池之充足性"),
    "SWE1-HMI-PROF-078": ("P2", "avatar 之分類數與分類按鈕之作用"),
    "SWE1-HMI-PROF-079": ("P1", "最終步之偏好選擇與沿用；新 profile 之初始狀態"),
    "SWE1-HMI-PROF-080": ("P1", "設定完成後之去向與新 profile 之啟用"),
    "SWE1-HMI-PROF-081": ("P2", "自 Edit Profile 起始之編輯，其返回頁"),
    "SWE1-HMI-PROF-082": ("P1", "狀態列圖示隨新現用 profile 更新"),
    "SWE1-HMI-PROF-083": ("P2", "只改 username 或 avatar 時之單一 popup"),
    "SWE1-HMI-PROF-084": ("P2", "返回鍵之上一步與選擇之保留"),
}

REF_EXTRA = {}

TCS = {

    # ══════════════════ ch7 / PRWEL ══════════════════════════════════

    "SWE1-HMI-PROF-056": dict(
        title="Welcome popup shown at ignition on and on activation",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "The Welcome popup setting is on for both Profiles",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Switch the ignition on and read the screen",
                   "Activate Driver Profile B and read the screen"),
        er=steps("A welcome popup is displayed at ignition on",
                 "A welcome popup is displayed for Driver Profile B"),
        remarks="**條文列兩個觸發**（`at ignition on` 與 `any time a Profile "
                "is activated`），依 §7 兩者皆須走到 —— 故本條兩步。"
                "`Unless user has selected to turn off welcome popups` 為"
                "適用條件（§8.7.3），以 pre-condition 固定為開啟；"
                "**關閉後不再顯示一側由 `SWE1-HMI-PROF-051`（6.3.2）承擔**。"
                "**X-1**：步驟 2 之切換所觸發者（5.3.1 之 PU0580）"
                "**即 ER2 所斷言者** —— 標的而非干擾。",
        reasoning=(
            "驗證目標：7.1（PRWEL1）—— 除非使用者關閉，welcome popup 於"
            "電門開啟時與任何 profile 被啟用時顯示。"
            "關鍵情境條件：兩個 profile 之設定皆為開啟，"
            "否則第二個觸發無從觀察。"
            "為什麼這樣切：本 leaf 之單位為**顯示之觸發**；"
            "popup 之內容屬 7.2／7.2.1，其清除屬 7.4。"),
        kw=["welcome popup", "ignition on", "activated", "PRWEL1"],
    ),

    "SWE1-HMI-PROF-057": dict(
        title="PU0841 shown when Tutorials are not complete",
        design=FUNCTIONAL,
        pre=steps("The active Driver Profile has not completed the Tutorials",
                  "The active Driver Profile has not chosen to exit the "
                  "Tutorials",
                  "The Welcome popup setting is on for that Profile",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Switch the ignition on and read the popup shown",
                   "Press X on the popup and read the popup shown"),
        er=steps("Welcome popup PU0841 is displayed",
                 "Popup PU0611 is displayed, offering to remind me later or "
                 "not show again"),
        remarks="**兩個 pre-condition 是條文之兩個合取條件** —— "
                "`has not completed` 與 `has not chosen to exit`；"
                "少任一個，PU0841 之適用條件即不成立，而本條會測到別的 popup。"
                "PU0841／PU0611 之**內文不寫**（R-U27 同型）：spec 只給 id 與"
                "其選項名稱，未給文字。",
        reasoning=(
            "驗證目標：7.1.1（PRWEL1.1）—— 未完成 Tutorials 之 profile 顯示 "
            "PU0841；按 X 則顯示 PU0611。"
            "關鍵情境條件：Tutorials 未完成**且**未選擇退出。"
            "為什麼這樣切：兩個 popup 為**同一條路徑之前後兩步**，"
            "依 §5.7 併為一條之兩個 ER 行；"
            "PU0611 之兩個選項之後果分屬 6.3.1／6.3.2，本條只驗其被提供。"),
        kw=["PU0841", "PU0611", "Tutorials", "welcome popup"],
    ),

    "SWE1-HMI-PROF-058": dict(
        title="Small welcome popup shows username, avatar and options",
        design=FUNCTIONAL,
        pre=steps("The active Driver Profile has a username and an avatar",
                  "The small welcome popup version applies to this vehicle",
                  "The Welcome popup setting is on for that Profile",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Switch the ignition on and read the popup shown",
                   "Read the popup and check the username, the avatar and "
                   "the options"),
        er=steps("The small welcome popup is displayed",
                 "The active Profile's username and avatar are shown with "
                 "options to switch users or close the popup"),
        remarks="**「小版」與「大版」之選用條件條文未載** —— 7.2 與 7.2.1 各自"
                "描述其內容，未說何時用哪一個。依 §8.4.1 不推定，"
                "以 pre-condition 具名為本車適用小版，**該條件本身不由本條驗**。"
                "大版之內容屬 `SWE1-HMI-PROF-059-01`（`NR1L-UserProfiles-007`）。"
                "兩個選項**按下之後**之行為屬 7.3（`SWE1-HMI-PROF-061`）。",
        reasoning=(
            "驗證目標：7.2（PRWEL2）—— 小版 welcome popup 顯示現用 profile 之"
            "username 與 avatar，並提供切換使用者與關閉兩個選項。"
            "關鍵情境條件：該 profile 須有 username 與 avatar，"
            "否則「顯示了什麼」不可觀察。"
            "為什麼這樣切：四項內容為**同一畫面之並列斷言**，§5.7 併驗。"),
        kw=["small welcome popup", "username", "avatar", "switch users"],
    ),

    "SWE1-HMI-PROF-060": dict(
        title="Closing a custom welcome popup acts as Remind me Later",
        design=STATE,
        pre=steps("Two Driver Profiles exist and Driver Profile A is "
                  "customized",
                  "The custom welcome popup of Driver Profile A is displayed",
                  "The Welcome popup setting is on for both Profiles",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press X on the custom welcome popup",
                   "Read the screen and check which popups are displayed",
                   "Activate Driver Profile B, then activate Driver Profile "
                   "A again",
                   "Read the screen and check whether the popup is displayed"),
        er=steps("The custom welcome popup is closed",
                 "No popup offering Remind me Later or Don’t Show me Again "
                 "is displayed",
                 "Driver Profile A is active again",
                 "The custom welcome popup of Driver Profile A is displayed "
                 "again"),
        remarks="**ER4 是「視同 Remind me Later」之唯一可觀察形式** —— "
                "6.3.1 定 Remind me Later 為「關到該 profile 下次被啟用」；"
                "只驗 ER1／ER2（關了、沒問），一個**永久關閉**之實作會通過"
                "（§8.3）。故步驟 3 切走再切回。"
                "**與 `SWE1-HMI-PROF-051`（Don’t Show me Again）之結果相反** ——"
                "那一條之同位置斷言為「不再顯示」。"
                "**X-1**：步驟 3 之切換會觸發 5.3.1 之 PU0580，而該 popup **即 ER3／ER4 所涉者** —— 標的而非干擾。",
        reasoning=(
            "驗證目標：7.2.2（PRWEL2.2）—— 自訂 welcome popup 之關閉不出現"
            "Remind me Later／Don’t Show me Again 之詢問，且按 X 視同前者。"
            "關鍵情境條件：popup 須為**自訂** profile 之 popup ——"
            "預設 profile 之 popup 行為在 6.3.1，兩者相反。"
            "為什麼這樣切：`design_method` 取狀態轉換 ——"
            "本條驗的是一個**壓抑狀態之建立與其於再啟用時之解除**。"),
        kw=["custom welcome popup", "Remind me Later", "close", "X"],
    ),

    "SWE1-HMI-PROF-061": dict(
        title="Welcome popup links to All Profiles or the last known tab",
        design=FUNCTIONAL,
        pre=steps("The welcome popup of the active Profile is displayed",
                  "The last known tab of the active Profile is the “Edit "
                  "Profile” tab",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press “Switch Users” on the welcome popup",
                   "Read the screen and check which tab is shown",
                   "Return to the welcome popup and press the “Welcome "
                   "[username]” text",
                   "Read the screen and check which tab is shown"),
        er=steps("The Profile section is opened",
                 "The “All Profiles” tab is displayed",
                 "The Profile section is opened again",
                 "The “Edit Profile” tab, the last known tab, is displayed"),
        remarks="**條文列兩個入口而其去向不同**（Switch Users → All Profiles；"
                "avatar 或 Welcome 文字 → 上次分頁），依 §7 兩者皆須走到。"
                "上次分頁固定為 “Edit Profile”，**使兩個去向可分辨** ——"
                "若上次分頁本就是 All Profiles，兩個入口之結果相同。"
                "方括號 `[username]` **逐字引自 7.3**（§11 之 profile-scoped "
                "例外，D-UP22-01）。"
                "**與 `SWE1-HMI-PROF-054`／`-055`（6.5／6.6）之關係**："
                "那兩條之 popup 為 ch6 之預設 Welcome popup，本條為 ch7 之"
                "welcome popup；037 各自切了 leaf，故各自成條（§8.2.1）。",
        reasoning=(
            "驗證目標：7.3（PRWEL3）—— welcome popup 之兩個入口各自之去向。"
            "關鍵情境條件：上次分頁不得為 “All Profiles”。"
            "為什麼這樣切：兩個入口為同一句之列舉且去向不同，"
            "**併為一條方能在同一組前提下比較兩者**；分立則兩條之 "
            "pre-condition 相同而各驗一半。"),
        kw=["Switch Users", "welcome popup", "last known tab", "avatar"],
    ),

    "SWE1-HMI-PROF-062-01": dict(
        title="Welcome popup clears as soon as the vehicle moves",
        design=STATE,
        pre=steps("The welcome popup of the active Profile is displayed",
                  "The vehicle is stationary",
                  "The vehicle can be brought into motion on the test site"),
        data="NA",
        proc=steps("Bring the vehicle into motion",
                   "Read the screen and check whether the popup is displayed"),
        er=steps("The vehicle is in motion",
                 "The welcome popup is cleared"),
        remarks="**取 motion 一側而非 30 秒一側**：條文之三個清除觸發"
                "（motion／30 秒／互動）為 `whichever comes first`，"
                "故本條須在 30 秒**之內**使車輛移動，否則清除之原因不可歸屬。"
                "30 秒一側屬 `SWE1-HMI-PROF-062-02`（`NR1L-UserProfiles-008`），"
                "互動一側屬 `SWE1-HMI-PROF-062-03`。"
                "**判 P0**：行車中之畫面遮蔽屬 §10.2 之 safety 條件，"
                "與 `SWE1-HMI-PROF-029`／`031` 同類 —— 本條驗的是**防線成立本身**。",
        reasoning=(
            "驗證目標：7.4（PRWEL4）之 motion 分支 —— 車輛開始移動時，"
            "welcome popup 自動清除。"
            "關鍵情境條件：popup 須在顯示中，且移動須發生在 30 秒逾時之前。"
            "為什麼這樣切：三個觸發互斥於歸因（`whichever comes first`），"
            "**不可併為一條** —— 併了就無從判定是哪一個造成清除。"),
        kw=["welcome popup", "in motion", "clear", "PRWEL4"],
    ),

    "SWE1-HMI-PROF-062-03": dict(
        title="Welcome popup clears immediately on screen interaction",
        design=FUNCTIONAL,
        pre=steps("The welcome popup of the active Profile is displayed",
                  "The vehicle is stationary"),
        data="Screen pressed about five seconds after the popup appears, "
             "that is before the 30-second timeout",
        proc=steps("Press the screen while the welcome popup is displayed",
                   "Read the screen and check whether the popup is displayed"),
        er=steps("The screen is pressed while the welcome popup is displayed",
                 "The welcome popup is cleared"),
        remarks="**互動之時點寫在 `input_test_data`** —— 條文之三個觸發為"
                "`whichever comes first`，若互動發生在第 30 秒附近，"
                "清除之原因即不可歸屬。該時點為**測試方法所要求之值**（J-4），"
                "非條文之值，故不寫入 ER。"
                "車輛須靜止：否則 motion 分支（`SWE1-HMI-PROF-062-01`）"
                "會先於互動成立。",
        reasoning=(
            "驗證目標：7.4（PRWEL4）之互動分支 —— 使用者觸碰畫面即清除。"
            "關鍵情境條件：互動須明確早於 30 秒逾時，且車輛靜止。"
            "為什麼這樣切：同 `062-01` —— 三個觸發之歸因不可混。"),
        kw=["welcome popup", "interaction", "clear", "timeout"],
    ),

    "SWE1-HMI-PROF-062-04": dict(
        title="Cleared welcome popup returns only on reactivation",
        design=STATE,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "The welcome popup of Driver Profile A is displayed",
                  "The Welcome popup setting is on for both Profiles",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the screen to clear the welcome popup",
                   "Open and close the Profile section, then read the screen",
                   "Activate Driver Profile B, then activate Driver Profile "
                   "A again",
                   "Read the screen and check whether the popup is displayed"),
        er=steps("The welcome popup is cleared",
                 "The welcome popup does not return during the current "
                 "session",
                 "Driver Profile A is active again",
                 "The welcome popup of Driver Profile A is displayed again"),
        remarks="**ER2 與 ER4 缺一不可**：只驗 ER2 者，一個永不再顯示之實作"
                "會通過；只驗 ER4 者，一個每次回到主畫面就重彈之實作會通過。"
                "**盲區（R-G11）**：`for the duration of the current session` "
                "之「session」條文未定義其邊界。步驟 2 以一次畫面往返代表之，"
                "**那是抽樣而非窮舉** —— 更長之 session 內是否返回，本條不保證。"
                "**X-1**：步驟 3 之切換會觸發 5.3.1 之 PU0580，而該 popup **即 ER3／ER4 所涉者** —— 標的而非干擾。",
        reasoning=(
            "驗證目標：7.4（PRWEL4）之後半 —— 清除後於本 session 內不返回，"
            "直到該 profile 再次被啟用。"
            "關鍵情境條件：須有第二個 profile，"
            "否則「再次啟用」這個唯一無歧義之解除條件造不出來。"
            "為什麼這樣切：`design_method` 取狀態轉換 ——"
            "清除建立一個壓抑狀態，再啟用解除之。"),
        kw=["welcome popup", "session", "reactivated", "suppressed"],
    ),

    "SWE1-HMI-PROF-063": dict(
        title="Remote start time does not count toward the 30 seconds",
        design=STATE,
        pre=steps("The vehicle is in remote start",
                  "The welcome popup of the active Profile is displayed",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Wait 30 seconds while the vehicle is in remote start",
                   "Read the screen and check whether the popup is displayed",
                   "Exit the remote start and wait 30 more seconds",
                   "Read the screen and check whether the popup is displayed"),
        er=steps("The vehicle stays in remote start for 30 seconds",
                 "The welcome popup is still displayed",
                 "The remote start ends and 30 seconds pass",
                 "The welcome popup is cleared"),
        remarks="**ER4 不可省** —— 只驗 ER2（遙控起動期間不清除），"
                "一個**根本沒有 30 秒計時**之實作會通過；"
                "ER4 證明計時仍在，只是排除了遙控起動之時間。"
                "步驟 3 之後須全程無互動且車輛靜止，"
                "否則清除可歸因於另兩個觸發。",
        reasoning=(
            "驗證目標：7.4.1（PRWEL4.1）—— 30 秒之計時不含遙控起動之時間。"
            "關鍵情境條件：popup 於遙控起動期間即已顯示。"
            "為什麼這樣切：`design_method` 取狀態轉換 ——"
            "本條之判定取決於**一次狀態離開**（退出遙控起動）之後計時才開始。"),
        kw=["remote start", "30 seconds", "timer", "welcome popup"],
    ),

    "SWE1-HMI-PROF-064": dict(
        title="Valet Mode welcome popup clears like the other popups",
        design=FUNCTIONAL,
        pre=steps("Valet Mode is active on the vehicle",
                  "The Valet Mode welcome popup is displayed",
                  "The vehicle is stationary"),
        data="Screen pressed about five seconds after the popup appears",
        proc=steps("Press the screen while the Valet Mode welcome popup is "
                   "displayed",
                   "Read the screen and check whether the popup is displayed"),
        er=steps("The screen is pressed while the popup is displayed",
                 "The Valet Mode welcome popup is cleared"),
        remarks="**條文說的是「與其他 welcome popup 相同之清除／逾時行為」——"
                "即三個觸發**（motion／30 秒／互動）。本條取**互動**一側，"
                "**為抽樣而非窮舉**（§8.4.2）：另兩側之同型性不由本條保證。"
                "取互動一側之理由：三者中唯一**不需等待亦不需移動車輛**者，"
                "而 Valet Mode 下移動車輛另有 12.x 之限制介入。"
                "同型之三個觸發本身由 `SWE1-HMI-PROF-062-01`／"
                "`SWE1-HMI-PROF-062-03`／`SWE1-HMI-PROF-062-02` 各自驗證。",
        reasoning=(
            "驗證目標：7.5（PRWEL5）—— Valet Mode 之 welcome popup 具有與"
            "其他 welcome popup 相同之清除／逾時行為。"
            "關鍵情境條件：Valet Mode 須為作用中，且其 popup 在顯示中。"
            "為什麼這樣切：本 leaf 之單位為**同型性**；"
            "把三個觸發都走一遍等於把 7.4 重測一次，"
            "而 037 已為 7.4 切了獨立 leaf。"),
        kw=["Valet Mode", "welcome popup", "clear", "same behavior"],
    ),

    # ══════════════════ ch8 / NEWPR ══════════════════════════════════

    "SWE1-HMI-PROF-065": dict(
        title="R1 High begins Tutorials after the preferences step",
        design=SCENARIO,
        pre=steps("The vehicle is an R1 High variant",
                  "A New Profile Setup is in progress",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Complete the New Profile Setup up to step 4",
                   "Read the screen and check that the preferences prompt is "
                   "shown",
                   "Choose to create from current preferences",
                   "Read the screen shown after the preferences step"),
        er=steps("Step 4 of the New Profile Setup is completed",
                 "The prompt to choose current or default preferences is "
                 "displayed",
                 "The choice is accepted",
                 "Tutorials begin and no Connected Personal Account login is "
                 "launched"),
        remarks="**變體 axis `r1h-cpa-8.1`**：本條為 R1 High 側。"
                "base 側（`Is CPA present?` 為是 → 啟動 CPA 登入）"
                "**在 037 內無 leaf**，只見於 PDF p12 之流程圖，依 R-U56 不造；"
                "已於 `audit_variant_pairs.AXES` 由 `pending` 改為具名不配"
                "（述詞 `no-other-side-leaf` 實測）—— 同 `SWE1-HMI-PROF-046`。"
                "**ER4 之缺席斷言不可省**：只驗 Tutorials 有沒有開，"
                "一個**先開 CPA 再開 Tutorials** 之實作會通過（§8.3）。"
                "條文之 `accessible from the Edit Profile screen only` 一句，"
                "其正向屬 `SWE1-HMI-PROF-110`（11.3.1），本條不涵蓋其全稱反向。",
        reasoning=(
            "驗證目標：8.1（NEWPR0）—— R1 High 上，第 4 步之後依偏好請求"
            "並進入 Tutorials，CPA 不啟動。"
            "關鍵情境條件：車型須為 R1 High。"
            "為什麼這樣切：`design_method` 取情境／用例 ——"
            "本條驗的是設定流程末段之**走向**，跨偏好選擇與 Tutorials 兩處。"),
        kw=["R1 High", "Tutorials", "CPA", "New Profile Setup"],
    ),

    "SWE1-HMI-PROF-066": dict(
        title="New Profile Setup starts from the All Profiles tab",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and press the option to add "
                   "a new Profile",
                   "Read the screen and check that the New Profile Setup "
                   "started"),
        er=steps("The option to add a new Profile is pressed",
                 "The first step of the New Profile Setup is displayed"),
        remarks="**8.2 之內容為對流程圖之指涉**（`See flow for setting up a "
                "New Profile above`）—— 圖之內容不逐字重述（§8.4.1）；"
                "各步驟之細節分屬 8.6–8.9，本條只驗**流程被起始**。"
                "條文另註 `Connecting an account or downloading an existing "
                "Connected account are not pictured here` —— 該句是說**圖上沒畫**，"
                "不是說該功能不存在；下載既有帳號一側屬 8.6"
                "（`SWE1-HMI-PROF-072`）。"
                "**本條之 label 依 RD #5 之答覆可能調整**"
                "（39 包作業 2 之命中：本節寫 `Connected account`）。",
        reasoning=(
            "驗證目標：8.2（NEWPR1）—— New Profile Setup 之起始。"
            "關鍵情境條件：profile 數未達上限，否則新增入口會被隱藏"
            "（5.2，`SWE1-HMI-PROF-021-02`）。"
            "為什麼這樣切：本 leaf 之單位為**起始**；"
            "起始之後之每一步各有其 leaf。"),
        kw=["New Profile Setup", "All Profiles", "add", "initiate"],
    ),

    "SWE1-HMI-PROF-067": dict(
        title="Profile Setup is presented as a series of popups",
        design=FUNCTIONAL,
        pre=steps("A New Profile Setup is in progress at its first step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Complete each step of the New Profile Setup in turn",
                   "Read each screen and check that every step is a popup"),
        er=steps("Each step of the New Profile Setup is completed",
                 "Every step is presented as a popup"),
        remarks="**具體之 popup id 不寫** —— 條文說 `Specific popups can be "
                "found in the HMI Pop Up List`，而該清單之逐步對映**不在本 "
                "feature 之輸入內**（`data/spec_popup_ids.tsv` 只記 id 與其"
                "出現節次，非流程對映）。依 §8.4.1 不自擬，ER 只驗**形態**。"
                "此為**上游文件依賴**，同 `SWE1-HMI-PROF-044` 之截斷規則 ——"
                "**不援引 R-U56**（本 leaf 存在，缺的是規則之權威文件）。",
        reasoning=(
            "驗證目標：8.3（NEWPR2）—— 設定流程以一連串 popup 呈現。"
            "關鍵情境條件：須自第一步走到最後一步，"
            "否則「每一步都是 popup」只驗了其中一步。"
            "為什麼這樣切：**可判定之部分只有「是不是 popup」** ——"
            "「是不是清單上的那一個 popup」之權威在外部文件。"),
        kw=["Profile Setup", "popups", "series", "HMI Pop Up List"],
    ),

    "SWE1-HMI-PROF-068": dict(
        title="Pressing another button during setup asks to discard",
        design=FUNCTIONAL,
        pre=steps("A New Profile Setup is in progress at the username step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press a button on the status bar during the setup",
                   "Read the screen and check which popup is displayed"),
        er=steps("The status bar button is pressed during the New Profile "
                 "Setup",
                 "A popup asking to confirm discarding the New Profile setup "
                 "is displayed"),
        remarks="**條文列兩處入口**（`main menu bar or status bar`）——"
                "本條取狀態列一側，**為抽樣**（§8.4.2）："
                "主選單列一側之結果不由本條保證。"
                "取狀態列之理由：其於設定 popup 顯示期間仍可見（4.6），"
                "主選單列是否可見條文未述。"
                "**未驗「確認之後真的丟棄」** —— 條文只說「給另一個 popup 問」，"
                "丟棄之後果未述，依 §8.4.1 不推定。",
        reasoning=(
            "驗證目標：8.3.1（NEWPR2.1）—— 設定中按其他按鍵視同 Cancel／X，"
            "並出現確認丟棄之 popup。"
            "關鍵情境條件：設定須在進行中且已有輸入，"
            "否則「丟棄」無標的。"
            "為什麼這樣切：本 leaf 之單位為**該詢問之出現**。"),
        kw=["status bar", "discard", "New Profile Setup", "cancel"],
    ),

    # ── 8.4：兩個 leaf 併寫（同節多 leaf 之順序，41 包 §五）
    "SWE1-HMI-PROF-069-01": dict(
        title="Avatars already in use are filtered out of the list",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist, each with a different avatar",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “Edit Profile” tab and record the avatars of "
                   "both Profiles",
                   "Start a New Profile Setup and open the avatar selection "
                   "screen",
                   "Read the avatar list and check that the recorded avatars "
                   "are absent"),
        er=steps("The avatars of both Profiles are recorded",
                 "The avatar selection screen is displayed",
                 "Neither avatar recorded in step 1 is offered in the list"),
        remarks="**ER3 斷言「兩個都不在」而非「有一個不在」** —— "
                "條文之 `No two Profiles can use the same Avatar` 是全稱；"
                "只檢一個，一個「只濾掉現用 profile 之 avatar」之實作會通過。"
                "**與 `SWE1-HMI-PROF-077`（8.8.1）之關係**："
                "8.8.1 之 `As avatars are in use, they will not be shown` 與"
                "本 leaf 之過濾**是同一件事在兩節之兩次出現**；"
                "隱藏一側由本 leaf（`SWE1-HMI-PROF-069-01`）承擔，"
                "`SWE1-HMI-PROF-077` 只驗初始數目。",
        reasoning=(
            "驗證目標：8.4（NEWPR3）—— avatar 清單只顯示未被使用者，"
            "兩個 profile 不得共用同一 avatar。"
            "關鍵情境條件：兩個 profile 之 avatar 須不同且已記錄，"
            "缺席斷言方有標的。"
            "為什麼這樣切：037 對 8.4 切兩個 leaf；本 leaf 為**過濾**，"
            "自動 highlight 屬 `SWE1-HMI-PROF-069-02`。"),
        kw=["avatar", "filtered", "in use", "unique"],
    ),

    "SWE1-HMI-PROF-069-02": dict(
        title="Next available default avatar is highlighted automatically",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist, each using one of the first "
                  "default avatars",
                  "A New Profile Setup is in progress",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the avatar selection screen of the New Profile "
                   "Setup",
                   "Read the screen and check which avatar is highlighted"),
        er=steps("The avatar selection screen is displayed",
                 "An avatar is highlighted without any choice being made, "
                 "and it is the next available default avatar"),
        remarks="**ER2 併驗兩件事** —— 「未做任何選擇即已有一個被 highlight」"
                "與「它是下一個可用之預設 avatar」。"
                "只驗前者，一個**永遠 highlight 第一個（含已被使用者）**之實作"
                "會通過；只驗後者則測不到「不必先選」這個條文之目的"
                "（`so that the user does not need to make a choice`）。"
                "pre-condition 令兩個 profile 各佔一個前段預設 avatar，"
                "**使「下一個可用」與「第一個」不是同一個**。",
        reasoning=(
            "驗證目標：8.4（NEWPR3）—— 進入 avatar 選擇畫面時，"
            "系統自動 highlight 下一個未被使用之預設 avatar。"
            "關鍵情境條件：前段預設 avatar 須已被佔用，"
            "否則「下一個可用」與「第一個」不可分辨。"
            "為什麼這樣切：與 `069-01` 同節不同 leaf ——"
            "前者驗清單之內容，本條驗清單之初始選取狀態。"),
        kw=["avatar", "highlighted", "default", "next available"],
    ),

    "SWE1-HMI-PROF-071": dict(
        title="The same username can be used by two Driver Profiles",
        design=FUNCTIONAL,
        pre=steps("Driver Profile A exists with the username Alex",
                  "Two Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="Username entered for the new Profile: Alex",
        proc=steps("Start a New Profile Setup and enter the username Alex",
                   "Complete the setup",
                   "Open the “All Profiles” tab and read the usernames shown"),
        er=steps("The username Alex is accepted",
                 "The new Driver Profile is saved",
                 "Two Driver Profiles with the username Alex are shown"),
        remarks="**ER3 不可省** —— 只驗 ER1（輸入被接受），"
                "一個接受輸入卻在儲存時把第二個改名之實作會通過。"
                "Alex 為測試設置（J-12）：條文未指定名稱。"
                "**與 `SWE1-HMI-PROF-069-01` 之對比值得記**："
                "avatar **不得**重複而 username **得**重複 ——"
                "兩者同在 ch8 而規則相反，故本條之 ER 須明說「兩個都在」。",
        reasoning=(
            "驗證目標：8.5（NEWPR4）—— 同一個 username 可用於多個 profile。"
            "關鍵情境條件：已存在一個使用該 username 之 profile。"
            "為什麼這樣切：本 leaf 為單一允許性斷言；"
            "username 之字元規則屬 8.7／8.7.2。"),
        kw=["username", "same", "multiple Profiles", "allowed"],
    ),

    "SWE1-HMI-PROF-072": dict(
        title="Connected vehicles offer create new or download existing",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with connectivity",
                  "A New Profile Setup is in progress at its first step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read the first step of the New Profile Setup",
                   "Read the screen and check the options offered"),
        er=steps("The first step of the New Profile Setup is displayed",
                 "The options to create new or to download an existing "
                 "Profile are offered"),
        remarks="**`For connected vehicles` 為適用條件**（§8.7.3）——"
                "以 pre-condition 固定為連網車輛。"
                "**非連網車輛之第一步條文未述**，依 §8.4.1 不推定，"
                "亦不列為覆蓋缺口（037 未為其切 leaf）。"
                "下載既有 profile **之後**之流程屬 8.7.1 之 Back 選項"
                "（`SWE1-HMI-PROF-074`），本條只驗選項之存在。",
        reasoning=(
            "驗證目標：8.6（NEWPR5）—— 連網車輛之設定第一步提供"
            "「建立新的或下載既有」兩個選項。"
            "關鍵情境條件：車輛須具連網能力。"
            "為什麼這樣切：本 leaf 之單位為**第一步之選項**。"),
        kw=["connected vehicle", "create new", "download existing", "Step 1"],
    ),

    # ── 8.7：兩個 leaf 併寫（同一個上限之兩端）
    "SWE1-HMI-PROF-073-02": dict(
        title="Next button stays unavailable while the username is empty",
        design=BVA,
        pre=steps("A New Profile Setup is at the username step",
                  "The username field is empty",
                  "The vehicle is stationary"),
        data="Username length: 0 → 1 characters",
        proc=steps("Read the Next button while the username field is empty",
                   "Type one character into the username field",
                   "Read the Next button and check whether it is available"),
        er=steps("The Next button is not available",
                 "One character is shown in the username field",
                 "The Next button is available"),
        remarks="**邊界對為 0 → 1**（§5.6 之界前／界上兩讀）："
                "只讀界上（1 字元時可按），一個**永遠可按**之實作會通過。"
                "本 leaf 為下界；上界 12 字元屬 `SWE1-HMI-PROF-073-01`"
                "（`NR1L-UserProfiles-009`），空格計入屬 "
                "`SWE1-HMI-PROF-073-03` —— **三者為同一條條文之三個界**。",
        reasoning=(
            "驗證目標：8.7（NEWPR6）—— username 之最小長度為 1，"
            "欄位為空時 Next 不可用。"
            "關鍵情境條件：起始須為完全空白之欄位。"
            "為什麼這樣切：`design_method` 取邊界值分析 ——"
            "判定完全取決於 0 與 1 這一個界。"),
        kw=["Next button", "username", "minimum", "one character"],
    ),

    "SWE1-HMI-PROF-073-03": dict(
        title="Spaces count toward the username character limit",
        design=BVA,
        pre=steps("A New Profile Setup is at the username step",
                  "The username field is empty",
                  "The vehicle is stationary"),
        # K-4a 要求 `input_test_data` 明載邊界對；首跑判紅（散文寫法讀不出）。
        data="Username length: 12 → 13 characters "
             "(eleven letters plus one space, then one more character)",
        proc=steps("Type eleven letters and one space into the username "
                   "field",
                   "Read the field and record the characters accepted",
                   "Type one more character and read the username field"),
        er=steps("The eleven letters and the space are accepted",
                 "Twelve characters are shown in the username field",
                 "The keyboard does not allow a thirteenth character in "
                 "the field"),
        remarks="**空格放在第十二個位置** —— 若放在中間，"
                "一個「不計空格」之實作仍會在第十二個字母處停下，"
                "與正確實作**在此設置下不可分辨**；放在最後才使兩者分歧："
                "不計空格者會再接受一個字母。"
                "上限 12 出自 8.7 之條文；本條與 "
                "`SWE1-HMI-PROF-073-01`（`NR1L-UserProfiles-009`）"
                "**驗的是同一個上限之兩種輸入**（純字母／含空格）。",
        reasoning=(
            "驗證目標：8.7（NEWPR6）—— 空格為合法字元且計入 12 字元上限。"
            "關鍵情境條件：空格須落在使兩種實作分歧之位置（見 remarks）。"
            "為什麼這樣切：`design_method` 取邊界值分析 ——"
            "判定取決於第 12／13 個字元之接受與否。"),
        kw=["spaces", "character limit", "username", "twelve"],
    ),

    "SWE1-HMI-PROF-074": dict(
        title="Save, Cancel and Back options on the username step",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with connectivity",
                  "A New Profile Setup is at the username step",
                  "The setup was reached through the download step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read the screen and record the options offered",
                   "Press Save and read the screen",
                   "Return to the username step and press Cancel",
                   "Read the screen and check which popup is displayed"),
        er=steps("Options to Save, Cancel and Back are offered",
                 "Step 3 of the New Profile Setup is displayed",
                 "Cancel is pressed",
                 "A confirmation popup is displayed"),
        remarks="**pre-condition 之「經下載步驟而來」是 Back 之適用條件** —— "
                "條文寫 `Back (only available if there was a previous step "
                "for downloading a connected Profile)`；"
                "不設此前提，ER1 之三個選項只會出現兩個，**而那不是缺陷**。"
                "**未驗「無前一步時 Back 不出現」** —— 那是同一句之反向，"
                "037 未為其切 leaf，依 R-U56 不造。"
                "Cancel 之確認 popup **按下之後**之後果屬 8.3.1"
                "（`SWE1-HMI-PROF-068`）。",
        reasoning=(
            "驗證目標：8.7.1（NEWPR6.1）—— username 步驟提供 Save／Cancel／"
            "Back 三個選項，Save 進到第 3 步，Cancel 出現確認 popup。"
            "關鍵情境條件：須有前一步（下載既有 profile），Back 方會出現。"
            "為什麼這樣切：三個選項為同一句之列舉，§7 要求皆走到；"
            "本條走 Save 與 Cancel 兩者之去向，Back 只驗其存在 ——"
            "**其去向即步驟 3 所走之回程**，重複驗證無新資訊。"),
        kw=["Save", "Cancel", "Back", "username step"],
    ),

    "SWE1-HMI-PROF-075": dict(
        title="Special characters are not accepted in a username",
        design=NEGATIVE,
        pre=steps("A New Profile Setup is at the username step",
                  "The username field is empty",
                  "The vehicle is stationary"),
        data="Characters typed: letters, digits, then a special character",
        proc=steps("Type letters and digits into the username field",
                   "Attempt to type a special character",
                   "Read the field and check which characters are shown"),
        er=steps("The letters and digits are accepted",
                 "The special character is not accepted",
                 "Only the letters and digits typed in step 1 are shown"),
        remarks="**ER1 不可省** —— 只驗「特殊字元不被接受」，"
                "一個**什麼都不接受**之實作會通過（§8.3）。"
                "**ER3 斷言欄位之最終內容**：一個接受特殊字元卻不顯示之實作，"
                "只看 ER2 會通過而其儲存值已錯。"
                "條文未列舉何謂 special character，依 §8.4.1 不代其列舉；"
                "執行時所用之字元記於執行紀錄。",
        reasoning=(
            "驗證目標：8.7.2（NEWPR6.2）—— username 得為英數，不得含特殊字元。"
            "關鍵情境條件：同一次輸入中兼有合法與非法字元，"
            "使「擋的是特殊字元」而非「擋了全部」可分辨。"
            "為什麼這樣切：`design_method` 取負向測試 ——"
            "步驟 2 為對一個**不該生效之輸入**的嘗試。"),
        kw=["special characters", "username", "alphanumeric", "blocked"],
    ),

    # ── 8.8：三個 leaf 併寫（同一句所切之 highlight ＋ 兩個螢幕尺寸）
    "SWE1-HMI-PROF-076-01": dict(
        title="Highlight moves to the newly chosen avatar",
        design=FUNCTIONAL,
        pre=steps("A New Profile Setup is at the avatar step",
                  "One avatar is highlighted by default",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read the avatar screen and record which avatar is "
                   "highlighted",
                   "Choose a different avatar",
                   "Read the screen and check which avatar is highlighted"),
        er=steps("The highlighted avatar is recorded",
                 "A different avatar is chosen",
                 "The chosen avatar is highlighted and the avatar recorded "
                 "in step 1 is not"),
        remarks="**ER3 之後半不可省** —— 只驗「新選者被 highlight」，"
                "一個**兩個都 highlight** 之實作會通過（同 "
                "`NR1L-UserProfiles-117` 之形狀）。"
                "預設 highlight 之**選定規則**屬 `SWE1-HMI-PROF-069-02`"
                "（8.4），本條只以其為起點。",
        reasoning=(
            "驗證目標：8.8（NEWPR7）—— 選了不同 avatar 時，highlight 隨之移動。"
            "關鍵情境條件：起始須已有一個被 highlight 者且已記錄。"
            "為什麼這樣切：037 對 8.8 切三個 leaf；本 leaf 為 highlight 之移動，"
            "兩個螢幕尺寸之版面屬 `SWE1-HMI-PROF-076-02`／`-03`。"),
        kw=["highlight", "avatar", "chosen", "moves"],
    ),

    "SWE1-HMI-PROF-076-02": dict(
        title="Avatar shown above the Save & Continue button on 8.4 inch",
        design=FUNCTIONAL,
        pre=steps("The vehicle screen is 8.4 inches or larger",
                  "A New Profile Setup is at the avatar step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Choose an avatar",
                   "Read the screen and check the avatar position and the "
                   "button text"),
        er=steps("The avatar is chosen",
                 "The chosen avatar is shown above the button and the button "
                 "reads “Save & Continue”"),
        remarks="**與 `SWE1-HMI-PROF-076-03` 為 §7 之列舉配對** —— "
                "同一句切出之兩個螢幕尺寸，兩者之**位置與字樣皆不同**"
                "（上方／旁邊、`Save & Continue`／`Save`）。"
                "**兩者皆須造**：只造其一，一個在所有尺寸上都用同一版面之實作"
                "會通過其中一條。"
                "**此非變體覆寫**（`audit_variant_pairs` 之母體不含之）："
                "spec 未以覆寫註記標示，而是**同一句正面寫出兩側** ——"
                "兩者之判別由 037 之 `SWE1-HMI-PROF-076-02` 與 "
                "`SWE1-HMI-PROF-076-03` 兩個 leaf 承擔。",
        reasoning=(
            "驗證目標：8.8（NEWPR7）—— 8.4 吋以上之螢幕，"
            "選定之 avatar 顯示於儲存鍵**上方**，鍵上字樣為 “Save & Continue”。"
            "關鍵情境條件：螢幕尺寸為 8.4 吋以上。"
            "為什麼這樣切：位置與字樣為同一句之並列斷言，§5.7 併於 ER2。"),
        kw=["8.4 inch", "avatar", "Save & Continue", "above"],
    ),

    "SWE1-HMI-PROF-076-03": dict(
        title="Avatar shown next to the Save button on 7 inch screens",
        design=FUNCTIONAL,
        pre=steps("The vehicle screen is 7 inches",
                  "A New Profile Setup is at the avatar step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Choose an avatar",
                   "Read the screen and check the avatar position and the "
                   "button text"),
        er=steps("The avatar is chosen",
                 "The chosen avatar is shown next to the button and the "
                 "button reads “Save”"),
        remarks="**與 `SWE1-HMI-PROF-076-02` 為 §7 之列舉配對**（見該條）。"
                "**ER2 之字樣斷言是本對之關鍵**：位置之「上方／旁邊」在 7 吋"
                "小螢幕上可能難以目視分辨，而字樣之 `Save` 與 "
                "`Save & Continue` 是二值的。",
        reasoning=(
            "驗證目標：8.8（NEWPR7）—— 7 吋螢幕，選定之 avatar 顯示於"
            "儲存鍵**旁邊**，鍵上字樣為 “Save”。"
            "關鍵情境條件：螢幕尺寸為 7 吋。"
            "為什麼這樣切：同 `076-02`，兩者互為配對之另一側。"),
        kw=["7 inch", "avatar", "Save", "next to"],
    ),

    "SWE1-HMI-PROF-077": dict(
        title="At least ten avatars are offered initially",
        design=FUNCTIONAL,
        pre=steps("A New Profile Setup is at the avatar step",
                  "No avatar is in use by another Driver Profile",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the avatar selection screen and count the avatars "
                   "offered",
                   "Read the count and check whether it reaches ten"),
        er=steps("The avatars offered are counted",
                 "At least ten avatars are offered"),
        remarks="**pre-condition 指定「無 avatar 被佔用」** —— 否則"
                "「至少十個」與「原本十一個而被隱藏一個」不可分辨，"
                "本條會把一個數目不足之實作判成通過。"
                "**「使用中者不顯示」一側由 `SWE1-HMI-PROF-069-01`（8.4）承擔** ——"
                "8.8.1 之該句與 8.4 之過濾**是同一件事在兩節之兩次出現**，"
                "依 §8.2.1 不重複造。"
                "分類是否影響一次可見之數目，條文未述；"
                "本條之計數為**跨分類之總數**，已於 reasoning 具名。",
        reasoning=(
            "驗證目標：8.8.1（NEWPR7.1）—— 初始至少提供 10 個 avatar。"
            "關鍵情境條件：無 avatar 被其他 profile 佔用。"
            "為什麼這樣切：本 leaf 之單位為**數目下界**；"
            "隱藏規則已由 `SWE1-HMI-PROF-069-01`（8.4）承擔。"
            "**計數之範圍**：條文只說 `at least 10 Avatars initially`，"
            "未說是否須於同一畫面可見；本條計跨分類之總數，"
            "**一個把十個分散在三個分類之實作會通過** —— 此為條文之留白。"),
        kw=["ten avatars", "initial", "count", "avatar selection"],
    ),

    "SWE1-HMI-PROF-078": dict(
        title="Avatars are sorted into at least three categories",
        design=FUNCTIONAL,
        pre=steps("A New Profile Setup is at the avatar step",
                  "The vehicle screen is 8.4 inches or larger",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read the avatar screen and count the category buttons",
                   "Press one category button",
                   "Read the list and check which avatars are shown"),
        er=steps("At least three category buttons are offered",
                 "The category button is pressed",
                 "Only the avatars of that category are shown"),
        remarks="**ER3 不可省** —— 只驗分類按鈕之數目，"
                "一個**按了沒反應**之實作會通過；條文明說"
                "`Pushing a category button will show the respective grouping`。"
                "**7 吋之獨立分類畫面未涵蓋**：條文寫 `7\" will have a "
                "separate screen for category selection`，"
                "而 037 未為其另切 leaf —— 本條取 8.4 吋以上一側，"
                "**為抽樣，7 吋之分類畫面不由本條保證**。",
        reasoning=(
            "驗證目標：8.8.2（NEWPR7.2）—— avatar 至少分為 3 類，"
            "按下分類按鈕顯示該類之 avatar。"
            "關鍵情境條件：螢幕尺寸取 8.4 吋以上（分類與清單同畫面）。"
            "為什麼這樣切：數目與作用為同一句之兩個斷言，§5.7 併於一條。"),
        kw=["categories", "avatar", "three", "category button"],
    ),

    "SWE1-HMI-PROF-079": dict(
        title="Final setup step offers current or default preferences",
        design=SCENARIO,
        pre=steps("Driver Profile A is the active Profile and has known "
                  "preferences",
                  "A New Profile Setup is in progress",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record the preferences of Driver Profile A",
                   "Complete the New Profile Setup up to its final step",
                   "Read the prompt shown at the final step",
                   "Choose to create from current preferences, then read the "
                   "new Profile's preferences"),
        er=steps("The preferences of Driver Profile A are recorded",
                 "The final step of the New Profile Setup is displayed",
                 "The prompt reads “Create from Current Preferences or "
                 "Create from Default?”",
                 "The new Profile's preferences match those recorded in "
                 "step 1"),
        remarks="**ER4 是條文後半之唯一可觀察形式** —— "
                "`carry-over all of the previously active Profile’s "
                "preferences`；只驗提示文字（ER3），"
                "一個顯示該提示卻兩個選項都給預設值之實作會通過。"
                "**未走 `Create from Default` 一側**：條文只說選了 current 會"
                "沿用，未說選了 default 會如何（`Default` 之內容未定義），"
                "依 §8.4.1 不推定。"
                "此提示為 **New Profile setup only**（條文明載），"
                "編輯既有 profile 時不出現 —— 該側屬 8.10.1／8.11。",
        reasoning=(
            "驗證目標：8.9（NEWPR8）—— 設定之最終步提示選擇沿用現有偏好或"
            "採用預設；選前者則沿用前一個現用 profile 之全部偏好與設定。"
            "關鍵情境條件：前一個現用 profile 之偏好須先記錄。"
            "為什麼這樣切：`design_method` 取情境／用例 ——"
            "本條跨設定流程之末段與新 profile 之初始狀態兩處。"),
        kw=["final step", "current preferences", "default", "carry-over"],
    ),

    "SWE1-HMI-PROF-080": dict(
        title="Setup completion returns to All Profiles with the new Profile",
        design=FUNCTIONAL,
        pre=steps("A New Profile Setup is at its final step",
                  "Driver Profile A is the active Profile",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Complete the New Profile Setup",
                   "Read the screen and check the tab shown and the active "
                   "Profile"),
        er=steps("The New Profile Setup is completed",
                 "The “All Profiles” tab is shown and the new Profile is the "
                 "active Profile"),
        remarks="**ER2 併驗畫面與現用者** —— 條文兩句（`return to the “All "
                "Profiles” tab`、`The new Profile will be the active "
                "Profile`）為同一個完成事件之兩個結果，§5.7 併驗。"
                "pre-condition 具名 A 為原現用者，**使「新 profile 成為現用者」"
                "是一次可觀察之改變**，而非恆真。"
                "狀態列圖示之更新屬 `SWE1-HMI-PROF-082`（8.10.2）。",
        reasoning=(
            "驗證目標：8.10（NEWPR9）—— 設定完成後回到 “All Profiles” 分頁，"
            "且新 profile 成為現用者。"
            "關鍵情境條件：設定前之現用者須為另一個 profile。"
            "為什麼這樣切：本 leaf 之單位為**完成之後果**；"
            "編輯（非新增）之回程屬 `SWE1-HMI-PROF-081`，其結果不同。"),
        kw=["setup complete", "All Profiles", "active Profile", "new"],
    ),

    "SWE1-HMI-PROF-081": dict(
        title="Editing returns to the originating Edit Profile page",
        design=FUNCTIONAL,
        pre=steps("Driver Profile A is the active Profile",
                  "The “Edit Profile” tab is open at the page holding the "
                  "username option",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Record which page of the “Edit Profile” tab is open",
                   "Select the option to edit the username and complete the "
                   "edit",
                   "Read the screen and check which page is shown"),
        er=steps("The page of the “Edit Profile” tab is recorded",
                 "The username edit is completed",
                 "The page recorded in step 1 is shown again"),
        remarks="**與 `SWE1-HMI-PROF-080` 之結果相反** —— 新增完成回 "
                "“All Profiles”，編輯完成回**發起編輯之該頁**；"
                "兩者同為「完成之後去哪」而條文分兩節，故各自成條。"
                "**ER3 以步驟 1 所記者為準而非寫死頁名** —— "
                "條文說的是 `the page … they initiated the editing from`，"
                "寫死頁名等於把一個相對斷言改成絕對斷言。",
        reasoning=(
            "驗證目標：8.10.1（NEWPR9.1）—— 自 Edit Profile 畫面發起之編輯，"
            "完成後回到發起之該頁。"
            "關鍵情境條件：發起頁須先記錄，否則「回到原頁」無對照。"
            "為什麼這樣切：本 leaf 為編輯路徑之回程。"),
        kw=["Edit Profile", "return", "originating page", "editing"],
    ),

    "SWE1-HMI-PROF-082": dict(
        title="Status bar icon updates to the new active Profile",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist with different avatars",
                  "Driver Profile A is the active Profile",
                  "A New Profile Setup is at its final step",
                  "The Welcome popup setting is off for all Profiles",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Read the status bar and record the Profile button icon",
                   "Complete the New Profile Setup",
                   "Read the status bar and check whether the icon changed"),
        er=steps("The Profile button icon is recorded",
                 "The new Profile is created and becomes the active Profile",
                 "The Profile button icon matches the new Profile and "
                 "differs from the icon recorded in step 1"),
        remarks="**與 `SWE1-HMI-PROF-013`（`NR1L-UserProfiles-101`，4.6）之"
                "分別**：那一條驗的是**切換 profile 時**圖示隨之改變，"
                "本條驗的是**新增完成時**。兩節各自明載，故各自成條（§8.2.1）。"
                "**X-1**：pre-condition 指定 Welcome popup 設定為關閉 ——"
                "新 profile 之啟用會觸發 7.1 之 welcome popup 而遮住狀態列，"
                "而本條之判定全在狀態列。",
        reasoning=(
            "驗證目標：8.10.2（NEWPR9.2）—— 狀態列之 Profile 鍵圖示更新為"
            "新的現用 profile。"
            "關鍵情境條件：原現用者之圖示須先記錄，且兩者之 avatar 不同。"
            "為什麼這樣切：本 leaf 之單位為**圖示之更新**；"
            "分頁之去向屬 `SWE1-HMI-PROF-080`。"),
        kw=["status bar", "icon", "active Profile", "update"],
    ),

    "SWE1-HMI-PROF-083": dict(
        title="Editing only the avatar shows only the avatar popup",
        design=FUNCTIONAL,
        pre=steps("Driver Profile A is the active Profile with a username "
                  "and an avatar",
                  "The “Edit Profile” tab is open",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Select the option to edit the avatar",
                   "Read the screen and check which popups are shown",
                   "Press the back arrow and read the Profile"),
        er=steps("The avatar edit is started",
                 "Only the avatar selection popup is shown and no username "
                 "popup appears",
                 "The edit is cancelled and the avatar is unchanged"),
        remarks="**ER2 之缺席斷言是本條之判別力** —— 只驗「avatar popup 有出現」，"
                "一個把整段新增流程都跑一遍之實作會通過。"
                "**ER3 驗的是「back arrow 等同取消」**：條文之 "
                "`the back arrow would be the same as canceling` ——"
                "只驗畫面關閉不足，須斷言**值未被寫入**。"
                "條文列 username 與 avatar 兩個入口，本條取 avatar 一側"
                "（條文自己舉的例即為 avatar），**username 一側為同型**，"
                "其結果不由本條保證。",
        reasoning=(
            "驗證目標：8.11（NEWPR10）—— 只編輯 username 或 avatar 時只顯示"
            "相關之 popup，且 back arrow 等同取消。"
            "關鍵情境條件：自 Edit Profile 畫面發起，而非自新增流程。"
            "為什麼這樣切：兩個斷言（只出現相關 popup／back 等同取消）"
            "為同一句之兩半，§5.7 併於一條。"),
        kw=["avatar", "relevant popup", "back arrow", "cancel"],
    ),

    "SWE1-HMI-PROF-084": dict(
        title="Back arrow returns to the previous step keeping selections",
        # **K-4a 首跑判紅，改判之。** 原標狀態轉換。本條所驗者為
        # **已輸入之值在一次前進與後退之後仍在** —— 那是不變性，
        # 不是 A→B 之遷移（畫面之來回不是系統狀態之遷移）。
        # 同 `SWE1-HMI-PROF-038`（40 輪）與 `SWE1-HMI-PROF-015`（28 輪）之先例：
        # **改判方法，不放寬詞表**。
        design=FUNCTIONAL,
        pre=steps("A New Profile Setup is in progress at the username step",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Enter a username at the username step and record it",
                   "Continue to the avatar step and choose an avatar",
                   "Press the back arrow and read the username step",
                   "Read the username field and check whether it matches "
                   "step 1"),
        er=steps("The username is entered and recorded",
                 "The avatar step is displayed and an avatar is chosen",
                 "The username step is displayed again",
                 "The username field holds the username recorded in step 1"),
        remarks="**輸入動作留在 procedure 而非 pre-condition**（W-1）："
                "ER4 所斷言者正是該輸入之保留，"
                "若把它寫成 pre-condition 之完成式，"
                "「保留」與「一開始就在那裡」不可分辨。"
                "`(until canceled)` 之取消側未驗 —— 條文未說取消後選擇何時清除，"
                "依 §8.4.1 不推定。"
                "`(if applicable)` 為適用條件：第一步無前一步，"
                "故本條自第二步（username）發起。",
        reasoning=(
            "驗證目標：8.12（NEWPR11）—— 設定流程中之返回鍵回到上一步，"
            "並保留已做之選擇。"
            "關鍵情境條件：上一步須已有輸入且已記錄。"
            "為什麼這樣切：`design_method` 取狀態轉換 ——"
            "`design_method` 取功能測試而非狀態轉換："
            "所驗者為**值之保留**，畫面之來回不是系統狀態之遷移（K-4a）。"),
        kw=["back arrow", "previous step", "selections", "retained"],
    ),
}


def build() -> list:
    rows = B.leaf_rows()
    missing = [r for r in SAMPLE if r not in TCS]
    extra = [r for r in TCS if r not in SAMPLE]
    if missing or extra:
        raise SystemExit(f"取樣清單與內容不一致：缺 {missing}／多 {extra}")

    out, n = [], TC_START
    for req_id in SAMPLE:
        ctx = B.assemble(req_id, rows[req_id])
        spec = TCS[req_id]
        prio, why = PRIORITY[req_id]
        refs = ctx["specification_reference"]
        for sec, _provides in REF_EXTRA.get(req_id, []):
            refs += f"; {B.SPEC_STEM}_{sec}"
        rec = _rec(req_id, ctx, spec, refs, prio, why, n)
        rec["batch"] = "batch06"
        out.append(rec)
        n += 1
    return out


if __name__ == "__main__":
    OUT.mkdir(exist_ok=True)
    recs = build()
    for r in recs:
        (OUT / f"{r['parent']}.json").write_text(
            json.dumps(r, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8")
    print(f"寫出 {len(recs)} 個檔，共 {sum(len(r['tcs']) for r in recs)} 條 TC "
          f"（{recs[0]['tcs'][0]['tc_id']} … {recs[-1]['tcs'][0]['tc_id']}）")
