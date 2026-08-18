# B1 / B2 —— 第一級改值紀錄（R-P256 / R-P257）

> 模式：**套用**；改動 **62** 處。

| 項 | 條數 |
|---|---|
| (B2) SWE-PM-025 觸發具名 | **8** |
| (a) axis | **31** |
| (b) split_index=0 | **4** |
| (c) split_flag 單條 | **9** |
| (d) remarks 補註 | **8** |
| (e) delta 重複 | **2** |

| 項 | tc | 欄 | 舊值 | 新值 |
|---|---|---|---|---|
| (a) axis | `…-001` | `distinguishing_axis.axis` | trigger_state | mode |
| (a) axis | `…-002` | `distinguishing_axis.axis` | trigger_state | mode |
| (a) axis | `…-003` | `distinguishing_axis.axis` | trigger_state | mode |
| (a) axis | `…-009` | `distinguishing_axis.axis` | trigger_state | mode |
| (a) axis | `…-014` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-023` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-024` | `distinguishing_axis.axis` | behaviour | mode |
| (c) split_flag 單條 | `…-028` | `split_flag` | true | false |
| (d) remarks 補註 | `…-033` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (d) remarks 補註 | `…-034` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (d) remarks 補註 | `…-035` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (d) remarks 補註 | `…-036` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (d) remarks 補註 | `…-038` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (d) remarks 補註 | `…-040` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (d) remarks 補註 | `…-041` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (d) remarks 補註 | `…-043` | `remarks` | "" | "DR-PW10 待範圍確認" |
| (a) axis | `…-046` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-048` | `distinguishing_axis.axis` | behaviour | mode |
| (b) split_index=0 | `…-053` | `split_index` | 0 | 2 |
| (b) split_index=0 | `…-054` | `split_index` | 0 | 3 |
| (b) split_index=0 | `…-055` | `split_index` | 0 | 4 |
| (a) axis | `…-060` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-064` | `distinguishing_axis.axis` | branch | trigger_state |
| (a) axis | `…-067` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (a) axis | `…-069` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (c) split_flag 單條 | `…-071` | `split_flag` | true | false |
| (c) split_flag 單條 | `…-072` | `split_flag` | true | false |
| (a) axis | `…-075` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (a) axis | `…-076` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (c) split_flag 單條 | `…-082` | `split_flag` | true | false |
| (c) split_flag 單條 | `…-083` | `split_flag` | true | false |
| (c) split_flag 單條 | `…-084` | `split_flag` | true | false |
| (c) split_flag 單條 | `…-085` | `split_flag` | true | false |
| (a) axis | `…-086` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (B2) SWE-PM-025 觸發具名 | `…-087` | `test_procedure` | "1. Accept the popup as the user\n2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby" | "1. Accept the Front_Panel_OnOff.Req popup as the user\n2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby" |
| (B2) SWE-PM-025 觸發具名 | `…-087` | `pre_conditions` | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown" | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown after the Front_Panel_OnOff.Req press" |
| (B2) SWE-PM-025 觸發具名 | `…-088` | `test_procedure` | "1. Decline the popup as the user\n2. Read TLM_Status.Info to check that Timed state is kept" | "1. Decline the Front_Panel_OnOff.Req popup as the user\n2. Read TLM_Status.Info to check that Timed state is kept" |
| (B2) SWE-PM-025 觸發具名 | `…-088` | `pre_conditions` | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown" | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown after the Front_Panel_OnOff.Req press" |
| (a) axis | `…-089` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (B2) SWE-PM-025 觸發具名 | `…-091` | `test_procedure` | "1. Accept the popup as the user\n2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby" | "1. Accept the CLIMATIC_PANEL.Radio_Btn0 popup as the user\n2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby" |
| (B2) SWE-PM-025 觸發具名 | `…-091` | `pre_conditions` | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown" | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown after the CLIMATIC_PANEL.Radio_Btn0 press" |
| (B2) SWE-PM-025 觸發具名 | `…-092` | `test_procedure` | "1. Decline the popup as the user\n2. Read TLM_Status.Info to check that Timed state is kept" | "1. Decline the CLIMATIC_PANEL.Radio_Btn0 popup as the user\n2. Read TLM_Status.Info to check that Timed state is kept" |
| (B2) SWE-PM-025 觸發具名 | `…-092` | `pre_conditions` | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown" | "1. A LIN and CAN simulation tool is connected\n2. TLM_Status.Info and $Telematic_Power$ read \"Timed\"\n3. The transfer popup is shown after the CLIMATIC_PANEL.Radio_Btn0 press" |
| (b) split_index=0 | `…-097` | `split_index` | 0 | 4 |
| (a) axis | `…-098` | `distinguishing_axis.axis` | behaviour | timing |
| (a) axis | `…-105` | `distinguishing_axis.axis` | behaviour | timing |
| (c) split_flag 單條 | `…-110` | `split_flag` | true | false |
| (c) split_flag 單條 | `…-111` | `split_flag` | true | false |
| (a) axis | `…-123` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (a) axis | `…-130` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-133` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-135` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-137` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-141` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-142` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-144` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-174` | `distinguishing_axis.axis` | behaviour | trigger_state |
| (a) axis | `…-178` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-207` | `distinguishing_axis.axis` | behaviour | mode |
| (a) axis | `…-209` | `distinguishing_axis.axis` | behaviour | mode |
| (e) delta 重複 | `…-002` | `distinguishing_axis.delta` | 本條驗抑制分支：轉往 Standby 或 Bench 時不得顯示 splash，… |  時不得顯示 splash，與 -01 為互斥條件；本條之分支為：Standby |
| (e) delta 重複 | `…-003` | `distinguishing_axis.delta` | 本條驗抑制分支：轉往 Standby 或 Bench 時不得顯示 splash，… | ch 時不得顯示 splash，與 -01 為互斥條件；本條之分支為：Bench |
