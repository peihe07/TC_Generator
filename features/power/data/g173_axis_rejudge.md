# G173 —— `axis` 全批重判提案（R-P248）

> **本檔只出提案，不改值**（R-P248(d)）。
> §4.6 之六值：`trigger_state`、`input_data`、`timing`、`boundary`、`mode`、`none`。
> 判準為**結構差異**而非 `delta` 之散文 —— 理由見腳本首段（R-P250 之量測）。

## 一、現行違規（G173）

現行 `axis` 不在六值內者 **227 / 264**：

| 現行值 | 條數 | 合法 |
|---|---|---|
| `behaviour` | 219 | **否** |
| `mode` | 20 | 是 |
| `trigger_state` | 11 | 是 |
| `timing` | 5 | 是 |
| `branch` | 5 | **否** |
| `trigger` | 3 | **否** |
| `input_data` | 1 | 是 |

## 二、重判提案之分布

| 提案 axis | 條數 |
|---|---|
| `input_data` | **92** |
| `trigger_state` | **68** |
| `mode` | **42** |
| `**無對應**` | **40** |
| `timing` | **17** |
| `boundary` | **5** |

## 三、無可映者 —— **40** 條

> 六值皆預設「與他條之區分」，而該 leaf 僅產出 1 條 TC，無他條可區分。
> **不新增列舉值**（R-P248(b)）；處置屬分析層。

| tc | leaf | 現行 axis |
|---|---|---|
| `…-028` | `SWE-PM-063` | `behaviour` |
| `…-071` | `SWE-PM-016` | `behaviour` |
| `…-072` | `SWE-PM-017` | `behaviour` |
| `…-082` | `SWE-PM-021` | `behaviour` |
| `…-083` | `SWE-PM-022` | `behaviour` |
| `…-084` | `SWE-PM-023` | `behaviour` |
| `…-085` | `SWE-PM-024` | `behaviour` |
| `…-110` | `SWE-PM-031` | `behaviour` |
| `…-111` | `SWE-PM-032` | `behaviour` |
| `…-114` | `SWE-PM-034` | `behaviour` |
| `…-119` | `SWE-PM-036` | `behaviour` |
| `…-120` | `SWE-PM-037` | `behaviour` |
| `…-125` | `SWE-PM-040` | `behaviour` |
| `…-147` | `SWE-PM-049` | `behaviour` |
| `…-148` | `SWE-PM-050` | `behaviour` |
| `…-149` | `SWE-PM-051` | `behaviour` |
| `…-150` | `SWE-PM-052` | `behaviour` |
| `…-151` | `SWE-PM-053` | `behaviour` |
| `…-158` | `SWE-PM-056` | `behaviour` |
| `…-159` | `SWE-PM-058` | `behaviour` |
| `…-164` | `SWE-PM-067` | `behaviour` |
| `…-165` | `SWE-PM-068` | `behaviour` |
| `…-168` | `SWE-PM-070` | `behaviour` |
| `…-187` | `SWE-PM-094` | `behaviour` |
| `…-188` | `SWE-PM-095` | `behaviour` |
| `…-189` | `SWE-PM-097` | `behaviour` |
| `…-190` | `SWE-PM-098` | `behaviour` |
| `…-195` | `SWE-PM-100` | `behaviour` |
| `…-220` | `SWE-PM-106` | `behaviour` |
| `…-221` | `SWE-PM-107` | `behaviour` |
| `…-222` | `SWE-PM-108` | `behaviour` |
| `…-223` | `SWE-PM-109` | `behaviour` |
| `…-228` | `SWE-PM-113` | `behaviour` |
| `…-229` | `SWE-PM-114` | `behaviour` |
| `…-230` | `SWE-PM-115` | `behaviour` |
| `…-231` | `SWE-PM-077` | `behaviour` |
| `…-234` | `SWE-PM-079` | `behaviour` |
| `…-254` | `SWE-PM-088` | `behaviour` |
| `…-257` | `SWE-PM-091` | `behaviour` |
| `…-258` | `SWE-PM-092` | `behaviour` |

## 四、逐條

| tc | leaf | 現行 | 提案 | 依據 |
|---|---|---|---|---|
| `…-001` | `SWE-PM-071` | `mode` | `mode` | 對照 `003`，差異落在運作模式／狀態：`Bench` |
| `…-002` | `SWE-PM-071` | `mode` | `mode` | 對照 `003`，差異落在運作模式／狀態：`Bench` |
| `…-003` | `SWE-PM-071` | `mode` | `mode` | 對照 `002`，差異落在運作模式／狀態：`Bench` |
| `…-004` | `SWE-PM-071` | `timing` | `timing` | 對照 `001`，差異落在時間量／時序：`SplashScreen_Time` |
| `…-005` | `SWE-PM-072` | `input_data` | `input_data` | 對照 `006`，差異為其餘輸入之取值 |
| `…-006` | `SWE-PM-072` | `timing` | `input_data` | 對照 `005`，差異為其餘輸入之取值 |
| `…-007` | `SWE-PM-073` | `trigger_state` | `input_data` | 對照 `016`，差異為其餘輸入之取值 |
| `…-008` | `SWE-PM-073` | `trigger_state` | `trigger_state` | 對照 `011`，差異落在觸發訊號：`STATUS_LIN.PN14_LS_Actv` |
| `…-009` | `SWE-PM-073` | `mode` | `mode` | 對照 `014`，差異落在運作模式／狀態：`OFF` |
| `…-010` | `SWE-PM-073` | `timing` | `timing` | 對照 `015`，差異落在時間量／時序：`window` |
| `…-011` | `SWE-PM-073` | `behaviour` | `input_data` | 對照 `012`，差異為其餘輸入之取值 |
| `…-012` | `SWE-PM-073` | `behaviour` | `trigger_state` | 對照 `013`，差異落在觸發訊號：`STATUS_LIN.Batt_ST_Crit` |
| `…-013` | `SWE-PM-073` | `behaviour` | `trigger_state` | 對照 `012`，差異落在觸發訊號：`STATUS_LIN.Batt_ST_Crit` |
| `…-014` | `SWE-PM-073` | `mode` | `mode` | 對照 `009`，差異落在運作模式／狀態：`OFF` |
| `…-015` | `SWE-PM-073` | `behaviour` | `mode` | 對照 `013`，差異落在運作模式／狀態：`bench` |
| `…-016` | `SWE-PM-073` | `branch` | `input_data` | 對照 `007`，差異為其餘輸入之取值 |
| `…-017` | `SWE-PM-073` | `branch` | `trigger_state` | 對照 `016`，差異落在觸發訊號：`STATUS_LIN.Batt_ST_Crit` |
| `…-018` | `SWE-PM-057` | `behaviour` | `input_data` | 對照 `019`，差異為其餘輸入之取值 |
| `…-019` | `SWE-PM-057` | `behaviour` | `input_data` | 對照 `018`，差異為其餘輸入之取值 |
| `…-020` | `SWE-PM-057` | `behaviour` | `input_data` | 對照 `018`，差異為其餘輸入之取值 |
| `…-021` | `SWE-PM-060` | `behaviour` | `input_data` | 對照 `022`，差異為其餘輸入之取值 |
| `…-022` | `SWE-PM-060` | `behaviour` | `input_data` | 對照 `021`，差異為其餘輸入之取值 |
| `…-023` | `SWE-PM-061` | `mode` | `mode` | 對照 `024`，差異落在運作模式／狀態：`Full-Operation` |
| `…-024` | `SWE-PM-061` | `mode` | `mode` | 對照 `023`，差異落在運作模式／狀態：`Full-Operation` |
| `…-025` | `SWE-PM-062` | `behaviour` | `input_data` | 對照 `027`，差異為其餘輸入之取值 |
| `…-026` | `SWE-PM-062` | `behaviour` | `boundary` | 對照 `025`，差異落在界線值：`other than` |
| `…-027` | `SWE-PM-062` | `behaviour` | `input_data` | 對照 `025`，差異為其餘輸入之取值 |
| `…-028` | `SWE-PM-063` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-029` | `SWE-PM-064` | `behaviour` | `timing` | 對照 `030`，差異落在時間量／時序：`expiration` |
| `…-030` | `SWE-PM-064` | `behaviour` | `timing` | 對照 `029`，差異落在時間量／時序：`expiration` |
| `…-031` | `SWE-PM-065` | `behaviour` | `timing` | 對照 `032`，差異落在時間量／時序：`expires` |
| `…-032` | `SWE-PM-065` | `behaviour` | `timing` | 對照 `031`，差異落在時間量／時序：`expires` |
| `…-033` | `SWE-PM-038` | `behaviour` | `timing` | 對照 `039`，差異落在時間量／時序：`expiration` |
| `…-034` | `SWE-PM-038` | `behaviour` | `timing` | 對照 `039`，差異落在時間量／時序：`expiration` |
| `…-035` | `SWE-PM-038` | `behaviour` | `trigger_state` | 對照 `038`，差異落在觸發訊號：`TLM_Status.Info` |
| `…-036` | `SWE-PM-038` | `behaviour` | `input_data` | 對照 `041`，差異為其餘輸入之取值 |
| `…-037` | `SWE-PM-038` | `behaviour` | `timing` | 對照 `042`，差異落在時間量／時序：`expired` |
| `…-038` | `SWE-PM-038` | `behaviour` | `input_data` | 對照 `039`，差異為其餘輸入之取值 |
| `…-039` | `SWE-PM-038` | `behaviour` | `input_data` | 對照 `038`，差異為其餘輸入之取值 |
| `…-040` | `SWE-PM-038` | `behaviour` | `input_data` | 對照 `043`，差異為其餘輸入之取值 |
| `…-041` | `SWE-PM-038` | `behaviour` | `input_data` | 對照 `036`，差異為其餘輸入之取值 |
| `…-042` | `SWE-PM-038` | `behaviour` | `timing` | 對照 `037`，差異落在時間量／時序：`expired` |
| `…-043` | `SWE-PM-038` | `trigger` | `input_data` | 對照 `040`，差異為其餘輸入之取值 |
| `…-044` | `SWE-PM-011` | `behaviour` | `input_data` | 對照 `049`，差異為其餘輸入之取值 |
| `…-045` | `SWE-PM-011` | `behaviour` | `mode` | 對照 `046`，差異落在運作模式／狀態：`OFF` |
| `…-046` | `SWE-PM-011` | `mode` | `mode` | 對照 `047`，差異落在運作模式／狀態：`OFF` |
| `…-047` | `SWE-PM-011` | `behaviour` | `mode` | 對照 `046`，差異落在運作模式／狀態：`OFF` |
| `…-048` | `SWE-PM-011` | `mode` | `mode` | 對照 `045`，差異落在運作模式／狀態：`IDLE` |
| `…-049` | `SWE-PM-011` | `branch` | `input_data` | 對照 `044`，差異為其餘輸入之取值 |
| `…-050` | `SWE-PM-012` | `behaviour` | `trigger_state` | 對照 `051`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-051` | `SWE-PM-012` | `behaviour` | `trigger_state` | 對照 `050`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-052` | `SWE-PM-013` | `behaviour` | `input_data` | 對照 `055`，差異為其餘輸入之取值 |
| `…-053` | `SWE-PM-013` | `behaviour` | `input_data` | 對照 `052`，差異為其餘輸入之取值 |
| `…-054` | `SWE-PM-013` | `behaviour` | `input_data` | 對照 `052`，差異為其餘輸入之取值 |
| `…-055` | `SWE-PM-013` | `behaviour` | `input_data` | 對照 `052`，差異為其餘輸入之取值 |
| `…-056` | `SWE-PM-013` | `behaviour` | `mode` | 對照 `057`，差異落在運作模式／狀態：`OFF` |
| `…-057` | `SWE-PM-013` | `behaviour` | `mode` | 對照 `056`，差異落在運作模式／狀態：`OFF` |
| `…-058` | `SWE-PM-014` | `behaviour` | `input_data` | 對照 `066`，差異為其餘輸入之取值 |
| `…-059` | `SWE-PM-014` | `behaviour` | `timing` | 對照 `060`，差異落在時間量／時序：`Timeout1` |
| `…-060` | `SWE-PM-014` | `mode` | `mode` | 對照 `061`，差異落在運作模式／狀態：`Standby` |
| `…-061` | `SWE-PM-014` | `behaviour` | `mode` | 對照 `060`，差異落在運作模式／狀態：`Standby` |
| `…-062` | `SWE-PM-014` | `behaviour` | `trigger_state` | 對照 `060`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-063` | `SWE-PM-014` | `behaviour` | `trigger_state` | 對照 `065`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-064` | `SWE-PM-014` | `trigger_state` | `trigger_state` | 對照 `060`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-065` | `SWE-PM-014` | `branch` | `trigger_state` | 對照 `064`，差異落在觸發訊號：`Phone_Call.Info` |
| `…-066` | `SWE-PM-014` | `trigger` | `input_data` | 對照 `058`，差異為其餘輸入之取值 |
| `…-067` | `SWE-PM-015` | `trigger_state` | `trigger_state` | 對照 `068`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-068` | `SWE-PM-015` | `behaviour` | `trigger_state` | 對照 `067`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-069` | `SWE-PM-015` | `trigger_state` | `trigger_state` | 對照 `070`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-070` | `SWE-PM-015` | `behaviour` | `trigger_state` | 對照 `069`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-071` | `SWE-PM-016` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-072` | `SWE-PM-017` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-073` | `SWE-PM-018` | `behaviour` | `input_data` | 對照 `074`，差異為其餘輸入之取值 |
| `…-074` | `SWE-PM-018` | `trigger` | `input_data` | 對照 `073`，差異為其餘輸入之取值 |
| `…-075` | `SWE-PM-019` | `trigger_state` | `trigger_state` | 對照 `077`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-076` | `SWE-PM-019` | `trigger_state` | `trigger_state` | 對照 `078`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-077` | `SWE-PM-019` | `behaviour` | `trigger_state` | 對照 `075`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-078` | `SWE-PM-019` | `behaviour` | `trigger_state` | 對照 `076`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-079` | `SWE-PM-020` | `behaviour` | `input_data` | 對照 `080`，差異為其餘輸入之取值 |
| `…-080` | `SWE-PM-020` | `behaviour` | `trigger_state` | 對照 `081`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-081` | `SWE-PM-020` | `behaviour` | `trigger_state` | 對照 `080`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-082` | `SWE-PM-021` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-083` | `SWE-PM-022` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-084` | `SWE-PM-023` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-085` | `SWE-PM-024` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-086` | `SWE-PM-025` | `trigger_state` | `trigger_state` | 對照 `090`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-087` | `SWE-PM-025` | `behaviour` | `trigger_state` | 對照 `091`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-088` | `SWE-PM-025` | `behaviour` | `trigger_state` | 對照 `092`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-089` | `SWE-PM-025` | `trigger_state` | `trigger_state` | 對照 `093`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-090` | `SWE-PM-025` | `behaviour` | `trigger_state` | 對照 `086`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-091` | `SWE-PM-025` | `behaviour` | `trigger_state` | 對照 `087`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-092` | `SWE-PM-025` | `behaviour` | `trigger_state` | 對照 `088`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-093` | `SWE-PM-025` | `behaviour` | `trigger_state` | 對照 `089`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-094` | `SWE-PM-026` | `behaviour` | `trigger_state` | 對照 `096`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-095` | `SWE-PM-026` | `behaviour` | `trigger_state` | 對照 `096`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-096` | `SWE-PM-026` | `behaviour` | `trigger_state` | 對照 `095`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-097` | `SWE-PM-026` | `behaviour` | `trigger_state` | 對照 `096`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-098` | `SWE-PM-027` | `timing` | `timing` | 對照 `099`，差異落在時間量／時序：`Timeout1` |
| `…-099` | `SWE-PM-027` | `behaviour` | `timing` | 對照 `098`，差異落在時間量／時序：`Timeout1` |
| `…-100` | `SWE-PM-028` | `behaviour` | `trigger_state` | 對照 `102`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-101` | `SWE-PM-028` | `behaviour` | `trigger_state` | 對照 `103`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-102` | `SWE-PM-028` | `behaviour` | `trigger_state` | 對照 `100`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-103` | `SWE-PM-028` | `branch` | `trigger_state` | 對照 `101`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-104` | `SWE-PM-029` | `behaviour` | `trigger_state` | 對照 `107`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-105` | `SWE-PM-029` | `timing` | `timing` | 對照 `106`，差異落在時間量／時序：`Switch_Off_Time` |
| `…-106` | `SWE-PM-029` | `behaviour` | `timing` | 對照 `105`，差異落在時間量／時序：`Switch_Off_Time` |
| `…-107` | `SWE-PM-029` | `behaviour` | `trigger_state` | 對照 `104`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-108` | `SWE-PM-030` | `behaviour` | `input_data` | 對照 `109`，差異為其餘輸入之取值 |
| `…-109` | `SWE-PM-030` | `behaviour` | `input_data` | 對照 `108`，差異為其餘輸入之取值 |
| `…-110` | `SWE-PM-031` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-111` | `SWE-PM-032` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-112` | `SWE-PM-033` | `behaviour` | `input_data` | 對照 `113`，差異為其餘輸入之取值 |
| `…-113` | `SWE-PM-033` | `behaviour` | `input_data` | 對照 `112`，差異為其餘輸入之取值 |
| `…-114` | `SWE-PM-034` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-115` | `SWE-PM-035` | `behaviour` | `trigger_state` | 對照 `117`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-116` | `SWE-PM-035` | `behaviour` | `input_data` | 對照 `118`，差異為其餘輸入之取值 |
| `…-117` | `SWE-PM-035` | `behaviour` | `trigger_state` | 對照 `115`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-118` | `SWE-PM-035` | `behaviour` | `input_data` | 對照 `116`，差異為其餘輸入之取值 |
| `…-119` | `SWE-PM-036` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-120` | `SWE-PM-037` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-121` | `SWE-PM-039` | `behaviour` | `timing` | 對照 `122`，差異落在時間量／時序：`Switch_Off_Time` |
| `…-122` | `SWE-PM-039` | `behaviour` | `trigger_state` | 對照 `123`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-123` | `SWE-PM-039` | `trigger_state` | `trigger_state` | 對照 `122`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-124` | `SWE-PM-039` | `behaviour` | `timing` | 對照 `122`，差異落在時間量／時序：`Switch_Off_Time` |
| `…-125` | `SWE-PM-040` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-126` | `SWE-PM-041` | `behaviour` | `trigger_state` | 對照 `127`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-127` | `SWE-PM-041` | `behaviour` | `trigger_state` | 對照 `126`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-128` | `SWE-PM-042` | `behaviour` | `trigger_state` | 對照 `129`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-129` | `SWE-PM-042` | `behaviour` | `trigger_state` | 對照 `128`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-130` | `SWE-PM-043` | `mode` | `mode` | 對照 `131`，差異落在運作模式／狀態：`off` |
| `…-131` | `SWE-PM-043` | `behaviour` | `mode` | 對照 `130`，差異落在運作模式／狀態：`off` |
| `…-132` | `SWE-PM-044` | `behaviour` | `mode` | 對照 `133`，差異落在運作模式／狀態：`Sleep` |
| `…-133` | `SWE-PM-044` | `mode` | `mode` | 對照 `132`，差異落在運作模式／狀態：`Sleep` |
| `…-134` | `SWE-PM-044` | `behaviour` | `mode` | 對照 `135`，差異落在運作模式／狀態：`Sleep` |
| `…-135` | `SWE-PM-044` | `mode` | `mode` | 對照 `134`，差異落在運作模式／狀態：`Sleep` |
| `…-136` | `SWE-PM-045` | `behaviour` | `mode` | 對照 `137`，差異落在運作模式／狀態：`Sleep` |
| `…-137` | `SWE-PM-045` | `mode` | `mode` | 對照 `136`，差異落在運作模式／狀態：`Sleep` |
| `…-138` | `SWE-PM-046` | `behaviour` | `input_data` | 對照 `139`，差異為其餘輸入之取值 |
| `…-139` | `SWE-PM-046` | `behaviour` | `input_data` | 對照 `138`，差異為其餘輸入之取值 |
| `…-140` | `SWE-PM-047` | `behaviour` | `mode` | 對照 `141`，差異落在運作模式／狀態：`Sleep` |
| `…-141` | `SWE-PM-047` | `mode` | `mode` | 對照 `140`，差異落在運作模式／狀態：`Sleep` |
| `…-142` | `SWE-PM-048` | `mode` | `mode` | 對照 `143`，差異落在運作模式／狀態：`Full-Operation` |
| `…-143` | `SWE-PM-048` | `behaviour` | `mode` | 對照 `142`，差異落在運作模式／狀態：`Full-Operation` |
| `…-144` | `SWE-PM-048` | `mode` | `mode` | 對照 `145`，差異落在運作模式／狀態：`Full-Operation` |
| `…-145` | `SWE-PM-048` | `behaviour` | `mode` | 對照 `144`，差異落在運作模式／狀態：`Full-Operation` |
| `…-146` | `SWE-PM-048` | `behaviour` | `trigger_state` | 對照 `145`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-147` | `SWE-PM-049` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-148` | `SWE-PM-050` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-149` | `SWE-PM-051` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-150` | `SWE-PM-052` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-151` | `SWE-PM-053` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-152` | `SWE-PM-054` | `behaviour` | `input_data` | 對照 `153`，差異為其餘輸入之取值 |
| `…-153` | `SWE-PM-054` | `behaviour` | `input_data` | 對照 `155`，差異為其餘輸入之取值 |
| `…-154` | `SWE-PM-054` | `behaviour` | `input_data` | 對照 `155`，差異為其餘輸入之取值 |
| `…-155` | `SWE-PM-054` | `behaviour` | `input_data` | 對照 `154`，差異為其餘輸入之取值 |
| `…-156` | `SWE-PM-055` | `behaviour` | `boundary` | 對照 `157`，差異落在界線值：`greater than` |
| `…-157` | `SWE-PM-055` | `behaviour` | `boundary` | 對照 `156`，差異落在界線值：`greater than` |
| `…-158` | `SWE-PM-056` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-159` | `SWE-PM-058` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-160` | `SWE-PM-059` | `behaviour` | `input_data` | 對照 `161`，差異為其餘輸入之取值 |
| `…-161` | `SWE-PM-059` | `behaviour` | `input_data` | 對照 `160`，差異為其餘輸入之取值 |
| `…-162` | `SWE-PM-066` | `behaviour` | `input_data` | 對照 `163`，差異為其餘輸入之取值 |
| `…-163` | `SWE-PM-066` | `behaviour` | `input_data` | 對照 `162`，差異為其餘輸入之取值 |
| `…-164` | `SWE-PM-067` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-165` | `SWE-PM-068` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-166` | `SWE-PM-069` | `behaviour` | `input_data` | 對照 `167`，差異為其餘輸入之取值 |
| `…-167` | `SWE-PM-069` | `behaviour` | `input_data` | 對照 `166`，差異為其餘輸入之取值 |
| `…-168` | `SWE-PM-070` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-169` | `SWE-PM-074` | `behaviour` | `input_data` | 對照 `170`，差異為其餘輸入之取值 |
| `…-170` | `SWE-PM-074` | `behaviour` | `input_data` | 對照 `171`，差異為其餘輸入之取值 |
| `…-171` | `SWE-PM-074` | `behaviour` | `input_data` | 對照 `170`，差異為其餘輸入之取值 |
| `…-172` | `SWE-PM-075` | `behaviour` | `mode` | 對照 `173`，差異落在運作模式／狀態：`idle` |
| `…-173` | `SWE-PM-075` | `behaviour` | `mode` | 對照 `172`，差異落在運作模式／狀態：`idle` |
| `…-174` | `SWE-PM-075` | `trigger_state` | `trigger_state` | 對照 `173`，差異落在觸發訊號：`$ACCDlyAct$` |
| `…-175` | `SWE-PM-076` | `behaviour` | `input_data` | 對照 `176`，差異為其餘輸入之取值 |
| `…-176` | `SWE-PM-076` | `behaviour` | `input_data` | 對照 `175`，差異為其餘輸入之取值 |
| `…-177` | `SWE-PM-076` | `behaviour` | `input_data` | 對照 `175`，差異為其餘輸入之取值 |
| `…-178` | `SWE-PM-093` | `mode` | `mode` | 對照 `179`，差異落在運作模式／狀態：`SLEEP` |
| `…-179` | `SWE-PM-093` | `behaviour` | `mode` | 對照 `178`，差異落在運作模式／狀態：`SLEEP` |
| `…-180` | `SWE-PM-093` | `behaviour` | `mode` | 對照 `178`，差異落在運作模式／狀態：`SLEEP` |
| `…-181` | `SWE-PM-093` | `behaviour` | `trigger_state` | 對照 `179`，差異落在觸發訊號：`$Door_Ajar_Status$` |
| `…-182` | `SWE-PM-093` | `behaviour` | `mode` | 對照 `184`，差異落在運作模式／狀態：`TIMED` |
| `…-183` | `SWE-PM-093` | `behaviour` | `trigger_state` | 對照 `184`，差異落在觸發訊號：`$PowerMode$` |
| `…-184` | `SWE-PM-093` | `behaviour` | `trigger_state` | 對照 `183`，差異落在觸發訊號：`$PowerMode$` |
| `…-185` | `SWE-PM-093` | `behaviour` | `trigger_state` | 對照 `184`，差異落在觸發訊號：`$Door_Ajar_Status$` |
| `…-186` | `SWE-PM-093` | `behaviour` | `trigger_state` | 對照 `181`，差異落在觸發訊號：`$DriverDoorOnOffSts$` |
| `…-187` | `SWE-PM-094` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-188` | `SWE-PM-095` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-189` | `SWE-PM-097` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-190` | `SWE-PM-098` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-191` | `SWE-PM-099` | `behaviour` | `input_data` | 對照 `193`，差異為其餘輸入之取值 |
| `…-192` | `SWE-PM-099` | `behaviour` | `input_data` | 對照 `194`，差異為其餘輸入之取值 |
| `…-193` | `SWE-PM-099` | `behaviour` | `input_data` | 對照 `192`，差異為其餘輸入之取值 |
| `…-194` | `SWE-PM-099` | `behaviour` | `input_data` | 對照 `192`，差異為其餘輸入之取值 |
| `…-195` | `SWE-PM-100` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-196` | `SWE-PM-101` | `behaviour` | `input_data` | 對照 `197`，差異為其餘輸入之取值 |
| `…-197` | `SWE-PM-101` | `behaviour` | `input_data` | 對照 `199`，差異為其餘輸入之取值 |
| `…-198` | `SWE-PM-101` | `behaviour` | `input_data` | 對照 `199`，差異為其餘輸入之取值 |
| `…-199` | `SWE-PM-101` | `behaviour` | `input_data` | 對照 `198`，差異為其餘輸入之取值 |
| `…-200` | `SWE-PM-102` | `behaviour` | `boundary` | 對照 `201`，差異落在界線值：`greater than` |
| `…-201` | `SWE-PM-102` | `behaviour` | `boundary` | 對照 `200`，差異落在界線值：`greater than` |
| `…-202` | `SWE-PM-103` | `behaviour` | `input_data` | 對照 `204`，差異為其餘輸入之取值 |
| `…-203` | `SWE-PM-103` | `behaviour` | `input_data` | 對照 `202`，差異為其餘輸入之取值 |
| `…-204` | `SWE-PM-103` | `behaviour` | `input_data` | 對照 `202`，差異為其餘輸入之取值 |
| `…-205` | `SWE-PM-103` | `behaviour` | `input_data` | 對照 `202`，差異為其餘輸入之取值 |
| `…-206` | `SWE-PM-103` | `behaviour` | `input_data` | 對照 `202`，差異為其餘輸入之取值 |
| `…-207` | `SWE-PM-104` | `mode` | `mode` | 對照 `208`，差異落在運作模式／狀態：`Timed` |
| `…-208` | `SWE-PM-104` | `behaviour` | `mode` | 對照 `207`，差異落在運作模式／狀態：`Timed` |
| `…-209` | `SWE-PM-104` | `mode` | `mode` | 對照 `210`，差異落在運作模式／狀態：`Idle` |
| `…-210` | `SWE-PM-104` | `behaviour` | `mode` | 對照 `209`，差異落在運作模式／狀態：`Idle` |
| `…-211` | `SWE-PM-104` | `behaviour` | `mode` | 對照 `209`，差異落在運作模式／狀態：`Idle` |
| `…-212` | `SWE-PM-105` | `behaviour` | `input_data` | 對照 `214`，差異為其餘輸入之取值 |
| `…-213` | `SWE-PM-105` | `behaviour` | `input_data` | 對照 `218`，差異為其餘輸入之取值 |
| `…-214` | `SWE-PM-105` | `behaviour` | `input_data` | 對照 `212`，差異為其餘輸入之取值 |
| `…-215` | `SWE-PM-105` | `behaviour` | `input_data` | 對照 `212`，差異為其餘輸入之取值 |
| `…-216` | `SWE-PM-105` | `behaviour` | `input_data` | 對照 `218`，差異為其餘輸入之取值 |
| `…-217` | `SWE-PM-105` | `behaviour` | `input_data` | 對照 `212`，差異為其餘輸入之取值 |
| `…-218` | `SWE-PM-105` | `behaviour` | `input_data` | 對照 `216`，差異為其餘輸入之取值 |
| `…-219` | `SWE-PM-105` | `behaviour` | `mode` | 對照 `218`，差異落在運作模式／狀態：`Timed` |
| `…-220` | `SWE-PM-106` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-221` | `SWE-PM-107` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-222` | `SWE-PM-108` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-223` | `SWE-PM-109` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-224` | `SWE-PM-110` | `behaviour` | `trigger_state` | 對照 `225`，差異落在觸發訊號：`$Country_Code$` |
| `…-225` | `SWE-PM-110` | `behaviour` | `trigger_state` | 對照 `224`，差異落在觸發訊號：`$Country_Code$` |
| `…-226` | `SWE-PM-111` | `behaviour` | `trigger_state` | 對照 `227`，差異落在觸發訊號：`$Country_Code$` |
| `…-227` | `SWE-PM-111` | `behaviour` | `trigger_state` | 對照 `226`，差異落在觸發訊號：`$Country_Code$` |
| `…-228` | `SWE-PM-113` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-229` | `SWE-PM-114` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-230` | `SWE-PM-115` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-231` | `SWE-PM-077` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-232` | `SWE-PM-078` | `behaviour` | `input_data` | 對照 `233`，差異為其餘輸入之取值 |
| `…-233` | `SWE-PM-078` | `behaviour` | `input_data` | 對照 `232`，差異為其餘輸入之取值 |
| `…-234` | `SWE-PM-079` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-235` | `SWE-PM-080` | `behaviour` | `trigger_state` | 對照 `236`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-236` | `SWE-PM-080` | `behaviour` | `trigger_state` | 對照 `235`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-237` | `SWE-PM-081` | `behaviour` | `input_data` | 對照 `238`，差異為其餘輸入之取值 |
| `…-238` | `SWE-PM-081` | `behaviour` | `input_data` | 對照 `237`，差異為其餘輸入之取值 |
| `…-239` | `SWE-PM-081` | `behaviour` | `input_data` | 對照 `238`，差異為其餘輸入之取值 |
| `…-240` | `SWE-PM-082` | `behaviour` | `input_data` | 對照 `241`，差異為其餘輸入之取值 |
| `…-241` | `SWE-PM-082` | `behaviour` | `input_data` | 對照 `240`，差異為其餘輸入之取值 |
| `…-242` | `SWE-PM-082` | `behaviour` | `input_data` | 對照 `241`，差異為其餘輸入之取值 |
| `…-243` | `SWE-PM-083` | `behaviour` | `input_data` | 對照 `245`，差異為其餘輸入之取值 |
| `…-244` | `SWE-PM-083` | `behaviour` | `input_data` | 對照 `243`，差異為其餘輸入之取值 |
| `…-245` | `SWE-PM-083` | `behaviour` | `input_data` | 對照 `243`，差異為其餘輸入之取值 |
| `…-246` | `SWE-PM-084` | `behaviour` | `trigger_state` | 對照 `247`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-247` | `SWE-PM-084` | `behaviour` | `trigger_state` | 對照 `246`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-248` | `SWE-PM-085` | `behaviour` | `trigger_state` | 對照 `249`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-249` | `SWE-PM-085` | `behaviour` | `trigger_state` | 對照 `248`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-250` | `SWE-PM-086` | `behaviour` | `trigger_state` | 對照 `251`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-251` | `SWE-PM-086` | `behaviour` | `trigger_state` | 對照 `250`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-252` | `SWE-PM-087` | `behaviour` | `trigger_state` | 對照 `253`，差異落在觸發訊號：`$VC_VEH_BRAND$` |
| `…-253` | `SWE-PM-087` | `behaviour` | `trigger_state` | 對照 `252`，差異落在觸發訊號：`$VC_VEH_BRAND$` |
| `…-254` | `SWE-PM-088` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-255` | `SWE-PM-090` | `behaviour` | `input_data` | 對照 `256`，差異為其餘輸入之取值 |
| `…-256` | `SWE-PM-090` | `behaviour` | `input_data` | 對照 `255`，差異為其餘輸入之取值 |
| `…-257` | `SWE-PM-091` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-258` | `SWE-PM-092` | `behaviour` | **無對應** | 該 leaf 僅產出 1 條 TC —— 無他條可區分，六值皆無對應 |
| `…-259` | `SWE-PM-096` | `behaviour` | `input_data` | 對照 `261`，差異為其餘輸入之取值 |
| `…-260` | `SWE-PM-096` | `behaviour` | `input_data` | 對照 `261`，差異為其餘輸入之取值 |
| `…-261` | `SWE-PM-096` | `behaviour` | `input_data` | 對照 `259`，差異為其餘輸入之取值 |
| `…-262` | `SWE-PM-096` | `behaviour` | `input_data` | 對照 `260`，差異為其餘輸入之取值 |
| `…-263` | `SWE-PM-096` | `behaviour` | `input_data` | 對照 `264`，差異為其餘輸入之取值 |
| `…-264` | `SWE-PM-096` | `behaviour` | `input_data` | 對照 `263`，差異為其餘輸入之取值 |
