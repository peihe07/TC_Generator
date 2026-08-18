# 上繳包 18 —— `source_clause` 保真度與第二批啟動

> 對應下放包：`features/power/docs/handoff/18_source_fidelity.md`
> 執行層：Claude（TC_Generator）
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；
> **未觸碰客戶樹與 `inputs/` 之原始檔**；**未指派最終 tc_id**；
> **未實作亦未建議 R-P116 之任一處置**；**未為求 G94 相符而擴大正規化**；
> **未為使 `remarks` 通過而放寬 §11**；**未自行改判 `SWE-PM-057` 之歸屬**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

**編號查核（§H 步驟 2，先查後開）**：
開新號前之現行最大號為 **A-PW88**、**R-P124**、**DR-PW8**、閘門 **G93**。
本包新號自 **A-PW89**、**R-P125**、**G94** 起，無衝突。**本包無新增 DR。**

---

## 一、B1 —— `016` / `017` 全文與其補寫依據（必附一，置於最前）

### 1.1 補寫依據

| 項 | 內容 |
|---|---|
| **觸發之殘差詞** | 透鏡 3 對 `4942354` 行為項 #2 / #11（`and if the volume was **greater**, send the AUD_LVL signal with the updated volume level`）列出殘差 `greater` |
| **透鏡 1 之判定** | overlap **0.86 —— 判「已覆蓋」**。若無透鏡 3，此分支不會被任何人問起 |
| **為何判為真缺口** | 原文之 `if the volume was greater` 為**條件**，其否定側（音量未超過上限）之可觀察結果不同：**不送 `AUD_LVL`**。15 條之起始音量皆為 25（> 20），**負分支從未被觸發** |
| **為何補二條而非四條** | `4942354` 於 **Load Shed** 與 **Battery Critical** 兩段各載一次該條件，二者為**不同觸發**（§5.7）故各補一條。未再依 mode（BODY ON / BODY OFF-TIMED）細分 —— 該條件之判準不隨 mode 改變，細分會產生同一失效模式之重複條目（§8.2.2）|
| **狀態** | 依 R-P126 **為暫定，待分析層覆核** |

### NR1L-PowerManagement-016 — SWE-PM-073（split_index 2）

**tc_id**：`NR1L-PowerManagement-016`

**req_id**：`SWE-PM-073`

**split_index**：`2`

**tc_title**：`Load Shed with volume already below the cap: no AUD_LVL update`

**test_set**：`Power Down`

**test_item**：`Load Shed with volume already below the cap: no AUD_LVL update`

**pre_conditions**

```
1. The bench is an Atlantis High configuration
2. A LIN and CAN simulation tool is connected
3. Ecall, ACN and chimes modes are inactive
```

**input_test_data**

```
STATUS_LIN.PN14_LS_Actv = [1h]
STATUS_LIN.PN14_LS_Lvl7 = [1h]
Starting volume level: 15
```

**test_procedure**

```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the two Load Shed signals listed in Input Test Data
3. Read the CAN trace and the volume level to check that AUD_LVL is not updated
```

**expected_result**

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts both Load Shed signals without a bus error
3. No AUD_LVL signal carrying a new volume level appears in the trace and the volume level is unchanged
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗音量未超過上限之負分支（Load Shed 側）：不送 AUD_LVL`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P118 反向涵蓋（17 包）**：`4942354` 兩處皆載「**and if the volume was greater**, send the AUD_LVL signal with the updated volume level」。15 條僅測「原音量大於 20」之正分支（`007` / `009` / `014` 之起始音量 25）；**未超過 20 之負分支未測**。透鏡 3 之殘差詞 `greater` 使該分支現形（透鏡 1 判該項 overlap 0.86 為已覆蓋）。依 R-P118(d) 裁為**真缺口**並補測。

**leaf `SWE-PM-073` 之 `source_clause`**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

### NR1L-PowerManagement-017 — SWE-PM-073（split_index 7）

**tc_id**：`NR1L-PowerManagement-017`

**req_id**：`SWE-PM-073`

**split_index**：`7`

**tc_title**：`Battery Critical with volume already below the cap: no AUD_LVL update`

**test_set**：`Power Down`

**test_item**：`Battery Critical with volume already below the cap: no AUD_LVL update`

**pre_conditions**

```
1. A LIN and CAN simulation tool is connected
2. The TLM is in BODY ON mode
3. Ecall, ACN and chimes modes are inactive
```

**input_test_data**

```
STATUS_LIN.Batt_ST_Crit = [1h]
Starting volume level: 15
```

**test_procedure**

```
1. Set the TLM volume level to the starting value listed in Input Test Data
2. Send the Battery Critical signal listed in Input Test Data
3. Read the CAN trace and the volume level to check that AUD_LVL is not updated
```

**expected_result**

```
1. The TLM volume indicator shows the starting level and the audio output is unmuted
2. The TLM accepts the Battery Critical signal without a bus error
3. No AUD_LVL signal carrying a new volume level appears in the trace and the volume level is unchanged
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_010_Power Down _SR26_20250909-1658_1.7.2`

**design_method**：`決策表 (Decision Table Testing)`

**priority**：`P2`

**split_flag**：`True`

**split_reason**：`本條驗音量未超過上限之負分支（Battery Critical 側）：不送 AUD_LVL`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P118 反向涵蓋（17 包）**：`4942354` 兩處皆載「**and if the volume was greater**, send the AUD_LVL signal with the updated volume level」。15 條僅測「原音量大於 20」之正分支（`007` / `009` / `014` 之起始音量 25）；**未超過 20 之負分支未測**。透鏡 3 之殘差詞 `greater` 使該分支現形（透鏡 1 判該項 overlap 0.86 為已覆蓋）。依 R-P118(d) 裁為**真缺口**並補測。

**leaf `SWE-PM-073` 之 `source_clause`**

```
When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals are received by the TLM,  the TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. ICS module shall power down. Under fault condition of missing load shed signals on the CAN bus, the last values of load shed signals shall be used until load shed signal broadcast resumes. If the load shed signals do not recover, the on-going load shed action shall be maintained for the rest of current ignition key cycle. The TLM shall transfer the call(not-Ecall/ACN call)  to the head set in case a continuing call is still active

While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_Crit=[1h], the TLM shall mimimize current withdraw while keeping only the display on and controls active for HVAC controls, and active phone for ACN. TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chimes/Beeps/Alerts  and if the volume was greater, send the AUD_LVL signal with the updated volume level. If Ecall/ACN/chimes mode is not active, TLM shall be muted. The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a continuing call is still active. Unless defined otherwise, TLM shall stay in this state until either voltage out of range conditions are satisfied  or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h].
```

---

## 二、G94 —— `source_clause` 保真度（必附二）

`features/power/scripts/verify_source_clause.py` → `data/g94_source_clause.md`

原文依 **R-P17 之文字層定義**抽取（`anchor_bodies()`）。
**正規化僅限 NBSP / thin space / 連續空白 —— 未擴大**（R-P125(a)）。

| leaf | anchor | 原文字元 | `source_clause` 字元 | 判定 |
|---|---|---|---|---|
| `SWE-PM-071` | `4942337` | 305 | 305 | **逐字相符** |
| `SWE-PM-072` | `4942338` | 304 | 304 | **逐字相符** |
| `SWE-PM-073` | `4942354` | 1563 | 1563 | **逐字相符** |
| `SWE-PM-057` | `4941692,4941693,4941695,4941706,4941707,4941708,4941814,4941815,4941817` | 1795 | 1795 | **逐字相符** |
| `SWE-PM-060` | `4941702` | 240 | 240 | **逐字相符** |
| `SWE-PM-061` | `4941703` | 63 | 63 | **逐字相符** |
| `SWE-PM-062` | `4941710` | 245 | 245 | **逐字相符** |
| `SWE-PM-063` | `4941715` | 187 | 187 | **逐字相符** |
| `SWE-PM-064` | `4941718` | 327 | 327 | **逐字相符** |
| `SWE-PM-065` | `4941720,4941721` | 397 | 397 | **逐字相符** |
| `SWE-PM-038` | `4941722,4941723,4941724,4941725,4941726,4941727,4941728,4941729,4941730,4941731,4941732,4941735,4941736` | 2376 | 2376 | **逐字相符** |

**11 / 11 逐字相符。**


### 2.1 刻意弄壞之 FAIL 證明（R-P125(d)）

| fixture | 期望 | 實測 |
|---|---|---|
| 原文逐字 | 相符 | **相符** |
| NBSP 與連續空白之差異 | 相符 | **相符** |
| **刻意刪去中段一句** | FAIL | **FAIL —— 逐字不符**，首異 offset 345，長度 1563 → 1534 |
| **截斷（取前半）** | FAIL | **FAIL —— 判為「截斷（R-P109 / R-P125(c)）」**，長度 1563 → 781 |
| **改一個字（`20` → `30`）** | FAIL | **FAIL —— 逐字不符**，首異 offset 162，長度不變 |

### 2.2 一項實作補述

第二批之 leaf **多錨點**（`SWE-PM-038` 13 個、`SWE-PM-057` 9 個），
首批之單錨點寫法不足以涵蓋。`source_anchor` 改以逗號分隔，原文依該序串接。
**若無此修改，第二批之 G94 會全數判「錨點原文為空」而 FAIL** ——
此為首批之單一資料形態掩蓋之限制，於第二批方顯現。

---

## 三、G95 / G96 之 fixture 證明（必附三）

### 3.1 G95 —— `structure_snapshot` 併入閘門（R-P130）

涵蓋目標分頁內之**五類**：合併儲存格、條件式格式、DV（含 x14）、欄寬、凍結窗格。

| 案例 | 期望 | 實測 | 判定 |
|---|---|---|---|
| 正常：dry-run 寫回後 | 五類皆相同 | 五類皆相同 | **PASS** |
| 刪去一個 `<mergeCell>`（`sheet1.xml`）| 偵出 | 偵出 `merges` | **PASS** |
| 改動 `<conditionalFormatting>` sqref（`sheet6.xml`）| 偵出 | 偵出 `cf` | **PASS** |
| 抹去一條 `<dataValidation>`（`sheet5.xml`）| 偵出 | 偵出 `dv` | **PASS** |
| 改動一個 `<col>` 寬度（`sheet1.xml`）| 偵出 | 偵出 `cols` | **PASS** |
| 改動 `<pane>` topLeftCell | 偵出 | **未實測** —— 本工作簿十個分頁**皆無 `<pane>` 元素** | **未實測（非 PASS）** |

> **一項作業瑕疵**：首次實作時五類之弄壞一律施於 `_target_sheet()`
> （首個含 DV 之分頁 = `sheet5`），而條件式格式與凍結窗格位於資料分頁 `sheet6`，
> 致該二案未觸發。**當時的輸出長得像「本閘攔不住 cf 與 pane」，那是我的 fixture 建構錯，不是閘門的弱點。**
> 已改為逐類尋找含該屬性之分頁；凍結窗格一類依 R-P119(c) 之標準標「未實測」而非 PASS（A-PW95）。

### 3.2 G96 —— `remarks` 入 `LONG_FIELDS`（R-P131）

| fixture | 期望 | 實測 |
|---|---|---|
| `remarks` 無句點、無方括號 | 0 項 | **0 項** |
| `remarks` 以句點結尾 | ≥ 1 項 | **1 項** |
| `remarks` 以方括號標 UI 標籤 | ≥ 1 項 | **1 項** |

`015` 之原 `remarks` 以句點結尾，補入後即觸發 —— **依明令改內容而非放寬規則**。
現值：`DR-PW8 (High) —— \`4942354\` 未載 voltage out of range 之電壓門檻值；本條在取得該門檻前不可實際執行`。
**A-PW88 之「判準空洞」自此解除。**

---

## 四、第二批 —— `Timeout Settings` 8 leaf / 26 條 TC（必附四）

### 4.1 概況（G97）

| 項目 | 實測 |
|---|---|
| leaf 數 | **8**（§E 定版值）|
| TC 數 | **26**（臨時 tc_id `018`–`043`）|
| `specification_reference` | **26 / 26 指向 CFTS009**（`R1LR_Atl-H_25PI3.5_…_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_{章節}`）|
| 章節 | 1.6.2.1.17 / 1.6.3.1 / 1.6.3.1.1 / 1.6.3.1.2 / 1.6.4.1 / 1.8.1.1.1 |
| G94 | **8 / 8 逐字相符** |
| lint | `exit=0`；阻斷類 **PASS**；待人工裁決類 **12 項**（見 §五之結構性回報）|

**（b）`SWE-PM-057` 之歸屬檢驗 —— R-P34 成立，無須停並上繳。**
其九個錨點原文**全部**述及 `SwitchOff_Timeout_Setting.Req` 與 `Timeout1`，
即 Timeout Settings 之核心對象。037 之 Requirement Title 為
`Proxi Parameter management`（名稱指向 Proxi），**而行為確屬 Timeout Settings** ——
與 R-P34 之裁定一致。**執行層未自行改判，亦無改判之必要。**

另記：`4941814` / `4941815` / `4941817`（§1.8.1.1.1）與
`4941692` / `4941693` / `4941695`（§1.6.2.1.17）**逐字相同**，
屬同一行為之重複登載，未另拆條。

### 4.2 取樣法（canon §1.2）

26 條逾十條，依 §1.2 **分層取樣**：
**每 leaf 取 `split_index` 最小之一條全文**（8 條）
＋ **`SWE-PM-038` 全部 11 條**（該 leaf 之 13 錨點為本批最複雜者，且含盲測命中之 `043`）
= **18 / 26 全文**。
未取樣之 8 條為 `019` `020` `022` `024` `026` `027` `030` `032` ——
皆為同 leaf 內之**平行變體**（PROXI 值 60/180、其餘 Radio 型別、否定分支、
`Auto_SwitchOn_Setting.Req` 之另二值、第二啟動條件、第二通話），
其結構與已取樣者相同，僅參數值或分支不同。

## leaf `SWE-PM-057`（本 leaf 共 3 條）

**`source_clause`（錨點 `4941692,4941693,4941695,4941706,4941707,4941708,4941814,4941815,4941817`，G94 逐字相符）**

```
IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "20 min" in TLM menu; so Timeout1 is equal to "00 min" OR "20 minutes" respectively.
IF "Switch_Off_Time" parameter  is set  to "60 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "60 min" in TLM menu; so Timeout1 is equal to "00 min" OR "60 minutes" respectively.
IF "Switch_Off_Time" parameter  is set  to "180 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "180 min" in TLM menu; so Timeout1 is equal to "00 min" OR "180 minutes" respectively.
For the case of LTM High Radio not present, the user can select SwitchOff_Timeout_Setting.Req value equal to "00 minutes" OR equal to the value specified by PROXI parameter "Switch_Off_Time". For case of LTM High Radio present, see Auto_SwitchOn_Setting.Req management section
Timeout1 parameter is equal to the value set by the user through SwitchOff_Timeout_Setting.Req.
So, user can set SwitchOff_Timeout_Setting.Req to "00 minutes" OR to "20 minutes" IF PROXI parameter "Switch_Off_Time" is equal to "20 minutes".
IF "Switch_Off_Time" parameter  is set  to "20 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "20 min" in TLM menu; so Timeout1 is equal to "00 min" OR "20 minutes" respectively.
IF "Switch_Off_Time" parameter  is set  to "60 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "60 min" in TLM menu; so Timeout1 is equal to "00 min" OR "60 minutes" respectively.
IF "Switch_Off_Time" parameter  is set  to "180 minutes"  then the user can select SwitchOff_Timeout_Setting.Req to "00 min" OR to "180 min" in TLM menu; so Timeout1 is equal to "00 min" OR "180 minutes" respectively.
```

**`reasoning`**

> 驗證目標：`Timeout1` 之可選值由 PROXI 參數 `Switch_Off_Time` 決定，使用者經 TLM menu 以 `SwitchOff_Timeout_Setting.Req` 於「00 min」與該 PROXI 值之間擇一。為什麼這樣切：三個 PROXI 值（20 / 60 / 180 分）為三組獨立之可選集合，依 §8.2.2 各拆一條；`4941814` / `4941815` / `4941817`（§1.8.1.1.1）與 `4941692` / `4941693` / `4941695`（§1.6.2.1.17）**逐字相同**，屬同一行為之重複登載，不另拆條。刻意略過：`4941706` 之「LTM High Radio present」分支明指另一節（Auto_SwitchOn_Setting.Req management），依 R-P42 不在本 leaf 之錨點範圍。　**R-P132(b) 歸屬檢驗（18 包）**：本 leaf 之九個錨點原文**全部**述及 `SwitchOff_Timeout_Setting.Req` 與 `Timeout1`，即 Timeout Settings 之核心對象；037 之 Requirement Title 雖為 `Proxi Parameter management`，其行為確屬 Timeout Settings。**R-P34 之歸屬經本批實際撰寫檢驗為正確，無須停並上繳。**

### NR1L-PowerManagement-018 — SWE-PM-057（split_index 1）

**tc_id**：`NR1L-PowerManagement-018`

**req_id**：`SWE-PM-057`

**split_index**：`1`

**tc_title**：`Timeout1 options follow PROXI "Switch_Off_Time" set to 20 minutes`

**test_set**：`Timeout Settings`

**test_item**：`Timeout1 options follow PROXI "Switch_Off_Time" set to 20 minutes`

**pre_conditions**

```
1. An LTM High Radio is absent from the bench configuration
2. The PROXI parameter "Switch_Off_Time" is at 20 minutes
3. The TLM is in Full-Operation status
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Open the timeout setting entry in the TLM menu
2. Read the selectable values offered for SwitchOff_Timeout_Setting.Req
3. Select each offered value in turn and read Timeout1 to check that it follows the selection
```

**expected_result**

```
1. The timeout setting entry is shown in the TLM menu
2. The offered values are "00 min" and "20 min" and no other value is offered
3. Timeout1 reads "00 min" after the first selection and "20 minutes" after the second
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.2.1.17; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.1; R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.8.1.1.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗 PROXI "Switch_Off_Time" = 20 分鐘時之可選集合與 Timeout1 結果`

**functional_safety**：`NA`

**remarks**：``

## leaf `SWE-PM-060`（本 leaf 共 2 條）

**`source_clause`（錨點 `4941702`，G94 逐字相符）**

```
For LTM/ETM, the user can set one parameter, by means of Auto_SwitchOn_Setting.Req. For other Radios the user can set two parameters, by means of SwitchOff_Timeout_Setting.Req and Auto_SwitchOn_Setting.Req signals, selectable from TLM menu.
```

**`reasoning`**

> 驗證目標：可設定之逾時參數數量隨 Radio 型別而異 —— LTM/ETM 一個、其餘兩個。為什麼這樣切：二型別為不同前提下之不同可觀察結果，依 §8.3 以 Radio 型別為軸拆為兩條。

### NR1L-PowerManagement-021 — SWE-PM-060（split_index 1）

**tc_id**：`NR1L-PowerManagement-021`

**req_id**：`SWE-PM-060`

**split_index**：`1`

**tc_title**：`LTM or ETM Radio offers one timeout parameter`

**test_set**：`Timeout Settings`

**test_item**：`LTM or ETM Radio offers one timeout parameter`

**pre_conditions**

```
1. An LTM Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Open the timeout setting entry in the TLM menu
2. Read the parameters offered for user selection to check that only one is present
```

**expected_result**

```
1. The timeout setting entry is shown in the TLM menu
2. Auto_SwitchOn_Setting.Req is the only parameter offered and SwitchOff_Timeout_Setting.Req is absent
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗 LTM/ETM 型別：僅一個可設定參數`

**functional_safety**：`NA`

**remarks**：``

## leaf `SWE-PM-061`（本 leaf 共 2 條）

**`source_clause`（錨點 `4941703`，G94 逐字相符）**

```
These settings could be only done in TLM Full-Operation Status.
```

**`reasoning`**

> 驗證目標：該等設定僅得於 TLM Full-Operation 狀態進行。為什麼這樣切：肯定分支（Full-Operation 可設定）與否定分支（非 Full-Operation 不可設定）為兩個獨立部分失效，依 §7 拆為兩條 —— 僅驗肯定側則「任何狀態皆可設定」之實作亦會通過。

### NR1L-PowerManagement-023 — SWE-PM-061（split_index 1）

**tc_id**：`NR1L-PowerManagement-023`

**req_id**：`SWE-PM-061`

**split_index**：`1`

**tc_title**：`Timeout settings are selectable in Full-Operation status`

**test_set**：`Timeout Settings`

**test_item**：`Timeout settings are selectable in Full-Operation status`

**pre_conditions**

```
1. The TLM is in Full-Operation status
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Open the timeout setting entry in the TLM menu
2. Change the offered timeout parameter and read it back to check that the change is accepted
```

**expected_result**

```
1. The timeout setting entry is shown and its controls are enabled
2. The parameter reads back the newly selected value
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗肯定分支：Full-Operation 下設定可用`

**functional_safety**：`NA`

**remarks**：``

## leaf `SWE-PM-062`（本 leaf 共 3 條）

**`source_clause`（錨點 `4941710`，G94 逐字相符）**

```
User can select Auto_SwitchOn_Setting.Req value equal to "Active" (If LTM High is present: "Timeout1" = "00 minutes");"Not_Active (If LTM High is present:"Timeout1" <> "00 minutes");"Recall_Last" (If LTM High is present:"Timeout1 = "00 minutes")
```

**`reasoning`**

> 驗證目標：`Auto_SwitchOn_Setting.Req` 之三個可選值及其於 LTM High 存在時對 `Timeout1` 之條件。為什麼這樣切：三值為三個獨立之使用者選擇與其後果，依 §8.2.2 各拆一條。

### NR1L-PowerManagement-025 — SWE-PM-062（split_index 1）

**tc_id**：`NR1L-PowerManagement-025`

**req_id**：`SWE-PM-062`

**split_index**：`1`

**tc_title**：`Auto_SwitchOn_Setting.Req can be set to Active`

**test_set**：`Timeout Settings`

**test_item**：`Auto_SwitchOn_Setting.Req can be set to Active`

**pre_conditions**

```
1. An LTM High Radio is present in the bench configuration
2. The TLM is in Full-Operation status
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Open the timeout setting entry in the TLM menu
2. Select "Active" for Auto_SwitchOn_Setting.Req
3. Read Auto_SwitchOn_Setting.Req and Timeout1 to check the stored selection
```

**expected_result**

```
1. The timeout setting entry is shown in the TLM menu
2. The TLM accepts the selection without reverting it
3. Auto_SwitchOn_Setting.Req reads "Active" and Timeout1 reads "00 minutes"
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.3.1.2`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗 Auto_SwitchOn_Setting.Req = "Active" 之選擇與其 Timeout1 條件`

**functional_safety**：`NA`

**remarks**：``

## leaf `SWE-PM-063`（本 leaf 共 1 條）

**`source_clause`（錨點 `4941715`，G94 逐字相符）**

```
In Timed state, it is possible either to make and to receive one or more bluetooth phone calls according to following logics that depend on Timeout1 and on MaxCallTimeout time parameters.
```

**`reasoning`**

> 驗證目標：Timed 狀態下得撥出與接聽藍牙通話。為什麼這樣切：本錨點為概括陳述，其細部邏輯由 `SWE-PM-064` / `065` / `038` 之錨點承載；本條僅驗「Timed 狀態下通話功能可用」此一可觀察事實，不重複測其後續轉換。

### NR1L-PowerManagement-028 — SWE-PM-063（split_index 1）

**tc_id**：`NR1L-PowerManagement-028`

**req_id**：`SWE-PM-063`

**split_index**：`1`

**tc_title**：`Bluetooth calls can be made and received in Timed state`

**test_set**：`Timeout Settings`

**test_item**：`Bluetooth calls can be made and received in Timed state`

**pre_conditions**

```
1. A paired bluetooth phone is available on the bench
2. The TLM is in Timed state
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Place an outgoing bluetooth call from the paired phone through the TLM
2. End that call and receive an incoming bluetooth call
3. Read the call audio routing and the TLM state to check that both calls were served
```

**expected_result**

```
1. The outgoing call is connected and its audio is routed through the TLM
2. The incoming call is presented and can be answered
3. Both calls were served and the TLM remains in Timed state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗 Timed 狀態下通話功能可用（概括陳述之可觀察面）`

**functional_safety**：`NA`

**remarks**：``

## leaf `SWE-PM-064`（本 leaf 共 2 條）

**`source_clause`（錨點 `4941718`，G94 逐字相符）**

```
MaxCallTimeout starts in the following two conditions: Timeout1 == 00 min: IF Phone_Call.Info is equal to “Active” in TLM Full-Operation state, AND the Ignition working condition switches to "Ignition Pre Off" OR to "Ignition Off";   Timeout1 <> 00 min: at Timeout1 expiration, only IF Phone_Call.Info is still equal to “Active”;
```

**`reasoning`**

> 驗證目標：`MaxCallTimeout` 之兩個啟動條件。為什麼這樣切：二條件之觸發前提不同（`Timeout1 == 00 min` 之點火轉換 vs `Timeout1 <> 00 min` 之 Timeout1 到期），依 §5.7 不同觸發即拆分。

### NR1L-PowerManagement-029 — SWE-PM-064（split_index 1）

**tc_id**：`NR1L-PowerManagement-029`

**req_id**：`SWE-PM-064`

**split_index**：`1`

**tc_title**：`MaxCallTimeout starts on ignition off with Timeout1 at 00 min`

**test_set**：`Timeout Settings`

**test_item**：`MaxCallTimeout starts on ignition off with Timeout1 at 00 min`

**pre_conditions**

```
1. Timeout1 is at "00 min"
2. The TLM is in Full-Operation state
3. Phone_Call.Info is at "Active"
```

**input_test_data**

```
Ignition working condition: "Ignition Pre Off"
```

**test_procedure**

```
1. Switch the ignition working condition to the value listed in Input Test Data
2. Read the MaxCallTimeout counter to check that it started
```

**expected_result**

```
1. The TLM leaves Full-Operation state without dropping the active call
2. The MaxCallTimeout counter is running from the moment of the ignition change
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗啟動條件一：Timeout1 == 00 min 且點火轉為 Pre Off 或 Off`

**functional_safety**：`NA`

**remarks**：``

## leaf `SWE-PM-065`（本 leaf 共 2 條）

**`source_clause`（錨點 `4941720,4941721`，G94 逐字相符）**

```
Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN TLM has to restore the active source managed by TLM before the call (for example entertainment features like DAB Tuner, rather than USB or BT streaming audio) staying still in Timed state.
In this case, TLM is still able to manage other possible phone calls within Timeout1 expiration.
```

**`reasoning`**

> 驗證目標：Case 1 —— `Timeout1 <> 00 min` 且通話於 Timeout1 到期前結束時，還原通話前之音源並續留 Timed。為什麼這樣切：還原音源（`4941720`）與 Timeout1 到期前仍可處理其他通話（`4941721`）為兩個獨立部分失效，依 §8.2.2 拆為兩條。

### NR1L-PowerManagement-031 — SWE-PM-065（split_index 1）

**tc_id**：`NR1L-PowerManagement-031`

**req_id**：`SWE-PM-065`

**split_index**：`1`

**tc_title**：`Call ends before Timeout1 expiry: previous source is restored`

**test_set**：`Timeout Settings`

**test_item**：`Call ends before Timeout1 expiry: previous source is restored`

**pre_conditions**

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. A DAB Tuner source was active before the call
4. Phone_Call.Info is at "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Set Phone_Call.Info to "Not_Active" before Timeout1 expires
2. Read the active audio source and the TLM state to check that the previous source returned
```

**expected_result**

```
1. The call is released and its audio is removed from the TLM output
2. The DAB Tuner source is active again and the TLM remains in Timed state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P1`

**split_flag**：`True`

**split_reason**：`本條驗還原音源分支`

**functional_safety**：`NA`

**remarks**：``

## leaf `SWE-PM-038`（本 leaf 共 11 條）

**`source_clause`（錨點 `4941722,4941723,4941724,4941725,4941726,4941727,4941728,4941729,4941730,4941731,4941732,4941735,4941736`，G94 逐字相符）**

```
Case 1:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info passes to "Not_Active" before "Timeout1” expiration THEN
IF RemStartFail = ”True” TLM has to stop its active functionality (Media audio streaming, tuner, etc) and has to set RemStartFail  to “False” value and  TLM_Status.Info and $Telematic_Power$ to “Standby” value and it passes to Standby state
ELSE TLM has to restore the active source managed by TLM before the call (for example entertainment features like DAB Tuner, rather than USB or BT streaming audio) staying still in Timed state.
In this case, TLM is still able to manage other possible phone calls within Timeout1 expiration.
Case 2:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info is still "Active" at "Timeout1" expirationTHENat Timeout1 expiration TLM starts MaxCallTimeout AND stays still in Timed state until Phone_Call.Info passes to "Not_Active" OR at maximum until MaxCallTimeout expiration.
WHEN Phone_Call.Info passes to "Not_Active", OR at MaxCallTimeout expiration, TLM sets TLM_Status.Info to "Standby" value and then it passes to Standby state.
WHEN Phone_Call.Info passes to "Not_Active", OR at MaxCallTimeout expiration, TLM has to set RemStartFail  to “False” value and TLM_Status.Info to "Standby" value and then it passes to Standby state.
Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Timeout1 expiration THENTLM has to set TLM_Status.Info to “Standby” value and to pass to Standby state.
Case 3:IF Timeout1 <> 00 minutesAND IF Phone_Call.Info == "Not_Active" at Timeout1 expiration THENTLM has to set RemStartFail to "False" value and TLM_Status.Info to “Standby” value and to pass to Standby state.
Case 4:IF Timeout1 == 00 minutesAND in Full-Operation state Phone_Call.Info signal is equal to "Active" AND the ignition working condition passes to "Ignition Pre Off" OR to "Ignition Off"THENTLM has to pass in Timed state starting MaxCallTimeout counter.
In this case, TLM has to manage the phone call(s) and to stay in Timed state until Phone_Call.Info passes to "Not_Active" value OR at maximum until MaxCallTimeout expires.
IF any of the previous condition occurs, THEN TLM has to set TLM_Status.Info to “Standby” value and to pass to Standby state.
IF any of the previous condition occurs, THEN TLM has to set RemStartFail to “False” value  and  TLM_Status.Info to “Standby” value and to pass to Standby state.
```

**`reasoning`**

> 驗證目標：Standby 與 Timed 狀態下之通話管理四個 Case 及其 `RemStartFail` 變體。為什麼這樣切：Case 1–4 為四個互斥之進入條件（§5.7 不同觸發即拆分）；各 Case 之離開路徑（通話結束 vs `MaxCallTimeout` 到期）與 `RemStartFail` 之處置為獨立部分失效，依 §8.2.2 再拆。`4941727` / `4941728`、`4941729` / `4941730`、`4941735` / `4941736` 三組各為「不含 / 含 `RemStartFail` 處置」之成對錨點，各自成條。刻意略過：`$Telematic_Power$` 之訊號定義未見於本 leaf 之錨點，依 §8.4.1 不造值，ER 僅述其被設為「Standby」。

### NR1L-PowerManagement-033 — SWE-PM-038（split_index 1）

**tc_id**：`NR1L-PowerManagement-033`

**req_id**：`SWE-PM-038`

**split_index**：`1`

**tc_title**：`Case 1 with RemStartFail true: TLM stops and passes to Standby`

**test_set**：`Timeout Settings`

**test_item**：`Case 1 with RemStartFail true: TLM stops and passes to Standby`

**pre_conditions**

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state with media audio streaming active
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Set Phone_Call.Info to "Not_Active" before Timeout1 expires
2. Read the active functionality, RemStartFail, TLM_Status.Info and $Telematic_Power$ to check the transition
```

**expected_result**

```
1. The media audio streaming stops and no source stays active
2. RemStartFail reads "False", TLM_Status.Info and $Telematic_Power$ read "Standby" and the TLM is in Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 1 之 RemStartFail 為 True 之分支`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-034 — SWE-PM-038（split_index 2）

**tc_id**：`NR1L-PowerManagement-034`

**req_id**：`SWE-PM-038`

**split_index**：`2`

**tc_title**：`Case 1 with RemStartFail false: previous source is restored`

**test_set**：`Timeout Settings`

**test_item**：`Case 1 with RemStartFail false: previous source is restored`

**pre_conditions**

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. RemStartFail is at "False"
4. A DAB Tuner source was active before the call
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Set Phone_Call.Info to "Not_Active" before Timeout1 expires
2. Place a further bluetooth call while Timeout1 is still running
3. Read the active source and the TLM state to check the restore and the further call
```

**expected_result**

```
1. The DAB Tuner source is active again and the TLM remains in Timed state
2. The further call is connected and its audio is routed through the TLM
3. The TLM stayed in Timed state throughout and no transition to Standby occurred
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 1 之 ELSE 分支：還原音源並續管理其他通話`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-035 — SWE-PM-038（split_index 3）

**tc_id**：`NR1L-PowerManagement-035`

**req_id**：`SWE-PM-038`

**split_index**：`3`

**tc_title**：`Case 2: MaxCallTimeout starts at Timeout1 expiry and the TLM stays Timed`

**test_set**：`Timeout Settings`

**test_item**：`Case 2: MaxCallTimeout starts at Timeout1 expiry and the TLM stays Timed`

**pre_conditions**

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. Phone_Call.Info is at "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let Timeout1 run to its expiration while the call stays active
2. Read the MaxCallTimeout counter and the TLM state to check that the TLM stays Timed
```

**expected_result**

```
1. Phone_Call.Info is still at "Active" when Timeout1 expires and the MaxCallTimeout counter starts
2. The TLM remains in Timed state while MaxCallTimeout runs
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 2 之進入：Timeout1 到期啟動 MaxCallTimeout 並續留 Timed`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-036 — SWE-PM-038（split_index 4）

**tc_id**：`NR1L-PowerManagement-036`

**req_id**：`SWE-PM-038`

**split_index**：`4`

**tc_title**：`Case 2 exit on call end: TLM_Status.Info passes to Standby`

**test_set**：`Timeout Settings`

**test_item**：`Case 2 exit on call end: TLM_Status.Info passes to Standby`

**pre_conditions**

```
1. The TLM is in Timed state with MaxCallTimeout running
2. Phone_Call.Info is at "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Set Phone_Call.Info to "Not_Active" before MaxCallTimeout expires
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```

**expected_result**

```
1. The call is released and its audio is removed from the TLM output
2. TLM_Status.Info reads "Standby" and the TLM is in Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 2 之離開路徑：通話結束（不含 RemStartFail 處置）`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-037 — SWE-PM-038（split_index 5）

**tc_id**：`NR1L-PowerManagement-037`

**req_id**：`SWE-PM-038`

**split_index**：`5`

**tc_title**：`Case 2 exit with RemStartFail cleared on MaxCallTimeout expiry`

**test_set**：`Timeout Settings`

**test_item**：`Case 2 exit with RemStartFail cleared on MaxCallTimeout expiry`

**pre_conditions**

```
1. The TLM is in Timed state with MaxCallTimeout running
2. RemStartFail is at "True"
3. Phone_Call.Info is at "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let MaxCallTimeout run to its expiration while the call stays active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```

**expected_result**

```
1. The call is released at MaxCallTimeout expiration
2. RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 2 之離開路徑：MaxCallTimeout 到期（含 RemStartFail 處置）`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-038 — SWE-PM-038（split_index 6）

**tc_id**：`NR1L-PowerManagement-038`

**req_id**：`SWE-PM-038`

**split_index**：`6`

**tc_title**：`Case 3: call already ended at Timeout1 expiry`

**test_set**：`Timeout Settings`

**test_item**：`Case 3: call already ended at Timeout1 expiry`

**pre_conditions**

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. Phone_Call.Info is at "Not_Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let Timeout1 run to its expiration with no call active
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```

**expected_result**

```
1. No call is active when Timeout1 expires and MaxCallTimeout does not start
2. TLM_Status.Info reads "Standby" and the TLM is in Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 3（不含 RemStartFail 處置）`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-039 — SWE-PM-038（split_index 7）

**tc_id**：`NR1L-PowerManagement-039`

**req_id**：`SWE-PM-038`

**split_index**：`7`

**tc_title**：`Case 3 with RemStartFail cleared at Timeout1 expiry`

**test_set**：`Timeout Settings`

**test_item**：`Case 3 with RemStartFail cleared at Timeout1 expiry`

**pre_conditions**

```
1. Timeout1 is at a value other than "00 min"
2. The TLM is in Timed state
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Not_Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let Timeout1 run to its expiration with no call active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```

**expected_result**

```
1. No call is active when Timeout1 expires and MaxCallTimeout does not start
2. RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 3（含 RemStartFail 處置）`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-040 — SWE-PM-038（split_index 8）

**tc_id**：`NR1L-PowerManagement-040`

**req_id**：`SWE-PM-038`

**split_index**：`8`

**tc_title**：`Case 4: ignition off with Timeout1 at 00 min enters Timed state`

**test_set**：`Timeout Settings`

**test_item**：`Case 4: ignition off with Timeout1 at 00 min enters Timed state`

**pre_conditions**

```
1. Timeout1 is at "00 min"
2. The TLM is in Full-Operation state
3. Phone_Call.Info is at "Active"
```

**input_test_data**

```
Ignition working condition: "Ignition Off"
```

**test_procedure**

```
1. Keep the call active and switch the ignition working condition to the value listed in Input Test Data
2. Read the TLM state and the MaxCallTimeout counter to check that Timed state is entered
```

**expected_result**

```
1. The active call is not dropped by the ignition change
2. The TLM is in Timed state and the MaxCallTimeout counter is running
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 4 之進入：Timeout1 == 00 min 且點火轉為 Off`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-041 — SWE-PM-038（split_index 9）

**tc_id**：`NR1L-PowerManagement-041`

**req_id**：`SWE-PM-038`

**split_index**：`9`

**tc_title**：`Case 4 exit: TLM passes to Standby when the call ends`

**test_set**：`Timeout Settings`

**test_item**：`Case 4 exit: TLM passes to Standby when the call ends`

**pre_conditions**

```
1. The TLM is in Timed state entered through Case 4
2. MaxCallTimeout is running
3. Phone_Call.Info is at "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Set Phone_Call.Info to "Not_Active" before MaxCallTimeout expires
2. Read TLM_Status.Info and the TLM state to check the transition to Standby
```

**expected_result**

```
1. The TLM stayed in Timed state for the whole time the call was active
2. TLM_Status.Info reads "Standby" and the TLM is in Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 4 之離開路徑（`4941732` ＋ `4941735`，不含 RemStartFail 處置）`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-042 — SWE-PM-038（split_index 10）

**tc_id**：`NR1L-PowerManagement-042`

**req_id**：`SWE-PM-038`

**split_index**：`10`

**tc_title**：`Case 4 exit with RemStartFail cleared on MaxCallTimeout expiry`

**test_set**：`Timeout Settings`

**test_item**：`Case 4 exit with RemStartFail cleared on MaxCallTimeout expiry`

**pre_conditions**

```
1. The TLM is in Timed state entered through Case 4
2. MaxCallTimeout is running
3. RemStartFail is at "True"
4. Phone_Call.Info is at "Active"
```

**input_test_data**

```
NA
```

**test_procedure**

```
1. Let MaxCallTimeout run to its expiration while the call stays active
2. Read RemStartFail, TLM_Status.Info and the TLM state to check the transition to Standby
```

**expected_result**

```
1. The TLM stayed in Timed state until MaxCallTimeout expired
2. RemStartFail reads "False", TLM_Status.Info reads "Standby" and the TLM is in Standby state
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 4 之離開路徑（`4941736`，含 RemStartFail 處置）`

**functional_safety**：`NA`

**remarks**：``

### NR1L-PowerManagement-043 — SWE-PM-038（split_index 11）

**tc_id**：`NR1L-PowerManagement-043`

**req_id**：`SWE-PM-038`

**split_index**：`11`

**tc_title**：`Case 4 with ignition pre off: TLM enters Timed state`

**test_set**：`Timeout Settings`

**test_item**：`Case 4 with ignition pre off: TLM enters Timed state`

**pre_conditions**

```
1. Timeout1 is at "00 min"
2. The TLM is in Full-Operation state
3. Phone_Call.Info is at "Active"
```

**input_test_data**

```
Ignition working condition: "Ignition Pre Off"
```

**test_procedure**

```
1. Keep the call active and switch the ignition working condition to the value listed in Input Test Data
2. Read the TLM state and the MaxCallTimeout counter to check that Timed state is entered
```

**expected_result**

```
1. The active call is not dropped by the ignition change
2. The TLM is in Timed state and the MaxCallTimeout counter is running
```

**specification_reference**：`R1LR_Atl-H_25PI3.5_Activation and Configuration_CFTS_009_Wake-up and Power-up_SR26_20250909-1658_1.6.4.1`

**design_method**：`狀態轉換 (State Transition Testing)`

**priority**：`P0`

**split_flag**：`True`

**split_reason**：`本條驗 Case 4 之另一觸發：點火轉為 "Ignition Pre Off"（`040` 驗 "Ignition Off"）`

**functional_safety**：`NA`

**remarks**：``

**reasoning_note**

> **R-P118 反向涵蓋盲測（18 包）**：`4941731` 載 Case 4 之觸發為 「the ignition working condition passes to "Ignition Pre Off" **OR** to "Ignition Off"」。首次撰寫時 `040` 僅取 "Ignition Off"，**"Ignition Pre Off" 之分支漏測**。透鏡 1 對該行為項判 overlap 0.62 為已覆蓋；**是透鏡 3 之殘差詞 `pre` 使其現形**。依 §5.7「不同觸發即拆分」與 R-P118(d) 裁為**真缺口**並補本條。**本項為 R-P128 之盲測結果：事前未知，由工具抓出。**

---

## 五、第二批反向涵蓋（必附五）

`data/reverse_coverage_002-timeout-settings.md`

### 5.1 透鏡 1 / 2

| leaf | 行為項 | 已覆蓋 | 無對應 |
|---|---|---|---|
| `SWE-PM-057` | 15 | 15 | **0** |
| `SWE-PM-060` | 2 | 2 | **0** |
| `SWE-PM-061` | 1 | 1 | **0** |
| `SWE-PM-062` | 1 | 1 | **0** |
| `SWE-PM-063` | 1 | 0 | **1** |
| `SWE-PM-064` | 2 | 2 | **0** |
| `SWE-PM-065` | 2 | 1 | **1** |
| `SWE-PM-038` | 15 | 15 | **0** |
| **合計** | **39** | **37** | **2** |

兩項「無對應」之裁決（R-P118(d) 三選一）：

| leaf | 行為項 | 裁決 | 依據 |
|---|---|---|---|
| `SWE-PM-063` #1（overlap 0.32）| `In Timed state, it is possible either to make and to receive one or more bluetooth phone calls according to following logics that depend on Timeout1 and on MaxCallTimeout time parameters` | **已由他條涵蓋（跨 leaf）** | 「可撥可接」由 `028` 覆蓋；「following logics that depend on Timeout1 and MaxCallTimeout」之細部邏輯**由 `SWE-PM-064` / `065` / `038` 之錨點承載**，各自已有 TC。**反向涵蓋逐 leaf 比對，故跨 leaf 之涵蓋顯示為無對應**（A-PW93）|
| `SWE-PM-065` #2（overlap 0.36）| `In this case, TLM is still able to manage other possible phone calls within Timeout1 expiration` | **已由他條涵蓋** | `032`（`Further calls are still managed within Timeout1`）即為本項。overlap 低係措詞差異（`manage other possible phone calls` vs `place a second bluetooth call`），非缺口 |

### 5.2 R-P127 —— 殘差詞分桶與信噪比

| 桶 | 計數 | 說明 |
|---|---|---|
| `已由他條涵蓋`（機械可判：該詞見於同 leaf 之他條 TC）| **20** | 例：`SWE-PM-038` 之 `expiration`、`maxcalltimeout` |
| `候選（須人工判）` | **125** | 由執行層逐一判別，見下 |
| **殘差詞合計** | **145** | |

125 個候選之人工判別結果：

| 判別 | 計數 | 例示 |
|---|---|---|
| `措詞差異`（同義／時態／功能詞）| **123** | `equal`、`respectively`、`user`、`could`、`done`、`only`、`these`、`thi`、`pas`、`minutesand`、`thentlm`、`expirationthenat` —— 其中多項為 CFTS 原文之**排版黏連**（`minutesAND`、`THENTLM`）而非語義 |
| `已由他 leaf 涵蓋` | **1** | `SWE-PM-057` #8 之 `Auto_SwitchOn_Setting.Req` / `section` —— `4941706` 之「LTM High Radio present」分支明指另一節，**依 R-P42 不在本 leaf 範圍**，已於 `reasoning` 明載 |
| **`真缺口`** | **1** | **`SWE-PM-038` #10 之殘差 `pre`** —— 見 §5.3 |

> **信噪比 ＝ 真缺口 1 / 殘差詞 145 ≒ 0.7%。**
>
> 執行層之判讀：**產出量大而命中率極低**。
> 惟其所命中之一項，**透鏡 1 判其 overlap 0.62 為「已覆蓋」** ——
> 即該透鏡是唯一抓到它的機制。堪用與否，執行層不代分析層裁定。
> 另記：123 個 `措詞差異` 中有相當比例源自 CFTS 原文之**排版黏連**
> （`00 minutesAND`、`expirationTHENat`），此為抽取層之既有事實，非 TC 之問題。

### 5.3 R-P128 —— 盲測結果

**第二批之 26 條係逐 leaf 依錨點原文直接撰寫，撰寫時未跑反向涵蓋**；
撰寫完成後方執行工具。故其所指者皆為**事前未知**。

> **事前未知之缺口：1 項。**

`4941731`（Case 4）之觸發原文為
「the ignition working condition passes to **"Ignition Pre Off" OR to "Ignition Off"**」，
而首次撰寫之 `040` **僅取 "Ignition Off"**。
**透鏡 1 判該行為項 overlap 0.62 為「已覆蓋」；是透鏡 3 之殘差詞 `pre` 使其現形。**
依 §5.7（不同觸發即拆分）與 R-P118(d) 裁為**真缺口**，補 `043`（TC 25 → 26）。

**與既有兩例同型** —— A-PW87（`greater` 之負分支）、R-P117(c)（`BODY OFF-TIMED`）：
**三者皆為「原文以 OR 並列而 TC 只取其一」**，且**三者透鏡 1 皆判已覆蓋**。

**執行層之限度聲明**：本次盲測只證明「透鏡 3 至少抓到一項人漏掉的」，
**不證明它抓到了全部**。第二批仍可能有既未被人讀出、亦未被工具列出之缺口。

### 5.4 一項結構性回報 —— G77 與 G73 之張力（A-PW92）

第二批 26 條中 **12 條**觸發 R-P96(a)（待人工裁決類），**全為訊號／參數之狀態回讀**
（`TLM_Status.Info reads "Standby" and the TLM is in Standby state` 之形態）。

原因**不是任一閘門有瑕疵，而是兩條裁決彼此拉扯**：
R-P101 要求末步指名所檢查者（`Read TLM_Status.Info … to check the transition to Standby`），
而 ER 述及同一標的時，其實詞多已見於該步驟，**必然抬高 G73 tier1 之 overlap**
（其中三條達 **1.00**）。

**執行層之處置**：依 R-P76 之分流全數列為待人工裁決，
並逐項判為**偽陽性** —— 狀態回讀屬 §6 之 prove condition established，
與 A-PW62 所載之已交付慣例（`Turn Sync on` → `Sync is on`）同型。
**未改動任一閘門，亦未為降低觸發數而改寫 ER。**
是否調整判準或改列例外，屬分析層。

---

## 六、§D 全表自驗（必附六）

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G94** | `source_clause` 保真度 | 三 leaf 逐字相符；刻意刪句 → FAIL | **11 / 11 逐字相符**（首批 3 ＋ 第二批 8）；fixture 五案如期 | **PASS** | **合成＋真實** |
| **G95** | `structure_snapshot` 閘門 | 五類皆納入；刻意改動 → FAIL | 五類皆納入；**四類已證可失敗，凍結窗格一類未實測**（本簿無 `<pane>`）| **PASS（4/5），1 類未實測** | **合成＋真實** |
| **G96** | `remarks` 入 `LONG_FIELDS` | `015` 通過 §11 全部規則 | 通過；fixture 三案如期；**內容已改而規則未放寬** | **PASS** | **合成＋真實** |
| **G97** | 第二批產出 | 8 leaf；`spec_reference` 全部指向 CFTS009 | **8 leaf、26 條 TC**；`spec_reference` **26 / 26 指向 CFTS009** | **PASS** | 真實 |
| **G98** | 第二批反向涵蓋 | 行為項／已覆蓋／無對應；三桶計數與信噪比；事前未知之缺口數 | 行為項 **39**、已覆蓋 **37**、無對應 **2**（皆裁為已由他條／他 leaf 涵蓋）；殘差 **145**，真缺口 **1**，**信噪比 0.7%**；**事前未知之缺口 1 項** | **PASS** | **真實（盲測）** |
| **G70** | lint 全閘 | 全 PASS；leaf 3 → 11；TC 17 → N | `exit=0`；阻斷類 PASS；leaf **11**；TC **43**；待裁類 12 項（A-PW92）| **PASS** | 真實 |
| G85 | 排序腳本 | 沿用 | 五案如期；43 列對照表已產（**未指派**）| **PASS** | 合成 |
| G1–G93 | 沿用 | 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期** | **PASS** | 混合 |

---

## 七、必附七 —— 執行層對「本包是否仍有該驗而未驗者」之獨立判斷

17 §七之八項已由 R-P125 ~ R-P131 分派，本節**不覆述**。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 六項**

1. **第二批之 26 條 TC 全數出自我一人，且無任何一條經他人讀過。**
   首批之品質是靠分析層讀了十七條、發現三輪缺陷才逐步得到的。
   第二批目前只跑過閘門與工具 —— **閘門全綠，而首批的三次教訓都證明閘門全綠不代表什麼。**
   分層取樣（18 / 26）是依 §1.2，但那也意味著**有 8 條連上繳包都沒出現全文**。

2. **`SWE-PM-038` 之 13 個錨點我拆成 11 條，這個拆法沒有第二人看過。**
   `4941727`/`4941728`、`4941729`/`4941730`、`4941735`/`4941736` 三組
   各為「不含／含 `RemStartFail` 處置」之成對錨點，我各自成條。
   **若這三組其實是同一行為在不同車型變體下的登載，那就是三條多餘的 TC。**
   規格原文沒有說明它們為何成對出現，我也沒有可查之處。

3. **`SWE-PM-063` 我只寫了一條，理由是「其細部邏輯由他 leaf 承載」。**
   這個判斷讓反向涵蓋的「無對應」變成「已由他 leaf 涵蓋」，
   **但那是我自己下的定義**。若分析層認為該 leaf 應自行涵蓋其所引之邏輯，
   則 `028` 一條明顯不足。

4. **信噪比 0.7% 這個數字，我是用「我判它是措詞差異」算出來的。**
   125 個候選裡有 123 個是我判為無妨的。
   **若其中還有一個像 `pre` 那樣的，我現在不會知道。**
   分桶降低了回報成本，但沒有降低誤判風險 —— 判別者仍是同一個人。

5. **`4941814` / `4941815` / `4941817` 與 `4941692` / `4941693` / `4941695` 逐字相同，
   我判為「重複登載」而未另拆條。**
   它們分屬 §1.8.1.1.1 與 §1.6.2.1.17 兩個不同章節。
   **同樣的文字出現在兩個章節，可能是重複，也可能是兩處各有其上下文。**
   我選了前者，沒有證據。

6. **G95 之凍結窗格一類永遠測不到 —— 除非換一個有 `<pane>` 的工作簿。**
   我標了「未實測」，但這意味著該類別在本 feature 的整個生命週期內
   **都不會有證據**。若日後客戶的範本加了凍結窗格，該閘的這一支仍是未驗狀態。

**（乙）已驗而應標明其強度不足者 —— 二項**

7. **G94 的「11 / 11 逐字相符」證明的是「抄對了」，不是「抄全了該抄的」。**
   它比對的是 `source_clause` 與**我所填的 `source_anchor`**。
   **若某個該被引用的錨點根本沒被列進 `source_anchor`，G94 一樣會全綠。**
   錨點清單本身的完整性來自 layer3（`item_ids` 欄），
   而 layer3 的正確性是 03–06 包驗的，**不是本閘驗的**。

8. **第二批的盲測只有一次，樣本是 8 個 leaf。**
   「透鏡 3 抓到 1 項」與「透鏡 3 有用」之間還有很長的距離。

**（丙）本包自身之作業瑕疵 —— 一項**

9. **G95 的 fixture 我一開始把五類的弄壞全施在同一個分頁上**，
   而 cf 與 pane 不在那個分頁，導致輸出長得像「本閘攔不住這兩類」。
   我沒有據此下結論，而是去查為什麼 —— 但**如果我當時直接照著輸出寫上繳包，
   就會報出一個假的閘門弱點。**已於 §三之 3.1 與 A-PW95 記明。

---

## 八、DATA_REQUESTS

DR-PW1（High）、DR-PW5（High）、DR-PW8（High）、
DR-PW3（Medium）、DR-PW6（Medium）、DR-PW7（Low）維持 live；
DR-PW2、DR-PW4 維持撤回。**本包無新增** ——
第二批之唯一真缺口（`Ignition Pre Off`）已由 `043` 補測，不需外部資料。

---

## 九、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/generated/batch_002_timeout_settings.json` | **第二批 8 leaf / 26 條 TC（新增）** |
| `features/power/scripts/verify_source_clause.py` | G94（新增，含 self-test）|
| `features/power/data/g94_source_clause.md` | G94 報告（新增）|
| `features/power/data/reverse_coverage_002-timeout-settings.md` | 第二批反向涵蓋（新增）|
| `features/power/data/reverse_coverage_001-power-down.md` | 首批（更名，原 `reverse_coverage_batch1.md`）|
| `features/power/scripts/reverse_coverage.py` | 多批次輸出命名、R-P127 分桶（改）|
| `features/power/scripts/verify_writeback_path.py` | G95（改）|
| `features/power/scripts/lint_tcs.py` | `remarks` 入 `LONG_FIELDS`、G96 fixture（改）|
| `features/power/generated/batch_001_power_down.json` | `015` 之 `remarks` 依 §11 改寫（改）|
| `features/power/data/final_tc_id_map.tsv` | 43 列對照表預覽（改，**未指派**）|
| `features/power/RULINGS.md` | R-P125 ~ R-P132（改）|
| `features/power/ANOMALIES.md` | A-PW89 ~ A-PW95、A-PW88 更新（改）|
| `features/power/docs/handoff/18_source_fidelity.md` | 下放包逐字落檔（新增）|
| `features/power/docs/upstream/18_source_fidelity.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 18 輪索引（改）|
