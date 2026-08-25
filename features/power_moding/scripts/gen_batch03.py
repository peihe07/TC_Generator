#!/usr/bin/env python3
"""batch 3 —— `Power Transitions`（ch 9 為主，7 leaf）之 TC 產出（30 包步驟 4）。

**開批依據**：R-PMH111（ch 9 之限縮解凍）＋ R-PMH105(b)（apparatus 凍結不礙產出）。

**三項特別拘束**（29b §4.1 步驟 9）：
  (a) **9.1 之 `source_clause` 取自 SYS1，非 PDF**（R-PMH75 —— R-PMH50 於該 5 leaf 反轉）；
  (b) **逐條套用 R-PMH111 之判別法並具名**（含判為「否」者）——
      本檔以 `p9_dependency` 欄承載，其值進入 JSON，非只在 reasoning 之散文裡；
  (c) 依 R-PMH94／R-PMH97／R-PMH101 逐斷言導出限定與掃描。

**R-PMH113 之 Pre-Condition**：`No phone call or projection call is active` ——
其位置為 **Pre-Condition 而非 procedure**，因「無通話進行中」為一個**狀態**（canon §4.4），
非測試員之動作。

**本批 7 leaf 中有 2 leaf 未產出 TC**（`SWE1-HMI-PM-002` / `-023`），其理由見 `STOPPED`。

**`tc_id` 續為 provisional**；**零寫回工作簿**。
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SPEC = "Power Moding HMI Logic and Flow R1 SR24 2A"

FUNC = "功能測試 (Functional based ; no specific technique)"
STATE = "狀態轉換 (State Transition Testing)"
EP = "等價劃分 (Equivalence Partitioning, EP)"

# --- R-PMH75：9.1 之權威文本為 **SYS1 匯出**（PDF 側為未刪淨之舊文字）---
# 下列各段逐字取自 `SYS1_HMI_…xlsx` 之 `Basic Report` 分頁、`Outline Number = 9.1`
# 之 `Description` 欄。**唯一之變換為 `_x000D_` → 換行**（該記號為 Excel 匯出
# 對 CR 之 XML 轉義，非內容），該變換於此具名。
SYS1 = {
 "S0": ("PM1) In the event that there are popups to show at IGN OFF but the user has set "
        "Power Accessory Delay to 0 seconds, the head unit should ‘stay awake up to 2.5 "
        "minutes to display the popup(s). If the user does not interact with the popup within "
        "60 the timeout defined in pop-up list, the popup should close if no other popups are "
        "to be shown the radio should shut off. [CR22412]"),
 "S1": ("If the user interacts with the FOTA [CR22412] popup the radio shall ‘stay awake’ "
        "until the user has not interacted with the popup for 60 seconds. Maximum time the "
        "radio can ‘stay awake’ because of these popups is 10 minutes."),
 "S3": "1.    FOTA update available -",
 "S4": "- If user accepts FOTA popup, start update and dismiss FOTA via Wi-Fi / Charge",
 "S6": ("- If user schedules an update time or dismisses update, display FOTA via Wi-Fi / "
        "Charge Now (if applicable)."),
 "S8": ("If user chooses to configure Wi-Fi, display Charge Now (if applicable) when Wi-Fi "
        "configuration is complete."),
 "S9": "If user chooses to dismiss Wi-Fi configuration popup, display Charge Now (if applicable).",
 "S11": ("Charge Now/Summary; Preconditioning. Shut the radio down if user dismisses XEV key "
         "off Pop-ups. [CR22412]"),
}

# --- R-PMH113 之 Pre-Condition（**狀態，非動作** —— 故不寫成 `Do not…`）---
PC_CALL = "No phone call or projection call is active"

# --- 本批未產出 TC 之 leaf 及其理由（**不得靜默略過**）---
STOPPED = {
 "SWE1-HMI-PM-023": {
   "outline": "10.5",
   "clause": ("PITA8: During Key OFF (with no ACC position available), HU power ON, all "
              "headunit functionality is expected to have the same functionality as key on, "
              "except for controls that communicate with modules external to the headunit "
              "which are not functional during Key OFF."),
   "p9_dependency": "**是**",
   "why": ("**R-PMH111 之判別法命中** —— 其斷言之謂詞正是「**某受控對象（`Headunit`）於某電源"
           "狀態（`KEY OFF (No ACC position)` × `HEADUNIT POWER ON`）下是否可用**」，"
           "與 p9 能力矩陣同格之逐字 `Headunit: Full on, some limited functionality` 為同一謂詞。"
           "且 PDF 中本句之前一行逐字為 `HEADUNIT POWER ON:` —— **其為 p9 矩陣之欄標題**。"
           "依 R-PMH111 **該條停並登記，不得產出**。"),
 },
 "SWE1-HMI-PM-002": {
   "outline": "7.1.1",
   "clause": ("SU1.1) While ignition is off, transitions related to the power button to display "
              "splash, disclaimers, or radio last mode are based on vehicle architecture. "
              "See CFTS009 for clarification."),
   "p9_dependency": "否",
   "why": ("**非因 p9 而停** —— 其謂詞為「點火關閉時電源鍵所引發之畫面轉換」，"
           "與 p9 之「受控對象是否可用」不同（R-PMH111 判別法：**否**）。"
           "**其停手之理由為：本句未載任何可驗之行為** —— 其逐字將行為委於"
           "`vehicle architecture` 與 `CFTS009`，而 **CFTS009 非本 feature 所持有之素材**。"
           "任何 TC 皆須自行指定「哪一種架構對應哪一種轉換」，即造值（canon §8.4.1）。"
           "**其形態與 `SWE1-HMI-PM-028`（12.2，`Please refer to CFTS009`）相同**，"
           "該筆經 R-PMH47(a) 判為 out of scope、R-PMH72 裁定不寫入工作簿。"
           "**31 包 §四之裁定（R-PMH117）**：判 out of scope、不寫入交付工作簿，比照 R-PMH72。"
           "⚠ **R-PMH117 之效力起於 Pei 之核可** —— 其動到範圍（有 TC 之 leaf 47 → 46，"
           "而 R-PMH1 為範圍條文）。**核可前本筆維持停手、不產出、不寫入。**"),
 },
}

TCS = [
 dict(leaf="SWE1-HMI-PM-018-01", outline="9.1", frop="Power Management", src="S0",
   dm=STATE, pri="P1",
   title="Head unit stays awake at ignition off to display the pending pop-up",
   item=("PM1) In the event that there are popups to show at IGN OFF but the user has set "
     "Power Accessory Delay to 0 seconds, the head unit should ‘stay awake up to 2.5 "
     "minutes to display the popup(s).\n\n"
     "(維持喚醒之路徑 —— 與 -017 之 FOTA 互動延長路徑成對)"),
   pre=[f"1. {PC_CALL}",
        "2. Power Accessory Delay is set to 0 seconds",
        "3. At least one pop-up from the ignition off list is pending"],
   proc=["1. Turn the ignition off and record the head unit power state",
         "2. Read the display and record the pop-up shown",
         "3. Do not interact with the pop-up and record the awake duration",
         "4. Read the pop-up state after the 60-second timeout expires",
         "5. Read the radio power state when no other pop-ups remain",
         "6. Compare the recorded duration with the stated maximum"],
   er=["1. The head unit stays awake when the ignition is turned off",
       "2. The pending pop-up is displayed",
       "3. The head unit does not power off while the pop-up is being displayed",
       "4. The pop-up is closed after the 60-second timeout defined in the pop-up list",
       "5. The radio shuts off when no other pop-ups remain",
       "6. The head unit stays awake for no longer than 2.5 minutes"],
   p9="否",
   p9why=("其斷言為「head unit 於 IGN OFF 後是否維持喚醒、pop-up 是否顯示」，"
          "**非**「某受控對象於某電源狀態下是否可用」。"),
   reason=("**P1 —— 主要功能邏輯**（非 P0）：其失效使 IGN OFF 之 popup 無法顯示，"
     "惟不阻斷開機或回復。設計方法 STATE —— 標的為 IGN OFF 所引發之電源狀態轉換及其延遲。"
     "⚠ **`source_clause` 取自 SYS1 之 9.1，非 PDF**（**R-PMH75** —— R-PMH50 於本 5 leaf 反轉）。"
     "⚠ **三個結果不拆之依據（36 包 §二，canon §5.7）** —— 本條斷言三事："
     "維持喚醒 <= 2.5 分（ER6）、60 秒後 popup 關閉（ER4）、無其他 popup 則 radio 關機（ER5）。"
     "**三者為同一觸發（IGN OFF ＋ 有 popup 待顯示 ＋ 使用者不互動）之連續後果**，"
     "屬同一驗證單位，依 §5.7 不拆。"
     "**§8.2.2 之壓力測試於此不觸發** —— 該條所禁者為**兩個獨立分支**之部分失效落在同一判定上；"
     "**本處三者為一條時序鏈上之三點**，其前一點不成立則後一點無從觀測，**非獨立**。"
     "⚠ **35 包 §3（R-PMH133）之修正 —— 前開「不造值」之前提已被 037 之 DESC 推翻**："
     "本 leaf 之 `Requirement Description` 逐字為 `If the user does not interact with the popup "
     "within **the 60-second timeout defined in the pop-up list**, the system shall close the "
     "popup. If no other popups remain, the system shall shut off the radio.` —— "
     "**60 秒與其後二句皆完整**，故 ER4／ER5 補之。**A-PMH25 已改 `RESOLVED`。**"
     "**DESC 決定要驗什麼，PDF／SYS1 決定其措詞為何**（R-PMH133 之分工）。"
     "⚠ **以下為 31 包當時之陳述，依 R-PMH44 保留，其前提已不成立**："
     "SYS1 之權威文本於逾時處逐字為 `If the user does not interact with the popup within 60 "
     "the timeout defined in pop-up list` —— **該句於權威文本中即為破句**（A-PMH25），"
     "故本條**不斷言該處之逾時秒數**。"
     "**⚠ 30 包 §4.6 原記為「不斷言任何逾時秒數」，與本條 ER4 之 `2.5 minutes` 自相矛盾**"
     "（R-PMH45 之同檔內互斥陳述）——**該表述已於本包更正**。"
     "**三值皆在權威文本內，非造值**（執行層獨立複驗，SYS1 9.1 各 1 命中）："
     "`2.5 minutes` 1／`for 60 seconds` 1（FOTA 句，見 -017）／`10 minutes` 1；"
     "而 `within 60 seconds`、`stay awake for 60 seconds` **各 0 命中** —— "
     "**該子句正是 A-PMH16 所查出、SYS1 已刪者**（R-PMH75）。"
     "⚠ **R-PMH113 之 Pre-Condition**：`No phone call or projection call is active` —— "
     "State Matrix `r31`／`r32` 於 key-off 且 `Radio off Delay = 0` 時取 `HU OFF`，"
     "與本條之「維持喚醒」**取相反值且條件互斥未證**（29b 步驟 8 所查出之牴觸）。"
     "**其位置為 Pre-Condition 而非 procedure —— 「無通話進行中」為狀態，非動作**（canon §4.4）。"
     "**該限定不預判 `Power Accessory Delay` 與 `Radio off Delay` 是否同一**（A-PMH24，`DR-PMH8` Q4）。"),
   axis="路徑：無互動之維持喚醒（對 -017 之 FOTA 互動延長）"),

 dict(leaf="SWE1-HMI-PM-018-02", outline="9.1", frop="FOTA Via Wi-fi", src="S1",
   dm=STATE, pri="P1",
   title="FOTA pop-up interaction extends the stay awake time up to ten minutes",
   item=("If the user interacts with the FOTA [CR22412] popup the radio shall ‘stay awake’ "
     "until the user has not interacted with the popup for 60 seconds. Maximum time the radio "
     "can ‘stay awake’ because of these popups is 10 minutes.\n\n"
     "(FOTA 互動延長路徑 —— 與 -016 之無互動路徑成對；34 包改掛 018-02)"),
   pre=[f"1. {PC_CALL}",
        "2. A FOTA pop-up is displayed after the ignition has been turned off"],
   proc=["1. Interact with the FOTA pop-up and record the interaction time",
         "2. Stop interacting with the pop-up and record when the radio powers off",
         "3. Interact with the pop-up repeatedly beyond ten minutes and check that "
         "the radio powers off"],
   er=["1. The radio stays awake while the user is interacting with the FOTA pop-up",
       "2. The radio stays awake until the user has not interacted with the pop-up for 60 seconds",
       "3. The radio does not stay awake for more than 10 minutes because of these pop-ups"],
   p9="否",
   p9why="其斷言為「radio 因 popup 互動而維持喚醒之時長」，**非**受控對象之可用性。",
   reason=("**P1 —— 主要功能邏輯**：其失效使 radio 於 IGN OFF 後無限期喚醒（電池耗損）"
     "或過早關閉（使用者無法完成 FOTA 互動）。"
     "⚠ **34 包 §2.2／R-PMH128 之改掛** —— 本條原掛 `SWE1-HMI-PM-018-01`，**改掛 `-018-02`**："
     "037 之 `Requirement Description` 逐字為 `If the user interacts with the FOTA popup, "
     "the system shall stay awake until the user has not interacted with the popup for 60 "
     "seconds. The maximum time the system can stay awake due to these popups is 10 minutes.` "
     "—— **與本條逐項相符**；而 `-018-01` 之 DESC 為 2.5 分鐘與該逾時，**是 -016 之標的**。"
     "**本條因而不再是同 leaf 之第二條**，profile §4 之拆分依據隨之撤回。設計方法 STATE。"
     "⚠ **本條之二個秒數皆得斷言** —— `60 seconds` 與 `10 minutes` 於 SYS1 之權威文本中"
     "**皆完整**（與 -016 之破句處不同，該差異已於 A-PMH25 具名）。"
     "⚠ **R-PMH113 之 Pre-Condition** 同 -016，其理由不重述（§8.5）。"
     "⚠ **`until the user has not interacted … for 60 seconds` 與 `Maximum … 10 minutes` "
     "二者何者先到即何者生效** —— 規格未言其優先，**本條以二個獨立步驟分別驗之而不斷言其交互作用**。"),
   axis="路徑：FOTA 互動延長（對 -016 之無互動；34 包改掛 `-018-02`）"),

 dict(leaf="SWE1-HMI-PM-018-03", outline="9.1", frop="FOTA Via Wi-fi", src="S4",
   dm=EP, pri="P1",
   title="Accepting the FOTA pop-up starts the update and dismisses the later pop-ups",
   item=("- If user accepts FOTA popup, start update and dismiss FOTA via Wi-Fi / Charge\n\n"
     "(使用者選擇之第一類：接受 —— 與 -019 之排程、-020 之取消同軸)"),
   pre=[f"1. {PC_CALL}",
        "2. The FOTA update available pop-up is displayed after the ignition has been turned off",
        "3. FOTA via Wi-Fi and Charge Now are applicable on this vehicle"],
   proc=["1. Accept the FOTA pop-up",
         "2. Read the update state and record it",
         "3. Check that the FOTA via Wi-Fi and Charge Now pop-ups are dismissed"],
   er=["1. The FOTA update available pop-up is accepted",
       "2. The update starts",
       "3. The FOTA via Wi-Fi and Charge Now pop-ups are dismissed"],
   p9="否",
   p9why="其斷言為「FOTA 更新是否開始、後續 popup 是否被 dismiss」，**非**受控對象之可用性。",
   reason=("**P1 —— 主要功能邏輯**：其失效使使用者接受之 FOTA 更新不會開始。"
     "⚠ **設計方法 EP（31 包 §2.4 之修正，原標 FUNC）** —— 依 **R-PMH118**："
     "`design_method` 之判準為**輸入是否被劃分為等價類，非該 TC 之內含幾類**。"
     "`accepts`／`schedules`／`dismisses` 為使用者於同一 popup 上之三個等價類，"
     "**本條只涵蓋其一，其技術仍為 EP**。"
     "⚠ **34 包 §2.2／R-PMH128 之改掛** —— 本條原掛 `-018-02`，**改掛 `-018-03`**："
     "037 之 DESC 逐字為 `For Priority 1 (FOTA update available): If the user accepts the FOTA "
     "popup, the system shall start the update and dismiss FOTA via Wi-Fi / Charge Now …` "
     "—— **本條與 -019／-020 三者同屬該 leaf**。"
     "⚠ **`(if applicable)` 之處置** —— 權威文本逐字載 `Charge Now (if applicable)`；"
     "本條以 **pre_condition 3** 承載該條件，**不於 ER 中重述其條件式**（canon §5）。"
     "⚠ **`source_clause` 為權威文本之逐字子句，其於 SYS1 中即斷行於 `Charge` 之後** —— "
     "**未補其下一行之 `Now (if applicable)`**（§4.3.1 逐字，不修補）。"
     "⚠ **R-PMH113 之 Pre-Condition** 同 -016，其理由不重述（§8.5）。"),
   axis="使用者選擇之等價類：接受（對 -019 之排程、-020 之取消；34 包改掛 `-018-03`）"),

 dict(leaf="SWE1-HMI-PM-018-03", outline="9.1", frop="FOTA Via Wi-fi", src="S6",
   dm=EP, pri="P1",
   title="Scheduling an update time displays the later pop-ups",
   item=("- If user schedules an update time or dismisses update, display FOTA via Wi-Fi / "
     "Charge Now (if applicable).\n\n"
     "(使用者選擇之第二類：排程 —— 與 -020 之取消為兩個獨立分支，31 包 §2.2 拆分)"),
   pre=[f"1. {PC_CALL}",
        "2. The FOTA update available pop-up is displayed after the ignition has been turned off",
        "3. FOTA via Wi-Fi and Charge Now are applicable on this vehicle"],
   proc=["1. Schedule an update time on the FOTA pop-up",
         "2. Check that the FOTA via Wi-Fi and Charge Now pop-ups are displayed"],
   er=["1. The update time is scheduled",
       "2. The FOTA via Wi-Fi and Charge Now pop-ups are displayed"],
   p9="否",
   p9why="其斷言為「後續 popup 是否顯示」，**非**受控對象之可用性。",
   reason=("**P1 —— 主要功能邏輯**：其失效使後續之 FOTA via Wi-Fi／Charge Now 不會出現。"
     "⚠ **31 包 §2.2 之拆分** —— 原一條含「排程」與「取消」兩個獨立分支；"
     "依 canon §8.2.2 之壓力測試：**排程成功而取消失效時該條落 fail、"
     "取消成功而排程失效時亦落 fail —— 兩個獨立之部分失效落在同一個判定上，即 bundling**。"
     "故拆為本條與 -020。**其 design_method 為 EP 更使此點清楚**：EP 之每一等價類各為一條"
     "（batch 2 之 -012／-013／-014 即如此）。"
     "設計方法 EP（R-PMH118）。"
     "⚠ **`source_clause` 含二類而本條只驗其一** —— 權威文本以 `or` 連接排程與取消；"
     "**另一類由 -020 承載，二條共用同一 `source_clause`**（同 leaf、同句、不同等價類）。"
     "⚠ **R-PMH113 之 Pre-Condition** 同 -016。"),
   axis="使用者選擇之等價類：排程（對 -018 之接受、-020 之取消）"),

 dict(leaf="SWE1-HMI-PM-018-03", outline="9.1", frop="FOTA Via Wi-fi", src="S6",
   dm=EP, pri="P1",
   title="Dismissing the update displays the later pop-ups",
   item=("- If user schedules an update time or dismisses update, display FOTA via Wi-Fi / "
     "Charge Now (if applicable).\n\n"
     "(使用者選擇之第三類：取消 —— 與 -019 之排程為兩個獨立分支，31 包 §2.2 拆分)"),
   pre=[f"1. {PC_CALL}",
        "2. The FOTA update available pop-up is displayed after the ignition has been turned off",
        "3. FOTA via Wi-Fi and Charge Now are applicable on this vehicle"],
   proc=["1. Dismiss the update on the FOTA pop-up",
         "2. Check that the FOTA via Wi-Fi and Charge Now pop-ups are displayed"],
   er=["1. The update is dismissed",
       "2. The FOTA via Wi-Fi and Charge Now pop-ups are displayed"],
   p9="否",
   p9why="其斷言為「後續 popup 是否顯示」，**非**受控對象之可用性。",
   reason=("**P1 —— 主要功能邏輯**：同 -019 之依據（批內 priority 依據互不矛盾，R-PMH59）。"
     "⚠ **31 包 §2.2 之拆分** —— 本條為原 -019 之第二分支，其理由見 -019 之 reasoning。"
     "設計方法 EP（R-PMH118）。"
     "⚠ **與 -019 共用 `source_clause`** —— 同 leaf、同句、不同等價類；"
     "**其區別由 `distinguishing_axis` 承載**（canon §5.7 之拆分依據為觸發之不同，"
     "本處之不同者為**使用者之選擇**，二者皆為合法之拆分軸）。"
     "⚠ **R-PMH113 之 Pre-Condition** 同 -016。"),
   axis="使用者選擇之等價類：取消更新（對 -018 之接受、-019 之排程）"),

 dict(leaf="SWE1-HMI-PM-018-04", outline="9.1", frop="WiFi", src="S8",
   dm=EP, pri="P1",
   title="Charge Now is displayed when the Wi-Fi configuration is complete",
   item=("If user chooses to configure Wi-Fi, display Charge Now (if applicable) when Wi-Fi "
     "configuration is complete.\n\n"
     "(Wi-Fi 選擇之第一類：完成設定 —— 與 -022 之取消為兩個獨立分支，31 包 §2.2 拆分)"),
   pre=[f"1. {PC_CALL}",
        "2. The FOTA via Wi-Fi configuration pop-up is displayed after the ignition has been "
        "turned off",
        "3. Charge Now is applicable on this vehicle"],
   proc=["1. Choose to configure Wi-Fi and complete the Wi-Fi configuration",
         "2. Check that the Charge Now pop-up is displayed"],
   er=["1. The Wi-Fi configuration is completed",
       "2. The Charge Now pop-up is displayed"],
   p9="否",
   p9why="其斷言為「Charge Now popup 是否顯示」，**非**受控對象之可用性。",
   reason=("**P1 —— 主要功能邏輯**：其失效使 Charge Now 不會出現。"
     "⚠ **31 包 §2.2 之拆分** —— 原一條含「完成設定」與「取消設定」兩個獨立分支，"
     "依 canon §8.2.2 為 bundling，故拆為本條與 -022。設計方法 EP（R-PMH118）。"
     "⚠ **§8.4.1 不造值：`when Wi-Fi configuration is complete` 未給任何秒數**，"
     "故 ER2 只斷言「顯示」而不斷言任何延遲。"
     "⚠ **R-PMH113 之 Pre-Condition** 同 -016。"),
   axis="Wi-Fi 選擇之等價類：完成設定（對 -022 之取消設定）"),

 dict(leaf="SWE1-HMI-PM-018-04", outline="9.1", frop="WiFi", src="S9",
   dm=EP, pri="P1",
   title="Charge Now is displayed after the Wi-Fi configuration pop-up is dismissed",
   item=("If user chooses to dismiss Wi-Fi configuration popup, display Charge Now (if "
     "applicable).\n\n"
     "(Wi-Fi 選擇之第二類：取消設定 —— 與 -021 之完成設定為兩個獨立分支)"),
   pre=[f"1. {PC_CALL}",
        "2. The FOTA via Wi-Fi configuration pop-up is displayed after the ignition has been "
        "turned off",
        "3. Charge Now is applicable on this vehicle"],
   proc=["1. Dismiss the FOTA via Wi-Fi configuration pop-up",
         "2. Check that the Charge Now pop-up is displayed"],
   er=["1. The FOTA via Wi-Fi configuration pop-up is dismissed",
       "2. The Charge Now pop-up is displayed"],
   p9="否",
   p9why="其斷言為「Charge Now popup 是否顯示」，**非**受控對象之可用性。",
   reason=("**P1 —— 主要功能邏輯**：同 -021 之依據。"
     "⚠ **31 包 §2.2 之拆分** —— 本條為原 -020 之第二分支。"
     "⚠ **本條之 `source_clause` 為權威文本之另一句**（`If user chooses to dismiss Wi-Fi "
     "configuration popup, …`），**與 -021 不同句** —— 此與 -019／-020 之共用同句不同，"
     "其差異據實記載。設計方法 EP（R-PMH118）。"
     "⚠ **R-PMH113 之 Pre-Condition** 同 -016。"),
   axis="Wi-Fi 選擇之等價類：取消設定（對 -021 之完成設定）"),

 dict(leaf="SWE1-HMI-PM-018-05", outline="9.1", frop="EV/PHEV Pages", src="S11",
   dm=FUNC, pri="P1",
   title="Dismissing the XEV key off pop-ups shuts the radio down",
   item=("Charge Now/Summary; Preconditioning. Shut the radio down if user dismisses XEV key "
     "off Pop-ups. [CR22412]\n\n"
     "(XEV 之 key off popup 群及其忽略後之關機)"),
   pre=[f"1. {PC_CALL}",
        "2. The vehicle is an XEV on which the Charge Now, Summary and Preconditioning pages "
        "are applicable",
        "3. The ignition has been turned off"],
   proc=["1. Read the pop-ups shown after ignition off and record them",
         "2. Dismiss the XEV key off pop-ups",
         "3. Check that the radio shuts down"],
   er=["1. The Charge Now, Summary and Preconditioning pop-ups are shown",
       "2. The XEV key off pop-ups are dismissed",
       "3. The radio shuts down"],
   p9="否",
   p9why=("其斷言為「XEV popup 是否顯示、radio 是否關機」，**非**受控對象於某電源狀態下之可用性。"
          "⚠ **`radio shuts down` 與 p9 之 `Headunit: OFF` 用詞相近，惟其謂詞不同** —— "
          "p9 述「在某電源狀態下 headunit 之可用程度」，本條述「某使用者動作之後 radio 是否關機」。"),
   reason=("**P1 —— 主要功能邏輯**：其失效使 radio 於使用者忽略 XEV popup 後不關機（電池耗損）。"
     "⚠ **設計方法 FUNC 而非 EP —— 其理由須與 R-PMH118 並讀**：R-PMH118 令「一條只含一類者"
     "其技術仍為 EP」，**惟本條之輸入自始未被劃分為等價類** —— 權威文本只給一個分支"
     "（`dismisses` → 關機），未給其對立分支之行為。**無劃分即無 EP**，"
     "故落 canon §12 之 `Functional based`。**該區別即 R-PMH118 之界線，於此具名。**"
     "⚠ **`Charge Now/Summary; Preconditioning.` 之三者本檔讀為一個 popup 群** —— "
     "權威文本以 `/` 與 `;` 並列而未言其為一個或三個 popup；"
     "**ER1 逐一列舉三者而不斷言其為一個畫面或三個畫面**（§8.4.1 不造值）。"
     "⚠ **R-PMH113 之 Pre-Condition** 同 -016。"),
   axis="事件：忽略 XEV key off popup 群（本批唯一之非等價類軸）"),
]

def norm_item(s: str) -> str:
    """canon §11 之正規化 —— **只用於 `test_item`，不用於 `source_clause`**。"""
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = re.sub(r"\s*\[CR\d+\]", "", s)
    return re.sub(r"  +", " ", s)


BASE = 15         # batch 1 用 001–008、batch 2 用 009–015，本批續 016 起（R-PMH16）


def main() -> None:
    out = []
    for n, t in enumerate(TCS, BASE + 1):
        out.append({
            "tc_id": f"NR1L-DisclaimerScreen-{n:03d}",
            "leaf_id": t["leaf"],
            "test_group": "Disclaimer screen",
            "test_set": "Power Transitions",
            "tc_title": t["title"],
            # canon §11（方括號禁止／無彎引號）vs canon §4.3.1（上半逐字）之衝突：
            # **`source_clause` 保持未經觸碰之逐字**；**`test_item` 之上半施二項具名之正規化**
            # —— 彎引號 → 直引號、去 `[CRnnnnn]` 之變更請求標記。二者皆非行為內容。
            # 該處置為執行層之判斷，**未經裁定**（A-PMH26）。
            "test_item": norm_item(t["item"]),
            "pre_conditions": "\n".join(t["pre"]),
            # 33 包 §2.3 之連帶：canon §4.5 逐字為 `set Input Test Data to NA`。
            # ⚠ **下放包謂「batch 1／2／3 皆為 NA」而實測 batch 3 為 `N/A`** —— 一併更正。
            "input_test_data": "NA",
            "test_procedure": "\n".join(t["proc"]),
            "expected_result": "\n".join(t["er"]),
            "specification_reference": f"{SPEC}_{t['outline']}",
            "design_method": t["dm"],
            "priority": t["pri"],
            "functional_safety": "NA",
            "estimated_test_time": "",          # profile §3.6 留白
            "vehicle_models": "",               # profile §3.8 留白
            "remarks": f"FROP: {t['frop']}",
            "reasoning": t["reason"],
            "distinguishing_axis": t["axis"],
            "source_clause": SYS1[t["src"]],
            # R-PMH75 —— 9.1 之 5 leaf 其來源為 SYS1，**非 PDF**
            "source_clause_origin": "sys1_export 9.1",
            # R-PMH111 之判別法，**逐條具名（含「否」者）**
            "p9_dependency": t["p9"],
            "p9_dependency_basis": t["p9why"],
        })
    doc = {
        "batch": "batch03",
        "feature": "power_moding",
        "test_group": "Disclaimer screen",
        "test_set": "Power Transitions",
        "handoff": "docs/handoff/30_batch3.md",
        "profile": "docs/runtime/profiles/FW036_R1L_PowerModing_Profile.md",
        "selection": ("Test Set `Power Transitions` 之 7 leaf（R-PMH36 之 Layer 2 定版）。"
                      "**6 條 TC 自 5 leaf** —— `SWE1-HMI-PM-018-01` 依 profile §4"
                      "「不同觸發即拆分」拆為 2 條（IGN OFF 本身／FOTA popup 之互動）；"
                      "**`SWE1-HMI-PM-002` 與 `-023` 未產出**，其理由見 `stopped`。"),
        "tc_id_status": "provisional",
        "leaf_scope": sorted({t["leaf"] for t in TCS}),
        "source_clause_basis": ("**R-PMH75** —— 9.1 之權威文本為 **SYS1 匯出**（PDF 側為未刪淨之"
                                "舊文字），R-PMH50 於本 5 leaf 反轉。唯一之變換為 `_x000D_` → 換行。"),
        "write_back": "凍結 —— 本批只產出 JSON，不寫回工作簿",
        # 29b／30：本批之 Pre-Condition 型限定（R-PMH113）——
        # **不入 `limits`**：`limits` 為 procedure 之字串檢查（R-PMH99(c)），
        # 而本項在 pre_conditions。**其位置由型別決定**，故其檢查亦不同處。
        "limits": {},
        "pre_condition_limits": {tc["tc_id"]: [PC_CALL] for tc in out},
        "stopped": STOPPED,
        "tcs": out,
    }
    p = ROOT / "generated" / "batch03.json"
    p.parent.mkdir(exist_ok=True)
    p.write_text(json.dumps(doc, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"wrote {p} — {len(out)} TC（自 {len(doc['leaf_scope'])} leaf；"
          f"另 {len(STOPPED)} leaf 停手並登記）")


if __name__ == "__main__":
    main()
