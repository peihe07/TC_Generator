# B1 —— 反向涵蓋報告（R-P118）

> **本報告不判 pass / fail、不使 exit=1**（R-P118(c)）。
> 「無對應」者須逐項人工裁決三選一（R-P118(d)）；**沉默不算裁決**。
> 拆句規則於 `reverse_coverage.py` 一次寫定，對三個 leaf 一體適用。
> 產生指令：`python features/power/scripts/reverse_coverage.py --batch batch_003_power_state_a.json`

## 現況（batch_003_power_state_a.json，61 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-011 —— 行為項 10，已覆蓋 6，無對應 **4**

TC：044, 045, 046, 047, 048, 049

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | While the HU is in IDLE mode, the HU shall transition to Full-Operation mode i | 044 | 0.88 | 已覆蓋 | `press` |
| 2 | Refer to CFTS042 for VR button press definition | 044 | 0.50 | 已覆蓋 | `cfts042`、`definition`、`refer` |
| 3 | The VR button press defined in CFTS009-2326 refers to both short and long pres | 044 | 0.44 | **無對應** | `cfts009-2326`、`defin`、`long`、`press`、`refer` |
| 4 | If CarPlay VR was activated by the button press defined in CFTS009-2326, then  | 046 | 0.30 | **無對應** | `accessory`、`apple`、`button`、`cfts009-2326`、`cfts009-2329`、`command`、`complete`、`defin`、`depend`、`different`、`interface`、`issu`、`once`、`pres`、`siri`、`specification` |
| 5 | If the CarPlay Device requests audio control and video control, then the HU sh | 045 | 0.93 | 已覆蓋 | `remain` |
| 6 | If the Carplay device requests audio control and does not request video contro | 046 | 0.82 | 已覆蓋 | `doe`、`remain`、`video` |
| 7 | See CFTS020 for Screen Off definition | 046 | 0.40 | **無對應** | `cfts020`、`definition`、`see` |
| 8 | If the Carplay device does not request audio control and does request video co | 047 | 0.86 | 已覆蓋 | `doe`、`remain` |
| 9 | See CFTS020 for Screen On definition | 045 | 0.25 | **無對應** | `cfts020`、`definition`、`see` |
| 10 | If the CarPlay Device does not request audio control or video control, then th | 048 | 0.91 | 已覆蓋 | `doe` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`2326`、`2329`

**R-P127 殘差詞分桶**（合計 38）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **4** | `long`(#3)、`button`(#4)、`pres`(#4)、`video`(#6) |
| 候選（須人工判 措詞差異 / 真缺口） | **34** | `press`(#1)、`cfts042`(#2)、`definition`(#2)、`refer`(#2)、`cfts009-2326`(#3)、`defin`(#3)、`press`(#3)、`refer`(#3)、`accessory`(#4)、`apple`(#4)、`cfts009-2326`(#4)、`cfts009-2329`(#4) |

### SWE-PM-012 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：050, 051

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | After a battery reconnection and also when TLM has to exit INIT state (as soon | 050 | 0.57 | 已覆蓋 | `able`、`accord`、`also`、`behave`、`certain`、`exit`、`last`、`limit`、`par`、`properly`、`requirement`、`reset`、`restore`、`soon`、`work` |
| 2 | "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Inf | 051 | 0.50 | 已覆蓋 | `first`、`sett`、`signal`、`telematic_power$` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`Telematic_Power`

**R-P127 殘差詞分桶**（合計 19）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `exit`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `able`(#1)、`accord`(#1)、`also`(#1)、`behave`(#1)、`certain`(#1)、`last`(#1)、`limit`(#1)、`par`(#1)、`properly`(#1)、`requirement`(#1)、`reset`(#1)、`restore`(#1) |

### SWE-PM-013 —— 行為項 4，已覆蓋 3，無對應 **1**

TC：052, 053, 054

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Star | 052 | 0.56 | 已覆蓋 | `crank`、`engine`、`follow`、`off`、`pre-off`、`pre_start`、`thi` |
| 2 | This mode shall exist for AMP, ICS, and DTV when STATUS_BH_BCM2.RemStActvSts i | 052 | 0.47 | 已覆蓋 | `amp`、`dtv`、`equal`、`exist`、`ics`、`off`、`reciev`、`relat`、`statu`、`thi` |
| 3 | AMP/ICS/DTV shall be OFF | 053 | 1.00 | 已覆蓋 | （無） |
| 4 | Audio for ANC, ACN, and chimes (if equipped) shall be active in this state) Al | 053 | 0.40 | **無對應** | `background`、`but`、`change`、`enabl`、`except`、`functionaliti`、`hmi`、`interaction`、`permit`、`ready`、`run`、`state`、`statu`、`thi`、`within` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`Pre_Start`、`TLM OFF`

**R-P127 殘差詞分桶**（合計 32）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **14** | `off`(#1)、`amp`(#2)、`dtv`(#2)、`ics`(#2)、`off`(#2)、`statu`(#2)、`background`(#4)、`change`(#4)、`except`(#4)、`functionaliti`(#4)、`hmi`(#4)、`interaction`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `crank`(#1)、`engine`(#1)、`follow`(#1)、`pre-off`(#1)、`pre_start`(#1)、`thi`(#1)、`equal`(#2)、`exist`(#2)、`reciev`(#2)、`relat`(#2)、`thi`(#2)、`but`(#4) |

### SWE-PM-014 —— 行為項 14，已覆蓋 9，無對應 **5**

TC：055, 056, 057, 058, 059, 060, 061, 062

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation" AND STATUS_BH_BCM | 055 | 0.52 | 已覆蓋 | `case`、`equal`、`false`、`pass`、`phone_call.info`、`pre`、`standby`、`state`、`state.if`、`state.in`、`stay`、`thi`、`tim`、`value` |
| 2 | until Phone_Call.Info becomes equal to "Not_Active", OR at maximum | 058 | 0.60 | 已覆蓋 | `equal`、`maximum` |
| 3 | until MaxCallTimeout expiration | — | 0.00 | **無對應** | `expiration`、`maxcalltimeout` |
| 4 | “Phone call management in Timed state” .ELSE IF LTM_OperationalModeSts.Info is | 055 | 0.34 | **無對應** | `behaviour`、`call`、`different`、`else`、`equal`、`false`、`full`、`management`、`menu`、`min`、`operation`、`original`、`phone`、`possible`、`pre`、`selectable`、`sett`、`signal`、`state`、`stay`、`switchoff_timeout_setting.req`、`thenaccord`、`tim`、`time`、`timeout1`、`two`、`valueand` |
| 5 | If Auto_SwitchOn_Setting.Req =="Active", when Timeout1 == 00 MIN" for LTM High | 061 | 1.00 | 已覆蓋 | （無） |
| 6 | If Phone_Call.Info == Not_Active, at LTM_OperationalModeSts.Info transition TL | 057 | 0.83 | 已覆蓋 | `set`、`value` |
| 7 | If Phone_Call.Info == Active, at LTM_OperationalModeSts.Info transition TLM se | 057 | 0.75 | 已覆蓋 | `set`、`tim`、`value` |
| 8 | In this case, TLM has to stay in this state | 056 | 0.40 | **無對應** | `case`、`stay`、`thi` |
| 9 | until Phone_Call.Info becomes equal to "Not_Active", OR at maximum | 058 | 0.60 | 已覆蓋 | `equal`、`maximum` |
| 10 | until MaxCallTimeout expiration | — | 0.00 | **無對應** | `expiration`、`maxcalltimeout` |
| 11 | “Phone call management in Timed state” | 056 | 0.40 | **無對應** | `management`、`phone`、`tim` |
| 12 | Behaviour 2: "SwitchOff_Timeout_Setting.Req == Timeout1 <> 00 MIN" or ( | 057 | 1.00 | 已覆蓋 | （無） |
| 13 | If Auto_SwitchOn_Setting.Req =="Not_Active ", when Timeout1 <> 00 MIN" for LTM | 059 | 0.77 | 已覆蓋 | `auto_switchon_setting.req`、`high`、`ltm`、`radio`、`set` |
| 14 | ELSE at LTM_OperationalModeSts.Info transition, TLM sets TLM_Status.Info and $ | 060 | 0.73 | 已覆蓋 | `else`、`mantain`、`set`、`state` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`ELSE`、`ELSE IF`、`IF`、`OR`、`THEN IF`、`THEN TLM`、`state.IF`、`state.In`

**R-P127 殘差詞分桶**（合計 69）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **32** | `false`(#1)、`pass`(#1)、`phone_call.info`(#1)、`standby`(#1)、`state`(#1)、`stay`(#1)、`tim`(#1)、`value`(#1)、`behaviour`(#4)、`call`(#4)、`false`(#4)、`min`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **37** | `case`(#1)、`equal`(#1)、`pre`(#1)、`state.if`(#1)、`state.in`(#1)、`thi`(#1)、`equal`(#2)、`maximum`(#2)、`expiration`(#3)、`maxcalltimeout`(#3)、`different`(#4)、`else`(#4) |

### SWE-PM-015 —— 行為項 4，已覆蓋 4，無對應 **0**

TC：063, 064, 065, 066

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_P | 063 | 0.79 | 已覆蓋 | `set`、`signal`、`value`、`valuethen` |
| 2 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATI | 064 | 0.79 | 已覆蓋 | `set`、`signal`、`value`、`valuethen` |
| 3 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal Front_P | 065 | 0.74 | 已覆蓋 | `parameter`、`provid`、`proxi`、`set`、`signal`、`value`、`valuethen` |
| 4 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND signal CLIMATI | 066 | 0.74 | 已覆蓋 | `parameter`、`provid`、`proxi`、`set`、`signal`、`value`、`valuethen` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 22）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **22** | `set`(#1)、`signal`(#1)、`value`(#1)、`valuethen`(#1)、`set`(#2)、`signal`(#2)、`value`(#2)、`valuethen`(#2)、`parameter`(#3)、`provid`(#3)、`proxi`(#3)、`set`(#3) |

### SWE-PM-016 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：067

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI paramete | 067 | 0.72 | 已覆蓋 | `activethen`、`becom`、`manage`、`parameter`、`proxi` |
| 2 | until Rear_Camera_Enable.Info passes to “False” again | 067 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND PROXI`、`IF`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `activethen`(#1)、`becom`(#1)、`manage`(#1)、`parameter`(#1)、`proxi`(#1) |

### SWE-PM-017 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：068

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation"AND PROXI paramete | 068 | 0.50 | 已覆蓋 | `also`、`becom`、`chang`、`could`、`depend`、`manage`、`parameter`、`prioriti`、`proxi`、`rvc`、`show`、`sourc`、`their`、`thentlm`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND PROXI`、`IF`、`THENTLM`

**R-P127 殘差詞分桶**（合計 15）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **15** | `also`(#1)、`becom`(#1)、`chang`(#1)、`could`(#1)、`depend`(#1)、`manage`(#1)、`parameter`(#1)、`prioriti`(#1)、`proxi`(#1)、`rvc`(#1)、`show`(#1)、`sourc`(#1) |

### SWE-PM-018 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：069

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal LTM_OperationalMo | 069 | 0.69 | 已覆蓋 | `pre`、`set`、`signal`、`value`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `pre`(#1)、`set`(#1)、`signal`(#1)、`value`(#1)、`valuethentlm`(#1) |

### SWE-PM-019 —— 行為項 4，已覆蓋 4，無對應 **0**

TC：070, 071, 072, 073

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Front_Panel_OnOff | 070 | 0.58 | 已覆蓋 | `depend`、`else`、`par`、`parameter`、`proper`、`proxi`、`show`、`signal`、`thi`、`value`、`valuethen` |
| 2 | "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has  | 071 | 0.67 | 已覆蓋 | `logic`、`logo`、`set`、`value`、`visualization` |
| 3 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal CLIMATIC_PANEL.Ra | 072 | 0.58 | 已覆蓋 | `depend`、`else`、`par`、`parameter`、`proper`、`proxi`、`show`、`signal`、`thi`、`value`、`valuethen` |
| 4 | "Splash Screen logo visualization" logics, for Response_Wait_Time AND TLM has  | 071 | 0.67 | 已覆蓋 | `logic`、`logo`、`set`、`value`、`visualization` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`ELSE
TLM`、`IF`、`IF PROXI`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 32）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `show`(#1)、`show`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **30** | `depend`(#1)、`else`(#1)、`par`(#1)、`parameter`(#1)、`proper`(#1)、`proxi`(#1)、`signal`(#1)、`thi`(#1)、`value`(#1)、`valuethen`(#1)、`logic`(#2)、`logo`(#2) |

### SWE-PM-020 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：074, 075, 076

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle"AND signal Phone_Call.Info h | 074 | 0.61 | 已覆蓋 | `apply`、`condition`、`doe`、`r1h`、`set`、`signal`、`sr21`、`state.thi`、`value`、`valuethentlm` |
| 2 | Then, IF Phone_Call.Info turns back to "Not_Active" when TLM_Display.GUI is in | 075 | 0.60 | 已覆蓋 | `action`、`another`、`back`、`due`、`dur`、`set`、`state.if`、`stay`、`turn`、`user` |
| 3 | Refer to TLM HMI document for further details about the screens visualization | 075 | 0.22 | **無對應** | `about`、`detail`、`document`、`further`、`hmi`、`refer`、`visualization` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`TLM HMI`、`state.IF`、`state.This`

**R-P127 殘差詞分桶**（合計 27）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `another`(#2)、`stay`(#2) |
| 候選（須人工判 措詞差異 / 真缺口） | **25** | `apply`(#1)、`condition`(#1)、`doe`(#1)、`r1h`(#1)、`set`(#1)、`signal`(#1)、`sr21`(#1)、`state.thi`(#1)、`value`(#1)、`valuethentlm`(#1)、`action`(#2)、`back`(#2) |

### SWE-PM-021 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：077

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Idle" AND PROXI parameter Rear_Vi | 077 | 0.57 | 已覆蓋 | `about`、`allow`、`availability`、`but`、`detail`、`parameter`、`pass`、`proxi`、`requirement`、`screen.refer`、`stay`、`thentlm`、`vf551` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND PROXI`、`IF`、`THENTLM`、`screen.Refer`

**R-P127 殘差詞分桶**（合計 13）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **13** | `about`(#1)、`allow`(#1)、`availability`(#1)、`but`(#1)、`detail`(#1)、`parameter`(#1)、`pass`(#1)、`proxi`(#1)、`requirement`(#1)、`screen.refer`(#1)、`stay`(#1)、`thentlm`(#1) |

### SWE-PM-022 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：078

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Full-Operation” || “Idle”AND sign | 078 | 0.86 | 已覆蓋 | `set`、`signal` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `set`(#1)、`signal`(#1) |

### SWE-PM-023 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：079

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal LTM_OperationalM | 079 | 0.82 | 已覆蓋 | `set`、`signal`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `set`(#1)、`signal`(#1)、`valuethentlm`(#1) |

### SWE-PM-024 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：080

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND STATUS_BH_BCM2.RemStAct | 080 | 0.87 | 已覆蓋 | `set`、`signal`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`IF`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `set`(#1)、`signal`(#1)、`valuethentlm`(#1) |

### SWE-PM-025 —— 行為項 4，已覆蓋 2，無對應 **2**

TC：081, 082, 083, 084, 085, 086, 087, 088

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND Front_Panel_OnOff.Req h | 081 | 0.46 | 已覆蓋 | `accept`、`activethen`、`case`、`doe`、`hmi`、`off`、`order`、`pass`、`refer`、`set`、`specification`、`standby`、`state`、`state.if`、`stay`、`thi`、`turn`、`value`、`valuethenif` |
| 2 | IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Medi | 084 | 0.37 | **無對應** | `activation`、`already`、`audio`、`etc`、`media`、`network`、`not_activetlm`、`order`、`quickly`、`request`、`requir`、`respond`、`set`、`stream`、`user`、`value`、`without` |
| 3 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND CLIMATIC_PANEL.Radio_Bt | 085 | 0.46 | 已覆蓋 | `accept`、`activethen`、`case`、`doe`、`hmi`、`off`、`order`、`pass`、`refer`、`set`、`specification`、`standby`、`state`、`state.if`、`stay`、`thi`、`turn`、`value`、`valuethenif` |
| 4 | IF Phone_Call.Info == Not_ActiveTLM has to stop its active functionality (Medi | 084 | 0.37 | **無對應** | `activation`、`already`、`audio`、`etc`、`media`、`network`、`not_activetlm`、`order`、`quickly`、`request`、`requir`、`respond`、`set`、`stream`、`user`、`value`、`without` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`Not_ActiveTLM`、`TLM HMI`、`state.IF`

**R-P127 殘差詞分桶**（合計 72）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **12** | `accept`(#1)、`pass`(#1)、`standby`(#1)、`state`(#1)、`stay`(#1)、`user`(#2)、`accept`(#3)、`pass`(#3)、`standby`(#3)、`state`(#3)、`stay`(#3)、`user`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **60** | `activethen`(#1)、`case`(#1)、`doe`(#1)、`hmi`(#1)、`off`(#1)、`order`(#1)、`refer`(#1)、`set`(#1)、`specification`(#1)、`state.if`(#1)、`thi`(#1)、`turn`(#1) |

### SWE-PM-026 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：089, 090, 091

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND proxi parameter Brand_C | 089 | 0.65 | 已覆蓋 | `audio`、`equal`、`etc`、`media`、`parameter`、`proxi`、`set`、`standbythen`、`status_bh_bcm1.psngrdoorst`、`stream`、`tuner`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND
AND`、`IF`、`OR`、`OR IF`、`THEN
IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 12）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `status_bh_bcm1.psngrdoorst`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **11** | `audio`(#1)、`equal`(#1)、`etc`(#1)、`media`(#1)、`parameter`(#1)、`proxi`(#1)、`set`(#1)、`standbythen`(#1)、`stream`(#1)、`tuner`(#1)、`value`(#1) |

### SWE-PM-027 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：092, 093

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_ | 092 | 0.50 | 已覆蓋 | `back`、`equal`、`hmi`、`maximum`、`need`、`proper`、`set`、`show`、`value` |
| 2 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_ | 093 | 0.57 | 已覆蓋 | `back`、`hmi`、`need`、`proper`、`see`、`set`、`show`、`value`、`vf210` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 18）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `back`(#1)、`equal`(#1)、`hmi`(#1)、`maximum`(#1)、`need`(#1)、`proper`(#1)、`set`(#1)、`show`(#1)、`value`(#1)、`back`(#2)、`hmi`(#2)、`need`(#2) |

### SWE-PM-028 —— 行為項 3，已覆蓋 3，無對應 **0**

TC：094, 095, 096, 097

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activ | 094 | 0.54 | 已覆蓋 | `follow`、`guarante`、`logic`、`min`、`switchoff_timeout_setting.req`、`value` |
| 2 | If Auto_SwitchOn_Setting.Req =="Active ", when Timeout1 == 00 MIN" for LTM Hig | 097 | 0.56 | 已覆蓋 | `case`、`example`、`only`、`parameter`、`restor`、`set`、`specifi`、`thentlm`、`thi`、`value` |
| 3 | AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and  | 096 | 0.75 | 已覆蓋 | `set`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND TLM`、`IF`、`THEN TLM`、`THENTLM`

**R-P127 殘差詞分桶**（合計 18）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **4** | `min`(#1)、`switchoff_timeout_setting.req`(#1)、`set`(#2)、`set`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **14** | `follow`(#1)、`guarante`(#1)、`logic`(#1)、`value`(#1)、`case`(#2)、`example`(#2)、`only`(#2)、`parameter`(#2)、`restor`(#2)、`specifi`(#2)、`thentlm`(#2)、`thi`(#2) |

### SWE-PM-029 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：098, 099, 100, 101

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Successfully" THEN TLM has to set Antitheft_Activ | 099 | 0.39 | **無對應** | `antitheft_activation.req`、`back`、`case`、`example`、`false`、`guarante`、`logic`、`only`、`parameter`、`proxi`、`restor`、`set`、`specifi`、`thentlm`、`thi`、`tlm`、`value` |
| 2 | IF SwitchOff_Timeout_Setting.Req == 00 min THEN TLM has to set Timeout1 to the | 100 | 0.47 | 已覆蓋 | `case`、`example`、`only`、`restor`、`set`、`specifi`、`thi`、`tlm`、`value` |
| 3 | AND TLM has to set TLM_Status.Info and $Telematic_Power$ to "Timed" value and  | 101 | 0.75 | 已覆蓋 | `set`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND TLM`、`IF`、`PROXI`、`THEN TLM`、`THENTLM`

**R-P127 殘差詞分桶**（合計 28）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **10** | `antitheft_activation.req`(#1)、`back`(#1)、`false`(#1)、`set`(#1)、`thi`(#1)、`tlm`(#1)、`set`(#2)、`thi`(#2)、`tlm`(#2)、`set`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **18** | `case`(#1)、`example`(#1)、`guarante`(#1)、`logic`(#1)、`only`(#1)、`parameter`(#1)、`proxi`(#1)、`restor`(#1)、`specifi`(#1)、`thentlm`(#1)、`value`(#1)、`case`(#2) |

### SWE-PM-030 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：102

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Auto_SwitchOn_Setting.Req == Active OR IF Auto_SwitchOn_Setting.Req == Reca | 102 | 0.50 | 已覆蓋 | `depend`、`onthen`、`par`、`recall_last`、`show`、`vplaststatu` |
| 2 | "Splash Screen logo visualization" logics, for Response_Wait_Time | 102 | 0.50 | 已覆蓋 | `logic`、`logo`、`visualization` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR IF`、`Recall_Last`

**R-P127 殘差詞分桶**（合計 9）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **9** | `depend`(#1)、`onthen`(#1)、`par`(#1)、`recall_last`(#1)、`show`(#1)、`vplaststatu`(#1)、`logic`(#2)、`logo`(#2)、`visualization`(#2) |

### SWE-PM-031 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：103

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Rear_View_Camera PROXI parameter == "Present", according to the value of Re | 103 | 0.62 | 已覆蓋 | `accord`、`parameter`、`proxi`、`show`、`telematic_power$`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`PROXI`、`Telematic_Power`

**R-P127 殘差詞分桶**（合計 6）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **6** | `accord`(#1)、`parameter`(#1)、`proxi`(#1)、`show`(#1)、`telematic_power$`(#1)、`value`(#1) |

### SWE-PM-032 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：104

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND STATUS_BH_ | 104 | 0.77 | 已覆蓋 | `set`、`sleep`、`value`、`valuethentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR`

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `set`(#1)、`sleep`(#1)、`value`(#1)、`valuethentlm`(#1) |

**合計**：行為項 **66**，已覆蓋 **52**，無對應 **14**。
