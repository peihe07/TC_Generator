# 53 包 — 錨點歸屬複核素材（R-P345(b)）

母體：**須判斷者 155 條**（另 125 條之 leaf 只有一個錨點，歸屬唯一，不入母體）。
抽樣：**31 / 155 = 20.0%**，種子 **53**。
排列：**按 leaf 交錯**（round-robin），非依序 —— R-P316 之教訓。

提案由 `scripts/propose_anchor_53.py` 產生，自驗 **5 / 6**（R-P250 之六條人讀實例）。
**其為提案非裁決**；不符者於 54 包訂正（R-P345(c)）。

| # | tc_id | leaf | 候選數 | 提案錨點 | F1 | 依據（`split_reason` 逐字） | 錨點文字（前 90 字） |
|---|---|---|---|---|---|---|---|
| 1 | `NR1L-PowerManagement-096` | `SWE-PM-026` | 3 | `4941576` | 0.18 | 本條驗守衛條件之否定側（非 Jeep）——（R-P198(b) 補測） | IF previous internal state TLM_Status.Info == "Full-Operation" AND PhoneCall.Info == "Not_ |
| 2 | `NR1L-PowerManagement-176` | `SWE-PM-093` | 2 | `4941301` | 0.21 | 本條驗 OR 之 PARTIAL OPERATION MODE 支 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when driver door |
| 3 | `NR1L-PowerManagement-195` | `SWE-PM-101` | 4 | `4941676` | 0.48 | 本條驗組合四（Present ＋ Beats Brand White） | - IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to sho |
| 4 | `NR1L-PowerManagement-030` | `SWE-PM-065` | 2 | `4941720` | 0.45 | 本條驗還原音源分支 | Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Time |
| 5 | `NR1L-PowerManagement-123` | `SWE-PM-041` | 4 | `4941412` | 0.56 | 本條驗 Network on 狀態之功能不可用 | No TLM, FPDM, AMP, ICS, and DTV functionality is available. |
| 6 | `NR1L-PowerManagement-126` | `SWE-PM-042` | 4 | `4941417` | 0.53 | 本條驗 Network off 狀態之進入動作 | This status is related to TLM OFF with Network off |
| 7 | `NR1L-PowerManagement-267` | `SWE-PM-003` | 9 | `4941392` | 0.51 | 本條驗 Remote Start Active 之觸發與其後之子系統狀態 | In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation". This mode sh |
| 8 | `NR1L-PowerManagement-042` | `SWE-PM-038` | 13 | `4941731` | 0.50 | 本條驗 Case 4 之另一觸發：點火轉為 "Ignition Pre Off"（`040` 驗 "Ignition Off"） | Case 4:IF Timeout1 == 00 minutesAND in Full-Operation state Phone_Call.Info signal is equa |
| 9 | `NR1L-PowerManagement-173` | `SWE-PM-076` | 4 | `4941867` | 0.63 | 本條驗韌體安裝中之例外 | If the HU is currently installing a firmware image the HU shall not reset due to a power b |
| 10 | `NR1L-PowerManagement-050` | `SWE-PM-012` | 2 | `4941450` | 0.27 | 本條驗離開 INIT 後之起始狀態 | Then, TLM has to behave according to requirements of par. "TLM_Status.Info and $Telematic_ |
| 11 | `NR1L-PowerManagement-102` | `SWE-PM-029` | 4 | `4941589` | 0.40 | 本條驗本變體之請求復歸 | AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and it passes to |
| 12 | `NR1L-PowerManagement-141` | `SWE-PM-048` | 5 | `4941605` | 0.51 | 本條驗 Behaviour 3 之 VPLastStatus ON 分支 | Behaviour 1: "Auto_SwitchOn_Setting.Req == Active"After the LTM_OperationalModeSts.Info tr |
| 13 | `NR1L-PowerManagement-048` | `SWE-PM-011` | 8 | `4941375` | 0.56 | 本條驗長按之觸發（`051` 驗短按）——`4941376` 載二者皆為該定義所指 | While the HU is in IDLE mode, the HU shall transition to Full-Operation mode if the VR but |
| 14 | `NR1L-PowerManagement-101` | `SWE-PM-028` | 3 | `4941581` | 0.42 | 本條驗 LTM High 形態之 Timeout1 取值（`100` 之對應條驗 SwitchOff_Timeout_Setting.Req | IF SwitchOff_Timeout_Setting.Req == 00 min or ( If Auto_SwitchOn_Setting.Req =="Active ",  |
| 15 | `NR1L-PowerManagement-109` | `SWE-PM-033` | 2 | `4941634` | 0.49 | 本條驗 OR 之左支 Ignition Pre Off | IF TLM_Status.Info and $Telematic_Power$ == "Partial Operation"AND signal LTM_OperationalM |
| 16 | `NR1L-PowerManagement-280` | `SWE-PM-009` | 11 | `4941449` | 0.51 | 本條驗離開 INIT **之後**之還原與起始狀態 | After a battery reconnection and also when TLM has to exit INIT state (as soon as the volt |
| 17 | `NR1L-PowerManagement-263` | `SWE-PM-002` | 10 | `4941365` | 0.26 | 本條驗音訊與畫面之限制 | This status is related to TLM audio is OFF. TLM shall allow only Splash Screen visualizati |
| 18 | `NR1L-PowerManagement-188` | `SWE-PM-099` | 2 | `4941945` | 0.27 | 本條驗「新的一天」之判定 —— 手動調整 | For the purposes of CFTS009-2299, the HU shall consider it a new "day" to allow the sound  |
| 19 | `NR1L-PowerManagement-277` | `SWE-PM-007` | 5 | `4941423` | 0.41 | 原文為單一斷言，依 §5.7 為一條 | This status is related to TLM AMP, ICS, and DTV ON only for testing, diagnostics and devel |
| 20 | `NR1L-PowerManagement-068` | `SWE-PM-015` | 4 | `4941542` | 0.61 | 本條驗 Front_Panel_OnOff.Req 於 Rear_View_Camera 存在而未啟動時之分支 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_Panel_OnOff.R |
| 21 | `NR1L-PowerManagement-274` | `SWE-PM-005` | 7 | `4941413` | 0.45 | 本條驗進入 Standby 之際之動作 | Entering this state, TLM has to set Antitheft_Activation.Req to "False" value. |
| 22 | `NR1L-PowerManagement-087` | `SWE-PM-025` | 6 | `4941570` | 0.29 | 本條驗 Front_Panel_OnOff.Req popup 之拒絕分支 | In this case, IF user accepts, TLM shall set TLM_Status.Info and $Telematic_Power$ to “Sta |
| 23 | `NR1L-PowerManagement-079` | `SWE-PM-020` | 2 | `4941559` | 0.30 | 本條驗通話結束於 Phone Main Screen 之分支 | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in Phone Main  |
| 24 | `NR1L-PowerManagement-098` | `SWE-PM-027` | 2 | `4941642` | 0.44 | 本條驗防盜失敗於 Partial Operation 之停留 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_Activation.R |
| 25 | `NR1L-PowerManagement-019` | `SWE-PM-057` | 9 | `4941692` | 0.43 | 本條驗 PROXI "Switch_Off_Time" = 180 分鐘時之可選集合與 Timeout1 結果 | IF "Switch_Off_Time" parameter is set to "20 minutes" then the user can select SwitchOff_T |
| 26 | `NR1L-PowerManagement-203` | `SWE-PM-104` | 2 | `4941950` | 0.59 | 本條驗首次進入 Timed | The splash screen and disclaimer screen shall be shown the first time each bus cycle the H |
| 27 | `NR1L-PowerManagement-152` | `SWE-PM-054` | 4 | `4941676` | 0.48 | 本條驗組合四（Present ＋ Beats Brand White） | - IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TLM has to sho |
| 28 | `NR1L-PowerManagement-262` | `SWE-PM-001` | 6 | `4941360` | 0.37 | 本條驗其餘四種 ignition 條件之取值 | All TLM, AMP/ICS/DTV functionalities are available. |
| 29 | `NR1L-PowerManagement-132` | `SWE-PM-044` | 2 | `4941584` | 0.30 | 本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ OR 之右支 Sleep | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND CLIMATIC_PANEL.Radio_B |
| 30 | `NR1L-PowerManagement-158` | `SWE-PM-059` | 2 | `4941617` | 0.42 | 本條驗 boot 未結束之等待分支 | If TLM Boot is not ended, TLM has to wait for its end before passing to Sleep state and st |
| 31 | `NR1L-PowerManagement-076` | `SWE-PM-019` | 6 | `4941555` | 0.47 | 本條驗 CLIMATIC_PANEL.Radio_Btn0 於後視攝影機啟用時被忽略 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal CLIMATIC_PANEL.Radio_Btn0 has |

## 風險（R-P345(d)）

**改值先於複核** —— 280 條之 `test_item` 已於本包寫入，其首段即依上表之提案。
若複核不符，須二次改值；以自驗 5 / 6 推，155 條中約 **26 條**可能有誤，本抽樣預期可捕獲約 **5 條**。
