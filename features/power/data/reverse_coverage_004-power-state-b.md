# B1 —— 反向涵蓋報告（R-P118）

> **本報告不判 pass / fail、不使 exit=1**（R-P118(c)）。
> 「無對應」者須逐項人工裁決三選一（R-P118(d)）；**沉默不算裁決**。
> 拆句規則於 `reverse_coverage.py` 一次寫定，對三個 leaf 一體適用。
> 產生指令：`python features/power/scripts/reverse_coverage.py --batch batch_004_power_state_b.json`

## 現況（batch_004_power_state_b.json，50 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-033 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：108, 109

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Partial Operation"AND signal LTM_ | 108 | 0.77 | 已覆蓋 | `set`、`signal`、`value`、`valuethen` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR`

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `set`(#1)、`signal`(#1)、`value`(#1)、`valuethen`(#1) |

### SWE-PM-034 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：110

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Partial Operation" AND signal Fro | 110 | 0.71 | 已覆蓋 | `set`、`signal`、`tlm`、`value` |
| 2 | AND TLM has to show a proper Splash Screen, depending on "Splash Screen logo v | 110 | 0.50 | 已覆蓋 | `depend`、`logic`、`logo`、`tlm`、`visualization` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 9）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **9** | `set`(#1)、`signal`(#1)、`tlm`(#1)、`value`(#1)、`depend`(#2)、`logic`(#2)、`logo`(#2)、`tlm`(#2)、`visualization`(#2) |

### SWE-PM-035 —— 行為項 7，已覆蓋 7，無對應 **0**

TC：111, 112, 113, 114

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activa | 111 | 0.46 | 已覆蓋 | `andit`、`back`、`behaviour`、`depend`、`par`、`parameter`、`possible`、`scenario`、`selectable`、`set`、`show`、`three`、`user` |
| 2 | "Splash Screen logo visualization" logics, for Response_Wait_Time | 111 | 0.50 | 已覆蓋 | `logic`、`logo`、`visualization` |
| 3 | At Response_wait_Time expired TLM has to set VPLastStatus to “On” value and TL | 111 | 0.82 | 已覆蓋 | `expir`、`set` |
| 4 | Behaviour 2: "Auto_SwitchOn_Setting.Req == Not_Active ":TLM has to set VPLastS | 112 | 0.85 | 已覆蓋 | `behaviour`、`set` |
| 5 | Behaviour 3: "Auto_SwitchOn_Setting.Req == Recall_Last":IF VPLastStatus == On  | 113 | 0.64 | 已覆蓋 | `behaviour`、`depend`、`par`、`show` |
| 6 | "Splash Screen logo visualization" logics, for Response_Wait_Time | 111 | 0.50 | 已覆蓋 | `logic`、`logo`、`visualization` |
| 7 | At Response_wait_Time expired then TLM sets TLM_Status.Info and $Telematic_Pow | 111 | 0.64 | 已覆蓋 | `expir`、`idle`、`off`、`set`、`stateif` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`Response_wait_Time`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 32）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `idle`(#7)、`off`(#7) |
| 候選（須人工判 措詞差異 / 真缺口） | **30** | `andit`(#1)、`back`(#1)、`behaviour`(#1)、`depend`(#1)、`par`(#1)、`parameter`(#1)、`possible`(#1)、`scenario`(#1)、`selectable`(#1)、`set`(#1)、`show`(#1)、`three`(#1) |

### SWE-PM-036 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：115

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed"AND signal STATUS_BH_BCM2.R | 115 | 0.81 | 已覆蓋 | `set`、`signal`、`thentlm`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`THENTLM`

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `set`(#1)、`signal`(#1)、`thentlm`(#1)、`value`(#1) |

### SWE-PM-037 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：116

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Timed" AND PhoneCall.Info becames | 116 | 0.80 | 已覆蓋 | `becam`、`set`、`thentlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`THENTLM`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `becam`(#1)、`set`(#1)、`thentlm`(#1) |

### SWE-PM-039 —— 行為項 5，已覆蓋 5，無對應 **0**

TC：117, 118, 119, 120

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the following "Ignition Working Conditions": Ignition Off Ignition On Ignit | 117 | 0.53 | 已覆蓋 | `accord`、`behave`、`engine`、`equal`、`follow`、`occur`、`par`、`receiv`、`signal` |
| 2 | "TLM Operative state management" | 117 | 1.00 | 已覆蓋 | （無） |
| 3 | IF TLM_Status.Info was equal to "Full-Operation" AND SwitchOff_Timeout_Setting | 119 | 0.81 | 已覆蓋 | `min`、`set`、`switchoff_timeout_setting.req` |
| 4 | IF TLM passes to Timed status due to this two conditions, THEN only TLM menu i | 120 | 1.00 | 已覆蓋 | （無） |
| 5 | See TLM HMI documents for TLM items | 120 | 0.80 | 已覆蓋 | `see` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`IF TLM`、`THEN`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 13）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **3** | `equal`(#1)、`min`(#3)、`switchoff_timeout_setting.req`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **10** | `accord`(#1)、`behave`(#1)、`engine`(#1)、`follow`(#1)、`occur`(#1)、`par`(#1)、`receiv`(#1)、`signal`(#1)、`set`(#3)、`see`(#5) |

### SWE-PM-040 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：121

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | When the HU shall power down in a normal sequence into Suspend to RAM | 121 | 1.00 | 已覆蓋 | （無） |
| 2 | The following action shall be taken:If Suspend to RAM is allowed, HU shall sta | 121 | 0.79 | 已覆蓋 | `action`、`follow`、`taken` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `action`(#2)、`follow`(#2)、`taken`(#2) |

### SWE-PM-041 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：122, 123

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off | 122 | 0.82 | 已覆蓋 | `follow`、`pre`、`thi` |
| 2 | Entering this state, TLM has to set Antitheft_Activation.Req to "False" value | 123 | 0.62 | 已覆蓋 | `set`、`state`、`thi` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 6）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `pre`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `follow`(#1)、`thi`(#1)、`set`(#2)、`state`(#2)、`thi`(#2) |

### SWE-PM-042 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：124, 125

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the following "Ignition Working Conditions": Ignition Pre Off, Ignition Off | 124 | 0.82 | 已覆蓋 | `follow`、`pre`、`thi` |
| 2 | Entering this state, TLM has to set Antitheft_Activation.Req to "False" value | 125 | 0.62 | 已覆蓋 | `set`、`state`、`thi` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 6）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `pre`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `follow`(#1)、`thi`(#1)、`set`(#2)、`state`(#2)、`thi`(#2) |

### SWE-PM-043 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：126, 127

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The HU shall keep the backlight OFF during Standby mode except if it is requir | 126 | 0.83 | 已覆蓋 | `except`、`keep` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `except`(#1)、`keep`(#1) |

### SWE-PM-044 —— 行為項 5，已覆蓋 4，無對應 **1**

TC：128, 129, 130, 131

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Standby" OR “Sleep”AND Front_Pane | 128 | 0.65 | 已覆蓋 | `deactivatedthentlm`、`depend`、`par`、`set`、`signal`、`sleep`、`tlm`、`value` |
| 2 | "Splash Screen logo visualization", for Response_Wait_Time | 128 | 0.60 | 已覆蓋 | `logo`、`visualization` |
| 3 | For Splash Screen logo, refer to TLM HMI Specification IF TLM_Status.Info and  | 130 | 0.56 | 已覆蓋 | `deactivatedthentlm`、`depend`、`hmi`、`logo`、`par`、`refer`、`set`、`signal`、`sleep`、`specification`、`tlm`、`value` |
| 4 | "Splash Screen logo visualization", for Response_Wait_Time | 128 | 0.60 | 已覆蓋 | `logo`、`visualization` |
| 5 | For Splash Screen logo, refer to TLM HMI Specification | 128 | 0.29 | **無對應** | `hmi`、`logo`、`refer`、`specification`、`tlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`AND TLM`、`IF`、`OR`、`TLM HMI`

**R-P127 殘差詞分桶**（合計 29）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `sleep`(#1)、`sleep`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **27** | `deactivatedthentlm`(#1)、`depend`(#1)、`par`(#1)、`set`(#1)、`signal`(#1)、`tlm`(#1)、`value`(#1)、`logo`(#2)、`visualization`(#2)、`deactivatedthentlm`(#3)、`depend`(#3)、`hmi`(#3) |

### SWE-PM-045 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：132, 133

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_ | 132 | 0.65 | 已覆蓋 | `back`、`equal`、`maximum`、`need`、`set`、`show`、`sleep`、`time` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`OR`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 8）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `sleep`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **7** | `back`(#1)、`equal`(#1)、`maximum`(#1)、`need`(#1)、`set`(#1)、`show`(#1)、`time`(#1) |

### SWE-PM-046 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：134, 135

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Rear_View_Camera PROXI parameter == "Present" AND Rear_Camera_Enable.Info = | 134 | 0.63 | 已覆蓋 | `about`、`availability`、`detail`、`equal`、`long`、`not_successfully`、`provide`、`refer`、`requirement`、`theneven`、`vf551` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 11）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `long`(#1)、`not_successfully`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **9** | `about`(#1)、`availability`(#1)、`detail`(#1)、`equal`(#1)、`provide`(#1)、`refer`(#1)、`requirement`(#1)、`theneven`(#1)、`vf551`(#1) |

### SWE-PM-047 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：136, 137

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_ | 136 | 0.76 | 已覆蓋 | `back`、`see`、`set`、`sleep`、`vf210` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`OR`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `sleep`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `back`(#1)、`see`(#1)、`set`(#1)、`vf210`(#1) |

### SWE-PM-048 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：138, 139, 140, 141, 142

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activa | 139 | 0.50 | 已覆蓋 | `back`、`behaviour`、`default`、`depend`、`ex-factory`、`full-operation`、`off`、`parameter`、`possible`、`recall_last`、`scenario`、`selectable`、`set`、`stateif`、`three`、`user`、`vplaststatu` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 17）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **9** | `default`(#1)、`ex-factory`(#1)、`full-operation`(#1)、`off`(#1)、`parameter`(#1)、`recall_last`(#1)、`selectable`(#1)、`user`(#1)、`vplaststatu`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **8** | `back`(#1)、`behaviour`(#1)、`depend`(#1)、`possible`(#1)、`scenario`(#1)、`set`(#1)、`stateif`(#1)、`three`(#1) |

### SWE-PM-049 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：143

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Not_Successfully", THEN TLM has to set Antitheft_ | 143 | 0.71 | 已覆蓋 | `back`、`mean`、`see`、`set`、`show`、`vf210` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 6）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **6** | `back`(#1)、`mean`(#1)、`see`(#1)、`set`(#1)、`show`(#1)、`vf210`(#1) |

### SWE-PM-050 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：144

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | ELSE TLM sets VPLastStatus to "Off" value and sets TLM_Status.Info and $Telema | 144 | 0.82 | 已覆蓋 | `set`、`value` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`ELSE TLM`

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `set`(#1)、`value`(#1) |

### SWE-PM-051 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：145

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Successfully"THEN TLM has to set Antitheft_Activa | 145 | 0.80 | 已覆蓋 | `andtlm`、`back`、`set` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`ANDTLM`、`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `andtlm`(#1)、`back`(#1)、`set`(#1) |

### SWE-PM-052 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：146

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF Antitheft_Result.Info == "Not_Successfully"THEN TLM has to set Antitheft_Ac | 146 | 0.76 | 已覆蓋 | `back`、`see`、`set`、`show`、`vf210` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `back`(#1)、`see`(#1)、`set`(#1)、`show`(#1)、`vf210`(#1) |

### SWE-PM-053 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：147

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | TLM has to read Brand_Configuration_2 PROXI parameter in order to show the veh | 147 | 0.82 | 已覆蓋 | `order`、`show` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `order`(#1)、`show`(#1) |

### SWE-PM-054 —— 行為項 4，已覆蓋 4，無對應 **0**

TC：148, 149, 150, 151

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | - IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM ha | 148 | 0.93 | 已覆蓋 | `tlm` |
| 2 | - IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM | 149 | 0.82 | 已覆蓋 | `show`、`tlm` |
| 3 | - IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM h | 150 | 0.82 | 已覆蓋 | `show`、`tlm` |
| 4 | - IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TL | 151 | 0.83 | 已覆蓋 | `show`、`tlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 7）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **3** | `show`(#2)、`show`(#3)、`show`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `tlm`(#1)、`tlm`(#2)、`tlm`(#3)、`tlm`(#4) |

### SWE-PM-055 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：152, 153

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch | 152 | 0.91 | 已覆蓋 | `use` |
| 2 | The ETM shall use $SplashScreen_Type$ = [Klipsch (7)] to display the Klipsch S | 153 | 0.90 | 已覆蓋 | `use` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `use`(#1)、`use`(#2) |

### SWE-PM-056 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：154

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace  | 154 | 0.86 | 已覆蓋 | `replace`、`vc_veh_brand$` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`VC_Veh_Brand`

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `replace`(#1)、`vc_veh_brand$`(#1) |

### SWE-PM-058 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：155

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | Default:The ex-factory default must be "SwitchOff_Timeout_Setting.Req == 00 MI | 155 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 0）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **0** | （無） |

### SWE-PM-059 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：156, 157

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF TLM_Status.Info and $Telematic_Power$ == "Standby"AND a Network Sleep reque | 156 | 0.71 | 已覆蓋 | `occursthen`、`pas`、`provid`、`set`、`value` |
| 2 | If TLM Boot is not ended, TLM has to wait for its end before passing to Sleep  | 157 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `occursthen`(#1)、`pas`(#1)、`provid`(#1)、`set`(#1)、`value`(#1) |

**合計**：行為項 **48**，已覆蓋 **47**，無對應 **1**。
