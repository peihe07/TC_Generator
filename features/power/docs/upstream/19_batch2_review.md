# 上繳包 19 —— 第二批覆核與錨點完整性

> 對應下放包：`features/power/docs/handoff/19_batch2_review.md`
> 執行層：Claude（TC_Generator）
> **§J 自檢已先驗**：§A fenced block = **9**、§J 列數 = **9**、§H 步驟 10 = 「**九條**」——
> **三處一致，未停。**
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；
> **未觸碰客戶樹與 `inputs/`**；**未啟動第三批**；
> **未合併或拆分任何 TC**；**未改標 G95 凍結窗格類別**；
> **G73 之剝除僅限本專案自己強制加入之驗證意圖子句**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

**編號查核（§H 步驟 2，先查後開）**：
開新號前之現行最大號為 **A-PW95**、**R-P132**、**DR-PW8**、閘門 **G98**。
本包新號自 **A-PW96**、**R-P133**、**G99** 起，無衝突。**本包無新增 DR。**

---

## 一、B1 —— 第二批 26 條全文（R-P140，置於最前）

以 `batch_002_timeout_settings.json` 之原文分段附上，每段不逾 8 條。
首批 17 條依明令不重附。

**本包對第二批之異動僅一處**：`SWE-PM-063` 之 `reasoning` 補入 §8.2.1 委出清單（R-P137）。
其餘 26 條之十六欄**一字未改**。

### 1.0 `leaves` 陣列（8 leaf，含 `source_anchor` / `source_clause` / `reasoning`）

```json
[
  {
    "parent": "SWE-PM-057",
    "section": "1.6.2.1.17; 1.6.3.1.1; 1.8.1.1.1",
    "source_anchor": "4941692,4941693,4941695,4941706,4941707,4941708,4941814,4941815,4941817",
    "source_clause": "IF \"Switch_Off_Time\" parameter  is set  to \"20 minutes\"  then the user can select SwitchOff_Timeout_Setting.Req to \"00 min\" OR to \"20 min\" in TLM menu; so Timeout1 is equal to \"00 min\" OR \"20 minutes\" respectively.\nIF \"Switch_Off_Time\" parameter  is set  to \"60 minutes\"  then the user can select SwitchOff_Timeout_Setting.Req to \"00 min\" OR to \"60 min\" in TLM menu; so Timeout1 is equal to \"00 min\" OR \"60 minutes\" respectively.\nIF \"Switch_Off_Time\" parameter  is set  to \"180 minutes\"  then the user can select SwitchOff_Timeout_Setting.Req to \"00 min\" OR to \"180 min\" in TLM menu; so Timeout1 is equal to \"00 min\" OR \"180 minutes\" respectively.\nFor the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to \"00 minutes\" OR equal to the value specified by PROXI parameter \"Switch_Off_Time\". For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section\nTimeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Setting.Req.\nSo, user can set SwitchOff_Timeout_Setting.Req to \"00 minutes\" OR to \"20 minutes\" IF PROXI parameter \"Switch_Off_Time\" is equal to \"20 minutes\".\nIF \"Switch_Off_Time\" parameter  is set  to \"20 minutes\"  then the user can select SwitchOff_Timeout_Setting.Req to \"00 min\" OR to \"20 min\" in TLM menu; so Timeout1 is equal to \"00 min\" OR \"20 minutes\" respectively.\nIF \"Switch_Off_Time\" parameter  is set  to \"60 minutes\"  then the user can select SwitchOff_Timeout_Setting.Req to \"00 min\" OR to \"60 min\" in TLM menu; so Timeout1 is equal to \"00 min\" OR \"60 minutes\" respectively.\nIF \"Switch_Off_Time\" parameter  is set  to \"180 minutes\"  then the user can select SwitchOff_Timeout_Setting.Req to \"00 min\" OR to \"180 min\" in TLM menu; so Timeout1 is equal to \"00 min\" OR \"180 minutes\" respectively.",
    "reasoning": "驗證目標：`Timeout1` 之可選值由 PROXI 參數 `Switch_Off_Time` 決定，使用者經 TLM menu 以 `SwitchOff_Timeout_Setting.Req` 於「00 min」與該 PROXI 值之間擇一。為什麼這樣切：三個 PROXI 值（20 / 60 / 180 分）為三組獨立之可選集合，依 §8.2.2 各拆一條；`4941814` / `4941815` / `4941817`（§1.8.1.1.1）與 `4941692` / `4941693` / `4941695`（§1.6.2.1.17）**逐字相同**，屬同一行為之重複登載，不另拆條。刻意略過：`4941706` 之「LTM High Radio present」分支明指另一節（Auto_SwitchOn_Setting.Req management），依 R-P42 不在本 leaf 之錨點範圍。　**R-P132(b) 歸屬檢驗（18 包）**：本 leaf 之九個錨點原文**全部**述及 `SwitchOff_Timeout_Setting.Req` 與 `Timeout1`，即 Timeout Settings 之核心對象；037 之 Requirement Title 雖為 `Proxi Parameter management`，其行為確屬 Timeout Settings。**R-P34 之歸屬經本批實際撰寫檢驗為正確，無須停並上繳。**"
  },
  {
    "parent": "SWE-PM-060",
    "section": "1.6.3.1",
    "source_anchor": "4941702",
    "source_clause": "For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.Req. For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu.",
    "reasoning": "驗證目標：可設定之逾時參數數量隨 Radio 型別而異 —— LTM/ETM 一個、其餘兩個。為什麼這樣切：二型別為不同前提下之不同可觀察結果，依 §8.3 以 Radio 型別為軸拆為兩條。"
  },
  {
    "parent": "SWE-PM-061",
    "section": "1.6.3.1",
    "source_anchor": "4941703",
    "source_clause": "These settings could be only done in TLM Full-Operation Status.",
    "reasoning": "驗證目標：該等設定僅得於 TLM Full-Operation 狀態進行。為什麼這樣切：肯定分支（Full-Operation 可設定）與否定分支（非 Full-Operation 不可設定）為兩個獨立部分失效，依 §7 拆為兩條 —— 僅驗肯定側則「任何狀態皆可設定」之實作亦會通過。"
  },
  {
    "parent": "SWE-PM-062",
    "section": "1.6.3.1.2",
    "source_anchor": "4941710",
    "source_clause": "User can select Auto_SwitchOn_Setting.Req value equal to \"Active\" (If LTM High is present: \"Timeout1\" = \"00 minutes\");\"Not_Active (If LTM High is present:\"Timeout1\" <> \"00 minutes\");\"Recall_Last\" (If LTM High is present:\"Timeout1 = \"00 minutes\")",
    "reasoning": "驗證目標：`Auto_SwitchOn_Setting.Req` 之三個可選值及其於 LTM High 存在時對 `Timeout1` 之條件。為什麼這樣切：三值為三個獨立之使用者選擇與其後果，依 §8.2.2 各拆一條。"
  },
  {
    "parent": "SWE-PM-063",
    "section": "1.6.4.1",
    "source_anchor": "4941715",
    "source_clause": "In Timed state, it is possible either to make and to receive one or more bluetooth phone calls according to following logics that depend on Timeout1 and on MaxCallTimeout time parameters.",
    "reasoning": "驗證目標：Timed 狀態下得撥出與接聽藍牙通話。為什麼這樣切：本錨點為概括陳述，其細部邏輯由 `SWE-PM-064` / `065` / `038` 之錨點承載；本條僅驗「Timed 狀態下通話功能可用」此一可觀察事實，不重複測其後續轉換。　**§8.2.1 委出清單（R-P137，19 包）**：本錨點之「according to following logics that depend on Timeout1 and on MaxCallTimeout time parameters」所指之細部邏輯，逐項委由下列 sibling Req 承擔，各有具體 TC：\n（1）`Timeout1` 之可選值與其由 PROXI `Switch_Off_Time` 決定 → **`SWE-PM-057`**（`NR1L-PowerManagement-018` / `019` / `020`）；\n（2）`Auto_SwitchOn_Setting.Req` 對 `Timeout1` 之條件 → **`SWE-PM-062`**（`025` / `026` / `027`）；\n（3）`MaxCallTimeout` 之兩個啟動條件 → **`SWE-PM-064`**（`029` / `030`）；\n（4）通話於 `Timeout1` 到期前結束之邏輯（還原音源、續管理其他通話）→ **`SWE-PM-065`**（`031` / `032`）；\n（5）Case 1–4 之完整轉換邏輯與其離開路徑 → **`SWE-PM-038`**（`033`–`043`，共 11 條）。\n本 leaf 自身僅保留該錨點之**可獨立觀察面**：「Timed 狀態下得撥出與接聽藍牙通話」（`028`）。**上開五項皆可指出承擔之 leaf 與 TC id，故本項為『已由他 leaf 涵蓋』而非未涵蓋。**"
  },
  {
    "parent": "SWE-PM-064",
    "section": "1.6.4.1",
    "source_anchor": "4941718",
    "source_clause": "MaxCallTimeout starts in the following two conditions: Timeout1 == 00 min: IF Phone_Call.Info is equal to “Active” in TLM Full-Operation state, AND the Ignition working condition switches to \"Ignition Pre Off\" OR to \"Ignition Off\";   Timeout1 <> 00 min: at Timeout1 expiration, only IF Phone_Call.Info is still equal to “Active”;",
    "reasoning": "驗證目標：`MaxCallTimeout` 之兩個啟動條件。為什麼這樣切：二條件之觸發前提不同（`Timeout1 == 00 min` 之點火轉換 vs `Timeout1 <> 00 min` 之 Timeout1 到期），依 §5.7 不同觸發即拆分。"
  },
  {
    "parent": "SWE-PM-065",
    "section": "1.6.4.1",
    "source_anchor": "4941720,4941721",
    "source_clause": "Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to \"Not_Active\" before \"Timeout1” expiration THEN TLM has to restore the active source managed by TLM before the call (for example entertainment features like DAB Tuner, rather than USB or BT streaming audio) staying still in Timed state.\nIn this case, TLM is still able to manage other possible phone calls within Timeout1 expiration.",
    "reasoning": "驗證目標：Case 1 —— `Timeout1 <> 00 min` 且通話於 Timeout1 到期前結束時，還原通話前之音源並續留 Timed。為什麼這樣切：還原音源（`4941720`）與 Timeout1 到期前仍可處理其他通話（`4941721`）為兩個獨立部分失效，依 §8.2.2 拆為兩條。"
  },
  {
    "parent": "SWE-PM-038",
    "section": "1.6.4.1",
    "source_anchor": "4941722,4941723,4941724,4941725,4941726,4941727,4941728,4941729,4941730,4941731,4941732,4941735,4941736",
    "source_clause": "Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to \"Not_Active\" before \"Timeout1” expiration THEN\nIF RemStartFail = ”True” TLM has to stop its active functionality (Media audio streaming, tuner, etc) and has to set RemStartFail  to “False” value and  TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state\nELSE TLM has to restore the active source managed by TLM before the call (for example entertainment features like DAB Tuner, rather than USB or BT streaming audio) staying still in Timed state.\nIn this case, TLM is still able to manage other possible phone calls within Timeout1 expiration.\nCase 2:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info is still \"Active\" at \"Timeout1\" expirationTHENat Timeout1 expiration TLM starts MaxCallTimeout AND stays still in Timed state until Phone_Call.Info passes to \"Not_Active\" OR at maximum until MaxCallTimeout expiration.\nWHEN Phone_Call.Info passes to \"Not_Active\", OR at MaxCallTimeout expiration, TLM sets TLM_Status.Info to \"Standby\" value and then it passes to Standby state.\nWHEN Phone_Call.Info passes to \"Not_Active\", OR at MaxCallTimeout expiration, TLM has to set RemStartFail  to “False” value and TLM_Status.Info to \"Standby\" value and then it passes to Standby state.\nCase 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == \"Not_Active\" at Timeout1 expiration THENTLM has to set TLM_Status.Info to “Standby” value and to pass to Standby state.\nCase 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == \"Not_Active\" at Timeout1 expiration THENTLM has to set RemStartFail to \"False\" value and TLM_Status.Info to “Standby” value and to pass to Standby state.\nCase 4:IF Timeout1 == 00 minutesAND in Full-Operation state Phone_Call.Info signal is equal to \"Active\" AND the ignition working condition passes to \"Ignition Pre Off\" OR to \"Ignition Off\"THENTLM has to pass in Timed state starting MaxCallTimeout counter.\nIn this case, TLM has to manage the phone call(s) and to stay in Timed state until Phone_Call.Info passes to \"Not_Active\" value OR at maximum until MaxCallTimeout expires.\nIF any of the previous condition occurs, THEN TLM has to set TLM_Status.Info to “Standby” value and to pass to Standby state.\nIF any of the previous condition occurs, THEN TLM has to set RemStartFail to “False” value  and  TLM_Status.Info to “Standby” value and to pass to Standby state.",
    "reasoning": "驗證目標：Standby 與 Timed 狀態下之通話管理四個 Case 及其 `RemStartFail` 變體。為什麼這樣切：Case 1–4 為四個互斥之進入條件（§5.7 不同觸發即拆分）；各 Case 之離開路徑（通話結束 vs `MaxCallTimeout` 到期）與 `RemStartFail` 之處置為獨立部分失效，依 §8.2.2 再拆。`4941727` / `4941728`、`4941729` / `4941730`、`4941735` / `4941736` 三組各為「不含 / 含 `RemStartFail` 處置」之成對錨點，各自成條。刻意略過：`$Telematic_Power$` 之訊號定義未見於本 leaf 之錨點，依 §8.4.1 不造值，ER 僅述其被設為「Standby」。"
  }
]
```


### 第 1 段（018–024，7 條）

```json
[
  {
    "req_id": "SWE-PM-057",
    "tc_id": "NR1L-PowerManagement-018",
    "tc_title": "Timeout1 options follow PROXI \"Switch_Off_Time\" set to 20 minutes",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Timeout1 options follow PROXI \"Switch_Off_Time\" set to 20 minutes",
    "pre_conditions": "1. An LTM High Radio is absent from the bench configuration\n2. The PROXI parameter \"Switch_Off_Time\" is at 20 minutes\n3. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Read the selectable values offered for SwitchOff_Timeout_Setting.Req\n3. Select each offered value in turn and read Timeout1 to check that it follows the selection",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. The offered values are \"00 min\" and \"20 min\" and no other value is offered\n3. Timeout1 reads \"00 min\" after the first selection and \"20 minutes\" after the second",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.17; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.1; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.8.1.1.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 PROXI \"Switch_Off_Time\" = 20 分鐘時之可選集合與 Timeout1 結果",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 PROXI \"Switch_Off_Time\" = 20 分鐘時之可選集合與 Timeout1 結果"
    },
    "reasoning_note": "",
    "split_index": 1
  },
  {
    "req_id": "SWE-PM-057",
    "tc_id": "NR1L-PowerManagement-019",
    "tc_title": "Timeout1 options follow PROXI \"Switch_Off_Time\" set to 60 minutes",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Timeout1 options follow PROXI \"Switch_Off_Time\" set to 60 minutes",
    "pre_conditions": "1. An LTM High Radio is absent from the bench configuration\n2. The PROXI parameter \"Switch_Off_Time\" is at 60 minutes\n3. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Read the selectable values offered for SwitchOff_Timeout_Setting.Req\n3. Select each offered value in turn and read Timeout1 to check that it follows the selection",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. The offered values are \"00 min\" and \"60 min\" and no other value is offered\n3. Timeout1 reads \"00 min\" after the first selection and \"60 minutes\" after the second",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.17; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.1; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.8.1.1.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 PROXI \"Switch_Off_Time\" = 60 分鐘時之可選集合與 Timeout1 結果",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 PROXI \"Switch_Off_Time\" = 60 分鐘時之可選集合與 Timeout1 結果"
    },
    "reasoning_note": "",
    "split_index": 2
  },
  {
    "req_id": "SWE-PM-057",
    "tc_id": "NR1L-PowerManagement-020",
    "tc_title": "Timeout1 options follow PROXI \"Switch_Off_Time\" set to 180 minutes",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Timeout1 options follow PROXI \"Switch_Off_Time\" set to 180 minutes",
    "pre_conditions": "1. An LTM High Radio is absent from the bench configuration\n2. The PROXI parameter \"Switch_Off_Time\" is at 180 minutes\n3. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Read the selectable values offered for SwitchOff_Timeout_Setting.Req\n3. Select each offered value in turn and read Timeout1 to check that it follows the selection",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. The offered values are \"00 min\" and \"180 min\" and no other value is offered\n3. Timeout1 reads \"00 min\" after the first selection and \"180 minutes\" after the second",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.17; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.1; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.8.1.1.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 PROXI \"Switch_Off_Time\" = 180 分鐘時之可選集合與 Timeout1 結果",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 PROXI \"Switch_Off_Time\" = 180 分鐘時之可選集合與 Timeout1 結果"
    },
    "reasoning_note": "",
    "split_index": 3
  },
  {
    "req_id": "SWE-PM-060",
    "tc_id": "NR1L-PowerManagement-021",
    "tc_title": "LTM or ETM Radio offers one timeout parameter",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "LTM or ETM Radio offers one timeout parameter",
    "pre_conditions": "1. An LTM Radio is present in the bench configuration\n2. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Read the parameters offered for user selection to check that only one is present",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. Auto_SwitchOn_Setting.Req is the only parameter offered and SwitchOff_Timeout_Setting.Req is absent",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 LTM/ETM 型別：僅一個可設定參數",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 LTM/ETM 型別：僅一個可設定參數"
    },
    "reasoning_note": "",
    "split_index": 1
  },
  {
    "req_id": "SWE-PM-060",
    "tc_id": "NR1L-PowerManagement-022",
    "tc_title": "Radio other than LTM or ETM offers two timeout parameters",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Radio other than LTM or ETM offers two timeout parameters",
    "pre_conditions": "1. A Radio other than LTM or ETM is present in the bench configuration\n2. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Read the parameters offered for user selection to check that both are present",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req are both offered for selection",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗其餘 Radio 型別：兩個可設定參數",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗其餘 Radio 型別：兩個可設定參數"
    },
    "reasoning_note": "",
    "split_index": 2
  },
  {
    "req_id": "SWE-PM-061",
    "tc_id": "NR1L-PowerManagement-023",
    "tc_title": "Timeout settings are selectable in Full-Operation status",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Timeout settings are selectable in Full-Operation status",
    "pre_conditions": "1. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Change the offered timeout parameter and read it back to check that the change is accepted",
    "expected_result": "1. The timeout setting entry is shown and its controls are enabled\n2. The parameter reads back the newly selected value",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗肯定分支：Full-Operation 下設定可用",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗肯定分支：Full-Operation 下設定可用"
    },
    "reasoning_note": "",
    "split_index": 1
  },
  {
    "req_id": "SWE-PM-061",
    "tc_id": "NR1L-PowerManagement-024",
    "tc_title": "Timeout settings are not selectable outside Full-Operation status",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Timeout settings are not selectable outside Full-Operation status",
    "pre_conditions": "1. The TLM is in Timed status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Attempt to change the offered timeout parameter and read it back to check that it is rejected",
    "expected_result": "1. The timeout setting entry is either absent or shown with its controls disabled\n2. The parameter reads back its previous value and no change is stored",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗否定分支：非 Full-Operation 下設定不可用",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗否定分支：非 Full-Operation 下設定不可用"
    },
    "reasoning_note": "**§7 之獨立分支（18 包）**：`4941703` 逐字為「These settings could be only done in TLM Full-Operation Status」。僅驗肯定側時，「任何狀態皆可設定」之實作亦會通過 —— 否定側為該需求唯一可被證偽之處，故拆為獨立一條。",
    "split_index": 2
  }
]
```

### 第 2 段（025–031，7 條）

```json
[
  {
    "req_id": "SWE-PM-062",
    "tc_id": "NR1L-PowerManagement-025",
    "tc_title": "Auto_SwitchOn_Setting.Req can be set to Active",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Auto_SwitchOn_Setting.Req can be set to Active",
    "pre_conditions": "1. An LTM High Radio is present in the bench configuration\n2. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Select \"Active\" for Auto_SwitchOn_Setting.Req\n3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. The TLM accepts the selection without reverting it\n3. Auto_SwitchOn_Setting.Req reads \"Active\" and Timeout1 reads \"00 minutes\"",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.2",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Auto_SwitchOn_Setting.Req = \"Active\" 之選擇與其 Timeout1 條件",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Auto_SwitchOn_Setting.Req = \"Active\" 之選擇與其 Timeout1 條件"
    },
    "reasoning_note": "",
    "split_index": 1
  },
  {
    "req_id": "SWE-PM-062",
    "tc_id": "NR1L-PowerManagement-026",
    "tc_title": "Auto_SwitchOn_Setting.Req can be set to Not_Active",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Auto_SwitchOn_Setting.Req can be set to Not_Active",
    "pre_conditions": "1. An LTM High Radio is present in the bench configuration\n2. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Select \"Not_Active\" for Auto_SwitchOn_Setting.Req\n3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. The TLM accepts the selection without reverting it\n3. Auto_SwitchOn_Setting.Req reads \"Not_Active\" and Timeout1 holds a value other than \"00 minutes\"",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.2",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Auto_SwitchOn_Setting.Req = \"Not_Active\" 之選擇與其 Timeout1 條件",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Auto_SwitchOn_Setting.Req = \"Not_Active\" 之選擇與其 Timeout1 條件"
    },
    "reasoning_note": "",
    "split_index": 2
  },
  {
    "req_id": "SWE-PM-062",
    "tc_id": "NR1L-PowerManagement-027",
    "tc_title": "Auto_SwitchOn_Setting.Req can be set to Recall_Last",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Auto_SwitchOn_Setting.Req can be set to Recall_Last",
    "pre_conditions": "1. An LTM High Radio is present in the bench configuration\n2. The TLM is in Full-Operation status",
    "input_test_data": "NA",
    "test_procedure": "1. Open the timeout setting entry in the TLM menu\n2. Select \"Recall_Last\" for Auto_SwitchOn_Setting.Req\n3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection",
    "expected_result": "1. The timeout setting entry is shown in the TLM menu\n2. The TLM accepts the selection without reverting it\n3. Auto_SwitchOn_Setting.Req reads \"Recall_Last\" and Timeout1 reads \"00 minutes\"",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.2",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Auto_SwitchOn_Setting.Req = \"Recall_Last\" 之選擇與其 Timeout1 條件",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Auto_SwitchOn_Setting.Req = \"Recall_Last\" 之選擇與其 Timeout1 條件"
    },
    "reasoning_note": "",
    "split_index": 3
  },
  {
    "req_id": "SWE-PM-063",
    "tc_id": "NR1L-PowerManagement-028",
    "tc_title": "Bluetooth calls can be made and received in Timed state",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Bluetooth calls can be made and received in Timed state",
    "pre_conditions": "1. A paired bluetooth phone is available on the bench\n2. The TLM is in Timed state",
    "input_test_data": "NA",
    "test_procedure": "1. Place an outgoing bluetooth call from the paired phone through the TLM\n2. End that call and receive an incoming bluetooth call\n3. Read the call audio routing and the TLM state to check that both calls were served",
    "expected_result": "1. The outgoing call is connected and its audio is routed through the TLM\n2. The incoming call is presented and can be answered\n3. Both calls were served and the TLM remains in Timed state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Timed 狀態下通話功能可用（概括陳述之可觀察面）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Timed 狀態下通話功能可用（概括陳述之可觀察面）"
    },
    "reasoning_note": "",
    "split_index": 1
  },
  {
    "req_id": "SWE-PM-064",
    "tc_id": "NR1L-PowerManagement-029",
    "tc_title": "MaxCallTimeout starts on ignition off with Timeout1 at 00 min",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "MaxCallTimeout starts on ignition off with Timeout1 at 00 min",
    "pre_conditions": "1. Timeout1 is at \"00 min\"\n2. The TLM is in Full-Operation state\n3. Phone_Call.Info is at \"Active\"",
    "input_test_data": "Ignition working condition: \"Ignition Pre Off\"",
    "test_procedure": "1. Switch the ignition working condition to the value listed in Input Test Data\n2. Read the MaxCallTimeout counter to check that it started",
    "expected_result": "1. The TLM leaves Full-Operation state without dropping the active call\n2. The MaxCallTimeout counter is running from the moment of the ignition change",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗啟動條件一：Timeout1 == 00 min 且點火轉為 Pre Off 或 Off",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗啟動條件一：Timeout1 == 00 min 且點火轉為 Pre Off 或 Off"
    },
    "reasoning_note": "",
    "split_index": 1
  },
  {
    "req_id": "SWE-PM-064",
    "tc_id": "NR1L-PowerManagement-030",
    "tc_title": "MaxCallTimeout starts at Timeout1 expiry with the call still active",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "MaxCallTimeout starts at Timeout1 expiry with the call still active",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state\n3. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Let Timeout1 run to its expiration while the call stays active\n2. Read the MaxCallTimeout counter at Timeout1 expiration to check that it started",
    "expected_result": "1. Phone_Call.Info is still at \"Active\" when Timeout1 expires\n2. The MaxCallTimeout counter is running from the moment of Timeout1 expiration",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗啟動條件二：Timeout1 到期時通話仍為 Active",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗啟動條件二：Timeout1 到期時通話仍為 Active"
    },
    "reasoning_note": "",
    "split_index": 2
  },
  {
    "req_id": "SWE-PM-065",
    "tc_id": "NR1L-PowerManagement-031",
    "tc_title": "Call ends before Timeout1 expiry: previous source is restored",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Call ends before Timeout1 expiry: previous source is restored",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state\n3. A DAB Tuner source was active before the call\n4. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Set Phone_Call.Info to \"Not_Active\" before Timeout1 expires\n2. Read the active audio source and the TLM state to check that the previous source returned",
    "expected_result": "1. The call is released and its audio is removed from the TLM output\n2. The DAB Tuner source is active again and the TLM remains in Timed state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P1",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗還原音源分支",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗還原音源分支"
    },
    "reasoning_note": "",
    "split_index": 1
  }
]
```

### 第 3 段（032–038，7 條）

```json
[
  {
    "req_id": "SWE-PM-065",
    "tc_id": "NR1L-PowerManagement-032",
    "tc_title": "Further calls are still managed within Timeout1",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Further calls are still managed within Timeout1",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state\n3. One call has already ended before Timeout1 expiry",
    "input_test_data": "NA",
    "test_procedure": "1. Place a second bluetooth call while Timeout1 is still running\n2. Read the call audio routing and the TLM state to check that the second call is served",
    "expected_result": "1. The second call is connected and its audio is routed through the TLM\n2. The TLM remains in Timed state while the second call runs",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P2",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Timeout1 到期前仍可處理其他通話",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Timeout1 到期前仍可處理其他通話"
    },
    "reasoning_note": "",
    "split_index": 2
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-033",
    "tc_title": "Case 1 with RemStartFail true: TLM stops and passes to Standby",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 1 with RemStartFail true: TLM stops and passes to Standby",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state with media audio streaming active\n3. RemStartFail is at \"True\"\n4. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Set Phone_Call.Info to \"Not_Active\" before Timeout1 expires\n2. Read the active functionality, RemStartFail, TLM_Status.Info and $Telematic_Power$ to check the transition",
    "expected_result": "1. The media audio streaming stops and no source stays active\n2. RemStartFail reads \"False\", TLM_Status.Info and $Telematic_Power$ read \"Standby\" and the TLM is in Standby state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 1 之 RemStartFail 為 True 之分支",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 1 之 RemStartFail 為 True 之分支"
    },
    "reasoning_note": "",
    "split_index": 1
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-034",
    "tc_title": "Case 1 with RemStartFail false: previous source is restored",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 1 with RemStartFail false: previous source is restored",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state\n3. RemStartFail is at \"False\"\n4. A DAB Tuner source was active before the call",
    "input_test_data": "NA",
    "test_procedure": "1. Set Phone_Call.Info to \"Not_Active\" before Timeout1 expires\n2. Place a further bluetooth call while Timeout1 is still running\n3. Read the active source and the TLM state to check the restore and the further call",
    "expected_result": "1. The DAB Tuner source is active again and the TLM remains in Timed state\n2. The further call is connected and its audio is routed through the TLM\n3. The TLM stayed in Timed state throughout and no transition to Standby occurred",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 1 之 ELSE 分支：還原音源並續管理其他通話",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 1 之 ELSE 分支：還原音源並續管理其他通話"
    },
    "reasoning_note": "",
    "split_index": 2
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-035",
    "tc_title": "Case 2: MaxCallTimeout starts at Timeout1 expiry and the TLM stays Timed",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 2: MaxCallTimeout starts at Timeout1 expiry and the TLM stays Timed",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state\n3. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Let Timeout1 run to its expiration while the call stays active\n2. Read the MaxCallTimeout counter and the TLM state to check that the TLM stays Timed",
    "expected_result": "1. Phone_Call.Info is still at \"Active\" when Timeout1 expires and the MaxCallTimeout counter starts\n2. The TLM remains in Timed state while MaxCallTimeout runs",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 2 之進入：Timeout1 到期啟動 MaxCallTimeout 並續留 Timed",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 2 之進入：Timeout1 到期啟動 MaxCallTimeout 並續留 Timed"
    },
    "reasoning_note": "",
    "split_index": 3
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-036",
    "tc_title": "Case 2 exit on call end: TLM_Status.Info passes to Standby",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 2 exit on call end: TLM_Status.Info passes to Standby",
    "pre_conditions": "1. The TLM is in Timed state with MaxCallTimeout running\n2. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Set Phone_Call.Info to \"Not_Active\" before MaxCallTimeout expires\n2. Read TLM_Status.Info and the TLM state to check the transition to Standby",
    "expected_result": "1. The call is released and its audio is removed from the TLM output\n2. TLM_Status.Info reads \"Standby\" and the TLM is in Standby state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 2 之離開路徑：通話結束（不含 RemStartFail 處置）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 2 之離開路徑：通話結束（不含 RemStartFail 處置）"
    },
    "reasoning_note": "",
    "split_index": 4
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-037",
    "tc_title": "Case 2 exit with RemStartFail cleared on MaxCallTimeout expiry",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 2 exit with RemStartFail cleared on MaxCallTimeout expiry",
    "pre_conditions": "1. The TLM is in Timed state with MaxCallTimeout running\n2. RemStartFail is at \"True\"\n3. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Let MaxCallTimeout run to its expiration while the call stays active\n2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby",
    "expected_result": "1. The call is released at MaxCallTimeout expiration\n2. RemStartFail reads \"False\", TLM_Status.Info reads \"Standby\" and the TLM is in Standby state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 2 之離開路徑：MaxCallTimeout 到期（含 RemStartFail 處置）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 2 之離開路徑：MaxCallTimeout 到期（含 RemStartFail 處置）"
    },
    "reasoning_note": "",
    "split_index": 5
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-038",
    "tc_title": "Case 3: call already ended at Timeout1 expiry",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 3: call already ended at Timeout1 expiry",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state\n3. Phone_Call.Info is at \"Not_Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Let Timeout1 run to its expiration with no call active\n2. Read TLM_Status.Info and the TLM state to check the transition to Standby",
    "expected_result": "1. No call is active when Timeout1 expires and MaxCallTimeout does not start\n2. TLM_Status.Info reads \"Standby\" and the TLM is in Standby state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 3（不含 RemStartFail 處置）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 3（不含 RemStartFail 處置）"
    },
    "reasoning_note": "",
    "split_index": 6
  }
]
```

### 第 4 段（039–043，5 條）

```json
[
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-039",
    "tc_title": "Case 3 with RemStartFail cleared at Timeout1 expiry",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 3 with RemStartFail cleared at Timeout1 expiry",
    "pre_conditions": "1. Timeout1 is at a value other than \"00 min\"\n2. The TLM is in Timed state\n3. RemStartFail is at \"True\"\n4. Phone_Call.Info is at \"Not_Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Let Timeout1 run to its expiration with no call active\n2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby",
    "expected_result": "1. No call is active when Timeout1 expires and MaxCallTimeout does not start\n2. RemStartFail reads \"False\", TLM_Status.Info reads \"Standby\" and the TLM is in Standby state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 3（含 RemStartFail 處置）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 3（含 RemStartFail 處置）"
    },
    "reasoning_note": "",
    "split_index": 7
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-040",
    "tc_title": "Case 4: ignition off with Timeout1 at 00 min enters Timed state",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 4: ignition off with Timeout1 at 00 min enters Timed state",
    "pre_conditions": "1. Timeout1 is at \"00 min\"\n2. The TLM is in Full-Operation state\n3. Phone_Call.Info is at \"Active\"",
    "input_test_data": "Ignition working condition: \"Ignition Off\"",
    "test_procedure": "1. Keep the call active and switch the ignition working condition to the value listed in Input Test Data\n2. Read the TLM state and the MaxCallTimeout counter to check that Timed state is entered",
    "expected_result": "1. The active call is not dropped by the ignition change\n2. The TLM is in Timed state and the MaxCallTimeout counter is running",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 4 之進入：Timeout1 == 00 min 且點火轉為 Off",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 4 之進入：Timeout1 == 00 min 且點火轉為 Off"
    },
    "reasoning_note": "",
    "split_index": 8
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-041",
    "tc_title": "Case 4 exit: TLM passes to Standby when the call ends",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 4 exit: TLM passes to Standby when the call ends",
    "pre_conditions": "1. The TLM is in Timed state entered through Case 4\n2. MaxCallTimeout is running\n3. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Set Phone_Call.Info to \"Not_Active\" before MaxCallTimeout expires\n2. Read TLM_Status.Info and the TLM state to check the transition to Standby",
    "expected_result": "1. The TLM stayed in Timed state for the whole time the call was active\n2. TLM_Status.Info reads \"Standby\" and the TLM is in Standby state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 4 之離開路徑（`4941732` ＋ `4941735`，不含 RemStartFail 處置）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 4 之離開路徑（`4941732` ＋ `4941735`，不含 RemStartFail 處置）"
    },
    "reasoning_note": "",
    "split_index": 9
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-042",
    "tc_title": "Case 4 exit with RemStartFail cleared on MaxCallTimeout expiry",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 4 exit with RemStartFail cleared on MaxCallTimeout expiry",
    "pre_conditions": "1. The TLM is in Timed state entered through Case 4\n2. MaxCallTimeout is running\n3. RemStartFail is at \"True\"\n4. Phone_Call.Info is at \"Active\"",
    "input_test_data": "NA",
    "test_procedure": "1. Let MaxCallTimeout run to its expiration while the call stays active\n2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby",
    "expected_result": "1. The TLM stayed in Timed state until MaxCallTimeout expired\n2. RemStartFail reads \"False\", TLM_Status.Info reads \"Standby\" and the TLM is in Standby state",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 4 之離開路徑（`4941736`，含 RemStartFail 處置）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "behaviour",
      "delta": "本條驗 Case 4 之離開路徑（`4941736`，含 RemStartFail 處置）"
    },
    "reasoning_note": "",
    "split_index": 10
  },
  {
    "req_id": "SWE-PM-038",
    "tc_id": "NR1L-PowerManagement-043",
    "tc_title": "Case 4 with ignition pre off: TLM enters Timed state",
    "test_group": "Power Management",
    "test_set": "Timeout Settings",
    "test_item": "Case 4 with ignition pre off: TLM enters Timed state",
    "pre_conditions": "1. Timeout1 is at \"00 min\"\n2. The TLM is in Full-Operation state\n3. Phone_Call.Info is at \"Active\"",
    "input_test_data": "Ignition working condition: \"Ignition Pre Off\"",
    "test_procedure": "1. Keep the call active and switch the ignition working condition to the value listed in Input Test Data\n2. Read the TLM state and the MaxCallTimeout counter to check that Timed state is entered",
    "expected_result": "1. The active call is not dropped by the ignition change\n2. The TLM is in Timed state and the MaxCallTimeout counter is running",
    "specification_reference": "R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1",
    "priority": "P0",
    "design_method": "狀態轉換 (State Transition Testing)",
    "split_flag": true,
    "split_reason": "本條驗 Case 4 之另一觸發：點火轉為 \"Ignition Pre Off\"（`040` 驗 \"Ignition Off\"）",
    "functional_safety": "NA",
    "estimated_test_time": "",
    "remarks": "",
    "distinguishing_axis": {
      "axis": "trigger",
      "delta": "本條驗 Case 4 之 \"Ignition Pre Off\" 觸發"
    },
    "reasoning_note": "**R-P118 反向涵蓋盲測（18 包）**：`4941731` 載 Case 4 之觸發為 「the ignition working condition passes to \"Ignition Pre Off\" **OR** to \"Ignition Off\"」。首次撰寫時 `040` 僅取 \"Ignition Off\"，**\"Ignition Pre Off\" 之分支漏測**。透鏡 1 對該行為項判 overlap 0.62 為已覆蓋；**是透鏡 3 之殘差詞 `pre` 使其現形**。依 §5.7「不同觸發即拆分」與 R-P118(d) 裁為**真缺口**並補本條。**本項為 R-P128 之盲測結果：事前未知，由工具抓出。**",
    "split_index": 11
  }
]
```

---

## 二、B2 —— G99 錨點清單完整性（R-P134）

`features/power/scripts/verify_anchor_set.py` → `data/g99_anchor_set.md`

| leaf | `source_anchor` 數 | `item_ids` 數 | 該抄未抄 | 抄了不該抄 | 判定 |
|---|---|---|---|---|---|
| `SWE-PM-071` | 1 | 1 | — | — | **相等** |
| `SWE-PM-072` | 1 | 1 | — | — | **相等** |
| `SWE-PM-073` | 1 | 1 | — | — | **相等** |
| `SWE-PM-057` | 9 | 9 | — | — | **相等** |
| `SWE-PM-060` | 1 | 1 | — | — | **相等** |
| `SWE-PM-061` | 1 | 1 | — | — | **相等** |
| `SWE-PM-062` | 1 | 1 | — | — | **相等** |
| `SWE-PM-063` | 1 | 1 | — | — | **相等** |
| `SWE-PM-064` | 1 | 1 | — | — | **相等** |
| `SWE-PM-065` | 2 | 2 | — | — | **相等** |
| `SWE-PM-038` | 13 | 13 | — | — | **相等** |

**11 / 11 相等。**


### 2.1 刻意弄壞之 FAIL 證明

| fixture | 期望 | 實測 |
|---|---|---|
| 完整清單 | 相等 | **相等** |
| 次序不同 | 相等 | **相等**（集合比對，次序不具語義）|
| **刻意刪去一個錨點** | FAIL | **FAIL —— 缺 `4941736`** |
| **多列一個未被引用之錨點（R-P42）** | FAIL | **FAIL —— 多 `4941999`** |
| **空清單** | FAIL | **FAIL —— 缺全部 13 個** |

> **11 / 11 相等，未觸發停止條件。**
> G94 驗「抄對了」、G99 驗「抄全了該抄的」—— 反向涵蓋之地基兩側至此齊備。

---

## 三、B3 —— 成對／重複錨點之屬性查證（R-P135 / R-P136）

`features/power/scripts/build_anchor_attributes.py` → `data/b3_anchor_attributes.md`
屬性取自 CFTS 本文錨點標頭（R-P17 之文字層）。集合型屬性之次序不計。

## 1. R-P135 —— `SWE-PM-038` 之三組成對錨點

### `4941727` vs `4941728` —— **屬性相異：Model Year**（內文逐字不同）

| 屬性 | `4941727` | `4941728` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | RRM, LTM, ETM | 是 |
| EE Architecture | Atlantis Mid, Atlantis High | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | （無） | 2017 | **否** |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：**(b) 變體登載 —— 依 R-P135 須停並上繳，由 Pei 裁定是否合併**

### `4941729` vs `4941730` —— **屬性相異：Model Year、Radio、State**（內文逐字不同）

| 屬性 | `4941729` | `4941730` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | RRM, ETM, LTM | 是 |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis High, Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | （無） | 2017 | **否** |
| Radio | allSys, noSys | allSys | **否** |
| State | New | Under Review | **否** |

判定：**(b) 變體登載 —— 依 R-P135 須停並上繳，由 Pei 裁定是否合併**

### `4941735` vs `4941736` —— **屬性相異：Model Year、Radio、State**（內文逐字不同）

| 屬性 | `4941735` | `4941736` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | RRM, LTM, ETM | 是 |
| EE Architecture | Atlantis High, Atlantis Mid | Atlantis Mid, Atlantis High | 是 |
| Market | All | All | 是 |
| Model Year | （無） | 2017 | **否** |
| Radio | allSys, noSys | allSys | **否** |
| State | New | Under Review | **否** |

判定：**(b) 變體登載 —— 依 R-P135 須停並上繳，由 Pei 裁定是否合併**

## 2. R-P136 —— 跨章節逐字相同之三對錨點

### `4941692` vs `4941814` —— **屬性全同**（內文逐字相同）

| 屬性 | `4941692` | `4941814` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | RRM, ETM, LTM | LTM, RRM, ETM | 是 |
| EE Architecture | Atlantis Mid | Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：(a) 同一適用範圍下之不同行為 —— 各自成條正確

### `4941693` vs `4941815` —— **屬性全同**（內文逐字相同）

| 屬性 | `4941693` | `4941815` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | RRM, LTM, ETM | RRM, LTM, ETM | 是 |
| EE Architecture | Atlantis Mid | Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：(a) 同一適用範圍下之不同行為 —— 各自成條正確

### `4941695` vs `4941817` —— **屬性全同**（內文逐字相同）

| 屬性 | `4941695` | `4941817` | 相同 |
|---|---|---|---|
| Artifact Type | Subsystem Functional Requirement | Subsystem Functional Requirement | 是 |
| ECU | LTM, ETM, RRM | LTM, RRM, ETM | 是 |
| EE Architecture | Atlantis Mid | Atlantis Mid | 是 |
| Market | All | All | 是 |
| Model Year | 2017 | 2017 | 是 |
| Radio | allSys | allSys | 是 |
| State | Under Review | Under Review | 是 |

判定：(a) 同一適用範圍下之不同行為 —— 各自成條正確


### 3.1 結論

| 條 | 結果 | 處置 |
|---|---|---|
| **R-P135**（`SWE-PM-038` 三組成對錨點）| **三對之屬性皆相異** | **(b) 變體登載 —— 停並上繳，由 Pei 裁定是否合併。執行層未合併亦未拆分** |
| **R-P136**（跨章節逐字相同三對）| **三對之七項屬性全同且內文逐字相同** | **(a) 重複登載成立 —— 維持未另拆條之現行處置** |

**R-P135 之差異形態一致**（供裁定參考，**非建議**）：
含 `RemStartFail` 處置之一側皆帶 `Model Year:2017` 且 `State:Under Review`；
不含之一側或無 `Model Year`、或 `Radio` 多一個 `noSys`、或 `State:New`。
現行為各自成條（`036`/`037`、`038`/`039`、`041`/`042`，共六條）；
**若裁定合併，將減少三條。**

**R-P136 使 18 §七(甲)5 之「無證據」自陳於本包取得證據。**

---

## 四、B4 —— `SWE-PM-063` 之委出清單（R-P137）

依 §8.2.1，委出時 `reasoning` 須明確列出承擔該行為之 sibling Req ID。
已補入該 leaf 之 `reasoning`：

| # | 被委出之行為 | 承擔之 leaf | 承擔之 TC |
|---|---|---|---|
| 1 | `Timeout1` 之可選值與其由 PROXI `Switch_Off_Time` 決定 | `SWE-PM-057` | `018` / `019` / `020` |
| 2 | `Auto_SwitchOn_Setting.Req` 對 `Timeout1` 之條件 | `SWE-PM-062` | `025` / `026` / `027` |
| 3 | `MaxCallTimeout` 之兩個啟動條件 | `SWE-PM-064` | `029` / `030` |
| 4 | 通話於 `Timeout1` 到期前結束之邏輯（還原音源、續管理其他通話）| `SWE-PM-065` | `031` / `032` |
| 5 | Case 1–4 之完整轉換與其離開路徑 | `SWE-PM-038` | `033`–`043`（11 條）|

本 leaf 自身保留該錨點之**可獨立觀察面**：
「Timed 狀態下得撥出與接聽藍牙通話」（`028`）。

> **五項皆可指出承擔之 leaf 與 TC id，故為「已由他 leaf 涵蓋」而非未涵蓋，
> 無須依 R-P118(d) 重裁。**

---

## 五、B5 —— 殘差詞「措詞差異」抽樣（R-P138）

`features/power/scripts/build_residual_sample.py`（**`SEED = 19`**，＝本包編號）
＋ `residual_reasons.json` → `data/b5_residual_sample.md`

母體 **120**（候選 125 － 依 R-P42 委由他節者 5），抽 **20**，**抽樣率 16.7%**，可重現。
註：18 包所報之唯一真缺口（`pre`）已由 `043` 補測，故不再出現於本母體。

| leaf | 行為項 | 殘差詞 | 最佳對應 | overlap | 判為措詞差異之理由 |
|---|---|---|---|---|---|
| `SWE-PM-038` | #1 | `like` | `033` | 0.61 | `like` —— 舉例連接詞 |
| `SWE-PM-038` | #8 | `minutesand` | `033` | 0.69 | CFTS 原文之排版黏連（`minutes AND`），非語義單位 |
| `SWE-PM-038` | #11 | `thi` | `034` | 0.60 | `this` 之詞幹，指示代名詞 |
| `SWE-PM-057` | #4 | `respectively` | `018` | 0.60 | 英文連接副詞，無獨立可觀察標的 |
| `SWE-PM-057` | #7 | `user` | `018` | 0.67 | 規格以 `the user can select` 述主體，TC 之 procedure 以祈使句 `Select …` 述同一動作；主體詞於 TC 中不出現屬體例差異 |
| `SWE-PM-057` | #8 | `equal` | `018` | 0.47 | 規格用 `is equal to`，TC 用 `reads` —— 同一斷言之不同措詞 |
| `SWE-PM-057` | #9 | `equal` | `018` | 0.75 | 規格用 `is equal to`，TC 用 `reads` —— 同一斷言之不同措詞 |
| `SWE-PM-057` | #13 | `respectively` | `018` | 0.60 | 英文連接副詞，無獨立可觀察標的 |
| `SWE-PM-060` | #2 | `set` | `022` | 0.67 | `is set to` —— TC 之 pre_condition 以 `is at …` 述同一狀態 |
| `SWE-PM-060` | #2 | `signal` | `022` | 0.67 | `Phone_Call.Info signal` —— TC 以訊號名本身指稱 |
| `SWE-PM-061` | #1 | `only` | `023` | 0.50 | 限定副詞 —— 其語義由否定分支之獨立 TC（`024`）承載，非措詞遺漏 |
| `SWE-PM-063` | #1 | `accord` | `028` | 0.32 | `according to` 之介系詞 |
| `SWE-PM-063` | #1 | `follow` | `028` | 0.32 | `the following` 之文件內指涉，非行為 |
| `SWE-PM-063` | #1 | `parameter` | `028` | 0.32 | `parameters` 之上位詞 |
| `SWE-PM-063` | #1 | `time` | `028` | 0.32 | `time parameters` 之上位詞 |
| `SWE-PM-065` | #1 | `like` | `031` | 0.46 | `like` —— 舉例連接詞 |
| `SWE-PM-065` | #1 | `minutesand` | `031` | 0.46 | CFTS 原文之排版黏連（`minutes AND`），非語義單位 |
| `SWE-PM-065` | #1 | `pass` | `031` | 0.46 | 同 `pas` —— TC 以 `is in … state` 述同一轉換結果 |
| `SWE-PM-065` | #2 | `case` | `032` | 0.36 | `Case 1:` / `In this case` 之文件編號與指涉語 |
| `SWE-PM-065` | #2 | `manage` | `032` | 0.36 | `manage` —— 該行為由 `032` / `034` 覆蓋 |

## 抽中之行為項原文（供對照）

- `SWE-PM-038` #1（最佳對應 `033`，overlap 0.61）：Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN IF RemStartFail = ”True” TLM has to stop its active functi
- `SWE-PM-038` #8（最佳對應 `033`，overlap 0.69）：Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Timeout1 expiration THENTLM has to set TLM_Status.Info to “Standby” value and to pass to Standby
- `SWE-PM-038` #11（最佳對應 `034`，overlap 0.60）：In this case, TLM has to manage the phone call(s) and to stay in Timed state
- `SWE-PM-057` #4（最佳對應 `018`，overlap 0.60）：so Timeout1 is equal to "00 min" OR "60 minutes" respectively
- `SWE-PM-057` #7（最佳對應 `018`，overlap 0.67）：For the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to "00 minutes" OR equal to the value specified by PROXI paramet
- `SWE-PM-057` #8（最佳對應 `018`，overlap 0.47）：For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section Timeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Se
- `SWE-PM-057` #9（最佳對應 `018`，overlap 0.75）：So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes"
- `SWE-PM-057` #13（最佳對應 `018`，overlap 0.60）：so Timeout1 is equal to "00 min" OR "60 minutes" respectively
- `SWE-PM-060` #2（最佳對應 `022`，overlap 0.67）：For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu
- `SWE-PM-061` #1（最佳對應 `023`，overlap 0.50）：These settings could be only done in TLM Full-Operation Status
- `SWE-PM-063` #1（最佳對應 `028`，overlap 0.32）：In Timed state, it is possible either to make and to receive one or more bluetooth phone calls according to following logics that depend on Timeout1 and on MaxCallTimeout
- `SWE-PM-065` #1（最佳對應 `031`，overlap 0.46）：Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to restore the active source managed by TLM before
- `SWE-PM-065` #2（最佳對應 `032`，overlap 0.36）：In this case, TLM is still able to manage other possible phone calls within Timeout1 expiration


> **執行層未自我覆核該 20 項之判定 —— 覆核屬分析層。**
> 一項自陳：其中多項（`minutesand`、`thentlm`、`expirationthenat`）為
> **CFTS 原文之排版黏連**而非語義單位；此類佔母體之比例不低，
> **它們拉高了分母，也就拉低了信噪比** —— 0.7% 這個數字有一部分是抽取層的雜訊造成的。

---

## 六、B6 —— G73 剝除子句（R-P133）

### 6.1 實作與實測

剝除僅施於**末步**之 ER 行（非末步仍以完整步驟比對）；
剝除者為 `FINAL_STEP_INTENT_RE` 所匹配之子句起始至該步驟結尾。

| 條 | 剝除前 overlap | 剝除後 |
|---|---|---|
| `036` / `038` / `041` | **1.00** | **0.80** |
| `037` / `039` / `042` | 0.86 | 0.71 |
| `025` / `027` | 0.60 | 0.60 |
| `023` / `024` / `028` / `033` | 0.50 ~ 0.57 | 同 |

> **觸發數 12 → 12，無一條因剝除而脫離。**

### 6.2 執行層之判讀 —— 本條之前提只成立一半

overlap 確有一部分是 R-P101 之產物（1.00 → 0.80 即為證），
**但主因不是 check 子句** —— 而是「**末步讀 X、ER 述 X 之值**」這個回讀形態本身。
剝除後之步驟仍為 `Read TLM_Status.Info and the TLM state`，
而 ER `TLM_Status.Info reads "Standby" and the TLM is in Standby state` 之實詞
本就與之重疊 4 / 5。**這個重疊不是 R-P101 造成的，是「回讀」這件事本身造成的。**

### 6.3 十二條之逐項裁決（R-P76 分流）

本條後段載「剝除後若某條仍觸發，即為真複述」。
**執行層之評估與此不同**，二種讀法並陳如下，**不代分析層裁定**：

| TC | ER 行 | 依 R-P133 後段 | 執行層之評估 |
|---|---|---|---|
| `023` #2 | `The parameter reads back the newly selected value` | 真複述 | **偽陽性** —— 設定後之回讀，可失敗（值未存下即 fail）|
| `024` #2 | `The parameter reads back its previous value and no change is stored` | 真複述 | **偽陽性** —— 否定分支之回讀，另含 `no change is stored` 之新標的 |
| `025` #3 / `027` #3 | `Auto_SwitchOn_Setting.Req reads "…" and Timeout1 reads "…"` | 真複述 | **偽陽性** —— 兩個參數之值回讀，`Timeout1` 為 procedure 未逐字指名之新標的 |
| `028` #1 | `The outgoing call is connected and its audio is routed through the TLM` | 真複述 | **偽陽性** —— `is connected` 為系統側結果，且 `audio is routed` 為新標的 |
| `033` #2 | `RemStartFail reads "False", TLM_Status.Info and $Telematic_Power$ read "Standby" …` | 真複述 | **偽陽性** —— 三個訊號之值回讀 |
| `036` / `038` / `041` #2 | `TLM_Status.Info reads "Standby" and the TLM is in Standby state` | 真複述 | **偽陽性** —— 與 A-PW62 所載之已交付慣例（`Turn Sync on` → `Sync is on`、`The power button reads ON`）**同型** |
| `037` / `039` / `042` #2 | `RemStartFail reads "False", TLM_Status.Info reads "Standby" …` | 真複述 | **偽陽性** —— 同上，另含 `RemStartFail` 之值 |

**執行層未改動任一閘門、未改寫任一條 ER 以降低觸發數。**
若分析層採 R-P133 後段之讀法，則十二條之 ER 須改寫；
**該改寫會使末步所檢查之標的無法於 ER 中指名**，與 R-P101 直接衝突 ——
此衝突已呈請裁定（A-PW101）。

---

## 七、§D 全表自驗

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G99** | 錨點清單完整性 | 11 leaf 全數相等；刻意刪除 → FAIL | **11 / 11 相等**；fixture 五案如期 | **PASS** | **合成＋真實** |
| **G100** | 成對錨點屬性 | 各對之屬性相同或相異 | **R-P135 三對皆相異**（Model Year／Radio／State）→ 停並上繳；**R-P136 三對全同且內文逐字相同** → 重複登載成立 | **PASS（已查證）** | 真實 |
| **G101** | G73 剝除後觸發數 | 剝除前 12；剝除後之數與逐項裁決 | 剝除前 **12** → 剝除後 **12**（overlap 1.00→0.80、0.86→0.71）；**十二條已逐項裁決，二種讀法並陳** | **PASS（已回報）** | 真實 |
| **G102** | 殘差詞抽樣 | 20 個，種子已載明 | **20 / 120**（16.7%），`SEED = 19` 載明於報告與程式碼，可重現 | **PASS** | 真實 |
| **G70** | lint 全閘 | 全 PASS；leaf 11；TC 43 | `exit=0`；阻斷類 PASS；leaf **11**；TC **43**；待裁類 12 項 | **PASS** | 真實 |
| G94 | `source_clause` 保真度 | 沿用 | **11 / 11 逐字相符** | **PASS** | 合成＋真實 |
| G1–G98 | 沿用 | 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期** | **PASS** | 混合 |

**TC 數維持 43** —— R-P135 之裁定未下，未合併；R-P136 判為重複登載，未拆分；
R-P137 之委出清單成立，未重裁為真缺口。**三者皆未導致增減。**

---

## 八、執行層對「本包是否仍有該驗而未驗者」之獨立判斷

分析層於 §K 自判三項（第二批技術覆核未開始、屬性比對無法獨立複驗、`043` 未看過），
執行層無異議，**本節不覆述**，僅列自行判斷者。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 五項**

1. **G99 驗的是 `source_anchor` 等於 layer3，而 layer3 本身沒有在本包被驗。**
   `item_ids` 是 §C 錨點鏈的產物，其正確性由 03–06 包所驗。
   **若某個 leaf 的 `Source Requirement ID` 在 layer3 建表時就漏了一個 `Sys-RA-*` token，
   G94 全綠、G99 也全綠，而該錨點從頭到尾沒人看過。**
   這是地基再往下一層，本包沒有觸及。

2. **R-P135 之屬性比對，我是唯一讀過原始屬性字串的人。**
   §K 第 2 項已指出分析層讀不到 CFTS 本文。
   我把七項屬性逐欄列進報告，**但「這七項就是全部的屬性」也是我說的** ——
   `ATTR_RE` 只抓 `[名:值]` 形態，若標頭另有非方括號形態之屬性，我不會抓到也不會知道。

3. **B5 抽樣的 20 項理由是我寫的，而母體的分類也是我做的。**
   R-P138 要的是分析層覆核，這一步做到了；
   **但若我把某個真缺口誤分進「已由他條涵蓋」桶（機械判定，20 個），它根本進不了抽樣母體。**
   抽樣只覆核了我判「措詞差異」的那一桶。

4. **R-P133 之剝除我實作了，但它沒有解決 A-PW92。**
   12 → 12。我把它如實報成「前提只成立一半」，
   **然而現況是：第二批有 12 條處於待裁狀態，且二種讀法會導向相反的處置**
   （維持現狀 vs 改寫十二條 ER）。在裁定下來之前，第二批的這 12 條是懸著的。

5. **`SWE-PM-063` 的委出清單使該 leaf 只有一條，而這個結構未被檢驗過。**
   五項委出都能指到具體 TC，這一點是硬的。
   **但「一個 leaf 只保留可獨立觀察面、其餘全部委出」是否為 §8.2.1 所預期的用法，
   我沒有依據** —— §8.2.1 講的是 sibling 之間的行為歸屬，
   沒有講一個 leaf 可以委出到只剩一條。

**（乙）已驗而應標明其強度不足者 —— 一項**

6. **B5 的信噪比分母含相當比例的抽取層雜訊。**
   `minutesand` / `thentlm` / `expirationthenat` 這類是 CFTS 原文的排版黏連，
   不是語義單位。**它們拉高分母，也就拉低了信噪比** ——
   0.7% 這個數字有一部分是抽取層造成的，不全是透鏡 3 的問題。
   若先做黏連正規化再算，信噪比會較高；**本包未做，因為那會改動判準（17 §I 之教訓）。**

**（丙）本包自身之作業瑕疵 —— 一項**

7. **我在 R-P141 之回報中先寫了「已登記為 A-PW98」，而實際落號為 A-PW102。**
   原因是我在寫裁決回報時尚未定案 anomaly 編號，憑推估先填。
   落檔後校對時發現並更正。**這正是 16 包編號衝突之同型錯誤 —— 先寫號、後查號。**

---

## 九、DATA_REQUESTS

DR-PW1（High）、DR-PW5（High）、DR-PW8（High）、
DR-PW3（Medium）、DR-PW6（Medium）、DR-PW7（Low）維持 live；
DR-PW2、DR-PW4 維持撤回。**本包無新增。**

---

## 十、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/scripts/verify_anchor_set.py` | G99（新增，含 self-test）|
| `features/power/scripts/build_anchor_attributes.py` | B3 屬性查證（新增）|
| `features/power/scripts/build_residual_sample.py` ＋ `residual_reasons.json` | B5 抽樣（新增，`SEED = 19`）|
| `features/power/data/g99_anchor_set.md` | G99 報告（新增）|
| `features/power/data/b3_anchor_attributes.md` | 屬性查證報告（新增）|
| `features/power/data/b5_residual_sample.md` | 抽樣報告（新增）|
| `features/power/scripts/lint_tcs.py` | R-P133 之末步剝除（改）|
| `features/power/generated/batch_002_timeout_settings.json` | `SWE-PM-063` 之委出清單（改，僅此一處）|
| `features/power/RULINGS.md` | R-P133 ~ R-P141（改）|
| `features/power/ANOMALIES.md` | A-PW96 ~ A-PW102、A-PW92 / A-PW95 更新（改）|
| `features/power/docs/upstream/19_batch2_review.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 19 輪索引（改）|
