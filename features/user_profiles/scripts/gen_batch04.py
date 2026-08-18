#!/usr/bin/env python3
"""第四批之生成器（34 包）—— ch5 之 `PRACC` 群（5.1–5.10.1），tc_id 109–134。

## 批界

**第四批 ＝ ch5 之 `PRACC7`–`PRACC16.1` 共 25 leaf ＋ `030-01` 之反向配對 1
＝ 26 條。** 批界依 spec 自己的條款家族線（5.12 起變 `ALLPR`），
非我方所畫（34 包 §一）。

## 條數之更正（**下放包沿用了我 29 輪之措辭錯誤**）

34 包寫「25 leaf ＋ 2 額外造者（`030-01` 反向、`041-04` 故障注入），估 26 條」。
**其中 `041-04` 不屬本批** —— 它是 `5.13.2` 之 leaf，落在 `ALLPR` 群（第五批）；
且它本身就是一個 leaf，其 TC 是「一葉一 TC」而非額外造者。

成因在我 29 輪 §3.2 之寫法：我把 `041-04` 與 `030-01` 之反向並列為
「另須額外造者」，**而前者只是一個需要故障注入之 leaf**，不是額外的一條。
故該處之「38 ＋ 2 ＝ 40」多算了一條。

**本批以 25 leaf ＋ 1 額外造者 ＝ 26 條執行** —— 與下放包所載之
「估 26 條」及「5.1–5.10.1」之範圍一致，只有「2 額外造者」那個標籤是錯的。
`041-04` 之故障注入留待第五批。
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build_batch_context as B                       # noqa: E402
from gen_pilot import (steps, FUNCTIONAL, STATE,       # noqa: E402
                       NEGATIVE, SCENARIO)
from gen_batch01 import _rec                           # noqa: E402

FEATURE = Path(__file__).resolve().parent.parent
OUT = FEATURE / "generated"
TC_START = 109

SAMPLE = [
    "SWE1-HMI-PROF-018-01", "SWE1-HMI-PROF-018-02", "SWE1-HMI-PROF-018-03",
    "SWE1-HMI-PROF-019",
    "SWE1-HMI-PROF-020-01", "SWE1-HMI-PROF-020-02",
    "SWE1-HMI-PROF-021-02", "SWE1-HMI-PROF-021-03",
    "SWE1-HMI-PROF-022", "SWE1-HMI-PROF-023", "SWE1-HMI-PROF-024",
    "SWE1-HMI-PROF-025", "SWE1-HMI-PROF-026",
    "SWE1-HMI-PROF-027-01", "SWE1-HMI-PROF-027-02", "SWE1-HMI-PROF-027-03",
    "SWE1-HMI-PROF-028", "SWE1-HMI-PROF-029",
    "SWE1-HMI-PROF-030-01", "SWE1-HMI-PROF-030-02",
    "SWE1-HMI-PROF-031", "SWE1-HMI-PROF-033",
    "SWE1-HMI-PROF-034-01", "SWE1-HMI-PROF-034-02", "SWE1-HMI-PROF-034-03",
]

PRIORITY = {
    "SWE1-HMI-PROF-018-01": ("P2", "Profile 區之預設分頁；導覽之呈現"),
    "SWE1-HMI-PROF-018-02": ("P1", "分頁選擇之跨 key cycle 記憶；逐 profile 之狀態保留"),
    "SWE1-HMI-PROF-018-03": ("P3", "再按 Profile 鍵之回位；罕用導覽"),
    "SWE1-HMI-PROF-019": ("P1", "All Profiles 主畫面之內容與三個入口"),
    "SWE1-HMI-PROF-020-01": ("P2", "profile 專屬設定圖示與其說明字串之常駐"),
    "SWE1-HMI-PROF-020-02": ("P2", "設定畫面內各 profile 專屬項之圖示標示"),
    "SWE1-HMI-PROF-021-02": ("P1", "達上限時新增入口之隱藏；上限管理之分支"),
    "SWE1-HMI-PROF-021-03": ("P2", "達上限時之替代文字（PU0584）"),
    "SWE1-HMI-PROF-022": ("P0", "自 All Profiles 分頁切換 profile —— R-U5 核心五類之一"),
    "SWE1-HMI-PROF-023": ("P2", "切換過程之載入訊息與 welcome popup"),
    "SWE1-HMI-PROF-024": ("P2", "切換後之分頁停留"),
    "SWE1-HMI-PROF-025": ("P1", "載入中不得再選另一 profile；避免載入競態"),
    "SWE1-HMI-PROF-026": ("P2", "自現用 profile 進入 Edit Profile 之入口"),
    "SWE1-HMI-PROF-027-01": ("P2", "記憶座椅編號於 avatar 下之呈現"),
    "SWE1-HMI-PROF-027-02": ("P1", "profile 數超過座椅數時之預設不連結"),
    "SWE1-HMI-PROF-027-03": ("P1", "Valet Mode Profile 不得連結座椅位置"),
    "SWE1-HMI-PROF-028": ("P0", "自 All Profiles 分頁建立新 profile —— 核心五類之一"),
    "SWE1-HMI-PROF-029": ("P0", "行車中不得新增 profile —— **防線成立本身**"
                                "（§10.2 safety；D-UP16-01 附二）"),
    "SWE1-HMI-PROF-030-01": ("P1", "座椅連結之唯一入口；連結途徑之限制"),
    "SWE1-HMI-PROF-030-02": ("P1", "存座椅位置不得自動連到現用 profile"),
    "SWE1-HMI-PROF-031": ("P0", "行車中座椅不得移動 —— **防線成立本身**（§10.2 safety）"),
    "SWE1-HMI-PROF-033": ("P1", "存座椅位置之歸屬；儲存機制之對象判定"),
    "SWE1-HMI-PROF-034-01": ("P2", "跨 profile 存座椅時之詢問（PU0588）"),
    "SWE1-HMI-PROF-034-02": ("P1", "改派後之座椅歸屬（現用 profile 原無座椅）"),
    "SWE1-HMI-PROF-034-03": ("P1", "改派後之座椅歸屬（現用 profile 原有座椅）"),
}

ICON_STRING = ("This icon is associated to settings that are specific to your "
               "profile and are not shared across the vehicle")

# 5.2 之條文以**指涉**帶入該字串（`the icon and the string described in note
# PRACC7.2`），未逐字重複。ER 逐字寫出時，其來源節須併列（D-UP12-02／D-3 之先例），
# 且 J-10 要求該節之 `provides` 字面值確實出現在該 TC 內 —— 此處即 ICON_STRING。
REF_EXTRA = {
    "SWE1-HMI-PROF-021-02": [("5.1.2", ICON_STRING)],
    # X-1（35 包）：`030-02` 之 procedure 須處理 5.10.1 之 PU0588，
    # 該字面值遂出現於本 TC —— 依 J-10 登記其來源節。
    "SWE1-HMI-PROF-030-02": [("5.10.1", "PU0588")],
}

TCS = {

    # ── 5.1 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-018-01": dict(
        title="All Profiles is the default tab of the Profile section",
        design=FUNCTIONAL,
        pre=steps("The active Driver Profile has never opened the Profile "
                  "section on this vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the Profile button in the status bar",
                   "Read the Profile section and check that the “All Profiles” tab is shown"),
        er=steps("The Profile section is opened",
                 "The “All Profiles” tab is the tab shown"),
        remarks="pre-condition 指定「該 profile 從未開過 Profile 區」——"
                "**否則 5.1 之 latch 行為（`SWE1-HMI-PROF-018-02`）會蓋過預設值**，"
                "測到的將是上次之分頁而非預設分頁。",
        reasoning=(
            "驗證目標：5.1（PRACC7）—— Profile 區之**預設**分頁為 "
            "“All Profiles”。"
            "關鍵情境條件：latch 行為以「上次用過之分頁」為準，"
            "故須以「從未開過」排除之，預設值方可觀察。"
            "為什麼這樣切：037 對 5.1 切三個 leaf；本 leaf 之單位為**預設值**，"
            "latch 屬 `SWE1-HMI-PROF-018-02`、再按回位屬 `SWE1-HMI-PROF-018-03`。"),
        kw=["default tab", "All Profiles", "Profile section"],
    ),

    "SWE1-HMI-PROF-018-02": dict(
        title="Last used tab remembered per Profile across key cycles",
        design=STATE,
        pre=steps("Two Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Activate Driver Profile A and open the “Edit Profile” tab",
                   "Switch the ignition off and then on again",
                   "Press the Profile button and check that the “Edit Profile” tab is shown"),
        er=steps("Driver Profile A is active and the “Edit Profile” tab is "
                 "shown",
                 "The ignition is off and then on again with Driver Profile "
                 "A active",
                 "The “Edit Profile” tab is shown"),
        remarks="條文之 latch 有兩個範圍（`within and over key cycles`）與一個"
                "**逐 profile** 之限定。本 TC 取**跨 key cycle** 一側 ——"
                "其為兩者中較難成立者（同一 key cycle 內之保留為其必要條件）。"
                "**逐 profile 之隔離未於本條驗**：另一 profile 之分頁是否互不影響，"
                "條文有述而 037 未為其另切 leaf ——依 **R-U56** 為 OUT-OF-SCOPE，"
                "不列缺口。",
        reasoning=(
            "驗證目標：5.1（PRACC7）之 latch —— 系統記住上次使用之分頁，"
            "跨 key cycle 仍然有效。"
            "關鍵情境條件：**須先離開預設分頁**（開 “Edit Profile”），"
            "否則 latch 與預設值之結果相同，無從分辨。"
            "為什麼這樣切：取跨 key cycle 一側；**若只驗同一 key cycle 內之保留，"
            "一個把分頁存在揮發性記憶體之實作會通過**。"),
        kw=["latch", "last used tab", "key cycle", "per Profile"],
    ),

    "SWE1-HMI-PROF-018-03": dict(
        title="Pressing the Profile button again returns to All Profiles",
        design=FUNCTIONAL,
        pre=steps("The Profile section is open on the “Edit Profile” tab",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the Profile button in the status bar",
                   "Read the Profile section and check that the “All Profiles” tab is shown"),
        er=steps("The Profile button is pressed while the “Edit Profile” tab "
                 "is open",
                 "The “All Profiles” tab is shown"),
        remarks="條文之 `if not already on that tab` 為適用條件；"
                "本 TC 以 pre-condition 固定為「不在該分頁」，使回位可觀察。"
                "已在該分頁時再按之行為條文未述，依 §8.4.1 不推定。",
        reasoning=(
            "驗證目標：5.1（PRACC7）末句 —— 於 Profile 區內再按 Profile 鍵，"
            "回到 “All Profiles” 分頁。"
            "關鍵情境條件：起始須**不在**該分頁（§8.7.3 之條件本身）。"
            "為什麼這樣切：本 leaf 之單位為**再按之回位**；"
            "首次進入之分頁判定屬 `SWE1-HMI-PROF-018-01` 與 "
            "`SWE1-HMI-PROF-018-02`。"),
        kw=["Profile button", "All Profiles", "return", "tab"],
    ),

    # ── 5.1.1 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-019": dict(
        title="All Profiles tab shows every user and the three options",
        design=FUNCTIONAL,
        pre=steps("Three Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the user list and check that every Profile is shown",
                   "Read the screen and check the three options offered"),
        er=steps("The “All Profiles” tab is displayed",
                 "All three Driver Profiles are shown and the active one is "
                 "highlighted and larger than the others",
                 "Options to add a new Profile, to switch the active Profile "
                 "and to enter Valet Mode are present"),
        remarks="**ER2 併驗 highlighted 與 larger 兩者** —— 條文寫的是"
                "`highlighted **and** larger than the others`；"
                "只驗其一，另一半失效不會被發現。"
                "profile 數（3）為**測試設置**（J-12）：條文只寫 all available "
                "users，未指定數目；取 3 是為使「其他人」為複數。",
        reasoning=(
            "驗證目標：5.1.1（PRACC7.1）—— All Profiles 分頁顯示全部使用者、"
            "現用者放大並 highlight，並提供三個入口。"
            "關鍵情境條件：至少三個 profile，使「其他人」為複數，"
            "`larger than the others` 方為可觀察之比較。"
            "為什麼這樣切：三個入口為同一畫面之並列斷言，依 §5.7 併為一條之 ER3。"
            "刻意略過：各入口按下後之行為分屬 5.3／5.6／12.x，本條只驗其**存在**。"),
        kw=["All Profiles", "highlighted", "larger", "options"],
    ),

    # ── 5.1.2 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-020-01": dict(
        title="Profile-specific settings icon and string always on All Profiles",
        design=FUNCTIONAL,
        pre=steps("The vehicle screen is larger than 7 inches",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the screen and check the icon and its string"),
        er=steps("The “All Profiles” tab is displayed",
                 f"An icon is shown together with the string “{ICON_STRING}”"),
        remarks="條文末句 `This logic is not applicable for 7” screens` 為"
                "**適用條件**（M-3 之三分法，非覆寫），故以 pre-condition 排除 7 吋。"
                "037 之 leaf 標題亦已載 `Large Screens`。"
                "字串逐字引自 5.1.2，未改寫（§8.4.1）。",
        reasoning=(
            "驗證目標：5.1.2（PRACC7.2）前半 —— “All Profiles” 畫面**恆**顯示"
            "該圖示與其字串。"
            "關鍵情境條件：螢幕大於 7 吋，否則本條不適用。"
            "為什麼這樣切：037 對 5.1.2 切兩個 leaf —— 本 leaf 為 **All Profiles "
            "畫面上之常駐**，設定畫面內之標示屬 `SWE1-HMI-PROF-020-02`。"),
        kw=["icon", "string", "All Profiles", "7 inch"],
    ),

    "SWE1-HMI-PROF-020-02": dict(
        title="Profile-tied settings marked with the icon in the settings screen",
        design=FUNCTIONAL,
        pre=steps("The vehicle screen is larger than 7 inches",
                  "At least one profile-tied setting exists in the “My "
                  "Profile” tab and one in another tab"),
        data="NA",
        proc=steps("Open the settings screen and the “My Profile” tab",
                   "Read the profile-tied setting and check for the icon",
                   "Open another settings tab and check that its profile-tied "
                   "setting carries the icon"),
        er=steps("The settings screen is displayed on the “My Profile” tab",
                 "The profile-tied setting carries the icon",
                 "The profile-tied setting in the other tab also carries the "
                 "icon"),
        remarks="條文明言 `both inside the My Profile tab **and all the other "
                "tabs**` —— **ER 兩處併驗**：只驗 My Profile 一處，"
                "一個只在該分頁標圖示之實作會通過。",
        reasoning=(
            "驗證目標：5.1.2（PRACC7.2）後半 —— 設定畫面內所有繫於 profile 之"
            "設定項皆標該圖示，涵蓋 “My Profile” 分頁與其他分頁。"
            "關鍵情境條件：pre-condition 要求兩個分頁**各有**一個 profile 專屬設定，"
            "否則「其他分頁」一側無從觀察。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-020-01` 之分野在**位置** ——"
            "前者為 All Profiles 畫面之常駐，本條為設定畫面內之逐項標示。"),
        kw=["icon", "settings", "My Profile", "profile-tied"],
    ),

    # ── 5.2 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-021-02": dict(
        title="Add New button and icon hidden at the maximum Profile count",
        design=FUNCTIONAL,
        pre=steps("Five Driver Profiles exist on the vehicle",
                  "The vehicle screen is larger than 7 inches"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the screen and check that the Add New Profile "
                   "button and the icon are absent"),
        er=steps("The “All Profiles” tab is displayed",
                 f"No Add New Profile button is present and neither the icon "
                 f"nor the string “{ICON_STRING}” is shown"),
        remarks="**ER 併驗按鈕與圖示／字串兩者** —— 條文寫的是"
                "`the Add New Profile button will not be present, **and** the "
                "icon and the string described in note PRACC7.2 will not be "
                "present either`。"
                "螢幕尺寸之 pre-condition 為使「圖示原本會在」成立"
                "（5.1.2 於 7 吋不適用）—— **否則圖示不在是因為螢幕，不是因為上限**。",
        reasoning=(
            "驗證目標：5.2（PRACC8）之中段 —— 達 5 個 profile 上限時，"
            "新增按鈕與 PRACC7.2 之圖示／字串皆不顯示。"
            "關鍵情境條件：螢幕須大於 7 吋 —— **這一點是本條之關鍵**："
            "7 吋螢幕上該圖示本來就不顯示（5.1.2），"
            "屆時「圖示不在」證不了任何事。"
            "為什麼這樣切：037 對 5.2 切三個 leaf；上限之**數目**屬 "
            "`SWE1-HMI-PROF-021-01`（`NR1L-UserProfiles-003`），"
            "替代文字屬 `SWE1-HMI-PROF-021-03`。"),
        kw=["max profiles", "Add New", "icon hidden", "five"],
    ),

    "SWE1-HMI-PROF-021-03": dict(
        title="Max Profiles reached text shown in place of the Add New entry",
        design=FUNCTIONAL,
        pre=steps("Five Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the screen and check the text shown in place of the "
                   "Add New entry"),
        er=steps("The “All Profiles” tab is displayed",
                 "The text “Max Profiles reached. Delete to create a new "
                 "one.” (PU0584) is displayed"),
        remarks="字串與 PU id 逐字引自 5.2。"
                "與 `SWE1-HMI-PROF-021-02` 之分野：該條驗**什麼不見了**，"
                "本條驗**取而代之顯示了什麼** —— 兩者為同一情境之兩個斷言，"
                "037 切兩個 leaf 故不合併（§8.2.1）。",
        reasoning=(
            "驗證目標：5.2（PRACC8）末句 —— 達上限時改顯示一段告知使用者"
            "須先刪除之文字。"
            "關鍵情境條件：五個 profile 已存在（上限本身）。"
            "為什麼這樣切：**只驗「按鈕不見了」，一個什麼都不顯示之實作會通過** ——"
            "條文要求的是**替代顯示**，故本條必須獨立於 `021-02`。"),
        kw=["PU0584", "Max Profiles reached", "text", "five"],
    ),

    # ── 5.3 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-022": dict(
        title="Selecting another Profile switches to it and highlights it",
        design=STATE,
        pre=steps("Two Driver Profiles exist and Driver Profile A is active",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and record which Profile is "
                   "highlighted",
                   "Select the username of Driver Profile B",
                   "Read the tab and check that Driver Profile B is active "
                   "and highlighted"),
        er=steps("Driver Profile A is highlighted and recorded as the active "
                 "Profile",
                 "Driver Profile B is selected",
                 "Driver Profile B is the active Profile and is highlighted "
                 "instead of the Profile recorded in step 1"),
        remarks="條文之選取對象為 `Profile username **or** avatar` ——"
                "本 TC 取 username 一側；avatar 一側之觸發相同而**入口不同**，"
                "條文以 or 並列，**未另切 leaf**，故不另生成（§8.2.1）。"
                "**ER3 併驗「不再是步驟 1 所記者」** —— 只驗 B 被 highlight，"
                "一個把兩者都 highlight 之實作會通過。",
        reasoning=(
            "驗證目標：5.3（PRACC9）—— 於 All Profiles 分頁選取另一 profile，"
            "系統切換至該 profile 且其進入 highlight 狀態。"
            "關鍵情境條件：步驟 1 記錄原本被 highlight 者，"
            "使「highlight 移轉」而非「本來就 highlight」可分辨（§5.6）。"
            "為什麼這樣切：切換之**後續呈現**（載入訊息與 welcome popup）屬 "
            "`SWE1-HMI-PROF-023`；分頁停留屬 `SWE1-HMI-PROF-024`。"),
        kw=["switch Profile", "highlighted", "All Profiles", "select"],
    ),

    # ── 5.3.1 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-023": dict(
        title="Loading message then welcome popup shown after a switch",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist and the welcome popup is turned "
                  "on for Driver Profile B",
                  "Driver Profile A is active and the vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and select Driver Profile B",
                   "Read the screen and check that the Profile loading "
                   "message is shown",
                   "Read the screen after loading and check the welcome "
                   "popup and how long it stays"),
        er=steps("Driver Profile B is selected",
                 "The Profile loading message is shown",
                 "The welcome popup PU0580 for Driver Profile B is shown for "
                 "5 seconds"),
        remarks="條文之 `(if turned on for that Profile)` 為適用條件，"
                "以 pre-condition 固定為已開啟 —— 否則 popup 不出現而本條假失敗。"
                "**順序為條文所載**（loading **then** welcome），ER2／ER3 依序斷言。"
                "`5 seconds` 與 `PU0580` 逐字引自 5.3.1。",
        reasoning=(
            "驗證目標：5.3.1（PRACC9.1）—— 切換後先顯示載入訊息，"
            "再顯示該 profile 之 welcome popup，持續 5 秒。"
            "關鍵情境條件：目標 profile 之 welcome popup 須為開啟狀態。"
            "為什麼這樣切：**兩個顯示之先後是條文明載者**，"
            "故 ER 分兩條依序斷言；併為一條會失去順序（同 `TC-088` 之理由）。"
            "刻意略過：條文之 `which is different than on vehicle entry` "
            "為對照說明，其另一情境屬 ch7 之 welcome flow。"),
        kw=["loading message", "welcome popup", "PU0580", "5 seconds"],
    ),

    # ── 5.3.2 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-024": dict(
        title="Screen stays on All Profiles after switching Profile",
        design=FUNCTIONAL,
        pre=steps("Two Driver Profiles exist and the last used tab of Driver "
                  "Profile B is the “Edit Profile” tab",
                  "Driver Profile A is active and the vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and select Driver Profile B",
                   "Read the screen and check that the “All Profiles” tab is shown"),
        er=steps("Driver Profile B is the active Profile",
                 "The “All Profiles” tab is still shown"),
        remarks="**pre-condition 之「B 之上次分頁為 Edit Profile」是本條之關鍵** ——"
                "條文括號明言 `even if last known Profile tab was “Edit Profile” "
                "for newly active Profile`；不設此前提，"
                "本條與 latch（`SWE1-HMI-PROF-018-02`）之結果無從分辨。",
        reasoning=(
            "驗證目標：5.3.2（PRACC9.2）—— 於 All Profiles 分頁切換 profile 後，"
            "畫面仍停留在 All Profiles 分頁。"
            "關鍵情境條件：新 profile 之 latch 分頁**須為 Edit Profile** ——"
            "那是條文括號所指之情形，**也是唯一能證明本條之情境**："
            "若 B 之上次分頁本來就是 All Profiles，停留與 latch 之結果相同。"
            "為什麼這樣切：本條與 `SWE1-HMI-PROF-018-02` 為**互相衝突之兩條規則**，"
            "037 各切一個 leaf；本條驗的是「切換情境下 5.3.2 勝過 latch」。"),
        kw=["All Profiles", "stay", "switch", "latch"],
    ),

    # ── 5.3.3 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-025": dict(
        title="Selecting another Profile blocked while one is loading",
        design=NEGATIVE,
        pre=steps("Three Driver Profiles exist on the vehicle",
                  "Driver Profile A is active and the vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and select Driver Profile B",
                   "Attempt to select Driver Profile C while Driver Profile "
                   "B is still loading",
                   "Read the screen and check which Profile becomes active"),
        er=steps("Driver Profile B is selected and starts loading",
                 "The attempt to select Driver Profile C is not accepted",
                 "Driver Profile B is the active Profile"),
        remarks="**ER3 併驗「最後作用中者為 B」** —— 只驗「C 之選取不被接受」，"
                "一個把選取吞掉卻仍切到 C 之實作會通過。"
                "三個 profile 為**測試設置**（J-12）：條文只寫 another profile，"
                "取三個是為使「載入中之目標」與「被擋之目標」為不同兩者。",
        reasoning=(
            "驗證目標：5.3.3（PRACC9.3）—— 一個 profile 載入期間，"
            "使用者不能再選另一個。"
            "關鍵情境條件：須有第三個 profile 作為被擋之對象，"
            "否則「再選一個」與「重選同一個」混淆。"
            "為什麼這樣切：受測動作為載入期間之選取（§12 首匹配 → 負向測試）。"
            "刻意略過：載入之時長條文未述，本條不對其設限（§8.4.1）。"),
        kw=["loading", "blocked", "select", "another Profile"],
    ),

    # ── 5.4 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-026": dict(
        title="Pressing the active Profile opens the Edit Profile tab",
        design=FUNCTIONAL,
        pre=steps("Driver Profile A is active and highlighted on the “All "
                  "Profiles” tab",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Press the avatar of the active Driver Profile",
                   "Read the screen and check which tab is shown"),
        er=steps("The avatar of the active Driver Profile is pressed",
                 "The “Edit Profile” tab is displayed"),
        remarks="條文首句 `Editing a Profile is **only** available for the "
                "active Profile` 為**全稱限制**。"
                "其反向由 `SWE1-HMI-PROF-022` 承擔 —— 該 leaf 驗"
                "「選取另一個 profile 會 switch system to that Profile」，"
                "即「不進入編輯」之另一面。",
        reasoning=(
            "驗證目標：5.4（PRACC10）後半 —— 於 All Profiles 分頁按下**已作用中且"
            "已 highlight** 之 profile，進入 “Edit Profile” 分頁。"
            "關鍵情境條件：條文明言 `after that Profile is already active and "
            "highlighted`，故 pre-condition 固定之。"
            "為什麼這樣切：**「只能編輯現用 profile」之限制不另立 TC** ——"
            "按非現用者之行為由 5.3 定義為切換，"
            "`SWE1-HMI-PROF-022` 已驗其確實切換而非進入編輯。"),
        kw=["Edit Profile", "active Profile", "avatar", "press"],
    ),

    # ── 5.5 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-027-01": dict(
        title="Memory seat number shown under the linked Profile avatar",
        design=FUNCTIONAL,
        pre=steps("The vehicle is equipped with memory seats",
                  "Driver Profile A is linked to a memory seat position"),
        data="NA",
        proc=steps("Open the “All Profiles” tab",
                   "Read the area under the avatar of Driver Profile A and "
                   "check the memory seat number shown"),
        er=steps("The “All Profiles” tab is displayed",
                 "The memory seat number linked to Driver Profile A is shown "
                 "under its avatar"),
        remarks="ER 不寫座椅編號之數值 —— 條文只述「顯示哪一個座椅編號連到哪一個 "
                "profile」，**未指定編號**；寫死數值會使本 TC 只能在特定佈署上跑。",
        reasoning=(
            "驗證目標：5.5（PRACC11）首句 —— 每個適用 profile 之 avatar 下方"
            "顯示其所連之記憶座椅編號。"
            "關鍵情境條件：至少一個 profile 已連座椅，否則無可顯示者。"
            "為什麼這樣切：037 對 5.5 切三個 leaf —— 本 leaf 為**呈現**；"
            "超出座椅數之預設不連結屬 `SWE1-HMI-PROF-027-02`，"
            "Valet 之限制屬 `SWE1-HMI-PROF-027-03`。"),
        kw=["memory seat number", "avatar", "linked", "display"],
    ),

    "SWE1-HMI-PROF-027-02": dict(
        title="New Profile gets no memory seat when seats are outnumbered",
        design=FUNCTIONAL,
        pre=steps("The vehicle has 3 memory seats and each is linked to a "
                  "Driver Profile",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Create one more Driver Profile",
                   "Open the “All Profiles” tab",
                   "Read the area under the new Profile avatar and check its "
                   "memory seat status"),
        er=steps("The new Driver Profile is created",
                 "The “All Profiles” tab is displayed",
                 "No memory seat is linked to the new Driver Profile"),
        remarks="座椅數（3）取自條文之 `currently up to 3`，非自擬。"
                "條文另載 `unless the user initiates a swap of Memory seat "
                "preferences` —— 該互換屬 9.5.x 之 leaf，本條不代測。",
        reasoning=(
            "驗證目標：5.5（PRACC11）中段 —— profile 數超過車上記憶座椅數時，"
            "新建之 profile 預設不連任何座椅。"
            "關鍵情境條件：**全部座椅皆已被連走**，"
            "否則新 profile 不連座椅可能只是因為還有空位。"
            "為什麼這樣切：本 leaf 之單位為**新 profile 之預設不連結**；"
            "互換之途徑屬他節，具名不代測。"),
        kw=["memory seats", "exceed", "no link", "new Profile"],
    ),

    "SWE1-HMI-PROF-027-03": dict(
        title="Valet Mode Profile cannot be linked to a memory seat",
        design=NEGATIVE,
        pre=steps("The vehicle is equipped with memory seats",
                  "A Valet Mode Profile is present and at least one memory "
                  "seat is unlinked"),
        data="NA",
        proc=steps("Open the “Edit Profile” screen for the Valet Mode Profile",
                   "Attempt to link the unlinked memory seat to the Valet "
                   "Mode Profile",
                   "Read the seat links and check that the Valet Mode "
                   "Profile holds none"),
        er=steps("The Valet Mode Profile screen is displayed",
                 "The attempt is not accepted",
                 "No memory seat position is linked to the Valet Mode Profile"),
        remarks="**ER3 斷言「一個都沒有」而非「這一個沒連上」** ——"
                "後者容許實作改連到別的座椅位置，那同樣違反條文"
                "（同 `NR1L-UserProfiles-105` 之形狀）。"
                "若該畫面根本不提供連結入口，步驟 2 之「嘗試」即為「找不到入口」，"
                "ER2 仍成立 —— **條文說的是不得連結，未規定以何種方式阻止**。",
        reasoning=(
            "驗證目標：5.5（PRACC11）末句 —— Valet Mode Profile 不得連結"
            "記憶座椅位置。"
            "關鍵情境條件：須有未被連走之座椅，否則「不得連」與「沒得連」混淆。"
            "為什麼這樣切：受測動作為一個**不被允許之連結**（§12 首匹配 → 負向）。"
            "**ER3 為全稱形式**：該 profile 之座椅連結數恆為零。"),
        kw=["Valet Mode Profile", "memory seat", "not allowed", "link"],
    ),

    # ── 5.6 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-028": dict(
        title="New Profile setup from All Profiles ends on that tab",
        design=SCENARIO,
        pre=steps("Fewer than five Driver Profiles exist on the vehicle",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Open the “All Profiles” tab and press the “Add New” text",
                   "Complete the new Profile setup process",
                   "Read the active Profile and check that it is the new one",
                   "Read the screen and check that the “All Profiles” tab is shown"),
        er=steps("The new Profile setup process is initiated",
                 "The new Profile setup is completed",
                 "The new Driver Profile is the active Profile",
                 "The “All Profiles” tab is shown"),
        remarks="條文三句為**同一次流程之三個結果**（啟動／成為現用／回到該分頁），"
                "依 §5.7 併為一條；其跨越四個步驟與兩個功能（建立與導覽），"
                "故 design_method 取情境／用例（§12）。"
                "`“Add New”` 與 `“+”` 為條文並列之兩個入口，本 TC 取前者；"
                "後者之觸發相同，**037 未另切 leaf**，故不另生成。",
        reasoning=(
            "驗證目標：5.6（PRACC12）—— 自 All Profiles 分頁啟動新 profile 設定，"
            "完成後新 profile 成為現用者，且畫面回到 All Profiles 分頁。"
            "關鍵情境條件：profile 數須未達上限，否則入口不存在（5.2）。"
            "為什麼這樣切：**ER3 與 ER4 缺一不可** ——"
            "只驗「回到分頁」，一個沒把新 profile 設為現用之實作會通過；"
            "只驗「成為現用」，一個停在設定畫面之實作會通過。"),
        kw=["Add New", "setup", "active Profile", "All Profiles"],
    ),

    # ── 5.6.1 ─────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-029": dict(
        title="Add New greyed out and blocked while the vehicle moves",
        design=NEGATIVE,
        pre=steps("Fewer than five Driver Profiles exist on the vehicle",
                  "The “All Profiles” tab is open"),
        data="NA",
        proc=steps("Read the “Add New” text and record whether it is "
                   "selectable",
                   "Bring the vehicle into motion",
                   "Select the greyed-out “Add New” text and check that a bonk "
                   "tone and a message are given"),
        er=steps("The “Add New” text is selectable and its state is recorded",
                 "The vehicle is in motion and the “Add New” text is greyed "
                 "out",
                 "The selection is not accepted, a bonk tone is played and "
                 "the message “Function not available while vehicle in "
                 "Motion.” is displayed"),
        remarks="**ER3 併驗「不被接受」與「提示」兩者** —— 依 P-1 之分野"
                "（§8.7.4：視覺狀態不蘊含不可操作），**變灰本身不是防線**；"
                "**防線是「按下不生效」**，故其斷言不可省。"
                "訊息字串逐字引自 5.6.1。基準線（行車前可選）為 §5.6 之要求。",
        reasoning=(
            "驗證目標：5.6.1（PRACC12.1）—— 行車中 “Add New” 變灰；"
            "若被選取則播 bonk 並顯示不可用訊息。"
            "關鍵情境條件：步驟 1 之基準線使「變灰」與「本來就不可選」可分辨（§5.6）。"
            "為什麼這樣切：受測動作為對已變灰項目之按壓（§12 首匹配 → 負向測試）。"
            "**判級 P0**：行車中不得新增 profile 為分心防線，"
            "其**成立本身**（按下不生效）之斷言落在 ER3 前半（D-UP16-01 附二）。"),
        kw=["Add New", "greyed out", "bonk", "in motion"],
    ),

    # ── 5.7 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-030-01": dict(
        title="Memory seat linked to a Profile from the Edit Profile screen",
        design=FUNCTIONAL,
        pre=steps("Driver Profile A is active and has no memory seat linked",
                  "At least one memory seat position is unlinked"),
        data="NA",
        proc=steps("Open the “Edit Profile” screen for Driver Profile A",
                   "Link the unlinked memory seat position to Driver Profile A",
                   "Read the seat links and check that the position is linked "
                   "to Driver Profile A"),
        er=steps("The “Edit Profile” screen is displayed",
                 "The link is accepted",
                 "The memory seat position is linked to Driver Profile A"),
        remarks="§7 之列舉配對：反向為 `NR1L-UserProfiles-133`"
                "（自 Edit Profile 以外之途徑連結不成立）。"
                "條文之 `can **only** be done through the Edit Profile screen` "
                "為**全稱限制** —— **只驗此處連得成，不足以證「只能」**。"
                "`(unless it is linked by default)` 為適用條件，"
                "以 pre-condition 之「A 尚未連任何座椅」排除預設連結之情形。",
        reasoning=(
            "驗證目標：5.7（PRACC13）首句之正向 —— 經 Edit Profile 畫面可將"
            "profile 連結至記憶座椅。"
            "關鍵情境條件：A 尚未連座椅且有空位，使連結之效果可觀察。"
            "為什麼這樣切：條文之限制詞為 `only`，**其反向由 "
            "`NR1L-UserProfiles-133` 承擔**；兩條並存才擋得住"
            "一個允許自他處連結之實作（§7）。"),
        kw=["Edit Profile", "link", "memory seat", "only"],
    ),

    "SWE1-HMI-PROF-030-02": dict(
        title="Saving a seat position does not link it to the active Profile",
        design=FUNCTIONAL,
        pre=steps("Driver Profile A is active and has no memory seat linked",
                  "A memory seat position is linked to Driver Profile B"),
        data="NA",
        # **X-1（35 包）**：步驟 2 之動作正是 5.10.1 之觸發條件 ——
        # 存到**非現用 profile 所連**之座椅時 **PU0588 會跳出來問**。
        # 原 procedure 完全沒提它，測試者會撞上未預期之 popup，
        # **而結果取決於他按了什麼**（選 Yes 則該座椅就會連到 A，與 ER3 相反）。
        # 兩條條文不衝突：5.7 之 `not **automatically**` 是「不經詢問即發生」，
        # 5.10.1 是「問過且答 Yes 才發生」—— **衝突的是 TC 之寫法**。
        # 加一步明確選 No，「不自動」方為**被觀察到的**而非碰運氣。
        proc=steps("Change the seat position",
                   "Save the position to the memory seat linked to Driver "
                   "Profile B",
                   "Select No on PU0588",
                   "Read the seat links and check that Driver Profile A still "
                   "has none"),
        er=steps("The seat position is changed",
                 "The position is saved to the memory seat linked to Driver "
                 "Profile B and PU0588 is displayed",
                 "No is selected on PU0588",
                 "No memory seat is linked to Driver Profile A"),
        remarks="條文之 `it will not automatically save to the active Profile` "
                "為**缺席斷言**；其正向（存到原本連結之 profile）屬 "
                "`SWE1-HMI-PROF-033`（5.10）。"
                "本條之 pre-condition 使 A（現用）原本無座椅 ——"
                "**若 A 本來就有座椅，「沒有自動連過去」無從觀察**。"
                "**X-1（35 包）**：步驟 2 會觸發 5.10.1 之 **PU0588**，"
                "故 procedure 明確選 **No** —— 其 Yes 之後果由 "
                "`SWE1-HMI-PROF-034-02` 驗。"
                "**不處理該 popup，本條之結果取決於測試者按了什麼**（§2）。"
                "引用欄併列 **5.10.1**：PU0588 之字面值出現於本 TC，"
                "依 J-10 須登記其來源節。",
        reasoning=(
            "驗證目標：5.7（PRACC13）末句 —— 儲存座椅位置時，"
            "不會自動把該位置連到現用 profile。"
            "關鍵情境條件：現用 profile 原本**無**座椅連結，"
            "使「自動連過去」若發生即可見。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-033` 之分野在斷言方向 ——"
            "該條驗**存到誰**（原連結者），本條驗**沒存到誰**（現用者）。"
            "**PU0588 之處理（X-1）**：本條之情境同時滿足 5.10.1 之觸發，"
            "故必須明確答 No —— **5.7 說的是「不經詢問即自動發生」，"
            "而非「詢問後也不發生」**；答 Yes 之路徑屬 5.10.1，不在本條。"),
        kw=["save seat", "not automatic", "active Profile", "link"],
    ),

    # ── 5.8 ───────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-031": dict(
        title="Seat does not move when the Profile switches during motion",
        design=STATE,
        pre=steps("Two Driver Profiles exist, each linked to a different "
                  "memory seat position",
                  "Driver Profile A is active and the vehicle is stationary"),
        data="NA",
        proc=steps("Read and record the current seat position",
                   "Bring the vehicle into motion",
                   "Switch to Driver Profile B and check that the seat position "
                   "is unchanged"),
        er=steps("The current seat position is recorded",
                 "The vehicle is in motion",
                 "The seat position matches the position recorded in step 1 "
                 "and a popup indicates that the seat could not adjust while "
                 "the vehicle is in motion"),
        remarks="**ER3 併驗「座椅未動」與「提示」兩者** —— 前者為防線本身"
                "（§8.7.4 之分野），後者為其呈現；**只驗提示，一個顯示提示卻仍"
                "移動座椅之實作會通過**。"
                "popup 之 PU id 條文未給，故 ER 只述其**內容要旨**，不寫 PU 編號"
                "（§8.4.1 不推定）。",
        reasoning=(
            "驗證目標：5.8（PRACC14）—— 行車中切換 profile 時座椅位置不變，"
            "並以 popup 告知無法調整。"
            "關鍵情境條件：兩 profile 各連**不同**座椅位置 ——"
            "位置相同則「座椅未動」與「本來就一樣」無從分辨。"
            "**判級 P0**：行車中座椅不得移動為安全防線，"
            "其成立本身之斷言落在 ER3 前半（D-UP16-01 附二）。"),
        kw=["in motion", "seat unchanged", "popup", "switch Profile"],
    ),

    # ── 5.10 ──────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-033": dict(
        title="Saved seat position goes to the Profile linked to that seat",
        design=FUNCTIONAL,
        pre=steps("Driver Profile B is linked to a memory seat position",
                  "Driver Profile B is the active Profile"),
        data="NA",
        proc=steps("Change the seat position and record the new position",
                   "Save the position to the memory seat linked to Driver "
                   "Profile B",
                   "Read the seat position stored for Driver Profile B and "
                   "check that it matches"),
        er=steps("The new seat position is recorded",
                 "The position is saved to the memory seat linked to Driver "
                 "Profile B",
                 "The seat position stored for Driver Profile B matches the "
                 "position recorded in step 1"),
        remarks="本條以**現用者即該座椅之連結者**為前提 ——"
                "現用者非連結者之情形屬 5.10.1（`SWE1-HMI-PROF-034-01`～`-03`），"
                "其行為不同（會先詢問）。",
        reasoning=(
            "驗證目標：5.10（PRACC16）—— 以記憶座椅之 set/save 控制儲存新位置時，"
            "存到**已連結該座椅**之 profile。"
            "關鍵情境條件：現用者與該座椅之連結者相同，"
            "使本條與 5.10.1 之詢問流程不重疊。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-030-02` 之分野 ——"
            "該條驗**沒存到現用者**，本條驗**存到了連結者**。"),
        kw=["save seat position", "linked Profile", "memory seat"],
    ),

    # ── 5.10.1 ────────────────────────────────────────────────────────
    "SWE1-HMI-PROF-034-01": dict(
        title="PU0588 prompt when saving a seat linked to another Profile",
        design=FUNCTIONAL,
        pre=steps("Driver Profile A is active and Driver Profile B is linked "
                  "to a memory seat position",
                  "The vehicle is stationary"),
        data="NA",
        proc=steps("Change the seat position",
                   "Save the position to the memory seat linked to Driver "
                   "Profile B",
                   "Read the screen and check that PU0588 asks about "
                   "switching the seat preference"),
        er=steps("The seat position is changed",
                 "The position is saved to the memory seat linked to Driver "
                 "Profile B",
                 "PU0588 is displayed and asks whether to switch the seat "
                 "preference to the newly saved memory seat number"),
        remarks="pre-condition 使**現用者非該座椅之連結者** ——"
                "那是 5.10.1 之觸發條件本身；現用者即連結者之情形屬 5.10。"
                "本條只驗**詢問出現**；選 Yes 之後果分屬 "
                "`SWE1-HMI-PROF-034-02`（現用者原無座椅）與 `-03`（原有座椅）。",
        reasoning=(
            "驗證目標：5.10.1（PRACC16.1）首句 —— 將新座椅位置存到"
            "**非現用** profile 所連之座椅時，以 PU0588 詢問是否改用該座椅。"
            "關鍵情境條件：現用者與該座椅之連結者**不同**，此為觸發條件。"
            "為什麼這樣切：037 對 5.10.1 切三個 leaf —— 詢問／兩種 Yes 之後果。"),
        kw=["PU0588", "prompt", "memory seat", "switch preference"],
    ),

    "SWE1-HMI-PROF-034-02": dict(
        title="Yes on PU0588 moves the seat to an unlinked active Profile",
        design=STATE,
        pre=steps("Driver Profile A is active and has no memory seat linked",
                  "Driver Profile B is linked to the memory seat position "
                  "under test"),
        data="NA",
        proc=steps("Change the seat position and save it to the memory seat "
                   "linked to Driver Profile B",
                   "Select Yes on PU0588",
                   "Read the seat links of both Profiles and check where the "
                   "seat now belongs"),
        er=steps("PU0588 is displayed",
                 "Yes is selected on PU0588",
                 "The memory seat position is linked to Driver Profile A and "
                 "the seat status of Driver Profile B is “None”"),
        remarks="**ER3 併驗兩側** —— A 得到該座椅、**且** B 之狀態變為 “None”；"
                "只驗 A 得到，一個讓兩個 profile 同時連著該座椅之實作會通過。"
                "`“None”` 逐字引自 5.10.1。"
                "與 `SWE1-HMI-PROF-034-03` 之分野：本條之現用者**原無**座椅。",
        reasoning=(
            "驗證目標：5.10.1（PRACC16.1）中段 —— 使用者選 Yes 且現用 profile "
            "原本沒有連座椅時，該座椅改連現用 profile，原連結者變為 “None”。"
            "關鍵情境條件：現用者原本**無**座椅 —— 那是本 leaf 與 `-03` 之分界。"
            "為什麼這樣切：兩個結果（A 得到、B 變 None）為同一次選擇之兩面，"
            "依 §5.7 併於一條 ER。"),
        kw=["PU0588", "Yes", "None", "seat reassign"],
    ),

    "SWE1-HMI-PROF-034-03": dict(
        title="Yes on PU0588 passes the old seat to the next Profile",
        design=STATE,
        pre=steps("Driver Profile A is active and already linked to its own "
                  "memory seat position",
                  "Driver Profile B is linked to the memory seat position "
                  "under test and a further Profile has no seat linked"),
        data="NA",
        proc=steps("Change the seat position and save it to the memory seat "
                   "linked to Driver Profile B",
                   "Select Yes on PU0588",
                   "Read the seat links of all Profiles and check where each "
                   "seat now belongs"),
        er=steps("PU0588 is displayed",
                 "Yes is selected on PU0588",
                 "The memory seat position under test is linked to Driver "
                 "Profile A, the seat status of Driver Profile B is “None” "
                 "and the original seat of Driver Profile A is linked to the "
                 "leftmost Profile without a seat"),
        remarks="**三個變動併於 ER3** —— 目標座椅改連 A、B 變 “None”、"
                "A 之原座椅改派給最左之無座椅 profile。"
                "條文之 `prioritizing from left to right based on the order of "
                "the Profiles on the All Profiles Tab` 使「最左」為明確對象 ——"
                "**只驗「改派給某人」，一個隨機挑選之實作會通過**"
                "（同 `NR1L-UserProfiles-097` 之理由）。"
                "pre-condition 要求另有一個無座椅之 profile，否則改派無對象。",
        reasoning=(
            "驗證目標：5.10.1（PRACC16.1）末句 —— 現用 profile **已有**座椅時選 "
            "Yes，其原座椅改派給下一個可用 profile（由左至右）。"
            "關鍵情境條件：須另有無座椅之 profile 作為改派對象。"
            "為什麼這樣切：與 `SWE1-HMI-PROF-034-02` 之分野在現用者**原有無座椅**；"
            "兩者為條文之兩個分支，037 各切一個 leaf。"),
        kw=["PU0588", "reassign", "left to right", "None"],
    ),
}

# ── 額外造者（1 條）—— 5.7 之全稱限制之反向 ────────────────────────
EXTRAS = [
    dict(
        suffix="neg",
        req_id="SWE1-HMI-PROF-030-01",
        prio=("P1", "座椅連結之唯一入口 —— 全稱限制之反向"),
        spec=dict(
            title="Memory seat link refused outside the Edit Profile screen",
            design=NEGATIVE,
            pre=steps("Driver Profile A is active and has no memory seat "
                      "linked",
                      "At least one memory seat position is unlinked"),
            data="NA",
            # **X-2（35 包）**：原步驟 2 寫 `from outside the “Edit Profile”
            # screen` —— **「outside」不是一個測試者能執行的位置**。
            # 比照 `NR1L-UserProfiles-047` 之作法：逐一指名實際受檢之畫面，
            # 並於 reasoning 具名其為抽樣。
            proc=steps("Open the “All Profiles” tab and read its entries",
                       "Attempt to link the memory seat position from the "
                       "“All Profiles” tab and from vehicle settings",
                       "Read the seat links and check that Driver Profile A "
                       "still has none"),
            er=steps("The “All Profiles” tab is displayed",
                     "The attempt is not accepted",
                     "No memory seat position is linked to Driver Profile A"),
            remarks="§7 之列舉配對：正向為 `NR1L-UserProfiles-127`"
                    "（`SWE1-HMI-PROF-030-01`，自 Edit Profile 連得成）。"
                    "條文之 `can **only** be done through the Edit Profile "
                    "screen` 為全稱限制 —— **只驗正向不足以證之**，"
                    "故另立本條（同 `009`／`105` 之形狀）。"
                    "**若該畫面根本不提供連結入口，步驟 2 即為「找不到入口」，"
                    "ER2 仍成立** —— 條文說的是不得自他處連結，"
                    "未規定以何種方式阻止。"
                    "**受檢之兩個畫面為抽樣（X-2）**，非窮舉；見 reasoning。",
            reasoning=(
                "驗證目標：5.7（PRACC13）之 `only` —— 記憶座椅之連結"
                "**不得**經 Edit Profile 以外之途徑完成。"
                "關鍵情境條件：A 無座椅且有空位，使「連上了」若發生即可見。"
                "為什麼這樣切：**全稱之限制只能以反向證之** ——"
                "正向（自 Edit Profile 連得成）與「他處也連得成」相容，"
                "故 `SWE1-HMI-PROF-030-01` 之正向不足以擋下該實作（§7）。"
                "**ER3 斷言「一個都沒連上」** 而非「這一次沒成功」，"
                "以排除連到別的座椅之實作。"
                "**受檢畫面為抽樣（X-2，35 包）**：「Edit Profile 以外」之位置"
                "**不可窮舉** —— 本條取兩個最可能提供該操作者"
                "（All Profiles 分頁、車輛設定），"
                "比照 `NR1L-UserProfiles-047` 之作法。"
                "**未涵蓋之其他入口，其結果不由本條保證。**"),
            kw=["only", "Edit Profile", "refused", "memory seat"],
        ),
    ),
]


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
        for extra, _provides in REF_EXTRA.get(req_id, []):
            refs += f"; {B.SPEC_STEM}_{extra}"
        rec = _rec(req_id, ctx, spec, refs, prio, why, n)
        rec["batch"] = "batch04"
        out.append(rec)
        n += 1

    for item in EXTRAS:
        rid = item["req_id"]
        ctx = B.assemble(rid, rows[rid])
        rec = _rec(rid, ctx, item["spec"], ctx["specification_reference"],
                   *item["prio"], n)
        rec["batch"] = "batch04"
        rec["parent"] = f"{rid}-{item['suffix']}"
        rec["note"] = (f"§7 之反向配對 —— 與 `{rid}` 同一 leaf，**非新 leaf**；"
                       f"檔名加 `-{item['suffix']}`")
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
