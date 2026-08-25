# W-VF70 —— 事實抽不出之逐條表（取代 W-VF69 版）

候選 554（選池 574 − pilot 20）逐條抽事實，**抽不出 50 條**。

**與 W-VF69 版之差**：首報 77 條，其中 **7 條為抽取式過窄所致之假缺陷**
（值之終點由散文界定），已於本輪回收；A 類 46 條改由分級 `B8-signal-incomplete` 排除。

| 類 | 條數 |
|---|---|
| A' 抽不出訊號名（含純 propId 式） | **27** |
| B PROXI 無值或無參數名 | **11** |
| C 條文之值對不上 DBC 值域 | **8** |
| D 其他 | **4** |

> C 類之逐條成因見 `vf230_wvf70_cclass.md`。
> 另有 **128 條**依 R-VF81 三列入隔離（未指名值且無語意對應，DR-39）——
> 其非「抽不出」，而是**抽得出而不得取值**，故不在本表。

---

## A' 抽不出訊號名（含純 propId 式）（27 條）

| leaf | 形態 | writability | 缺何項 |
|---|---|---|---|
| `SWE1-VC-CorneringLights-004` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-CorneringLights-005` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-ForwardCollisionWarning-036` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-ForwardCollisionWarning-037` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-ForwardCollisionWarning-038` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-ForwardCollisionWarningSensitivity-043` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-ForwardCollisionWarningSensitivity-044` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-ForwardCollisionWarningSensitivity-045` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-GreetingLights-010` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-GreetingLights-011` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-LaneSenseStrength-029` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-LaneSenseStrength-030` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-LaneSenseStrength-031` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-LaneSenseWarning-016` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-LaneSenseWarning-017` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-LaneSenseWarning-018` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-PedestrianEmergencyBrakingorWarning&ActiveBraking-050` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-PedestrianEmergencyBrakingorWarning&ActiveBraking-051` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-RainSensingWipers-056` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-RainSensingWipers-057` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-SignatureLighting-023` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-SignatureLighting-024` | 訊號送出型 | W0 | 訊號送出型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-SuspensionDefaultRideHeight-020` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - NAFTASetting-059` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - NAFTASetting-072` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - non-NAFTASetting-093` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - non-NAFTASetting-101` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
## B PROXI 無值或無參數名（11 條）

| leaf | 形態 | writability | 缺何項 |
|---|---|---|---|
| `SWE1-VC-4AUXSwitches-027` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-ChargePowerLevel-044` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-ChargePowerLevel-045` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-ConsumptionUnit-032` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-EngineOffPowerDelay-044` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-EngineOffPowerDelay-045` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-Language-060` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-RearSeatReminder-053` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-RearSeatReminder-054` | PROXI 型 | W0 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraView-065` | PROXI 型 | W0 | PROXI 型而抽不出參數名（無 `retrieve the … configuration`） |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraView-066` | PROXI 型 | W0 | PROXI 型而抽不出參數名（無 `retrieve the … configuration`） |
## C 條文之值對不上 DBC 值域（8 條）

| leaf | 形態 | writability | 缺何項 |
|---|---|---|---|
| `SWE1-VC-DaytimeRunningLights-005` | 訊號送出型 | W0 | 條文指名之值 `Early] to CarPropertySer` 對不上 `DRLEnable_Req` 之 DBC 值域 ['False', 'True'] —— 不臆造 |
| `SWE1-VC-EngineOffPowerDelay-047` | 訊號送出型 | W0 | 條文指名之值 `Forty_Five_Sec] to CarPr` 對不上 `Eng_Off_Pwr_Delay_Req` 之 DBC 值域 ['Five_Min', 'Fourty_Five_Sec', 'Ten_Mi |
| `SWE1-VC-PowerTailgate-025` | 訊號送出型 | W0 | 條文指名之值 `Disable] to CarPropertyS` 對不上 `Power_Tailgate_Enable_Req` 之 DBC 值域 ['Disabled', 'Enabled'] —— 不臆造 |
| `SWE1-VC-PowerTailgate-026` | 訊號送出型 | W0 | 條文指名之值 `Enable] to CarPropertySe` 對不上 `Power_Tailgate_Enable_Req` 之 DBC 值域 ['Disabled', 'Enabled'] —— 不臆造 |
| `SWE1-VC-TrailerBrakeType032` | 訊號送出型 | W0 | 條文指名之值 `One. CarPropertyService ` 對不上 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hy |
| `SWE1-VC-TrailerBrakeType033` | 訊號送出型 | W0 | 條文指名之值 `Two. CarPropertyService ` 對不上 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hy |
| `SWE1-VC-TrailerBrakeType034` | 訊號送出型 | W0 | 條文指名之值 `Three. CarPropertyServic` 對不上 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hy |
| `SWE1-VC-TrailerBrakeType035` | 訊號送出型 | W0 | 條文指名之值 `Four. CarPropertyService` 對不上 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hy |
## D 其他（4 條）

| leaf | 形態 | writability | 缺何項 |
|---|---|---|---|
| `SWE1-VC-TimeandDateSettings-003` | 其他 | W0 | 形態 `其他` 無對應之書寫式（未經 pilot） |
| `SWE1-VC-TimeandDateSettings-006` | 其他 | W0 | 形態 `其他` 無對應之書寫式（未經 pilot） |
| `SWE1-VC-TimeandDateSettings-007` | 其他 | W0 | 形態 `其他` 無對應之書寫式（未經 pilot） |
| `SWE1-VC-TimeandDateSettings-008` | 其他 | W0 | 形態 `其他` 無對應之書寫式（未經 pilot） |
