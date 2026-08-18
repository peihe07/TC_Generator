# G198 —— `axis` 之正向判準重判（R-P283）

> **判準之改法**：舊法以二條之 **token 差**為輸入，其失在於 token 脫離語義框架（`20` / `60` 只是數字）。新法改以**相異之整行**為輸入。
> **判序**：`boundary → input_data → timing → trigger_state → mode`；
> `input_data` 前移至第二（其形態最具語法特徵）；
> **五者皆未命中者標「無對應」並停**（R-P283(c)：末項不得為預設落點）。

## 一、六值分布（前 → 後）

| 值 | 前 | 後 |
|---|---|---|
| `**無對應**` | 0 | **43** |
| `boundary` | 5 | **2** |
| `input_data` | 90 | **59** |
| `mode` | 42 | **6** |
| `timing` | 18 | **19** |
| `trigger_state` | 69 | **95** |

**`input_data` 90 → 59；移出 64 條。**

## 二、自 `input_data` 移出者（**64** 條）

| tc | 舊 | 新 | 依據 |
|---|---|---|---|
| `…-005` | `input_data` | **`**無對應**`** | 對照 `006`，五個正向判準皆未命中；相異行：（無） |
| `…-011` | `input_data` | **`trigger_state`** | 對照 `008`，相異行命中 trigger_state：`STATUS_LIN.` |
| `…-021` | `input_data` | **`mode`** | 對照 `022`，相異行命中 mode：`Radio is present` |
| `…-022` | `input_data` | **`mode`** | 對照 `021`，相異行命中 mode：`Radio other than` |
| `…-025` | `input_data` | **`trigger_state`** | 對照 `026`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-027` | `input_data` | **`trigger_state`** | 對照 `025`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-036` | `input_data` | **`trigger_state`** | 對照 `041`，相異行命中 trigger_state：`is in Timed` |
| `…-038` | `input_data` | **`trigger_state`** | 對照 `039`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-039` | `input_data` | **`trigger_state`** | 對照 `038`，相異行命中 trigger_state：`RemStartFail` |
| `…-040` | `input_data` | **`trigger_state`** | 對照 `043`，相異行命中 trigger_state：`Ignition working condition` |
| `…-041` | `input_data` | **`timing`** | 對照 `042`，相異行命中 timing：`before MaxCallTimeout expires` |
| `…-043` | `input_data` | **`trigger_state`** | 對照 `040`，相異行命中 trigger_state：`Ignition working condition` |
| `…-044` | `input_data` | **`**無對應**`** | 對照 `049`，五個正向判準皆未命中；相異行：1. Press the VR button with a short pres |
| `…-049` | `input_data` | **`**無對應**`** | 對照 `044`，五個正向判準皆未命中；相異行：1. Press the VR button with a long press |
| `…-052` | `input_data` | **`trigger_state`** | 對照 `053`，相異行命中 trigger_state：`ignition working condition` |
| `…-053` | `input_data` | **`trigger_state`** | 對照 `052`，相異行命中 trigger_state：`ignition working condition` |
| `…-054` | `input_data` | **`trigger_state`** | 對照 `052`，相異行命中 trigger_state：`ignition working condition` |
| `…-055` | `input_data` | **`trigger_state`** | 對照 `052`，相異行命中 trigger_state：`ignition working condition` |
| `…-058` | `input_data` | **`trigger_state`** | 對照 `066`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-066` | `input_data` | **`trigger_state`** | 對照 `058`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-073` | `input_data` | **`trigger_state`** | 對照 `074`，相異行命中 trigger_state：`Ignition Off` |
| `…-074` | `input_data` | **`trigger_state`** | 對照 `073`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-079` | `input_data` | **`trigger_state`** | 對照 `080`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-108` | `input_data` | **`trigger_state`** | 對照 `109`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-109` | `input_data` | **`trigger_state`** | 對照 `108`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-112` | `input_data` | **`trigger_state`** | 對照 `113`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-113` | `input_data` | **`trigger_state`** | 對照 `112`，相異行命中 trigger_state：`Ignition Off` |
| `…-116` | `input_data` | **`trigger_state`** | 對照 `115`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-118` | `input_data` | **`trigger_state`** | 對照 `117`，相異行命中 trigger_state：`VPLastStatus` |
| `…-138` | `input_data` | **`trigger_state`** | 對照 `139`，相異行命中 trigger_state：`Antitheft_Result.Info` |
| `…-139` | `input_data` | **`trigger_state`** | 對照 `138`，相異行命中 trigger_state：`Antitheft_Result.Info` |
| `…-160` | `input_data` | **`timing`** | 對照 `161`，相異行命中 timing：`boot of the TLM has been completed` |
| `…-161` | `input_data` | **`timing`** | 對照 `160`，相異行命中 timing：`boot of the TLM is not ended` |
| `…-162` | `input_data` | **`**無對應**`** | 對照 `163`，五個正向判準皆未命中；相異行：An SOS call is placed |
| `…-163` | `input_data` | **`**無對應**`** | 對照 `162`，五個正向判準皆未命中；相異行：An Assist call is placed |
| `…-166` | `input_data` | **`**無對應**`** | 對照 `167`，五個正向判準皆未命中；相異行：3. The display is on the phone main scre |
| `…-167` | `input_data` | **`**無對應**`** | 對照 `166`，五個正向判準皆未命中；相異行：3. The display is on the phone projectio |
| `…-169` | `input_data` | **`**無對應**`** | 對照 `170`，五個正向判準皆未命中；相異行：A FOTA update available for the Radio |
| `…-170` | `input_data` | **`**無對應**`** | 對照 `169`，五個正向判準皆未命中；相異行：A FOTA update available for the TBM |
| `…-171` | `input_data` | **`**無對應**`** | 對照 `169`，五個正向判準皆未命中；相異行：A FOTA update available for the ROV |
| `…-175` | `input_data` | **`**無對應**`** | 對照 `176`，五個正向判準皆未命中；相異行：（無） |
| `…-176` | `input_data` | **`**無對應**`** | 對照 `175`，五個正向判準皆未命中；相異行：（無） |
| `…-177` | `input_data` | **`**無對應**`** | 對照 `175`，五個正向判準皆未命中；相異行：2. The HU is currently installing a firm |
| `…-191` | `input_data` | **`**無對應**`** | 對照 `193`，五個正向判準皆未命中；相異行：4. The HU has not yet played the startup ／ 1. Bring the HU through a startup that p |
| `…-192` | `input_data` | **`**無對應**`** | 對照 `194`，五個正向判準皆未命中；相異行：A manual time adjustment that changes th |
| `…-194` | `input_data` | **`**無對應**`** | 對照 `192`，五個正向判準皆未命中；相異行：An automatic adjustment due to time zone |
| `…-202` | `input_data` | **`trigger_state`** | 對照 `203`，相異行命中 trigger_state：`Ignition On` |
| `…-203` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`Ignition Pre_Start` |
| `…-204` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`working condition` |
| `…-205` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`working condition` |
| `…-206` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`Ignition On` |
| `…-212` | `input_data` | **`**無對應**`** | 對照 `213`，五個正向判準皆未命中；相異行：An ongoing call at the moment of the tra |
| `…-213` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：A backup camera view at the moment of th |
| `…-214` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：An incoming call at the moment of the tr |
| `…-215` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：An outgoing call at the moment of the tr |
| `…-216` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：A climate pop-up at the moment of the tr |
| `…-217` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：An SOS or Assist call at the moment of t |
| `…-218` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：A FOTA pop up at the moment of the trans |
| `…-259` | `input_data` | **`timing`** | 對照 `260`，相異行命中 timing：`before the Summer start` |
| `…-260` | `input_data` | **`timing`** | 對照 `259`，相異行命中 timing：`before the Fall start` |
| `…-261` | `input_data` | **`timing`** | 對照 `259`，相異行命中 timing：`before the Winter start` |
| `…-262` | `input_data` | **`timing`** | 對照 `259`，相異行命中 timing：`before the Spring start` |
| `…-263` | `input_data` | **`trigger_state`** | 對照 `264`，相異行命中 trigger_state：`Ignition On` |
| `…-264` | `input_data` | **`trigger_state`** | 對照 `263`，相異行命中 trigger_state：`Ignition On` |

## 三、無對應（**43** 條）—— 不逕歸末項

| tc | 舊 | 依據 |
|---|---|---|
| `…-005` | `input_data` | 對照 `006`，五個正向判準皆未命中；相異行：（無） |
| `…-006` | `timing` | 對照 `005`，五個正向判準皆未命中；相異行：（無） |
| `…-044` | `input_data` | 對照 `049`，五個正向判準皆未命中；相異行：1. Press the VR button with a short pres |
| `…-049` | `input_data` | 對照 `044`，五個正向判準皆未命中；相異行：1. Press the VR button with a long press |
| `…-051` | `trigger_state` | 對照 `050`，五個正向判準皆未命中；相異行：2. The battery has just been reconnected ／ 1. Let the TLM exit INIT state |
| `…-067` | `trigger_state` | 對照 `069`，五個正向判準皆未命中；相異行：（無） |
| `…-068` | `trigger_state` | 對照 `070`，五個正向判準皆未命中；相異行：（無） |
| `…-080` | `trigger_state` | 對照 `081`，五個正向判準皆未命中；相異行：3. TLM_Display.GUI is in Phone Main Scre |
| `…-081` | `trigger_state` | 對照 `080`，五個正向判準皆未命中；相異行：3. TLM_Display.GUI is on a screen other  |
| `…-091` | `trigger_state` | 對照 `092`，五個正向判準皆未命中；相異行：1. Accept the CLIMATIC_PANEL.Radio_Btn0  |
| `…-092` | `trigger_state` | 對照 `091`，五個正向判準皆未命中；相異行：1. Decline the CLIMATIC_PANEL.Radio_Btn0 |
| `…-096` | `trigger_state` | 對照 `094`，五個正向判準皆未命中；相異行：4. The previous internal state was Stand |
| `…-100` | `trigger_state` | 對照 `102`，五個正向判準皆未命中；相異行：（無） |
| `…-102` | `trigger_state` | 對照 `100`，五個正向判準皆未命中；相異行：（無） |
| `…-104` | `trigger_state` | 對照 `107`，五個正向判準皆未命中；相異行：（無） |
| `…-107` | `trigger_state` | 對照 `104`，五個正向判準皆未命中；相異行：（無） |
| `…-130` | `mode` | 對照 `131`，五個正向判準皆未命中；相異行：3. No HMI screen is required ／ 1. Leave the HU in Standby mode without  |
| `…-162` | `input_data` | 對照 `163`，五個正向判準皆未命中；相異行：An SOS call is placed |
| `…-163` | `input_data` | 對照 `162`，五個正向判準皆未命中；相異行：An Assist call is placed |
| `…-166` | `input_data` | 對照 `167`，五個正向判準皆未命中；相異行：3. The display is on the phone main scre |
| `…-167` | `input_data` | 對照 `166`，五個正向判準皆未命中；相異行：3. The display is on the phone projectio |
| `…-169` | `input_data` | 對照 `170`，五個正向判準皆未命中；相異行：A FOTA update available for the Radio |
| `…-170` | `input_data` | 對照 `169`，五個正向判準皆未命中；相異行：A FOTA update available for the TBM |
| `…-171` | `input_data` | 對照 `169`，五個正向判準皆未命中；相異行：A FOTA update available for the ROV |
| `…-172` | `mode` | 對照 `173`，五個正向判準皆未命中；相異行：1. Leave the FOTA pop-up without any use |
| `…-173` | `mode` | 對照 `172`，五個正向判準皆未命中；相異行：1. Dismiss the FOTA pop-up on the screen |
| `…-175` | `input_data` | 對照 `176`，五個正向判準皆未命中；相異行：（無） |
| `…-176` | `input_data` | 對照 `175`，五個正向判準皆未命中；相異行：（無） |
| `…-177` | `input_data` | 對照 `175`，五個正向判準皆未命中；相異行：2. The HU is currently installing a firm |
| `…-184` | `trigger_state` | 對照 `182`，五個正向判準皆未命中；相異行：An HU power mode status change to TIMED  ／ 1. Send the change listed in Input Test  |
| `…-191` | `input_data` | 對照 `193`，五個正向判準皆未命中；相異行：4. The HU has not yet played the startup ／ 1. Bring the HU through a startup that p |
| `…-192` | `input_data` | 對照 `194`，五個正向判準皆未命中；相異行：A manual time adjustment that changes th |
| `…-194` | `input_data` | 對照 `192`，五個正向判準皆未命中；相異行：An automatic adjustment due to time zone |
| `…-207` | `mode` | 對照 `208`，五個正向判準皆未命中；相異行：1. Bring the HU to Timed mode for the fi |
| `…-208` | `mode` | 對照 `207`，五個正向判準皆未命中；相異行：1. Bring the HU to Full Operation mode f |
| `…-212` | `input_data` | 對照 `213`，五個正向判準皆未命中；相異行：An ongoing call at the moment of the tra |
| `…-213` | `input_data` | 對照 `212`，五個正向判準皆未命中；相異行：A backup camera view at the moment of th |
| `…-214` | `input_data` | 對照 `212`，五個正向判準皆未命中；相異行：An incoming call at the moment of the tr |
| `…-215` | `input_data` | 對照 `212`，五個正向判準皆未命中；相異行：An outgoing call at the moment of the tr |
| `…-216` | `input_data` | 對照 `212`，五個正向判準皆未命中；相異行：A climate pop-up at the moment of the tr |
| `…-217` | `input_data` | 對照 `212`，五個正向判準皆未命中；相異行：An SOS or Assist call at the moment of t |
| `…-218` | `input_data` | 對照 `212`，五個正向判準皆未命中；相異行：A FOTA pop up at the moment of the trans |
| `…-227` | `trigger_state` | 對照 `226`，五個正向判準皆未命中；相異行：4. $Country_Code$ does not require SOS o |

## 四、逐條

| tc | 舊 | 新 | 依據 |
|---|---|---|---|
| `…-001` | `mode` | **`timing`** | 對照 `002`，相異行命中 timing：`boot sequence` |
| `…-002` | `mode` | **`timing`** | 對照 `001`，相異行命中 timing：`boot sequence` |
| `…-003` | `mode` | **`timing`** | 對照 `001`，相異行命中 timing：`boot sequence` |
| `…-004` | `timing` | `timing` | 對照 `001`，相異行命中 timing：`boot sequence` |
| `…-005` | `input_data` | **`**無對應**`** | 對照 `006`，五個正向判準皆未命中；相異行：（無） |
| `…-006` | `timing` | **`**無對應**`** | 對照 `005`，五個正向判準皆未命中；相異行：（無） |
| `…-007` | `trigger_state` | **`input_data`** | 對照 `016`，相異行命中 input_data：`Starting volume level: 2` |
| `…-008` | `trigger_state` | **`timing`** | 對照 `011`，相異行命中 timing：`to the end of` |
| `…-009` | `mode` | **`input_data`** | 對照 `017`，相異行命中 input_data：`Starting volume level: 2` |
| `…-010` | `timing` | **`trigger_state`** | 對照 `015`，相異行命中 trigger_state：`STATUS_LIN.` |
| `…-011` | `input_data` | **`trigger_state`** | 對照 `008`，相異行命中 trigger_state：`STATUS_LIN.` |
| `…-012` | `trigger_state` | `trigger_state` | 對照 `007`，相異行命中 trigger_state：`call is active` |
| `…-013` | `trigger_state` | `trigger_state` | 對照 `009`，相異行命中 trigger_state：`call is active` |
| `…-014` | `mode` | **`trigger_state`** | 對照 `009`，相異行命中 trigger_state：`is in BODY OFF-TIMED` |
| `…-015` | `mode` | **`trigger_state`** | 對照 `010`，相異行命中 trigger_state：`STATUS_LIN.` |
| `…-016` | `input_data` | `input_data` | 對照 `007`，相異行命中 input_data：`Starting volume level: 1` |
| `…-017` | `trigger_state` | **`input_data`** | 對照 `009`，相異行命中 input_data：`Starting volume level: 1` |
| `…-018` | `input_data` | `input_data` | 對照 `019`，相異行命中 input_data：`PROXI parameter` |
| `…-019` | `input_data` | `input_data` | 對照 `018`，相異行命中 input_data：`PROXI parameter` |
| `…-020` | `input_data` | `input_data` | 對照 `018`，相異行命中 input_data：`PROXI parameter` |
| `…-021` | `input_data` | **`mode`** | 對照 `022`，相異行命中 mode：`Radio is present` |
| `…-022` | `input_data` | **`mode`** | 對照 `021`，相異行命中 mode：`Radio other than` |
| `…-023` | `mode` | **`trigger_state`** | 對照 `024`，相異行命中 trigger_state：`is in Full-Operation` |
| `…-024` | `mode` | **`trigger_state`** | 對照 `023`，相異行命中 trigger_state：`is in Timed` |
| `…-025` | `input_data` | **`trigger_state`** | 對照 `026`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-026` | `boundary` | **`trigger_state`** | 對照 `025`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-027` | `input_data` | **`trigger_state`** | 對照 `025`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-029` | `timing` | **`trigger_state`** | 對照 `030`，相異行命中 trigger_state：`is in Full-Operation` |
| `…-030` | `timing` | `timing` | 對照 `029`，相異行命中 timing：`expiration` |
| `…-031` | `timing` | `timing` | 對照 `032`，相異行命中 timing：`before the call` |
| `…-032` | `timing` | `timing` | 對照 `031`，相異行命中 timing：`before Timeout1` |
| `…-033` | `timing` | **`trigger_state`** | 對照 `034`，相異行命中 trigger_state：`is in Timed` |
| `…-034` | `timing` | `timing` | 對照 `033`，相異行命中 timing：`before the call` |
| `…-035` | `trigger_state` | **`timing`** | 對照 `034`，相異行命中 timing：`expiration` |
| `…-036` | `input_data` | **`trigger_state`** | 對照 `041`，相異行命中 trigger_state：`is in Timed` |
| `…-037` | `timing` | **`trigger_state`** | 對照 `042`，相異行命中 trigger_state：`is in Timed` |
| `…-038` | `input_data` | **`trigger_state`** | 對照 `039`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-039` | `input_data` | **`trigger_state`** | 對照 `038`，相異行命中 trigger_state：`RemStartFail` |
| `…-040` | `input_data` | **`trigger_state`** | 對照 `043`，相異行命中 trigger_state：`Ignition working condition` |
| `…-041` | `input_data` | **`timing`** | 對照 `042`，相異行命中 timing：`before MaxCallTimeout expires` |
| `…-042` | `timing` | `timing` | 對照 `041`，相異行命中 timing：`expiration` |
| `…-043` | `input_data` | **`trigger_state`** | 對照 `040`，相異行命中 trigger_state：`Ignition working condition` |
| `…-044` | `input_data` | **`**無對應**`** | 對照 `049`，五個正向判準皆未命中；相異行：1. Press the VR button with a short pres |
| `…-045` | `mode` | **`input_data`** | 對照 `046`，相異行命中 input_data：`CarPlay request: a` |
| `…-046` | `mode` | **`input_data`** | 對照 `045`，相異行命中 input_data：`CarPlay request: a` |
| `…-047` | `mode` | **`input_data`** | 對照 `045`，相異行命中 input_data：`CarPlay request: v` |
| `…-048` | `mode` | **`input_data`** | 對照 `045`，相異行命中 input_data：`CarPlay request: n` |
| `…-049` | `input_data` | **`**無對應**`** | 對照 `044`，五個正向判準皆未命中；相異行：1. Press the VR button with a long press |
| `…-050` | `trigger_state` | `trigger_state` | 對照 `051`，相異行命中 trigger_state：`VPLastStatus` |
| `…-051` | `trigger_state` | **`**無對應**`** | 對照 `050`，五個正向判準皆未命中；相異行：2. The battery has just been reconnected ／ 1. Let the TLM exit INIT state |
| `…-052` | `input_data` | **`trigger_state`** | 對照 `053`，相異行命中 trigger_state：`ignition working condition` |
| `…-053` | `input_data` | **`trigger_state`** | 對照 `052`，相異行命中 trigger_state：`ignition working condition` |
| `…-054` | `input_data` | **`trigger_state`** | 對照 `052`，相異行命中 trigger_state：`ignition working condition` |
| `…-055` | `input_data` | **`trigger_state`** | 對照 `052`，相異行命中 trigger_state：`ignition working condition` |
| `…-056` | `mode` | **`trigger_state`** | 對照 `057`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-057` | `mode` | **`trigger_state`** | 對照 `056`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-058` | `input_data` | **`trigger_state`** | 對照 `066`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-059` | `timing` | `timing` | 對照 `060`，相異行命中 timing：`after the RemStartFail transition` |
| `…-060` | `mode` | **`trigger_state`** | 對照 `061`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-061` | `mode` | **`trigger_state`** | 對照 `060`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-062` | `trigger_state` | `trigger_state` | 對照 `063`，相異行命中 trigger_state：`PhoneCall.Info` |
| `…-063` | `trigger_state` | `trigger_state` | 對照 `062`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-064` | `trigger_state` | `trigger_state` | 對照 `065`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-065` | `trigger_state` | `trigger_state` | 對照 `064`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-066` | `input_data` | **`trigger_state`** | 對照 `058`，相異行命中 trigger_state：`LTM_OperationalModeSts.Info` |
| `…-067` | `trigger_state` | **`**無對應**`** | 對照 `069`，五個正向判準皆未命中；相異行：（無） |
| `…-068` | `trigger_state` | **`**無對應**`** | 對照 `070`，五個正向判準皆未命中；相異行：（無） |
| `…-069` | `trigger_state` | `trigger_state` | 對照 `070`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-070` | `trigger_state` | **`input_data`** | 對照 `069`，相異行命中 input_data：`Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" t` |
| `…-073` | `input_data` | **`trigger_state`** | 對照 `074`，相異行命中 trigger_state：`Ignition Off` |
| `…-074` | `input_data` | **`trigger_state`** | 對照 `073`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-075` | `trigger_state` | `trigger_state` | 對照 `077`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-076` | `trigger_state` | `trigger_state` | 對照 `075`，相異行命中 trigger_state：`Rear_Camera_Enable.Info` |
| `…-077` | `trigger_state` | **`input_data`** | 對照 `075`，相異行命中 input_data：`Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" t` |
| `…-078` | `trigger_state` | `trigger_state` | 對照 `077`，相異行命中 trigger_state：`Rear_Camera_Enable.Info` |
| `…-079` | `input_data` | **`trigger_state`** | 對照 `080`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-080` | `trigger_state` | **`**無對應**`** | 對照 `081`，五個正向判準皆未命中；相異行：3. TLM_Display.GUI is in Phone Main Scre |
| `…-081` | `trigger_state` | **`**無對應**`** | 對照 `080`，五個正向判準皆未命中；相異行：3. TLM_Display.GUI is on a screen other  |
| `…-086` | `trigger_state` | `trigger_state` | 對照 `089`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-087` | `trigger_state` | `trigger_state` | 對照 `088`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-088` | `trigger_state` | `trigger_state` | 對照 `087`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-089` | `trigger_state` | `trigger_state` | 對照 `093`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-090` | `trigger_state` | `trigger_state` | 對照 `093`，相異行命中 trigger_state：`Phone_Call.Info` |
| `…-091` | `trigger_state` | **`**無對應**`** | 對照 `092`，五個正向判準皆未命中；相異行：1. Accept the CLIMATIC_PANEL.Radio_Btn0  |
| `…-092` | `trigger_state` | **`**無對應**`** | 對照 `091`，五個正向判準皆未命中；相異行：1. Decline the CLIMATIC_PANEL.Radio_Btn0 |
| `…-093` | `trigger_state` | **`input_data`** | 對照 `089`，相異行命中 input_data：`Drive CLIMATIC_PANEL.Radio_Btn0 from "Not_Pressed" t` |
| `…-094` | `trigger_state` | `trigger_state` | 對照 `096`，相異行命中 trigger_state：`Full-Operation` |
| `…-095` | `trigger_state` | `trigger_state` | 對照 `094`，相異行命中 trigger_state：`PhoneCall.Info` |
| `…-096` | `trigger_state` | **`**無對應**`** | 對照 `094`，五個正向判準皆未命中；相異行：4. The previous internal state was Stand |
| `…-097` | `trigger_state` | **`input_data`** | 對照 `094`，相異行命中 input_data：`Brand_Configuration_2 reads a value other than ` |
| `…-098` | `timing` | **`trigger_state`** | 對照 `099`，相異行命中 trigger_state：`Antitheft_Activation.Req` |
| `…-099` | `timing` | **`trigger_state`** | 對照 `098`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-100` | `trigger_state` | **`**無對應**`** | 對照 `102`，五個正向判準皆未命中；相異行：（無） |
| `…-101` | `trigger_state` | `trigger_state` | 對照 `100`，相異行命中 trigger_state：`SwitchOff_Timeout_Setting.Req` |
| `…-102` | `trigger_state` | **`**無對應**`** | 對照 `100`，五個正向判準皆未命中；相異行：（無） |
| `…-103` | `trigger_state` | `trigger_state` | 對照 `100`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-104` | `trigger_state` | **`**無對應**`** | 對照 `107`，五個正向判準皆未命中；相異行：（無） |
| `…-105` | `timing` | **`input_data`** | 對照 `106`，相異行命中 input_data：`Switch_Off_Time reads 20 minutes` |
| `…-106` | `timing` | **`input_data`** | 對照 `105`，相異行命中 input_data：`$PwrAccDelayAct$ reads 10 minutes` |
| `…-107` | `trigger_state` | **`**無對應**`** | 對照 `104`，五個正向判準皆未命中；相異行：（無） |
| `…-108` | `input_data` | **`trigger_state`** | 對照 `109`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-109` | `input_data` | **`trigger_state`** | 對照 `108`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-112` | `input_data` | **`trigger_state`** | 對照 `113`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-113` | `input_data` | **`trigger_state`** | 對照 `112`，相異行命中 trigger_state：`Ignition Off` |
| `…-115` | `trigger_state` | `trigger_state` | 對照 `116`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-116` | `input_data` | **`trigger_state`** | 對照 `115`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-117` | `trigger_state` | `trigger_state` | 對照 `118`，相異行命中 trigger_state：`VPLastStatus` |
| `…-118` | `input_data` | **`trigger_state`** | 對照 `117`，相異行命中 trigger_state：`VPLastStatus` |
| `…-121` | `timing` | **`trigger_state`** | 對照 `122`，相異行命中 trigger_state：`Ignition On` |
| `…-122` | `trigger_state` | `trigger_state` | 對照 `123`，相異行命中 trigger_state：`SwitchOff_Timeout_Setting.Req` |
| `…-123` | `trigger_state` | `trigger_state` | 對照 `122`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-124` | `timing` | **`input_data`** | 對照 `121`，相異行命中 input_data：`NA` |
| `…-126` | `trigger_state` | `trigger_state` | 對照 `127`，相異行命中 trigger_state：`Ignition Off` |
| `…-127` | `trigger_state` | `trigger_state` | 對照 `126`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-128` | `trigger_state` | `trigger_state` | 對照 `129`，相異行命中 trigger_state：`Ignition Off` |
| `…-129` | `trigger_state` | `trigger_state` | 對照 `128`，相異行命中 trigger_state：`Ignition Pre Off` |
| `…-130` | `mode` | **`**無對應**`** | 對照 `131`，五個正向判準皆未命中；相異行：3. No HMI screen is required ／ 1. Leave the HU in Standby mode without  |
| `…-131` | `mode` | **`trigger_state`** | 對照 `130`，相異行命中 trigger_state：`is in Standby` |
| `…-132` | `mode` | **`trigger_state`** | 對照 `134`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-133` | `mode` | **`trigger_state`** | 對照 `135`，相異行命中 trigger_state：`Front_Panel_OnOff.Req` |
| `…-134` | `mode` | **`input_data`** | 對照 `132`，相異行命中 input_data：`CLIMATIC_PANEL.Radio_Btn0: "` |
| `…-135` | `mode` | **`input_data`** | 對照 `133`，相異行命中 input_data：`CLIMATIC_PANEL.Radio_Btn0: "` |
| `…-136` | `mode` | **`trigger_state`** | 對照 `137`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-137` | `mode` | **`trigger_state`** | 對照 `136`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-138` | `input_data` | **`trigger_state`** | 對照 `139`，相異行命中 trigger_state：`Antitheft_Result.Info` |
| `…-139` | `input_data` | **`trigger_state`** | 對照 `138`，相異行命中 trigger_state：`Antitheft_Result.Info` |
| `…-140` | `mode` | **`trigger_state`** | 對照 `141`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-141` | `mode` | **`trigger_state`** | 對照 `140`，相異行命中 trigger_state：`TLM_Status.Info` |
| `…-142` | `mode` | **`trigger_state`** | 對照 `143`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-143` | `mode` | **`trigger_state`** | 對照 `142`，相異行命中 trigger_state：`Auto_SwitchOn_Setting.Req` |
| `…-144` | `mode` | **`trigger_state`** | 對照 `145`，相異行命中 trigger_state：`VPLastStatus` |
| `…-145` | `mode` | **`trigger_state`** | 對照 `144`，相異行命中 trigger_state：`VPLastStatus` |
| `…-146` | `trigger_state` | **`input_data`** | 對照 `142`，相異行命中 input_data：`NA` |
| `…-152` | `input_data` | `input_data` | 對照 `153`，相異行命中 input_data：`Audio_Brand: "` |
| `…-153` | `input_data` | `input_data` | 對照 `152`，相異行命中 input_data：`Audio_Brand: "` |
| `…-154` | `input_data` | `input_data` | 對照 `155`，相異行命中 input_data：`Audio_Brand: "` |
| `…-155` | `input_data` | `input_data` | 對照 `154`，相異行命中 input_data：`Audio_Brand: "` |
| `…-156` | `boundary` | **`input_data`** | 對照 `157`，相異行命中 input_data：`$VC_SpecialPKG_IC$: "` |
| `…-157` | `boundary` | `boundary` | 對照 `156`，相異行命中 boundary：`greater than` |
| `…-160` | `input_data` | **`timing`** | 對照 `161`，相異行命中 timing：`boot of the TLM has been completed` |
| `…-161` | `input_data` | **`timing`** | 對照 `160`，相異行命中 timing：`boot of the TLM is not ended` |
| `…-162` | `input_data` | **`**無對應**`** | 對照 `163`，五個正向判準皆未命中；相異行：An SOS call is placed |
| `…-163` | `input_data` | **`**無對應**`** | 對照 `162`，五個正向判準皆未命中；相異行：An Assist call is placed |
| `…-166` | `input_data` | **`**無對應**`** | 對照 `167`，五個正向判準皆未命中；相異行：3. The display is on the phone main scre |
| `…-167` | `input_data` | **`**無對應**`** | 對照 `166`，五個正向判準皆未命中；相異行：3. The display is on the phone projectio |
| `…-169` | `input_data` | **`**無對應**`** | 對照 `170`，五個正向判準皆未命中；相異行：A FOTA update available for the Radio |
| `…-170` | `input_data` | **`**無對應**`** | 對照 `169`，五個正向判準皆未命中；相異行：A FOTA update available for the TBM |
| `…-171` | `input_data` | **`**無對應**`** | 對照 `169`，五個正向判準皆未命中；相異行：A FOTA update available for the ROV |
| `…-172` | `mode` | **`**無對應**`** | 對照 `173`，五個正向判準皆未命中；相異行：1. Leave the FOTA pop-up without any use |
| `…-173` | `mode` | **`**無對應**`** | 對照 `172`，五個正向判準皆未命中；相異行：1. Dismiss the FOTA pop-up on the screen |
| `…-174` | `trigger_state` | **`input_data`** | 對照 `172`，相異行命中 input_data：`$ACCDlyAct$: a` |
| `…-175` | `input_data` | **`**無對應**`** | 對照 `176`，五個正向判準皆未命中；相異行：（無） |
| `…-176` | `input_data` | **`**無對應**`** | 對照 `175`，五個正向判準皆未命中；相異行：（無） |
| `…-177` | `input_data` | **`**無對應**`** | 對照 `175`，五個正向判準皆未命中；相異行：2. The HU is currently installing a firm |
| `…-178` | `mode` | **`trigger_state`** | 對照 `179`，相異行命中 trigger_state：`is in SLEEP` |
| `…-179` | `mode` | **`trigger_state`** | 對照 `178`，相異行命中 trigger_state：`is in STANDBY` |
| `…-180` | `mode` | **`trigger_state`** | 對照 `178`，相異行命中 trigger_state：`is in PARTIAL OPERATION` |
| `…-181` | `trigger_state` | **`input_data`** | 對照 `179`，相異行命中 input_data：`$DriverDoorOnOffSts$: "` |
| `…-182` | `mode` | **`trigger_state`** | 對照 `183`，相異行命中 trigger_state：`BODY ON` |
| `…-183` | `trigger_state` | **`input_data`** | 對照 `182`，相異行命中 input_data：`$PowerMode$: "` |
| `…-184` | `trigger_state` | **`**無對應**`** | 對照 `182`，五個正向判準皆未命中；相異行：An HU power mode status change to TIMED  ／ 1. Send the change listed in Input Test  |
| `…-185` | `trigger_state` | `trigger_state` | 對照 `179`，相異行命中 trigger_state：`BODY ON` |
| `…-186` | `trigger_state` | **`input_data`** | 對照 `178`，相異行命中 input_data：`NA` |
| `…-191` | `input_data` | **`**無對應**`** | 對照 `193`，五個正向判準皆未命中；相異行：4. The HU has not yet played the startup ／ 1. Bring the HU through a startup that p |
| `…-192` | `input_data` | **`**無對應**`** | 對照 `194`，五個正向判準皆未命中；相異行：A manual time adjustment that changes th |
| `…-193` | `input_data` | `input_data` | 對照 `192`，相異行命中 input_data：`NA` |
| `…-194` | `input_data` | **`**無對應**`** | 對照 `192`，五個正向判準皆未命中；相異行：An automatic adjustment due to time zone |
| `…-196` | `input_data` | `input_data` | 對照 `197`，相異行命中 input_data：`Audio_Brand: "` |
| `…-197` | `input_data` | `input_data` | 對照 `196`，相異行命中 input_data：`Audio_Brand: "` |
| `…-198` | `input_data` | `input_data` | 對照 `199`，相異行命中 input_data：`Audio_Brand: "` |
| `…-199` | `input_data` | `input_data` | 對照 `198`，相異行命中 input_data：`Audio_Brand: "` |
| `…-200` | `boundary` | **`input_data`** | 對照 `201`，相異行命中 input_data：`$VC_SpecialPKG_IC$: "` |
| `…-201` | `boundary` | `boundary` | 對照 `200`，相異行命中 boundary：`greater than` |
| `…-202` | `input_data` | **`trigger_state`** | 對照 `203`，相異行命中 trigger_state：`Ignition On` |
| `…-203` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`Ignition Pre_Start` |
| `…-204` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`working condition` |
| `…-205` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`working condition` |
| `…-206` | `input_data` | **`trigger_state`** | 對照 `202`，相異行命中 trigger_state：`Ignition On` |
| `…-207` | `mode` | **`**無對應**`** | 對照 `208`，五個正向判準皆未命中；相異行：1. Bring the HU to Timed mode for the fi |
| `…-208` | `mode` | **`**無對應**`** | 對照 `207`，五個正向判準皆未命中；相異行：1. Bring the HU to Full Operation mode f |
| `…-209` | `mode` | **`trigger_state`** | 對照 `210`，相異行命中 trigger_state：`is in Idle` |
| `…-210` | `mode` | **`trigger_state`** | 對照 `209`，相異行命中 trigger_state：`is in Standby` |
| `…-211` | `mode` | **`trigger_state`** | 對照 `209`，相異行命中 trigger_state：`is in Partial Operation` |
| `…-212` | `input_data` | **`**無對應**`** | 對照 `213`，五個正向判準皆未命中；相異行：An ongoing call at the moment of the tra |
| `…-213` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：A backup camera view at the moment of th |
| `…-214` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：An incoming call at the moment of the tr |
| `…-215` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：An outgoing call at the moment of the tr |
| `…-216` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：A climate pop-up at the moment of the tr |
| `…-217` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：An SOS or Assist call at the moment of t |
| `…-218` | `input_data` | **`**無對應**`** | 對照 `212`，五個正向判準皆未命中；相異行：A FOTA pop up at the moment of the trans |
| `…-219` | `mode` | **`input_data`** | 對照 `212`，相異行命中 input_data：`NA` |
| `…-224` | `trigger_state` | **`input_data`** | 對照 `225`，相異行命中 input_data：`$TBM_Present$ reads "Not Present` |
| `…-225` | `trigger_state` | **`input_data`** | 對照 `224`，相異行命中 input_data：`$TBM_Present$ reads "Present` |
| `…-226` | `trigger_state` | **`input_data`** | 對照 `227`，相異行命中 input_data：`$TBM_Present$ reads "Not Present` |
| `…-227` | `trigger_state` | **`**無對應**`** | 對照 `226`，五個正向判準皆未命中；相異行：4. $Country_Code$ does not require SOS o |
| `…-232` | `input_data` | `input_data` | 對照 `233`，相異行命中 input_data：`$VC_SpecialPKG$: "` |
| `…-233` | `input_data` | `input_data` | 對照 `232`，相異行命中 input_data：`$VC_SpecialPKG$: a` |
| `…-235` | `trigger_state` | **`input_data`** | 對照 `236`，相異行命中 input_data：`NA` |
| `…-236` | `trigger_state` | **`input_data`** | 對照 `235`，相異行命中 input_data：`$VC_SpecialPKG$: a` |
| `…-237` | `input_data` | `input_data` | 對照 `238`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-238` | `input_data` | `input_data` | 對照 `237`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-239` | `input_data` | `input_data` | 對照 `237`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-240` | `input_data` | `input_data` | 對照 `241`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-241` | `input_data` | `input_data` | 對照 `240`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-242` | `input_data` | `input_data` | 對照 `240`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-243` | `input_data` | `input_data` | 對照 `244`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-244` | `input_data` | `input_data` | 對照 `243`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-245` | `input_data` | `input_data` | 對照 `243`，相異行命中 input_data：`$VC_VEH_BRAND$: "` |
| `…-246` | `trigger_state` | **`mode`** | 對照 `247`，相異行命中 mode：`Atlantis` |
| `…-247` | `trigger_state` | **`mode`** | 對照 `246`，相異行命中 mode：`architecture` |
| `…-248` | `trigger_state` | **`mode`** | 對照 `249`，相異行命中 mode：`Atlantis` |
| `…-249` | `trigger_state` | **`mode`** | 對照 `248`，相異行命中 mode：`architecture` |
| `…-250` | `trigger_state` | **`input_data`** | 對照 `251`，相異行命中 input_data：`NA` |
| `…-251` | `trigger_state` | **`input_data`** | 對照 `250`，相異行命中 input_data：`$VC_SpecialPKG$: a` |
| `…-252` | `trigger_state` | **`input_data`** | 對照 `253`，相異行命中 input_data：`$VC_VEH_LINE$: "` |
| `…-253` | `trigger_state` | **`input_data`** | 對照 `252`，相異行命中 input_data：`$VC_VEH_LINE$: a` |
| `…-255` | `input_data` | `input_data` | 對照 `256`，相異行命中 input_data：`$Day_Night_Mode$: t` |
| `…-256` | `input_data` | `input_data` | 對照 `255`，相異行命中 input_data：`$Day_Night_Mode$: t` |
| `…-259` | `input_data` | **`timing`** | 對照 `260`，相異行命中 timing：`before the Summer start` |
| `…-260` | `input_data` | **`timing`** | 對照 `259`，相異行命中 timing：`before the Fall start` |
| `…-261` | `input_data` | **`timing`** | 對照 `259`，相異行命中 timing：`before the Winter start` |
| `…-262` | `input_data` | **`timing`** | 對照 `259`，相異行命中 timing：`before the Spring start` |
| `…-263` | `input_data` | **`trigger_state`** | 對照 `264`，相異行命中 trigger_state：`Ignition On` |
| `…-264` | `input_data` | **`trigger_state`** | 對照 `263`，相異行命中 trigger_state：`Ignition On` |
