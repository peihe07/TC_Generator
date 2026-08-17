# G28 — `Verification Criteria` / `Verification Method` 可執行性（R-P49）

> 判準見 06 下放包 §D 之 G28。本閘**不設期望值，首次量測即為基線**。
> 具體性訊號為明列正則（見 `scripts/build_vcvm.py` 之 `SIGNALS`）；
> 邊界個案以 `OVERRIDES` 人工覆寫，隨腳本版控並附理由。
> 產生指令：`python features/power/scripts/build_vcvm.py`

## 1. 基線

| 判定層 | 可執行 | 不可執行 | 母體 |
|---|---|---|---|
| `Verification Criteria` 單欄 | 113 | **2** | 115 |
| `Verification Method` 單欄 | 115 | **0** | 115 |
| **二欄合觀（Phase 4 之實際輸入）** | 115 | **0** | 115 |

二欄合觀之判定規則：任一欄可執行即為可執行 —— 一欄泛稱而另一欄具體者，TC 作者仍有可操作之依據。

## 2.1 `Verification Criteria` 判定為不可執行者（2 個）

| leaf | Test Set | 欄位全文 | 判定依據 |
|---|---|---|---|
| `SWE-PM-007` | Power State | Vehicle not equiped with CAN or engineering line is active | 「Vehicle not equiped with CAN or engineering line is active」—— `CAN` 雖為全大寫 token 而命中「具名訊號／參數」，但此處僅為總線之泛稱，非可設定之訊號；「engineering line is active」亦無具名訊號或設定值。全句無任何可操作之條件，與判準所舉之反例同型。 |
| `SWE-PM-008` | Power State | Vehicle equiped with CAN | 「Vehicle equiped with CAN」—— **判準所舉之反例本身**。`CAN` 為總線泛稱，全句無任何可操作條件。 |

## 2.2 `Verification Method` 判定為不可執行者（0 個）

（無）

## 3. 二欄合觀為不可執行者（0 個）

**（無）** —— 每個 leaf 至少有一欄含具體性訊號。

## 4. 逐 leaf 明細（依據字串）

| leaf | VC 判定 | VC 命中訊號（依據字串） | VM 判定 | VM 命中訊號（依據字串） |
|---|---|---|---|---|
| `SWE-PM-001` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名訊號／參數=`AACP`；具名元件／畫面=`HU`；操作動詞=`Change` |
| `SWE-PM-002` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`ADAS`；具名元件／畫面=`panel` |
| `SWE-PM-003` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名訊號／參數=`STATUS_BH_BCM2`；引號字面值=`"Remote Start Active"`；操作動詞=`Change` |
| `SWE-PM-004` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`SWITCH_OFF_DOOR`；具名元件／畫面=`HU`；具名狀態=`Timed`；操作動詞=`Change` |
| `SWE-PM-005` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名訊號／參數=`$Telematic_Power$`；引號字面值=`"Standby"`；具名元件／畫面=`Splash`；具名狀態=`Standby` |
| `SWE-PM-006` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名元件／畫面=`HU` |
| `SWE-PM-007` | 不可執行 | — | 可執行 | 具名元件／畫面=`HU`；操作動詞=`Change` |
| `SWE-PM-008` | 不可執行 | — | 可執行 | 具名訊號／參數=`STATUS_BH_BCM1`；引號字面值=`"Logistic_Mode_On"`；具名元件／畫面=`HU`；操作動詞=`Change` |
| `SWE-PM-009` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full operation` | 可執行 | — |
| `SWE-PM-010` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full operation` | 可執行 | 具體數值=`6 sec`；具名元件／畫面=`HU` |
| `SWE-PM-011` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Idle` | 可執行 | 具名元件／畫面=`button`；具名狀態=`Full-Operation` |
| `SWE-PM-012` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`SwitchOffSetting.Req`；引號字面值=`'Sleep'`；具名狀態=`Sleep` |
| `SWE-PM-013` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`sleep` | 可執行 | 引號字面值=`'Remote Start Active'`；具名元件／畫面=`TLM`；操作動詞=`Trigger` |
| `SWE-PM-014` | 可執行 | 引號字面值=`"Full-Operation"`；具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`Phone_Call`；具名狀態=`Standby`；操作動詞=`trigger` |
| `SWE-PM-015` | 可執行 | 引號字面值=`"Full-Operation"`；具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`Phone_Call`；具名元件／畫面=`ICS`；具名狀態=`Idle`；操作動詞=`press` |
| `SWE-PM-016` | 可執行 | 引號字面值=`"Full-Operation"`；具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`Rear_Camera_Enable`；具名狀態=`Full-Operation` |
| `SWE-PM-017` | 可執行 | 引號字面值=`"Full-Operation"`；具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`Audio_Data_Exchange`；操作動詞=`change` |
| `SWE-PM-018` | 可執行 | 引號字面值=`"Idle"`；具名元件／畫面=`HU`；具名狀態=`Idle` | 可執行 | 具名訊號／參數=`LTM_OperationalModeSts`；引號字面值=`'Ignition Pre Off'`；具名元件／畫面=`TLM`；具名狀態=`Idle`；操作動詞=`Set` |
| `SWE-PM-019` | 可執行 | 引號字面值=`"Idle"`；具名元件／畫面=`HU`；具名狀態=`Idle` | 可執行 | 具名訊號／參數=`Response_Wait_Time`；具名元件／畫面=`ICS`；具名狀態=`Idle`；操作動詞=`press` |
| `SWE-PM-020` | 可執行 | 引號字面值=`"Idle"`；具名元件／畫面=`HU`；具名狀態=`Idle` | 可執行 | 具名訊號／參數=`Phone_Call`；具名元件／畫面=`Screen`；具名狀態=`Idle` |
| `SWE-PM-021` | 可執行 | 具名訊號／參數=`PROXI`；引號字面值=`"Idle"`；具名元件／畫面=`HU`；具名狀態=`Idle` | 可執行 | 具名訊號／參數=`Rear_Camera_Enable`；具名元件／畫面=`TLM`；具名狀態=`Idle`；操作動詞=`Set` |
| `SWE-PM-022` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-operation` | 可執行 | 具名訊號／參數=`PowerModeSts_Telematic`；引號字面值=`'Logistic_Mode_On'`；具名狀態=`Idle`；操作動詞=`trigger` |
| `SWE-PM-023` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名訊號／參數=`LTM_OperationalModeSts`；引號字面值=`'Ignition Off'`；具名元件／畫面=`TLM`；具名狀態=`Timed`；操作動詞=`Set` |
| `SWE-PM-024` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名訊號／參數=`LTM_OperationalModeSts`；引號字面值=`'Ignition Off'`；具名元件／畫面=`TLM`；具名狀態=`Timed`；操作動詞=`Set` |
| `SWE-PM-025` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名元件／畫面=`ICS`；具名狀態=`Timed`；操作動詞=`press` |
| `SWE-PM-026` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名狀態=`Timed`；操作動詞=`change` |
| `SWE-PM-027` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名訊號／參數=`Not_Successful`；具名元件／畫面=`screen`；具名狀態=`Standby` |
| `SWE-PM-028` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具體數值=`00 min`；具名元件／畫面=`button`；具名狀態=`Standby`；操作動詞=`press` |
| `SWE-PM-029` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名元件／畫面=`button`；具名狀態=`Standby`；操作動詞=`press` |
| `SWE-PM-030` | 可執行 | 具名訊號／參數=`$RemoteStartActive$`；引號字面值=`"Not_active"`；具名元件／畫面=`HU`；具名狀態=`standby` | 可執行 | 具名訊號／參數=`Auto_SwitchOn`；具名元件／畫面=`Splash`；具名狀態=`Standby` |
| `SWE-PM-031` | 可執行 | 具名訊號／參數=`PROXI`；引號字面值=`"Present"` | 可執行 | 具名訊號／參數=`Rear_Camera_Enable`；具名狀態=`Idle` |
| `SWE-PM-032` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Standby` | 可執行 | 具名狀態=`Standby`；操作動詞=`trigger` |
| `SWE-PM-033` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Partial operation` | 可執行 | 具名訊號／參數=`LTM_OperationalModeSts`；引號字面值=`'Ignition Pre Off'`；具名元件／畫面=`TLM`；具名狀態=`Partial Operation`；操作動詞=`Set` |
| `SWE-PM-034` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Partial operation` | 可執行 | 具名訊號／參數=`Response_Wait_Time`；具名元件／畫面=`ICS`；具名狀態=`Partial Operation`；操作動詞=`press` |
| `SWE-PM-035` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Partial operation` | 可執行 | 具名訊號／參數=`Auto_SwitchOn`；具名元件／畫面=`Splash`；具名狀態=`Idle` |
| `SWE-PM-036` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名元件／畫面=`TLM`；具名狀態=`Timed`；操作動詞=`Set` |
| `SWE-PM-037` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名狀態=`Timed` |
| `SWE-PM-038` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名狀態=`Standby` |
| `SWE-PM-039` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-Operation` | 可執行 | 具名訊號／參數=`LTM_OperationalModeSts`；引號字面值=`'SNA'`；具名元件／畫面=`TLM`；具名狀態=`Idle`；操作動詞=`Trigger` |
| `SWE-PM-040` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`sleep` | 可執行 | 操作動詞=`Trigger` |
| `SWE-PM-041` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名訊號／參數=`Antitheft_Activation`；引號字面值=`'False'`；具名元件／畫面=`TLM`；具名狀態=`Ignition Pre Off`；操作動詞=`Trigger` |
| `SWE-PM-042` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`sleep` | 可執行 | 具名元件／畫面=`TLM`；具名狀態=`Ignition Pre Off`；操作動詞=`Trigger` |
| `SWE-PM-043` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`standby` | 可執行 | 具名狀態=`Standby`；操作動詞=`Trigger` |
| `SWE-PM-044` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名訊號／參數=`Response_Wait_Time`；具名元件／畫面=`ICS`；具名狀態=`Standby` |
| `SWE-PM-045` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名訊號／參數=`Not_Successful`；具名元件／畫面=`button`；具名狀態=`Standby`；操作動詞=`Trigger` |
| `SWE-PM-046` | 可執行 | 具名訊號／參數=`$RemoteStartActive$`；引號字面值=`"Not_active"`；具名元件／畫面=`HU`；具名狀態=`standby` | 可執行 | 具名訊號／參數=`In_Progress`；具名元件／畫面=`display`；操作動詞=`Trigger` |
| `SWE-PM-047` | 可執行 | 具名訊號／參數=`$RemoteStartActive$`；引號字面值=`"Not_active"`；具名元件／畫面=`HU`；具名狀態=`standby` | 可執行 | 具名訊號／參數=`Not_Successful`；具名元件／畫面=`screen`；具名狀態=`Standby`；操作動詞=`Trigger` |
| `SWE-PM-048` | 可執行 | 具名訊號／參數=`$RemoteStartActive$`；引號字面值=`"Not_active"`；具名元件／畫面=`HU`；具名狀態=`standby` | 可執行 | 具名訊號／參數=`Auto_SwitchOn`；具名狀態=`Idle` |
| `SWE-PM-049` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Logistic` | 可執行 | 具名訊號／參數=`Not_Successful`；具名元件／畫面=`screen`；具名狀態=`Logistic`；操作動詞=`Trigger` |
| `SWE-PM-050` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Logistic` | 可執行 | 具名狀態=`Logistic`；操作動詞=`exit` |
| `SWE-PM-051` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Partial operation` | 可執行 | 引號字面值=`'On'`；具名元件／畫面=`ICS`；具名狀態=`Full-Operation`；操作動詞=`set` |
| `SWE-PM-052` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Sleep` | 可執行 | 具名訊號／參數=`Not_Successful`；具名元件／畫面=`screen`；操作動詞=`trigger` |
| `SWE-PM-053` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`idle` | 可執行 | 具名狀態=`suspend resume` |
| `SWE-PM-054` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`idle` | 可執行 | 具名元件／畫面=`splash`；具名狀態=`suspend resume` |
| `SWE-PM-055` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`idle` | 可執行 | 具名元件／畫面=`Splash`；具名狀態=`suspend resume` |
| `SWE-PM-056` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`idle` | 可執行 | 具名狀態=`suspend resume` |
| `SWE-PM-057` | 可執行 | 具名訊號／參數=`Switch_Off_Time`；具體數值=`180 minutes`；引號字面值=`"Switch_Off_Time"`；操作動詞=`set` | 可執行 | 具體數值=`00 min`；具名元件／畫面=`HU`；具名狀態=`Timed`；操作動詞=`select` |
| `SWE-PM-058` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full-Operation` | 可執行 | 具名訊號／參數=`SwitchOff_Timeout_Settin`；具體數值=`00 MIN`；操作動詞=`Change` |
| `SWE-PM-059` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full-Operation` | 可執行 | 具名訊號／參數=`TLM_Status`；具名狀態=`Sleep`；操作動詞=`Send` |
| `SWE-PM-060` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full-Operation` | 可執行 | 具名訊號／參數=`Auto_SwitchOn_Setting`；操作動詞=`select` |
| `SWE-PM-061` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full-Operation` | 可執行 | 具名訊號／參數=`Auto_SwitchOn_Setting`；操作動詞=`select` |
| `SWE-PM-062` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full-Operation` | 可執行 | 具名訊號／參數=`Auto_SwitchOn_Setting`；引號字面值=`"active"`；具名元件／畫面=`menu`；操作動詞=`select` |
| `SWE-PM-063` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 具名狀態=`Timed` |
| `SWE-PM-064` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | 操作動詞=`set` |
| `SWE-PM-065` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Timed` | 可執行 | — |
| `SWE-PM-066` | 可執行 | 具名元件／畫面=`HU` | 可執行 | 具名元件／畫面=`HMI` |
| `SWE-PM-067` | 可執行 | 具名元件／畫面=`HU` | 可執行 | 具名元件／畫面=`HU` |
| `SWE-PM-068` | 可執行 | 具名訊號／參數=`IDLE`；具名元件／畫面=`HU`；具名狀態=`IDLE` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-Operation` |
| `SWE-PM-069` | 可執行 | 具名訊號／參數=`IDLE`；具名元件／畫面=`HU`；具名狀態=`IDLE` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-Operation` |
| `SWE-PM-070` | 可執行 | 具名訊號／參數=`IDLE`；具名元件／畫面=`HU`；具名狀態=`IDLE` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full-Operation`；操作動詞=`Press` |
| `SWE-PM-071` | 可執行 | 具名訊號／參數=`SplashScreen_Time`；具名元件／畫面=`Splash`；具名狀態=`Standby` | 可執行 | — |
| `SWE-PM-072` | 可執行 | 具名訊號／參數=`TLM_Status`；具名元件／畫面=`TLM` | 可執行 | — |
| `SWE-PM-073` | 可執行 | 具名訊號／參數=`PN14_LS_Actv`；具體數值=`10 sec`；具名元件／畫面=`TLM`；具名狀態=`TIMED` | 可執行 | 具名訊號／參數=`STATUS_LIN`；具體數值=`10 sec`；具名元件／畫面=`HMI` |
| `SWE-PM-074` | 可執行 | 具名訊號／參數=`FOTA`；具名元件／畫面=`TLM` | 可執行 | 具名訊號／參數=`FOTA`；具名元件／畫面=`HU`；具名狀態=`Timed` |
| `SWE-PM-075` | 可執行 | 具名訊號／參數=`FOTA`；具名元件／畫面=`TLM` | 可執行 | 具名訊號／參數=`FOTA`；具體數值=`1 min`；具名元件／畫面=`HU`；具名狀態=`Timed` |
| `SWE-PM-076` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full-operation` | 可執行 | 具體數值=`10 seconds`；具名元件／畫面=`button`；操作動詞=`Trigger` |
| `SWE-PM-077` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full-operation` | 可執行 | 具名訊號／參數=`$VC_SpecialPKG$`；具名元件／畫面=`HU` |
| `SWE-PM-078` | 可執行 | 具名訊號／參數=`$VC_SpecialPKG$` | 可執行 | 具名訊號／參數=`$VC_SpecialPKG$`；具名元件／畫面=`HU`；操作動詞=`Set` |
| `SWE-PM-079` | 可執行 | 具名訊號／參數=`$VC_SpecialPKG$` | 可執行 | 具名元件／畫面=`HU` |
| `SWE-PM-080` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Full operation` | 可執行 | 具名訊號／參數=`$Radio_Theme$`；具名元件／畫面=`HU`；操作動詞=`Change` |
| `SWE-PM-081` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名元件／畫面=`HU`；操作動詞=`apply` |
| `SWE-PM-082` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名元件／畫面=`icon` |
| `SWE-PM-083` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名元件／畫面=`screen` |
| `SWE-PM-084` | 可執行 | 具名訊號／參數=`$VC_VEH_LINE$`；操作動詞=`set` | 可執行 | 具名訊號／參數=`CUSW`；具名元件／畫面=`icon`；操作動詞=`change` |
| `SWE-PM-085` | 可執行 | 具名訊號／參數=`$VC_VEH_LINE$`；操作動詞=`set` | 可執行 | 具名訊號／參數=`CUSW`；具名元件／畫面=`HMI`；操作動詞=`change` |
| `SWE-PM-086` | 可執行 | 具名元件／畫面=`Hu`；具名狀態=`Full operation` | 可執行 | 具名訊號／參數=`$Radio_Theme$`；具名元件／畫面=`HU`；操作動詞=`Change` |
| `SWE-PM-087` | 可執行 | 具名訊號／參數=`$VC_VEH_LINE$`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$VC_VEH_LINE$`；操作動詞=`Set` |
| `SWE-PM-088` | 可執行 | 具名訊號／參數=`$VC_VEH_LINE$`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$VC_VEH_LINE$`；具名元件／畫面=`HMI`；操作動詞=`set` |
| `SWE-PM-089` | 可執行 | 具名狀態=`Ignition On`；操作動詞=`Set` | 可執行 | 具名狀態=`Ignition On`；操作動詞=`Set` |
| `SWE-PM-090` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full operation` | 可執行 | 具名訊號／參數=`$Day_Night_Mode$`；引號字面值=`"Theme Mode"`；操作動詞=`Set` |
| `SWE-PM-091` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full operation` | 可執行 | 具名訊號／參數=`$Day_Night_Mode$`；引號字面值=`"Theme Mode"`；具名元件／畫面=`HU`；操作動詞=`Set` |
| `SWE-PM-092` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`full operation` | 可執行 | 具名訊號／參數=`$Day_Night_Mode$`；引號字面值=`"Theme Mode"`；具名元件／畫面=`HU`；操作動詞=`Set` |
| `SWE-PM-093` | 可執行 | 具名元件／畫面=`HU` | 可執行 | 具名訊號／參數=`CLOSED`；具體數值=`30 min`；具名狀態=`Sleep` |
| `SWE-PM-094` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`suspend-resume` | 可執行 | 具名元件／畫面=`Splash` |
| `SWE-PM-095` | 可執行 | 具名訊號／參數=`LTM_OperationalModeSts`；具名狀態=`Timed` | 可執行 | 具名訊號／參數=`$OperationalModeSts$`；操作動詞=`Set` |
| `SWE-PM-096` | 可執行 | 具名狀態=`suspend-resume` | 可執行 | 具名狀態=`Ignition On`；操作動詞=`Set` |
| `SWE-PM-097` | 可執行 | 引號字面值=`'Startup Animation Selec`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`$VC_Veh_Brand$`；引號字面值=`'Startup Animation Selec`；操作動詞=`Set` |
| `SWE-PM-098` | 可執行 | 具名訊號／參數=`$Themed_Sound$`；引號字面值=`'Welcome Onboard Sound'`；具名狀態=`suspend-resume`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$Themed_Sound$`；引號字面值=`'Always'`；操作動詞=`trigger` |
| `SWE-PM-099` | 可執行 | 具名訊號／參數=`$Themed_Sound$`；引號字面值=`'Welcome Onboard Sound'`；具名狀態=`suspend-resume`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$Themed_Sound$`；操作動詞=`change` |
| `SWE-PM-100` | 可執行 | 具名訊號／參數=`$Themed_Sound$`；引號字面值=`'Welcome Onboard Sound'`；具名狀態=`suspend-resume`；操作動詞=`set` | 可執行 | 具名訊號／參數=`$Themed_Sound$`；引號字面值=`'Never'`；操作動詞=`trigger` |
| `SWE-PM-101` | 可執行 | 具名訊號／參數=`$SDARS_Presence$`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`SDARS` |
| `SWE-PM-102` | 可執行 | 具名訊號／參數=`$VC_MODEL_YEAR$`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`$VC_MODEL_YEAR$`；具名元件／畫面=`splash` |
| `SWE-PM-103` | 可執行 | 具名狀態=`Ignition On` | 可執行 | 具名元件／畫面=`Splash`；具名狀態=`Ignition On`；操作動詞=`Trigger` |
| `SWE-PM-104` | 可執行 | 具名狀態=`suspend-resume` | 可執行 | 具名元件／畫面=`Splash`；具名狀態=`Timed` |
| `SWE-PM-105` | 可執行 | 具名訊號／參數=`Phone_Call`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`FOTA`；具名元件／畫面=`Splash`；具名狀態=`Timed` |
| `SWE-PM-106` | 可執行 | 具名訊號／參數=`$Ecall_Button_Variant$`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`$Ecall_Button_Variant$`；具名元件／畫面=`display`；操作動詞=`Set` |
| `SWE-PM-107` | 可執行 | 具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`$Ecall_Button_Variant$`；引號字面值=`'SOS'`；具名元件／畫面=`display`；操作動詞=`Set` |
| `SWE-PM-108` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；操作動詞=`trigger` |
| `SWE-PM-109` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`GDPR` |
| `SWE-PM-110` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`GDPR` |
| `SWE-PM-111` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名元件／畫面=`screen`；具名狀態=`suspend-resume` | 可執行 | 具名訊號／參數=`ADAS`；具名元件／畫面=`Screen` |
| `SWE-PM-112` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名元件／畫面=`Screen` | 可執行 | 具名訊號／參數=`ADAS`；具名元件／畫面=`Screen` |
| `SWE-PM-113` | 可執行 | 具名訊號／參數=`$VC_VEH_BRAND$`；具名元件／畫面=`Screen` | 可執行 | 具名訊號／參數=`ADAS`；具名元件／畫面=`Screen` |
| `SWE-PM-114` | 可執行 | 具名元件／畫面=`HU` | 可執行 | 具名訊號／參數=`Phone_Call`；具名狀態=`Idle` |
| `SWE-PM-115` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Idle` | 可執行 | 具名元件／畫面=`HU`；具名狀態=`Idle` |
