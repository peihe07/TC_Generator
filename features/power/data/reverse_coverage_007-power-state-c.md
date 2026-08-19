# B1 —— 反向涵蓋報告（R-P118）

> **本報告不判 pass / fail、不使 exit=1**（R-P118(c)）。
> 「無對應」者須逐項人工裁決三選一（R-P118(d)）；**沉默不算裁決**。
> 拆句規則於 `reverse_coverage.py` 一次寫定，對三個 leaf 一體適用。
> 產生指令：`python features/power/scripts/reverse_coverage.py --batch batch_007_power_state_c.json`

## 現況（batch_007_power_state_c.json，20 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-001 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：261, 262

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Star | 262 | 0.67 | 已覆蓋 | `follow`、`relat`、`statu`、`thi` |
| 2 | All TLM, AMP/ICS/DTV functionalities are available | 261 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `follow`(#1)、`relat`(#1)、`statu`(#1)、`thi`(#1) |

### SWE-PM-002 —— 行為項 6，已覆蓋 6，無對應 **0**

TC：263, 264, 265, 266

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | This status is related to TLM audio is OFF | 263 | 0.50 | 已覆蓋 | `relat`、`statu`、`thi` |
| 2 | TLM shall allow only Splash Screen visualization on its display | 263 | 0.86 | 已覆蓋 | `visualization` |
| 3 | ICS functionalities are available | 264 | 1.00 | 已覆蓋 | （無） |
| 4 | DTV shall be OFF | 264 | 1.00 | 已覆蓋 | （無） |
| 5 | Rear View Camera images shall be available if needed | 265 | 1.00 | 已覆蓋 | （無） |
| 6 | In this state, user cannot do any setting All TLM functionalities run in backg | 266 | 0.50 | 已覆蓋 | `background`、`but`、`cannot`、`do`、`functionaliti`、`ready`、`run`、`state`、`thi` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 13）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `functionaliti`(#6)、`state`(#6) |
| 候選（須人工判 措詞差異 / 真缺口） | **11** | `relat`(#1)、`statu`(#1)、`thi`(#1)、`visualization`(#2)、`background`(#6)、`but`(#6)、`cannot`(#6)、`do`(#6)、`ready`(#6)、`run`(#6)、`thi`(#6) |

### SWE-PM-003 —— 行為項 5，已覆蓋 4，無對應 **1**

TC：267, 268, 269, 270

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In this mode TLM shall shall report $Telematic_Power$ = " Partial_Operation" | 267 | 0.83 | 已覆蓋 | `thi` |
| 2 | This mode shall exist for AMP, ICS, and DTV when STATUS_BH_BCM2.RemStActvSts i | 267 | 0.68 | 已覆蓋 | `equal`、`exist`、`reciev`、`relat`、`statu`、`thi` |
| 3 | AMP/ICS/DTV shall be OFF | 267 | 1.00 | 已覆蓋 | （無） |
| 4 | Audio for ANC, ACN, and chimes (if equipped) shall be active in this state) Al | 267 | 0.24 | **無對應** | `acn`、`anc`、`audio`、`background`、`but`、`change`、`chim`、`enabl`、`equipp`、`except`、`functionaliti`、`hmi`、`interaction`、`permit`、`ready`、`run`、`statu`、`thi`、`within` |
| 5 | the R1 HU shall not enter stolen vehicle mode under any condition | 270 | 0.88 | 已覆蓋 | `r1` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`TLM OFF`

**R-P127 殘差詞分桶**（合計 27）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **12** | `statu`(#2)、`acn`(#4)、`anc`(#4)、`audio`(#4)、`change`(#4)、`chim`(#4)、`enabl`(#4)、`equipp`(#4)、`hmi`(#4)、`interaction`(#4)、`permit`(#4)、`statu`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **15** | `thi`(#1)、`equal`(#2)、`exist`(#2)、`reciev`(#2)、`relat`(#2)、`thi`(#2)、`background`(#4)、`but`(#4)、`except`(#4)、`functionaliti`(#4)、`ready`(#4)、`run`(#4) |

### SWE-PM-004 —— 行為項 6，已覆蓋 3，無對應 **3**

TC：271, 272

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | This status is related to TLM ON | 271 | 0.25 | **無對應** | `relat`、`statu`、`thi` |
| 2 | All TLM AMP/ICS/DTV shall be ON and functionalities are available | 271 | 1.00 | 已覆蓋 | （無） |
| 3 | Entering this state, TLM is ON for a limited time | 271 | 0.67 | 已覆蓋 | `enter`、`thi` |
| 4 | Phone Call management in Timed state for further details and par | 271 | 0.25 | **無對應** | `call`、`detail`、`further`、`management`、`par`、`phone` |
| 5 | Configuration parameters for Timeout1 details | 271 | 0.25 | **無對應** | `configuration`、`detail`、`parameter` |
| 6 | In “Timed Mode” the Customer setting screens shall be disabled | 272 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`TLM AMP`

**R-P127 殘差詞分桶**（合計 14）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **14** | `relat`(#1)、`statu`(#1)、`thi`(#1)、`enter`(#3)、`thi`(#3)、`call`(#4)、`detail`(#4)、`further`(#4)、`management`(#4)、`par`(#4)、`phone`(#4)、`configuration`(#5) |

### SWE-PM-005 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：273, 274

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | This status is related to TLM OFF with Network on No TLM, FPDM, AMP, ICS, and  | 273 | 0.75 | 已覆蓋 | `relat`、`statu`、`thi` |
| 2 | Entering this state, TLM has to set Antitheft_Activation.Req to "False" value | 274 | 0.50 | 已覆蓋 | `set`、`state`、`thi`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`TLM OFF`

**R-P127 殘差詞分桶**（合計 7）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `state`(#2) |
| 候選（須人工判 措詞差異 / 真缺口） | **6** | `relat`(#1)、`statu`(#1)、`thi`(#1)、`set`(#2)、`thi`(#2)、`value`(#2) |

### SWE-PM-006 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：275, 276

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | This status is related to TLM OFF with Network off No TLM, FPDM AMP, ICS, and  | 275 | 0.75 | 已覆蓋 | `relat`、`statu`、`thi` |
| 2 | Entering this state, TLM has to set Antitheft_Activation.Req to "False" value | 276 | 0.50 | 已覆蓋 | `set`、`state`、`thi`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`FPDM AMP`、`TLM OFF`

**R-P127 殘差詞分桶**（合計 7）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `state`(#2) |
| 候選（須人工判 措詞差異 / 真缺口） | **6** | `relat`(#1)、`statu`(#1)、`thi`(#1)、`set`(#2)、`thi`(#2)、`value`(#2) |

### SWE-PM-007 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：277

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the "Ignition Working Conditions" "Ignition Off" This status is related to  | 277 | 0.53 | 已覆蓋 | `component`、`development`、`diagnostic`、`only`、`relat`、`relatively`、`statu`、`test`、`thi` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`DTV ON`、`TLM AMP`

**R-P127 殘差詞分桶**（合計 9）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **9** | `component`(#1)、`development`(#1)、`diagnostic`(#1)、`only`(#1)、`relat`(#1)、`relatively`(#1)、`statu`(#1)、`test`(#1)、`thi`(#1) |

### SWE-PM-009 —— 行為項 10，已覆蓋 5，無對應 **5**

TC：278, 279, 280

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | First default values for TLM are: TLM_Status.Info, $Telematic_Power$ equal to  | 278 | 0.78 | 已覆蓋 | `equal`、`value` |
| 2 | VPLastStatus equal to "On" value | 278 | 0.33 | **無對應** | `equal`、`value` |
| 3 | SwitchOff_Timeout_Setting.Req equal to "00 min" == Timeout1 equal to 00 minute | 278 | 0.40 | **無對應** | `equal`、`minut`、`timeout1` |
| 4 | Timeout1 equal to 00 minutes for LTM High Auto_SwitchOn_Setting.Req equal to " | 278 | 0.25 | **無對應** | `equal`、`high`、`ltm`、`minut`、`timeout1`、`value` |
| 5 | Antitheft_Activation.Req equal to "False" value | 278 | 0.50 | 已覆蓋 | `equal`、`value` |
| 6 | RemStartFail equal to “False” value | 278 | 0.50 | 已覆蓋 | `equal`、`value` |
| 7 | IF the voltage exceeds the higher or the lower voltage threshold for a certain | 279 | 0.44 | **無對應** | `also`、`certain`、`event`、`exceed`、`higher`、`lower`、`threshold`、`time`、`voltage` |
| 8 | until certain conditions that allow TLM to exit from this status occur | 280 | 0.25 | **無對應** | `allow`、`certain`、`condition`、`occur`、`statu`、`thi` |
| 9 | After a battery reconnection and also when TLM has to exit INIT state (as soon | 280 | 0.49 | 已覆蓋 | `able`、`accord`、`also`、`behave`、`certain`、`limit`、`par`、`properly`、`reconnection`、`requirement`、`reset`、`soon`、`threshold`、`user`、`variabl`、`voltage`、`within`、`work` |
| 10 | "TLM_Status.Info and $Telematic_Power$ signal setting", setting TLM_Status.Inf | 278 | 0.50 | 已覆蓋 | `sett`、`signal`、`start`、`state` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`LTM`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 54）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **3** | `time`(#7)、`start`(#10)、`state`(#10) |
| 候選（須人工判 措詞差異 / 真缺口） | **51** | `equal`(#1)、`value`(#1)、`equal`(#2)、`value`(#2)、`equal`(#3)、`minut`(#3)、`timeout1`(#3)、`equal`(#4)、`high`(#4)、`ltm`(#4)、`minut`(#4)、`timeout1`(#4) |

**合計**：行為項 **34**，已覆蓋 **25**，無對應 **9**。
