# G187 —— 第 4 列代理判準之條件來源擴充（R-P267）

> **本檔只出提案，不改值**（R-P267(d)）。
> 代理判準仍不得凌駕實質判準（R-P236(b)）。

## 一、條件之計數方式（先量語料）

| 來源 | 計法 |
|---|---|
| `pre_conditions` | 實質條件項數（扣除 bench 樣板列），沿用 `substantive_conditions` |
| `test_procedure` | **設定或施加某具名參數之值**之步驟數 —— 措詞實測：`Set … to` / `Select "…" for` / `Send … signal` / `Apply …` / `Keep … at` |
| `input_test_data` | 非 `NA` 之每一列（每列一個參數取值） |

## 二、影響面

| | 條數 |
|---|---|
| 現行第 4 列（只數 `pre_conditions`） | **80** |
| 擴充後第 4 列 | **141** |
| **新增** | **61** |

## 三、新增者逐條（61）—— 供分析層抽樣複核

| tc | 現落點 | 總條件 | 新增之條件（來自 procedure / data） |
|---|---|---|---|
| `…-007` | 第 8 列 | 6 | 1. Set the TLM volume level to the starting value listed in ；2. Send the two Load Shed signals listed in Input Test Data；STATUS_LIN.PN14_LS_Actv = [1h]；STATUS_LIN.PN14_LS_Lvl7 = [1h]；Starting volume level: 25 |
| `…-010` | 第 9 列 | 4 | 1. Send the recovery signal listed in Input Test Data and st；STATUS_LIN.Batt_ST_Crit = [0h]；Measurement window: 10 seconds |
| `…-011` | 第 9 列 | 3 | STATUS_LIN.PN14_LS_Actv = [0h]；STATUS_LIN.PN14_LS_Lvl7 = [0h] |
| `…-012` | 第 9 列 | 4 | 1. Send the two Load Shed signals listed in Input Test Data；STATUS_LIN.PN14_LS_Actv = [1h]；STATUS_LIN.PN14_LS_Lvl7 = [1h] |
| `…-015` | 第 5 列 | 4 | 1. Keep the Battery Critical signal at the value listed in I；2. Apply the voltage out of range condition on the bench；STATUS_LIN.Batt_ST_Crit = [1h] (held) |
| `…-016` | 第 9 列 | 6 | 1. Set the TLM volume level to the starting value listed in ；2. Send the two Load Shed signals listed in Input Test Data；STATUS_LIN.PN14_LS_Actv = [1h]；STATUS_LIN.PN14_LS_Lvl7 = [1h]；Starting volume level: 15 |
| `…-025` | 第 9 列 | 2 | 2. Select "Active" for Auto_SwitchOn_Setting.Req |
| `…-026` | 第 9 列 | 2 | 2. Select "Not_Active" for Auto_SwitchOn_Setting.Req |
| `…-027` | 第 9 列 | 2 | 2. Select "Recall_Last" for Auto_SwitchOn_Setting.Req |
| `…-052` | 第 9 列 | 3 | 1. Send the signal listed in Input Test Data；STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| `…-053` | 第 9 列 | 3 | 1. Send the signal listed in Input Test Data；STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| `…-054` | 第 9 列 | 3 | 1. Send the signal listed in Input Test Data；STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| `…-055` | 第 9 列 | 3 | 1. Send the signal listed in Input Test Data；STATUS_BH_BCM2.RemStActvSts = "Remote Start Active" |
| `…-098` | 第 9 列 | 3 | 1. Send the signal listed in Input Test Data；Antitheft_Result.Info = "Not_Successfully" |
| `…-100` | 第 9 列 | 3 | 1. Send the signal listed in Input Test Data；Antitheft_Result.Info = "Successfully" |
| `…-104` | 第 9 列 | 3 | 1. Send the signal listed in Input Test Data；Antitheft_Result.Info = "Successfully" |
| `…-114` | 第 9 列 | 2 | Front_Panel_OnOff.Req: "Not_Pressed" to "Pressed" |
| `…-121` | 第 9 列 | 2 | LTM_OperationalModeSts.Info: "SNA" |
| `…-122` | 第 9 列 | 2 | SwitchOff_Timeout_Setting.Req: "00 min" |
| `…-136` | 第 9 列 | 2 | Antitheft_Result.Info: "Not_Successfully" |
| `…-137` | 第 9 列 | 2 | Antitheft_Result.Info: "Not_Successfully" |
| `…-140` | 第 9 列 | 2 | Antitheft_Result.Info: "Not_Successfully" |
| `…-141` | 第 9 列 | 2 | Antitheft_Result.Info: "Not_Successfully" |
| `…-147` | 第 9 列 | 2 | Antitheft_Result.Info: "Not_Successfully" |
| `…-150` | 第 9 列 | 2 | Antitheft_Result.Info: "Not_Successfully" |
| `…-152` | 第 9 列 | 2 | Audio_Brand: "No Audio Brand" |
| `…-153` | 第 9 列 | 2 | Audio_Brand: "Beats Brand White" |
| `…-154` | 第 9 列 | 2 | Audio_Brand: "No Audio Brand" |
| `…-155` | 第 9 列 | 2 | Audio_Brand: "Beats Brand White" |
| `…-158` | 第 9 列 | 2 | DID "Startup Animation Selection": "Fiat Latam" |
| `…-162` | 第 9 列 | 2 | An SOS call is placed |
| `…-163` | 第 9 列 | 2 | An Assist call is placed |
| `…-175` | 第 9 列 | 2 | $ICSPowerButton$: Pressed for 10 seconds consecutively |
| `…-176` | 第 9 列 | 2 | $ICSPowerButton$: Pressed for 10 seconds consecutively |
| `…-177` | 第 9 列 | 2 | $ICSPowerButton$: Pressed for 10 seconds consecutively |
| `…-181` | 第 9 列 | 2 | $DriverDoorOnOffSts$: "DOOR_OFF" |
| `…-188` | 第 9 列 | 2 | LTM_OperationalModeSts.Info: a value different from "SNA" |
| `…-189` | 第 9 列 | 2 | DID "Startup Animation Selection": "Fiat Latam" |
| `…-196` | 第 9 列 | 2 | Audio_Brand: "No Audio Brand" |
| `…-197` | 第 9 列 | 2 | Audio_Brand: "Beats Brand White" |
| `…-198` | 第 9 列 | 2 | Audio_Brand: "No Audio Brand" |
| `…-199` | 第 9 列 | 2 | Audio_Brand: "Beats Brand White" |
| `…-220` | 第 9 列 | 2 | $Ecall_Button_Variant$: "SOS" |
| `…-221` | 第 9 列 | 2 | $Ecall_Button_Variant$: "Help" |
| `…-231` | 第 9 列 | 2 | $VC_SpecialPKG$: a value defined in the PDO Theme Configurat |
| `…-232` | 第 9 列 | 2 | $VC_SpecialPKG$: "none" |
| `…-233` | 第 9 列 | 2 | $VC_SpecialPKG$: a value that is not supported by the HU |
| `…-234` | 第 9 列 | 2 | A referenced CAN signal carrying a value that is not support |
| `…-237` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Chrysler" |
| `…-238` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Jeep" |
| `…-239` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Fiat" |
| `…-240` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Chrysler" |
| `…-241` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Jeep" |
| `…-242` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Fiat" |
| `…-243` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Jeep" |
| `…-244` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Fiat" |
| `…-245` | 第 9 列 | 2 | $VC_VEH_BRAND$: "Abarth" |
| `…-252` | 第 9 列 | 2 | $VC_VEH_LINE$: "M240" |
| `…-254` | 第 9 列 | 2 | $VC_VEH_LINE$: a configured vehicle line value |
| `…-255` | 第 9 列 | 2 | $Day_Night_Mode$: the value indicating day |
| `…-256` | 第 9 列 | 2 | $Day_Night_Mode$: the value indicating night |
