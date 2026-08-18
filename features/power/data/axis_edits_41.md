# B2 —— `axis` 187 條重判提案之套用（R-P278）

> 模式：**套用**；改動 **187** 條。
> **套用範圍**：現值不在 §4.6 六值內者。
> 現值已合法而與提案相異者 **不動** —— 其係 37 包經「依據逐字可見」之嚴格判準所改，本包之提案不優於之（R-P236(b)）。

## 一、`axis` 值分布（前 → 後）

| 值 | 合法 | 前 | 後 |
|---|---|---|---|
| `behaviour` | **否** | 179 | **0** |
| `boundary` | 是 | 0 | **5** |
| `branch` | **否** | 5 | **0** |
| `input_data` | 是 | 1 | **90** |
| `mode` | 是 | 20 | **42** |
| `timing` | 是 | 5 | **18** |
| `trigger` | **否** | 3 | **0** |
| `trigger_state` | 是 | 11 | **69** |

## 二、現值已合法而與提案相異者 —— **2** 條（不動）

| tc | 現值 | 提案 | 依據 |
|---|---|---|---|
| `…-006` | `timing` | `input_data` | 對照 `005`，差異為其餘輸入之取值 |
| `…-007` | `trigger_state` | `input_data` | 對照 `016`，差異為其餘輸入之取值 |

## 三、逐條套用（187）

| tc | 舊 | 新 | 依據 |
|---|---|---|---|
| `…-011` | `behaviour` | **`input_data`** | 對照 `012`，差異為其餘輸入之取值 |
| `…-012` | `behaviour` | **`trigger_state`** | 對照 `013`，差異落在觸發訊號：`STATUS_LIN.Batt_ST_Crit` |
| `…-013` | `behaviour` | **`trigger_state`** | 對照 `012`，差異落在觸發訊號：`STATUS_LIN.Batt_ST_Crit` |
| `…-015` | `behaviour` | **`mode`** | 對照 `013`，差異落在運作模式／狀態：`bench` |
| `…-016` | `branch` | **`input_data`** | 對照 `007`，差異為其餘輸入之取值 |
| `…-017` | `branch` | **`trigger_state`** | 對照 `016`，差異落在觸發訊號：`STATUS_LIN.Batt_ST_Crit` |
| `…-018` | `behaviour` | **`input_data`** | 對照 `019`，差異為其餘輸入之取值 |
| `…-019` | `behaviour` | **`input_data`** | 對照 `018`，差異為其餘輸入之取值 |
| `…-020` | `behaviour` | **`input_data`** | 對照 `018`，差異為其餘輸入之取值 |
| `…-021` | `behaviour` | **`input_data`** | 對照 `022`，差異為其餘輸入之取值 |
| `…-022` | `behaviour` | **`input_data`** | 對照 `021`，差異為其餘輸入之取值 |
| `…-025` | `behaviour` | **`input_data`** | 對照 `027`，差異為其餘輸入之取值 |
| `…-026` | `behaviour` | **`boundary`** | 對照 `025`，差異落在界線值：`other than` |
| `…-027` | `behaviour` | **`input_data`** | 對照 `025`，差異為其餘輸入之取值 |
| `…-029` | `behaviour` | **`timing`** | 對照 `030`，差異落在時間量／時序：`expiration` |
| `…-030` | `behaviour` | **`timing`** | 對照 `029`，差異落在時間量／時序：`expiration` |
| `…-031` | `behaviour` | **`timing`** | 對照 `032`，差異落在時間量／時序：`expires` |
| `…-032` | `behaviour` | **`timing`** | 對照 `031`，差異落在時間量／時序：`expires` |
| `…-033` | `behaviour` | **`timing`** | 對照 `039`，差異落在時間量／時序：`expiration` |
| `…-034` | `behaviour` | **`timing`** | 對照 `039`，差異落在時間量／時序：`expiration` |
| `…-035` | `behaviour` | **`trigger_state`** | 對照 `038`，差異落在觸發訊號：`TLM_Status.Info` |
| `…-036` | `behaviour` | **`input_data`** | 對照 `041`，差異為其餘輸入之取值 |
| `…-037` | `behaviour` | **`timing`** | 對照 `042`，差異落在時間量／時序：`expired` |
| `…-038` | `behaviour` | **`input_data`** | 對照 `039`，差異為其餘輸入之取值 |
| `…-039` | `behaviour` | **`input_data`** | 對照 `038`，差異為其餘輸入之取值 |
| `…-040` | `behaviour` | **`input_data`** | 對照 `043`，差異為其餘輸入之取值 |
| `…-041` | `behaviour` | **`input_data`** | 對照 `036`，差異為其餘輸入之取值 |
| `…-042` | `behaviour` | **`timing`** | 對照 `037`，差異落在時間量／時序：`expired` |
| `…-043` | `trigger` | **`input_data`** | 對照 `040`，差異為其餘輸入之取值 |
| `…-044` | `behaviour` | **`input_data`** | 對照 `049`，差異為其餘輸入之取值 |
| `…-045` | `behaviour` | **`mode`** | 對照 `046`，差異落在運作模式／狀態：`OFF` |
| `…-047` | `behaviour` | **`mode`** | 對照 `046`，差異落在運作模式／狀態：`OFF` |
| `…-049` | `branch` | **`input_data`** | 對照 `044`，差異為其餘輸入之取值 |
| `…-050` | `behaviour` | **`trigger_state`** | 對照 `051`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-051` | `behaviour` | **`trigger_state`** | 對照 `050`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-052` | `behaviour` | **`input_data`** | 對照 `055`，差異為其餘輸入之取值 |
| `…-053` | `behaviour` | **`input_data`** | 對照 `052`，差異為其餘輸入之取值 |
| `…-054` | `behaviour` | **`input_data`** | 對照 `052`，差異為其餘輸入之取值 |
| `…-055` | `behaviour` | **`input_data`** | 對照 `052`，差異為其餘輸入之取值 |
| `…-056` | `behaviour` | **`mode`** | 對照 `057`，差異落在運作模式／狀態：`OFF` |
| `…-057` | `behaviour` | **`mode`** | 對照 `056`，差異落在運作模式／狀態：`OFF` |
| `…-058` | `behaviour` | **`input_data`** | 對照 `066`，差異為其餘輸入之取值 |
| `…-059` | `behaviour` | **`timing`** | 對照 `060`，差異落在時間量／時序：`Timeout1` |
| `…-061` | `behaviour` | **`mode`** | 對照 `060`，差異落在運作模式／狀態：`Standby` |
| `…-062` | `behaviour` | **`trigger_state`** | 對照 `060`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-063` | `behaviour` | **`trigger_state`** | 對照 `065`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-065` | `branch` | **`trigger_state`** | 對照 `064`，差異落在觸發訊號：`Phone_Call.Info` |
| `…-066` | `trigger` | **`input_data`** | 對照 `058`，差異為其餘輸入之取值 |
| `…-068` | `behaviour` | **`trigger_state`** | 對照 `067`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-070` | `behaviour` | **`trigger_state`** | 對照 `069`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-073` | `behaviour` | **`input_data`** | 對照 `074`，差異為其餘輸入之取值 |
| `…-074` | `trigger` | **`input_data`** | 對照 `073`，差異為其餘輸入之取值 |
| `…-077` | `behaviour` | **`trigger_state`** | 對照 `075`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-078` | `behaviour` | **`trigger_state`** | 對照 `076`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-079` | `behaviour` | **`input_data`** | 對照 `080`，差異為其餘輸入之取值 |
| `…-080` | `behaviour` | **`trigger_state`** | 對照 `081`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-081` | `behaviour` | **`trigger_state`** | 對照 `080`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-087` | `behaviour` | **`trigger_state`** | 對照 `091`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-088` | `behaviour` | **`trigger_state`** | 對照 `092`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-090` | `behaviour` | **`trigger_state`** | 對照 `086`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-091` | `behaviour` | **`trigger_state`** | 對照 `087`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-092` | `behaviour` | **`trigger_state`** | 對照 `088`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-093` | `behaviour` | **`trigger_state`** | 對照 `089`，差異落在觸發訊號：`Front_Panel_OnOff.Req` |
| `…-094` | `behaviour` | **`trigger_state`** | 對照 `096`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-095` | `behaviour` | **`trigger_state`** | 對照 `096`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-096` | `behaviour` | **`trigger_state`** | 對照 `095`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-097` | `behaviour` | **`trigger_state`** | 對照 `096`，差異落在觸發訊號：`PhoneCall.Info` |
| `…-099` | `behaviour` | **`timing`** | 對照 `098`，差異落在時間量／時序：`Timeout1` |
| `…-100` | `behaviour` | **`trigger_state`** | 對照 `102`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-101` | `behaviour` | **`trigger_state`** | 對照 `103`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-102` | `behaviour` | **`trigger_state`** | 對照 `100`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-103` | `branch` | **`trigger_state`** | 對照 `101`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-104` | `behaviour` | **`trigger_state`** | 對照 `107`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-106` | `behaviour` | **`timing`** | 對照 `105`，差異落在時間量／時序：`Switch_Off_Time` |
| `…-107` | `behaviour` | **`trigger_state`** | 對照 `104`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-108` | `behaviour` | **`input_data`** | 對照 `109`，差異為其餘輸入之取值 |
| `…-109` | `behaviour` | **`input_data`** | 對照 `108`，差異為其餘輸入之取值 |
| `…-112` | `behaviour` | **`input_data`** | 對照 `113`，差異為其餘輸入之取值 |
| `…-113` | `behaviour` | **`input_data`** | 對照 `112`，差異為其餘輸入之取值 |
| `…-115` | `behaviour` | **`trigger_state`** | 對照 `117`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-116` | `behaviour` | **`input_data`** | 對照 `118`，差異為其餘輸入之取值 |
| `…-117` | `behaviour` | **`trigger_state`** | 對照 `115`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-118` | `behaviour` | **`input_data`** | 對照 `116`，差異為其餘輸入之取值 |
| `…-121` | `behaviour` | **`timing`** | 對照 `122`，差異落在時間量／時序：`Switch_Off_Time` |
| `…-122` | `behaviour` | **`trigger_state`** | 對照 `123`，差異落在觸發訊號：`Auto_SwitchOn_Setting.Req` |
| `…-124` | `behaviour` | **`timing`** | 對照 `122`，差異落在時間量／時序：`Switch_Off_Time` |
| `…-126` | `behaviour` | **`trigger_state`** | 對照 `127`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-127` | `behaviour` | **`trigger_state`** | 對照 `126`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-128` | `behaviour` | **`trigger_state`** | 對照 `129`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-129` | `behaviour` | **`trigger_state`** | 對照 `128`，差異落在觸發訊號：`Antitheft_Activation.Req` |
| `…-131` | `behaviour` | **`mode`** | 對照 `130`，差異落在運作模式／狀態：`off` |
| `…-132` | `behaviour` | **`mode`** | 對照 `133`，差異落在運作模式／狀態：`Sleep` |
| `…-134` | `behaviour` | **`mode`** | 對照 `135`，差異落在運作模式／狀態：`Sleep` |
| `…-136` | `behaviour` | **`mode`** | 對照 `137`，差異落在運作模式／狀態：`Sleep` |
| `…-138` | `behaviour` | **`input_data`** | 對照 `139`，差異為其餘輸入之取值 |
| `…-139` | `behaviour` | **`input_data`** | 對照 `138`，差異為其餘輸入之取值 |
| `…-140` | `behaviour` | **`mode`** | 對照 `141`，差異落在運作模式／狀態：`Sleep` |
| `…-143` | `behaviour` | **`mode`** | 對照 `142`，差異落在運作模式／狀態：`Full-Operation` |
| `…-145` | `behaviour` | **`mode`** | 對照 `144`，差異落在運作模式／狀態：`Full-Operation` |
| `…-146` | `behaviour` | **`trigger_state`** | 對照 `145`，差異落在觸發訊號：`$Telematic_Power$` |
| `…-152` | `behaviour` | **`input_data`** | 對照 `153`，差異為其餘輸入之取值 |
| `…-153` | `behaviour` | **`input_data`** | 對照 `155`，差異為其餘輸入之取值 |
| `…-154` | `behaviour` | **`input_data`** | 對照 `155`，差異為其餘輸入之取值 |
| `…-155` | `behaviour` | **`input_data`** | 對照 `154`，差異為其餘輸入之取值 |
| `…-156` | `behaviour` | **`boundary`** | 對照 `157`，差異落在界線值：`greater than` |
| `…-157` | `behaviour` | **`boundary`** | 對照 `156`，差異落在界線值：`greater than` |
| `…-160` | `behaviour` | **`input_data`** | 對照 `161`，差異為其餘輸入之取值 |
| `…-161` | `behaviour` | **`input_data`** | 對照 `160`，差異為其餘輸入之取值 |
| `…-162` | `behaviour` | **`input_data`** | 對照 `163`，差異為其餘輸入之取值 |
| `…-163` | `behaviour` | **`input_data`** | 對照 `162`，差異為其餘輸入之取值 |
| `…-166` | `behaviour` | **`input_data`** | 對照 `167`，差異為其餘輸入之取值 |
| `…-167` | `behaviour` | **`input_data`** | 對照 `166`，差異為其餘輸入之取值 |
| `…-169` | `behaviour` | **`input_data`** | 對照 `170`，差異為其餘輸入之取值 |
| `…-170` | `behaviour` | **`input_data`** | 對照 `171`，差異為其餘輸入之取值 |
| `…-171` | `behaviour` | **`input_data`** | 對照 `170`，差異為其餘輸入之取值 |
| `…-172` | `behaviour` | **`mode`** | 對照 `173`，差異落在運作模式／狀態：`idle` |
| `…-173` | `behaviour` | **`mode`** | 對照 `172`，差異落在運作模式／狀態：`idle` |
| `…-175` | `behaviour` | **`input_data`** | 對照 `176`，差異為其餘輸入之取值 |
| `…-176` | `behaviour` | **`input_data`** | 對照 `175`，差異為其餘輸入之取值 |
| `…-177` | `behaviour` | **`input_data`** | 對照 `175`，差異為其餘輸入之取值 |
| `…-179` | `behaviour` | **`mode`** | 對照 `178`，差異落在運作模式／狀態：`SLEEP` |
| `…-180` | `behaviour` | **`mode`** | 對照 `178`，差異落在運作模式／狀態：`SLEEP` |
| `…-181` | `behaviour` | **`trigger_state`** | 對照 `179`，差異落在觸發訊號：`$Door_Ajar_Status$` |
| `…-182` | `behaviour` | **`mode`** | 對照 `184`，差異落在運作模式／狀態：`TIMED` |
| `…-183` | `behaviour` | **`trigger_state`** | 對照 `184`，差異落在觸發訊號：`$PowerMode$` |
| `…-184` | `behaviour` | **`trigger_state`** | 對照 `183`，差異落在觸發訊號：`$PowerMode$` |
| `…-185` | `behaviour` | **`trigger_state`** | 對照 `184`，差異落在觸發訊號：`$Door_Ajar_Status$` |
| `…-186` | `behaviour` | **`trigger_state`** | 對照 `181`，差異落在觸發訊號：`$DriverDoorOnOffSts$` |
| `…-191` | `behaviour` | **`input_data`** | 對照 `193`，差異為其餘輸入之取值 |
| `…-192` | `behaviour` | **`input_data`** | 對照 `194`，差異為其餘輸入之取值 |
| `…-193` | `behaviour` | **`input_data`** | 對照 `192`，差異為其餘輸入之取值 |
| `…-194` | `behaviour` | **`input_data`** | 對照 `192`，差異為其餘輸入之取值 |
| `…-196` | `behaviour` | **`input_data`** | 對照 `197`，差異為其餘輸入之取值 |
| `…-197` | `behaviour` | **`input_data`** | 對照 `199`，差異為其餘輸入之取值 |
| `…-198` | `behaviour` | **`input_data`** | 對照 `199`，差異為其餘輸入之取值 |
| `…-199` | `behaviour` | **`input_data`** | 對照 `198`，差異為其餘輸入之取值 |
| `…-200` | `behaviour` | **`boundary`** | 對照 `201`，差異落在界線值：`greater than` |
| `…-201` | `behaviour` | **`boundary`** | 對照 `200`，差異落在界線值：`greater than` |
| `…-202` | `behaviour` | **`input_data`** | 對照 `204`，差異為其餘輸入之取值 |
| `…-203` | `behaviour` | **`input_data`** | 對照 `202`，差異為其餘輸入之取值 |
| `…-204` | `behaviour` | **`input_data`** | 對照 `202`，差異為其餘輸入之取值 |
| `…-205` | `behaviour` | **`input_data`** | 對照 `202`，差異為其餘輸入之取值 |
| `…-206` | `behaviour` | **`input_data`** | 對照 `202`，差異為其餘輸入之取值 |
| `…-208` | `behaviour` | **`mode`** | 對照 `207`，差異落在運作模式／狀態：`Timed` |
| `…-210` | `behaviour` | **`mode`** | 對照 `209`，差異落在運作模式／狀態：`Idle` |
| `…-211` | `behaviour` | **`mode`** | 對照 `209`，差異落在運作模式／狀態：`Idle` |
| `…-212` | `behaviour` | **`input_data`** | 對照 `214`，差異為其餘輸入之取值 |
| `…-213` | `behaviour` | **`input_data`** | 對照 `218`，差異為其餘輸入之取值 |
| `…-214` | `behaviour` | **`input_data`** | 對照 `212`，差異為其餘輸入之取值 |
| `…-215` | `behaviour` | **`input_data`** | 對照 `212`，差異為其餘輸入之取值 |
| `…-216` | `behaviour` | **`input_data`** | 對照 `218`，差異為其餘輸入之取值 |
| `…-217` | `behaviour` | **`input_data`** | 對照 `212`，差異為其餘輸入之取值 |
| `…-218` | `behaviour` | **`input_data`** | 對照 `216`，差異為其餘輸入之取值 |
| `…-219` | `behaviour` | **`mode`** | 對照 `218`，差異落在運作模式／狀態：`Timed` |
| `…-224` | `behaviour` | **`trigger_state`** | 對照 `225`，差異落在觸發訊號：`$Country_Code$` |
| `…-225` | `behaviour` | **`trigger_state`** | 對照 `224`，差異落在觸發訊號：`$Country_Code$` |
| `…-226` | `behaviour` | **`trigger_state`** | 對照 `227`，差異落在觸發訊號：`$Country_Code$` |
| `…-227` | `behaviour` | **`trigger_state`** | 對照 `226`，差異落在觸發訊號：`$Country_Code$` |
| `…-232` | `behaviour` | **`input_data`** | 對照 `233`，差異為其餘輸入之取值 |
| `…-233` | `behaviour` | **`input_data`** | 對照 `232`，差異為其餘輸入之取值 |
| `…-235` | `behaviour` | **`trigger_state`** | 對照 `236`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-236` | `behaviour` | **`trigger_state`** | 對照 `235`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-237` | `behaviour` | **`input_data`** | 對照 `238`，差異為其餘輸入之取值 |
| `…-238` | `behaviour` | **`input_data`** | 對照 `237`，差異為其餘輸入之取值 |
| `…-239` | `behaviour` | **`input_data`** | 對照 `238`，差異為其餘輸入之取值 |
| `…-240` | `behaviour` | **`input_data`** | 對照 `241`，差異為其餘輸入之取值 |
| `…-241` | `behaviour` | **`input_data`** | 對照 `240`，差異為其餘輸入之取值 |
| `…-242` | `behaviour` | **`input_data`** | 對照 `241`，差異為其餘輸入之取值 |
| `…-243` | `behaviour` | **`input_data`** | 對照 `245`，差異為其餘輸入之取值 |
| `…-244` | `behaviour` | **`input_data`** | 對照 `243`，差異為其餘輸入之取值 |
| `…-245` | `behaviour` | **`input_data`** | 對照 `243`，差異為其餘輸入之取值 |
| `…-246` | `behaviour` | **`trigger_state`** | 對照 `247`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-247` | `behaviour` | **`trigger_state`** | 對照 `246`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-248` | `behaviour` | **`trigger_state`** | 對照 `249`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-249` | `behaviour` | **`trigger_state`** | 對照 `248`，差異落在觸發訊號：`$Car_Shape_Configuration$` |
| `…-250` | `behaviour` | **`trigger_state`** | 對照 `251`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-251` | `behaviour` | **`trigger_state`** | 對照 `250`，差異落在觸發訊號：`$VC_SpecialPKG$` |
| `…-252` | `behaviour` | **`trigger_state`** | 對照 `253`，差異落在觸發訊號：`$VC_VEH_BRAND$` |
| `…-253` | `behaviour` | **`trigger_state`** | 對照 `252`，差異落在觸發訊號：`$VC_VEH_BRAND$` |
| `…-255` | `behaviour` | **`input_data`** | 對照 `256`，差異為其餘輸入之取值 |
| `…-256` | `behaviour` | **`input_data`** | 對照 `255`，差異為其餘輸入之取值 |
| `…-259` | `behaviour` | **`input_data`** | 對照 `261`，差異為其餘輸入之取值 |
| `…-260` | `behaviour` | **`input_data`** | 對照 `261`，差異為其餘輸入之取值 |
| `…-261` | `behaviour` | **`input_data`** | 對照 `259`，差異為其餘輸入之取值 |
| `…-262` | `behaviour` | **`input_data`** | 對照 `260`，差異為其餘輸入之取值 |
| `…-263` | `behaviour` | **`input_data`** | 對照 `264`，差異為其餘輸入之取值 |
| `…-264` | `behaviour` | **`input_data`** | 對照 `263`，差異為其餘輸入之取值 |
