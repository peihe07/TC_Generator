# 上繳包 17 —— 反向涵蓋、寫回路徑閘門與第二批前置

> 對應下放包：`features/power/docs/handoff/17_reverse_coverage.md`
> 執行層：Claude（TC_Generator）
> 本包**未執行任何 git 操作**；**未對任何 workbook 呼叫 `save()`**；
> **未觸碰客戶樹與 `inputs/` 之原始檔**（SHA256 前後相同）；
> **未指派最終 tc_id**；**未實作亦未建議 R-P116 之任一處置**；
> **未開始第二批**；**未為求結果好看而調整拆句規則或門檻**。

**G0 前置閘：7 / 7 素材 SHA256 相符 —— PASS。**

**B6 編號查核（§H 步驟 2，先查後開）**：
開新號前之現行最大號為 **A-PW79**、**R-P117**、**DR-PW7**。
本包新號自 **A-PW80**、**R-P118**、**DR-PW8** 起，無衝突。

---

## 一、B1 反向涵蓋報告與其驗證條件（必附一）

`features/power/scripts/reverse_coverage.py` →
`features/power/data/reverse_coverage_batch1.md`。

### 1.1 驗證條件 —— **透鏡 1 單獨只重現三項已知缺口中之一項**

下放包之驗證條件為「對修補前之資料須能重現 R-P117 之三項缺口」。
以 `b1_before16.json`（十條，缺口尚存）實測：

| R-P117 之缺口 | 透鏡 1（行為項 overlap）| 透鏡 2（具名標的）| 透鏡 3（逐項殘差詞）|
|---|---|---|---|
| (a) Load Shed 回復分支 | **漏檢** —— #6 overlap **0.80** 判已覆蓋 | 未涵蓋（非具名標的）| **捕獲** —— 殘差 `resum` |
| (b) 通話轉移（兩處）| **捕獲** —— #8 / #13 皆 0.40 無對應 | —— | 捕獲（`transfer` / `not-ecall`）|
| (c) BODY OFF-TIMED | **漏檢** —— #9 overlap **0.72** 判已覆蓋 | **捕獲** —— `BODY OFF-TIMED` 未見於任何 TC | 捕獲（殘差 `off-tim`）|
| (c) voltage out of range | **捕獲** —— #15 0.43 無對應 | 未涵蓋（非具名標的）| 捕獲 |

**三項缺口全數可重現，惟其中兩項不是靠透鏡 1。**

#### 漏檢形態之說明（下放包所要求者）

透鏡 1 之漏檢形態為：**當缺失部分只是一個詞，而該行為項其餘實詞皆已見於某條 TC 時，
overlap 會很高而該項被判為已覆蓋。**
#6「until load shed signal broadcast **resumes**」——
`008` 已含 load / shed / signal / broadcast，缺者僅 `resumes` 一詞，overlap 4/5 = 0.80。
**這是重疊率判準之結構性弱點，不是門檻調得不對。**
調低門檻只會讓偽陽性暴增而不解決此形態。

#### 執行層之處置與其順序（必須明載）

**依 17 §I 未調整任何拆句規則或門檻。**
改為加設兩道獨立透鏡：

- **透鏡 2 —— 具名標的**：`source_clause` 之訊號名／全大寫術語／`_Time` 參數／數值，
  列出未見於該 leaf 任何 TC 者。此即 G82 之鏡像。
- **透鏡 3 —— 逐項殘差詞**：對**每一個**行為項（不論判為已覆蓋與否），
  列出「該項有而其最佳對應 TC 沒有」之實詞。

> **透鏡 3 是在我看到透鏡 1 漏掉 (a) 之後才加的。**
> 此順序已逐字寫入程式碼 docstring 與報告。
> 它與 13 包 §七(丙)7 所指之「先看答案再定門檻」屬同型風險，
> 差別在於：**本次未改動任何判準，只是把原本丟棄的殘差列出來。**
> 這個差別是我自己主張的，讀者應自行判斷它是否足夠。

另補一項字元正規化：規格原文之 `BODY\xa0OFF-TIMED` 使用 NBSP，
而 TC 使用一般空格 —— 不正規化會在**修補後**產生純字元層之偽陽性。
此為字元層處理，對三 leaf 一體適用。

### 1.2 現況實測（17 條 TC）

行為項合計 **20**（`071` 2、`072` 3、`073` 15），
已覆蓋 **17**，無對應 **3**。透鏡 2 之未見標的：`072` 之 `TLM_Status.Info` 一項。

## 現況（batch_001_power_down.json，17 條 TC）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-071 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：001, 002, 003, 004

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | TLM boot requires following timings: After SplashScreen_Time the splash screen | 001 | 0.50 | 已覆蓋 | `cas`、`follow`、`nor`、`only`、`pas`、`requir`、`standby`、`statu`、`these`、`timing` |
| 2 | After StandardScreen_Time the standard screen is visualized on TLM screen | 004 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

### SWE-PM-072 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：005, 006

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | Any event occurring during the boot must be recognized by TLM and then TLM has | 006 | 0.42 | **無對應** | `accord`、`behave`、`describ`、`occurr`、`par`、`proces`、`recogniz` |
| 2 | “TLM_Status.Info setting” while the boot is still completing | 005 | 0.50 | 已覆蓋 | `sett`、`tlm_status.info` |
| 3 | TLM must buffer the events and process them as soon as possible, depending on  | 006 | 0.60 | 已覆蓋 | `depend`、`proces`、`them`、`timing` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`TLM_Status.Info`

### SWE-PM-073 —— 行為項 15，已覆蓋 13，無對應 **2**

TC：007, 008, 009, 010, 011, 012, 013, 014, 015, 016, 017

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals ar | 007 | 0.81 | 已覆蓋 | `immediately`、`receiv`、`reduce` |
| 2 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 3 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 4 | ICS module shall power down | 007 | 1.00 | 已覆蓋 | （無） |
| 5 | Under fault condition of missing load shed signals on the CAN bus, the last va | 008 | 0.64 | 已覆蓋 | `fault`、`miss`、`under`、`used` |
| 6 | until load shed signal broadcast resumes | 011 | 1.00 | 已覆蓋 | （無） |
| 7 | If the load shed signals do not recover, the on-going load shed action shall b | 008 | 0.77 | 已覆蓋 | `do`、`on-go`、`recover` |
| 8 | The TLM shall transfer the call(not-Ecall/ACN call) to the head set in case a  | 012 | 0.60 | 已覆蓋 | `acn`、`case`、`not-ecall`、`transfer` |
| 9 | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_ | 009 | 0.72 | 已覆蓋 | `mimimize`、`off-tim`、`only`、`receiv`、`withdraw` |
| 10 | TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chim | 007 | 0.82 | 已覆蓋 | `immediately`、`reduce` |
| 11 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 12 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 13 | The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a | 012 | 0.60 | 已覆蓋 | `acn`、`case`、`not-ecall`、`transfer` |
| 14 | Unless defined otherwise, TLM shall stay in this state | 008 | 0.43 | **無對應** | `defin`、`otherwise`、`thi`、`unles` |
| 15 | until either voltage out of range conditions are satisfied or shall go back to | 010 | 0.43 | **無對應** | `back`、`becom`、`behavior`、`either`、`go`、`range`、`satisfi`、`voltage` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

**合計**：行為項 **20**，已覆蓋 **17**，無對應 **3**。

---

### 1.3 修補前之對照（十條）

## 驗證條件 —— 修補前（`b1_before16.json`，10 條 TC，R-P117 之三項缺口尚存）

門檻 `overlap >= 0.45`（透鏡 1）。

### SWE-PM-071 —— 行為項 2，已覆蓋 2，無對應 **0**

TC：001, 002, 003, 004

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | TLM boot requires following timings: After SplashScreen_Time the splash screen | 001 | 0.50 | 已覆蓋 | `cas`、`follow`、`nor`、`only`、`pas`、`requir`、`standby`、`statu`、`these`、`timing` |
| 2 | After StandardScreen_Time the standard screen is visualized on TLM screen | 004 | 1.00 | 已覆蓋 | （無） |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：（無）

### SWE-PM-072 —— 行為項 3，已覆蓋 2，無對應 **1**

TC：005, 006

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | Any event occurring during the boot must be recognized by TLM and then TLM has | 006 | 0.42 | **無對應** | `accord`、`behave`、`describ`、`occurr`、`par`、`proces`、`recogniz` |
| 2 | “TLM_Status.Info setting” while the boot is still completing | 005 | 0.50 | 已覆蓋 | `sett`、`tlm_status.info` |
| 3 | TLM must buffer the events and process them as soon as possible, depending on  | 006 | 0.60 | 已覆蓋 | `depend`、`proces`、`them`、`timing` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`TLM_Status.Info`

### SWE-PM-073 —— 行為項 15，已覆蓋 11，無對應 **4**

TC：007, 008, 009, 010

| # | 行為項 | 最佳對應 | overlap | 狀態 | 透鏡 3 —— 最佳對應所缺之實詞 |
|---|---|---|---|---|---|
| 1 | When STATUS_LIN.PN14_LS_Actv=[1h] and STATUS_LIN.PN14_LS_Lvl7= [1h] signals ar | 007 | 0.69 | 已覆蓋 | `alert`、`beep`、`immediately`、`receiv`、`reduce` |
| 2 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 3 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 4 | ICS module shall power down | 007 | 1.00 | 已覆蓋 | （無） |
| 5 | Under fault condition of missing load shed signals on the CAN bus, the last va | 008 | 0.64 | 已覆蓋 | `fault`、`miss`、`under`、`used` |
| 6 | until load shed signal broadcast resumes | 008 | 0.80 | 已覆蓋 | `resum` |
| 7 | If the load shed signals do not recover, the on-going load shed action shall b | 008 | 0.77 | 已覆蓋 | `do`、`on-go`、`recover` |
| 8 | The TLM shall transfer the call(not-Ecall/ACN call) to the head set in case a  | 009 | 0.40 | **無對應** | `call`、`case`、`continu`、`head`、`not-ecall`、`transfer` |
| 9 | While in BODY ON or BODY OFF-TIMED mode, when TLM receives STATUS_LIN.Batt_ST_ | 009 | 0.72 | 已覆蓋 | `mimimize`、`off-tim`、`only`、`receiv`、`withdraw` |
| 10 | TLM shall immediately reduce the maximum volume level to 20 for Ecall/ACN/Chim | 007 | 0.64 | 已覆蓋 | `alert`、`beep`、`immediately`、`reduce` |
| 11 | and if the volume was greater, send the AUD_LVL signal with the updated volume | 007 | 0.86 | 已覆蓋 | `greater` |
| 12 | If Ecall/ACN/chimes mode is not active, TLM shall be muted | 009 | 1.00 | 已覆蓋 | （無） |
| 13 | The TLM shall transfer the call (not-Ecall/ACN call) to the head set in case a | 009 | 0.40 | **無對應** | `call`、`case`、`continu`、`head`、`not-ecall`、`transfer` |
| 14 | Unless defined otherwise, TLM shall stay in this state | 008 | 0.43 | **無對應** | `defin`、`otherwise`、`thi`、`unles` |
| 15 | until either voltage out of range conditions are satisfied or shall go back to | 010 | 0.43 | **無對應** | `back`、`becom`、`behavior`、`either`、`go`、`range`、`satisfi`、`voltage` |

**透鏡 2 —— `source_clause` 之具名標的未見於任何 TC 者**：`BODY OFF-TIMED`

**合計**：行為項 **20**，已覆蓋 **15**，無對應 **5**。

---

## 二、三 leaf 無對應項之逐項裁決（必附二，R-P118(d) 三選一）

**沉默不算裁決**（R-P118(e)）。以下三項皆已裁決並登記。

| # | leaf | 行為項 | 裁決 | 依據 |
|---|---|---|---|---|
| 1 | `SWE-PM-072` #1 | `Any event occurring during the boot must be recognized by TLM and then TLM has to behave and process it according to the transitions described in par. "TLM_Status.Info setting"` | **已由他條涵蓋** | 辨識與緩衝面由 `005` 覆蓋（ER「No injected event is rejected」「no event dropped」），依轉換處理面由 `006` 覆蓋。**`TLM_Status.Info setting` 之轉換定義位於 CFTS009 §1.6.2.1.15，依 R-P42 不在本 leaf 之錨點範圍**，故該部分不測。overlap 0.42 僅略低於門檻 0.45，係因該項橫跨兩條 TC 而無單一最佳對應 |
| 2 | `SWE-PM-073` #14 | `Unless defined otherwise, TLM shall stay in this state` | **已由他條涵蓋** | 「停留於該狀態」由 `010` ER1（「stays reduced to 20 and the TLM stays muted before the measurement window elapses」）與 `015` ER1（「stays in the Battery Critical state while the signal is held」）覆蓋。`Unless defined otherwise` 為規格之免責語，非可測行為 |
| 3 | `SWE-PM-073` #15 | `until either voltage out of range conditions are satisfied or shall go back to normal behavior 10 seconds after STATUS_LIN.Batt_ST_Crit becomes [0h]` | **已由他條涵蓋（`015` ＋ `010`）**，惟 `015` 另受 DR-PW8 阻斷 | 該項係拆句時將**兩個回復分支併為一項**之產物：voltage 分支由 `015` 覆蓋、10 秒分支由 `010` 覆蓋，故無單一 TC 之 overlap 達門檻。**`015` 依 R-P121 為可撰寫而不可執行**（A-PW83），此狀態已於其 `remarks` 標明 |

### 2.1 透鏡 3 另使兩項新缺口現形 —— 一併裁決

| 項 | 殘差詞 | 裁決 | 處置 |
|---|---|---|---|
| `4942354` #1 / #10 之音訊類別範圍 `for Ecall/ACN/Chimes/Beeps/Alerts` | `alert`、`beep` | **同一行為之措詞不足**（非另一行為）| 於 `007` / `009` / `014` 之 ER 明列該五類音訊，**未另拆條** —— 音量上限為單一行為，其適用範圍屬同一失效模式（§8.2.2）|
| `4942354` #2 / #11 之 `and if the volume was **greater**` | `greater` | **真缺口** | 15 條僅測「原音量 25 > 20」之正分支，**未超過 20 時不送 `AUD_LVL` 之負分支未測**。依 R-P118(d) 補 **`016`**（Load Shed 側）與 **`017`**（Battery Critical 側），起始音量 15。TC **15 → 17**，**leaf 仍為 3** |

> **透鏡 1 對 `greater` 該項判 overlap 0.86「已覆蓋」。**
> 若無透鏡 3，這個分支不會被任何人問起。
> 這是本包最直接的證據：**單一判準的反向涵蓋檢查不夠。**

### 2.2 補測二條之全文

#### NR1L-PowerManagement-016 — SWE-PM-073（split_index 2）

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

#### NR1L-PowerManagement-017 — SWE-PM-073（split_index 7）

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

---

## 三、B2 / B3 之刻意弄壞證明（必附三）

來源 SHA256 前後相同 —— **`inputs/` 未被觸碰**（`ce93174794d0d43c…`）。
全程僅對 `features/power/sandbox/` 之副本為之，**無任何 `Workbook.save()` 呼叫**。

### 3.1 G89 —— `verify_structure()` 之三項檢查（R-P119）

| 案例 | 期望 | 實測 | 判定 |
|---|---|---|---|
| 正常：位元組複製（不得誤拋） | 不得拋 | `raised=False` | **PASS** |
| 弄壞 1：刪去一個 zip member（`xl/calcChain.xml` 或次末者） | 須拋 | `raised=True` | **PASS** |
| | | `zip member set changed — lost ['xl/comments1.xml'], added []. The delivered file must carry ever` | |
| 弄壞 2：抹去目標分頁之一條 `dataValidation` | 須拋 | `raised=True` | **PASS** |
| | | `data-validation counts changed (classic, x14): {'xl/worksheets/sheet5.xml': ((1, 0), (0, 0))}. T` | |
| 弄壞 3：改動未被寫入之 `xl/styles.xml` | 須拋 | `raised=True` | **PASS** |
| | | `members differ that were not written: ['xl/styles.xml']. Only the target sheets' XML may change` | |

**四案全數如期。三項檢查皆可以刻意弄壞觸發，無一須標「未實測」。**

本專案唯一授權之寫回路徑，至此首度有閘門在驗它（A-PW81）。

### 3.2 G90 —— append 邊界保護（R-P120）

合成之非 BLANK 副本：前 **5** 列為「他人既有列」
（author 欄寫 `SomeoneElse`），共 **80** 格。

| 項 | 期望 | 實測 | 判定 |
|---|---|---|---|
| (a) 既有列逐格內容不變 | 完全相同 | 快照 SHA256 `2d2edfffb83f04f6…` → `2d2edfffb83f04f6…`，**逐格相同** | **PASS** |
| (b) 新列自既有列之後起始，無覆蓋 | 無既有格被改動 | 新列自 **r15** 起；改動之既有格 **0** | **PASS** |
| (c) B 欄序號與既有列銜接 | 連續 | `[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]` —— **1–22 連續** | **PASS** |
| (d) 刻意重疊 → 須 FAIL | 偵出 | 自 **r13** 起（重疊二列）→ 既有格被改動 **15** 格，如 `AB13`、`AB14`、`D14`、`F13`、`F14` | **PASS（確實可能失敗）** |

> **一項須明報之限制**：(d) 之偵測係由**本腳本之逐格快照比對**得出。
> **`surgical_save` 自身不會因覆蓋既有列而拋錯** ——
> 它保證的是「除目標分頁外一切不變」，**不保證「目標分頁內既有列不變」**。
> **append 起始列之正確性目前仍靠呼叫端**，已登記 A-PW82 並列入待裁。

---

## 四、B5 —— R-P116 素材三 feature 併表（必附四，**不含建議**）

| feature | 工作簿 | `D` 欄非空列 | **僅 `D`（＋`B` 序號）有值、其餘全空者** |
|---|---|---|---|
| Comfort | `…_Comfort_20260817.xlsx` | 466 | **0** |
| **Home** | `…_Home_20260809.xlsx` | **216** | **0** |
| Privacy | `…_Privacy_20260813.xlsx` | 11 | **0** |
| **合計** | | **693** | **0** |

三份皆 `read_only=True`，未呼叫 `save()`。
15 包因加入 Home 而使 G77 之結論翻轉，本次擴查**未使結論翻轉** —— 三者一致為 0。

> **執行層對此素材之限制聲明**：三者共 693 列**皆為已完成之交付件**。
> 「保留空白列」若存在於實務中，較可能出現在**進行中**之工作簿而非已交付者。
> 本素材能支持的結論是「已交付件中無此形態」，
> **不能支持「此形態不被接受」**。R-P116 仍待 Pei，執行層不建議。

---

## 五、§D 全表自驗（必附五）

| # | 項目 | 期望值 | **實測** | 判定 | 證據型別 |
|---|---|---|---|---|---|
| **G0** | 素材同一性 | 7 / 7 | 7 / 7 | **PASS** | 真實 |
| **G91** | 反向涵蓋報告 | 行為項／已覆蓋／無對應；**且須能重現 R-P117 三項缺口** | 行為項 **20**、已覆蓋 **17**、無對應 **3**；**三項缺口全數重現，惟透鏡 1 單獨僅重現 1 項**，另二項靠透鏡 2 / 3 | **PASS（附條件）** | **真實** |
| **G89** | `verify_structure` 三項檢查 | 各有刻意弄壞之案例確實拋 `StructureError`；正常案例不誤拋 | **四案全數如期**；三項皆可觸發，無「未實測」 | **PASS** | **合成＋真實** |
| **G90** | append 邊界保護 | 既有列逐格不變；新列不覆蓋；B 欄銜接；重疊 FAIL | 四項全數如期（80 格快照逐格相同；重疊時 15 格被改動）| **PASS** | **合成＋真實** |
| **G92** | `015` remarks 標記 | `remarks` 有值且不觸發任何既有閘門 | `remarks` 有值；lint `exit=0`。**惟此結果在很大程度上是空的** —— G50 之 `LONG_FIELDS` 不含 `remarks`（A-PW88）| **PASS（判準空洞，已標示）** | 真實 |
| **G93** | R-P116 素材三 feature 併表 | Comfort / Home / Privacy 各自之結果 | 466 / 216 / 11 列，**皆為 0** | **PASS** | 真實 |
| **G70** | lint 全閘 | 全 PASS；leaf 仍 3；TC 15 | `exit=0`；阻斷類 PASS；待裁類無觸發；leaf **3**；**TC 17**（R-P118(d) 補 `016`/`017`）| **PASS（TC 數與期望不同，見下）** | 真實 |
| G85 | 排序腳本 | 沿用 | 五案如期（073 之 split_index 已重排為 1–11）| **PASS** | 合成 |
| G1–G87 | 沿用 | 期望值不變 | `--self-test` **35 / 35 TC fixture ＋ G46 皆如期** | **PASS** | 混合 |

**§D 之 G70 期望「TC 15」而實測 17** —— 因 R-P118(d) 之裁決要求對真缺口補 TC，
本包依該條補 `016` / `017`。**leaf 仍為 3，未擴大批次範圍。**

---

## 六、必附六 —— R-P124 之三項前置是否全備，第二批可否開始

> **明確回答：三項前置全備，第二批（`Timeout Settings`，8 leaf）可以開始。**

| 前置 | 狀態 | 依據 |
|---|---|---|
| **R-P118** 反向涵蓋 | **全備** | 腳本已實作並對修補前資料實測；三項已知缺口全數重現；**其漏檢形態已明報而未以調整判準掩蓋** |
| **R-P119** `surgical_save` 閘門 | **全備** | 三項檢查各以刻意弄壞證明會拋，正常案例不誤拋，四案如期 |
| **R-P120** append 邊界 | **全備（附一限制）** | 四項如期；惟 `surgical_save` 自身不保證目標分頁內既有列不變，起始列正確性仍靠呼叫端 |

**執行層之一項保留（不構成阻斷）**：
R-P118 之產物是**報告與人工裁決**，不是閘門。
其效力完全取決於**有人真的讀那份報告並逐項裁決**。
本包三 leaf 共 20 個行為項，是我逐項讀過的；
第二批 8 leaf 之行為項數量將數倍於此。
**「沉默不算裁決」是唯一的保護，而它是紀律，不是機制。**
若第二批之反向涵蓋報告只被掃過而未逐項裁決，本包所建立者即形同虛設。

---

## 七、必附七 —— 執行層對「本包是否仍有該驗而未驗者」之獨立判斷

16 §八之九項已由 R-P118 ~ R-P123 分派，本節**不覆述**。

**（甲）本包新產生或新暴露之該驗而未驗者 —— 五項**

1. **`016` / `017` 是我自己裁決出來、自己補的，無人覆核。**
   透鏡 3 列出殘差詞 `greater`，是**我**判定它是真缺口而非措詞差異，
   也是**我**決定補兩條而非四條（Load Shed 與 Battery Critical 各一，不再依 mode 細分）。
   R-P118(d) 要求裁決並登記，我做了；但**裁決者與被裁決之工作出自同一人**，
   與 15 / 16 包所指之風險同型，且本次連分析層都尚未看過。

2. **透鏡 3 會列出大量殘差詞，其中絕大多數不是缺口。**
   本包 20 個行為項共列出殘差詞數十個，我判定其中兩項為問題。
   **另外那幾十個是我判「無妨」的，沒有逐一寫下理由。**
   第二批的量會大得多 —— 這道透鏡有沒有實用的信噪比，本包沒有量測。

3. **反向涵蓋只做了三個 leaf，而這三個的 `source_clause` 是我抄的。**
   15 包 §七第 7 項已指出 G79 不驗 `source_clause` 抄得對不對。
   反向涵蓋建立在同一份材料上 —— **若某條規格句根本沒被抄進 `source_clause`，
   反向涵蓋在原理上看不見它。**這是整條鏈路最上游的未驗點。

4. **G90 之 (d) 只證明「重疊會改動既有格」，未證明有任何東西會攔下它。**
   偵測是我的腳本做的，不是寫回路徑做的。
   真實寫回時若起始列算錯，`surgical_save` **會照寫不誤**。
   我把這點寫進 A-PW82 與待裁，但**它現在仍是一個未設防的失敗模式**。

5. **G92 實質上沒有驗到東西。**
   `remarks` 有值而 lint 綠，是因為沒有任何格式閘門看那一欄（A-PW88）。
   我把它標成「判準空洞」而非 PASS，但這意味著
   **DR-PW8 之標記在工作簿內可見與否，靠的是人去看，不是閘門。**

**（乙）已驗而應標明其強度不足者 —— 二項**

6. **B5 之三 feature 併表，母體全是已交付件。**
   「保留空白列」若存在，較可能出現在進行中之簿。已於 §四明載，不重複。

7. **G89 驗的是 `verify_structure` 會不會拋，不是它拋得對不對。**
   我證明了三項檢查各自可觸發；**沒有證明它們涵蓋了所有該攔的情形。**
   例如：若寫回改動了目標分頁之 `<mergeCell>` 或 `<conditionalFormatting>`，
   該分頁本就在允許相異之清單內，`verify_structure` **不會攔**。
   16 包是靠我另寫的 `structure_snapshot` 才驗到 merges / cf 未變。

**（丙）本包自身之作業瑕疵 —— 一項**

8. **透鏡 3 之新增順序。** 已於 §一之 1.1 逐字說明：
   它是在看到透鏡 1 漏檢之後才加的。
   我主張「未改動判準、只增加輸出」與調門檻有本質差別，
   但**這個主張是我自己的，讀者應自行判斷。**

---

## 八、DATA_REQUESTS

**新增 DR-PW8（High）** —— `voltage out of range` 之電壓門檻值（R-P121 / A-PW83）。
現存 live：DR-PW1（High）、DR-PW5（High）、**DR-PW8（High）**、
DR-PW3（Medium）、DR-PW6（Medium）、DR-PW7（Low）；DR-PW2、DR-PW4 維持撤回。

---

## 九、產出檔案

| 檔案 | 說明 |
|---|---|
| `features/power/scripts/reverse_coverage.py` | 反向涵蓋三透鏡（新增）|
| `features/power/scripts/verify_writeback_path.py` | G89 / G90（新增）|
| `features/power/data/reverse_coverage_batch1.md` | 反向涵蓋報告（新增）|
| `features/power/data/b2b3_writeback_path.json` | G89 / G90 實測資料（新增）|
| `features/power/data/b1_before17.json` | 16 包版快照（新增）|
| `features/power/generated/batch_001_power_down.json` | 補 `016`/`017`、ER 明列音訊類別、`015` remarks、split_index 重排（改）|
| `features/power/DATA_REQUESTS.md` | DR-PW8（改）|
| `features/power/RULINGS.md` | R-P118 ~ R-P124（改）|
| `features/power/ANOMALIES.md` | A-PW80 ~ A-PW88（改）|
| `features/power/docs/handoff/17_reverse_coverage.md` | 下放包逐字落檔（新增）|
| `features/power/docs/upstream/17_reverse_coverage.md` | 本檔（新增）|
| `features/power/docs/INDEX.md` | 第 17 輪索引（改）|
