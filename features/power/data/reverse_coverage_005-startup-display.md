# B1 —— 反向涵蓋報告（R-P118）

> **本報告不判 pass / fail、不使 exit=1**（R-P118(c)）。
> 「無對應」者須逐項人工裁決三選一（R-P118(d)）；**沉默不算裁決**。
> 拆句規則於 `reverse_coverage.py` 一次寫定，對三個 leaf 一體適用。
> 產生指令：`python features/power/scripts/reverse_coverage.py --batch batch_005_startup_display.json`

## 現況（batch_005_startup_display.json，66 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-066 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：158, 159

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The HU shall consider SOS and Assist calls as Phone calls becoming active | 158 | 0.75 | 已覆蓋 | `assist`、`consider` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **1** | `assist`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **1** | `consider`(#1) |

### SWE-PM-067 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：160

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The HU shall consider Projection device calls as Phone calls becoming active | 160 | 0.88 | 已覆蓋 | `consider` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 1）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **1** | `consider`(#1) |

### SWE-PM-068 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：161

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone cal | 161 | 0.86 | 已覆蓋 | `bypas`、`due` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN`

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `bypas`(#1)、`due`(#1) |

### SWE-PM-069 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：162, 163

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone cal | 162 | 0.82 | 已覆蓋 | `due`、`projection`、`ui` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`THEN`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `projection`(#1)、`ui`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **1** | `due`(#1) |

### SWE-PM-070 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：164

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone cal | 164 | 0.82 | 已覆蓋 | `bypas`、`due` |
| 2 | THEN if the HU returns to IDLE when the phone call becomes inactive, the HU sh | 164 | 0.92 | 已覆蓋 | `show` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `bypas`(#1)、`due`(#1)、`show`(#2) |

### SWE-PM-074 —— 行為項 2，已覆蓋 1，無對應 **1**

TC：165, 166, 167

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If there is a FOTA update available for the Radio, TBM, or ROV (see CFTS057) w | 165 | 0.79 | 已覆蓋 | `cfts057`、`rov`、`see`、`tbm` |
| 2 | See HMI for pop-up details | 165 | 0.25 | **無對應** | `detail`、`hmi`、`see` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 7）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `rov`(#1)、`tbm`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `cfts057`(#1)、`see`(#1)、`detail`(#2)、`hmi`(#2)、`see`(#2) |

### SWE-PM-075 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：168, 169, 170

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If the HU Transitions to Timed mode due to the condition described in CFTS009- | 168 | 0.73 | 已覆蓋 | `accdlyact$`、`active`、`dismiss`、`inactive`、`interact`、`pop` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 6）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **5** | `accdlyact$`(#1)、`active`(#1)、`dismiss`(#1)、`inactive`(#1)、`pop`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **1** | `interact`(#1) |

### SWE-PM-076 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：171, 172, 173

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | When the HU Receives $ICSPowerButton$ = [Pressed] for 10 seconds consecutively | 171 | 0.69 | 已覆蓋 | `cpu`、`main`、`micro`、`receiv`、`save` |
| 2 | If the HU is currently installing a firmware image the HU shall not reset due  | 173 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **3** | `cpu`(#1)、`main`(#1)、`micro`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `receiv`(#1)、`save`(#1) |

### SWE-PM-093 —— 行為項 14，已覆蓋 14，無對應 **0**

TC：174, 175, 176, 177, 178, 179, 180, 181, 182

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when | 176 | 0.79 | 已覆蓋 | `ajar`、`sleep`、`standby`、`statu` |
| 2 | The startup animation will be unique for each vehicle or/and brand as defined  | 174 | 0.56 | 已覆蓋 | `brand`、`pdo`、`startup`、`unique` |
| 3 | If driver door is not present or removed for current vehicle ($DriverDoorOnOff | 181 | 0.52 | 已覆蓋 | `ajar`、`chang`、`current`、`door_off`、`driverdooronoffsts$`、`due`、`event`、`ignition`、`present`、`remov`、`tim`、`vehicle` |
| 4 | While HU is playing a start-up animation and HU changes mode (due to ignition  | 179 | 0.76 | 已覆蓋 | `body`、`chang`、`due`、`statu`、`tim` |
| 5 | Once a start-up animation is played, HU shall not play the next start-up anima | 182 | 0.83 | 已覆蓋 | `once` |
| 6 | until the next CAN wakeup cycle OR at least 30 minutes passed from last time t | 182 | 0.77 | 已覆蓋 | `last`、`least`、`pass` |
| 7 | given all other conditions are met for startup animation to play as defined he | 182 | 0.50 | 已覆蓋 | `defin`、`given`、`here`、`startup` |
| 8 | While HU is in SLEEP MODE, STANDBY MODE, or in PARTIAL OPERATION MODE and when | 176 | 0.79 | 已覆蓋 | `ajar`、`sleep`、`standby`、`statu` |
| 9 | The startup animation will be unique for each vehicle or/and brand as defined  | 174 | 0.56 | 已覆蓋 | `brand`、`pdo`、`startup`、`unique` |
| 10 | If driver door is not present or removed for current vehicle ($DriverDoorOnOff | 181 | 0.52 | 已覆蓋 | `ajar`、`chang`、`current`、`door_off`、`driverdooronoffsts$`、`due`、`event`、`ignition`、`present`、`remov`、`tim`、`vehicle` |
| 11 | While HU is playing a start-up animation and HU changes mode (due to ignition  | 179 | 0.76 | 已覆蓋 | `body`、`chang`、`due`、`statu`、`tim` |
| 12 | Once a start-up animation is played, HU shall not play the next start-up anima | 182 | 0.83 | 已覆蓋 | `once` |
| 13 | until the next CAN wakeup cycle OR at least 30 minutes passed from last time t | 182 | 0.77 | 已覆蓋 | `last`、`least`、`pass` |
| 14 | given all other conditions are met for startup animation to play as defined he | 182 | 0.50 | 已覆蓋 | `defin`、`given`、`here`、`startup` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`OR`、`PDO`

**R-P127 殘差詞分桶**（合計 66）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **36** | `sleep`(#1)、`standby`(#1)、`statu`(#1)、`chang`(#3)、`current`(#3)、`door_off`(#3)、`driverdooronoffsts$`(#3)、`event`(#3)、`ignition`(#3)、`present`(#3)、`remov`(#3)、`tim`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **30** | `ajar`(#1)、`brand`(#2)、`pdo`(#2)、`startup`(#2)、`unique`(#2)、`ajar`(#3)、`due`(#3)、`due`(#4)、`once`(#5)、`last`(#6)、`least`(#6)、`pass`(#6) |

### SWE-PM-094 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：183

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The HU shall display the startup animation separately from the Splash screen a | 183 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 0）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **0** | （無） |

### SWE-PM-095 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：184

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | As soon as signal LTM_OperationalModeSts.Info becomes different from "SNA" val | 184 | 0.74 | 已覆蓋 | `becom`、`behave`、`consider`、`signal`、`soon` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `becom`(#1)、`behave`(#1)、`consider`(#1)、`signal`(#1)、`soon`(#1) |

### SWE-PM-097 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：185

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If DID "Startup Animation Selection" = [Fiat Latam] then the HU shall replace  | 185 | 0.86 | 已覆蓋 | `replace`、`vc_veh_brand$` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`VC_Veh_Brand`

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `replace`(#1)、`vc_veh_brand$`(#1) |

### SWE-PM-098 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：186

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If $Themed_Sound$ = [Fiat Latam] and the "Welcome Onboard Sound" setting is se | 186 | 0.93 | 已覆蓋 | `set` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 1）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **1** | `set`(#1) |

### SWE-PM-099 —— 行為項 3，已覆蓋 3，無對應 **0**

TC：187, 188, 189, 190

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is se | 187 | 0.94 | 已覆蓋 | `set` |
| 2 | For the purposes of CFTS009-2299, the HU shall consider it a new "day" to allo | 188 | 0.79 | 已覆蓋 | `cfts009-2299`、`consider`、`purpos` |
| 3 | including manual time adjustments from the user, the time passing midnight, or | 190 | 0.58 | 已覆蓋 | `includ`、`manual`、`midnight`、`pass`、`user` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`2299`、`AND`

**R-P127 殘差詞分桶**（合計 9）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **3** | `manual`(#3)、`midnight`(#3)、`pass`(#3) |
| 候選（須人工判 措詞差異 / 真缺口） | **6** | `set`(#1)、`cfts009-2299`(#2)、`consider`(#2)、`purpos`(#2)、`includ`(#3)、`user`(#3) |

### SWE-PM-100 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：191

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If $Themed_Sound$ = [Fiat Latam] AND the "Welcome Onboard Sound" setting is se | 191 | 0.80 | 已覆蓋 | `begin`、`set`、`time` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `begin`(#1)、`set`(#1)、`time`(#1) |

### SWE-PM-101 —— 行為項 4，已覆蓋 4，無對應 **0**

TC：192, 193, 194, 195

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | - IF SDARS_Presence == "Absent" AND Audio_Brand == "No Audio Brand"THEN TLM ha | 192 | 0.93 | 已覆蓋 | `tlm` |
| 2 | - IF SDARS_Presence == "Absent" AND Audio_Brand == "Beats Brand White"THEN TLM | 193 | 0.82 | 已覆蓋 | `show`、`tlm` |
| 3 | - IF SDARS_Presence == "Present" AND Audio_Brand == "No Audio Brand"THEN TLM h | 194 | 0.82 | 已覆蓋 | `show`、`tlm` |
| 4 | - IF SDARS_Presence == "Present" AND Audio_Brand == "Beats Brand White"THEN TL | 195 | 0.83 | 已覆蓋 | `show`、`tlm` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`IF`、`THEN TLM`

**R-P127 殘差詞分桶**（合計 7）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **3** | `show`(#2)、`show`(#3)、`show`(#4) |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `tlm`(#1)、`tlm`(#2)、`tlm`(#3)、`tlm`(#4) |

### SWE-PM-102 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：196, 197

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The ETM shall use $VC_SpecialPKG_IC$ = [Tungsten (147)] to display the Klipsch | 196 | 0.91 | 已覆蓋 | `use` |
| 2 | The ETM shall use $SplashScreen_Type$ = [Klipsch (7)] to display the Klipsch S | 197 | 0.90 | 已覆蓋 | `use` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `use`(#1)、`use`(#2) |

### SWE-PM-103 —— 行為項 4，已覆蓋 4，無對應 **0**

TC：198, 199

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | In the following "Ignition Working Conditions": Ignition On, Ignition Pre_Star | 199 | 0.71 | 已覆蓋 | `crank`、`follow`、`pre_start`、`start` |
| 2 | TLM shall allow only Splash Screen visualization on its display | 198 | 1.00 | 已覆蓋 | （無） |
| 3 | ICS functionalities are available | 199 | 1.00 | 已覆蓋 | （無） |
| 4 | DTV shall be OFF | 199 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`Pre_Start`

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `crank`(#1)、`follow`(#1)、`pre_start`(#1)、`start`(#1) |

### SWE-PM-104 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：200, 201, 202, 203, 204

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The splash screen and disclaimer screen shall be shown the first time each bus | 201 | 0.86 | 已覆蓋 | `mod`、`tim` |
| 2 | If the disclaimer screen needs to be shown it shall be shown the first time ea | 202 | 0.71 | 已覆蓋 | `full`、`mod`、`operation`、`partial`、`standby` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 7）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **5** | `tim`(#1)、`full`(#2)、`operation`(#2)、`partial`(#2)、`standby`(#2) |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `mod`(#1)、`mod`(#2) |

### SWE-PM-105 —— 行為項 2，已覆蓋 0，無對應 **2**

TC：205, 206, 207, 208, 209, 210, 211, 212

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | The disclaimer and splash screen can be temporarily skipped for incoming/outgo | 210 | 0.41 | **無對應** | `backup`、`but`、`camera`、`climate`、`display`、`dur`、`fota`、`full`、`incom`、`mod`、`next`、`ongo`、`operation`、`outgo`、`pop`、`pop-up`、`ups` |
| 2 | See HMI logic and Flow "Startup" requirements for details | 205 | 0.14 | **無對應** | `detail`、`flow`、`hmi`、`logic`、`requirement`、`see` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 23）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **13** | `backup`(#1)、`camera`(#1)、`climate`(#1)、`display`(#1)、`fota`(#1)、`full`(#1)、`incom`(#1)、`next`(#1)、`ongo`(#1)、`operation`(#1)、`outgo`(#1)、`pop`(#1) |
| 候選（須人工判 措詞差異 / 真缺口） | **10** | `but`(#1)、`dur`(#1)、`mod`(#1)、`ups`(#1)、`detail`(#2)、`flow`(#2)、`hmi`(#2)、`logic`(#2)、`requirement`(#2)、`see`(#2) |

### SWE-PM-106 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：213

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | For all variations of the disclaimer screen and geolocation pop up listed belo | 213 | 0.71 | 已覆蓋 | `below`、`geolocation`、`parameter`、`pop` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `below`(#1)、`geolocation`(#1)、`parameter`(#1)、`pop`(#1) |

### SWE-PM-107 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：214

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | For all variations of the disclaimer screen and geolocation pop up listed belo | 214 | 0.69 | 已覆蓋 | `below`、`geolocation`、`parameter`、`pop`、`replace` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **5** | `below`(#1)、`geolocation`(#1)、`parameter`(#1)、`pop`(#1)、`replace`(#1) |

### SWE-PM-108 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：215

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If $VC_VEH_BRAND$ <> [Maserati] the R1 Head Unit shall only show the core disc | 215 | 0.92 | 已覆蓋 | `r1` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**R-P127 殘差詞分桶**（合計 1）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **1** | `r1`(#1) |

### SWE-PM-109 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：216

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present] AND $Country_Cod | 216 | 0.83 | 已覆蓋 | `configuration`、`countri`、`see`、`table` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`

**R-P127 殘差詞分桶**（合計 4）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **4** | `configuration`(#1)、`countri`(#1)、`see`(#1)、`table`(#1) |

### SWE-PM-110 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：217, 218

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR $Country | 218 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`OR`

**R-P127 殘差詞分桶**（合計 0）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **0** | （無） |

### SWE-PM-111 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：219, 220

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | For all screen sizes except 7 inch | 219 | 0.50 | 已覆蓋 | `except`、`siz` |
| 2 | If $VC_VEH_BRAND$ <> [Maserati] AND ($TBM_Present$ = [Not Present] OR$Country_ | 220 | 0.79 | 已覆蓋 | `or$country_code$`、`present`、`tbm_present$` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`、`OR`

**R-P127 殘差詞分桶**（合計 5）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **2** | `present`(#2)、`tbm_present$`(#2) |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `except`(#1)、`siz`(#1)、`or$country_code$`(#2) |

### SWE-PM-113 —— 行為項 3，已覆蓋 3，無對應 **0**

TC：221

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | For all screen sizes except 7 inch | 221 | 0.50 | 已覆蓋 | `except`、`siz` |
| 2 | If $VC_VEH_BRAND$ <> [Maserati] AND $TBM_Present$ = [Present] AND $Country_Cod | 221 | 1.00 | 已覆蓋 | （無） |
| 3 | See HMI for different statup conditions to determine when to add geolocation + | 221 | 0.50 | 已覆蓋 | `condition`、`determine`、`different`、`hmi`、`see`、`statup` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`AND`

**R-P127 殘差詞分桶**（合計 8）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **8** | `except`(#1)、`siz`(#1)、`condition`(#3)、`determine`(#3)、`different`(#3)、`hmi`(#3)、`see`(#3)、`statup`(#3) |

### SWE-PM-114 —— 行為項 1，已覆蓋 1，無對應 **0**

TC：222

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone cal | 222 | 0.86 | 已覆蓋 | `bypas`、`due` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN`

**R-P127 殘差詞分桶**（合計 2）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **2** | `bypas`(#1)、`due`(#1) |

### SWE-PM-115 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：223

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | IF the HU transitions from IDLE to FULL OPERATION due to an incoming phone cal | 223 | 0.82 | 已覆蓋 | `bypas`、`due` |
| 2 | THEN if the HU returns to IDLE when the phone call becomes inactive, the HU sh | 223 | 0.92 | 已覆蓋 | `show` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`IF`、`THEN`

**R-P127 殘差詞分桶**（合計 3）：

| 桶 | 計數 | 例（前 12）|
|---|---|---|
| 已由他條涵蓋 | **0** | （無） |
| 候選（須人工判 措詞差異 / 真缺口） | **3** | `bypas`(#1)、`due`(#1)、`show`(#2) |

**合計**：行為項 **60**，已覆蓋 **57**，無對應 **3**。
