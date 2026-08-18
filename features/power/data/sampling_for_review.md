# G151 —— R-P159 分層取樣（R-P224 備料）

> **執行層備料，分析層讀**（R-P224）。
> 取樣規則：**全部 P0** ＋ **每 leaf 至少一條**（P0 已涵蓋者不重複；未有 P0 者取 `split_index = 1`）。
> **十六欄逐條全附，未節錄任何欄位**（§I）。

## 涵蓋率

| 項 | 數 |
|---|---|
| 全部 P0 | **193** |
| 補足每 leaf 至少一條 | **18** |
| **取樣合計** | **211** / 264 = **79.9%** |
| **leaf 涵蓋** | **103** / 103 = **100.0%** |

---

## 段 1 —— 001 ~ 025（8 條）

### `NR1L-PowerManagement-001`

- **req_id**：SWE-PM-071
- **tc_id**：NR1L-PowerManagement-001
- **tc_title**：Splash screen shown after SplashScreen_Time on normal boot
- **test_group**：Power Management
- **test_set**：Power Down
- **test_item**：Splash screen shown after SplashScreen_Time on normal boot
- **pre_conditions**：1. A suspend-resume boot sequence is available on the bench
- **input_test_data**：NA
- **test_procedure**：

```
1. Start the suspend-resume boot sequence
2. Read the TLM display before and after SplashScreen_Time to check that the splash screen is loaded
```
- **expected_result**：

```
1. The TLM display stays blank while the boot sequence runs
2. No splash screen appears before SplashScreen_Time has elapsed, and the splash screen is loaded once it has
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗正常開機分支：未轉往 Standby / Bench 時，SplashScreen_Time 到期後顯示 splash
- **reasoning_note**：**時序需求之下界斷言（R-P102）**：`4942337` 原文僅載「After SplashScreen_Time / StandardScreen_Time 畫面顯示」，**未載在此之前不得顯示**。本 TC 之 ER 仍斷言「到期前不顯示」，其依據**不是規格明文禁止提早顯示**，而是**時序需求之可驗證性要求** —— 不設下界，該需求無法被證偽（T=0 即顯示亦會通過）。此為刻意選擇，非誤讀規格。ER 措詞僅描述觀察到之行為，未暗示規格明文禁止。

### `NR1L-PowerManagement-005`

- **req_id**：SWE-PM-072
- **tc_id**：NR1L-PowerManagement-005
- **tc_title**：Events during boot are buffered without loss
- **test_group**：Power Management
- **test_set**：Power Down
- **test_item**：Events during boot are buffered without loss
- **pre_conditions**：1. An event injection tool is connected to the bench
- **input_test_data**：Event burst: 20 events injected at 100 ms intervals during boot
- **test_procedure**：

```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM event log to check that every injected event was buffered without loss
```
- **expected_result**：

```
1. No injected event is rejected and no error is reported while the boot is still completing
2. The buffered event count equals the injected event count with no event dropped
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.1.1.1
- **priority**：P0
- **design_method**：功能測試 (Functional based ; no specific technique)
- **functional_safety**：NA
- **split_reason**：本條驗緩衝面：開機期間到達之事件不得遺失。與 -02 之處理面為兩個獨立部分失效（§8.2.2）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-007`

- **req_id**：SWE-PM-073
- **tc_id**：NR1L-PowerManagement-007
- **tc_title**：Load Shed limits volume and mutes TLM
- **test_group**：Power Management
- **test_set**：Power Down
- **test_item**：Load Shed limits volume and mutes TLM
- **pre_conditions**：

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. Ecall, ACN and chimes modes are inactive
```
- **input_test_data**：

```
STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
Starting volume level: 25
```
- **test_procedure**：

```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data
3. Read AUD_LVL, the audio output and the ICS power state to check the Load Shed action
```
- **expected_result**：

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts both Load Shed signals without a bus error
3. The maximum volume for Ecall, ACN, chimes, beeps and alerts is reduced to 20, AUD_LVL carries the updated level, the TLM is muted and the ICS module powers down
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2
- **priority**：P0
- **design_method**：決策表 (Decision Table Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Load Shed 之偵測與四項動作。與 -03 之 Battery Critical 為不同觸發訊號、不同控制實體，依 §8.2.2 拆分
- **reasoning_note**：（空）

### `NR1L-PowerManagement-009`

- **req_id**：SWE-PM-073
- **tc_id**：NR1L-PowerManagement-009
- **tc_title**：Battery Critical minimizes draw and keeps ACN active
- **test_group**：Power Management
- **test_set**：Power Down
- **test_item**：Battery Critical minimizes draw and keeps ACN active
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY ON mode
3. Ecall, ACN and chimes modes are inactive
```
- **input_test_data**：

```
STATUS_LIN.Batt_ST_Crit = [1h]
Starting volume level: 25
```
- **test_procedure**：

```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data
3. Read the display, HVAC controls, ACN phone state and AUD_LVL to check the current minimization
```
- **expected_result**：

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts the Battery Critical signal without a bus error
3. The display stays on, HVAC controls and ACN phone stay active, the maximum volume for Ecall, ACN, chimes, beeps and alerts is reduced to 20 and the TLM is muted
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2
- **priority**：P0
- **design_method**：決策表 (Decision Table Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Battery Critical 之偵測與四項動作。BODY ON 與 BODY OFF-TIMED 共用同一控制實體，故合為一條之多列 ER
- **reasoning_note**：（空）

### `NR1L-PowerManagement-018`

- **req_id**：SWE-PM-057
- **tc_id**：NR1L-PowerManagement-018
- **tc_title**：Timeout1 options follow PROXI "Switch_Off_Time" set to 20 minutes
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Timeout1 options follow PROXI "Switch_Off_Time" set to 20 minutes
- **pre_conditions**：

```
1. An LTM High Radio is absent from the bench configuration
2. The PROXI parameter "Switch_Off_Time" is at 20 minutes
3. The TLM is in Full-Operation status
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Open the timeout setting entry in the TLM menu
2. Read the selectable values offered for SwitchOff_Timeout_Setting.Req
3. Select each offered value in turn and read Timeout1 to check that it follows the selection
```
- **expected_result**：

```
1. The timeout setting entry is shown in the TLM menu
2. The offered values are "00 min" and "20 min" and no other value is offered
3. Timeout1 reads "00 min" after the first selection and "20 minutes" after the second
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.17; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.1; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.8.1.1.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 PROXI "Switch_Off_Time" = 20 分鐘時之可選集合與 Timeout1 結果
- **reasoning_note**：（空）

### `NR1L-PowerManagement-021`

- **req_id**：SWE-PM-060
- **tc_id**：NR1L-PowerManagement-021
- **tc_title**：LTM or ETM Radio offers one timeout parameter
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：LTM or ETM Radio offers one timeout parameter
- **pre_conditions**：

```
1. An LTM Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that only one is present
```
- **expected_result**：

```
1. The timeout setting entry is shown in the TLM menu
2. Auto_SwitchOn_Setting.Req is the only parameter offered and SwitchOff_Timeout_Setting.Req is absent
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 LTM/ETM 型別：僅一個可設定參數
- **reasoning_note**：（空）

### `NR1L-PowerManagement-023`

- **req_id**：SWE-PM-061
- **tc_id**：NR1L-PowerManagement-023
- **tc_title**：Timeout settings are selectable in Full-Operation status
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Timeout settings are selectable in Full-Operation status
- **pre_conditions**：1. The TLM is in Full-Operation status
- **input_test_data**：NA
- **test_procedure**：

```
1. Open the timeout setting entry in the TLM menu
2. Change the offered timeout parameter and read it back to check that the change is accepted
```
- **expected_result**：

```
1. The timeout setting entry is shown and its controls are enabled
2. The parameter reads back the newly selected value
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗肯定分支：Full-Operation 下設定可用
- **reasoning_note**：**R-P157(ii)（22 包）**：本條 ER1 述「timeout setting entry 之呈現／其控制項啟用與否」。`4941703` 僅載「These settings could be only done in TLM Full-Operation Status」，**未載該項於 HMI 上如何呈現**。該行為**僅描述觀察到之事實，不以之為 pass/fail 判準** ——本條之判準為 ER2（設定是否被接受／被拒），其依據即該錨點原文。

### `NR1L-PowerManagement-025`

- **req_id**：SWE-PM-062
- **tc_id**：NR1L-PowerManagement-025
- **tc_title**：Auto_SwitchOn_Setting.Req can be set to Active
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Auto_SwitchOn_Setting.Req can be set to Active
- **pre_conditions**：

```
1. An LTM High Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Open the timeout setting entry in the TLM menu
2. Select "Active" for Auto_SwitchOn_Setting.Req
3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection
```
- **expected_result**：

```
1. The timeout setting entry is shown in the TLM menu
2. The TLM accepts the selection without reverting it
3. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 minutes"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.2
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Auto_SwitchOn_Setting.Req = "Active" 之選擇與其 Timeout1 條件
- **reasoning_note**：（空）

---

## 段 2 —— 028 ~ 037（8 條）

### `NR1L-PowerManagement-028`

- **req_id**：SWE-PM-063
- **tc_id**：NR1L-PowerManagement-028
- **tc_title**：Bluetooth calls can be made and received in Timed state
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Bluetooth calls can be made and received in Timed state
- **pre_conditions**：

```
1. A paired bluetooth phone is available on the bench
2. The TLM is in Timed state
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Place an outgoing bluetooth call from the paired phone through the TLM
2. End that call and receive an incoming bluetooth call
3. Read the call audio routing and the TLM state to check that both calls were served
```
- **expected_result**：

```
1. The outgoing call is connected
2. The incoming call is presented and can be answered
3. Both calls were served and the TLM remains in Timed state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Timed 狀態下通話功能可用（概括陳述之可觀察面）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-029`

- **req_id**：SWE-PM-064
- **tc_id**：NR1L-PowerManagement-029
- **tc_title**：MaxCallTimeout starts on ignition off with Timeout1 at 00 min
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：MaxCallTimeout starts on ignition off with Timeout1 at 00 min
- **pre_conditions**：

```
1. Timeout1 is at "00 min"
2. The TLM is in Full-Operation state
3. Phone_Call.Info is at "Active"
```
- **input_test_data**：Ignition working condition: "Ignition Pre Off"
- **test_procedure**：

```
1. Switch the ignition working condition to the value listed in Input Test Data
2. Read the MaxCallTimeout counter to check that it started
```
- **expected_result**：

```
1. The TLM leaves Full-Operation state without dropping the active call
2. The MaxCallTimeout counter is running from the moment of the ignition change
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗啟動條件一：Timeout1 == 00 min 且點火轉為 Pre Off 或 Off
- **reasoning_note**：（空）

### `NR1L-PowerManagement-031`

- **req_id**：SWE-PM-065
- **tc_id**：NR1L-PowerManagement-031
- **tc_title**：Call ends before Timeout1 expiry: previous source is restored
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Call ends before Timeout1 expiry: previous source is restored
- **pre_conditions**：

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. A DAB Tuner source was active before the call
4. Phone_Call.Info is at "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Set Phone_Call.Info to "Not_Active" before Timeout1 expires
2. Read the active audio source and the TLM state to check that the previous source returned
```
- **expected_result**：

```
1. Phone_Call.Info reads "Not_Active" before Timeout1 expires
2. The DAB Tuner source is active again and the TLM remains in Timed state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗還原音源分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-033`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-033
- **tc_title**：Case 1 with RemStartFail true: TLM stops and passes to Standby
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 1 with RemStartFail true: TLM stops and passes to Standby
- **pre_conditions**：

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state with media audio streaming active
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Set Phone_Call.Info to "Not_Active" before Timeout1 expires
2. Read the active functionality, RemStartFail, TLM_Status.Info and $Telematic_Power$ to check the transition
```
- **expected_result**：

```
1. The media audio streaming stops and no source stays active
2. RemStartFail reads "False", TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM is in Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 1 之 RemStartFail 為 True 之分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-034`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-034
- **tc_title**：Case 1 with RemStartFail false: previous source is restored
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 1 with RemStartFail false: previous source is restored
- **pre_conditions**：

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. RemStartFail is at "False"
4. A DAB Tuner source was active before the call
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Set Phone_Call.Info to "Not_Active" before Timeout1 expires
2. Place a further bluetooth call while Timeout1 is still running
3. Read the active source and the TLM state to check the restore and the further call
```
- **expected_result**：

```
1. The DAB Tuner source is active again and the TLM remains in Timed state
2. The further call is connected and is managed by the TLM
3. The TLM stayed in Timed state throughout and no transition to Standby occurred
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 1 之 ELSE 分支：還原音源並續管理其他通話
- **reasoning_note**：（空）

### `NR1L-PowerManagement-035`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-035
- **tc_title**：Case 2: MaxCallTimeout starts at Timeout1 expiry and the TLM stays Timed
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 2: MaxCallTimeout starts at Timeout1 expiry and the TLM stays Timed
- **pre_conditions**：

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. Phone_Call.Info is at "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let Timeout1 run to its expiration while the call stays active
2. Read the MaxCallTimeout counter and the TLM state to check that the TLM stays Timed
```
- **expected_result**：

```
1. Phone_Call.Info is still at "Active" when Timeout1 expires and the MaxCallTimeout counter starts
2. The TLM remains in Timed state while MaxCallTimeout runs
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 2 之進入：Timeout1 到期啟動 MaxCallTimeout 並續留 Timed
- **reasoning_note**：（空）

### `NR1L-PowerManagement-036`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-036
- **tc_title**：Case 2 exit on call end: TLM_Status.Info passes to Standby
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 2 exit on call end: TLM_Status.Info passes to Standby
- **pre_conditions**：

```
1. The TLM is in Timed state with MaxCallTimeout running
2. Phone_Call.Info is at "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Set Phone_Call.Info to "Not_Active" before MaxCallTimeout expires
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```
- **expected_result**：

```
1. Phone_Call.Info reads "Not_Active" before MaxCallTimeout expires
2. TLM_Status.Info reads "Standby" and the TLM is in Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 2 之離開路徑：通話結束（不含 RemStartFail 處置）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-037`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-037
- **tc_title**：Case 2 exit with RemStartFail cleared on MaxCallTimeout expiry
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 2 exit with RemStartFail cleared on MaxCallTimeout expiry
- **pre_conditions**：

```
1. The TLM is in Timed state with MaxCallTimeout running
2. RemStartFail is at "True"
3. Phone_Call.Info is at "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let MaxCallTimeout run to its expiration while the call stays active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```
- **expected_result**：

```
1. MaxCallTimeout reaches its expiration while Phone_Call.Info is still "Active"
2. RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 2 之離開路徑：MaxCallTimeout 到期（含 RemStartFail 處置）
- **reasoning_note**：（空）

---

## 段 3 —— 038 ~ 045（8 條）

### `NR1L-PowerManagement-038`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-038
- **tc_title**：Case 3: call already ended at Timeout1 expiry
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 3: call already ended at Timeout1 expiry
- **pre_conditions**：

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. Phone_Call.Info is at "Not_Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let Timeout1 run to its expiration with no call active
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```
- **expected_result**：

```
1. No call is active when Timeout1 expires
2. TLM_Status.Info reads "Standby" and the TLM is in Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 3（不含 RemStartFail 處置）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-039`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-039
- **tc_title**：Case 3 with RemStartFail cleared at Timeout1 expiry
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 3 with RemStartFail cleared at Timeout1 expiry
- **pre_conditions**：

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Not_Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let Timeout1 run to its expiration with no call active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```
- **expected_result**：

```
1. No call is active when Timeout1 expires
2. RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 3（含 RemStartFail 處置）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-040`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-040
- **tc_title**：Case 4: ignition off with Timeout1 at 00 min enters Timed state
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 4: ignition off with Timeout1 at 00 min enters Timed state
- **pre_conditions**：

```
1. Timeout1 is at "00 min"
2. The TLM is in Full-Operation state
3. Phone_Call.Info is at "Active"
```
- **input_test_data**：Ignition working condition: "Ignition Off"
- **test_procedure**：

```
1. Keep the call active and switch the ignition working condition to the value listed in Input Test Data
2. Read the TLM state and the MaxCallTimeout counter to check that Timed state is entered
```
- **expected_result**：

```
1. The active call is not dropped by the ignition change
2. The TLM is in Timed state and the MaxCallTimeout counter is running
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 4 之進入：Timeout1 == 00 min 且點火轉為 Off
- **reasoning_note**：（空）

### `NR1L-PowerManagement-041`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-041
- **tc_title**：Case 4 exit: TLM passes to Standby when the call ends
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 4 exit: TLM passes to Standby when the call ends
- **pre_conditions**：

```
1. The TLM is in Timed state entered through Case 4
2. MaxCallTimeout is running
3. Phone_Call.Info is at "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Set Phone_Call.Info to "Not_Active" before MaxCallTimeout expires
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```
- **expected_result**：

```
1. The TLM stayed in Timed state for the whole time the call was active
2. TLM_Status.Info reads "Standby" and the TLM is in Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 4 之離開路徑（`4941732` ＋ `4941735`，不含 RemStartFail 處置）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-042`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-042
- **tc_title**：Case 4 exit with RemStartFail cleared on MaxCallTimeout expiry
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 4 exit with RemStartFail cleared on MaxCallTimeout expiry
- **pre_conditions**：

```
1. The TLM is in Timed state entered through Case 4
2. MaxCallTimeout is running
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let MaxCallTimeout run to its expiration while the call stays active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```
- **expected_result**：

```
1. The TLM stayed in Timed state until MaxCallTimeout expired
2. RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 4 之離開路徑（`4941736`，含 RemStartFail 處置）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-043`

- **req_id**：SWE-PM-038
- **tc_id**：NR1L-PowerManagement-043
- **tc_title**：Case 4 with ignition pre off: TLM enters Timed state
- **test_group**：Power Management
- **test_set**：Timeout Settings
- **test_item**：Case 4 with ignition pre off: TLM enters Timed state
- **pre_conditions**：

```
1. Timeout1 is at "00 min"
2. The TLM is in Full-Operation state
3. Phone_Call.Info is at "Active"
```
- **input_test_data**：Ignition working condition: "Ignition Pre Off"
- **test_procedure**：

```
1. Keep the call active and switch the ignition working condition to the value listed in Input Test Data
2. Read the TLM state and the MaxCallTimeout counter to check that Timed state is entered
```
- **expected_result**：

```
1. The active call is not dropped by the ignition change
2. The TLM is in Timed state and the MaxCallTimeout counter is running
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Case 4 之另一觸發：點火轉為 "Ignition Pre Off"（`040` 驗 "Ignition Off"）
- **reasoning_note**：**R-P118 反向涵蓋盲測（18 包）**：`4941731` 載 Case 4 之觸發為 「the ignition working condition passes to "Ignition Pre Off" **OR** to "Ignition Off"」。首次撰寫時 `040` 僅取 "Ignition Off"，**"Ignition Pre Off" 之分支漏測**。透鏡 1 對該行為項判 overlap 0.62 為已覆蓋；**是透鏡 3 之殘差詞 `pre` 使其現形**。依 §5.7「不同觸發即拆分」與 R-P118(d) 裁為**真缺口**並補本條。**本項為 R-P128 之盲測結果：事前未知，由工具抓出。**

### `NR1L-PowerManagement-044`

- **req_id**：SWE-PM-011
- **tc_id**：NR1L-PowerManagement-044
- **tc_title**：VR button press in IDLE mode transitions the HU to Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：VR button press in IDLE mode transitions the HU to Full-Operation
- **pre_conditions**：

```
1. The HU is in IDLE mode
2. A VR button is available on the bench
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Press the VR button with a short press and release it
2. Read the HU mode to check the transition to Full-Operation
```
- **expected_result**：

```
1. The HU accepts the VR button press
2. The HU is in Full-Operation mode
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 IDLE → Full-Operation 之 VR 觸發（短按）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-045`

- **req_id**：SWE-PM-011
- **tc_id**：NR1L-PowerManagement-045
- **tc_title**：CarPlay requesting audio and video keeps audio unmuted and screen on
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CarPlay requesting audio and video keeps audio unmuted and screen on
- **pre_conditions**：

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```
- **input_test_data**：CarPlay request: audio control and video control
- **test_procedure**：

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode, the entertainment audio and the screen to check the resulting behavior
```
- **expected_result**：

```
1. The HU accepts the request without leaving FULL OPERATION mode
2. The entertainment audio is unmuted and the screen is on
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 audio ＋ video 皆請求之分支
- **reasoning_note**：（空）

---

## 段 4 —— 046 ~ 053（8 條）

### `NR1L-PowerManagement-046`

- **req_id**：SWE-PM-011
- **tc_id**：NR1L-PowerManagement-046
- **tc_title**：CarPlay requesting audio only activates the Screen OFF function
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CarPlay requesting audio only activates the Screen OFF function
- **pre_conditions**：

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```
- **input_test_data**：CarPlay request: audio control only
- **test_procedure**：

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode, the audio and the screen to check the resulting behavior
```
- **expected_result**：

```
1. The HU accepts the request without leaving FULL OPERATION mode
2. The audio is unmuted and the Screen OFF function is activated
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗僅請求 audio 之分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-047`

- **req_id**：SWE-PM-011
- **tc_id**：NR1L-PowerManagement-047
- **tc_title**：CarPlay requesting video only mutes the audio and keeps the screen on
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CarPlay requesting video only mutes the audio and keeps the screen on
- **pre_conditions**：

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```
- **input_test_data**：CarPlay request: video control only
- **test_procedure**：

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode, the audio and the screen to check the resulting behavior
```
- **expected_result**：

```
1. The HU accepts the request without leaving FULL OPERATION mode
2. The audio is muted and the Screen On function is activated
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗僅請求 video 之分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-048`

- **req_id**：SWE-PM-011
- **tc_id**：NR1L-PowerManagement-048
- **tc_title**：CarPlay requesting neither audio nor video returns the HU to IDLE
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CarPlay requesting neither audio nor video returns the HU to IDLE
- **pre_conditions**：

```
1. The HU is in FULL OPERATION mode
2. A CarPlay Device is paired on the bench
3. A CarPlay VR interaction has completed
```
- **input_test_data**：CarPlay request: neither audio control nor video control
- **test_procedure**：

```
1. Let the CarPlay Device issue the request listed in Input Test Data
2. Read the HU mode to check the return to IDLE mode
```
- **expected_result**：

```
1. The HU accepts the request and leaves FULL OPERATION mode
2. The HU is in IDLE mode
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗二者皆不請求之分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-049`

- **req_id**：SWE-PM-011
- **tc_id**：NR1L-PowerManagement-049
- **tc_title**：VR button long press in IDLE mode transitions the HU to Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：VR button long press in IDLE mode transitions the HU to Full-Operation
- **pre_conditions**：

```
1. The HU is in IDLE mode
2. A VR button is available on the bench
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Press the VR button with a long press and release it
2. Read the HU mode to check the transition to Full-Operation
```
- **expected_result**：

```
1. The HU accepts the VR button long press
2. The HU is in Full-Operation mode
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗長按之觸發（`051` 驗短按）——`4941376` 載二者皆為該定義所指
- **reasoning_note**：**R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

### `NR1L-PowerManagement-050`

- **req_id**：SWE-PM-012
- **tc_id**：NR1L-PowerManagement-050
- **tc_title**：User settings are restored after a battery reconnection
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：User settings are restored after a battery reconnection
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req hold known values
3. The battery is disconnected
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Reconnect the battery and let the voltage settle within its thresholds
2. Read the three stored variables to check that their previous values returned
```
- **expected_result**：

```
1. The TLM leaves INIT state once the voltage is within its thresholds
2. VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req read their values before the battery disconnection
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.13
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗電池回接後之使用者設定還原
- **reasoning_note**：（空）

### `NR1L-PowerManagement-051`

- **req_id**：SWE-PM-012
- **tc_id**：NR1L-PowerManagement-051
- **tc_title**：TLM starts from Sleep state after leaving INIT
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：TLM starts from Sleep state after leaving INIT
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The battery has just been reconnected
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let the TLM exit INIT state
2. Read TLM_Status.Info and the state machine to check the starting state
```
- **expected_result**：

```
1. The TLM leaves INIT state without an error being reported
2. TLM_Status.Info reads "Sleep" and the TLM starts from Sleep state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.13
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗離開 INIT 後之起始狀態
- **reasoning_note**：（空）

### `NR1L-PowerManagement-052`

- **req_id**：SWE-PM-013
- **tc_id**：NR1L-PowerManagement-052
- **tc_title**：Remote Start Active reports Partial_Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start Active reports Partial_Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The ignition working condition is Ignition On
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts = "Remote Start Active"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read $Telematic_Power$ to check the reported mode
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. $Telematic_Power$ reads "Partial_Operation"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.3
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Remote Start Active 之模式回報
- **reasoning_note**：（空）

### `NR1L-PowerManagement-053`

- **req_id**：SWE-PM-013
- **tc_id**：NR1L-PowerManagement-053
- **tc_title**：Remote Start Active reports Partial_Operation in Ignition Pre_Start
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start Active reports Partial_Operation in Ignition Pre_Start
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The ignition working condition is Ignition Pre_Start
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts = "Remote Start Active"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read $Telematic_Power$ to check the reported mode
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. $Telematic_Power$ reads "Partial_Operation"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.3
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗逗號列舉之點火工作條件 Ignition Pre_Start（R-P199 補測）
- **reasoning_note**：

```
R-P199 補測 —— G131 測得本 leaf 之逗號列舉七項中，`Ignition Pre_Start` 無 TC 覆蓋。R-P192 所推遲者為立閘門，非補測。
**R-P207（28 包）**：本條所驗為**範圍主張** —— 規格列舉之該點火工作條件下該行為亦存在；**非驗其與他狀態間之行為差異**。故其 ER 與同組他條相同係屬正確，不得據此判為重複。
```

---

## 段 5 —— 054 ~ 062（8 條）

### `NR1L-PowerManagement-054`

- **req_id**：SWE-PM-013
- **tc_id**：NR1L-PowerManagement-054
- **tc_title**：Remote Start Active reports Partial_Operation in Ignition Cranking
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start Active reports Partial_Operation in Ignition Cranking
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The ignition working condition is Ignition Cranking
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts = "Remote Start Active"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read $Telematic_Power$ to check the reported mode
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. $Telematic_Power$ reads "Partial_Operation"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.3
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗逗號列舉之點火工作條件 Ignition Cranking（R-P199 補測）
- **reasoning_note**：

```
R-P199 補測 —— G131 測得本 leaf 之逗號列舉七項中，`Ignition Cranking` 無 TC 覆蓋。R-P192 所推遲者為立閘門，非補測。
**R-P207（28 包）**：本條所驗為**範圍主張** —— 規格列舉之該點火工作條件下該行為亦存在；**非驗其與他狀態間之行為差異**。故其 ER 與同組他條相同係屬正確，不得據此判為重複。
```

### `NR1L-PowerManagement-055`

- **req_id**：SWE-PM-013
- **tc_id**：NR1L-PowerManagement-055
- **tc_title**：Remote Start Active reports Partial_Operation in Ignition On Engine On
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start Active reports Partial_Operation in Ignition On Engine On
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The ignition working condition is Ignition On Engine On
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts = "Remote Start Active"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read $Telematic_Power$ to check the reported mode
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. $Telematic_Power$ reads "Partial_Operation"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.3
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗逗號列舉之點火工作條件 Ignition On Engine On（R-P199 補測）
- **reasoning_note**：

```
R-P199 補測 —— G131 測得本 leaf 之逗號列舉七項中，`Ignition On Engine On` 無 TC 覆蓋。R-P192 所推遲者為立閘門，非補測。
**R-P207（28 包）**：本條所驗為**範圍主張** —— 規格列舉之該點火工作條件下該行為亦存在；**非驗其與他狀態間之行為差異**。故其 ER 與同組他條相同係屬正確，不得據此判為重複。
```

### `NR1L-PowerManagement-056`

- **req_id**：SWE-PM-013
- **tc_id**：NR1L-PowerManagement-056
- **tc_title**：AMP, ICS and DTV are off while chime audio stays active
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：AMP, ICS and DTV are off while chime audio stays active
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in Partial Operation with AMP, ICS and DTV equipped
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let the TLM settle in Partial Operation
2. Read the AMP, ICS and DTV power states and the audio paths to check the active set
```
- **expected_result**：

```
1. The TLM stays in Partial Operation without further transition
2. AMP, ICS and DTV are OFF while audio for ANC, ACN and chimes is active
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.3
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Partial Operation 之各模組電源與音訊
- **reasoning_note**：（空）

### `NR1L-PowerManagement-058`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-058
- **tc_title**：Remote Start ends at ignition off: RemStartFail is set true
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start ends at ignition off: RemStartFail is set true
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. LTM_OperationalModeSts.Info is at "Ignition Off"
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts: "Remote Start Active" to "Remote Start Not Active"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read RemStartFail to check that it follows the transition
```
- **expected_result**：

```
1. The TLM accepts the transition without a bus error
2. RemStartFail reads "True"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Remote Start 結束於點火關閉時之 RemStartFail 設定
- **reasoning_note**：（空）

### `NR1L-PowerManagement-059`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-059
- **tc_title**：RemStartFail is cleared when the call is not active
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：RemStartFail is cleared when the call is not active
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. RemStartFail reads "True"
3. Phone_Call.Info reads "Not Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let the TLM evaluate the call state after the RemStartFail transition
2. Read RemStartFail and TLM_Status.Info to check the resulting values
```
- **expected_result**：

```
1. The TLM evaluates Phone_Call.Info without a further transition being needed
2. RemStartFail reads "False"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗通話未啟用時之 RemStartFail 清除
- **reasoning_note**：（空）

### `NR1L-PowerManagement-060`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-060
- **tc_title**：Behaviour 1 with no active call passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Behaviour 1 with no active call passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"
3. Phone_Call.Info reads "Not_Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```
- **expected_result**：

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM goes to TLM Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 1 之無通話分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-061`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-061
- **tc_title**：Behaviour 1 with an active call passes the TLM to Timed
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Behaviour 1 with an active call passes the TLM to Timed
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"
3. Phone_Call.Info reads "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```
- **expected_result**：

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM stays there until Phone_Call.Info becomes "Not_Active"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 1 之通話中分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-062`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-062
- **tc_title**：Behaviour 2 on a Jeep with the driver door open passes to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Behaviour 2 on a Jeep with the driver door open passes to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read a value other than "00 MIN"
3. Brand_Configuration _2 reads "Jeep"
4. PhoneCall.Info reads "Not_Active"
```
- **input_test_data**：STATUS_BH_BCM1.DriverDoorSts = "Open"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data and let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```
- **expected_result**：

```
1. The TLM registers both the door signal and the mode transition
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 2 之 Jeep ＋ 駕駛門開啟分支
- **reasoning_note**：（空）

---

## 段 6 —— 063 ~ 072（8 條）

### `NR1L-PowerManagement-063`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-063
- **tc_title**：Behaviour 2 otherwise passes to Timed keeping the active source
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Behaviour 2 otherwise passes to Timed keeping the active source
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req and Timeout1 read a value other than "00 MIN"
3. Brand_Configuration _2 reads a value other than "Jeep"
4. A tuner source is currently active
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info, $Telematic_Power$ and the active source to check the transition to Timed
```
- **expected_result**：

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the current active source is maintained
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 2 之 ELSE 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-064`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-064
- **tc_title**：Behaviour 1 reached through Auto_SwitchOn_Setting.Req on LTM High
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Behaviour 1 reached through Auto_SwitchOn_Setting.Req on LTM High
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 MIN"
4. Phone_Call.Info reads "Not_Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```
- **expected_result**：

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM goes to TLM Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 1 之 LTM High 形態（`063` 驗 SwitchOff_Timeout_Setting.Req 形態）
- **reasoning_note**：**R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

### `NR1L-PowerManagement-065`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-065
- **tc_title**：Behaviour 2 reached through Auto_SwitchOn_Setting.Req on LTM High
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Behaviour 2 reached through Auto_SwitchOn_Setting.Req on LTM High
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Not_Active " and Timeout1 reads a value other than "00 MIN"
4. Brand_Configuration _2 reads a value other than "Jeep"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Let LTM_OperationalModeSts.Info transition occur
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```
- **expected_result**：

```
1. The TLM registers the LTM_OperationalModeSts.Info transition
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the current active source is maintained
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 2 之 LTM High 形態（`066` 驗 SwitchOff_Timeout_Setting.Req 形態）
- **reasoning_note**：**R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

### `NR1L-PowerManagement-066`

- **req_id**：SWE-PM-014
- **tc_id**：NR1L-PowerManagement-066
- **tc_title**：Remote Start ends at ignition pre off: RemStartFail is set true
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start ends at ignition pre off: RemStartFail is set true
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. LTM_OperationalModeSts.Info is at "Ignition Pre Off"
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts: "Remote Start Active" to "Remote Start Not Active"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read RemStartFail to check that it follows the transition
```
- **expected_result**：

```
1. The TLM accepts the transition without a bus error
2. RemStartFail reads "True"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 `Ignition Pre Off` 之觸發（其對應條驗 `Ignition Off`）
- **reasoning_note**：**G113 之首次真實命中（23 包）**：`4941504` / `4941548` 皆載觸發為 「`Ignition Pre Off` **OR** `Ignition Off`」，而首次撰寫只取 `Ignition Off`。**此為「原文以 OR 並列而 TC 只取其一」之第八、第九例** —— 與 A-PW94 / A-PW87 / A-PW119 同型，**惟本次係由 G113 於現況資料上直接攔下，非事後由反向涵蓋抓到**。依 R-P161(c) 裁為真缺口並補本條。

### `NR1L-PowerManagement-067`

- **req_id**：SWE-PM-015
- **tc_id**：NR1L-PowerManagement-067
- **tc_title**：Front_Panel_OnOff.Req press with no active call passes the TLM to Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front_Panel_OnOff.Req press with no active call passes the TLM to Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Phone_Call.Info reads "Not_Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition to Idle
```
- **expected_result**：

```
1. The TLM registers the press transition
2. VPLastStatus reads "OFF", TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req 之按下 → Idle
- **reasoning_note**：（空）

### `NR1L-PowerManagement-068`

- **req_id**：SWE-PM-015
- **tc_id**：NR1L-PowerManagement-068
- **tc_title**：CLIMATIC_PANEL.Radio_Btn0 press with no active call passes the TLM to Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CLIMATIC_PANEL.Radio_Btn0 press with no active call passes the TLM to Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Phone_Call.Info reads "Not_Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition to Idle
```
- **expected_result**：

```
1. The TLM registers the press transition
2. VPLastStatus reads "OFF", TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 之按下 → Idle
- **reasoning_note**：（空）

### `NR1L-PowerManagement-071`

- **req_id**：SWE-PM-016
- **tc_id**：NR1L-PowerManagement-071
- **tc_title**：Rear camera activation keeps the TLM in Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Rear camera activation keeps the TLM in Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Rear_View_Camera reads "Present"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Make the Rear Camera become active
2. Read the TLM screen and Rear_Camera_Enable.Info to check that images are managed
```
- **expected_result**：

```
1. The TLM stays in Full-Operation state on the camera activation
2. The rear view camera images are managed on the TLM screen until Rear_Camera_Enable.Info passes to "False"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗後視攝影機啟動時之停留與影像管理
- **reasoning_note**：（空）

### `NR1L-PowerManagement-072`

- **req_id**：SWE-PM-017
- **tc_id**：NR1L-PowerManagement-072
- **tc_title**：Rear camera deactivation restores the last active source
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Rear camera deactivation restores the last active source
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
3. Rear_View_Camera reads "Present" and the Rear Camera is active
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Make the Rear Camera become inactive
2. Read the active source to check that the last active source is managed
```
- **expected_result**：

```
1. The TLM leaves the rear view camera images on the deactivation
2. The last active source is managed according to Audio_Data_Exchange.Info and Phone_Call.Info values
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗後視攝影機關閉後之音源回復
- **reasoning_note**：（空）

---

## 段 7 —— 073 ~ 080（8 條）

### `NR1L-PowerManagement-073`

- **req_id**：SWE-PM-018
- **tc_id**：NR1L-PowerManagement-073
- **tc_title**：Ignition off in Idle passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Ignition off in Idle passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
```
- **input_test_data**：LTM_OperationalModeSts: "Ignition Off"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Idle ＋ 點火關閉 → Standby
- **reasoning_note**：（空）

### `NR1L-PowerManagement-074`

- **req_id**：SWE-PM-018
- **tc_id**：NR1L-PowerManagement-074
- **tc_title**：Ignition pre off in Idle passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Ignition pre off in Idle passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
```
- **input_test_data**：LTM_OperationalModeSts: "Ignition Pre Off"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 `Ignition Pre Off` 之觸發（`073` 之對應條驗 `Ignition Off`）
- **reasoning_note**：**G113 之首次真實命中（23 包）**：`4941504` / `4941548` 皆載觸發為 「`Ignition Pre Off` **OR** `Ignition Off`」，而首次撰寫只取 `Ignition Off`。**此為「原文以 OR 並列而 TC 只取其一」之第八、第九例** —— 與 A-PW94 / A-PW87 / A-PW119 同型，**惟本次係由 G113 於現況資料上直接攔下，非事後由反向涵蓋抓到**。依 R-P161(c) 裁為真缺口並補本條。

### `NR1L-PowerManagement-075`

- **req_id**：SWE-PM-019
- **tc_id**：NR1L-PowerManagement-075
- **tc_title**：Front_Panel_OnOff.Req press is ignored while the rear camera is enabled
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front_Panel_OnOff.Req press is ignored while the rear camera is enabled
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_View_Camera reads "Present" and Rear_Camera_Enable.Info reads "True"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read TLM_Status.Info and the screen to check that the transition is ignored
```
- **expected_result**：

```
1. The TLM receives the press transition
2. TLM_Status.Info still reads "Idle" and no Splash Screen is shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req 於後視攝影機啟用時被忽略
- **reasoning_note**：（空）

### `NR1L-PowerManagement-076`

- **req_id**：SWE-PM-019
- **tc_id**：NR1L-PowerManagement-076
- **tc_title**：Front_Panel_OnOff.Req press otherwise shows the Splash Screen and enters Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front_Panel_OnOff.Req press otherwise shows the Splash Screen and enters Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_Camera_Enable.Info reads "False"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read the screen, VPLastStatus and TLM_Status.Info to check the transition
```
- **expected_result**：

```
1. A Splash Screen is shown for Response_Wait_Time
2. VPLastStatus reads "ON", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req 之 ELSE 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-077`

- **req_id**：SWE-PM-019
- **tc_id**：NR1L-PowerManagement-077
- **tc_title**：CLIMATIC_PANEL.Radio_Btn0 press is ignored while the rear camera is enabled
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CLIMATIC_PANEL.Radio_Btn0 press is ignored while the rear camera is enabled
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_View_Camera reads "Present" and Rear_Camera_Enable.Info reads "True"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read TLM_Status.Info and the screen to check that the transition is ignored
```
- **expected_result**：

```
1. The TLM receives the press transition
2. TLM_Status.Info still reads "Idle" and no Splash Screen is shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 於後視攝影機啟用時被忽略
- **reasoning_note**：（空）

### `NR1L-PowerManagement-078`

- **req_id**：SWE-PM-019
- **tc_id**：NR1L-PowerManagement-078
- **tc_title**：CLIMATIC_PANEL.Radio_Btn0 press otherwise shows the Splash Screen and enters Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CLIMATIC_PANEL.Radio_Btn0 press otherwise shows the Splash Screen and enters Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_Camera_Enable.Info reads "False"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read the screen, VPLastStatus and TLM_Status.Info to check the transition
```
- **expected_result**：

```
1. A Splash Screen is shown for Response_Wait_Time
2. VPLastStatus reads "ON", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 之 ELSE 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-079`

- **req_id**：SWE-PM-020
- **tc_id**：NR1L-PowerManagement-079
- **tc_title**：Incoming call in Idle passes the TLM to Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Incoming call in Idle passes the TLM to Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. The call is not made through Apple CarPlay
```
- **input_test_data**：Phone_Call.Info: "Not_Active" to "Active"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. VPLastStatus reads "ON", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Idle ＋ 通話進入 → Full-Operation
- **reasoning_note**：（空）

### `NR1L-PowerManagement-080`

- **req_id**：SWE-PM-020
- **tc_id**：NR1L-PowerManagement-080
- **tc_title**：Call ending on the Phone Main Screen returns the TLM to Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Call ending on the Phone Main Screen returns the TLM to Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info reads "Full-Operation" entered through a call
3. TLM_Display.GUI is in Phone Main Screen
```
- **input_test_data**：Phone_Call.Info: "Active" to "Not_Active"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the return to Idle
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗通話結束於 Phone Main Screen 之分支
- **reasoning_note**：（空）

---

## 段 8 —— 081 ~ 088（8 條）

### `NR1L-PowerManagement-081`

- **req_id**：SWE-PM-020
- **tc_id**：NR1L-PowerManagement-081
- **tc_title**：Call ending on another screen keeps the TLM in Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Call ending on another screen keeps the TLM in Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info reads "Full-Operation" entered through a call
3. TLM_Display.GUI is on a screen other than Phone Main Screen
```
- **input_test_data**：Phone_Call.Info: "Active" to "Not_Active"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info to check that Full-Operation state is kept
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info still reads "Full-Operation" and the TLM stays in Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗通話結束於其他畫面之分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-082`

- **req_id**：SWE-PM-021
- **tc_id**：NR1L-PowerManagement-082
- **tc_title**：Rear camera enable in Idle keeps Idle with video only
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Rear camera enable in Idle keeps Idle with video only
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
3. Rear_View_Camera reads "Present"
```
- **input_test_data**：Rear_Camera_Enable.Info: "False" to "True"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and the screen content to check what the screen shows
```
- **expected_result**：

```
1. The TLM registers the transition without leaving Idle state
2. The screen shows the rear view camera video and nothing else
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Idle 下後視攝影機啟用之停留與畫面限制
- **reasoning_note**：（空）

### `NR1L-PowerManagement-083`

- **req_id**：SWE-PM-022
- **tc_id**：NR1L-PowerManagement-083
- **tc_title**：Logistic mode on passes the TLM to Logistic Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Logistic mode on passes the TLM to Logistic Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"
```
- **input_test_data**：PowerModeSts_Telematic: "Standard_Power" to "Logistic_Mode_On"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info reads "Logistic Idle", $Telematic_Power$ reads "Logistic_On" and the TLM passes to Logistic Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗物流模式進入
- **reasoning_note**：（空）

### `NR1L-PowerManagement-084`

- **req_id**：SWE-PM-023
- **tc_id**：NR1L-PowerManagement-084
- **tc_title**：Leaving Ignition Off in Timed passes the TLM to Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Leaving Ignition Off in Timed passes the TLM to Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
```
- **input_test_data**：LTM_OperationalModeSts.Info: from "Ignition Off" to another value
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read VPLastStatus, TLM_Status.Info and $Telematic_Power$ to check the transition
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. VPLastStatus reads "On", TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Timed ＋ 離開 Ignition Off → Full-Operation
- **reasoning_note**：（空）

### `NR1L-PowerManagement-085`

- **req_id**：SWE-PM-024
- **tc_id**：NR1L-PowerManagement-085
- **tc_title**：Remote Start not active on leaving Ignition Off clears RemStartFail
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start not active on leaving Ignition Off clears RemStartFail
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. STATUS_BH_BCM2.RemStActvSts reads "Remote Start Not Active"
```
- **input_test_data**：LTM_OperationalModeSts.Info: from "Ignition Off" to another value
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read VPLastStatus, RemStartFail and TLM_Status.Info to check the resulting values
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. VPLastStatus reads "On", RemStartFail reads "False" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Remote Start Not Active 下之 RemStartFail 清除
- **reasoning_note**：（空）

### `NR1L-PowerManagement-086`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-086
- **tc_title**：Front_Panel_OnOff.Req press in Timed with an active call shows a popup
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front_Panel_OnOff.Req press in Timed with an active call shows a popup
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read the screen to check that the transfer popup is shown
```
- **expected_result**：

```
1. The TLM registers the press transition
2. A popup asking whether to transfer the call is shown to the user
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req ＋ 通話中之 popup
- **reasoning_note**：（空）

### `NR1L-PowerManagement-087`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-087
- **tc_title**：Accepting the Front_Panel_OnOff.Req popup passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Accepting the Front_Panel_OnOff.Req popup passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Accept the popup as the user
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```
- **expected_result**：

```
1. The TLM accepts the user answer
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req popup 之接受分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-088`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-088
- **tc_title**：Declining the Front_Panel_OnOff.Req popup keeps the TLM in Timed
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Declining the Front_Panel_OnOff.Req popup keeps the TLM in Timed
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Decline the popup as the user
2. Read TLM_Status.Info to check that Timed state is kept
```
- **expected_result**：

```
1. The TLM accepts the user answer
2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req popup 之拒絕分支
- **reasoning_note**：（空）

---

## 段 9 —— 089 ~ 098（8 條）

### `NR1L-PowerManagement-089`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-089
- **tc_title**：Front_Panel_OnOff.Req press in Timed with no active call passes to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front_Panel_OnOff.Req press in Timed with no active call passes to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Not_Active"
4. A tuner source is currently active
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive Front_Panel_OnOff.Req from "Not_Pressed" to "Pressed"
2. Read the active functionality and TLM_Status.Info to check the transition to Standby
```
- **expected_result**：

```
1. The active functionality stops and no source stays active
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req ＋ 無通話之直接轉換
- **reasoning_note**：（空）

### `NR1L-PowerManagement-090`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-090
- **tc_title**：CLIMATIC_PANEL.Radio_Btn0 press in Timed with an active call shows a popup
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CLIMATIC_PANEL.Radio_Btn0 press in Timed with an active call shows a popup
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read the screen to check that the transfer popup is shown
```
- **expected_result**：

```
1. The TLM registers the press transition
2. A popup asking whether to transfer the call is shown to the user
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 通話中之 popup
- **reasoning_note**：（空）

### `NR1L-PowerManagement-091`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-091
- **tc_title**：Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Accepting the CLIMATIC_PANEL.Radio_Btn0 popup passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Accept the popup as the user
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Standby
```
- **expected_result**：

```
1. The TLM accepts the user answer
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之接受分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-092`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-092
- **tc_title**：Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Declining the CLIMATIC_PANEL.Radio_Btn0 popup keeps the TLM in Timed
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. The transfer popup is shown
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Decline the popup as the user
2. Read TLM_Status.Info to check that Timed state is kept
```
- **expected_result**：

```
1. The TLM accepts the user answer
2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 popup 之拒絕分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-093`

- **req_id**：SWE-PM-025
- **tc_id**：NR1L-PowerManagement-093
- **tc_title**：CLIMATIC_PANEL.Radio_Btn0 press in Timed with no active call passes to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：CLIMATIC_PANEL.Radio_Btn0 press in Timed with no active call passes to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Phone_Call.Info reads "Not_Active"
4. A tuner source is currently active
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" to "Pressed"
2. Read the active functionality and TLM_Status.Info to check the transition to Standby
```
- **expected_result**：

```
1. The active functionality stops and no source stays active
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ 無通話之直接轉換
- **reasoning_note**：（空）

### `NR1L-PowerManagement-094`

- **req_id**：SWE-PM-026
- **tc_id**：NR1L-PowerManagement-094
- **tc_title**：Door open on a Jeep from Full-Operation passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Door open on a Jeep from Full-Operation passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
4. The previous internal state was "Full-Operation" and PhoneCall.Info reads "Not_Active"
```
- **input_test_data**：STATUS_BH_BCM1.DriverDoorSts = "Open"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read the active functionality and TLM_Status.Info to check the transition to Standby
```
- **expected_result**：

```
1. The active functionality stops and no source stays active
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Jeep 車門開啟 ＋ 前狀態 Full-Operation 之分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-095`

- **req_id**：SWE-PM-026
- **tc_id**：NR1L-PowerManagement-095
- **tc_title**：Door open with an active call keeps the TLM in Timed
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Door open with an active call keeps the TLM in Timed
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. Brand_Configuration_2 reads "Jeep" and SWITCH_OFF_DOOR reads "enable"
4. PhoneCall.Info reads "Active"
```
- **input_test_data**：STATUS_BH_BCM1.PsngrDoorSts = "Open"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info to check that Timed state is kept
```
- **expected_result**：

```
1. The TLM registers the door signal without a bus error
2. TLM_Status.Info still reads "Timed" and the TLM stays in Timed state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗通話中之門開啟分支，**並承擔 OR 之右支 `STATUS_BH_BCM1.PsngrDoorSts`**（R-P202 —— 使該涵蓋自附帶轉為設計）
- **reasoning_note**：R-P202：本 leaf 之拆分軸為前狀態與通話狀態，而 `source_clause` 之車門 OR 有二支。**本條指定承擔 `PsngrDoorSts` 支**，`094` / `096` / `097` 承擔 `DriverDoorSts` 支。改寫本條時**須保留副駕駛門之輸入**，否則該支之涵蓋將無聲消失。

### `NR1L-PowerManagement-098`

- **req_id**：SWE-PM-027
- **tc_id**：NR1L-PowerManagement-098
- **tc_title**：Antitheft failure clears the activation request within Timeout1
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft failure clears the activation request within Timeout1
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```
- **input_test_data**：Antitheft_Result.Info = "Not_Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req and the screen to check the reset and the screen time
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False" and the Antitheft screens are shown for a time not longer than Timeout1
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗防盜失敗後之請求復歸與畫面時限
- **reasoning_note**：（空）

---

## 段 10 —— 099 ~ 106（8 條）

### `NR1L-PowerManagement-099`

- **req_id**：SWE-PM-027
- **tc_id**：NR1L-PowerManagement-099
- **tc_title**：Antitheft failure in Partial Operation keeps the original state
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft failure in Partial Operation keeps the original state
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in Partial Operation
3. Antitheft_Activation.Req reads "True"
```
- **input_test_data**：Antitheft_Result.Info = "Not_Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req and the TLM state to check that the state is kept
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original state Partial Operation and the Antitheft screens are shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗防盜失敗於 Partial Operation 之停留
- **reasoning_note**：（空）

### `NR1L-PowerManagement-100`

- **req_id**：SWE-PM-028
- **tc_id**：NR1L-PowerManagement-100
- **tc_title**：Antitheft success clears the activation request
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success clears the activation request
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req to check that it is set back
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗防盜成功後之請求復歸
- **reasoning_note**：（空）

### `NR1L-PowerManagement-101`

- **req_id**：SWE-PM-028
- **tc_id**：NR1L-PowerManagement-101
- **tc_title**：Antitheft success with a zero timeout takes Timeout1 from PROXI
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success with a zero timeout takes Timeout1 from PROXI
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. Switch_Off_Time reads 20 minutes
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```
- **expected_result**：

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Timeout1 之暫時取值與其復歸
- **reasoning_note**：（空）

### `NR1L-PowerManagement-102`

- **req_id**：SWE-PM-028
- **tc_id**：NR1L-PowerManagement-102
- **tc_title**：Antitheft success passes the TLM to Timed state
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success passes the TLM to Timed state
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM passes to TLM Timed state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗防盜成功後之狀態轉換
- **reasoning_note**：（空）

### `NR1L-PowerManagement-103`

- **req_id**：SWE-PM-028
- **tc_id**：NR1L-PowerManagement-103
- **tc_title**：Antitheft success on LTM High takes Timeout1 from PROXI
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success on LTM High takes Timeout1 from PROXI
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. An LTM High Radio is present in the bench configuration
3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN"
4. Switch_Off_Time reads 20 minutes
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```
- **expected_result**：

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 LTM High 形態之 Timeout1 取值（`100` 之對應條驗 SwitchOff_Timeout_Setting.Req 形態）
- **reasoning_note**：**R-P118(d) 反向涵蓋裁決（22 包）**：原文以 OR 並列而首次撰寫只取其一 —— 與 A-PW94（`Ignition Pre Off` / `Ignition Off`）、A-PW87（`greater` 負分支）、R-P117(c)（`BODY OFF-TIMED`）同型。裁為**真缺口**並補本條。

### `NR1L-PowerManagement-104`

- **req_id**：SWE-PM-029
- **tc_id**：NR1L-PowerManagement-104
- **tc_title**：Antitheft success clears the activation request on this variant
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success clears the activation request on this variant
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req to check that it is set back
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗本變體之請求復歸
- **reasoning_note**：（空）

### `NR1L-PowerManagement-105`

- **req_id**：SWE-PM-029
- **tc_id**：NR1L-PowerManagement-105
- **tc_title**：Timeout1 follows Switch_Off_Time when the setting is zero
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Timeout1 follows Switch_Off_Time when the setting is zero
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. Switch_Off_Time reads 20 minutes
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```
- **expected_result**：

```
1. Timeout1 reads 20 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Timeout1 取自 Switch_Off_Time 之分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-106`

- **req_id**：SWE-PM-029
- **tc_id**：NR1L-PowerManagement-106
- **tc_title**：Timeout1 follows PwrAccDelayAct when the setting is zero
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Timeout1 follows PwrAccDelayAct when the setting is zero
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SwitchOff_Timeout_Setting.Req reads "00 min"
3. $PwrAccDelayAct$ reads 10 minutes
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read Timeout1 and then trigger an Ignition On event to check the restore
```
- **expected_result**：

```
1. Timeout1 reads 10 minutes after the antitheft success
2. Timeout1 reads "00 minutes" again at the next Ignition On event
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Timeout1 取自 $PwrAccDelayAct$ 之分支
- **reasoning_note**：（空）

---

## 段 11 —— 107 ~ 114（8 條）

### `NR1L-PowerManagement-107`

- **req_id**：SWE-PM-029
- **tc_id**：NR1L-PowerManagement-107
- **tc_title**：Antitheft success on this variant passes the TLM to Timed
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success on this variant passes the TLM to Timed
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```
- **input_test_data**：Antitheft_Result.Info = "Successfully"
- **test_procedure**：

```
1. Send the signal listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition to Timed
```
- **expected_result**：

```
1. The TLM accepts the signal without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Timed" and the TLM passes to TLM Timed state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗本變體之狀態轉換
- **reasoning_note**：（空）

### `NR1L-PowerManagement-108`

- **req_id**：SWE-PM-030
- **tc_id**：NR1L-PowerManagement-108
- **tc_title**：Splash Screen is shown for the configured wait time
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Splash Screen is shown for the configured wait time
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM through the switch on sequence
2. Read the screen and its duration to check the Splash Screen presentation
```
- **expected_result**：

```
1. A proper Splash Screen is shown on the TLM screen
2. The Splash Screen stays for Response_Wait_Time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Auto_SwitchOn_Setting.Req 為 Active 時之 Splash Screen
- **reasoning_note**：（空）

### `NR1L-PowerManagement-109`

- **req_id**：SWE-PM-030
- **tc_id**：NR1L-PowerManagement-109
- **tc_title**：Splash Screen is shown for the Recall_Last branch
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Splash Screen is shown for the Recall_Last branch
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Recall_Last"
3. VPLastStatus reads "On"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM through the switch on sequence
2. Read the screen and its duration to check the Splash Screen presentation
```
- **expected_result**：

```
1. A proper Splash Screen is shown on the TLM screen
2. The Splash Screen stays for Response_Wait_Time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 Recall_Last ＋ VPLastStatus == On
- **reasoning_note**：R-P118(d) 反向涵蓋裁決（G113 分桶，R-P171）—— `source_clause` 之 OR 右支 `Auto_SwitchOn_Setting.Req == Recall_Last AND VPLastStatus == On` 原無任何 TC 覆蓋，裁為真缺口並補此條。為 G113 前瞻捕獲之第十例。

### `NR1L-PowerManagement-110`

- **req_id**：SWE-PM-031
- **tc_id**：NR1L-PowerManagement-110
- **tc_title**：Rear view camera images follow the enable signal in any state
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Rear view camera images follow the enable signal in any state
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Rear_View_Camera reads "Present"
3. The TLM is in Standby state
```
- **input_test_data**：Rear_Camera_Enable.Info: "False" then "True"
- **test_procedure**：

```
1. Send the two values listed in Input Test Data in turn
2. Read the screen against TLM_Status.Info to check that images follow the signal only
```
- **expected_result**：

```
1. No rear view camera images are shown while the signal reads "False"
2. The rear view camera images are shown while the signal reads "True" regardless of TLM_Status.Info
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗後視影像之顯示與狀態無關
- **reasoning_note**：（空）

### `NR1L-PowerManagement-111`

- **req_id**：SWE-PM-032
- **tc_id**：NR1L-PowerManagement-111
- **tc_title**：Remote Start from Standby passes the TLM to Partial Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote Start from Standby passes the TLM to Partial Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts: "Remote Start Not Active" to "Remote Start Active"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the transition
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Partial Operation" and the TLM passes to TLM Partial Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Standby ＋ Remote Start → Partial Operation
- **reasoning_note**：（空）

### `NR1L-PowerManagement-112`

- **req_id**：SWE-PM-033
- **tc_id**：NR1L-PowerManagement-112
- **tc_title**：Ignition Pre Off from Partial Operation passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Ignition Pre Off from Partial Operation passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Partial Operation"
```
- **input_test_data**：LTM_OperationalModeSts: transition to "Ignition Pre Off"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the resulting state
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 Ignition Pre Off
- **reasoning_note**：（空）

### `NR1L-PowerManagement-113`

- **req_id**：SWE-PM-033
- **tc_id**：NR1L-PowerManagement-113
- **tc_title**：Ignition Off from Partial Operation passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Ignition Off from Partial Operation passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Partial Operation"
```
- **input_test_data**：LTM_OperationalModeSts: transition to "Ignition Off"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read TLM_Status.Info and $Telematic_Power$ to check the resulting state
```
- **expected_result**：

```
1. The TLM registers the transition without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to TLM Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 Ignition Off
- **reasoning_note**：（空）

### `NR1L-PowerManagement-114`

- **req_id**：SWE-PM-034
- **tc_id**：NR1L-PowerManagement-114
- **tc_title**：Front panel press in Partial Operation arms the antitheft and shows the Splash Screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front panel press in Partial Operation arms the antitheft and shows the Splash Screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Partial Operation"
```
- **input_test_data**：Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read the antitheft request and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "True"
2. A proper Splash Screen is shown for Response_Wait_Time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Partial Operation 之前面板觸發
- **reasoning_note**：（空）

---

## 段 12 —— 115 ~ 123（8 條）

### `NR1L-PowerManagement-115`

- **req_id**：SWE-PM-035
- **tc_id**：NR1L-PowerManagement-115
- **tc_title**：Antitheft success with auto switch on active passes the TLM to Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success with auto switch on active passes the TLM to Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request, the screen and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False" and a proper Splash Screen is shown for Response_Wait_Time
2. VPLastStatus reads "On" and TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 1（Active）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-116`

- **req_id**：SWE-PM-035
- **tc_id**：NR1L-PowerManagement-116
- **tc_title**：Antitheft success with auto switch on not active passes the TLM to Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success with auto switch on not active passes the TLM to Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Not_Active"
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. VPLastStatus reads "Off" and TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 2（Not_Active）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-117`

- **req_id**：SWE-PM-035
- **tc_id**：NR1L-PowerManagement-117
- **tc_title**：Antitheft success with recall last and last status on passes the TLM to Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success with recall last and last status on passes the TLM to Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Recall_Last"
3. VPLastStatus reads "On"
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the screen and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. A proper Splash Screen is shown for Response_Wait_Time
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 3 之 VPLastStatus On 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-118`

- **req_id**：SWE-PM-035
- **tc_id**：NR1L-PowerManagement-118
- **tc_title**：Antitheft success with recall last and last status off passes the TLM to Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success with recall last and last status off passes the TLM to Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Recall_Last"
3. VPLastStatus reads "Off"
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 3 之 VPLastStatus Off 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-119`

- **req_id**：SWE-PM-036
- **tc_id**：NR1L-PowerManagement-119
- **tc_title**：Remote start from Timed passes the TLM to Partial Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Remote start from Timed passes the TLM to Partial Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
```
- **input_test_data**：STATUS_BH_BCM2.RemStActvSts: "Remote Start Not Active" to "Remote Start Active"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read the remote start outcome flags and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. RemStartFail reads "False" and VPLastStatus reads "On"
2. TLM_Status.Info and $Telematic_Power$ read "Partial-Operation" and the TLM passes to TLM Partial Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Timed ＋ Remote Start → Partial Operation
- **reasoning_note**：（空）

### `NR1L-PowerManagement-120`

- **req_id**：SWE-PM-037
- **tc_id**：NR1L-PowerManagement-120
- **tc_title**：Call end in Timed with a failed remote start passes the TLM to Standby
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Call end in Timed with a failed remote start passes the TLM to Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Timed"
3. RemStartFail reads "True"
```
- **input_test_data**：PhoneCall.Info: "not Active"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the remote start outcome flag and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. RemStartFail reads "False"
2. TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM passes to Standby state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Timed ＋ 通話結束 ＋ RemStartFail 為真
- **reasoning_note**：（空）

### `NR1L-PowerManagement-122`

- **req_id**：SWE-PM-039
- **tc_id**：NR1L-PowerManagement-122
- **tc_title**：A zero switch off timeout loads Timeout1 from the PROXI value
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A zero switch off timeout loads Timeout1 from the PROXI value
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info was equal to "Full-Operation"
```
- **input_test_data**：SwitchOff_Timeout_Setting.Req: "00 min"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read Timeout1 against the configured parameter to check the loaded value
```
- **expected_result**：

```
1. The TLM registers the value without a bus error
2. Timeout1 reads the "Switch_Off_Time" PROXI value
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.7.1.1.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 SwitchOff_Timeout_Setting.Req
- **reasoning_note**：（空）

### `NR1L-PowerManagement-123`

- **req_id**：SWE-PM-039
- **tc_id**：NR1L-PowerManagement-123
- **tc_title**：Auto switch on active on LTM High Radio loads Timeout1 from the PROXI value
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Auto switch on active on LTM High Radio loads Timeout1 from the PROXI value
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info was equal to "Full-Operation"
3. The unit is an LTM High Radio
```
- **input_test_data**：Auto_SwitchOn_Setting.Req: "Active"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read Timeout1 against the configured parameter to check the loaded value
```
- **expected_result**：

```
1. The TLM registers the value without a bus error
2. Timeout1 reads the "Switch_Off_Time" PROXI value
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.7.1.1.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 Auto_SwitchOn_Setting.Req for LTM High Radio
- **reasoning_note**：（空）

---

## 段 13 —— 125 ~ 133（8 條）

### `NR1L-PowerManagement-125`

- **req_id**：SWE-PM-040
- **tc_id**：NR1L-PowerManagement-125
- **tc_title**：A normal power down into Suspend to RAM starts the 8 day timer
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A normal power down into Suspend to RAM starts the 8 day timer
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Suspend to RAM is allowed on the HU
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through a normal power down sequence
2. Read the HU timer and its power mode to check the resulting behavior
```
- **expected_result**：

```
1. The HU starts an 8 day timer
2. The HU enters low power mode
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.12
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Suspend to RAM 之正常關機序列
- **reasoning_note**：（空）

### `NR1L-PowerManagement-126`

- **req_id**：SWE-PM-041
- **tc_id**：NR1L-PowerManagement-126
- **tc_title**：No TLM function is available in the TLM off with network on status
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：No TLM function is available in the TLM off with network on status
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition Off working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM OFF with Network on
2. Read the FPDM, AMP, ICS and DTV functions to check their availability
```
- **expected_result**：

```
1. The TLM reaches the status related to TLM OFF with Network on
2. No TLM, FPDM, AMP, ICS and DTV functionality is available
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.6
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Network on 狀態之功能不可用
- **reasoning_note**：（空）

### `NR1L-PowerManagement-127`

- **req_id**：SWE-PM-041
- **tc_id**：NR1L-PowerManagement-127
- **tc_title**：Entering the TLM off with network on status clears the antitheft request
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Entering the TLM off with network on status clears the antitheft request
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition Pre Off working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM OFF with Network on
2. Read the antitheft request to check its value on entering the status
```
- **expected_result**：

```
1. The TLM reaches the status related to TLM OFF with Network on
2. Antitheft_Activation.Req reads "False"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.6
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Network on 狀態之進入動作
- **reasoning_note**：（空）

### `NR1L-PowerManagement-128`

- **req_id**：SWE-PM-042
- **tc_id**：NR1L-PowerManagement-128
- **tc_title**：No TLM function is available in the TLM off with network off status
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：No TLM function is available in the TLM off with network off status
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition Off working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM OFF with Network off
2. Read the FPDM, AMP, ICS and DTV functions to check their availability
```
- **expected_result**：

```
1. The TLM reaches the status related to TLM OFF with Network off
2. No TLM, FPDM AMP, ICS and DTV functionality is available
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.7
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Network off 狀態之功能不可用
- **reasoning_note**：（空）

### `NR1L-PowerManagement-129`

- **req_id**：SWE-PM-042
- **tc_id**：NR1L-PowerManagement-129
- **tc_title**：Entering the TLM off with network off status clears the antitheft request
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Entering the TLM off with network off status clears the antitheft request
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition Pre Off working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM OFF with Network off
2. Read the antitheft request to check its value on entering the status
```
- **expected_result**：

```
1. The TLM reaches the status related to TLM OFF with Network off
2. Antitheft_Activation.Req reads "False"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.7
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Network off 狀態之進入動作
- **reasoning_note**：（空）

### `NR1L-PowerManagement-130`

- **req_id**：SWE-PM-043
- **tc_id**：NR1L-PowerManagement-130
- **tc_title**：The backlight stays off during Standby mode
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The backlight stays off during Standby mode
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in Standby mode
3. No HMI screen is required
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Leave the HU in Standby mode without requesting an HMI screen
2. Read the display backlight to check whether it stays off
```
- **expected_result**：

```
1. The HU stays in Standby mode
2. The backlight is OFF
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Standby 之背光關閉常態
- **reasoning_note**：（空）

### `NR1L-PowerManagement-132`

- **req_id**：SWE-PM-044
- **tc_id**：NR1L-PowerManagement-132
- **tc_title**：Front panel press in Standby arms the antitheft and shows the Splash Screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front panel press in Standby arms the antitheft and shows the Splash Screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
3. The Engineering Line is deactivated
```
- **input_test_data**：Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read the antitheft request and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "True"
2. A proper Splash Screen is shown for Response_Wait_Time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req ＋ OR 之左支 Standby
- **reasoning_note**：（空）

### `NR1L-PowerManagement-133`

- **req_id**：SWE-PM-044
- **tc_id**：NR1L-PowerManagement-133
- **tc_title**：Front panel press in Sleep arms the antitheft and shows the Splash Screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Front panel press in Sleep arms the antitheft and shows the Splash Screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Sleep"
3. The Engineering Line is deactivated
```
- **input_test_data**：Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read the antitheft request and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "True"
2. A proper Splash Screen is shown for Response_Wait_Time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Front_Panel_OnOff.Req ＋ OR 之右支 Sleep
- **reasoning_note**：（空）

---

## 段 14 —— 134 ~ 142（8 條）

### `NR1L-PowerManagement-134`

- **req_id**：SWE-PM-044
- **tc_id**：NR1L-PowerManagement-134
- **tc_title**：Climatic panel press in Standby arms the antitheft and shows the Splash Screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Climatic panel press in Standby arms the antitheft and shows the Splash Screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
3. The Engineering Line is deactivated
```
- **input_test_data**：CLIMATIC_PANEL.Radio_Btn0: "Not_Pressed" to "Pressed"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read the antitheft request and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "True"
2. A proper Splash Screen is shown for Response_Wait_Time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ OR 之左支 Standby
- **reasoning_note**：（空）

### `NR1L-PowerManagement-135`

- **req_id**：SWE-PM-044
- **tc_id**：NR1L-PowerManagement-135
- **tc_title**：Climatic panel press in Sleep arms the antitheft and shows the Splash Screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Climatic panel press in Sleep arms the antitheft and shows the Splash Screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Sleep"
3. The Engineering Line is deactivated
```
- **input_test_data**：CLIMATIC_PANEL.Radio_Btn0: "Not_Pressed" to "Pressed"
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read the antitheft request and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "True"
2. A proper Splash Screen is shown for Response_Wait_Time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CLIMATIC_PANEL.Radio_Btn0 ＋ OR 之右支 Sleep
- **reasoning_note**：（空）

### `NR1L-PowerManagement-136`

- **req_id**：SWE-PM-045
- **tc_id**：NR1L-PowerManagement-136
- **tc_title**：A failed antitheft keeps the TLM in the original Standby state
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A failed antitheft keeps the TLM in the original Standby state
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
```
- **input_test_data**：Antitheft_Result.Info: "Not_Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Standby state for at most Timeout1, with proper HMI Antitheft screens
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 Standby
- **reasoning_note**：（空）

### `NR1L-PowerManagement-137`

- **req_id**：SWE-PM-045
- **tc_id**：NR1L-PowerManagement-137
- **tc_title**：A failed antitheft keeps the TLM in the original Sleep state
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A failed antitheft keeps the TLM in the original Sleep state
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Sleep"
```
- **input_test_data**：Antitheft_Result.Info: "Not_Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Sleep state for at most Timeout1, with proper HMI Antitheft screens
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 Sleep
- **reasoning_note**：（空）

### `NR1L-PowerManagement-138`

- **req_id**：SWE-PM-046
- **tc_id**：NR1L-PowerManagement-138
- **tc_title**：Rear view camera is provided while the antitheft is still in progress
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Rear view camera is provided while the antitheft is still in progress
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The Rear_View_Camera PROXI parameter reads "Present"
3. Rear_Camera_Enable.Info reads "True"
```
- **input_test_data**：Antitheft_Result.Info: "In_Progress"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the screen and the audio path to check the rear view camera component
```
- **expected_result**：

```
1. The TLM registers the value without a bus error
2. The TLM provides audio and video for the rear view camera component as soon as the images are available
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 In_Progress
- **reasoning_note**：（空）

### `NR1L-PowerManagement-139`

- **req_id**：SWE-PM-046
- **tc_id**：NR1L-PowerManagement-139
- **tc_title**：Rear view camera is provided after an unsuccessful antitheft
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Rear view camera is provided after an unsuccessful antitheft
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The Rear_View_Camera PROXI parameter reads "Present"
3. Rear_Camera_Enable.Info reads "True"
```
- **input_test_data**：Antitheft_Result.Info: "Not_Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the screen and the audio path to check the rear view camera component
```
- **expected_result**：

```
1. The TLM registers the value without a bus error
2. The TLM provides audio and video for the rear view camera component as long as Rear_Camera_Enable.Info reads "True"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 Not_Successfully
- **reasoning_note**：（空）

### `NR1L-PowerManagement-140`

- **req_id**：SWE-PM-047
- **tc_id**：NR1L-PowerManagement-140
- **tc_title**：A failed antitheft keeps the TLM in Standby and shows the antitheft screens
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A failed antitheft keeps the TLM in Standby and shows the antitheft screens
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
```
- **input_test_data**：Antitheft_Result.Info: "Not_Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request, the TLM state and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Standby state and proper HMI Antitheft screens are shown if needed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 Standby
- **reasoning_note**：（空）

### `NR1L-PowerManagement-142`

- **req_id**：SWE-PM-048
- **tc_id**：NR1L-PowerManagement-142
- **tc_title**：Antitheft success with auto switch on active reaches Full-Operation after the mode transition
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success with auto switch on active reaches Full-Operation after the mode transition
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
3. The LTM_OperationalModeSts.Info transition has occurred
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 1（Active）
- **reasoning_note**：（空）

---

## 段 15 —— 143 ~ 151（8 條）

### `NR1L-PowerManagement-143`

- **req_id**：SWE-PM-048
- **tc_id**：NR1L-PowerManagement-143
- **tc_title**：Antitheft success with auto switch on not active reaches Idle after the mode transition
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success with auto switch on not active reaches Idle after the mode transition
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Not_Active"
3. The LTM_OperationalModeSts.Info transition has occurred
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 2（Not_Active）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-144`

- **req_id**：SWE-PM-048
- **tc_id**：NR1L-PowerManagement-144
- **tc_title**：Recall last with last status on reaches Full-Operation after the mode transition
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Recall last with last status on reaches Full-Operation after the mode transition
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Recall_Last"
3. VPLastStatus reads "ON"
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. The TLM registers the value without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 3 之 VPLastStatus ON 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-145`

- **req_id**：SWE-PM-048
- **tc_id**：NR1L-PowerManagement-145
- **tc_title**：Recall last with last status off reaches Idle after the mode transition
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Recall last with last status off reaches Idle after the mode transition
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Recall_Last"
3. VPLastStatus reads "OFF"
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. The TLM registers the value without a bus error
2. TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to TLM Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Behaviour 3 之 VPLastStatus OFF 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-147`

- **req_id**：SWE-PM-049
- **tc_id**：NR1L-PowerManagement-147
- **tc_title**：A failed antitheft keeps the TLM blocked in Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A failed antitheft keeps the TLM blocked in Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Idle"
```
- **input_test_data**：Antitheft_Result.Info: "Not_Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request, the TLM state and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays blocked in Idle state and proper HMI Antitheft screens are shown if needed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Idle 之封鎖分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-148`

- **req_id**：SWE-PM-050
- **tc_id**：NR1L-PowerManagement-148
- **tc_title**：The else branch stores the last status off and passes the TLM to Idle
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The else branch stores the last status off and passes the TLM to Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The condition of the preceding clause of this chapter is not met
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM through the switch on sequence with that condition not met
2. Read the stored last status and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. VPLastStatus reads "Off"
2. TLM_Status.Info and $Telematic_Power$ read "Idle" and the TLM passes to Idle state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 ELSE 分支
- **reasoning_note**：本 leaf 之錨點原文以 `ELSE` 起首，其**前件不在本 leaf 之錨點內** ——前提僅能寫成「前一條款之條件未成立」。已列為觀察，見上繳 §五。

### `NR1L-PowerManagement-149`

- **req_id**：SWE-PM-051
- **tc_id**：NR1L-PowerManagement-149
- **tc_title**：Antitheft success stores the last status on and passes the TLM to Full-Operation
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Antitheft success stores the last status on and passes the TLM to Full-Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is running the antitheft check
```
- **input_test_data**：Antitheft_Result.Info: "Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request, the stored last status and the TLM state to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False" and VPLastStatus reads "On"
2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation" and the TLM passes to TLM Full-Operation state
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Successfully 分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-150`

- **req_id**：SWE-PM-052
- **tc_id**：NR1L-PowerManagement-150
- **tc_title**：A failed antitheft keeps the TLM in the original Partial Operation state
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A failed antitheft keeps the TLM in the original Partial Operation state
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Partial Operation"
```
- **input_test_data**：Antitheft_Result.Info: "Not_Successfully"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the antitheft request, the TLM state and the screen to check the resulting behavior
```
- **expected_result**：

```
1. Antitheft_Activation.Req reads "False"
2. The TLM stays in the original Partial Operation state and proper HMI Antitheft screens are shown if needed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Partial Operation 之留置分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-151`

- **req_id**：SWE-PM-053
- **tc_id**：NR1L-PowerManagement-151
- **tc_title**：The vehicle brand logo screen follows the brand configuration parameter
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The vehicle brand logo screen follows the brand configuration parameter
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM carries a configured brand parameter
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the brand logo screen presentation
2. Read the shown logo against the configured parameter to check the source of the logo
```
- **expected_result**：

```
1. The brand logo screen is presented
2. The vehicle brand logo shown matches the Brand_Configuration_2 PROXI parameter
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Brand_Configuration_2 之讀取
- **reasoning_note**：（空）

---

## 段 16 —— 152 ~ 160（8 條）

### `NR1L-PowerManagement-152`

- **req_id**：SWE-PM-054
- **tc_id**：NR1L-PowerManagement-152
- **tc_title**：No audio brand without SDARS shows the vehicle brand logo only
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：No audio brand without SDARS shows the vehicle brand logo only
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Absent"
```
- **input_test_data**：Audio_Brand: "No Audio Brand"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. The vehicle brand logo that depends on the Brand_Configuration_2 parameter value is shown alone
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合一（Absent ＋ No Audio Brand）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-153`

- **req_id**：SWE-PM-054
- **tc_id**：NR1L-PowerManagement-153
- **tc_title**：Beats brand white without SDARS adds the Beats logo
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：Beats brand white without SDARS adds the Beats logo
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Absent"
```
- **input_test_data**：Audio_Brand: "Beats Brand White"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. The Beats Brand White logo is shown in addition to the vehicle brand logo
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合二（Absent ＋ Beats Brand White）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-154`

- **req_id**：SWE-PM-054
- **tc_id**：NR1L-PowerManagement-154
- **tc_title**：SDARS present without audio brand adds the Sirius logo
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：SDARS present without audio brand adds the Sirius logo
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Present"
```
- **input_test_data**：Audio_Brand: "No Audio Brand"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. The Sirius logo is shown in addition to the vehicle brand logo
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合三（Present ＋ No Audio Brand）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-155`

- **req_id**：SWE-PM-054
- **tc_id**：NR1L-PowerManagement-155
- **tc_title**：SDARS present with beats brand white adds both logos
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：SDARS present with beats brand white adds both logos
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Present"
```
- **input_test_data**：Audio_Brand: "Beats Brand White"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. Both the Sirius and the Beats logos are shown in addition to the vehicle brand logo
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合四（Present ＋ Beats Brand White）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-156`

- **req_id**：SWE-PM-055
- **tc_id**：NR1L-PowerManagement-156
- **tc_title**：The special package drives the Klipsch Splash Screen on the 2025 model year
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The special package drives the Klipsch Splash Screen on the 2025 model year
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The ETM carries $VC_MODEL_YEAR$ equal to "2025"
3. The ETM carries $VC_VEH_LINE$ equal to "DT"
```
- **input_test_data**：$VC_SpecialPKG_IC$: "Tungsten (147)"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown Splash Screen to check which screen the ETM displays
```
- **expected_result**：

```
1. The ETM accepts the configuration value
2. The Klipsch Splash Screen is displayed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 2025 年式之 $VC_SpecialPKG_IC$ 路徑
- **reasoning_note**：（空）

### `NR1L-PowerManagement-158`

- **req_id**：SWE-PM-056
- **tc_id**：NR1L-PowerManagement-158
- **tc_title**：The Fiat Latam startup animation replaces the vehicle brand logo
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The Fiat Latam startup animation replaces the vehicle brand logo
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU carries a configured vehicle brand
```
- **input_test_data**：DID "Startup Animation Selection": "Fiat Latam"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logo against the configured brand to check which logo the HU displays
```
- **expected_result**：

```
1. The HU accepts the configuration value
2. The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Fiat Latam 之覆蓋規則
- **reasoning_note**：（空）

### `NR1L-PowerManagement-159`

- **req_id**：SWE-PM-058
- **tc_id**：NR1L-PowerManagement-159
- **tc_title**：The ex-factory default sets a zero switch off timeout
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The ex-factory default sets a zero switch off timeout
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM carries the ex-factory configuration
3. The unit is an LTM High Radio
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Read the user selectable timeout parameter on an ex-factory unit
2. Read the auto switch on parameter and Timeout1 to check the ex-factory default of this clause
```
- **expected_result**：

```
1. SwitchOff_Timeout_Setting.Req reads "00 MIN"
2. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 MIN"
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗出廠預設值
- **reasoning_note**：（空）

### `NR1L-PowerManagement-160`

- **req_id**：SWE-PM-059
- **tc_id**：NR1L-PowerManagement-160
- **tc_title**：A network sleep request in Standby passes the TLM to Sleep
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A network sleep request in Standby passes the TLM to Sleep
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
3. The boot of the TLM has been completed
```
- **input_test_data**：A Network Sleep request
- **test_procedure**：

```
1. Send the request listed in Input Test Data
2. Read the TLM state and the shutdown counter to check the resulting behavior
```
- **expected_result**：

```
1. TLM_Status.Info and $Telematic_Power$ read "Sleep" and the TLM passes to Sleep state
2. Shutdown_Time starts
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 boot 已完成之分支
- **reasoning_note**：（空）

---

## 段 17 —— 161 ~ 168（8 條）

### `NR1L-PowerManagement-161`

- **req_id**：SWE-PM-059
- **tc_id**：NR1L-PowerManagement-161
- **tc_title**：A network sleep request during boot is served only after the boot ends
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A network sleep request during boot is served only after the boot ends
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info and $Telematic_Power$ read "Standby"
3. The boot of the TLM is not ended
```
- **input_test_data**：A Network Sleep request
- **test_procedure**：

```
1. Send the request listed in Input Test Data
2. Read the TLM state and the shutdown counter at the end of the boot to check the wait
```
- **expected_result**：

```
1. The TLM waits for the end of the boot before passing to Sleep state
2. Shutdown_Time starts only after the end of the boot
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.15
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 boot 未結束之等待分支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-162`

- **req_id**：SWE-PM-066
- **tc_id**：NR1L-PowerManagement-162
- **tc_title**：An SOS call is treated as a phone call becoming active
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：An SOS call is treated as a phone call becoming active
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in a state that reacts to a phone call becoming active
```
- **input_test_data**：An SOS call is placed
- **test_procedure**：

```
1. Place the call listed in Input Test Data
2. Read the HU reaction to check that it treats the call as a phone call
```
- **expected_result**：

```
1. The HU registers the call
2. The HU behaves as for a Phone call becoming active
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 SOS call
- **reasoning_note**：（空）

### `NR1L-PowerManagement-163`

- **req_id**：SWE-PM-066
- **tc_id**：NR1L-PowerManagement-163
- **tc_title**：An Assist call is treated as a phone call becoming active
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：An Assist call is treated as a phone call becoming active
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in a state that reacts to a phone call becoming active
```
- **input_test_data**：An Assist call is placed
- **test_procedure**：

```
1. Place the call listed in Input Test Data
2. Read the HU reaction to check that it treats the call as a phone call
```
- **expected_result**：

```
1. The HU registers the call
2. The HU behaves as for a Phone call becoming active
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Assist call
- **reasoning_note**：（空）

### `NR1L-PowerManagement-164`

- **req_id**：SWE-PM-067
- **tc_id**：NR1L-PowerManagement-164
- **tc_title**：A projection device call is treated as a phone call becoming active
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A projection device call is treated as a phone call becoming active
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. A projection device is paired on the bench
```
- **input_test_data**：A Projection device call is placed
- **test_procedure**：

```
1. Place the call listed in Input Test Data
2. Read the HU reaction to check that it treats the call as a phone call
```
- **expected_result**：

```
1. The HU registers the call
2. The HU behaves as for a Phone call becoming active
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Projection device call
- **reasoning_note**：（空）

### `NR1L-PowerManagement-165`

- **req_id**：SWE-PM-068
- **tc_id**：NR1L-PowerManagement-165
- **tc_title**：An incoming call from IDLE bypasses the disclaimer screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：An incoming call from IDLE bypasses the disclaimer screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The disclaimer screen has not yet been shown
```
- **input_test_data**：An incoming phone call
- **test_procedure**：

```
1. Let the bench place the call listed in Input Test Data
2. Read the HU mode and the screen to check whether the disclaimer appears
```
- **expected_result**：

```
1. The HU transitions from IDLE to FULL OPERATION
2. The disclaimer screen is bypassed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗來電所致之 IDLE → FULL OPERATION 免顯免責畫面
- **reasoning_note**：（空）

### `NR1L-PowerManagement-166`

- **req_id**：SWE-PM-069
- **tc_id**：NR1L-PowerManagement-166
- **tc_title**：The HU returns to IDLE when the call ends on the phone main screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The HU returns to IDLE when the call ends on the phone main screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone main screen
```
- **input_test_data**：An incoming phone call that then becomes inactive
- **test_procedure**：

```
1. Let the bench place and then end the call listed in Input Test Data
2. Read the HU mode to check the transition after the call ends
```
- **expected_result**：

```
1. The HU transitions from IDLE to FULL OPERATION for the call
2. The HU transitions back to IDLE
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 phone main screen
- **reasoning_note**：（空）

### `NR1L-PowerManagement-167`

- **req_id**：SWE-PM-069
- **tc_id**：NR1L-PowerManagement-167
- **tc_title**：The HU returns to IDLE when the call ends on the phone projection call UI
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The HU returns to IDLE when the call ends on the phone projection call UI
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The display is on the phone projection call UI
```
- **input_test_data**：An incoming phone call that then becomes inactive
- **test_procedure**：

```
1. Let the bench place and then end the call listed in Input Test Data
2. Read the HU mode to check the transition after the call ends
```
- **expected_result**：

```
1. The HU transitions from IDLE to FULL OPERATION for the call
2. The HU transitions back to IDLE
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 phone projection call UI
- **reasoning_note**：（空）

### `NR1L-PowerManagement-168`

- **req_id**：SWE-PM-070
- **tc_id**：NR1L-PowerManagement-168
- **tc_title**：The bypassed disclaimer is shown at the next transition to FULL OPERATION
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The bypassed disclaimer is shown at the next transition to FULL OPERATION
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The disclaimer has not yet been shown
```
- **input_test_data**：An incoming phone call that then becomes inactive
- **test_procedure**：

```
1. Let the bench place and then end the call listed in Input Test Data
2. Bring the HU to FULL OPERATION again and read the screen to check the disclaimer
```
- **expected_result**：

```
1. The HU bypasses the disclaimer for the call and returns to IDLE
2. The disclaimer is shown at the next transition to FULL OPERATION
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗免責畫面之延後補顯
- **reasoning_note**：（空）

---

## 段 18 —— 169 ~ 176（8 條）

### `NR1L-PowerManagement-169`

- **req_id**：SWE-PM-074
- **tc_id**：NR1L-PowerManagement-169
- **tc_title**：A Radio FOTA update at Body OFF brings the HU to Timed for the pop-up
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A Radio FOTA update at Body OFF brings the HU to Timed for the pop-up
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU transitions to Standby mode as the vehicle enters Body OFF mode
```
- **input_test_data**：A FOTA update available for the Radio
- **test_procedure**：

```
1. Make available the update listed in Input Test Data
2. Read the HU mode and the screen to check the resulting presentation
```
- **expected_result**：

```
1. The HU transitions to Timed mode
2. The FOTA update available pop-up is displayed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.10
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之 Radio 支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-170`

- **req_id**：SWE-PM-074
- **tc_id**：NR1L-PowerManagement-170
- **tc_title**：A TBM FOTA update at Body OFF brings the HU to Timed for the pop-up
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A TBM FOTA update at Body OFF brings the HU to Timed for the pop-up
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU transitions to Standby mode as the vehicle enters Body OFF mode
```
- **input_test_data**：A FOTA update available for the TBM
- **test_procedure**：

```
1. Make available the update listed in Input Test Data
2. Read the HU mode and the screen to check the resulting presentation
```
- **expected_result**：

```
1. The HU transitions to Timed mode
2. The FOTA update available pop-up is displayed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.10
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之 TBM 支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-171`

- **req_id**：SWE-PM-074
- **tc_id**：NR1L-PowerManagement-171
- **tc_title**：A ROV FOTA update at Body OFF brings the HU to Timed for the pop-up
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A ROV FOTA update at Body OFF brings the HU to Timed for the pop-up
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU transitions to Standby mode as the vehicle enters Body OFF mode
```
- **input_test_data**：A FOTA update available for the ROV
- **test_procedure**：

```
1. Make available the update listed in Input Test Data
2. Read the HU mode and the screen to check the resulting presentation
```
- **expected_result**：

```
1. The HU transitions to Timed mode
2. The FOTA update available pop-up is displayed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.10
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之 ROV 支
- **reasoning_note**：（空）

### `NR1L-PowerManagement-172`

- **req_id**：SWE-PM-075
- **tc_id**：NR1L-PowerManagement-172
- **tc_title**：The HU leaves Timed one minute after the FOTA pop-up is left untouched
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The HU leaves Timed one minute after the FOTA pop-up is left untouched
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in Timed mode due to the condition described in CFTS009-1809
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Leave the FOTA pop-up without any user interaction
2. Read the HU mode after the idle period to check the transition
```
- **expected_result**：

```
1. The pop-up stays on the screen while no interaction occurs
2. The HU transitions to Standby mode after 1 minute has passed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.10
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗條件一 —— 1 分鐘無互動
- **reasoning_note**：（空）

### `NR1L-PowerManagement-173`

- **req_id**：SWE-PM-075
- **tc_id**：NR1L-PowerManagement-173
- **tc_title**：The HU leaves Timed when the FOTA pop-up is dismissed
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The HU leaves Timed when the FOTA pop-up is dismissed
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in Timed mode due to the condition described in CFTS009-1809
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Dismiss the FOTA pop-up on the screen
2. Read the HU mode to check the transition after the dismissal
```
- **expected_result**：

```
1. The FOTA pop up is dismissed
2. The HU transitions to Standby mode
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.10
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗條件二 —— pop-up 被關閉
- **reasoning_note**：（空）

### `NR1L-PowerManagement-174`

- **req_id**：SWE-PM-075
- **tc_id**：NR1L-PowerManagement-174
- **tc_title**：The HU leaves Timed when the accessory delay becomes inactive
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The HU leaves Timed when the accessory delay becomes inactive
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in Timed mode due to the condition described in CFTS009-1809
```
- **input_test_data**：$ACCDlyAct$: active to inactive
- **test_procedure**：

```
1. Send the transition listed in Input Test Data
2. Read the HU mode to check the transition that follows
```
- **expected_result**：

```
1. The HU registers the transition without a bus error
2. The HU transitions to Standby mode
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.10
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗條件三 —— $ACCDlyAct$ 轉為 inactive
- **reasoning_note**：（空）

### `NR1L-PowerManagement-175`

- **req_id**：SWE-PM-076
- **tc_id**：NR1L-PowerManagement-175
- **tc_title**：A ten second power button press performs a radio reset and saves logs
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：A ten second power button press performs a radio reset and saves logs
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is not installing a firmware image
```
- **input_test_data**：$ICSPowerButton$: Pressed for 10 seconds consecutively
- **test_procedure**：

```
1. Send the input listed in Input Test Data
2. Read the HU behavior and the stored logs to check the reset
```
- **expected_result**：

```
1. The HU performs a radio reset
2. The HU collects and saves logs at the time of the reset
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.3
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗重置本身與 log 保存
- **reasoning_note**：（空）

### `NR1L-PowerManagement-176`

- **req_id**：SWE-PM-076
- **tc_id**：NR1L-PowerManagement-176
- **tc_title**：The power button reset covers both the main CPU and the CAN micro
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The power button reset covers both the main CPU and the CAN micro
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is not installing a firmware image
```
- **input_test_data**：$ICSPowerButton$: Pressed for 10 seconds consecutively
- **test_procedure**：

```
1. Send the input listed in Input Test Data
2. Read both processors to check what the reset covers
```
- **expected_result**：

```
1. The main CPU resets at the time of the reset
2. The CAN micro resets at the time of the reset
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.3
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗重置範圍涵蓋二個處理器
- **reasoning_note**：（空）

---

## 段 19 —— 178 ~ 185（8 條）

### `NR1L-PowerManagement-178`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-178
- **tc_title**：Closing the driver door in SLEEP MODE plays the start-up animation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：Closing the driver door in SLEEP MODE plays the start-up animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in SLEEP MODE
3. A driver door is present for the vehicle
```
- **input_test_data**：$Door_Ajar_Status$: changed to CLOSED
- **test_procedure**：

```
1. Send the change listed in Input Test Data
2. Read the screen to check the start-up animation defined per HMI
```
- **expected_result**：

```
1. The HU registers the change without a bus error
2. The HU plays a start-up animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之 SLEEP MODE 支
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

### `NR1L-PowerManagement-179`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-179
- **tc_title**：Closing the driver door in STANDBY MODE plays the start-up animation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：Closing the driver door in STANDBY MODE plays the start-up animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in STANDBY MODE
3. A driver door is present for the vehicle
```
- **input_test_data**：$Door_Ajar_Status$: changed to CLOSED
- **test_procedure**：

```
1. Send the change listed in Input Test Data
2. Read the screen to check the start-up animation defined per HMI
```
- **expected_result**：

```
1. The HU registers the change without a bus error
2. The HU plays a start-up animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之 STANDBY MODE 支
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

### `NR1L-PowerManagement-180`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-180
- **tc_title**：Closing the driver door in PARTIAL OPERATION MODE plays the start-up animation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：Closing the driver door in PARTIAL OPERATION MODE plays the start-up animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in PARTIAL OPERATION MODE
3. A driver door is present for the vehicle
```
- **input_test_data**：$Door_Ajar_Status$: changed to CLOSED
- **test_procedure**：

```
1. Send the change listed in Input Test Data
2. Read the screen to check the start-up animation defined per HMI
```
- **expected_result**：

```
1. The HU registers the change without a bus error
2. The HU plays a start-up animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之 PARTIAL OPERATION MODE 支
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

### `NR1L-PowerManagement-181`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-181
- **tc_title**：A removed driver door makes the HU skip the start-up animation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A removed driver door makes the HU skip the start-up animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in STANDBY MODE
```
- **input_test_data**：$DriverDoorOnOffSts$: "DOOR_OFF"
- **test_procedure**：

```
1. Send the value listed in Input Test Data and close the driver door
2. Read the screen to check whether an animation is played
```
- **expected_result**：

```
1. The HU registers the value without a bus error
2. The HU skips the start-up animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 $DriverDoorOnOffSts$ 之略過分支
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

### `NR1L-PowerManagement-182`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-182
- **tc_title**：A mode change cancels a start-up animation in progress
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A mode change cancels a start-up animation in progress
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is playing a start-up animation
```
- **input_test_data**：An ignition event that changes the HU power mode to BODY ON
- **test_procedure**：

```
1. Send the event listed in Input Test Data during the animation
2. Read the screen and the power mode to check the cancellation
```
- **expected_result**：

```
1. The HU cancels the current start-up animation
2. The HU switches to the required power mode as defined
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗播放中之模式變更取消
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

### `NR1L-PowerManagement-183`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-183
- **tc_title**：An ignition crank event cancels a start-up animation in progress
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：An ignition crank event cancels a start-up animation in progress
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is playing a start-up animation
```
- **input_test_data**：$PowerMode$: "IGN_START"
- **test_procedure**：

```
1. Send the value listed in Input Test Data during the animation
2. Read the screen and the power mode to check the cancellation
```
- **expected_result**：

```
1. The HU cancels the current start-up animation
2. The HU switches to the required power mode as defined
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 IGN_START 取消
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

### `NR1L-PowerManagement-184`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-184
- **tc_title**：A mode change to TIMED MODE cancels a start-up animation in progress
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A mode change to TIMED MODE cancels a start-up animation in progress
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is playing a start-up animation
```
- **input_test_data**：An HU power mode status change to TIMED MODE
- **test_procedure**：

```
1. Send the change listed in Input Test Data during the animation
2. Read the screen and the power mode to check the cancellation
```
- **expected_result**：

```
1. The HU cancels the current start-up animation
2. The HU switches to the required power mode as defined
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之 TIMED MODE 支（R-P118(d) 反向涵蓋裁決補測）
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

### `NR1L-PowerManagement-185`

- **req_id**：SWE-PM-093
- **tc_id**：NR1L-PowerManagement-185
- **tc_title**：An open driver door makes the HU skip the animation on a mode change
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：An open driver door makes the HU skip the animation on a mode change
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in STANDBY MODE
3. $Door_Ajar_Status$ reads OPEN
```
- **input_test_data**：An HU power mode status change to BODY ON
- **test_procedure**：

```
1. Send the change listed in Input Test Data
2. Read the screen to check whether an animation is played
```
- **expected_result**：

```
1. The HU switches to the required power mode
2. The HU skips the start-up animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.3.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗門開啟時之模式變更略過（R-P118(d) 反向涵蓋裁決補測）
- **reasoning_note**：**本 leaf 之二錨點（`4941301` §1.3.5 / `4941941` §1.9.8）內文逐字相同，而屬性相異五欄**（ECU / EE Architecture / Model Year / Radio / State）——為 R-P136 所定之「屬性相異 → 停並上繳」形態。二者之 ECU 皆含 `LTM`、Radio 皆涵蓋本專案，故適用性未變，TC 照常產出；**是否為變體登載，呈請裁定於 26 包**。

---

## 段 20 —— 187 ~ 197（8 條）

### `NR1L-PowerManagement-187`

- **req_id**：SWE-PM-094
- **tc_id**：NR1L-PowerManagement-187
- **tc_title**：The startup animation is displayed separately from the other startup screens
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The startup animation is displayed separately from the other startup screens
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in STANDBY MODE
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through a startup that plays the animation
2. Read the screen sequence to check how the animation is presented
```
- **expected_result**：

```
1. The startup animation is displayed
2. The startup animation is displayed separately from the Splash screen and disclaimer screen
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.8
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗三畫面之分離呈現
- **reasoning_note**：（空）

### `NR1L-PowerManagement-188`

- **req_id**：SWE-PM-095
- **tc_id**：NR1L-PowerManagement-188
- **tc_title**：Leaving the SNA value resumes the state diagram without a splash screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Leaving the SNA value resumes the state diagram without a splash screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. LTM_OperationalModeSts.Info reads "SNA"
```
- **input_test_data**：LTM_OperationalModeSts.Info: a value different from "SNA"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the TLM state and the screen to check the resumed behavior
```
- **expected_result**：

```
1. The TLM follows the state diagram using the updated value
2. The possible visualization of the splash screen is avoided
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.7.1.1.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗離開 SNA 之恢復行為
- **reasoning_note**：（空）

### `NR1L-PowerManagement-189`

- **req_id**：SWE-PM-097
- **tc_id**：NR1L-PowerManagement-189
- **tc_title**：The Fiat Latam startup animation selection replaces the vehicle brand logo
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The Fiat Latam startup animation selection replaces the vehicle brand logo
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU carries a configured vehicle brand
```
- **input_test_data**：DID "Startup Animation Selection": "Fiat Latam"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logo against the configured brand to check which logo appears
```
- **expected_result**：

```
1. The HU accepts the configuration value
2. The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Fiat Latam 之覆蓋規則
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-056` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-056` 承擔，**呈請裁定於 26 包**。

### `NR1L-PowerManagement-190`

- **req_id**：SWE-PM-098
- **tc_id**：NR1L-PowerManagement-190
- **tc_title**：The always setting plays a startup sound with the animation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The always setting plays a startup sound with the animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. $Themed_Sound$ reads "Fiat Latam"
3. The "Welcome Onboard Sound" setting reads "Always"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```
- **expected_result**：

```
1. The HU startup animation is played
2. A startup sound accompanies the animation and begins at the same time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.8
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Always 設定
- **reasoning_note**：（空）

### `NR1L-PowerManagement-191`

- **req_id**：SWE-PM-099
- **tc_id**：NR1L-PowerManagement-191
- **tc_title**：The once a day setting plays the startup sound on the first startup of the day
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The once a day setting plays the startup sound on the first startup of the day
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. $Themed_Sound$ reads "Fiat Latam"
3. The "Welcome Onboard Sound" setting reads "Once a Day"
4. The HU has not yet played the startup sound that day
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```
- **expected_result**：

```
1. The HU startup animation is played
2. A startup sound accompanies the animation and begins at the same time
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.8
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Once a Day 之當日首次
- **reasoning_note**：（空）

### `NR1L-PowerManagement-195`

- **req_id**：SWE-PM-100
- **tc_id**：NR1L-PowerManagement-195
- **tc_title**：The never setting plays no startup sound with the animation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The never setting plays no startup sound with the animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. $Themed_Sound$ reads "Fiat Latam"
3. The "Welcome Onboard Sound" setting reads "Never"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through a startup that plays the animation
2. Read the audio output against the animation start to check the accompaniment
```
- **expected_result**：

```
1. The HU startup animation is played
2. No startup sound accompanies the animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.8
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Never 設定
- **reasoning_note**：（空）

### `NR1L-PowerManagement-196`

- **req_id**：SWE-PM-101
- **tc_id**：NR1L-PowerManagement-196
- **tc_title**：No audio brand without SDARS shows the vehicle brand logo only
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：No audio brand without SDARS shows the vehicle brand logo only
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Absent"
```
- **input_test_data**：Audio_Brand: "No Audio Brand"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. The vehicle brand logo that depends on the Brand_Configuration_2 parameter value is shown alone
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合一（Absent ＋ No Audio Brand）
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-054` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-054` 承擔，**呈請裁定於 26 包**。

### `NR1L-PowerManagement-197`

- **req_id**：SWE-PM-101
- **tc_id**：NR1L-PowerManagement-197
- **tc_title**：Beats brand white without SDARS adds the Beats logo
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：Beats brand white without SDARS adds the Beats logo
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Absent"
```
- **input_test_data**：Audio_Brand: "Beats Brand White"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. The Beats Brand White logo is shown in addition to the vehicle brand logo
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合二（Absent ＋ Beats Brand White）
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-054` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-054` 承擔，**呈請裁定於 26 包**。

---

## 段 21 —— 198 ~ 207（8 條）

### `NR1L-PowerManagement-198`

- **req_id**：SWE-PM-101
- **tc_id**：NR1L-PowerManagement-198
- **tc_title**：SDARS present without audio brand adds the Sirius logo
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：SDARS present without audio brand adds the Sirius logo
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Present"
```
- **input_test_data**：Audio_Brand: "No Audio Brand"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. The Sirius logo is shown in addition to the vehicle brand logo
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合三（Present ＋ No Audio Brand）
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-054` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-054` 承擔，**呈請裁定於 26 包**。

### `NR1L-PowerManagement-199`

- **req_id**：SWE-PM-101
- **tc_id**：NR1L-PowerManagement-199
- **tc_title**：SDARS present with beats brand white adds both logos
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：SDARS present with beats brand white adds both logos
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Present"
```
- **input_test_data**：Audio_Brand: "Beats Brand White"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```
- **expected_result**：

```
1. The brand logo screen is presented
2. Both the Sirius and the Beats logos are shown in addition to the vehicle brand logo
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗組合四（Present ＋ Beats Brand White）
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-054` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-054` 承擔，**呈請裁定於 26 包**。

### `NR1L-PowerManagement-200`

- **req_id**：SWE-PM-102
- **tc_id**：NR1L-PowerManagement-200
- **tc_title**：The special package drives the Klipsch Splash Screen on the 2025 model year
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The special package drives the Klipsch Splash Screen on the 2025 model year
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The ETM carries $VC_MODEL_YEAR$ equal to "2025"
3. The ETM carries $VC_VEH_LINE$ equal to "DT"
```
- **input_test_data**：$VC_SpecialPKG_IC$: "Tungsten (147)"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown Splash Screen to check which screen the ETM displays
```
- **expected_result**：

```
1. The ETM accepts the configuration value
2. The Klipsch Splash Screen is displayed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.16
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 2025 年式之 $VC_SpecialPKG_IC$ 路徑
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-055` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-055` 承擔，**呈請裁定於 26 包**。

### `NR1L-PowerManagement-202`

- **req_id**：SWE-PM-103
- **tc_id**：NR1L-PowerManagement-202
- **tc_title**：Audio is off and only the Splash Screen is allowed in this status
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Audio is off and only the Splash Screen is allowed in this status
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition On working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM audio is OFF
2. Read the audio path and the display to check what is allowed
```
- **expected_result**：

```
1. The TLM audio is OFF
2. The TLM allows only Splash Screen visualization on its display
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗音訊關閉與畫面限制
- **reasoning_note**：（空）

### `NR1L-PowerManagement-203`

- **req_id**：SWE-PM-103
- **tc_id**：NR1L-PowerManagement-203
- **tc_title**：Audio is off and only the Splash Screen is allowed in Ignition Pre_Start
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Audio is off and only the Splash Screen is allowed in Ignition Pre_Start
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition Pre_Start working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM audio is OFF
2. Read the audio path and the display to check what is allowed
```
- **expected_result**：

```
1. The TLM audio is OFF
2. The TLM allows only Splash Screen visualization on its display
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗逗號列舉之點火工作條件 Ignition Pre_Start（R-P199 補測）
- **reasoning_note**：

```

**R-P207（28 包）**：本條所驗為**範圍主張** —— 規格列舉之該點火工作條件下該行為亦存在；**非驗其與他狀態間之行為差異**。故其 ER 與同組他條相同係屬正確，不得據此判為重複。
```

### `NR1L-PowerManagement-204`

- **req_id**：SWE-PM-103
- **tc_id**：NR1L-PowerManagement-204
- **tc_title**：Audio is off and only the Splash Screen is allowed in Ignition Start
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Audio is off and only the Splash Screen is allowed in Ignition Start
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition Start working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM audio is OFF
2. Read the audio path and the display to check what is allowed
```
- **expected_result**：

```
1. The TLM audio is OFF
2. The TLM allows only Splash Screen visualization on its display
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗逗號列舉之點火工作條件 Ignition Start（R-P199 補測）
- **reasoning_note**：

```

**R-P207（28 包）**：本條所驗為**範圍主張** —— 規格列舉之該點火工作條件下該行為亦存在；**非驗其與他狀態間之行為差異**。故其 ER 與同組他條相同係屬正確，不得據此判為重複。
```

### `NR1L-PowerManagement-205`

- **req_id**：SWE-PM-103
- **tc_id**：NR1L-PowerManagement-205
- **tc_title**：Audio is off and only the Splash Screen is allowed in Ignition Cranking
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：Audio is off and only the Splash Screen is allowed in Ignition Cranking
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition Cranking working condition
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the TLM to the status related to TLM audio is OFF
2. Read the audio path and the display to check what is allowed
```
- **expected_result**：

```
1. The TLM audio is OFF
2. The TLM allows only Splash Screen visualization on its display
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.2
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗逗號列舉之點火工作條件 Ignition Cranking（R-P199 補測）
- **reasoning_note**：

```

**R-P207（28 包）**：本條所驗為**範圍主張** —— 規格列舉之該點火工作條件下該行為亦存在；**非驗其與他狀態間之行為差異**。故其 ER 與同組他條相同係屬正確，不得據此判為重複。
```

### `NR1L-PowerManagement-207`

- **req_id**：SWE-PM-104
- **tc_id**：NR1L-PowerManagement-207
- **tc_title**：The splash and disclaimer screens appear on the first transition to Timed
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The splash and disclaimer screens appear on the first transition to Timed
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. A new bus cycle has started
3. Neither screen has been shown in this bus cycle
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU to Timed mode for the first time in the bus cycle
2. Read the screen sequence to check both startup screens
```
- **expected_result**：

```
1. The splash screen is shown
2. The disclaimer screen is shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗首次進入 Timed
- **reasoning_note**：（空）

---

## 段 22 —— 208 ~ 221（8 條）

### `NR1L-PowerManagement-208`

- **req_id**：SWE-PM-104
- **tc_id**：NR1L-PowerManagement-208
- **tc_title**：The splash and disclaimer screens appear on the first transition to Full Operation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The splash and disclaimer screens appear on the first transition to Full Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. A new bus cycle has started
3. Neither screen has been shown in this bus cycle
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU to Full Operation mode for the first time in the bus cycle
2. Read the screen sequence to check both startup screens
```
- **expected_result**：

```
1. The splash screen is shown
2. The disclaimer screen is shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗首次進入 Full Operation
- **reasoning_note**：（空）

### `NR1L-PowerManagement-209`

- **req_id**：SWE-PM-104
- **tc_id**：NR1L-PowerManagement-209
- **tc_title**：The disclaimer appears on the first transition from Idle
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The disclaimer appears on the first transition from Idle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in Idle mode
3. The disclaimer needs to be shown
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU from Idle to Timed mode for the first time in the bus cycle
2. Read the screen to check the disclaimer presentation
```
- **expected_result**：

```
1. The HU reaches Timed mode
2. The disclaimer screen is shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗來源狀態 Idle
- **reasoning_note**：（空）

### `NR1L-PowerManagement-210`

- **req_id**：SWE-PM-104
- **tc_id**：NR1L-PowerManagement-210
- **tc_title**：The disclaimer appears on the first transition from Standby
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The disclaimer appears on the first transition from Standby
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in Standby mode
3. The disclaimer needs to be shown
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU from Standby to Timed mode for the first time in the bus cycle
2. Read the screen to check the disclaimer presentation
```
- **expected_result**：

```
1. The HU reaches Timed mode
2. The disclaimer screen is shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗來源狀態 Standby
- **reasoning_note**：（空）

### `NR1L-PowerManagement-211`

- **req_id**：SWE-PM-104
- **tc_id**：NR1L-PowerManagement-211
- **tc_title**：The disclaimer appears on the first transition from Partial Operation
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The disclaimer appears on the first transition from Partial Operation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in Partial Operation mode
3. The disclaimer needs to be shown
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU from Partial Operation to Full Operation for the first time
2. Read the screen to check the disclaimer presentation
```
- **expected_result**：

```
1. The HU reaches Full Operation mode
2. The disclaimer screen is shown
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗來源狀態 Partial Operation
- **reasoning_note**：（空）

### `NR1L-PowerManagement-212`

- **req_id**：SWE-PM-105
- **tc_id**：NR1L-PowerManagement-212
- **tc_title**：An ongoing call temporarily skips the disclaimer and splash screens
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：An ongoing call temporarily skips the disclaimer and splash screens
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. A new bus cycle has started
```
- **input_test_data**：An ongoing call at the moment of the transition
- **test_procedure**：

```
1. Bring the HU to Timed mode while the event listed in Input Test Data holds
2. Read the screen to check whether the startup screens appear
```
- **expected_result**：

```
1. The HU reaches Timed mode
2. The disclaimer and splash screen are temporarily skipped
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗通話類之暫時略過
- **reasoning_note**：（空）

### `NR1L-PowerManagement-219`

- **req_id**：SWE-PM-105
- **tc_id**：NR1L-PowerManagement-219
- **tc_title**：The skipped screens are displayed at the next transition in the bus cycle
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The skipped screens are displayed at the next transition in the bus cycle
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The startup screens were skipped earlier in this bus cycle
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU to Full Operation mode again within the same bus cycle
2. Read the screen to check the deferred presentation
```
- **expected_result**：

```
1. The HU reaches Full Operation mode
2. The skipped screens are displayed at this transition
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗延後補顯之義務
- **reasoning_note**：（空）

### `NR1L-PowerManagement-220`

- **req_id**：SWE-PM-106
- **tc_id**：NR1L-PowerManagement-220
- **tc_title**：The SOS button variant selects the SOS disclaimer text
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The SOS button variant selects the SOS disclaimer text
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is configured for a disclaimer screen variation
```
- **input_test_data**：$Ecall_Button_Variant$: "SOS"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the disclaimer wording to check which text the HU uses
```
- **expected_result**：

```
1. The HU accepts the configuration value
2. The HU uses the SOS text for the disclaimer
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 SOS 變體
- **reasoning_note**：（空）

### `NR1L-PowerManagement-221`

- **req_id**：SWE-PM-107
- **tc_id**：NR1L-PowerManagement-221
- **tc_title**：The help button variant replaces the SOS text in the disclaimer
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：The help button variant replaces the SOS text in the disclaimer
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is configured for a disclaimer screen variation
```
- **input_test_data**：$Ecall_Button_Variant$: "Help"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the disclaimer wording to check which text the HU uses
```
- **expected_result**：

```
1. The HU accepts the configuration value
2. The HU replaces the "SOS" text with the "Help" version of the disclaimer
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Help 變體
- **reasoning_note**：（空）

---

## 段 23 —— 222 ~ 230（8 條）

### `NR1L-PowerManagement-222`

- **req_id**：SWE-PM-108
- **tc_id**：NR1L-PowerManagement-222
- **tc_title**：A non Maserati brand shows the core disclaimer once every thirty ignition cycles
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A non Maserati brand shows the core disclaimer once every thirty ignition cycles
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. $VC_VEH_BRAND$ reads a value other than "Maserati"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Run the head unit through consecutive ignition cycles
2. Read the screen across the cycles to check how often the disclaimer appears
```
- **expected_result**：

```
1. The core disclaimer screen is shown on the first ignition cycle
2. The core disclaimer screen is shown only once every 30 ignition cycles
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗免責畫面之顯示頻率
- **reasoning_note**：（空）

### `NR1L-PowerManagement-223`

- **req_id**：SWE-PM-109
- **tc_id**：NR1L-PowerManagement-223
- **tc_title**：A GDPR market with the TBM present follows the GDPR non Maserati startup flow
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A GDPR market with the TBM present follows the GDPR non Maserati startup flow
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. $VC_VEH_BRAND$ reads a value other than "Maserati"
3. $TBM_Present$ reads "Present"
4. $Country_Code$ is marked as a country needing the combined Geolocation plus SOS Popup
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through the startup sequence
2. Read the startup flow against the HMI to check which flow is followed
```
- **expected_result**：

```
1. The HU reaches the startup presentation
2. The HU follows the GDPR Non-Maserati startup flow in the HMI
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 GDPR 流程
- **reasoning_note**：（空）

### `NR1L-PowerManagement-224`

- **req_id**：SWE-PM-110
- **tc_id**：NR1L-PowerManagement-224
- **tc_title**：A missing TBM follows the non GDPR non Maserati startup flow
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A missing TBM follows the non GDPR non Maserati startup flow
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. $VC_VEH_BRAND$ reads a value other than "Maserati"
3. $TBM_Present$ reads "Not Present"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through the startup sequence
2. Read the startup flow against the HMI to check which flow is followed
```
- **expected_result**：

```
1. The HU reaches the startup presentation
2. The HU follows the Non-GDPR/Non-Maserati Startup flow in the HMI
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 TBM Not Present
- **reasoning_note**：（空）

### `NR1L-PowerManagement-225`

- **req_id**：SWE-PM-110
- **tc_id**：NR1L-PowerManagement-225
- **tc_title**：An unmarked country follows the non GDPR non Maserati startup flow
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：An unmarked country follows the non GDPR non Maserati startup flow
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. $VC_VEH_BRAND$ reads a value other than "Maserati"
3. $TBM_Present$ reads "Present"
4. $Country_Code$ is not marked as one of the "Countries which need the combined Geolocation plus SOS Popup" in the Market Configuration Table
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through the startup sequence
2. Read the startup flow against the HMI to check which flow is followed
```
- **expected_result**：

```
1. The HU reaches the startup presentation
2. The HU follows the Non-GDPR/Non-Maserati Startup flow in the HMI
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 country 未標記
- **reasoning_note**：（空）

### `NR1L-PowerManagement-226`

- **req_id**：SWE-PM-111
- **tc_id**：NR1L-PowerManagement-226
- **tc_title**：A missing TBM adds the ADAS text to the disclaimer
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A missing TBM adds the ADAS text to the disclaimer
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The screen size is other than 7 inch
3. $VC_VEH_BRAND$ reads a value other than "Maserati"
4. $TBM_Present$ reads "Not Present"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU to the disclaimer presentation
2. Read the disclaimer wording to check the added text
```
- **expected_result**：

```
1. The disclaimer screen is shown
2. The HU adds the ADAS text to the disclaimer
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 TBM Not Present
- **reasoning_note**：（空）

### `NR1L-PowerManagement-228`

- **req_id**：SWE-PM-113
- **tc_id**：NR1L-PowerManagement-228
- **tc_title**：A geolocation and SOS market adds the ADAS and SOS text
- **test_group**：Power Management
- **test_set**：Startup Display
- **test_item**：A geolocation and SOS market adds the ADAS and SOS text
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The screen size is other than 7 inch
3. $VC_VEH_BRAND$ reads a value other than "Maserati"
4. $TBM_Present$ reads "Present"
5. $Country_Code$ requires geolocation and SOS in the disclaimer
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU to the disclaimer presentation
2. Read the shown wording to check what the HU adds
```
- **expected_result**：

```
1. The geolocation pop-up or the disclaimer is shown
2. The HU adds the ADAS and SOS to the geolocation pop-up or disclaimer
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.9
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 geolocation ＋ SOS 之附加
- **reasoning_note**：（空）

### `NR1L-PowerManagement-229`

- **req_id**：SWE-PM-114
- **tc_id**：NR1L-PowerManagement-229
- **tc_title**：An incoming call from IDLE bypasses the not yet shown disclaimer screen
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：An incoming call from IDLE bypasses the not yet shown disclaimer screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The disclaimer screen has not yet been shown
```
- **input_test_data**：An incoming phone call
- **test_procedure**：

```
1. Let the bench place the call listed in Input Test Data
2. Read the HU mode and the screen to check whether the disclaimer appears
```
- **expected_result**：

```
1. The HU transitions from IDLE to FULL OPERATION
2. The disclaimer screen is bypassed
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗來電所致之 IDLE → FULL OPERATION 免顯免責畫面
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-068` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-068` 承擔，**呈請裁定於 26 包**。

### `NR1L-PowerManagement-230`

- **req_id**：SWE-PM-115
- **tc_id**：NR1L-PowerManagement-230
- **tc_title**：The disclaimer bypassed for a call is shown at the next FULL OPERATION
- **test_group**：Power Management
- **test_set**：Power State
- **test_item**：The disclaimer bypassed for a call is shown at the next FULL OPERATION
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is in IDLE mode
3. The disclaimer has not yet been shown
```
- **input_test_data**：An incoming phone call that then becomes inactive
- **test_procedure**：

```
1. Let the bench place and then end the call listed in Input Test Data
2. Bring the HU to FULL OPERATION again and read the screen to check the disclaimer
```
- **expected_result**：

```
1. The HU bypasses the disclaimer for the call and returns to IDLE
2. The disclaimer is shown at the next transition to FULL OPERATION
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗免責畫面之延後補顯
- **reasoning_note**：**本 leaf 之 `source_anchor` 與 `SWE-PM-070` 完全相同**，`source_clause` 逐字一致。執行層**未合併、未省略**，依 037 之 leaf 母體逐一產出以維持追溯；是否應改依 §8.2.1 委由 `SWE-PM-070` 承擔，**呈請裁定於 26 包**。

---

## 段 24 —— 231 ~ 240（8 條）

### `NR1L-PowerManagement-231`

- **req_id**：SWE-PM-077
- **tc_id**：NR1L-PowerManagement-231
- **tc_title**：The special package value determines the theme used by the HU
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The special package value determines the theme used by the HU
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU carries a supported special package configuration
```
- **input_test_data**：$VC_SpecialPKG$: a value defined in the PDO Theme Configuration
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the applied theme against the configured value to check the source
```
- **expected_result**：

```
1. The HU accepts the configuration value
2. The theme used by the HU is the one associated with $VC_SpecialPKG$
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 $VC_SpecialPKG$ 決定主題
- **reasoning_note**：（空）

### `NR1L-PowerManagement-232`

- **req_id**：SWE-PM-078
- **tc_id**：NR1L-PowerManagement-232
- **tc_title**：A none special package falls back to the brand default theme
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：A none special package falls back to the brand default theme
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU carries a configured vehicle brand
```
- **input_test_data**：$VC_SpecialPKG$: "none"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the applied theme against the brand signal to check the fallback
```
- **expected_result**：

```
1. The HU accepts the configuration value
2. The default theme based on the $VC_VEH_BRAND$ signal is used
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之左支 none
- **reasoning_note**：（空）

### `NR1L-PowerManagement-233`

- **req_id**：SWE-PM-078
- **tc_id**：NR1L-PowerManagement-233
- **tc_title**：An unsupported special package falls back to the brand default theme
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：An unsupported special package falls back to the brand default theme
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU carries a configured vehicle brand
```
- **input_test_data**：$VC_SpecialPKG$: a value that is not supported by the HU
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the applied theme against the brand signal to check the fallback
```
- **expected_result**：

```
1. The HU accepts the configuration value
2. The default theme based on the $VC_VEH_BRAND$ signal is used
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 OR 之右支 不受支援之值
- **reasoning_note**：（空）

### `NR1L-PowerManagement-234`

- **req_id**：SWE-PM-079
- **tc_id**：NR1L-PowerManagement-234
- **tc_title**：An unsupported CAN value on a branded element uses the PDO default
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：An unsupported CAN value on a branded element uses the PDO default
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU displays a PDO branded element
```
- **input_test_data**：A referenced CAN signal carrying a value that is not supported by the HU
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown element to check which value the HU falls back to
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The default value defined by PDO is used for that branded element
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗品牌化元素之回落規則
- **reasoning_note**：（空）

### `NR1L-PowerManagement-235`

- **req_id**：SWE-PM-080
- **tc_id**：NR1L-PowerManagement-235
- **tc_title**：The theme special package value is sent while the CAN network is awake
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The theme special package value is sent while the CAN network is awake
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The CAN network is awake
3. A theme is applied on the HU
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Observe the bus traffic while the CAN network stays awake
2. Read $Radio_Theme$ against the applied theme to check the sent value
```
- **expected_result**：

```
1. The HU sends $Radio_Theme$ on the bus
2. The value sent in $Radio_Theme$ is the special package value associated with that theme
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗喚醒時之送值
- **reasoning_note**：（空）

### `NR1L-PowerManagement-237`

- **req_id**：SWE-PM-081
- **tc_id**：NR1L-PowerManagement-237
- **tc_title**：The Chrysler brand selects the Chrysler font
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The Chrysler brand selects the Chrysler font
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is displaying branded text
```
- **input_test_data**：$VC_VEH_BRAND$: "Chrysler"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the displayed font to check which font the HU selects
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU displays the Chrysler font
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗一般品牌值之映射
- **reasoning_note**：（空）

### `NR1L-PowerManagement-238`

- **req_id**：SWE-PM-081
- **tc_id**：NR1L-PowerManagement-238
- **tc_title**：The Jeep brand selects the Jeep font
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The Jeep brand selects the Jeep font
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is displaying branded text
```
- **input_test_data**：$VC_VEH_BRAND$: "Jeep"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the displayed font to check which font the HU selects
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU displays the Jeep font
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.1
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Jeep 值之映射（與 R-P193 之品牌適用性相關）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-240`

- **req_id**：SWE-PM-082
- **tc_id**：NR1L-PowerManagement-240
- **tc_title**：The Chrysler brand selects the Chrysler App icon
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The Chrysler brand selects the Chrysler App icon
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is displaying the App icon
```
- **input_test_data**：$VC_VEH_BRAND$: "Chrysler"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the displayed App icon to check which icon the HU selects
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU displays the Chrysler App icon
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗一般品牌值之映射
- **reasoning_note**：（空）

---

## 段 25 —— 241 ~ 253（8 條）

### `NR1L-PowerManagement-241`

- **req_id**：SWE-PM-082
- **tc_id**：NR1L-PowerManagement-241
- **tc_title**：The Jeep brand selects the Jeep App icon
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The Jeep brand selects the Jeep App icon
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU is displaying the App icon
```
- **input_test_data**：$VC_VEH_BRAND$: "Jeep"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the displayed App icon to check which icon the HU selects
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU displays the Jeep App icon
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.4
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Jeep 值之映射
- **reasoning_note**：（空）

### `NR1L-PowerManagement-243`

- **req_id**：SWE-PM-083
- **tc_id**：NR1L-PowerManagement-243
- **tc_title**：The Jeep brand offers the Jeep avatars in the profile screen
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The Jeep brand offers the Jeep avatars in the profile screen
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The profile screen is reachable on the HU
```
- **input_test_data**：$VC_VEH_BRAND$: "Jeep"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the avatar list in the profile screen to check which set is offered
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The profile screen offers the Jeep avatars
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗自有 avatar 之品牌值
- **reasoning_note**：（空）

### `NR1L-PowerManagement-245`

- **req_id**：SWE-PM-083
- **tc_id**：NR1L-PowerManagement-245
- **tc_title**：The Abarth brand is mapped to the Fiat avatars
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The Abarth brand is mapped to the Fiat avatars
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The profile screen is reachable on the HU
```
- **input_test_data**：$VC_VEH_BRAND$: "Abarth"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the avatar list in the profile screen to check which set is offered
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The profile screen offers the Fiat avatars rather than an Abarth set
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.5
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗映射至他品牌 avatar 之規則（本 leaf 獨有）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-246`

- **req_id**：SWE-PM-084
- **tc_id**：NR1L-PowerManagement-246
- **tc_title**：The recirc icon follows the PROXI parameters on the Atlantis architecture
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The recirc icon follows the PROXI parameters on the Atlantis architecture
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU runs the CUSW or Atlantis architecture
3. The climate screen showing the recirc icon is reachable
```
- **input_test_data**：$VC_VEH_LINE$ with the $Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters
- **test_procedure**：

```
1. Send the configuration listed in Input Test Data
2. Read the shown recirc icon to check which assignment the HU applies
```
- **expected_result**：

```
1. The HU accepts the configuration
2. The recirc icon matches the assignment for that vehicle line and car shape
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.6
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CUSW / Atlantis 路徑（本專案適用）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-248`

- **req_id**：SWE-PM-085
- **tc_id**：NR1L-PowerManagement-248
- **tc_title**：The settings seat graphic follows the PROXI parameters on the Atlantis architecture
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The settings seat graphic follows the PROXI parameters on the Atlantis architecture
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU runs the CUSW or Atlantis architecture
3. The seat settings screen is reachable
```
- **input_test_data**：$VC_VEH_LINE$ with the $Car_Shape_Configuration$ and $Number_of_Doors$ PROXI parameters
- **test_procedure**：

```
1. Send the configuration listed in Input Test Data
2. Read the shown seat graphic to check which assignment the HU applies
```
- **expected_result**：

```
1. The HU accepts the configuration
2. The settings seat graphic matches the assignment for that vehicle line and car shape
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.7
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 CUSW / Atlantis 路徑（本專案適用）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-250`

- **req_id**：SWE-PM-086
- **tc_id**：NR1L-PowerManagement-250
- **tc_title**：The theme special package value is sent on this chapter while the network is awake
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The theme special package value is sent on this chapter while the network is awake
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The CAN network is awake
3. A theme is applied on the HU
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Observe the bus traffic while the CAN network stays awake
2. Read $Radio_Theme$ against the applied theme to check the sent value
```
- **expected_result**：

```
1. The HU sends $Radio_Theme$ on the bus
2. The value sent in $Radio_Theme$ is the special package value associated with that theme
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.7.1.1
- **priority**：P1
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗喚醒時之送值（與 SWE-PM-080 重疊，見 reasoning）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-252`

- **req_id**：SWE-PM-087
- **tc_id**：NR1L-PowerManagement-252
- **tc_title**：The M240 vehicle line uses the M240 seat graphics
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The M240 vehicle line uses the M240 seat graphics
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The seat settings screen is reachable
```
- **input_test_data**：$VC_VEH_LINE$: "M240"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown seat graphic to check which set the HU uses
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU uses the M240 seat graphics
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.7.1.1.6
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 IF 分支 M240
- **reasoning_note**：（空）

### `NR1L-PowerManagement-253`

- **req_id**：SWE-PM-087
- **tc_id**：NR1L-PowerManagement-253
- **tc_title**：A non M240 vehicle line falls back to the brand seat graphic
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：A non M240 vehicle line falls back to the brand seat graphic
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The seat settings screen is reachable
3. The HU carries a configured vehicle brand
```
- **input_test_data**：$VC_VEH_LINE$: a value other than "M240"
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown seat graphic against the brand signal to check the source
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU uses $VC_VEH_BRAND$ to determine the settings seat graphic
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.7.1.1.6
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 ELSE 分支
- **reasoning_note**：（空）

---

## 段 26 —— 254 ~ 261（8 條）

### `NR1L-PowerManagement-254`

- **req_id**：SWE-PM-088
- **tc_id**：NR1L-PowerManagement-254
- **tc_title**：The performance gauges follow the vehicle line signal
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The performance gauges follow the vehicle line signal
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The performance gauges screen is reachable
```
- **input_test_data**：$VC_VEH_LINE$: a configured vehicle line value
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the shown gauges to check which assignment the HU applies
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The performance gauges match the assignment for that vehicle line
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.15.1.10
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 $VC_VEH_LINE$ 決定 gauges
- **reasoning_note**：（空）

### `NR1L-PowerManagement-255`

- **req_id**：SWE-PM-090
- **tc_id**：NR1L-PowerManagement-255
- **tc_title**：The auto theme mode follows the day night signal into the day theme
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The auto theme mode follows the day night signal into the day theme
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The "Theme Mode" setting reads "Auto"
```
- **input_test_data**：$Day_Night_Mode$: the value indicating day
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the applied theme to check which theme the HU shows
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU shows the Day theme
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.17
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Auto 跟隨日間值
- **reasoning_note**：（空）

### `NR1L-PowerManagement-256`

- **req_id**：SWE-PM-090
- **tc_id**：NR1L-PowerManagement-256
- **tc_title**：The auto theme mode follows the day night signal into the night theme
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The auto theme mode follows the day night signal into the night theme
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The "Theme Mode" setting reads "Auto"
```
- **input_test_data**：$Day_Night_Mode$: the value indicating night
- **test_procedure**：

```
1. Send the value listed in Input Test Data
2. Read the applied theme to check which theme the HU shows
```
- **expected_result**：

```
1. The HU accepts the signal value
2. The HU shows the Night theme
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.17
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Auto 跟隨夜間值
- **reasoning_note**：（空）

### `NR1L-PowerManagement-257`

- **req_id**：SWE-PM-091
- **tc_id**：NR1L-PowerManagement-257
- **tc_title**：The day theme mode uses the Day theme
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The day theme mode uses the Day theme
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The "Theme Mode" setting reads "Day"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU to the theme presentation
2. Read the applied theme to check which theme the HU uses
```
- **expected_result**：

```
1. The theme presentation is reached
2. The HU uses the Day theme
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.17
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Theme Mode 設為 Day 之結果
- **reasoning_note**：（空）

### `NR1L-PowerManagement-258`

- **req_id**：SWE-PM-092
- **tc_id**：NR1L-PowerManagement-258
- **tc_title**：The night theme mode uses the Night theme
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The night theme mode uses the Night theme
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The "Theme Mode" setting reads "Night"
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU to the theme presentation
2. Read the applied theme to check which theme the HU uses
```
- **expected_result**：

```
1. The theme presentation is reached
2. The HU uses the Night theme
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.17
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗 Theme Mode 設為 Night 之結果
- **reasoning_note**：（空）

### `NR1L-PowerManagement-259`

- **req_id**：SWE-PM-096
- **tc_id**：NR1L-PowerManagement-259
- **tc_title**：The season changes to Summer at the December date
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The season changes to Summer at the December date
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Summer start date
```
- **input_test_data**：An Ignition On after the date passes December, 21st
- **test_procedure**：

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```
- **expected_result**：

```
1. The HU determines the season at Ignition On
2. The HU determines that Summer has started
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗季節界線一（12/21）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-260`

- **req_id**：SWE-PM-096
- **tc_id**：NR1L-PowerManagement-260
- **tc_title**：The season changes to Fall at the March date
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The season changes to Fall at the March date
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Fall start date
```
- **input_test_data**：An Ignition On after the date passes March, 20th
- **test_procedure**：

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```
- **expected_result**：

```
1. The HU determines the season at Ignition On
2. The HU determines that Fall has started
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗季節界線二（3/20）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-261`

- **req_id**：SWE-PM-096
- **tc_id**：NR1L-PowerManagement-261
- **tc_title**：The season changes to Winter at the June date
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The season changes to Winter at the June date
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Winter start date
```
- **input_test_data**：An Ignition On after the date passes June, 21st
- **test_procedure**：

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```
- **expected_result**：

```
1. The HU determines the season at Ignition On
2. The HU determines that Winter has started
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗季節界線三（6/21）
- **reasoning_note**：（空）

---

## 段 27 —— 262 ~ 264（3 條）

### `NR1L-PowerManagement-262`

- **req_id**：SWE-PM-096
- **tc_id**：NR1L-PowerManagement-262
- **tc_title**：The season changes to Spring at the September date
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：The season changes to Spring at the September date
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Spring start date
```
- **input_test_data**：An Ignition On after the date passes September, 23rd
- **test_procedure**：

```
1. Bring the HU through the event listed in Input Test Data
2. Read the season the HU determines to check the boundary
```
- **expected_result**：

```
1. The HU determines the season at Ignition On
2. The HU determines that Spring has started
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗季節界線四（9/23）
- **reasoning_note**：（空）

### `NR1L-PowerManagement-263`

- **req_id**：SWE-PM-096
- **tc_id**：NR1L-PowerManagement-263
- **tc_title**：A season change plays the new season startup animation
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：A season change plays the new season startup animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The previous Ignition On was in a different season
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through an Ignition On
2. Read the played animation to check which one the HU selects
```
- **expected_result**：

```
1. The HU determines that there has been a change in season
2. The HU plays the new season startup animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗有變更之後果
- **reasoning_note**：（空）

### `NR1L-PowerManagement-264`

- **req_id**：SWE-PM-096
- **tc_id**：NR1L-PowerManagement-264
- **tc_title**：No season change plays the normal brand based startup animation
- **test_group**：Power Management
- **test_set**：Branding and Theme
- **test_item**：No season change plays the normal brand based startup animation
- **pre_conditions**：

```
1. A LIN and CAN simulation tool is connected
2. The previous Ignition On was in the same season
```
- **input_test_data**：NA
- **test_procedure**：

```
1. Bring the HU through an Ignition On
2. Read the played animation to check which one the HU selects
```
- **expected_result**：

```
1. The HU determines that there has not been a change in season
2. The HU plays the normal Brand based startup animation
```
- **specification_reference**：R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.9.16
- **priority**：P0
- **design_method**：狀態轉換 (State Transition Testing)
- **functional_safety**：NA
- **split_reason**：本條驗無變更之後果
- **reasoning_note**：（空）
