# R-1 v3：訊號寫法（依 CR30580/30581 參考本，2026-08-21）

Pei 提供參考本 `CR30580_CR30581_Imp_FuelPower_&_Rem_Torque_TestCases_20260617.xlsx`
（TestResult 分頁）並指示：「內部訊號也是要觀察，重要的是要觀察哪些訊號」。
**R-1 v2 之 (a)(c)(d) 修訂如下；v2 其餘條款維持。**

## 一、分析層前次誤解之更正

v2(c) 將 `$` 指派給 PROXI，v2(d) 令內部訊號「維持原記法」。
參考本實測顯示**恰好相反**：

| 類別 | 參考本寫法 | `$` |
|---|---|---|
| PROXI | `PROXI Vehicle_Line_Configuration = 124 (DT)` | **無** |
| 訊號 | `$TELEMATIC_VEHICLE_SETUP.HP_Unit_Req$ = 0 (HP)` | **有** |

**`$` 是訊號之標記，不是 PROXI 之標記。** Pei 之「訊號值要加上 $」
即此意。v2(c) 撤銷。

## 二、R-1 v3 條文

```
(a) 訊號一律以 `$<MESSAGE>.<Signal>$` 全名書寫，`$` 包覆全名；
    值採 `= <raw> (<label>)`，label 逐字取自 DBC VAL_。
    Procedure 送出：
      `Send the signal $MESSAGE.Signal$ = <raw> (<label>) to <目的>`
    Procedure 由 HMI 觸發：
      `Select <項目> = <值> to trigger $Signal$ signal transmission`
    Expected Result 觀察：
      `The signal value $MESSAGE.Signal$ = <raw> (<label>) is transmitted`
    Expected Result 顯示：
      `The <項目> display changes to <值>`

(c) PROXI：`PROXI <Param> = <raw> (<label>)`，前綴必寫，**不加 `$`**。
    SWC 之 24 行加 `$` 者為少數例外，不採為通則。

(d) 內部訊號**必須轉為可觀察之 CAN 訊號**，依 §三對照表以
    `$MESSAGE.Signal$` 書寫。查無對應者不得留內部訊號名，
    改以該狀態之 HMI／實體可觀察現象書寫；兩者皆無則標
    `PENDING: DR-{n}`。
```

**不採參考本之下列習慣**（與 canon 牴觸）：行尾句號（§11 禁）、
`Check whether` 作步驟動詞（§5.1 禁，用 `Check that`）。

## 三、PM 內部訊號 → 可觀察訊號對照（DBC 實查）

DBC sha256：BH-CAN `9ef1ec98…30d0`／FD-CAN8 `51c8fd60…1cd2`

**已解析（2 種，涵蓋 197/390 次出現，佔 50.5%）**

| PM 內部訊號 | 次數 | 可觀察訊號 | VAL_ 列舉（逐字） |
|---|---|---|---|
| `TLM_Status.Info` | 177 | `$STATUS_TELEMATIC.PowerSts_Telematic$`（BH-CAN） | 0 Sleep／1 Standby／2 Timed／3 Idle／4 Full_Operation／5 Logistic_On／6 Bench／7 Partial_Operation |
| `LTM_OperationalModeSts.Info` | 20 | `$STATUS_BH_BCM1.OperationalModeSts$`（BH-CAN） | 0 Initialization／1 Ignition_Off_WithoutKey／2 Ignition_Off／3 Ignition_Acc／4 Ignition_On／5 Ignition_Pre_Start／6 Ignition_Start／7 Ignition_Cranking／8 Ignition_On_EngOn |

`PowerSts_Telematic` 之八個狀態與 PM 測項所述之 TLM 狀態逐一相符
（Sleep／Standby／Idle／Full-Operation／Logistic）；
`OperationalModeSts` 之列舉即 PM 之 ignition working conditions。
兩者於 FD-CAN8 亦存在同名訊號（`TELEMATIC_FD_4`／`BCM_FD_2`），
**採 BH-CAN 側**（PM 既有 message 全屬 BH-CAN）。

**未解析（11 種，193 次）**

`Phone_Call.Info`(41)、`Antitheft_Activation.Req`(39)、
`Auto_SwitchOn_Setting.Req`(34)、`Antitheft_Result.Info`(25)、
`SwitchOff_Timeout_Setting.Req`(16)、`Front_Panel_OnOff.Req`(13)、
`Rear_Camera_Enable.Info`(11)、`SwitchOffSetting.Req`(5)、
`TLM_Display.GUI`(2)、`Audio_Data_Exchange.Info`(1)

處置：多屬 HMI 設定項或使用者操作結果，依 (d) 改以 HMI 可觀察現象
書寫（該列 ER 多已載明可觀察結果，可直接回用）；仍無法判定者標
`PENDING: DR-{n}`。**不得逕自保留內部訊號名。**

## 四、對已交付內容之影響

PM 步驟 127 行含內部訊號、ER 側亦有 —— 全數依 §三改寫。
`TLM_Status.Info` 一項即涵蓋 177 次，為最大宗且已有精確對應。

R-6／R-6b 維持：verbatim 上半不動。
R-7 維持：Procedure 強制標籤、ER 選用。
