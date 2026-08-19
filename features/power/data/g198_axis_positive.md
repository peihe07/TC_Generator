# G198 —— `axis` 之正向判準重判（R-P283）

> **判準之改法**：舊法以二條之 **token 差**為輸入，其失在於 token 脫離語義框架（`20` / `60` 只是數字）。新法改以**相異之整行**為輸入。
> **判序**：`boundary → input_data → timing → trigger_state → mode`；
> `input_data` 前移至第二（其形態最具語法特徵）；
> **五者皆未命中者標「無對應」並停**（R-P283(c)：末項不得為預設落點）。

## 一、六值分布（前 → 後）

| 值 | 前 | 後 |
|---|---|---|
| `**無對應**` | 0 | **6** |
| `boundary` | 5 | **4** |
| `input_data` | 88 | **94** |
| `mode` | 42 | **10** |
| `timing` | 17 | **13** |
| `trigger_state` | 67 | **92** |

**`input_data` 88 → 94；移出 34 條。**

## 二、自 `input_data` 移出者（**34** 條）

| tc | 舊 | 新 | 依據 |
|---|---|---|---|
| `…-010` | `input_data` | **`timing`** | 對照 `007`，相異行命中 timing：`to the end of` |
| `…-020` | `input_data` | **`mode`** | 對照 `021`，相異行命中 mode：`Radio is present` |
| `…-021` | `input_data` | **`mode`** | 對照 `020`，相異行命中 mode：`Radio other than` |
| `…-024` | `input_data` | **`trigger_state`** | 對照 `025`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-026` | `input_data` | **`trigger_state`** | 對照 `024`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-035` | `input_data` | **`trigger_state`** | 對照 `040`，相異行命中 trigger_state：`is in Timed` |
| `…-037` | `input_data` | **`trigger_state`** | 對照 `038`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-038` | `input_data` | **`trigger_state`** | 對照 `037`，相異行命中 trigger_state：`RemStartFail` |
| `…-040` | `input_data` | **`trigger_state`** | 對照 `035`，相異行命中 trigger_state：`is in Timed` |
| `…-051` | `input_data` | **`trigger_state`** | 對照 `053`，相異行命中 trigger_state：`ignition working condition` |
| `…-052` | `input_data` | **`trigger_state`** | 對照 `051`，相異行命中 trigger_state：`ignition working condition` |
| `…-053` | `input_data` | **`trigger_state`** | 對照 `051`，相異行命中 trigger_state：`ignition working condition` |
| `…-054` | `input_data` | **`trigger_state`** | 對照 `051`，相異行命中 trigger_state：`ignition working condition` |
| `…-057` | `input_data` | **`trigger_state`** | 對照 `065`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-065` | `input_data` | **`trigger_state`** | 對照 `057`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-078` | `input_data` | **`trigger_state`** | 對照 `079`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-105` | `input_data` | **`trigger_state`** | 對照 `106`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-106` | `input_data` | **`trigger_state`** | 對照 `105`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-113` | `input_data` | **`trigger_state`** | 對照 `112`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-115` | `input_data` | **`trigger_state`** | 對照 `114`，相異行命中 trigger_state：`VPLastStatus` |
| `…-157` | `input_data` | **`timing`** | 對照 `158`，相異行命中 timing：`boot of the TLM has been completed` |
| `…-158` | `input_data` | **`timing`** | 對照 `157`，相異行命中 timing：`boot of the TLM is not ended` |
| `…-163` | `input_data` | **`**無對應**`** | 對照 `164`，五個正向判準皆未命中；相異行：3. The display is on the phone main scre ／ 3. The display is on the phone projectio |
| `…-164` | `input_data` | **`**無對應**`** | 對照 `163`，五個正向判準皆未命中；相異行：3. The display is on the phone projectio ／ 3. The display is on the phone main scre |
| `…-172` | `input_data` | **`trigger_state`** | 對照 `173`，相異行命中 trigger_state：`is not installing` |
| `…-173` | `input_data` | **`trigger_state`** | 對照 `172`，相異行命中 trigger_state：`is currently installing` |
| `…-187` | `input_data` | **`trigger_state`** | 對照 `189`，相異行命中 trigger_state：`has not yet played` |
| `…-198` | `input_data` | **`trigger_state`** | 對照 `200`，相異行命中 trigger_state：`Ignition On` |
| `…-199` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`Ignition Pre_Start` |
| `…-200` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`working condition` |
| `…-201` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`working condition` |
| `…-202` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`Ignition On` |
| `…-259` | `input_data` | **`trigger_state`** | 對照 `260`，相異行命中 trigger_state：`Ignition On` |
| `…-260` | `input_data` | **`trigger_state`** | 對照 `259`，相異行命中 trigger_state：`Ignition On` |

## 三、無對應（**6** 條）—— 不逕歸末項

| tc | 舊 | 依據 |
|---|---|---|
| `…-001` | `mode` | 對照 `004`，五個正向判準皆未命中；相異行：1. Start the suspend-resume boot sequenc ／ 1. Start the suspend-resume boot sequenc |
| `…-004` | `timing` | 對照 `001`，五個正向判準皆未命中；相異行：1. Start the suspend-resume boot sequenc ／ 1. Start the suspend-resume boot sequenc |
| `…-163` | `input_data` | 對照 `164`，五個正向判準皆未命中；相異行：3. The display is on the phone main scre ／ 3. The display is on the phone projectio |
| `…-164` | `input_data` | 對照 `163`，五個正向判準皆未命中；相異行：3. The display is on the phone projectio ／ 3. The display is on the phone main scre |
| `…-203` | `mode` | 對照 `204`，五個正向判準皆未命中；相異行：1. Bring the HU to Timed mode for the fi ／ 1. Bring the HU to Full Operation mode f |
| `…-204` | `mode` | 對照 `203`，五個正向判準皆未命中；相異行：1. Bring the HU to Full Operation mode f ／ 1. Bring the HU to Timed mode for the fi |

## 四、逐條

| tc | 舊 | 新 | 依據 |
|---|---|---|---|
| `…-001` | `mode` | **`**無對應**`** | 對照 `004`，五個正向判準皆未命中；相異行：1. Start the suspend-resume boot sequenc ／ 1. Start the suspend-resume boot sequenc |
| `…-002` | `mode` | `mode` | 對照 `001`，相異行命中 mode：`boot target status` |
| `…-003` | `mode` | `mode` | 對照 `001`，相異行命中 mode：`boot target status` |
| `…-004` | `timing` | **`**無對應**`** | 對照 `001`，五個正向判準皆未命中；相異行：1. Start the suspend-resume boot sequenc ／ 1. Start the suspend-resume boot sequenc |
| `…-006` | `trigger_state` | **`input_data`** | 對照 `015`，相異行命中 input_data：`Starting volume level: 2` |
| `…-007` | `trigger_state` | **`timing`** | 對照 `010`，相異行命中 timing：`to the end of` |
| `…-008` | `mode` | **`input_data`** | 對照 `016`，相異行命中 input_data：`Starting volume level: 2` |
| `…-009` | `timing` | **`trigger_state`** | 對照 `012`，相異行命中 trigger_state：`is already active` |
| `…-010` | `input_data` | **`timing`** | 對照 `007`，相異行命中 timing：`to the end of` |
| `…-011` | `trigger_state` | `trigger_state` | 對照 `006`，相異行命中 trigger_state：`call is active` |
| `…-012` | `trigger_state` | `trigger_state` | 對照 `008`，相異行命中 trigger_state：`call is active` |
| `…-013` | `mode` | **`trigger_state`** | 對照 `008`，相異行命中 trigger_state：`is in BODY OFF-TIMED` |
| `…-014` | `mode` | **`input_data`** | 對照 `009`，相異行命中 input_data：`STATUS_LIN.Batt_ST_Crit = [` |
| `…-015` | `input_data` | `input_data` | 對照 `006`，相異行命中 input_data：`Starting volume level: 1` |
| `…-016` | `trigger_state` | **`input_data`** | 對照 `008`，相異行命中 input_data：`Starting volume level: 1` |
| `…-017` | `input_data` | `input_data` | 對照 `018`，相異行命中 input_data：`PROXI parameter` |
| `…-018` | `input_data` | `input_data` | 對照 `017`，相異行命中 input_data：`PROXI parameter` |
| `…-019` | `input_data` | `input_data` | 對照 `017`，相異行命中 input_data：`PROXI parameter` |
| `…-020` | `input_data` | **`mode`** | 對照 `021`，相異行命中 mode：`Radio is present` |
| `…-021` | `input_data` | **`mode`** | 對照 `020`，相異行命中 mode：`Radio other than` |
| `…-022` | `mode` | **`trigger_state`** | 對照 `023`，相異行命中 trigger_state：`is in Full-Operation` |
| `…-023` | `mode` | **`trigger_state`** | 對照 `022`，相異行命中 trigger_state：`is in Timed` |
| `…-024` | `input_data` | **`trigger_state`** | 對照 `025`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-025` | `boundary` | **`trigger_state`** | 對照 `024`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-026` | `input_data` | **`trigger_state`** | 對照 `024`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-028` | `timing` | `timing` | 對照 `029`，相異行命中 timing：`expiration` |
| `…-029` | `timing` | `timing` | 對照 `028`，相異行命中 timing：`expiration` |
| `…-030` | `timing` | `timing` | 對照 `031`，相異行命中 timing：`before the call` |
| `…-031` | `timing` | `timing` | 對照 `030`，相異行命中 timing：`before Timeout1` |
| `…-032` | `timing` | `timing` | 對照 `038`，相異行命中 timing：`before Timeout1` |
| `…-033` | `timing` | `timing` | 對照 `032`，相異行命中 timing：`before the call` |
| `…-034` | `trigger_state` | `trigger_state` | 對照 `037`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-035` | `input_data` | **`trigger_state`** | 對照 `040`，相異行命中 trigger_state：`is in Timed` |
| `…-036` | `timing` | `timing` | 對照 `035`，相異行命中 timing：`expiration` |
| `…-037` | `input_data` | **`trigger_state`** | 對照 `038`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-038` | `input_data` | **`trigger_state`** | 對照 `037`，相異行命中 trigger_state：`RemStartFail` |
| `…-039` | `input_data` | `input_data` | 對照 `042`，相異行命中 input_data：`Ignition working condition: "` |
| `…-040` | `input_data` | **`trigger_state`** | 對照 `035`，相異行命中 trigger_state：`is in Timed` |
| `…-041` | `timing` | `timing` | 對照 `040`，相異行命中 timing：`expiration` |
| `…-042` | `input_data` | `input_data` | 對照 `039`，相異行命中 input_data：`Ignition working condition: "` |
| `…-043` | `input_data` | `input_data` | 對照 `048`，相異行命中 input_data：`short press` |
| `…-044` | `mode` | **`input_data`** | 對照 `045`，相異行命中 input_data：`CarPlay request: a` |
| `…-045` | `mode` | **`input_data`** | 對照 `046`，相異行命中 input_data：`CarPlay request: a` |
| `…-046` | `mode` | **`input_data`** | 對照 `045`，相異行命中 input_data：`CarPlay request: v` |
| `…-047` | `mode` | **`input_data`** | 對照 `045`，相異行命中 input_data：`CarPlay request: n` |
| `…-048` | `input_data` | `input_data` | 對照 `043`，相異行命中 input_data：`long press` |
| `…-049` | `trigger_state` | `trigger_state` | 對照 `050`，相異行命中 trigger_state：`VPLastStatus` |
| `…-050` | `trigger_state` | `trigger_state` | 對照 `049`，相異行命中 trigger_state：`VPLastStatus` |
| `…-051` | `input_data` | **`trigger_state`** | 對照 `053`，相異行命中 trigger_state：`ignition working condition` |
| `…-052` | `input_data` | **`trigger_state`** | 對照 `051`，相異行命中 trigger_state：`ignition working condition` |
| `…-053` | `input_data` | **`trigger_state`** | 對照 `051`，相異行命中 trigger_state：`ignition working condition` |
| `…-054` | `input_data` | **`trigger_state`** | 對照 `051`，相異行命中 trigger_state：`ignition working condition` |
| `…-055` | `mode` | **`trigger_state`** | 對照 `051`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-056` | `mode` | **`trigger_state`** | 對照 `055`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-057` | `input_data` | **`trigger_state`** | 對照 `065`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-058` | `timing` | `timing` | 對照 `060`，相異行命中 timing：`after the RemStartFail transition` |
| `…-059` | `mode` | **`trigger_state`** | 對照 `060`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-060` | `mode` | **`trigger_state`** | 對照 `059`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-061` | `trigger_state` | `trigger_state` | 對照 `062`，相異行命中 trigger_state：`PhoneCall.Info` |
| `…-062` | `trigger_state` | `trigger_state` | 對照 `060`，相異行命中 trigger_state：`SwitchOff_Timeout_Setting.Req` |
| `…-063` | `trigger_state` | `trigger_state` | 對照 `060`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-064` | `trigger_state` | `trigger_state` | 對照 `063`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-065` | `input_data` | **`trigger_state`** | 對照 `057`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-066` | `trigger_state` | **`input_data`** | 對照 `068`，相異行命中 input_data：`Rear_View_Camera reads "Present` |
| `…-067` | `trigger_state` | **`input_data`** | 對照 `069`，相異行命中 input_data：`Rear_View_Camera reads "Present` |
| `…-068` | `trigger_state` | **`input_data`** | 對照 `066`，相異行命中 input_data：`Rear_View_Camera reads "Present` |
| `…-069` | `trigger_state` | **`input_data`** | 對照 `067`，相異行命中 input_data：`Rear_View_Camera reads "Present` |
| `…-072` | `input_data` | `input_data` | 對照 `073`，相異行命中 input_data：`LTM_OperationalModeSts: "` |
| `…-073` | `input_data` | `input_data` | 對照 `072`，相異行命中 input_data：`LTM_OperationalModeSts: "` |
| `…-074` | `trigger_state` | `trigger_state` | 對照 `075`，相異行命中 trigger_state：`Rear_Camera_Enable.Info` |
| `…-075` | `trigger_state` | `trigger_state` | 對照 `074`，相異行命中 trigger_state：`Rear_Camera_Enable.Info` |
| `…-076` | `trigger_state` | `trigger_state` | 對照 `077`，相異行命中 trigger_state：`Rear_Camera_Enable.Info` |
| `…-077` | `trigger_state` | `trigger_state` | 對照 `076`，相異行命中 trigger_state：`Rear_Camera_Enable.Info` |
| `…-078` | `input_data` | **`trigger_state`** | 對照 `079`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-079` | `trigger_state` | `trigger_state` | 對照 `080`，相異行命中 trigger_state：`TLM_Display.GUI` |
| `…-080` | `trigger_state` | `trigger_state` | 對照 `079`，相異行命中 trigger_state：`TLM_Display.GUI` |
| `…-085` | `trigger_state` | `trigger_state` | 對照 `088`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-086` | `trigger_state` | `trigger_state` | 對照 `087`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-087` | `trigger_state` | `trigger_state` | 對照 `086`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-088` | `trigger_state` | `trigger_state` | 對照 `085`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-089` | `trigger_state` | `trigger_state` | 對照 `092`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-090` | `trigger_state` | **`input_data`** | 對照 `091`，相異行命中 input_data：`Accept the CLIMATIC_PANEL.Radio_Btn0 popup` |
| `…-091` | `trigger_state` | **`input_data`** | 對照 `090`，相異行命中 input_data：`Decline the CLIMATIC_PANEL.Radio_Btn0 popup` |
| `…-092` | `trigger_state` | `trigger_state` | 對照 `089`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-093` | `trigger_state` | `trigger_state` | 對照 `095`，相異行命中 trigger_state：`Full-Operation` |
| `…-094` | `trigger_state` | `trigger_state` | 對照 `095`，相異行命中 trigger_state：`PhoneCall.Info` |
| `…-095` | `trigger_state` | `trigger_state` | 對照 `093`，相異行命中 trigger_state：`Full-Operation` |
| `…-096` | `trigger_state` | **`input_data`** | 對照 `093`，相異行命中 input_data：`Brand_Configuration_2 reads a value other than ` |
| `…-097` | `timing` | **`trigger_state`** | 對照 `098`，相異行命中 trigger_state：`Antitheft_Activation.Req` |
| `…-098` | `timing` | **`trigger_state`** | 對照 `097`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-099` | `trigger_state` | `trigger_state` | 對照 `100`，相異行命中 trigger_state：`Antitheft_Activation.Req` |
| `…-100` | `trigger_state` | `trigger_state` | 對照 `099`，相異行命中 trigger_state：`SwitchOff_Timeout_Setting.Req` |
| `…-101` | `trigger_state` | `trigger_state` | 對照 `099`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-102` | `trigger_state` | `trigger_state` | 對照 `103`，相異行命中 trigger_state：`Antitheft_Activation.Req` |
| `…-103` | `timing` | **`input_data`** | 對照 `104`，相異行命中 input_data：`Switch_Off_Time reads 20 minutes` |
| `…-104` | `timing` | **`input_data`** | 對照 `103`，相異行命中 input_data：`$PwrAccDelayAct$ reads 10 minutes` |
| `…-105` | `input_data` | **`trigger_state`** | 對照 `106`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-106` | `input_data` | **`trigger_state`** | 對照 `105`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-109` | `input_data` | `input_data` | 對照 `110`，相異行命中 input_data：`LTM_OperationalModeSts: t` |
| `…-110` | `input_data` | `input_data` | 對照 `109`，相異行命中 input_data：`LTM_OperationalModeSts: t` |
| `…-112` | `trigger_state` | `trigger_state` | 對照 `113`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-113` | `input_data` | **`trigger_state`** | 對照 `112`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-114` | `trigger_state` | `trigger_state` | 對照 `115`，相異行命中 trigger_state：`VPLastStatus` |
| `…-115` | `input_data` | **`trigger_state`** | 對照 `114`，相異行命中 trigger_state：`VPLastStatus` |
| `…-118` | `timing` | **`trigger_state`** | 對照 `119`，相異行命中 trigger_state：`Ignition On` |
| `…-119` | `trigger_state` | **`mode`** | 對照 `120`，相異行命中 mode：`LTM High` |
| `…-120` | `trigger_state` | **`mode`** | 對照 `119`，相異行命中 mode：`LTM High` |
| `…-121` | `timing` | **`trigger_state`** | 對照 `118`，相異行命中 trigger_state：`Ignition On` |
| `…-123` | `trigger_state` | `trigger_state` | 對照 `124`，相異行命中 trigger_state：`Ignition Off` |
| `…-124` | `trigger_state` | `trigger_state` | 對照 `123`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-125` | `trigger_state` | `trigger_state` | 對照 `126`，相異行命中 trigger_state：`Ignition Off` |
| `…-126` | `trigger_state` | `trigger_state` | 對照 `125`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-127` | `mode` | **`trigger_state`** | 對照 `128`，相異行命中 trigger_state：`is in Standby` |
| `…-128` | `mode` | **`trigger_state`** | 對照 `127`，相異行命中 trigger_state：`is in Standby` |
| `…-129` | `mode` | **`input_data`** | 對照 `131`，相異行命中 input_data：`Front_Panel_OnOff.Req: "` |
| `…-130` | `mode` | **`input_data`** | 對照 `132`，相異行命中 input_data：`Front_Panel_OnOff.Req: "` |
| `…-131` | `mode` | **`input_data`** | 對照 `129`，相異行命中 input_data：`CLIMATIC_PANEL.Radio_Btn0: "` |
| `…-132` | `mode` | **`input_data`** | 對照 `130`，相異行命中 input_data：`CLIMATIC_PANEL.Radio_Btn0: "` |
| `…-133` | `mode` | **`trigger_state`** | 對照 `134`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-134` | `mode` | **`trigger_state`** | 對照 `133`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-135` | `input_data` | `input_data` | 對照 `136`，相異行命中 input_data：`Antitheft_Result.Info: "` |
| `…-136` | `input_data` | `input_data` | 對照 `135`，相異行命中 input_data：`Antitheft_Result.Info: "` |
| `…-137` | `mode` | **`trigger_state`** | 對照 `138`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-138` | `mode` | **`trigger_state`** | 對照 `137`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-139` | `mode` | **`trigger_state`** | 對照 `140`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-140` | `mode` | **`trigger_state`** | 對照 `139`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-141` | `mode` | **`trigger_state`** | 對照 `142`，相異行命中 trigger_state：`VPLastStatus` |
| `…-142` | `mode` | **`trigger_state`** | 對照 `141`，相異行命中 trigger_state：`VPLastStatus` |
| `…-143` | `trigger_state` | `trigger_state` | 對照 `141`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-149` | `input_data` | `input_data` | 對照 `150`，相異行命中 input_data：`Audio_Brand: "` |
| `…-150` | `input_data` | `input_data` | 對照 `149`，相異行命中 input_data：`Audio_Brand: "` |
| `…-151` | `input_data` | `input_data` | 對照 `152`，相異行命中 input_data：`Audio_Brand: "` |
| `…-152` | `input_data` | `input_data` | 對照 `151`，相異行命中 input_data：`Audio_Brand: "` |
| `…-153` | `boundary` | `boundary` | 對照 `154`，相異行命中 boundary：`greater than` |
| `…-154` | `boundary` | `boundary` | 對照 `153`，相異行命中 boundary：`greater than` |
| `…-157` | `input_data` | **`timing`** | 對照 `158`，相異行命中 timing：`boot of the TLM has been completed` |
| `…-158` | `input_data` | **`timing`** | 對照 `157`，相異行命中 timing：`boot of the TLM is not ended` |
| `…-159` | `input_data` | `input_data` | 對照 `160`，相異行**僅出自 `input_test_data`**：`An SOS call is placed` |
| `…-160` | `input_data` | `input_data` | 對照 `159`，相異行**僅出自 `input_test_data`**：`An Assist call is placed` |
| `…-163` | `input_data` | **`**無對應**`** | 對照 `164`，五個正向判準皆未命中；相異行：3. The display is on the phone main scre ／ 3. The display is on the phone projectio |
| `…-164` | `input_data` | **`**無對應**`** | 對照 `163`，五個正向判準皆未命中；相異行：3. The display is on the phone projectio ／ 3. The display is on the phone main scre |
| `…-166` | `input_data` | `input_data` | 對照 `167`，相異行**僅出自 `input_test_data`**：`A FOTA update available for the Radio` |
| `…-167` | `input_data` | `input_data` | 對照 `168`，相異行**僅出自 `input_test_data`**：`A FOTA update available for the TBM` |
| `…-168` | `input_data` | `input_data` | 對照 `167`，相異行**僅出自 `input_test_data`**：`A FOTA update available for the ROV` |
| `…-169` | `mode` | **`input_data`** | 對照 `170`，相異行命中 input_data：`Leave the FOTA pop-up` |
| `…-170` | `mode` | **`input_data`** | 對照 `169`，相異行命中 input_data：`Dismiss the FOTA pop-up` |
| `…-171` | `trigger_state` | **`input_data`** | 對照 `170`，相異行命中 input_data：`$ACCDlyAct$: a` |
| `…-172` | `input_data` | **`trigger_state`** | 對照 `173`，相異行命中 trigger_state：`is not installing` |
| `…-173` | `input_data` | **`trigger_state`** | 對照 `172`，相異行命中 trigger_state：`is currently installing` |
| `…-174` | `mode` | **`trigger_state`** | 對照 `175`，相異行命中 trigger_state：`is in SLEEP` |
| `…-175` | `mode` | **`trigger_state`** | 對照 `174`，相異行命中 trigger_state：`is in STANDBY` |
| `…-176` | `mode` | **`trigger_state`** | 對照 `174`，相異行命中 trigger_state：`is in PARTIAL OPERATION` |
| `…-177` | `trigger_state` | **`input_data`** | 對照 `181`，相異行命中 input_data：`$Door_Ajar_Status$ reads OPEN` |
| `…-178` | `mode` | **`input_data`** | 對照 `179`，相異行命中 input_data：`$PowerMode$: "` |
| `…-179` | `trigger_state` | **`input_data`** | 對照 `180`，相異行命中 input_data：`$PowerMode$: "` |
| `…-180` | `trigger_state` | **`input_data`** | 對照 `179`，相異行命中 input_data：`$PowerMode$: "` |
| `…-181` | `trigger_state` | **`input_data`** | 對照 `175`，相異行命中 input_data：`$Door_Ajar_Status$ reads OPEN` |
| `…-182` | `trigger_state` | `trigger_state` | 對照 `177`，相異行命中 trigger_state：`is in STANDBY` |
| `…-187` | `input_data` | **`trigger_state`** | 對照 `189`，相異行命中 trigger_state：`has not yet played` |
| `…-188` | `input_data` | `input_data` | 對照 `190`，相異行**僅出自 `input_test_data`**：`A manual time adjustment that changes the cust` |
| `…-189` | `input_data` | `input_data` | 對照 `188`，相異行命中 input_data：`NA` |
| `…-190` | `input_data` | `input_data` | 對照 `188`，相異行**僅出自 `input_test_data`**：`An automatic adjustment due to time zones or D` |
| `…-192` | `input_data` | `input_data` | 對照 `193`，相異行命中 input_data：`Audio_Brand: "` |
| `…-193` | `input_data` | `input_data` | 對照 `192`，相異行命中 input_data：`Audio_Brand: "` |
| `…-194` | `input_data` | `input_data` | 對照 `195`，相異行命中 input_data：`Audio_Brand: "` |
| `…-195` | `input_data` | `input_data` | 對照 `194`，相異行命中 input_data：`Audio_Brand: "` |
| `…-196` | `boundary` | `boundary` | 對照 `197`，相異行命中 boundary：`greater than` |
| `…-197` | `boundary` | `boundary` | 對照 `196`，相異行命中 boundary：`greater than` |
| `…-198` | `input_data` | **`trigger_state`** | 對照 `200`，相異行命中 trigger_state：`Ignition On` |
| `…-199` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`Ignition Pre_Start` |
| `…-200` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`working condition` |
| `…-201` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`working condition` |
| `…-202` | `input_data` | **`trigger_state`** | 對照 `198`，相異行命中 trigger_state：`Ignition On` |
| `…-203` | `mode` | **`**無對應**`** | 對照 `204`，五個正向判準皆未命中；相異行：1. Bring the HU to Timed mode for the fi ／ 1. Bring the HU to Full Operation mode f |
| `…-204` | `mode` | **`**無對應**`** | 對照 `203`，五個正向判準皆未命中；相異行：1. Bring the HU to Full Operation mode f ／ 1. Bring the HU to Timed mode for the fi |
| `…-205` | `mode` | **`trigger_state`** | 對照 `206`，相異行命中 trigger_state：`is in Idle` |
| `…-206` | `mode` | **`trigger_state`** | 對照 `205`，相異行命中 trigger_state：`is in Standby` |
| `…-207` | `mode` | **`trigger_state`** | 對照 `205`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-208` | `input_data` | `input_data` | 對照 `214`，相異行命中 input_data：`at the moment of` |
| `…-209` | `input_data` | `input_data` | 對照 `214`，相異行命中 input_data：`at the moment of` |
| `…-210` | `input_data` | `input_data` | 對照 `214`，相異行命中 input_data：`at the moment of` |
| `…-211` | `input_data` | `input_data` | 對照 `214`，相異行命中 input_data：`at the moment of` |
| `…-212` | `input_data` | `input_data` | 對照 `214`，相異行命中 input_data：`at the moment of` |
| `…-213` | `input_data` | `input_data` | 對照 `214`，相異行命中 input_data：`at the moment of` |
| `…-214` | `input_data` | `input_data` | 對照 `208`，相異行命中 input_data：`at the moment of` |
| `…-215` | `mode` | **`input_data`** | 對照 `214`，相異行命中 input_data：`NA` |
| `…-220` | `trigger_state` | **`input_data`** | 對照 `221`，相異行命中 input_data：`$TBM_Present$ reads "Not Present` |
| `…-221` | `trigger_state` | **`input_data`** | 對照 `220`，相異行命中 input_data：`$TBM_Present$ reads "Present` |
| `…-222` | `trigger_state` | **`input_data`** | 對照 `223`，相異行命中 input_data：`$TBM_Present$ reads "Not Present` |
| `…-223` | `trigger_state` | **`input_data`** | 對照 `222`，相異行命中 input_data：`$TBM_Present$ reads "Not Present` |
| `…-228` | `input_data` | `input_data` | 對照 `229`，相異行命中 input_data：`$VC_SpecialPKG$: "` |
| `…-229` | `input_data` | `input_data` | 對照 `228`，相異行命中 input_data：`$VC_SpecialPKG$: a` |
| `…-231` | `trigger_state` | **`input_data`** | 對照 `232`，相異行命中 input_data：`NA` |
| `…-232` | `trigger_state` | **`input_data`** | 對照 `231`，相異行命中 input_data：`$VC_SpecialPKG$: a` |
| `…-233` | `input_data` | `input_data` | 對照 `234`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-234` | `input_data` | `input_data` | 對照 `235`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-235` | `input_data` | `input_data` | 對照 `234`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-236` | `input_data` | `input_data` | 對照 `237`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-237` | `input_data` | `input_data` | 對照 `238`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-238` | `input_data` | `input_data` | 對照 `237`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-239` | `input_data` | `input_data` | 對照 `240`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-240` | `input_data` | `input_data` | 對照 `239`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-241` | `input_data` | `input_data` | 對照 `239`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-242` | `trigger_state` | **`mode`** | 對照 `243`，相異行命中 mode：`Atlantis` |
| `…-243` | `trigger_state` | **`mode`** | 對照 `242`，相異行命中 mode：`architecture` |
| `…-244` | `trigger_state` | **`mode`** | 對照 `245`，相異行命中 mode：`Atlantis` |
| `…-245` | `trigger_state` | **`mode`** | 對照 `244`，相異行命中 mode：`architecture` |
| `…-246` | `trigger_state` | **`input_data`** | 對照 `247`，相異行命中 input_data：`NA` |
| `…-247` | `trigger_state` | **`input_data`** | 對照 `246`，相異行命中 input_data：`$VC_SpecialPKG$: a` |
| `…-248` | `trigger_state` | **`input_data`** | 對照 `249`，相異行命中 input_data：`$VC_VEH_LINE$: "` |
| `…-249` | `trigger_state` | **`input_data`** | 對照 `248`，相異行命中 input_data：`$VC_VEH_LINE$: a` |
| `…-251` | `input_data` | `input_data` | 對照 `252`，相異行命中 input_data：`$Day_Night_Mode$: t` |
| `…-252` | `input_data` | `input_data` | 對照 `251`，相異行命中 input_data：`$Day_Night_Mode$: t` |
| `…-255` | `input_data` | `input_data` | 對照 `256`，相異行命中 input_data：`is set to` |
| `…-256` | `input_data` | `input_data` | 對照 `257`，相異行命中 input_data：`is set to` |
| `…-257` | `input_data` | `input_data` | 對照 `256`，相異行命中 input_data：`is set to` |
| `…-258` | `input_data` | `input_data` | 對照 `256`，相異行命中 input_data：`is set to` |
| `…-259` | `input_data` | **`trigger_state`** | 對照 `260`，相異行命中 trigger_state：`Ignition On` |
| `…-260` | `input_data` | **`trigger_state`** | 對照 `259`，相異行命中 trigger_state：`Ignition On` |
