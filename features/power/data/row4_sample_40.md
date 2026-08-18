# B1(b) —— 第 4 列新增 61 條之抽樣素材（R-P272(b)）

> **本檔不作判定、不作摘要，逐字呈現。**
> 母體 **61** 條（第 4 列 80 → 141 之新增部分）；抽 **13** 條 = **21.3%**，種子 `random.Random(40)`。
> 複核之問題：**該 TC 之結果是否確由所列之二個以上條件共同決定？**

**抽樣清單**：`…-011`、`…-027`、`…-098`、`…-104`、`…-122`、`…-158`、`…-176`、`…-189`、`…-198`、`…-220`、`…-237`、`…-242`、`…-245`

---

## 1 / 13 —— `NR1L-PowerManagement-011`（`SWE-PM-073`）

**`tc_title`**：Load Shed recovers: normal volume and audio restored

**現落點**：第 9 列　**擴充後之總條件數**：3

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 3. The Load Shed condition is already active |
| 2 | `input_test_data` | STATUS_LIN.PN14_LS_Actv = [0h] |
| 3 | `input_test_data` | STATUS_LIN.PN14_LS_Lvl7 = [0h] |

### 四欄逐字

**`pre_conditions`**：
```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. The Load Shed condition is already active
```

**`input_test_data`**：
```
STATUS_LIN.PN14_LS_Actv = [0h]
STATUS_LIN.PN14_LS_Lvl7 = [0h]
```

**`test_procedure`**：
```
1. Stop the broadcast of the two Load Shed signals on the bus
2. Resume the broadcast with the recovery values listed in Input Test Data
3. Read the volume limit and the audio output state to check that Load Shed ends
```

**`expected_result`**：
```
1. The two Load Shed signals are absent from the bus trace
2. The TLM accepts the resumed broadcast without a bus error
3. The volume limit returns to its normal maximum and the audio output is unmuted
```

## 2 / 13 —— `NR1L-PowerManagement-027`（`SWE-PM-062`）

**`tc_title`**：Auto_SwitchOn_Setting.Req can be set to Recall_Last

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The TLM is in Full-Operation status |
| 2 | `test_procedure` | 2. Select "Recall_Last" for Auto_SwitchOn_Setting.Req |

### 四欄逐字

**`pre_conditions`**：
```
1. An LTM High Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

**`input_test_data`**：
```
NA
```

**`test_procedure`**：
```
1. Open the timeout setting entry in the TLM menu
2. Select "Recall_Last" for Auto_SwitchOn_Setting.Req
3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection
```

**`expected_result`**：
```
1. The timeout setting entry is shown in the TLM menu
2. The TLM accepts the selection without reverting it
3. Auto_SwitchOn_Setting.Req reads "Recall_Last" and Timeout1 reads "00 minutes"
```

## 3 / 13 —— `NR1L-PowerManagement-098`（`SWE-PM-027`）

**`tc_title`**：Antitheft failure clears the activation request within Timeout1

**現落點**：第 9 列　**擴充後之總條件數**：3

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. Antitheft_Activation.Req reads "True" |
| 2 | `test_procedure` | 1. Send the signal listed in Input Test Data |
| 3 | `input_test_data` | Antitheft_Result.Info = "Not_Successfully" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```

**`input_test_data`**：
```
Antitheft_Result.Info = "Not_Successfully"
```

**`test_procedure`**：
```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req and the screen to check the reset and the screen time
```

**`expected_result`**：
```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False" and the Antitheft screens are shown for a time not longer than Timeout1
```

## 4 / 13 —— `NR1L-PowerManagement-104`（`SWE-PM-029`）

**`tc_title`**：Antitheft success clears the activation request on this variant

**現落點**：第 9 列　**擴充後之總條件數**：3

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. Antitheft_Activation.Req reads "True" |
| 2 | `test_procedure` | 1. Send the signal listed in Input Test Data |
| 3 | `input_test_data` | Antitheft_Result.Info = "Successfully" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. Antitheft_Activation.Req reads "True"
```

**`input_test_data`**：
```
Antitheft_Result.Info = "Successfully"
```

**`test_procedure`**：
```
1. Send the signal listed in Input Test Data
2. Read Antitheft_Activation.Req to check that it is set back
```

**`expected_result`**：
```
1. The TLM accepts the signal without a bus error
2. Antitheft_Activation.Req reads "False"
```

## 5 / 13 —— `NR1L-PowerManagement-122`（`SWE-PM-039`）

**`tc_title`**：A zero switch off timeout loads Timeout1 from the PROXI value

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. TLM_Status.Info was equal to "Full-Operation" |
| 2 | `input_test_data` | SwitchOff_Timeout_Setting.Req: "00 min" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. TLM_Status.Info was equal to "Full-Operation"
```

**`input_test_data`**：
```
SwitchOff_Timeout_Setting.Req: "00 min"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read Timeout1 against the configured parameter to check the loaded value
```

**`expected_result`**：
```
1. The TLM registers the value without a bus error
2. Timeout1 reads the "Switch_Off_Time" PROXI value
```

## 6 / 13 —— `NR1L-PowerManagement-158`（`SWE-PM-056`）

**`tc_title`**：The Fiat Latam startup animation replaces the vehicle brand logo

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The HU carries a configured vehicle brand |
| 2 | `input_test_data` | DID "Startup Animation Selection": "Fiat Latam" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. The HU carries a configured vehicle brand
```

**`input_test_data`**：
```
DID "Startup Animation Selection": "Fiat Latam"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read the shown logo against the configured brand to check which logo the HU displays
```

**`expected_result`**：
```
1. The HU accepts the configuration value
2. The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand
```

## 7 / 13 —— `NR1L-PowerManagement-176`（`SWE-PM-076`）

**`tc_title`**：The power button reset covers both the main CPU and the CAN micro

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The HU is not installing a firmware image |
| 2 | `input_test_data` | $ICSPowerButton$: Pressed for 10 seconds consecutively |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. The HU is not installing a firmware image
```

**`input_test_data`**：
```
$ICSPowerButton$: Pressed for 10 seconds consecutively
```

**`test_procedure`**：
```
1. Send the input listed in Input Test Data
2. Read both processors to check what the reset covers
```

**`expected_result`**：
```
1. The main CPU resets at the time of the reset
2. The CAN micro resets at the time of the reset
```

## 8 / 13 —— `NR1L-PowerManagement-189`（`SWE-PM-097`）

**`tc_title`**：The Fiat Latam startup animation selection replaces the vehicle brand logo

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The HU carries a configured vehicle brand |
| 2 | `input_test_data` | DID "Startup Animation Selection": "Fiat Latam" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. The HU carries a configured vehicle brand
```

**`input_test_data`**：
```
DID "Startup Animation Selection": "Fiat Latam"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read the shown logo against the configured brand to check which logo appears
```

**`expected_result`**：
```
1. The HU accepts the configuration value
2. The Fiat Latam Logo replaces the vehicle brand logo regardless of the configured brand
```

## 9 / 13 —— `NR1L-PowerManagement-198`（`SWE-PM-101`）

**`tc_title`**：SDARS present without audio brand adds the Sirius logo

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. SDARS_Presence reads "Present" |
| 2 | `input_test_data` | Audio_Brand: "No Audio Brand" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. SDARS_Presence reads "Present"
```

**`input_test_data`**：
```
Audio_Brand: "No Audio Brand"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read the shown logos to check the resulting presentation
```

**`expected_result`**：
```
1. The brand logo screen is presented
2. The Sirius logo is shown in addition to the vehicle brand logo
```

## 10 / 13 —— `NR1L-PowerManagement-220`（`SWE-PM-106`）

**`tc_title`**：The SOS button variant selects the SOS disclaimer text

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The HU is configured for a disclaimer screen variation |
| 2 | `input_test_data` | $Ecall_Button_Variant$: "SOS" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. The HU is configured for a disclaimer screen variation
```

**`input_test_data`**：
```
$Ecall_Button_Variant$: "SOS"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read the disclaimer wording to check which text the HU uses
```

**`expected_result`**：
```
1. The HU accepts the configuration value
2. The HU uses the SOS text for the disclaimer
```

## 11 / 13 —— `NR1L-PowerManagement-237`（`SWE-PM-081`）

**`tc_title`**：The Chrysler brand selects the Chrysler font

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The HU is displaying branded text |
| 2 | `input_test_data` | $VC_VEH_BRAND$: "Chrysler" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. The HU is displaying branded text
```

**`input_test_data`**：
```
$VC_VEH_BRAND$: "Chrysler"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read the displayed font to check which font the HU selects
```

**`expected_result`**：
```
1. The HU accepts the signal value
2. The HU displays the Chrysler font
```

## 12 / 13 —— `NR1L-PowerManagement-242`（`SWE-PM-082`）

**`tc_title`**：The Fiat brand selects the default Fiat App icon

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The HU is displaying the App icon |
| 2 | `input_test_data` | $VC_VEH_BRAND$: "Fiat" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. The HU is displaying the App icon
```

**`input_test_data`**：
```
$VC_VEH_BRAND$: "Fiat"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read the displayed App icon to check which icon the HU selects
```

**`expected_result`**：
```
1. The HU accepts the signal value
2. The HU displays the Fiat App icon that the specification marks as DEFAULT
```

## 13 / 13 —— `NR1L-PowerManagement-245`（`SWE-PM-083`）

**`tc_title`**：The Abarth brand is mapped to the Fiat avatars

**現落點**：第 9 列　**擴充後之總條件數**：2

### 條件之逐字出處

| # | 來源欄位 | 逐字 |
|---|---|---|
| 1 | `pre_conditions` | 2. The profile screen is reachable on the HU |
| 2 | `input_test_data` | $VC_VEH_BRAND$: "Abarth" |

### 四欄逐字

**`pre_conditions`**：
```
1. A LIN and CAN simulation tool is connected
2. The profile screen is reachable on the HU
```

**`input_test_data`**：
```
$VC_VEH_BRAND$: "Abarth"
```

**`test_procedure`**：
```
1. Send the value listed in Input Test Data
2. Read the avatar list in the profile screen to check which set is offered
```

**`expected_result`**：
```
1. The HU accepts the signal value
2. The profile screen offers the Fiat avatars rather than an Abarth set
```
