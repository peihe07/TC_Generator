"""第四批產生器（R-P174）—— `SWE-PM-033`–`063` 之未產出者。

R-P174 之範圍 31 leaf，其中 6 leaf（`038` / `057` / `060`–`063`）
**已於第二批產出**，故本批實為 **25 leaf**（落差見上繳 §五）。

`leaves` 之 `section` / `source_anchor` / `source_clause` **全部機械取得**：
章節與 item 取自 `layer3_full.tsv`，原文取自 CFTS 文字層
（`lint_tcs.anchor_bodies()`，R-P17）—— `source_clause` 未經任何改寫，
G94 之逐字比對即以此為對象。

TC 內容為人所撰（下表 `TCS`），拆分依 §5.7 / §8.2.2；
`tc_id` 為批次內臨時號（R-P113(b)），接續第三批之末（`107`）。

用法：
    python features/power/scripts/gen_batch04.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DATA = ROOT / "features/power/data"
GENERATED = ROOT / "features/power/generated"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lint_tcs import anchor_bodies  # noqa: E402

SPEC = ("R1LR_Atl-H_25PI3.5_Activation and Configuration_"
        "CFTS_009_Wake-up and Power-up_SR26_20250909-1658")
SIM = "A LIN and CAN simulation tool is connected"
START_ID = 108           # 第三批之末為 107
BATCH = "batch_004_power_state_b"

# leaf -> [(title, pre[], data, proc[], er[], priority, split_reason)]
TCS: dict[str, list[tuple]] = {
    "SWE-PM-033": [
        ("Ignition Pre Off from Partial Operation passes the TLM to Standby",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Partial Operation"'],
         'LTM_OperationalModeSts: transition to "Ignition Pre Off"',
         ["Send the transition listed in Input Test Data",
          "Read TLM_Status.Info and $Telematic_Power$ to check the resulting state"],
         ["The TLM registers the transition without a bus error",
          'TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state'],
         "P0", "本條驗 OR 之左支 Ignition Pre Off"),
        ("Ignition Off from Partial Operation passes the TLM to Standby",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Partial Operation"'],
         'LTM_OperationalModeSts: transition to "Ignition Off"',
         ["Send the transition listed in Input Test Data",
          "Read TLM_Status.Info and $Telematic_Power$ to check the resulting state"],
         ["The TLM registers the transition without a bus error",
          'TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state'],
         "P0", "本條驗 OR 之右支 Ignition Off"),
    ],
    "SWE-PM-034": [
        ("Front panel press in Partial Operation arms the antitheft and shows the Splash Screen",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Partial Operation"'],
         'Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed"',
         ["Send the transition listed in Input Test Data",
          "Read the antitheft request and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "True"',
          "A proper Splash Screen is shown for Response_Wait_Time"],
         "P0", "本條驗 Partial Operation 之前面板觸發"),
    ],
    "SWE-PM-035": [
        ("Antitheft success with auto switch on active passes the TLM to Full-Operation",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Active"'],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request, the screen and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False" and a proper Splash Screen is shown for Response_Wait_Time',
          'VPLastStatus reads "On" and TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state'],
         "P0", "本條驗 Behaviour 1（Active）"),
        ("Antitheft success with auto switch on not active passes the TLM to Idle",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Not_Active"'],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          'VPLastStatus reads "Off" and TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state'],
         "P0", "本條驗 Behaviour 2（Not_Active）"),
        ("Antitheft success with recall last and last status on passes the TLM to Full-Operation",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Recall_Last"',
          'VPLastStatus reads "On"'],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the screen and the TLM state to check the resulting behavior"],
         ["A proper Splash Screen is shown for Response_Wait_Time",
          'TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state'],
         "P0", "本條驗 Behaviour 3 之 VPLastStatus On 分支"),
        ("Antitheft success with recall last and last status off passes the TLM to Idle",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Recall_Last"',
          'VPLastStatus reads "Off"'],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          'TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state'],
         "P0", "本條驗 Behaviour 3 之 VPLastStatus Off 分支"),
    ],
    "SWE-PM-036": [
        ("Remote start from Timed passes the TLM to Partial Operation",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Timed"'],
         'STATUS_BH_BCM2.RemStActvSts: "Remote Start Not Active" to "Remote Start Active"',
         ["Send the transition listed in Input Test Data",
          "Read the remote start outcome flags and the TLM state to check the resulting behavior"],
         ['RemStartFail reads "False" and VPLastStatus reads "On"',
          'TLM_Status.Info and $Telematic_Power$ read "Partial-Operation" and the TLM passes to TLM Partial Operation state'],
         "P0", "本條驗 Timed ＋ Remote Start → Partial Operation"),
    ],
    "SWE-PM-037": [
        ("Call end in Timed with a failed remote start passes the TLM to Standby",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Timed"',
          'RemStartFail reads "True"'],
         'PhoneCall.Info: "not Active"',
         ["Send the value listed in Input Test Data",
          "Read the remote start outcome flag and the TLM state to check the resulting behavior"],
         ['RemStartFail reads "False"',
          'TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state'],
         "P0", "本條驗 Timed ＋ 通話結束 ＋ RemStartFail 為真"),
    ],
    "SWE-PM-039": [
        ("An SNA operational mode is handled as an ignition off event",
         [SIM, "The TLM is in an Ignition On working condition"],
         'LTM_OperationalModeSts.Info: "SNA"',
         ["Send the value listed in Input Test Data",
          "Read the TLM state against the operative state management rules to check the resulting behavior"],
         ["The TLM registers the value without a bus error",
          "The TLM behaves as for an Ignition Pre Off or Ignition Off event"],
         "P1", "本條驗 SNA 之等同處置"),
        ("A zero switch off timeout loads Timeout1 from the PROXI value",
         [SIM, 'TLM_Status.Info was equal to "Full-Operation"'],
         'SwitchOff_Timeout_Setting.Req: "00 min"',
         ["Send the value listed in Input Test Data",
          "Read Timeout1 against the configured parameter to check the loaded value"],
         ["The TLM registers the value without a bus error",
          'Timeout1 reads the "Switch_Off_Time" PROXI value'],
         "P0", "本條驗 OR 之左支 SwitchOff_Timeout_Setting.Req"),
        ("Auto switch on active on LTM High Radio loads Timeout1 from the PROXI value",
         [SIM, 'TLM_Status.Info was equal to "Full-Operation"',
          "The unit is an LTM High Radio"],
         'Auto_SwitchOn_Setting.Req: "Active"',
         ["Send the value listed in Input Test Data",
          "Read Timeout1 against the configured parameter to check the loaded value"],
         ["The TLM registers the value without a bus error",
          'Timeout1 reads the "Switch_Off_Time" PROXI value'],
         "P0", "本條驗 OR 之右支 Auto_SwitchOn_Setting.Req for LTM High Radio"),
        ("Only TLM menu items are guaranteed in the Timed status",
         [SIM, "The TLM passed to Timed status due to the two conditions of this clause"],
         "NA",
         ["Browse the menu items offered by the TLM",
          "Read the offered items against the TLM HMI documents to check what is guaranteed"],
         ["The menu is reachable in the Timed status",
          "Only TLM menu items that are not related to vehicle setup are guaranteed"],
         "P1", "本條驗 Timed 狀態下之選單保證範圍"),
    ],
    "SWE-PM-040": [
        ("A normal power down into Suspend to RAM starts the 8 day timer",
         [SIM, "Suspend to RAM is allowed on the HU"],
         "NA",
         ["Bring the HU through a normal power down sequence",
          "Read the HU timer and its power mode to check the resulting behavior"],
         ["The HU starts an 8 day timer",
          "The HU enters low power mode"],
         "P0", "本條驗 Suspend to RAM 之正常關機序列"),
    ],
    "SWE-PM-041": [
        ("No TLM function is available in the TLM off with network on status",
         [SIM, "The TLM is in an Ignition Off working condition"],
         "NA",
         ["Bring the TLM to the status related to TLM OFF with Network on",
          "Read the FPDM, AMP, ICS and DTV functions to check their availability"],
         ["The TLM reaches the status related to TLM OFF with Network on",
          "No TLM, FPDM, AMP, ICS and DTV functionality is available"],
         "P0", "本條驗 Network on 狀態之功能不可用"),
        ("Entering the TLM off with network on status clears the antitheft request",
         [SIM, "The TLM is in an Ignition Pre Off working condition"],
         "NA",
         ["Bring the TLM to the status related to TLM OFF with Network on",
          "Read the antitheft request to check its value on entering the status"],
         ["The TLM reaches the status related to TLM OFF with Network on",
          'Antitheft_Activation.Req reads "False"'],
         "P0", "本條驗 Network on 狀態之進入動作"),
    ],
    "SWE-PM-042": [
        ("No TLM function is available in the TLM off with network off status",
         [SIM, "The TLM is in an Ignition Off working condition"],
         "NA",
         ["Bring the TLM to the status related to TLM OFF with Network off",
          "Read the FPDM, AMP, ICS and DTV functions to check their availability"],
         ["The TLM reaches the status related to TLM OFF with Network off",
          "No TLM, FPDM AMP, ICS and DTV functionality is available"],
         "P0", "本條驗 Network off 狀態之功能不可用"),
        ("Entering the TLM off with network off status clears the antitheft request",
         [SIM, "The TLM is in an Ignition Pre Off working condition"],
         "NA",
         ["Bring the TLM to the status related to TLM OFF with Network off",
          "Read the antitheft request to check its value on entering the status"],
         ["The TLM reaches the status related to TLM OFF with Network off",
          'Antitheft_Activation.Req reads "False"'],
         "P0", "本條驗 Network off 狀態之進入動作"),
    ],
    "SWE-PM-043": [
        ("The backlight stays off during Standby mode",
         [SIM, "The HU is in Standby mode", "No HMI screen is required"],
         "NA",
         ["Leave the HU in Standby mode without requesting an HMI screen",
          "Read the display backlight to check whether it stays off"],
         ["The HU stays in Standby mode",
          "The backlight is OFF"],
         "P0", "本條驗 Standby 之背光關閉常態"),
        ("The backlight is allowed during Standby when an HMI screen is required",
         [SIM, "The HU is in Standby mode"],
         "NA",
         ["Request an HMI screen to be displayed while the HU is in Standby mode",
          "Read the display backlight to check the exception of this clause"],
         ["The HMI screen is displayed",
          "The backlight is not kept OFF while the HMI screen is displayed"],
         "P1", "本條驗 except 分支 —— 需顯示 HMI 畫面時"),
    ],
    "SWE-PM-044": [
        ("Front panel press in Standby arms the antitheft and shows the Splash Screen",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Standby"',
          "The Engineering Line is deactivated"],
         'Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed"',
         ["Send the transition listed in Input Test Data",
          "Read the antitheft request and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "True"',
          "A proper Splash Screen is shown for Response_Wait_Time"],
         "P0", "本條驗 Front_Panel_OnOff.Req ＋ OR 之左支 Standby"),
        ("Front panel press in Sleep arms the antitheft and shows the Splash Screen",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Sleep"',
          "The Engineering Line is deactivated"],
         'Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed"',
         ["Send the transition listed in Input Test Data",
          "Read the antitheft request and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "True"',
          "A proper Splash Screen is shown for Response_Wait_Time"],
         "P0", "本條驗 Front_Panel_OnOff.Req ＋ OR 之右支 Sleep"),
        ("Climatic panel press in Standby arms the antitheft and shows the Splash Screen",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Standby"',
          "The Engineering Line is deactivated"],
         'CLIMATIC_PANEL.Radio_Btn0: "Not_Pressed" to "Pressed"',
         ["Send the transition listed in Input Test Data",
          "Read the antitheft request and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "True"',
          "A proper Splash Screen is shown for Response_Wait_Time"],
         "P0", "本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ OR 之左支 Standby"),
        ("Climatic panel press in Sleep arms the antitheft and shows the Splash Screen",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Sleep"',
          "The Engineering Line is deactivated"],
         'CLIMATIC_PANEL.Radio_Btn0: "Not_Pressed" to "Pressed"',
         ["Send the transition listed in Input Test Data",
          "Read the antitheft request and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "True"',
          "A proper Splash Screen is shown for Response_Wait_Time"],
         "P0", "本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ OR 之右支 Sleep"),
    ],
    "SWE-PM-045": [
        ("A failed antitheft keeps the TLM in the original Standby state",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Standby"'],
         'Antitheft_Result.Info: "Not_Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          "The TLM stays in the original Standby state for at most Timeout1, with proper HMI Antitheft screens"],
         "P0", "本條驗 OR 之左支 Standby"),
        ("A failed antitheft keeps the TLM in the original Sleep state",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Sleep"'],
         'Antitheft_Result.Info: "Not_Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          "The TLM stays in the original Sleep state for at most Timeout1, with proper HMI Antitheft screens"],
         "P0", "本條驗 OR 之右支 Sleep"),
    ],
    "SWE-PM-046": [
        ("Rear view camera is provided while the antitheft is still in progress",
         [SIM, 'The Rear_View_Camera PROXI parameter reads "Present"',
          'Rear_Camera_Enable.Info reads "True"'],
         'Antitheft_Result.Info: "In_Progress"',
         ["Send the value listed in Input Test Data",
          "Read the screen and the audio path to check the rear view camera component"],
         ["The TLM registers the value without a bus error",
          "The TLM provides audio and video for the rear view camera component as soon as the images are available"],
         "P0", "本條驗 OR 之左支 In_Progress"),
        ("Rear view camera is provided after an unsuccessful antitheft",
         [SIM, 'The Rear_View_Camera PROXI parameter reads "Present"',
          'Rear_Camera_Enable.Info reads "True"'],
         'Antitheft_Result.Info: "Not_Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the screen and the audio path to check the rear view camera component"],
         ["The TLM registers the value without a bus error",
          'The TLM provides audio and video for the rear view camera component as long as Rear_Camera_Enable.Info reads "True"'],
         "P0", "本條驗 OR 之右支 Not_Successfully"),
    ],
    "SWE-PM-047": [
        ("A failed antitheft keeps the TLM in Standby and shows the antitheft screens",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Standby"'],
         'Antitheft_Result.Info: "Not_Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request, the TLM state and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          "The TLM stays in the original Standby state and proper HMI Antitheft screens are shown if needed"],
         "P1", "本條驗 OR 之左支 Standby"),
        ("A failed antitheft keeps the TLM in Sleep and shows the antitheft screens",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Sleep"'],
         'Antitheft_Result.Info: "Not_Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request, the TLM state and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          "The TLM stays in the original Sleep state and proper HMI Antitheft screens are shown if needed"],
         "P1", "本條驗 OR 之右支 Sleep"),
    ],
    "SWE-PM-048": [
        ("Antitheft success with auto switch on active reaches Full-Operation after the mode transition",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Active"',
          "The LTM_OperationalModeSts.Info transition has occurred"],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          'TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state'],
         "P0", "本條驗 Behaviour 1（Active）"),
        ("Antitheft success with auto switch on not active reaches Idle after the mode transition",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Not_Active"',
          "The LTM_OperationalModeSts.Info transition has occurred"],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          'TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state'],
         "P0", "本條驗 Behaviour 2（Not_Active）"),
        ("Recall last with last status on reaches Full-Operation after the mode transition",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Recall_Last"',
          'VPLastStatus reads "ON"'],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the TLM state to check the resulting behavior"],
         ["The TLM registers the value without a bus error",
          'TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state'],
         "P0", "本條驗 Behaviour 3 之 VPLastStatus ON 分支"),
        ("Recall last with last status off reaches Idle after the mode transition",
         [SIM, 'Auto_SwitchOn_Setting.Req reads "Recall_Last"',
          'VPLastStatus reads "OFF"'],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the TLM state to check the resulting behavior"],
         ["The TLM registers the value without a bus error",
          'TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state'],
         "P0", "本條驗 Behaviour 3 之 VPLastStatus OFF 分支"),
        ("The ex-factory default selects recall last with the last status on",
         [SIM, "The TLM carries the ex-factory configuration"],
         "NA",
         ["Read the user selectable parameter on an ex-factory unit",
          "Read the stored last status to check the ex-factory default of this clause"],
         ['Auto_SwitchOn_Setting.Req reads "Recall_Last"',
          'VPLastStatus reads "On"'],
         "P1", "本條驗 Default 之出廠預設"),
    ],
    "SWE-PM-049": [
        ("A failed antitheft keeps the TLM blocked in Idle",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Idle"'],
         'Antitheft_Result.Info: "Not_Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request, the TLM state and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          "The TLM stays blocked in Idle state and proper HMI Antitheft screens are shown if needed"],
         "P0", "本條驗 Idle 之封鎖分支"),
    ],
    "SWE-PM-050": [
        ("The else branch stores the last status off and passes the TLM to Idle",
         [SIM, "The condition of the preceding clause of this chapter is not met"],
         "NA",
         ["Bring the TLM through the switch on sequence with that condition not met",
          "Read the stored last status and the TLM state to check the resulting behavior"],
         ['VPLastStatus reads "Off"',
          'TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to Idle state'],
         "P1", "本條驗 ELSE 分支"),
    ],
    "SWE-PM-051": [
        ("Antitheft success stores the last status on and passes the TLM to Full-Operation",
         [SIM, "The TLM is running the antitheft check"],
         'Antitheft_Result.Info: "Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request, the stored last status and the TLM state to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False" and VPLastStatus reads "On"',
          'TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state'],
         "P0", "本條驗 Successfully 分支"),
    ],
    "SWE-PM-052": [
        ("A failed antitheft keeps the TLM in the original Partial Operation state",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Partial Operation"'],
         'Antitheft_Result.Info: "Not_Successfully"',
         ["Send the value listed in Input Test Data",
          "Read the antitheft request, the TLM state and the screen to check the resulting behavior"],
         ['Antitheft_Activation.Req reads "False"',
          "The TLM stays in the original Partial Operation state and proper HMI Antitheft screens are shown if needed"],
         "P0", "本條驗 Partial Operation 之留置分支"),
    ],
    "SWE-PM-053": [
        ("The vehicle brand logo screen follows the brand configuration parameter",
         [SIM, "The TLM carries a configured brand parameter"],
         "NA",
         ["Bring the TLM to the brand logo screen presentation",
          "Read the shown logo against the configured parameter to check the source of the logo"],
         ["The brand logo screen is presented",
          "The vehicle brand logo shown matches the Brand_Configuration_2 PROXI parameter"],
         "P0", "本條驗 Brand_Configuration_2 之讀取"),
    ],
    "SWE-PM-054": [
        ("No audio brand without SDARS shows the vehicle brand logo only",
         [SIM, 'SDARS_Presence reads "Absent"'],
         'Audio_Brand: "No Audio Brand"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "The vehicle brand logo that depends on the Brand_Configuration_2 parameter value is shown alone"],
         "P0", "本條驗組合一（Absent ＋ No Audio Brand）"),
        ("Beats brand white without SDARS adds the Beats logo",
         [SIM, 'SDARS_Presence reads "Absent"'],
         'Audio_Brand: "Beats Brand White"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "The Beats Brand White logo is shown in addition to the vehicle brand logo"],
         "P0", "本條驗組合二（Absent ＋ Beats Brand White）"),
        ("SDARS present without audio brand adds the Sirius logo",
         [SIM, 'SDARS_Presence reads "Present"'],
         'Audio_Brand: "No Audio Brand"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "The Sirius logo is shown in addition to the vehicle brand logo"],
         "P0", "本條驗組合三（Present ＋ No Audio Brand）"),
        ("SDARS present with beats brand white adds both logos",
         [SIM, 'SDARS_Presence reads "Present"'],
         'Audio_Brand: "Beats Brand White"',
         ["Send the value listed in Input Test Data",
          "Read the shown logos to check the resulting presentation"],
         ["The brand logo screen is presented",
          "Both the Sirius and the Beats logos are shown in addition to the vehicle brand logo"],
         "P0", "本條驗組合四（Present ＋ Beats Brand White）"),
    ],
    "SWE-PM-055": [
        ("The special package drives the Klipsch Splash Screen on the 2025 model year",
         [SIM, 'The ETM carries $VC_MODEL_YEAR$ equal to "2025"',
          'The ETM carries $VC_VEH_LINE$ equal to "DT"'],
         '$VC_SpecialPKG_IC$: "Tungsten (147)"',
         ["Send the value listed in Input Test Data",
          "Read the shown Splash Screen to check which screen the ETM displays"],
         ["The ETM accepts the configuration value",
          "The Klipsch Splash Screen is displayed"],
         "P1", "本條驗 2025 年式之 $VC_SpecialPKG_IC$ 路徑"),
        ("The splash screen type drives the Klipsch Splash Screen after the 2025 model year",
         [SIM, 'The ETM carries $VC_MODEL_YEAR$ greater than "2025"',
          'The ETM carries $VC_VEH_LINE$ equal to "DT"'],
         '$SplashScreen_Type$: "Klipsch (7)"',
         ["Send the value listed in Input Test Data",
          "Read the shown Splash Screen to check which screen the ETM displays"],
         ["The ETM accepts the configuration value",
          "The Klipsch Splash Screen is displayed"],
         "P1", "本條驗 2025 年式之後之 $SplashScreen_Type$ 路徑"),
    ],
    "SWE-PM-056": [
        ("The Fiat Latam startup animation replaces the vehicle brand logo",
         [SIM, "The HU carries a configured vehicle brand"],
         'DID "Startup Animation Selection": "Fiat Latam"',
         ["Send the value listed in Input Test Data",
          "Read the shown logo against the configured brand to check which logo the HU displays"],
         ["The HU accepts the configuration value",
          "The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand"],
         "P1", "本條驗 Fiat Latam 之覆蓋規則"),
    ],
    "SWE-PM-058": [
        ("The ex-factory default sets a zero switch off timeout",
         [SIM, "The TLM carries the ex-factory configuration",
          "The unit is an LTM High Radio"],
         "NA",
         ["Read the user selectable timeout parameter on an ex-factory unit",
          "Read the auto switch on parameter and Timeout1 to check the ex-factory default of this clause"],
         ['SwitchOff_Timeout_Setting.Req reads "00 MIN"',
          'Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 MIN"'],
         "P1", "本條驗出廠預設值"),
    ],
    "SWE-PM-059": [
        ("A network sleep request in Standby passes the TLM to Sleep",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Standby"',
          "The boot of the TLM has been completed"],
         "A Network Sleep request",
         ["Send the request listed in Input Test Data",
          "Read the TLM state and the shutdown counter to check the resulting behavior"],
         ['TLM_Status.Info and $Telematic_Power$ read "Sleep" and the TLM passes to Sleep state',
          "Shutdown_Time starts"],
         "P0", "本條驗 boot 已完成之分支"),
        ("A network sleep request during boot is served only after the boot ends",
         [SIM, 'TLM_Status.Info and $Telematic_Power$ read "Standby"',
          "The boot of the TLM is not ended"],
         "A Network Sleep request",
         ["Send the request listed in Input Test Data",
          "Read the TLM state and the shutdown counter at the end of the boot to check the wait"],
         ["The TLM waits for the end of the boot before passing to Sleep state",
          "Shutdown_Time starts only after the end of the boot"],
         "P0", "本條驗 boot 未結束之等待分支"),
    ],
}

NOTES = {
    "SWE-PM-050": "本 leaf 之錨點原文以 `ELSE` 起首，其**前件不在本 leaf 之錨點內** ——"
                  "前提僅能寫成「前一條款之條件未成立」。已列為觀察，見上繳 §五。",
}


def layer3() -> dict[str, list[dict]]:
    out: dict[str, list[dict]] = {}
    rows = (DATA / "layer3_full.tsv").read_text(encoding="utf-8").splitlines()
    head = rows[0].split("\t")
    for line in rows[1:]:
        r = dict(zip(head, line.split("\t")))
        out.setdefault(r["leaf"], []).append(r)
    return out


def leaf_testset() -> dict[str, str]:
    out = {}
    for line in (DATA / "leaf_testset.tsv").read_text(encoding="utf-8").splitlines()[1:]:
        parts = line.split("\t")
        out[parts[0]] = parts[1]
    return out


def numbered(items: list[str]) -> str:
    return "\n".join(f"{i}. {s}" for i, s in enumerate(items, 1))


def main() -> None:
    l3, ts, bodies = layer3(), leaf_testset(), anchor_bodies()
    leaves, tcs = [], []
    n = START_ID
    for leaf in sorted(TCS):
        rows = l3[leaf]
        anchors = [a for r in rows for a in r["item_ids"].split(",")
                   if a and bodies.get(a)]
        secs = sorted({r["chapter_num"] for r in rows})
        leaves.append({
            "parent": leaf,
            "section": "、".join(secs),
            "source_anchor": ",".join(anchors),
            "source_clause": "\n".join("\n".join(bodies[a]) for a in anchors),
            "reasoning": NOTES.get(leaf, ""),
        })
        for idx, (title, pre, data, proc, er, prio, reason) in enumerate(TCS[leaf], 1):
            tcs.append({
                "req_id": leaf,
                "tc_id": f"NR1L-PowerManagement-{n:03d}",
                "tc_title": title,
                "test_group": "Power Management",
                "test_set": ts[leaf],
                "test_item": title,
                "pre_conditions": numbered(pre),
                "input_test_data": data,
                "test_procedure": numbered(proc),
                "expected_result": numbered(er),
                "specification_reference": f"{SPEC}_{secs[0]}",
                "priority": prio,
                "design_method": "狀態轉換 (State Transition Testing)",
                "split_flag": len(TCS[leaf]) > 1,
                "split_reason": reason,
                "functional_safety": "NA",
                "estimated_test_time": "",
                "remarks": "",
                "distinguishing_axis": {"axis": "behaviour", "delta": reason},
                "reasoning_note": NOTES.get(leaf, ""),
                "split_index": idx,
            })
            n += 1
    batch = {
        "batch": BATCH,
        "test_group": "Power Management",
        "test_set": "Power State / Startup Display",
        "tc_id_status": "provisional",
        "tc_id_note": "R-P113(b)：本批之 `tc_id` 為批次內臨時號，接續第三批之末（107）。"
                      "JSON 陣列序維持遞增（§10.3 / G38）；寫回列序另由 "
                      "(SWE-PM ID, split_index) 決定。",
        "scope_note": f"R-P174 令第四批為 `SWE-PM-033`–`063`（31 leaf）。"
                      f"**本批實含 {len(leaves)} leaf** —— 其餘 6 leaf"
                      f"（`SWE-PM-038`、`SWE-PM-057`、`SWE-PM-060`–`063`）"
                      f"**已於第二批產出**，未重複產出。落差見上繳 §五。",
        "leaves": leaves,
        "tcs": tcs,
    }
    path = GENERATED / f"{BATCH}.json"
    path.write_text(json.dumps(batch, ensure_ascii=False, indent=1) + "\n",
                    encoding="utf-8")
    print(f"wrote {path.relative_to(ROOT)} — {len(leaves)} leaf / {len(tcs)} TC "
          f"（{tcs[0]['tc_id']} – {tcs[-1]['tc_id']}）")


if __name__ == "__main__":
    main()
