# W-VF69 —— 量產母體中事實抽不出之 77 條

母體 574（R-VF77 二）逐條抽事實後，**497 條可書寫、77 條缺必要事實**。
本表逐條列之。**其未生成任何 TC**，亦未被自檢涵蓋 —— 一條未生成之 TC 不會出現在任何違規數內。

| 類 | 條數 |
|---|---|
| A 只有 message、無訊號名 | **46** |
| B PROXI 無值或無參數名 | **11** |
| C 條文之值不在該訊號之 DBC 值域內 | **15** |
| D 其他 | **5** |

---

## A 只有 message、無訊號名（46 條）

| leaf | 形態 | writability | 缺何項 |
|---|---|---|---|
| `SWE1-VC-AutoDoorLocks-017` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-AutoDoorLocks-018` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-AutoDoorLocks-019` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ConsumptionUnit-033` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ConsumptionUnit-034` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ConsumptionUnit-035` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ConsumptionUnit-036` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ConsumptionUnit-037` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-DistanceUnit-022` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-DistanceUnit-023` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-DistanceUnit-024` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-HourMode-011` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-HourMode-012` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-HourMode-013` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ParkSense-086` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ParkSense-087` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ParkSense-088` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ParkSenseBasedCameraActivation-081` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_FD_1`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-ParkSenseBasedCameraActivation-082` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP2`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SpeedUnit-027` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SpeedUnit-028` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SpeedUnit-029` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SurroundViewCameraDelay-055` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SurroundViewCameraDelay-056` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SurroundViewCameraDelay-057` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SurroundViewCameraGuidelines-061` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SurroundViewCameraGuidelines-062` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SurroundViewCameraGuidelines-063` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SuspensionAutoEntryorExit-093` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SuspensionAutoEntryorExit-094` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-SuspensionAutoEntryorExit-095` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TemperatureUnit-048` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TemperatureUnit-049` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TemperatureUnit-050` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraView-067` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_FD_1`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraView-068` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_FD_1`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraView-069` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP2`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraViewwithTrailerOption-073` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_FD_1`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraViewwithTrailerOption-074` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_FD_1`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraViewwithTrailerOption-075` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_FD_1`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraViewwithTrailerOption-076` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP2`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-UnitEnergy-040` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-UnitEnergy-041` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-UnitEnergy-042` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-UnitEnergy-043` | 訊號送出型 | W0 | 訊號送出型 而條文**只有 message `TELEMATIC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
| `SWE1-VC-UnitEnergy-044` | 訊號上行型 | W0 | 訊號上行型 而條文**只有 message `IPC_VEHICLE_SETUP`、無訊號名** —— 不以 DBC 值域反解（多解者佔半），列 DR |
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
| `SWE1-VC-RearSeatReminder-053` | PROXI 型 | W1 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-RearSeatReminder-054` | PROXI 型 | W1 | PROXI 型而條文未帶值（無 `If … = [ … ]`，亦無 `receives the value … via signal`） |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraView-065` | PROXI 型 | W0 | PROXI 型而抽不出參數名（無 `retrieve the … configuration`） |
| `SWE1-VC-TurnSignalActivatedBlindSpotCameraView-066` | PROXI 型 | W0 | PROXI 型而抽不出參數名（無 `retrieve the … configuration`） |
## C 條文之值不在該訊號之 DBC 值域內（15 條）

| leaf | 形態 | writability | 缺何項 |
|---|---|---|---|
| `SWE1-VC-DaytimeRunningLights-005` | 訊號送出型 | W0 | 條文指名之值 `Early` 不在 `DRLEnable_Req` 之 DBC 值域 ['False', 'True'] 內 —— 不臆造 |
| `SWE1-VC-EngineOffPowerDelay-047` | 訊號送出型 | W0 | 條文指名之值 `Forty_Five_Sec` 不在 `Eng_Off_Pwr_Delay_Req` 之 DBC 值域 ['Five_Min', 'Fourty_Five_Sec', 'Ten_Min', 'Zero'] 內 —— 不臆造 |
| `SWE1-VC-HornWithLock-036` | 訊號送出型 | W0 | 條文指名之值 `1st` 不在 `SoundHornLock_Req` 之 DBC 值域 ['1st Press', '2nd Press', 'Off'] 內 —— 不臆造 |
| `SWE1-VC-HornWithLock-037` | 訊號送出型 | W0 | 條文指名之值 `2nd` 不在 `SoundHornLock_Req` 之 DBC 值域 ['1st Press', '2nd Press', 'Off'] 內 —— 不臆造 |
| `SWE1-VC-Language-061` | 訊號送出型 | W0 | 條文指名之值 `selected` 不在 `LanguageSelection_Req` 之 DBC 值域 ['Arabic', 'Brazilian', 'Canadian', 'Chinese', 'Czech', 'Deutsch', 'Dutch', 'English', 'English_US', 'Espanol', 'Francais', 'Hindi', 'Hungarian', 'Italian', 'Japanese', 'Korean', 'Mexican', 'Polish', 'Portugues', 'Russian', 'Slovakian', 'Turkish'] 內 —— 不臆造 |
| `SWE1-VC-MaxPowerLevel141` | 訊號送出型 | W0 | 條文指名之值 `Level` 不在 `SOC_Max_Lev_Req` 之 DBC 值域 ['Level1', 'Level2'] 內 —— 不臆造 |
| `SWE1-VC-MaxPowerLevel142` | 訊號送出型 | W0 | 條文指名之值 `Level` 不在 `SOC_Max_Lev_Req` 之 DBC 值域 ['Level1', 'Level2'] 內 —— 不臆造 |
| `SWE1-VC-PowerTailgate-025` | 訊號送出型 | W0 | 條文指名之值 `Disable` 不在 `Power_Tailgate_Enable_Req` 之 DBC 值域 ['Disabled', 'Enabled'] 內 —— 不臆造 |
| `SWE1-VC-PowerTailgate-026` | 訊號送出型 | W0 | 條文指名之值 `Enable` 不在 `Power_Tailgate_Enable_Req` 之 DBC 值域 ['Disabled', 'Enabled'] 內 —— 不臆造 |
| `SWE1-VC-RearviewCameraDynamicGuidelines-117` | 訊號送出型 | W0 | 條文指名之值 `Dynamic` 不在 `DynamicGrid_Req` 之 DBC 值域 ['Dynamic Gridlines OFF', 'Dynamic Gridlines ON'] 內 —— 不臆造 |
| `SWE1-VC-RearviewCameraDynamicGuidelines-118` | 訊號送出型 | W0 | 條文指名之值 `Dynamic` 不在 `DynamicGrid_Req` 之 DBC 值域 ['Dynamic Gridlines OFF', 'Dynamic Gridlines ON'] 內 —— 不臆造 |
| `SWE1-VC-TrailerBrakeType032` | 訊號送出型 | W0 | 條文指名之值 `One` 不在 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric', 'Light_Electric_Over_Hydraulic'] 內 —— 不臆造 |
| `SWE1-VC-TrailerBrakeType033` | 訊號送出型 | W0 | 條文指名之值 `Two` 不在 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric', 'Light_Electric_Over_Hydraulic'] 內 —— 不臆造 |
| `SWE1-VC-TrailerBrakeType034` | 訊號送出型 | W0 | 條文指名之值 `Three` 不在 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric', 'Light_Electric_Over_Hydraulic'] 內 —— 不臆造 |
| `SWE1-VC-TrailerBrakeType035` | 訊號送出型 | W0 | 條文指名之值 `Four` 不在 `Trail_Brk_Type_Req` 之 DBC 值域 ['Heavy_Electric', 'Heavy_Electric_Over_Hydraulic', 'Light_Electric', 'Light_Electric_Over_Hydraulic'] 內 —— 不臆造 |
## D 其他（5 條）

| leaf | 形態 | writability | 缺何項 |
|---|---|---|---|
| `SWE1-VC-SuspensionDefaultRideHeight-020` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - NAFTASetting-059` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - NAFTASetting-072` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - non-NAFTASetting-093` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
| `SWE1-VC-TrafficSignAssistOffset - non-NAFTASetting-101` | 訊號上行型 | W0 | 訊號上行型 而抽不出 `TELEMATIC_*`／`IPC_*` 訊號名 |
