# B3 前置 —— 代理量錨點可及性報告（59 包 / R-P367 / G252）

> **本檔不填代理量。** R-P367 令可及性報告經分析層覆核後始填代理量表。
> 母體：現行 corpus（283 條）之 `Read <X>` / `Check that <X>` 中**非白名單**之 `<X>`，按原文去重。
> 錨點來源限 **G0 台帳**（CFTS009 / CFTS010 / SYS3 文字層之 `{ObjectID}` 段落＋ BHCAN2 / FDCAN8 之 `VAL_` / `CM_`）。台帳外文件一律不得為錨。
> ⚠ 本 feature `sys1_export: null` —— R-P353 / R-P354(b) 之「SYS1」為空集（A-PW354），不列入錨點來源。

## 判準

`<X>` 去冠詞、去停用詞後取內容詞；**全部內容詞同時出現於同一錨點段落**者記「有錨」。此為**保守之機器判準**：

- 偽陽性風險低（要求全詞同段），
- **偽陰性風險高** —— 同義改寫、跨段落陳述皆會漏。

故「無錨」之列**不等於查無**，只等於「以本判準未命中」，須人讀該 `<X>` 所屬 TC 之 `test_item` 上半 verbatim 再判。
依 R-G13，本檔不得作為登記「查無」之依據。

## 總計：相異 `<X>` **121** 個（出現 274 次）

| 判定 | 數 | 佔比 |
|---|---|---|
| 有錨（全詞同段） | **61** | 50.4% |
| 有錨（分項） | **9** | 7.4% |
| 無錨（本判準未命中）| **51** | 42.1% |

## 逐名

| `<X>`（原文） | 出現 | TC 數 | 錨 | 錨點（至多 3）|
|---|---|---|---|---|
| `screen` | 18 | 18 | **有** | CFTS009-4941125、CFTS009-4941131、CFTS009-4941138 |
| `TLM_Status.Info and $Telematic_Power$` | 16 | 16 | **有** | CFTS009-4941396、CFTS009-4941441、CFTS009-4941445 |
| `HU mode` | 8 | 8 | **有** | CFTS009-4941018、CFTS009-4941022、CFTS009-4941024 |
| `shown logos` | 8 | 8 | **無** | **無** |
| `TLM_Status.Info` | 7 | 7 | **有** | CFTS009-4941396、CFTS009-4941441、CFTS009-4941445 |
| `VPLastStatus, TLM_Status.Info and $Telematic_Power$` | 6 | 6 | **有** | CFTS009-4941441、CFTS009-4941540、CFTS009-4941541 |
| `antitheft request and the TLM state` | 6 | 6 | **無** | **無** |
| `antitheft request and the screen` | 5 | 5 | **無** | **無** |
| `HU mode and the screen` | 5 | 5 | **有** | CFTS009-4941166、CFTS009-4941167、CFTS009-4941182 |
| `$Telematic_Power$` | 4 | 4 | **有** | CFTS009-4941035、CFTS009-4941037、CFTS009-4941039 |
| `Antitheft_Activation.Req` | 4 | 4 | **有** | CFTS009-4941413、CFTS009-4941419、CFTS009-4941441 |
| `Timeout1 and then trigger an Ignition On event` | 4 | 4 | **無** | **無** |
| `antitheft request, the TLM state and the screen` | 4 | 4 | **無** | **無** |
| `shown Splash Screen` | 4 | 4 | **有** | CFTS009-4941666、CFTS009-4941667、CFTS009-4941950 |
| `audio path and the display` | 4 | 4 | **有** | DBC `VAL_`/`CM_` |
| `disclaimer wording` | 4 | 4 | **無** | **無** |
| `applied theme` | 4 | 4 | **有** | CFTS009-4942089 |
| `season the HU determines` | 4 | 4 | **無** | **無** |
| `selectable values offered for SwitchOff_Timeout_Setting.Req` | 3 | 3 | **無** | **無** |
| `Auto_SwitchOn_Setting.Req and Timeout1` | 3 | 3 | **有** | CFTS009-4941441、CFTS009-4941505、CFTS009-4941509 |
| `TLM_Status.Info and the TLM state` | 3 | 3 | **有** | CFTS009-4941396、CFTS009-4941441、CFTS009-4941445 |
| `RemStartFail, TLM_Status.Info and the TLM state` | 3 | 3 | **有** | CFTS009-4941467、CFTS009-4941468、CFTS009-4941474 |
| `active functionality and TLM_Status.Info` | 3 | 3 | **有** | CFTS009-4941571、CFTS009-4941574、CFTS009-4941576 |
| `TLM state` | 3 | 3 | **有** | CFTS009-4941351、CFTS009-4941358、CFTS009-4941359 |
| `HU reaction` | 3 | 3 | **有** | DBC `VAL_`/`CM_` |
| `screen and the power mode` | 3 | 3 | **有** | CFTS009-4941166、CFTS009-4941167、CFTS009-4941182 |
| `screen sequence` | 3 | 3 | **有** | CFTS009-4941246、CFTS009-4941316、CFTS009-4941750 |
| `audio output against the animation start` | 3 | 3 | **無** | **無** |
| `audio output` | 3 | 3 | **有** | CFTS009-4941127、CFTS009-4941133、CFTS009-4941140 |
| `startup flow against the HMI` | 3 | 3 | **有** | CFTS009-4941951、CFTS009-4941953、CFTS009-4941962 |
| `displayed font` | 3 | 3 | **無** | **無** |
| `displayed App icon` | 3 | 3 | **無** | **無** |
| `avatar list in the profile screen` | 3 | 3 | **有** | CFTS009-4942027 |
| `shown seat graphic` | 3 | 3 | **有** | DBC `VAL_`/`CM_` |
| `TLM display through SplashScreen_Time` | 2 | 2 | **有** | CFTS010-4942337 |
| `volume limit and the audio output state` | 2 | 2 | **有** | DBC `VAL_`/`CM_` |
| `call audio routing` | 2 | 2 | **無** | **無** |
| `parameters offered for user selection` | 2 | 2 | **無** | **無** |
| `call audio routing and the TLM state` | 2 | 2 | **無** | **無** |
| `HU mode, the audio and the screen` | 2 | 2 | **有** | CFTS009-4941166、CFTS009-4941182、CFTS009-4941187 |
| `RemStartFail` | 2 | 2 | **有** | CFTS009-4941442、CFTS009-4941467、CFTS009-4941468 |
| `TLM_Status.Info and the screen` | 2 | 2 | **有** | CFTS009-4941544、CFTS009-4941554、CFTS009-4941557 |
| `screen, VPLastStatus and TLM_Status.Info` | 2 | 2 | **有** | CFTS009-4941554、CFTS009-4941557、CFTS009-4941650 |
| `screen and its duration` | 2 | 2 | **有（分項）** | screen→CFTS009-4941125、its duration→CFTS010-4942206 |
| `Timeout1 against the configured parameter` | 2 | 2 | **無** | **無** |
| `FPDM, AMP, ICS and DTV functions` | 2 | 2 | **無** | **無** |
| `antitheft request` | 2 | 2 | **無** | **無** |
| `display backlight` | 2 | 2 | **有** | CFTS009-4941165、CFTS009-4941316、CFTS009-4941750 |
| `screen and the audio path` | 2 | 2 | **有** | DBC `VAL_`/`CM_` |
| `shown logo against the configured brand` | 2 | 2 | **無** | **無** |
| `applied theme against the brand signal` | 2 | 2 | **無** | **無** |
| `$Radio_Theme$ against the applied theme` | 2 | 2 | **無** | **無** |
| `$Radio_Theme$ and its timing` | 2 | 2 | **有（分項）** | $Radio_Theme$→CFTS009-4941271、its timing→CFTS009-4941249 |
| `shown recirc icon` | 2 | 2 | **無** | **無** |
| `played animation` | 2 | 2 | **有** | CFTS009-4941301、CFTS009-4941941、CFTS009-4941944 |
| `TLM display` | 2 | 2 | **有** | CFTS009-4941365、CFTS009-4941559、CFTS009-4942029 |
| `TLM power indication and the network state` | 2 | 2 | **有** | DBC `VAL_`/`CM_` |
| `TLM, FPDM, AMP, ICS and DTV functionality availability` | 2 | 2 | **有** | DBC `VAL_`/`CM_` |
| `TLM display before and after SplashScreen_Time` | 1 | 1 | **有（分項）** | TLM display before→DBC、after SplashScreen_Time→CFTS010-4942337 |
| `TLM screen content before and after StandardScreen_Time` | 1 | 1 | **無** | **無** |
| `TLM_Status transitions during the remainder of the boot` | 1 | 1 | **無** | **無** |
| `volume limit before and at the end of the window` | 1 | 1 | **有** | DBC `VAL_`/`CM_` |
| `active audio source and the TLM state` | 1 | 1 | **有** | CFTS009-4941545、CFTS009-4941546、CFTS009-4941720 |
| `active functionality, RemStartFail, TLM_Status.Info and $Telematic_Power` | 1 | 1 | **有** | CFTS009-4941723 |
| `active source and the TLM state` | 1 | 1 | **有** | CFTS009-4941494、CFTS009-4941503、CFTS009-4941512 |
| `HU mode, the entertainment audio and the screen` | 1 | 1 | **有** | CFTS009-4941379、CFTS009-4941385 |
| `three stored variables` | 1 | 1 | **無** | **無** |
| `TLM_Status.Info and the state machine` | 1 | 1 | **無** | **無** |
| `AMP, ICS and DTV power states and the audio paths` | 1 | 1 | **無** | **無** |
| `RemStartFail and TLM_Status.Info` | 1 | 1 | **有** | CFTS009-4941467、CFTS009-4941468、CFTS009-4941474 |
| `TLM_Status.Info, $Telematic_Power$ and the active source` | 1 | 1 | **有** | CFTS009-4941494、CFTS009-4941503、CFTS009-4941512 |
| `TLM screen and Rear_Camera_Enable.Info` | 1 | 1 | **有** | CFTS009-4941544、CFTS009-4941560、CFTS009-4941561 |
| `active source` | 1 | 1 | **有** | CFTS009-4941494、CFTS009-4941503、CFTS009-4941512 |
| `TLM_Status.Info and the screen content` | 1 | 1 | **無** | **無** |
| `VPLastStatus, RemStartFail and TLM_Status.Info` | 1 | 1 | **有** | CFTS009-4941564、CFTS009-4941566、CFTS009-4941568 |
| `Antitheft_Activation.Req and the screen` | 1 | 1 | **有** | CFTS009-4941578、CFTS009-4941579、CFTS009-4941584 |
| `Antitheft_Activation.Req and the TLM state` | 1 | 1 | **有** | CFTS009-4941413、CFTS009-4941419、CFTS009-4941441 |
| `screen against TLM_Status.Info` | 1 | 1 | **有** | CFTS009-4941544、CFTS009-4941554、CFTS009-4941557 |
| `antitheft request, the screen and the TLM state` | 1 | 1 | **無** | **無** |
| `screen and the TLM state` | 1 | 1 | **有** | CFTS009-4941365、CFTS009-4941454、CFTS009-4941544 |
| `remote start outcome flags and the TLM state` | 1 | 1 | **無** | **無** |
| `remote start outcome flag and the TLM state` | 1 | 1 | **無** | **無** |
| `TLM state against the operative state management rules` | 1 | 1 | **無** | **無** |
| `offered items against the TLM HMI documents` | 1 | 1 | **無** | **無** |
| `HU timer and its power mode` | 1 | 1 | **有** | CFTS009-4941051、CFTS009-4941249、CFTS009-4941315 |
| `user selectable parameter on an ex-factory unit` | 1 | 1 | **無** | **無** |
| `stored last status` | 1 | 1 | **有** | CFTS009-4941141、CFTS009-4941449 |
| `stored last status and the TLM state` | 1 | 1 | **有** | CFTS009-4941449 |
| `antitheft request, the stored last status and the TLM state` | 1 | 1 | **無** | **無** |
| `shown logo against the configured parameter` | 1 | 1 | **無** | **無** |
| `user selectable timeout parameter on an ex-factory unit` | 1 | 1 | **無** | **無** |
| `auto switch on parameter and Timeout1` | 1 | 1 | **有** | CFTS009-4941581 |
| `HU mode after the idle period` | 1 | 1 | **無** | **無** |
| `HU behavior and the stored logs` | 1 | 1 | **無** | **無** |
| `both processors` | 1 | 1 | **無** | **無** |
| `HU behavior` | 1 | 1 | **有** | CFTS009-4941030、CFTS009-4941040、CFTS009-4941044 |
| `screen against the elapsed time` | 1 | 1 | **無** | **無** |
| `TLM state and the screen` | 1 | 1 | **有** | CFTS009-4941365、CFTS009-4941454、CFTS009-4941544 |
| `ICS functions and the DTV` | 1 | 1 | **無** | **無** |
| `screen across the cycles` | 1 | 1 | **無** | **無** |
| `shown wording` | 1 | 1 | **無** | **無** |
| `applied theme against the configured value` | 1 | 1 | **有** | DBC `VAL_`/`CM_` |
| `shown element` | 1 | 1 | **無** | **無** |
| `shown seat graphic against the brand signal` | 1 | 1 | **無** | **無** |
| `shown gauges` | 1 | 1 | **無** | **無** |
| `TLM_Status.Info and the TLM power indication` | 1 | 1 | **有（分項）** | TLM_Status.Info→CFTS009-4941396、the TLM power indication→DBC |
| `TLM, AMP, ICS and DTV functionality availability` | 1 | 1 | **有** | DBC `VAL_`/`CM_` |
| `TLM_Status.Info after each one` | 1 | 1 | **無** | **無** |
| `TLM audio output state` | 1 | 1 | **有** | DBC `VAL_`/`CM_` |
| `ICS functionality availability` | 1 | 1 | **有** | DBC `VAL_`/`CM_` |
| `DTV state` | 1 | 1 | **有** | CFTS009-4941018、CFTS009-4941111、CFTS009-4941145 |
| `$Telematic_Power$ and the AMP, ICS and DTV states` | 1 | 1 | **有（分項）** | $Telematic_Power$→CFTS009-4941035、the AMP→CFTS009-4941018、ICS→CFTS009-4941018 |
| `audio output for ANC, ACN and chimes` | 1 | 1 | **有（分項）** | audio output for ANC→CFTS009-4941150、ACN→CFTS009-4941029、chimes→CFTS009-4941234 |
| `TLM power indication and the AMP, ICS and DTV states` | 1 | 1 | **有（分項）** | TLM power indication→DBC、the AMP→CFTS009-4941018、ICS→CFTS009-4941018 |
| `TLM state again after Timeout1 has elapsed` | 1 | 1 | **無** | **無** |
| `TLM, AMP, ICS and DTV states` | 1 | 1 | **有（分項）** | TLM→CFTS009-4941351、AMP→CFTS009-4941018、ICS→CFTS009-4941018 |
| `TLM_Status.Info, VPLastStatus, SwitchOff_Timeout_Setting.Req, Auto_Switc` | 1 | 1 | **有（分項）** | TLM_Status.Info→CFTS009-4941396、VPLastStatus→CFTS009-4941042、SwitchOff_Timeout_Settin→CFTS009-4941441 |
| `VPLastStatus, SwitchOffSetting.Req and Auto_SwitchOn_Setting.Req` | 1 | 1 | **有** | CFTS009-4941449 |
| `audio power amplifier and the BoosterOUT states` | 1 | 1 | **無** | **無** |
| `analog and digital antenna supplies` | 1 | 1 | **無** | **無** |
| `USB and AUX MCU states` | 1 | 1 | **無** | **無** |
