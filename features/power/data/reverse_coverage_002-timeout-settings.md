# B1 —— 反向涵蓋報告（R-P118）

> **本報告不判 pass / fail、不使 exit=1**（R-P118(c)）。
> 「無對應」者須逐項人工裁決三選一（R-P118(d)）；**沉默不算裁決**。
> 拆句規則於 `reverse_coverage.py` 一次寫定，對三個 leaf 一體適用。
> 產生指令：`python features/power/scripts/reverse_coverage.py --batch batch_002_timeout_settings.json`

## 現況（batch_002_timeout_settings.json，26 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-057 —— 行為項 15，已覆蓋 15，無對應 **0**

TC：018, 019, 020

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF "Switch_Off_Time" parameter is set to "20 minutes" then the user can select | 018 | 0.90 | 已覆蓋 | `user` |
| 2 | so Timeout1 is equal to "00 min" OR "20 minutes" respectively | 018 | 0.60 | 已覆蓋 | `equal`、`respectively` |
| 3 | IF "Switch_Off_Time" parameter is set to "60 minutes" then the user can select | 018 | 0.90 | 已覆蓋 | `user` |
| 4 | so Timeout1 is equal to "00 min" OR "60 minutes" respectively | 018 | 0.60 | 已覆蓋 | `equal`、`respectively` |
| 5 | IF "Switch_Off_Time" parameter is set to "180 minutes" then the user can selec | 018 | 0.90 | 已覆蓋 | `user` |
| 6 | so Timeout1 is equal to "00 min" OR "180 minutes" respectively | 018 | 0.60 | 已覆蓋 | `equal`、`respectively` |
| 7 | For the case of LTM High Radio not present, the user can select SwitchOff_Time | 018 | 0.67 | 已覆蓋 | `case`、`equal`、`present`、`specifi`、`user` |
| 8 | For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management s | 018 | 0.47 | 已覆蓋 | `auto_switchon_setting.req`、`case`、`equal`、`management`、`present`、`section`、`see`、`through`、`user` |
| 9 | So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minut | 018 | 0.75 | 已覆蓋 | `equal`、`user` |
| 10 | IF "Switch_Off_Time" parameter is set to "20 minutes" then the user can select | 018 | 0.90 | 已覆蓋 | `user` |
| 11 | so Timeout1 is equal to "00 min" OR "20 minutes" respectively | 018 | 0.60 | 已覆蓋 | `equal`、`respectively` |
| 12 | IF "Switch_Off_Time" parameter is set to "60 minutes" then the user can select | 018 | 0.90 | 已覆蓋 | `user` |
| 13 | so Timeout1 is equal to "00 min" OR "60 minutes" respectively | 018 | 0.60 | 已覆蓋 | `equal`、`respectively` |
| 14 | IF "Switch_Off_Time" parameter is set to "180 minutes" then the user can selec | 018 | 0.90 | 已覆蓋 | `user` |
| 15 | so Timeout1 is equal to "00 min" OR "180 minutes" respectively | 018 | 0.60 | 已覆蓋 | `equal`、`respectively` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`Auto_SwitchOn_Setting.Req`、`IF`、`IF PROXI`、`OR`

**R-P127 殘差詞分桶**（合計 34）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **34** | `user`(#1)、`equal`(#2)、`respectively`(#2)、`user`(#3)、`equal`(#4)、`respectively`(#4)、`user`(#5)、`equal`(#6)、`respectively`(#6)、`case`(#7)、`equal`(#7)、`present`(#7) |

### SWE-PM-060 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：021, 022

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting | 021 | 0.75 | 已覆蓋 | `mean`、`set` |
| 2 | For other Radios the user can set two parameters, by means of SwitchOff_Timeou | 022 | 0.67 | 已覆蓋 | `mean`、`selectable`、`set`、`signal` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 6）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **6** | `mean`(#1)、`set`(#1)、`mean`(#2)、`selectable`(#2)、`set`(#2)、`signal`(#2) |

### SWE-PM-061 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：023, 024

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | These settings could be only done in TLM Full-Operation Status | 023 | 0.50 | 已覆蓋 | `could`、`done`、`only`、`these` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `could`(#1)、`done`(#1)、`only`(#1)、`these`(#1) |

### SWE-PM-062 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：025, 026, 027

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | User can select Auto_SwitchOn_Setting.Req value equal to "Active" (If LTM High | 026 | 0.69 | 已覆蓋 | `active`、`equal`、`recall_last`、`user` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `active`(#1)、`recall_last`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `equal`(#1)、`user`(#1) |

### SWE-PM-063 —— 行為項 1，已覆蓋 0，無對應 **1**

TC：028

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In Timed state, it is possible either to make and to receive one or more bluet | 028 | 0.32 | **無對應** | `accord`、`depend`、`either`、`follow`、`logic`、`make`、`maxcalltimeout`、`more`、`one`、`parameter`、`possible`、`time`、`timeout1` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 13）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **13** | `accord`(#1)、`depend`(#1)、`either`(#1)、`follow`(#1)、`logic`(#1)、`make`(#1)、`maxcalltimeout`(#1)、`more`(#1)、`one`(#1)、`parameter`(#1)、`possible`(#1)、`time`(#1) |

### SWE-PM-064 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：029, 030

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | MaxCallTimeout starts in the following two conditions: Timeout1 == 00 min: IF  | 029 | 0.83 | 已覆蓋 | `equal`、`follow`、`two` |
| 2 | Timeout1 <> 00 min: at Timeout1 expiration, only IF Phone_Call.Info is still e | 030 | 0.71 | 已覆蓋 | `equal`、`only` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`OR`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `equal`(#1)、`follow`(#1)、`two`(#1)、`equal`(#2)、`only`(#2) |

### SWE-PM-065 —— 行為項 2，已覆蓋 1，無對應 **1**

TC：031, 032

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active"  | 031 | 0.46 | 已覆蓋 | `bt`、`case`、`entertainment`、`example`、`expiration`、`featur`、`like`、`manag`、`minutesand`、`pass`、`rather`、`restore`、`stay`、`stream`、`usb` |
| 2 | In this case, TLM is still able to manage other possible phone calls within Ti | 032 | 0.36 | **無對應** | `able`、`case`、`expiration`、`manage`、`phone`、`possible`、`thi` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`BT`、`IF`、`THEN TLM`、`USB`

**R-P127 殘差詞分桶**（合計 22）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `manag`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **21** | `bt`(#1)、`case`(#1)、`entertainment`(#1)、`example`(#1)、`expiration`(#1)、`featur`(#1)、`like`(#1)、`minutesand`(#1)、`pass`(#1)、`rather`(#1)、`restore`(#1)、`stay`(#1) |

### SWE-PM-038 —— 行為項 15，已覆蓋 15，無對應 **0**

TC：033, 034, 035, 036, 037, 038, 039, 040, 041, 042, 043

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active"  | 033 | 0.61 | 已覆蓋 | `bt`、`call`、`dab`、`else`、`entertainment`、`etc`、`example`、`expiration`、`featur`、`like`、`manag`、`minutesand`、`rather`、`restore`、`tuner`、`usb` |
| 2 | In this case, TLM is still able to manage other possible phone calls within Ti | 035 | 0.46 | 已覆蓋 | `able`、`manage`、`phone`、`possible`、`thi`、`within` |
| 3 | Case 2:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info is still "Active" at "T | 035 | 0.85 | 已覆蓋 | `expirationthenat`、`minutesand` |
| 4 | until Phone_Call.Info passes to "Not_Active" OR at maximum | 033 | 0.75 | 已覆蓋 | `maximum` |
| 5 | until MaxCallTimeout expiration | 035 | 1.00 | 已覆蓋 | （無） |
| 6 | WHEN Phone_Call.Info passes to "Not_Active", OR at MaxCallTimeout expiration,  | 033 | 0.82 | 已覆蓋 | `expiration`、`maxcalltimeout` |
| 7 | WHEN Phone_Call.Info passes to "Not_Active", OR at MaxCallTimeout expiration,  | 033 | 0.85 | 已覆蓋 | `expiration`、`maxcalltimeout` |
| 8 | Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Time | 033 | 0.69 | 已覆蓋 | `expiration`、`minutesand`、`pas`、`thentlm` |
| 9 | Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Time | 033 | 0.73 | 已覆蓋 | `expiration`、`minutesand`、`pas`、`thentlm` |
| 10 | Case 4:IF Timeout1 == 00 minutesAND in Full-Operation state Phone_Call.Info si | 043 | 0.67 | 已覆蓋 | `equal`、`minutesand`、`pas`、`pass`、`signal`、`start`、`thentlm` |
| 11 | In this case, TLM has to manage the phone call(s) and to stay in Timed state | 034 | 0.60 | 已覆蓋 | `manage`、`phone`、`s`、`thi` |
| 12 | until Phone_Call.Info passes to "Not_Active" value OR at maximum | 033 | 0.80 | 已覆蓋 | `maximum` |
| 13 | until MaxCallTimeout expires | 035 | 1.00 | 已覆蓋 | （無） |
| 14 | IF any of the previous condition occurs, THEN TLM has to set TLM_Status.Info t | 033 | 0.60 | 已覆蓋 | `condition`、`occur`、`pas`、`previou` |
| 15 | IF any of the previous condition occurs, THEN TLM has to set RemStartFail to “ | 033 | 0.67 | 已覆蓋 | `condition`、`occur`、`pas`、`previou` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`BT`、`ELSE TLM`、`IF`、`OR`、`THEN
IF`、`THEN TLM`、`THENTLM`、`USB`、`WHEN`

**R-P127 殘差詞分桶**（合計 57）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **17** | `call`(#1)、`dab`(#1)、`expiration`(#1)、`restore`(#1)、`tuner`(#1)、`expiration`(#6)、`maxcalltimeout`(#6)、`expiration`(#7)、`maxcalltimeout`(#7)、`expiration`(#8)、`expiration`(#9)、`pass`(#10) |
| 候選（須人工判 措詞差異 / 真缺口） | **40** | `bt`(#1)、`else`(#1)、`entertainment`(#1)、`etc`(#1)、`example`(#1)、`featur`(#1)、`like`(#1)、`manag`(#1)、`minutesand`(#1)、`rather`(#1)、`usb`(#1)、`able`(#2) |

**合計**：行為項 **39**，已覆蓋 **37**，無對應 **2**。
