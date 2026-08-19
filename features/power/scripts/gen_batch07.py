"""B4 —— 第七批：`SWE-PM-001`–`009` 之 TC 產出（R-P320）。

DR-PW6 之阻斷經 49 包解除（WrapperResource 二份已入庫）。

**⚠ `SWE-PM-008` 不在本批** —— 其另受 **DR-PW11（blocking）**，
49 §K 第 3 項令執行層逐一確認，實測其阻斷**未解除**。
`SWE-PM-003` 之 DR-PW5 為 **advisory**（不阻斷），故納入。
**本批為 8 leaf。**

**R-P320 之界線逐字遵行**：
  得為之 —— 確認行為於規格中確有依據；抽出具名訊號與狀態名；產生 `spec_reference`
  不得為之 —— 自文字標籤之散列**推想轉換關係**
  不明者 —— **停並上繳，不得推想**

**本批之 TC 全部取自 CFTS009 §1.6.2.1.x 之文字錨點**
（各狀態之定義、其可用功能、進入該狀態時之動作），
**未使用圖之連線關係** —— 故無 R-P320(b) 之風險。
圖之用途限於「確認該 9 leaf 之行為於規格中確有依據」（R-P320(a)）。

用法：
    python features/power/scripts/gen_batch07.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
GEN = ROOT / "features/power/generated"
SPEC = ("R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_"
        "Wake-up and Power-up_SR26_20250909-1658")
START = 261                      # 接續現行末號（R-P113(b) 臨時號）
BENCH = "1. A LIN and CAN simulation tool is connected"

# （leaf, 章節, 錨點, clause 逐字, 各 TC）
LEAVES: list[dict] = [
    {"parent": "SWE-PM-001", "section": "1.6.2.1.1", "anchors": "4941357,4941358,4941360",
     "clause": ('In the following "Ignition Working Conditions": Ignition On, '
                'Ignition Pre_Start, Ignition Start, Ignition Cranking, '
                'Ignition On Engine On,\nThis status is related to TLM ON.\n'
                'All TLM, AMP/ICS/DTV functionalities are available.'),
     "reasoning": (
         "驗證目標：Full-Operation 狀態之二項定義性質 —— TLM 為 ON、"
         "全部 TLM/AMP/ICS/DTV 功能可用。關鍵情境條件：規格所列之五種 "
         "Ignition Working Condition。為什麼這樣切：原文為二個獨立斷言"
         "（狀態關聯與功能可用性），依 §5.7 各為一條之必然後果，"
         "而其觸發同為「處於所列之 ignition 條件」，故合為一條多 ER。"
         "刻意略過：**進入該狀態之轉換條件不在文字錨點中**，"
         "其僅見於 `4941354` 之狀態機圖；依 **R-P320(b)(c)** 不自圖之連線推想，"
         "本條僅驗其**處於該狀態時**之性質。"),
     "tcs": [
         {"title": "Full-Operation keeps the TLM ON with all functionalities available",
          "item": "TLM ON and full functionality availability in Full-Operation",
          "pre": [BENCH, 'The ignition working condition is Ignition On',
                  'TLM_Status.Info and $Telematic_Power$ read "Full-Operation"'],
          "data": "NA",
          "proc": ["1. Read TLM_Status.Info and the TLM power indication",
                   "2. Read the TLM, AMP, ICS and DTV functionality availability to check that all are available"],
          "er": ["1. The TLM is ON",
                 "2. All TLM, AMP, ICS and DTV functionalities are available"],
          "axis": ("trigger_state", "本條驗 Ignition On 之情形")},
         {"title": "Full-Operation holds in each listed ignition working condition",
          "item": "Full-Operation across the listed ignition working conditions",
          "pre": [BENCH, 'The TLM is in Full-Operation'],
          "data": ("Ignition working conditions: Ignition Pre_Start, Ignition Start, "
                   "Ignition Cranking, Ignition On Engine On"),
          "proc": ["1. Apply each ignition working condition listed in Input Test Data in turn",
                   "2. Read TLM_Status.Info after each one to check that Full-Operation is kept"],
          # **R-P109 / §8.4.2**：`SWE-PM-001` 之 `source_clause` **未載**
          # `TLM_Status.Info` / `$Telematic_Power$` 二訊號 —— 其僅載
          # 「此狀態關聯於 TLM ON」與「全部功能可用」。
          # 故 ER 改以 clause 所載之措詞陳述，不引該二訊號（依據越界）。
          "er": ["1. The TLM registers each ignition working condition without a bus error",
                 "2. The TLM stays ON with all TLM, AMP, ICS and DTV functionalities "
                 "available in each of the listed conditions"],
          "axis": ("input_data", "本條驗其餘四種 ignition 條件之取值")},
     ]},
    {"parent": "SWE-PM-002", "section": "1.6.2.1.2",
     "anchors": "4941365,4941366,4941371,4941372",
     "clause": ("This status is related to TLM audio is OFF. TLM shall allow only "
                "Splash Screen visualization on its display. ICS functionalities are "
                "available. DTV shall be OFF.\nRear View Camera images shall be "
                "available if needed.\nIn this state, user cannot do any setting\n"
                "All TLM functionalities run in background and are ready, but no HMI "
                "interaction is enabled, except TLM Power button"),
     "reasoning": (
         "驗證目標：Idle 狀態之四項限制 —— 音訊 OFF 且僅 Splash Screen 可視、"
         "DTV OFF 而 ICS 可用、後視攝影機影像於需要時可用、無法設定且 HMI 互動"
         "僅限電源鍵。關鍵情境條件：TLM 處於 Idle。為什麼這樣切：原文之四句"
         "各驗不同子系統（音訊／畫面、ICS/DTV、攝影機、HMI），"
         "其觀察對象互不重疊，依 §8.2.2 各拆一條。"
         "刻意略過：**進入 Idle 之轉換條件不在文字錨點中**，依 R-P320(c) 不推想。"),
     "tcs": [
         {"title": "Idle mutes the audio and allows only the Splash Screen",
          "item": "Audio off and Splash Screen only in Idle",
          "pre": [BENCH, 'TLM_Status.Info and $Telematic_Power$ read "Idle"'],
          "data": "NA",
          "proc": ["1. Read the TLM audio output state",
                   "2. Read the TLM display to check what is allowed"],
          "er": ["1. The TLM audio is OFF",
                 "2. Only the Splash Screen is visualized on the TLM display"],
          "axis": ("trigger_state", "本條驗音訊與畫面之限制")},
         {"title": "Idle keeps ICS available and DTV off",
          "item": "ICS available and DTV off in Idle",
          "pre": [BENCH, 'TLM_Status.Info and $Telematic_Power$ read "Idle"'],
          "data": "NA",
          "proc": ["1. Read the ICS functionality availability",
                   "2. Read the DTV state to check that it is off"],
          "er": ["1. The ICS functionalities are available",
                 "2. The DTV is OFF"],
          "axis": ("trigger_state", "本條驗 ICS 與 DTV 之可用性")},
         {"title": "Idle provides the rear view camera images when needed",
          "item": "Rear view camera availability in Idle",
          "pre": [BENCH, 'TLM_Status.Info and $Telematic_Power$ read "Idle"',
                  'The rear view camera images are requested'],
          "data": "NA",
          "proc": ["1. Request the rear view camera images",
                   "2. Read the TLM display to check whether the images are provided"],
          "er": ["1. The TLM registers the request without a bus error",
                 "2. The rear view camera images are available"],
          "axis": ("trigger_state", "本條驗後視攝影機之可用性")},
         {"title": "Idle disables settings and all HMI interaction except the power button",
          "item": "HMI restriction in Idle",
          "pre": [BENCH, 'TLM_Status.Info and $Telematic_Power$ read "Idle"'],
          "data": "NA",
          "proc": ["1. Attempt a user setting on the TLM",
                   "2. Attempt an HMI interaction other than the TLM Power button",
                   "3. Press the TLM Power button to check that it is the only enabled interaction"],
          "er": ["1. No user setting can be done",
                 "2. No HMI interaction other than the TLM Power button is enabled",
                 "3. The TLM Power button press is accepted"],
          "axis": ("trigger_state", "本條驗 HMI 互動之限制")},
     ]},
    {"parent": "SWE-PM-003", "section": "1.6.2.1.3",
     "anchors": "4941392,4941393,4941394,4941400",
     "clause": ('In this mode TLM shall shall report $Telematic_Power$ = '
                '" Partial_Operation". This mode shall exist for AMP, ICS, and DTV '
                'when STATUS_BH_BCM2.RemStActvSts is equal to "Remote Start Active" '
                'is recieved and TLM sends $Telematic_Power$ = "Partial_Operation"\n'
                'This status is related to TLM OFF. AMP/ICS/DTV shall be OFF. Audio '
                'for ANC, ACN, and chimes (if equipped) shall be active in this state)\n'
                'All TLM, AMP, ICS, and DTV functionalities run in background and are '
                'ready but not HMI interaction is enabled within this status, except '
                'for the interaction that permit a change status.\n'
                'the R1 HU shall not enter stolen vehicle mode under any condition'),
     "reasoning": (
         "驗證目標：Partial Operation 之三項性質與 Stolen Vehicle Mode 之否定規定。"
         "關鍵情境條件：收到 `STATUS_BH_BCM2.RemStActvSts = \"Remote Start Active\"`。"
         "為什麼這樣切：前三句同屬 Partial Operation 之狀態性質，"
         "而 `4941400` 為**否定規定**（不得進入 Stolen Vehicle Mode），"
         "其為 §12 第 1 列之 Negative 形態，依 §8.2.2 另拆一條。"
         "刻意略過：**DR-PW5 為 advisory**（不阻斷），其所指之範圍疑義不影響本條之撰寫。"),
     "tcs": [
         {"title": "Remote Start Active reports Partial_Operation with AMP, ICS and DTV off",
          "item": "Partial Operation entry reporting and subsystem state",
          "pre": [BENCH, 'The ignition working condition is Ignition On'],
          "data": 'STATUS_BH_BCM2.RemStActvSts = "Remote Start Active"',
          "proc": ["1. Send the signal listed in Input Test Data",
                   "2. Read $Telematic_Power$ and the AMP, ICS and DTV states to check the reported mode"],
          "er": ["1. The TLM registers the signal without a bus error",
                 '2. $Telematic_Power$ reads "Partial_Operation" and the AMP, ICS '
                 "and DTV are OFF"],
          "axis": ("trigger_state", "本條驗 Remote Start Active 之觸發與其後之子系統狀態")},
         {"title": "Partial Operation keeps ANC, ACN and chimes audio active",
          "item": "Audio exceptions in Partial Operation",
          "pre": [BENCH, '$Telematic_Power$ reads "Partial_Operation"',
                  'The unit is equipped with ANC, ACN and chimes'],
          "data": "NA",
          "proc": ["1. Read the audio output for ANC, ACN and chimes to check that they stay active"],
          "er": ["1. The audio for ANC, ACN and chimes is active"],
          "axis": ("trigger_state", "本條驗音訊之例外項")},
         {"title": "Partial Operation enables only the interaction that changes the status",
          "item": "HMI restriction in Partial Operation",
          "pre": [BENCH, '$Telematic_Power$ reads "Partial_Operation"'],
          "data": "NA",
          "proc": ["1. Attempt an HMI interaction that does not change the status",
                   "2. Attempt an HMI interaction that changes the status to check which one is enabled"],
          "er": ["1. The interaction that does not change the status is not enabled",
                 "2. The interaction that permits a status change is enabled"],
          "axis": ("trigger_state", "本條驗 HMI 互動之限制")},
         {"title": "The HU does not enter stolen vehicle mode under any condition",
          "item": "Stolen vehicle mode is never entered",
          "pre": [BENCH, 'The TLM is in an operative state'],
          "data": "NA",
          "proc": ["1. Attempt to bring the HU into stolen vehicle mode",
                   "2. Read the HU mode to check that it did not enter"],
          "er": ["1. The attempt is not accepted",
                 "2. The HU does not enter stolen vehicle mode"],
          "axis": ("trigger_state", "本條驗 Stolen Vehicle Mode 之否定規定")},
     ]},
    {"parent": "SWE-PM-004", "section": "1.6.2.1.5",
     "anchors": "4941403,4941404,4941406,4941663",
     "clause": ("This status is related to TLM ON.\nAll TLM AMP/ICS/DTV shall be ON "
                "and functionalities are available.\nEntering this state, TLM is ON "
                "for a limited time. See par. Phone Call management in Timed state "
                "for further details and par. Configuration parameters for Timeout1 "
                "details.\nIn “Timed Mode” the Customer setting screens shall be disabled."),
     "reasoning": (
         "驗證目標：Timed 狀態之 TLM ON 與全功能可用、其為限時、"
         "以及 Customer setting 畫面之停用。關鍵情境條件：TLM 處於 Timed。"
         "為什麼這樣切：功能可用性與 setting 畫面之停用為二個互不重疊之觀察對象，"
         "依 §8.2.2 各拆一條。"
         "刻意略過：Timeout1 之**確切時長**由 `Configuration parameters` 一節定義，"
         "其非本 leaf 之錨點；本條只驗「為限時」而不驗其值。"),
     "tcs": [
         {"title": "Timed keeps the TLM on with all functionalities available for a limited time",
          "item": "TLM ON and functionality availability in Timed",
          "pre": [BENCH, 'The ignition working condition is Ignition Off',
                  'TLM_Status.Info and $Telematic_Power$ read "Timed"'],
          "data": "NA",
          "proc": ["1. Read the TLM power indication and the AMP, ICS and DTV states",
                   "2. Read the TLM state again after Timeout1 has elapsed to check that the availability is limited"],
          "er": ["1. The TLM is ON and all TLM, AMP, ICS and DTV functionalities "
                 "are available",
                 "2. The availability is limited in time and does not continue "
                 "past Timeout1"],
          "axis": ("timing", "本條驗其限時性 —— 觀察於 Timeout1 之前與之後")},
         {"title": "Timed mode disables the Customer setting screens",
          "item": "Customer setting screens in Timed mode",
          "pre": [BENCH, 'TLM_Status.Info and $Telematic_Power$ read "Timed"'],
          "data": "NA",
          "proc": ["1. Attempt to open a Customer setting screen to check that it is disabled"],
          "er": ["1. The Customer setting screens are disabled"],
          "axis": ("trigger_state", "本條驗 Customer setting 畫面之停用")},
     ]},
    {"parent": "SWE-PM-005", "section": "1.6.2.1.6",
     "anchors": "4941411,4941412,4941413",
     "clause": ("This status is related to TLM OFF with Network on\nNo TLM, FPDM, "
                "AMP, ICS, and DTV functionality is available.\nEntering this state, "
                'TLM has to set Antitheft_Activation.Req to "False" value.'),
     "reasoning": (
         "驗證目標：Standby 之三項 —— TLM OFF 而網路仍 on、無任何功能可用、"
         "進入時將 `Antitheft_Activation.Req` 設為 `\"False\"`。"
         "關鍵情境條件：TLM 進入 Standby。為什麼這樣切：前二句為**狀態下之性質**、"
         "第三句為**進入時之動作**，其觀察時點不同（進入之際 vs 處於其中），"
         "依 §8.2.2 各拆一條。"
         "刻意略過：與 Sleep 之區分為「Network on 對 off」，"
         "該對照由 `SWE-PM-006` 承接（§8.2.1）。"),
     "tcs": [
         {"title": "Standby turns the TLM off while the network stays on",
          "item": "TLM off with network on in Standby",
          "pre": [BENCH, 'TLM_Status.Info and $Telematic_Power$ read "Standby"'],
          "data": "NA",
          "proc": ["1. Read the TLM power indication and the network state",
                   "2. Read the TLM, FPDM, AMP, ICS and DTV functionality availability to check that none is available"],
          "er": ["1. The TLM is OFF and the network is on",
                 "2. No TLM, FPDM, AMP, ICS or DTV functionality is available"],
          "axis": ("trigger_state", "本條驗處於 Standby 時之性質")},
         {"title": "Entering Standby clears the antitheft activation request",
          "item": "Antitheft_Activation.Req on entering Standby",
          "pre": [BENCH, 'Antitheft_Activation.Req reads "True"',
                  'The TLM is about to enter Standby'],
          "data": "NA",
          "proc": ["1. Let the TLM enter Standby",
                   "2. Read Antitheft_Activation.Req to check that it is cleared"],
          "er": ["1. The TLM enters Standby",
                 '2. Antitheft_Activation.Req reads "False"'],
          "axis": ("trigger_state", "本條驗進入 Standby 之際之動作")},
     ]},
    {"parent": "SWE-PM-006", "section": "1.6.2.1.7",
     "anchors": "4941417,4941418,4941419",
     "clause": ("This status is related to TLM OFF with Network off\nNo TLM, FPDM "
                "AMP, ICS, and DTV functionality is available.\nEntering this state, "
                'TLM has to set Antitheft_Activation.Req to "False" value.'),
     "reasoning": (
         "驗證目標：Sleep 之三項 —— TLM OFF 且網路亦 off、無任何功能可用、"
         "進入時將 `Antitheft_Activation.Req` 設為 `\"False\"`。"
         "關鍵情境條件：TLM 進入 Sleep。為什麼這樣切：同 `SWE-PM-005` 之切法 —— "
         "狀態性質與進入動作分屬不同觀察時點。"
         "**與 `SWE-PM-005` 之唯一區分為 Network off 對 on**，"
         "其為二個 leaf 各自之規定，依 §8.2.2 不合併。"),
     "tcs": [
         {"title": "Sleep turns the TLM off with the network off as well",
          "item": "TLM off with network off in Sleep",
          "pre": [BENCH, 'TLM_Status.Info and $Telematic_Power$ read "Sleep"'],
          "data": "NA",
          "proc": ["1. Read the TLM power indication and the network state",
                   "2. Read the TLM, FPDM, AMP, ICS and DTV functionality availability to check that none is available"],
          "er": ["1. The TLM is OFF and the network is off",
                 "2. No TLM, FPDM, AMP, ICS or DTV functionality is available"],
          "axis": ("trigger_state", "本條驗處於 Sleep 時之性質")},
         {"title": "Entering Sleep clears the antitheft activation request",
          "item": "Antitheft_Activation.Req on entering Sleep",
          "pre": [BENCH, 'Antitheft_Activation.Req reads "True"',
                  'The TLM is about to enter Sleep'],
          "data": "NA",
          "proc": ["1. Let the TLM enter Sleep",
                   "2. Read Antitheft_Activation.Req to check that it is cleared"],
          "er": ["1. The TLM enters Sleep",
                 '2. Antitheft_Activation.Req reads "False"'],
          "axis": ("trigger_state", "本條驗進入 Sleep 之際之動作")},
     ]},
    {"parent": "SWE-PM-007", "section": "1.6.2.1.8", "anchors": "4941422,4941423",
     "clause": ('In the "Ignition Working Conditions" "Ignition Off"\nThis status is '
                "related to TLM AMP, ICS, and DTV ON only for testing, diagnostics "
                "and development of TLM component, relatively to Engineering Line."),
     "reasoning": (
         "驗證目標：Bench 狀態於 Ignition Off 下，TLM/AMP/ICS/DTV 為 ON "
         "而其用途限於測試、診斷與開發，且繫於 Engineering Line。"
         "關鍵情境條件：Engineering Line 已啟用且 ignition 為 Off。"
         "為什麼這樣切：原文僅一個斷言（該狀態之性質與其限定用途），"
         "依 §5.7 為一條。"
         "刻意略過：「僅供測試」為**用途之限定**而非可觀察之行為，"
         "本條驗其**可觀察者** —— 於 Engineering Line 啟用時該等子系統為 ON。"),
     "tcs": [
         {"title": "Bench turns the AMP, ICS and DTV on for the Engineering Line",
          "item": "Subsystem state in Bench",
          "pre": [BENCH, 'The ignition working condition is Ignition Off',
                  'The Engineering Line is activated'],
          "data": "NA",
          "proc": ["1. Bring the TLM to the Bench state",
                   "2. Read the TLM, AMP, ICS and DTV states to check that they are on"],
          "er": ["1. The TLM reaches the Bench state",
                 "2. The TLM, AMP, ICS and DTV are ON"],
          "axis": ("mode", "本條驗 Engineering Line 之 bench 配置")},
     ]},
    {"parent": "SWE-PM-009", "section": "1.6.2.1.13",
     "anchors": "4941441,4941442,4941446,4941449,4941450",
     "clause": ('First default values for TLM are: TLM_Status.Info, $Telematic_Power$ '
                'equal to "Sleep" value; VPLastStatus equal to "On" value; '
                'SwitchOff_Timeout_Setting.Req equal to "00 min" == Timeout1 equal to '
                '00 minutes; Timeout1 equal to 00 minutes for LTM High '
                'Auto_SwitchOn_Setting.Req equal to "Recall_Last" value; '
                'Antitheft_Activation.Req equal to "False" value.\n'
                'RemStartFail equal to “False” value;\n'
                'IF the voltage exceeds the higher or the lower voltage threshold for '
                'a certain time, or also at every battery disconnection event,THEN TLM '
                'has to set itself in a INIT state, until certain conditions that allow '
                'TLM to exit from this status occur.\n'
                'After a battery reconnection and also when TLM has to exit INIT state '
                '(as soon as the voltage is limited within certain thresholds), TLM is '
                'able to work properly again and it has to restore the last user '
                'settings and the last variables values: VPLastStatus, '
                'SwitchOffSetting.Req, Auto_SwitchOn_Setting.Req shall be restored to '
                'their values before the battery disconnection / battery reset\n'
                'Then, TLM has to behave according to requirements of par. '
                '"TLM_Status.Info and $Telematic_Power$ signal setting", setting '
                'TLM_Status.Info to "Sleep" first and starting from Sleep state.'),
     "reasoning": (
         "驗證目標：Init 狀態之三事 —— 出廠預設值之內容、進入 INIT 之條件"
         "（電壓超限或斷電）、離開 INIT 後之還原與起始狀態。"
         "關鍵情境條件：斷電再接電。為什麼這樣切：預設值、進入條件、離開後之還原"
         "為三個不同之觀察時點，依 §8.2.2 各拆一條。"
         "**刻意略過：電壓門檻之數值與進出 INIT 之時間，原文明載其「refer to SIS」，"
         "SIS 不在本專案素材內** —— 依 §8.4.1 不造值，本批以「斷電事件」"
         "為進入 INIT 之可測觸發，不驗電壓門檻。"),
     "tcs": [
         {"title": "The ex-factory defaults are applied on the first power up",
          "item": "First default values",
          "pre": [BENCH, 'The unit carries the ex-factory configuration'],
          "data": "NA",
          "proc": ["1. Power up the TLM for the first time",
                   "2. Read TLM_Status.Info, VPLastStatus, "
                   "SwitchOff_Timeout_Setting.Req, Auto_SwitchOn_Setting.Req, "
                   "Antitheft_Activation.Req and RemStartFail to check the "
                   "ex-factory defaults"],
          "er": ['1. TLM_Status.Info and $Telematic_Power$ read "Sleep"',
                 '2. VPLastStatus reads "On", SwitchOff_Timeout_Setting.Req reads '
                 '"00 min", Auto_SwitchOn_Setting.Req reads "Recall_Last", '
                 'Antitheft_Activation.Req reads "False" and RemStartFail reads "False"'],
          "axis": ("trigger_state", "本條驗出廠預設值")},
         {"title": "A battery disconnection puts the TLM into the INIT state",
          "item": "INIT entry on battery disconnection",
          "pre": [BENCH, 'The TLM is running normally'],
          "data": "NA",
          "proc": ["1. Disconnect the battery",
                   "2. Read the TLM state to check that it entered INIT"],
          "er": ["1. The TLM registers the battery disconnection",
                 "2. The TLM sets itself in the INIT state"],
          "axis": ("trigger_state", "本條驗進入 INIT 之觸發")},
         {"title": "Leaving INIT restores the last settings and starts from Sleep",
          "item": "Restore and start state on leaving INIT",
          "pre": [BENCH, 'The TLM is in the INIT state after a battery disconnection',
                  'VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req '
                  'held known values before the disconnection'],
          "data": "NA",
          "proc": ["1. Reconnect the battery and let the TLM exit the INIT state",
                   "2. Read VPLastStatus, SwitchOffSetting.Req and "
                   "Auto_SwitchOn_Setting.Req",
                   "3. Read TLM_Status.Info to check the state the TLM starts from"],
          "er": ["1. The TLM exits the INIT state",
                 "2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req "
                 "are restored to their values before the disconnection",
                 '3. TLM_Status.Info is set to "Sleep" and the TLM starts from '
                 "the Sleep state"],
          "axis": ("timing", "本條驗離開 INIT **之後**之還原與起始狀態")},
     ]},
]


def main() -> None:
    tcs, leaves = [], []
    n = START
    for leaf in LEAVES:
        leaves.append({"parent": leaf["parent"], "source_anchor": leaf["anchors"],
                       "section": leaf["section"], "source_clause": leaf["clause"],
                       "reasoning": leaf["reasoning"]})
        multi = len(leaf["tcs"]) > 1
        for i, t in enumerate(leaf["tcs"], 1):
            ax, delta = t["axis"]
            tcs.append({
                "req_id": leaf["parent"],
                "tc_id": f"NR1L-PowerManagement-{n:03d}",
                "tc_title": t["title"],
                "test_group": "Power Management",
                "test_set": "Power State",
                "test_item": t["item"],
                "pre_conditions": "\n".join(t["pre"]),
                "input_test_data": t["data"],
                "test_procedure": "\n".join(t["proc"]),
                "expected_result": "\n".join(t["er"]),
                "specification_reference": f"{SPEC}_{leaf['section']}",
                "priority": "P0",
                "design_method": "決策表 (Decision Table Testing)",
                "split_flag": multi,
                "split_reason": (delta if multi else
                                 "原文為單一斷言，依 §5.7 為一條"),
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
                "distinguishing_axis": {"axis": ax, "delta": delta},
                "reasoning_note": "",
                "split_index": i,
            })
            n += 1
        if not multi:
            tcs[-1].pop("distinguishing_axis")     # R-P265：leaf 僅 1 條 TC
    out = {"batch": "batch_007_power_state_c", "test_group": "Power Management",
           "test_set": "Power State", "leaves": leaves, "tcs": tcs,
           "tc_id_status": "provisional",
           "tc_id_note": "臨時號，接續現行末號 260（R-P113(b)）；最終號於寫回時指派"}
    p = GEN / "batch_007_power_state_c.json"
    p.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"wrote {p.relative_to(ROOT)}")
    print(f"leaf {len(leaves)}、TC {len(tcs)}（{START}–{n - 1}）")
    for l in LEAVES:
        print(f"  {l['parent']}: {len(l['tcs'])} 條")


if __name__ == "__main__":
    main()
