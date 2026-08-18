# G170 —— 第 4 列 80 條之逐條確認證據（R-P243）

> **本檔不作判定，只蒐證。** 判定見上繳 §三。
> 證據甲＝`source_clause` 之條件子句數；證據乙＝同 leaf 內僅差一前提而 ER 不同之姊妹 TC；證據丙＝`input_test_data` 之獨立參數數。

## 一、證據交叉分布（80 條）

| 證據甲 規格條件子句 ≥ 2 | 證據乙 有姊妹 | 條數 | 意義 |
|---|---|---|---|
| 是 | 是 | **27** | 規格為多條件結構，且該條件確實改變結果 |
| 是 | 否 | **37** | 規格為多條件，惟未以姊妹枚舉 |
| 否 | 是 | **4** | 規格僅一條件子句，惟姊妹顯示條件改變結果 |
| 否 | 否 | **12** | 二證據皆無 —— 代理判準之疑似偽陽性 |

## 二、逐條

| tc | leaf | 實質前提 | 甲 | 乙 姊妹 | 丙 參數 |
|---|---|---|---|---|---|
| `009` | `SWE-PM-073` | 2. The TLM is in BODY ON mode；3. Ecall, ACN and chimes modes are inactive | 11 | `…-013` | 2 |
| `013` | `SWE-PM-073` | 2. The TLM is in BODY ON mode；3. A non-Ecall non-ACN call is active and continuing | 11 | `…-009` | 1 |
| `014` | `SWE-PM-073` | 2. The TLM is in BODY OFF-TIMED mode；3. Ecall, ACN and chimes modes are inactive | 11 | `…-017` | 2 |
| `017` | `SWE-PM-073` | 2. The TLM is in BODY ON mode；3. Ecall, ACN and chimes modes are inactive | 11 | `…-013` | 2 |
| `018` | `SWE-PM-057` | 2. The PROXI parameter "Switch_Off_Time" is at 20 minutes；3. The TLM is in Full-Operation status | 7 | `…-019` | 0 |
| `019` | `SWE-PM-057` | 2. The PROXI parameter "Switch_Off_Time" is at 60 minutes；3. The TLM is in Full-Operation status | 7 | `…-018` | 0 |
| `020` | `SWE-PM-057` | 2. The PROXI parameter "Switch_Off_Time" is at 180 minutes；3. The TLM is in Full-Operation statu | 7 | `…-018` | 0 |
| `029` | `SWE-PM-064` | 1. Timeout1 is at "00 min"；2. The TLM is in Full-Operation state；3. Phone_Call.Info is at "Activ | 2 | **無** | 1 |
| `030` | `SWE-PM-064` | 1. Timeout1 is at a value other than "00 min"；2. The TLM is in Timed state；3. Phone_Call.Info is | 2 | **無** | 0 |
| `031` | `SWE-PM-065` | 1. Timeout1 is at a value other than "00 min"；2. The TLM is in Timed state；3. A DAB Tuner source | 2 | **無** | 0 |
| `032` | `SWE-PM-065` | 1. Timeout1 is at a value other than "00 min"；2. The TLM is in Timed state；3. One call has alrea | 2 | **無** | 0 |
| `035` | `SWE-PM-038` | 1. Timeout1 is at a value other than "00 min"；2. The TLM is in Timed state；3. Phone_Call.Info is | 14 | `…-038` | 0 |
| `045` | `SWE-PM-011` | 1. The HU is in FULL OPERATION mode；3. A CarPlay VR interaction has completed | 8 | **無** | 1 |
| `046` | `SWE-PM-011` | 1. The HU is in FULL OPERATION mode；3. A CarPlay VR interaction has completed | 8 | **無** | 1 |
| `047` | `SWE-PM-011` | 1. The HU is in FULL OPERATION mode；3. A CarPlay VR interaction has completed | 8 | **無** | 1 |
| `058` | `SWE-PM-014` | 2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"；3. LTM_OperationalModeSts.Info is | 13 | **無** | 1 |
| `059` | `SWE-PM-014` | 2. RemStartFail reads "True"；3. Phone_Call.Info reads "Not Active" | 13 | **無** | 0 |
| `061` | `SWE-PM-014` | 2. SwitchOff_Timeout_Setting.Req and Timeout1 read "00 MIN"；3. Phone_Call.Info reads "Active" | 13 | `…-060` | 0 |
| `063` | `SWE-PM-014` | 2. SwitchOff_Timeout_Setting.Req and Timeout1 read a value other than "00 MIN"；3. Brand_Configur | 13 | **無** | 0 |
| `065` | `SWE-PM-014` | 3. Auto_SwitchOn_Setting.Req reads "Not_Active " and Timeout1 reads a value other than "00 MIN"； | 13 | **無** | 0 |
| `066` | `SWE-PM-014` | 2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"；3. LTM_OperationalModeSts.Info is | 13 | **無** | 1 |
| `072` | `SWE-PM-017` | 2. TLM_Status.Info and $Telematic_Power$ read "Full-Operation"；3. Rear_View_Camera reads "Presen | 2 | **無** | 0 |
| `075` | `SWE-PM-019` | 2. TLM_Status.Info and $Telematic_Power$ read "Idle"；3. Rear_View_Camera reads "Present" and Rea | 4 | `…-076` | 0 |
| `077` | `SWE-PM-019` | 2. TLM_Status.Info and $Telematic_Power$ read "Idle"；3. Rear_View_Camera reads "Present" and Rea | 4 | `…-076` | 0 |
| `081` | `SWE-PM-020` | 2. TLM_Status.Info reads "Full-Operation" entered through a call；3. TLM_Display.GUI is on a scre | 5 | `…-080` | 1 |
| `082` | `SWE-PM-021` | 2. TLM_Status.Info and $Telematic_Power$ read "Idle"；3. Rear_View_Camera reads "Present" | 1 | **無** | 1 |
| `086` | `SWE-PM-025` | 2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. Phone_Call.Info reads "Active" | 10 | `…-087` | 0 |
| `088` | `SWE-PM-025` | 2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. The transfer popup is shown | 10 | `…-086` | 0 |
| `090` | `SWE-PM-025` | 2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. Phone_Call.Info reads "Active" | 10 | `…-087` | 0 |
| `092` | `SWE-PM-025` | 2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. The transfer popup is shown | 10 | `…-086` | 0 |
| `095` | `SWE-PM-026` | 2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. Brand_Configuration_2 reads "Jeep" and  | 4 | `…-094` | 1 |
| `096` | `SWE-PM-026` | 2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. Brand_Configuration_2 reads "Jeep" and  | 4 | `…-094` | 1 |
| `097` | `SWE-PM-026` | 2. TLM_Status.Info and $Telematic_Power$ read "Timed"；3. Brand_Configuration_2 reads a value oth | 4 | `…-094` | 1 |
| `099` | `SWE-PM-027` | 2. The TLM is in Partial Operation；3. Antitheft_Activation.Req reads "True" | 4 | **無** | 1 |
| `101` | `SWE-PM-028` | 2. SwitchOff_Timeout_Setting.Req reads "00 min"；3. Switch_Off_Time reads 20 minutes | 5 | **無** | 1 |
| `103` | `SWE-PM-028` | 3. Auto_SwitchOn_Setting.Req reads "Active " and Timeout1 reads "00 MIN"；4. Switch_Off_Time read | 5 | **無** | 1 |
| `105` | `SWE-PM-029` | 2. SwitchOff_Timeout_Setting.Req reads "00 min"；3. Switch_Off_Time reads 20 minutes | 5 | `…-106` | 1 |
| `106` | `SWE-PM-029` | 2. SwitchOff_Timeout_Setting.Req reads "00 min"；3. $PwrAccDelayAct$ reads 10 minutes | 5 | `…-105` | 1 |
| `109` | `SWE-PM-030` | 2. Auto_SwitchOn_Setting.Req reads "Recall_Last"；3. VPLastStatus reads "On" | 2 | **無** | 0 |
| `110` | `SWE-PM-031` | 2. Rear_View_Camera reads "Present"；3. The TLM is in Standby state | 1 | **無** | 1 |
| `123` | `SWE-PM-039` | 2. TLM_Status.Info was equal to "Full-Operation"；3. The unit is an LTM High Radio | 3 | **無** | 1 |
| `130` | `SWE-PM-043` | 2. The HU is in Standby mode；3. No HMI screen is required | 1 | **無** | 0 |
| `132` | `SWE-PM-044` | 2. TLM_Status.Info and $Telematic_Power$ read "Standby"；3. The Engineering Line is deactivated | 2 | **無** | 1 |
| `133` | `SWE-PM-044` | 2. TLM_Status.Info and $Telematic_Power$ read "Sleep"；3. The Engineering Line is deactivated | 2 | **無** | 1 |
| `134` | `SWE-PM-044` | 2. TLM_Status.Info and $Telematic_Power$ read "Standby"；3. The Engineering Line is deactivated | 2 | **無** | 1 |
| `135` | `SWE-PM-044` | 2. TLM_Status.Info and $Telematic_Power$ read "Sleep"；3. The Engineering Line is deactivated | 2 | **無** | 1 |
| `138` | `SWE-PM-046` | 2. The Rear_View_Camera PROXI parameter reads "Present"；3. Rear_Camera_Enable.Info reads "True" | 3 | **無** | 1 |
| `139` | `SWE-PM-046` | 2. The Rear_View_Camera PROXI parameter reads "Present"；3. Rear_Camera_Enable.Info reads "True" | 3 | **無** | 1 |
| `156` | `SWE-PM-055` | 2. The ETM carries $VC_MODEL_YEAR$ equal to "2025"；3. The ETM carries $VC_VEH_LINE$ equal to "DT | 2 | **無** | 1 |
| `157` | `SWE-PM-055` | 2. The ETM carries $VC_MODEL_YEAR$ greater than "2025"；3. The ETM carries $VC_VEH_LINE$ equal to | 2 | **無** | 1 |
| `161` | `SWE-PM-059` | 2. TLM_Status.Info and $Telematic_Power$ read "Standby"；3. The boot of the TLM is not ended | 2 | `…-160` | 1 |
| `178` | `SWE-PM-093` | 2. The HU is in SLEEP MODE；3. A driver door is present for the vehicle | 16 | **無** | 1 |
| `179` | `SWE-PM-093` | 2. The HU is in STANDBY MODE；3. A driver door is present for the vehicle | 16 | `…-185` | 1 |
| `180` | `SWE-PM-093` | 2. The HU is in PARTIAL OPERATION MODE；3. A driver door is present for the vehicle | 16 | **無** | 1 |
| `186` | `SWE-PM-093` | 2. The HU has just played a start-up animation；3. All other conditions for the animation to play | 16 | **無** | 0 |
| `190` | `SWE-PM-098` | 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Always" | 1 | **無** | 0 |
| `191` | `SWE-PM-099` | 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Once a Day"；4 | 2 | `…-192` | 0 |
| `192` | `SWE-PM-099` | 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Once a Day"；4 | 2 | `…-191` | 1 |
| `193` | `SWE-PM-099` | 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Once a Day"；4 | 2 | `…-191` | 0 |
| `194` | `SWE-PM-099` | 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Once a Day"；4 | 2 | `…-191` | 1 |
| `195` | `SWE-PM-100` | 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Never" | 1 | **無** | 0 |
| `200` | `SWE-PM-102` | 2. The ETM carries $VC_MODEL_YEAR$ equal to "2025"；3. The ETM carries $VC_VEH_LINE$ equal to "DT | 2 | **無** | 1 |
| `201` | `SWE-PM-102` | 2. The ETM carries $VC_MODEL_YEAR$ greater than "2025"；3. The ETM carries $VC_VEH_LINE$ equal to | 2 | **無** | 1 |
| `207` | `SWE-PM-104` | 2. A new bus cycle has started；3. Neither screen has been shown in this bus cycle | 1 | **無** | 0 |
| `208` | `SWE-PM-104` | 2. A new bus cycle has started；3. Neither screen has been shown in this bus cycle | 1 | **無** | 0 |
| `223` | `SWE-PM-109` | 2. $VC_VEH_BRAND$ reads a value other than "Maserati"；3. $TBM_Present$ reads "Present"；4. $Count | 1 | **無** | 0 |
| `224` | `SWE-PM-110` | 2. $VC_VEH_BRAND$ reads a value other than "Maserati"；3. $TBM_Present$ reads "Not Present" | 1 | **無** | 0 |
| `225` | `SWE-PM-110` | 2. $VC_VEH_BRAND$ reads a value other than "Maserati"；3. $TBM_Present$ reads "Present"；4. $Count | 1 | **無** | 0 |
| `226` | `SWE-PM-111` | 2. The screen size is other than 7 inch；3. $VC_VEH_BRAND$ reads a value other than "Maserati"；4. | 1 | **無** | 0 |
| `227` | `SWE-PM-111` | 2. The screen size is other than 7 inch；3. $VC_VEH_BRAND$ reads a value other than "Maserati"；4. | 1 | **無** | 0 |
| `228` | `SWE-PM-113` | 2. The screen size is other than 7 inch；3. $VC_VEH_BRAND$ reads a value other than "Maserati"；4. | 2 | **無** | 0 |
| `235` | `SWE-PM-080` | 2. The CAN network is awake；3. A theme is applied on the HU | 2 | **無** | 0 |
| `236` | `SWE-PM-080` | 2. The CAN network is awake；3. A theme is applied on the HU | 2 | **無** | 1 |
| `246` | `SWE-PM-084` | 2. The HU runs the CUSW or Atlantis architecture；3. The climate screen showing the recirc icon i | 0 | `…-247` | 1 |
| `247` | `SWE-PM-084` | 2. The HU runs the PNET architecture；3. The climate screen showing the recirc icon is reachable | 0 | `…-246` | 1 |
| `248` | `SWE-PM-085` | 2. The HU runs the CUSW or Atlantis architecture；3. The seat settings screen is reachable | 0 | `…-249` | 1 |
| `249` | `SWE-PM-085` | 2. The HU runs the PNET architecture；3. The seat settings screen is reachable | 0 | `…-248` | 1 |
| `250` | `SWE-PM-086` | 2. The CAN network is awake；3. A theme is applied on the HU | 2 | **無** | 0 |
| `251` | `SWE-PM-086` | 2. The CAN network is awake；3. A theme is applied on the HU | 2 | **無** | 1 |
| `253` | `SWE-PM-087` | 2. The seat settings screen is reachable；3. The HU carries a configured vehicle brand | 2 | **無** | 1 |

## 三、二證據皆無者（逐條，供人工判偽陽性）

- `…-082`（`SWE-PM-021`）：實質前提 2. TLM_Status.Info and $Telematic_Power$ read "Idle"；3. Rear_View_Camera reads "Present"；規格條件子句 1
- `…-110`（`SWE-PM-031`）：實質前提 2. Rear_View_Camera reads "Present"；3. The TLM is in Standby state；規格條件子句 1
- `…-130`（`SWE-PM-043`）：實質前提 2. The HU is in Standby mode；3. No HMI screen is required；規格條件子句 1
- `…-190`（`SWE-PM-098`）：實質前提 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Always"；規格條件子句 1
- `…-195`（`SWE-PM-100`）：實質前提 2. $Themed_Sound$ reads "Fiat Latam"；3. The "Welcome Onboard Sound" setting reads "Never"；規格條件子句 1
- `…-207`（`SWE-PM-104`）：實質前提 2. A new bus cycle has started；3. Neither screen has been shown in this bus cycle；規格條件子句 1
- `…-208`（`SWE-PM-104`）：實質前提 2. A new bus cycle has started；3. Neither screen has been shown in this bus cycle；規格條件子句 1
- `…-223`（`SWE-PM-109`）：實質前提 2. $VC_VEH_BRAND$ reads a value other than "Maserati"；3. $TBM_Present$ reads "Present"；4. $Country_Code$ is marked as a country needing the combined Geolocation plus SOS Popup；規格條件子句 1
- `…-224`（`SWE-PM-110`）：實質前提 2. $VC_VEH_BRAND$ reads a value other than "Maserati"；3. $TBM_Present$ reads "Not Present"；規格條件子句 1
- `…-225`（`SWE-PM-110`）：實質前提 2. $VC_VEH_BRAND$ reads a value other than "Maserati"；3. $TBM_Present$ reads "Present"；4. $Country_Code$ is not marked as one of the "Countries which need the combined Geolocation plus SOS Popup" in the Market Configuration Table；規格條件子句 1
- `…-226`（`SWE-PM-111`）：實質前提 2. The screen size is other than 7 inch；3. $VC_VEH_BRAND$ reads a value other than "Maserati"；4. $TBM_Present$ reads "Not Present"；規格條件子句 1
- `…-227`（`SWE-PM-111`）：實質前提 2. The screen size is other than 7 inch；3. $VC_VEH_BRAND$ reads a value other than "Maserati"；4. $Country_Code$ does not require SOS or Geolocation；規格條件子句 1
