# B5 —— 自 `input_data` 移出者之抽樣素材（R-P285）

> **本檔不作判定、不作摘要，逐字呈現。**
> 母體：自 `input_data` 移出者 **64** 條；抽 **15** 條 = **23.4%**（≥ 20%），種子 `random.Random(42)`。
> **⚠ 按群輪轉交錯排列**（41 §K 第 2 項）—— 依序讀取即自然跨群，不致集中於單一群。

| 移出至 | 母體 | 抽樣 | 率 |
|---|---|---|---|
| `**無對應**` | 23 | **5** | 22% |
| `mode` | 2 | **1** | 50% |
| `timing` | 7 | **2** | 29% |
| `trigger_state` | 32 | **7** | 22% |

**閱讀序（交錯）**：`…-005`(**無對應**)、`…-021`(mode)、`…-259`(timing)、`…-036`(trigger_state)、`…-162`(**無對應**)、`…-260`(timing)、`…-038`(trigger_state)、`…-169`(**無對應**)、`…-073`(trigger_state)、`…-170`(**無對應**)、`…-108`(trigger_state)、`…-216`(**無對應**)、`…-116`(trigger_state)、`…-138`(trigger_state)、`…-206`(trigger_state)

**複核之問題**：該 TC 與其對照姊妹之區分，是否確為新值所指之語義框架（`input_data`＝餵入之資料值／`trigger_state`＝系統或車輛狀態／`mode`＝硬體或 bench 配置／`timing`＝事件時點）？

---

## 1 / 15 —— `NR1L-PowerManagement-005`（`SWE-PM-072`）　`input_data` → **`**無對應**`**

**`tc_title`**：Events during boot are buffered without loss

**執行層之依據**：對照 `006`，五個正向判準皆未命中；相異行：（無）

**對照條 `NR1L-PowerManagement-006`**：Buffered events processed as soon as possible during boot

**相異行（已排除觀察步驟）**：
```

```

**`test_procedure`**

本條：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM event log to check that every injected event was buffered without loss
```

對照：
```
1. Start the TLM boot sequence and inject the event burst listed in Input Test Data while the boot is still completing
2. Read the TLM_Status transitions during the remainder of the boot to check that every buffered event is processed
```


## 2 / 15 —— `NR1L-PowerManagement-021`（`SWE-PM-060`）　`input_data` → **`mode`**

**`tc_title`**：LTM or ETM Radio offers one timeout parameter

**執行層之依據**：對照 `022`，相異行命中 mode：`Radio is present`

**對照條 `NR1L-PowerManagement-022`**：Radio other than LTM or ETM offers two timeout parameters

**相異行（已排除觀察步驟）**：
```
1. An LTM Radio is present in the bench configuration
```

**`pre_conditions`**

本條：
```
1. An LTM Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

對照：
```
1. A Radio other than LTM or ETM is present in the bench configuration
2. The TLM is in Full-Operation status
```

**`test_procedure`**

本條：
```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that only one is present
```

對照：
```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that both are present
```


## 3 / 15 —— `NR1L-PowerManagement-259`（`SWE-PM-096`）　`input_data` → **`timing`**

**`tc_title`**：The season changes to Summer at the December date

**執行層之依據**：對照 `260`，相異行命中 timing：`before the Summer start`

**對照條 `NR1L-PowerManagement-260`**：The season changes to Fall at the March date

**相異行（已排除觀察步驟）**：
```
2. The HU clock is set to the day before the Summer start date
An Ignition On after the date passes December, 21st
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Summer start date
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Fall start date
```

**`input_test_data`**

本條：
```
An Ignition On after the date passes December, 21st
```

對照：
```
An Ignition On after the date passes March, 20th
```


## 4 / 15 —— `NR1L-PowerManagement-036`（`SWE-PM-038`）　`input_data` → **`trigger_state`**

**`tc_title`**：Case 2 exit on call end: TLM_Status.Info passes to Standby

**執行層之依據**：對照 `041`，相異行命中 trigger_state：`is in Timed`

**對照條 `NR1L-PowerManagement-041`**：Case 4 exit: TLM passes to Standby when the call ends

**相異行（已排除觀察步驟）**：
```
1. The TLM is in Timed state with MaxCallTimeout running
2. Phone_Call.Info is at "Active"
```

**`pre_conditions`**

本條：
```
1. The TLM is in Timed state with MaxCallTimeout running
2. Phone_Call.Info is at "Active"
```

對照：
```
1. The TLM is in Timed state entered through Case 4
2. MaxCallTimeout is running
3. Phone_Call.Info is at "Active"
```


## 5 / 15 —— `NR1L-PowerManagement-162`（`SWE-PM-066`）　`input_data` → **`**無對應**`**

**`tc_title`**：An SOS call is treated as a phone call becoming active

**執行層之依據**：對照 `163`，五個正向判準皆未命中；相異行：An SOS call is placed

**對照條 `NR1L-PowerManagement-163`**：An Assist call is treated as a phone call becoming active

**相異行（已排除觀察步驟）**：
```
An SOS call is placed
```

**`input_test_data`**

本條：
```
An SOS call is placed
```

對照：
```
An Assist call is placed
```


## 6 / 15 —— `NR1L-PowerManagement-260`（`SWE-PM-096`）　`input_data` → **`timing`**

**`tc_title`**：The season changes to Fall at the March date

**執行層之依據**：對照 `259`，相異行命中 timing：`before the Fall start`

**對照條 `NR1L-PowerManagement-259`**：The season changes to Summer at the December date

**相異行（已排除觀察步驟）**：
```
2. The HU clock is set to the day before the Fall start date
An Ignition On after the date passes March, 20th
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Fall start date
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The HU clock is set to the day before the Summer start date
```

**`input_test_data`**

本條：
```
An Ignition On after the date passes March, 20th
```

對照：
```
An Ignition On after the date passes December, 21st
```


## 7 / 15 —— `NR1L-PowerManagement-038`（`SWE-PM-038`）　`input_data` → **`trigger_state`**

**`tc_title`**：Case 3: call already ended at Timeout1 expiry

**執行層之依據**：對照 `039`，相異行命中 trigger_state：`Phone_Call.Info`

**對照條 `NR1L-PowerManagement-039`**：Case 3 with RemStartFail cleared at Timeout1 expiry

**相異行（已排除觀察步驟）**：
```
3. Phone_Call.Info is at "Not_Active"
```

**`pre_conditions`**

本條：
```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. Phone_Call.Info is at "Not_Active"
```

對照：
```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Not_Active"
```

**`test_procedure`**

本條：
```
1. Let Timeout1 run to its expiration with no call active
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```

對照：
```
1. Let Timeout1 run to its expiration with no call active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```


## 8 / 15 —— `NR1L-PowerManagement-169`（`SWE-PM-074`）　`input_data` → **`**無對應**`**

**`tc_title`**：A Radio FOTA update at Body OFF brings the HU to Timed for the pop-up

**執行層之依據**：對照 `170`，五個正向判準皆未命中；相異行：A FOTA update available for the Radio

**對照條 `NR1L-PowerManagement-170`**：A TBM FOTA update at Body OFF brings the HU to Timed for the pop-up

**相異行（已排除觀察步驟）**：
```
A FOTA update available for the Radio
```

**`input_test_data`**

本條：
```
A FOTA update available for the Radio
```

對照：
```
A FOTA update available for the TBM
```


## 9 / 15 —— `NR1L-PowerManagement-073`（`SWE-PM-018`）　`input_data` → **`trigger_state`**

**`tc_title`**：Ignition off in Idle passes the TLM to Standby

**執行層之依據**：對照 `074`，相異行命中 trigger_state：`Ignition Off`

**對照條 `NR1L-PowerManagement-074`**：Ignition pre off in Idle passes the TLM to Standby

**相異行（已排除觀察步驟）**：
```
LTM_OperationalModeSts: "Ignition Off"
```

**`input_test_data`**

本條：
```
LTM_OperationalModeSts: "Ignition Off"
```

對照：
```
LTM_OperationalModeSts: "Ignition Pre Off"
```


## 10 / 15 —— `NR1L-PowerManagement-170`（`SWE-PM-074`）　`input_data` → **`**無對應**`**

**`tc_title`**：A TBM FOTA update at Body OFF brings the HU to Timed for the pop-up

**執行層之依據**：對照 `169`，五個正向判準皆未命中；相異行：A FOTA update available for the TBM

**對照條 `NR1L-PowerManagement-169`**：A Radio FOTA update at Body OFF brings the HU to Timed for the pop-up

**相異行（已排除觀察步驟）**：
```
A FOTA update available for the TBM
```

**`input_test_data`**

本條：
```
A FOTA update available for the TBM
```

對照：
```
A FOTA update available for the Radio
```


## 11 / 15 —— `NR1L-PowerManagement-108`（`SWE-PM-030`）　`input_data` → **`trigger_state`**

**`tc_title`**：Splash Screen is shown for the configured wait time

**執行層之依據**：對照 `109`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req`

**對照條 `NR1L-PowerManagement-109`**：Splash Screen is shown for the Recall_Last branch

**相異行（已排除觀察步驟）**：
```
2. Auto_SwitchOn_Setting.Req reads "Active"
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Recall_Last"
3. VPLastStatus reads "On"
```


## 12 / 15 —— `NR1L-PowerManagement-216`（`SWE-PM-105`）　`input_data` → **`**無對應**`**

**`tc_title`**：A climate pop-up temporarily skips the disclaimer and splash screens

**執行層之依據**：對照 `212`，五個正向判準皆未命中；相異行：A climate pop-up at the moment of the tr

**對照條 `NR1L-PowerManagement-212`**：An ongoing call temporarily skips the disclaimer and splash screens

**相異行（已排除觀察步驟）**：
```
A climate pop-up at the moment of the transition
```

**`input_test_data`**

本條：
```
A climate pop-up at the moment of the transition
```

對照：
```
An ongoing call at the moment of the transition
```


## 13 / 15 —— `NR1L-PowerManagement-116`（`SWE-PM-035`）　`input_data` → **`trigger_state`**

**`tc_title`**：Antitheft success with auto switch on not active passes the TLM to Idle

**執行層之依據**：對照 `115`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req`

**對照條 `NR1L-PowerManagement-115`**：Antitheft success with auto switch on active passes the TLM to Full-Operation

**相異行（已排除觀察步驟）**：
```
2. Auto_SwitchOn_Setting.Req reads "Not_Active"
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Not_Active"
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. Auto_SwitchOn_Setting.Req reads "Active"
```

**`test_procedure`**

本條：
```
1. Send the value listed in Input Test Data
2. Read the antitheft request and the TLM state to check the resulting behavior
```

對照：
```
1. Send the value listed in Input Test Data
2. Read the antitheft request, the screen and the TLM state to check the resulting behavior
```


## 14 / 15 —— `NR1L-PowerManagement-138`（`SWE-PM-046`）　`input_data` → **`trigger_state`**

**`tc_title`**：Rear view camera is provided while the antitheft is still in progress

**執行層之依據**：對照 `139`，相異行命中 trigger_state：`Antitheft_Result.Info`

**對照條 `NR1L-PowerManagement-139`**：Rear view camera is provided after an unsuccessful antitheft

**相異行（已排除觀察步驟）**：
```
Antitheft_Result.Info: "In_Progress"
```

**`input_test_data`**

本條：
```
Antitheft_Result.Info: "In_Progress"
```

對照：
```
Antitheft_Result.Info: "Not_Successfully"
```


## 15 / 15 —— `NR1L-PowerManagement-206`（`SWE-PM-103`）　`input_data` → **`trigger_state`**

**`tc_title`**：ICS stays available while DTV is off in this status

**執行層之依據**：對照 `202`，相異行命中 trigger_state：`Ignition On`

**對照條 `NR1L-PowerManagement-202`**：Audio is off and only the Splash Screen is allowed in this status

**相異行（已排除觀察步驟）**：
```
2. The TLM is in an Ignition On Engine On working condition
```

**`pre_conditions`**

本條：
```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition On Engine On working condition
```

對照：
```
1. A LIN and CAN simulation tool is connected
2. The TLM is in an Ignition On working condition
```

**`test_procedure`**

本條：
```
1. Bring the TLM to the status related to TLM audio is OFF
2. Read the ICS functions and the DTV to check their availability
```

對照：
```
1. Bring the TLM to the status related to TLM audio is OFF
2. Read the audio path and the display to check what is allowed
```

