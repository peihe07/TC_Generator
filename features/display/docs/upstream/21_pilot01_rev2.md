# 上繳包 21 —— pilot-01 覆核之處置（rev2）

- 日期：2026-08-25
- 方向：執行層（Claude Code）→ 分析層（Claude Project）
- 對應下放：`features/display/docs/handoff/21_pilot01_rev2.md`
- 步驟 1–7 全數執行。**五十五條停止條件全未觸發。**
- **git 未執行**（§7 為建議）

---

## 摘要

| 退回項 | 處置 | 依據 |
|---|---|---|
| §2.1 #1／#2 觸發相同而結果不同 | **原 #2 deferred**，開 **DR-DM10**，登 **A-DM33** | 分支 3；四條查證路徑皆不產生可觀測之區分準據 |
| §2.2 欄位歸屬 | 門檻值移入 `pre_conditions` 之具體值；`input_test_data` 三條皆 `NA` | canon §8.7.1／§4.5 |
| §2.3 `{4820282}` 是否該留 | **保留於 #1 之 `specification_reference`** | 其本體即 #1 step 2／ER 2 所直接驗證者 |
| §2.4 缺負向／邊界 | **補列 #4**（`= 85 degrees C` 不進入 Hot） | `{4820289}` 明載 `<= 85 degrees C` 為 non-Hot |

**本輪之查證推翻了本包自己的第一版理由。** A-DM33 初稿寫「三組條款皆適用
且互不一致」；逐條讀屬性行後改正為「兩組適用且互相排斥，第三組之 DCSD 側
為 `Radio:noSys`」。**結論不變（#2 仍 deferred），理由改變。** 依 R-G19
理由與數字分別查證，故於 A-DM33、DR-DM10、`batch_context.md`、`INDEX.md`
四處分別更正並留註。

---

## 一、`{4820281}` 節與 `{4820282}` 之逐字全文，及其判定

### 1.1 抽取方式

`python-docx` 逐 block 走訪（段落與表格皆納），以「不含 tab 之
`1.11.2.2` 起始段」定位本文（含 tab 者為目次項，本文之外另有 1 筆），
至下一個同層級標題止。**逐字，未經改寫。** 區間 `items[3458..3492]`。

### 1.2 `1.11.2.2 DCSD Display Hot Behavior {4820281}` 全文

```text
4820282: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:VP5R120, R1H, R1M] [EE Architecture:PowerNet, Atlantis High]
When the DCSD determines that it is in a 'Display Hot State' it shall notify the HU by sending $DCSD_DISP_STAT$ = [DISP_HOT]. See {CFTS013-629} for the DCSD Display Hot Algorithm. See the DCSD Display Hot Diagnostics below for other details.
4820283: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1H, VP5R120, R1M] [EE Architecture:PowerNet, Atlantis High]
When the HU has finished displaying the Display Hot warning screen and determines that the DCSD display should now be 'Turned Off' to help it cool down, the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity].
4820284: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1H, R1M, VP5R120] [EE Architecture:PowerNet, Atlantis High]
While the DCSD is still in the Hot state and the DCSD receives $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity] the DCSD shall turn off the display backlighting in order to help it cool down and shall continue to send $DCSD_DISP_STAT$ = [DISP_HOT].
4820285: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1M, VP5R120, R1H] [EE Architecture:Atlantis High, PowerNet]
While the DCSD is still in the Hot state and the HU is sending $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity], if the HU determines it needs to have the display temporarily turn back on, the HU shall send $TGW_DISP_STAT$ <> [DISP_OFF] and $RQ_DISP_INTS$ = [current non-zero value].
4820286: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1M, VP5R120, R1H] [EE Architecture:Atlantis High, PowerNet]
When the DCSD receives a sequence of $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity] and then $TGW_DISP_STAT$ <> [DISP_OFF] and $RQ_DISP_INTS$ = [current non-zero value] the DCSD shall turn the backlighting back on to temporarily display the screen sent by the HU.
4820287: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1H, R1M, VP5R120] [EE Architecture:Atlantis High, PowerNet]
When the DCSD determines that it is no longer in a 'Display Hot State' it shall notify the HU by sending $DCSD_DISP_STAT$ = [DISP_ON].
4820288: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:VP5R120, R1M, R1H] [EE Architecture:PowerNet, Atlantis High]
When the HU receives a sequence of $DCSD_DISP_STAT$ = [DISP_HOT] and then $DCSD_DISP_STAT$ = [DISP_ON] the HU shall resume normal screen display behavior - i.e. execute the 'Display is not Hot' behavior part of the DCSD Display Hot algorithm.
4820289: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1H] [EE Architecture:Atlantis High]
When the DCSD Display transitions to a Hot state (> 85 degrees C) from a non-Hot state (<= 85 degrees C), and if there is no high priority screen (RVC), then DCSD shall:
 Send CAN signal $DCSD_DISP_STAT$=[DISP_HOT]
 Set the DTC (B1429-00) Radio Display High Temperature after the enable conditions and mature time thresholds are met.
 Turn off the backlight (both top and bottom portion) and disable touch.
 Send CAN signal $DCSD_DISP_STAT$=[DISP_OFF]
4820290: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1H] [EE Architecture:Atlantis High]
When the DCSD Display transitions from a Hot state (> 85 deg C) to a non-Hot state (<= 85 deg C), and then DCSD shall:  
           a. Clear the DTC (B1429-00) Radio Display High Temperature after the de-mature time thresholds are met. 
           b. Turn on the backlight (both top and bottom portion) and Enable touch.
           c. Send CAN signal $DCSD_DISP_STAT$=[DISP_ON].        
4820291: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1H] [EE Architecture:Atlantis High]
During Display HOT condition, if a high priority screen (RVC) is active and DCSD receives $TGW_DISP_STAT$ <> [DISP_OFF] and $RQ_DISP_INTS$ = [current non-zero value], and DCSD shall turn ON the backlight and enable the touch.
4820292: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:R1H] [EE Architecture:Atlantis High]
During Display HOT condition, Upon dismissing high priority screen ( RVC ), DCSD shall turn OFF the backlight (full screen), disable the touch and send the $DCSD_DISP_STAT$ = [DISP_OFF].
```

### 1.3 `{4820282}` 之判定（§2.3 之複驗）

其逐字為：

> `4820282: [Artifact Type:Subsystem Functional Requirement] [State:Approved] [Market:All] [Model Year:Default] [Radio:VP5R120, R1H, R1M] [EE Architecture:PowerNet, Atlantis High]`
> `When the DCSD determines that it is in a 'Display Hot State' it shall notify the HU by sending $DCSD_DISP_STAT$ = [DISP_HOT]. See {CFTS013-629} for the DCSD Display Hot Algorithm. See the DCSD Display Hot Diagnostics below for other details.`

**判定：保留於 #1 之 `specification_reference`。** 三點：

1. 該條之**規範本體**是「DCSD 判定進入 Display Hot State 時，以
   `$DCSD_DISP_STAT$ = [DISP_HOT]` 通知 HU」。#1 之 step 2 讀該訊號、
   ER 2 驗其值為 `4 (DISP_HOT)` —— **直接驗證，非間接關聯**，
   符合 canon §10.7「列出該 TC 直接驗證之每一節」。
2. `See {CFTS013-629} for the DCSD Display Hot Algorithm` 為**節內指標**，
   指的是「Hot State 之判定演算法」而非「通知行為」。演算法本體不在手上
   （DR-DM4），但**本 TC 不驗演算法，驗的是判定成立後之通知**。
   兩者可分，故該指標不使本條失去可驗性。
3. 其屬性行含 `Radio:… R1H …` 與 `EE Architecture:… Atlantis High`，
   對本專案適用。

### 1.4 架構適用性之逐條讀（A-DM33 之更正）

| 條 | 屬性行（逐字節錄） | 對 `R1H`／`Atlantis High` |
|---|---|---|
| `{4820282}` | `[Radio:VP5R120, R1H, R1M] [EE Architecture:PowerNet, Atlantis High]` | 適用 |
| `{4820283}` | `[Radio:R1H, VP5R120, R1M] [EE Architecture:PowerNet, Atlantis High]` | 適用 |
| `{4820284}` | `[Radio:R1H, R1M, VP5R120] [EE Architecture:PowerNet, Atlantis High]` | 適用 |
| `{4820287}` | `[Radio:R1H, R1M, VP5R120] [EE Architecture:Atlantis High, PowerNet]` | 適用 |
| `{4820288}` | `[Radio:VP5R120, R1M, R1H] [EE Architecture:PowerNet, Atlantis High]` | 適用 |
| `{4820289}`–`{4820292}` | `[Radio:R1H] [EE Architecture:Atlantis High]` | 適用（且僅本專案） |
| `{4820948}`（Multi-stage 節首） | `[Radio:R1H, R1L-R, R1L, R1M] [EE Architecture:Atlantis High, Atlantis Mid, PowerNet]`，本文為 `The Multi-stage Display Hot algorithm shall not be implemented by the DCSD supplier.` | 節首宣告**不由 DCSD 實作** |
| `{4820951}`／`{4819862}` | `[ECU:DCSD] … [Radio:noSys] …` | **不適用**（`noSys`） |
| `{4820952}` | `[ECU:ETM, LTM] … [Radio:R1M, R1L-R, R1H, R1L] …` | HU 側適用 |
| `{4820953}`／`{4820955}`／`{4820956}` | `[ECU:DCSD] … [Radio:noSys] …` | **不適用**（`noSys`） |

即 Multi-stage 節以 **ECU 角色**切分：HU 側（`ETM`／`LTM`）帶 `R1H`，
DCSD 側一律 `Radio:noSys`。**該節不構成本專案之第三個適用流程。**

**組 A 與組 B 之矛盾（皆適用）：**

| 事項 | 組 A `{4820282}`–`{4820288}` | 組 B `{4820289}`–`{4820292}` |
|---|---|---|
| 誰關背光 | `{4820283}` HU 判定後送 `[DISP_OFF]` ＋ `[0% Intensity]` → `{4820284}` DCSD 收到才關 | `{4820289}` DCSD 越過門檻即 `Turn off the backlight (both top and bottom portion) and disable touch` |
| 警示階段 | 有（`{4820283}` 之 `has finished displaying the Display Hot warning screen`） | 無（四項動作中不含警示畫面） |
| 關背光後之 `$DCSD_DISP_STAT$` | `continue to send $DCSD_DISP_STAT$ = [DISP_HOT]`（`{4820284}`） | `Send CAN signal $DCSD_DISP_STAT$=[DISP_OFF]`（`{4820289}`） |

**本層不裁定何者為準**（Tier 2，上游文件之內部矛盾）→ DR-DM10 (a)。

---

## 二、§2.1 之處置：**deferred**（三選一，記理由）

**擇「deferred」，不擇「修訂」，不擇「併入 DR-DM4」。**

### 2.1 為何不擇「修訂」

修訂之前提是「區分準據存在，只是未寫進 TC」。逐字查證四條路徑：

| 路徑 | 逐字所得 | 產生可觀測之區分準據？ |
|---|---|---|
| 組 A `{4820283}` | `When the HU has finished displaying the Display Hot warning screen and determines that the DCSD display should now be 'Turned Off' to help it cool down, the HU shall send $TGW_DISP_STAT$ = [DISP_OFF] and $RQ_DISP_INTS$ = [0% Intensity].` | **否** —— `has finished` 與 `determines` 皆未給時長、門檻或可觀測事件 |
| 組 B `{4820289}` | 四項動作之清單，前後無時序連接詞 | **否** —— 未給任一步之時間關係 |
| 組 C `{4820951}`／`{4819862}` | `When the DCSD determines it wants to turn off it's backlighting (see {CFTS013-XXX}), the DCSD shall send $DCSD_DISP_STAT$ = [DISP_OFF].` | **否** —— 指向未填佔位符；且該條 `Radio:noSys` |
| Pop Up List | `PU0130` 說明欄逐字 `If the screen is determined to be too hot this pop-up will be displayed for 10 seconds, if the screen has not cooled down the display will turn off until it has cooled`；`Timeout` 欄 `10` | **否** —— `has not cooled down` 之判準與其觀測時點未給 |

四路皆空 → **無可修訂之對象**。若此時寫 TC，其步驟中之「等待 N 秒」
必為本層自造之值（canon §8.4.1、停止條件 53）。

### 2.2 為何不併入 DR-DM4

DR-DM4 之標的為 CFTS_013 之 `-629`／`-633`／`-952` **三個已編號條款之內容**。
DR-DM10 求三件 DR-DM4 涵蓋不到者：

- (a) 組 A 與組 B 何者為本架構之準 —— **是一項條款衝突之裁定，不是一份文件**
- (b) `{4820283}` 之警示階段時長／終止準據 —— **在 CFTS_020，不在 CFTS_013**
- (c) `{CFTS013-XXX}` 之實際條號 —— **一個尚未編號的條款無法用既有 DR 索取**

故分立。DR-DM10 已登記為 **HIGH**，關聯 A-DM33。

### 2.3 deferred 之範圍

| 項 | 狀態 |
|---|---|
| 原 #2（`SWE1-DM-005` 保護性關閉） | deferred，DR-DM10 |
| `PU0130`（`Screen is Hot. Display turning off to cool down.`） | 隨 #2 deferred |
| `SWE1-DM-005` 之 multi-stage 分級門檻 | deferred，DR-DM4（既有） |

**#3（回復路徑）不受影響** —— 組 A（`{4820287}`／`{4820288}`）與
組 B（`{4820290}`）對回復側無分歧，兩組皆為「溫度降回 non-Hot →
背光開、觸控啟用、送 `[DISP_ON]`」。

---

## 三、修訂後之 TC 全文

### 3.0 編號對照

| rev1 | rev2 | 說明 |
|---|---|---|
| #1 Hot 警示 popup | **#1**（欄位歸屬修正） | 保留 |
| #2 保護性關閉 | **—** | **deferred**（§二） |
| #3 回復 | **#3**（欄位歸屬修正） | 保留 |
| — | **#4**（新） | §2.4 之邊界負向條 |

`generated/pilot-01.json` 之 `tcs` 陣列依 leaf 排序為 `[#1, #4, #3]`，
共 **3 筆**。`tc_id` 皆為 `null`（未寫回，編號屬 036 母本）。

### 3.1 #1 — `SWE1-DM-004` 正向

| 欄 | 值 |
|---|---|
| `leaf_id` | `SWE1-DM-004` |
| `test_group` | `Display` |
| `test_set` | `Thermal Management` |
| `tc_title` | `Hot threshold exceeded → thermal warning popup displayed` |
| `design_method` | `狀態轉換 (State Transition Testing)` |
| `priority` | `P1` |
| `functional_safety` | `NA` |
| `specification_reference` | `CFTS020-4820282` / `CFTS020-4820289` |

```text
[test_item]
The Display Management software shall monitor thermal status inputs and evaluate Hot condition thresholds based on configured thermal algorithm logic. The software shall trigger warning popup requests when configured warning threshold conditions are satisfied.

(Warning stage on crossing the Hot threshold — the popup that follows the DISP_HOT notification)

[pre_conditions]
1. The DCSD display temperature is 85 degrees C or below
2. No high priority screen (RVC) is active

[input_test_data]
NA

[test_procedure]
1. Raise the DCSD display temperature above 85 degrees C
2. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and check that it is 4 (DISP_HOT)
3. Read the popup shown on the display and record how long it stays

[expected_result]
1. The DCSD Display transitions to a Hot state
2. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ = 4 (DISP_HOT) is received
3. The popup "Screen is Hot. Display brightness has been reduced." is displayed for 10 seconds
```

值之出處：`85 degrees C` 與 `no high priority screen (RVC)` 為 `{4820289}`
逐字；`4 (DISP_HOT)` 為 R-DM17 三段解析所得（SYS2 `$DCSD_DISP_STAT$` →
LID `CAN Mapping` → DBC `VAL_`）；popup 文字與 `10 seconds` 為
`Pop Up List HMI R1 (26PI).xlsx` `Main` 之 `PU0517` 逐字。

**#1 之 ER 不驗亮度數值** —— `PU0517` 之文字說「brightness has been
reduced」，而 CFTS `1.11.2.2` 與 SYS2 r31 對本架構**皆未載降低後之亮度值**
（SYS2 r31 反而寫 `$RQ_DISP_INTS$ = [current non-zero value]`）。
依 canon §8.4.1 不自造。

### 3.2 #4 — `SWE1-DM-004` 邊界負向（新）

| 欄 | 值 |
|---|---|
| `leaf_id` | `SWE1-DM-004` |
| `tc_title` | `Temperature at 85 degrees C → Hot state not entered` |
| `design_method` | `邊界值分析 (Boundary Value Analysis, BVA)` |
| `split_flag` | `True` |
| `specification_reference` | `CFTS020-4820289` |

```text
[test_item]
The Display Management software shall monitor thermal status inputs and evaluate Hot condition thresholds based on configured thermal algorithm logic.

(Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, so nothing is triggered)

[pre_conditions]
1. The DCSD display temperature is below 85 degrees C
2. No high priority screen (RVC) is active

[input_test_data]
NA

[test_procedure]
1. Raise the DCSD display temperature to 85 degrees C
2. Read the signal $DIS_CENTERSTACK.DCSD_DISP_STAT$ and record its value
3. Read the display and record any popup shown

[expected_result]
1. The DCSD Display stays in a non-Hot state
2. The signal value $DIS_CENTERSTACK.DCSD_DISP_STAT$ is not 4 (DISP_HOT)
3. No popup is shown on the display
```

`split_reason`（逐字）：

> `§8.3 boundary 軸：{4820289} 之 > 85 degrees C 與 <= 85 degrees C 使 85 恰屬 non-Hot，為 spec 明載之邊界；與正向條之失效可獨立發生（§9 第 11 項之 negative）`

**邊界值非推論**：`{4820289}` 逐字為
`transitions to a Hot state (> 85 degrees C) from a non-Hot state (<= 85 degrees C)`
—— 85 落在 `<=` 側，spec 明載。

**ER 2 只寫否定** —— 寫 `is not 4 (DISP_HOT)`，不寫「應為 `0 (OFF)`」。
理由：`[DISP_OFF]`／`[DISP_ON]` 之 raw 值尚未取得（DR-DM9），依 R-DM48
不得寫入未逐字解析之值標籤（停止條件 54）。

### 3.3 #3 — `SWE1-DM-005` 回復

| 欄 | 值 |
|---|---|
| `leaf_id` | `SWE1-DM-005` |
| `tc_title` | `Temperature falls back to non-Hot → backlight on and touch enabled` |
| `design_method` | `狀態轉換 (State Transition Testing)` |
| `specification_reference` | `CFTS020-4820287` / `CFTS020-4820288` / `CFTS020-4820290` |

```text
[test_item]
The Display Management software shall determine display ON/OFF operational decision based on thermal protection algorithm evaluation.

(Return path of the ON/OFF decision — verifies the recovery side, not the protective shutdown)

[pre_conditions]
1. The DCSD display temperature is above 85 deg C
2. The backlight is off on both the top and the bottom portion

[input_test_data]
NA

[test_procedure]
1. Read the backlight state of the top and the bottom portion of the display and record it
2. Lower the DCSD display temperature to 85 deg C or below
3. Read the backlight state of the top and the bottom portion of the display
4. Touch the display and check that the touch input is accepted

[expected_result]
1. The backlight is off on both the top and the bottom portion
2. The DCSD Display transitions from a Hot state to a non-Hot state
3. The backlight is turned on for both the top and the bottom portion
4. Touch input is enabled
```

step 1／ER 1 為 canon §5.6 之 baseline（回復須有前後對照）。
`85 deg C`（非 `degrees C`）為 `{4820290}` 之逐字寫法，**不統一改寫**。

### 3.4 §2.2 欄位歸屬之修正對照

| 欄 | rev1 | rev2 | 依據 |
|---|---|---|---|
| `pre_conditions` | 狀態名（`non-Hot state`／`Hot state`），無具體值 | **具體門檻值**（`85 degrees C or below`／`below 85 degrees C`／`above 85 deg C`） | §8.7.1「門檻須為 spec 來源之具體值」 |
| `input_test_data` | 門檻值 | **`NA`** | §4.5 欄位歸屬；資料已在 PC／Procedure，重複即應改 `NA` |
| `test_procedure` | 操作值 | **維持** | 步驟須可執行，非欄位重複 |

三條之 `pre_conditions` 皆經機器檢查無動作動詞（停止條件 55，見 §五）。

---

## 四、逐條 §9 自檢十七項

判讀慣例：**「符」＝已逐項對照 canon 該節；「NA」＝該項之前提不存在
（非「略過」）。** 凡「符」而其判準為機器可測者，於 §五附輸出。

### 4.1 #1（`SWE1-DM-004` 正向）

| # | 項 | 判定 | 依據 |
|---|---|---|---|
| 1 | Test Set 名詞片語、與 `framework.md` 一致 | 符 | `Thermal Management`，`framework.md` Layer 2 第 2 組（001-003／**004-005**／006／007-008）；無 Test Group 前綴、非 `Misc` |
| 2 | tc_title 三形之一、2–14 字、可見 sibling token、無情態 | 符 | 「條件 → 結果」形；**8 字**；sibling token `Hot threshold exceeded`；無 `shall`／`should` |
| 3 | PC 僅狀態／環境；每項為 spec 觸發條件 | 符 | 兩項皆自 `{4820289}` 之觸發子句（溫度側、RVC 側）；非「環境穩定」之隱含前提 |
| 4 | Input Test Data 欄位歸屬正確 | 符 | 已改 `NA`；門檻值移入 PC，操作值留 Procedure |
| 5 | 步驟可執行、無禁用動詞、Final Step 承載驗證 | 符 | 主動詞 `Raise`／`Read`／`Read`；lint A 檢查 0（`Observe` 與 `check whether` 已於 20 輪改為 `Read`／`check that`） |
| 6 | 步驟長度與意圖層級 | 符 | 三步皆單一動作；step 2 為 necessary-intent（讀訊號並判值） |
| 7 | 標準 setup 片語逐字重用 | NA | 本 feature 尚無已核定之 setup 片語庫 |
| 8 | CLI 步驟採 描述 ＋ `$` 格式 | NA | 無 CLI 步驟 |
| 9 | 需前後對照時建 baseline | NA | 本條為單向轉換，非回復；baseline 見 #3 |
| 10 | Procedure ↔ ER 1:1、ER 可觀測、無情態、涵蓋完整結果 | 符 | **3:3**（§五）；三項 ER 皆為可讀之狀態／訊號／畫面 |
| 11 | 無 FP／FF；supported 配負向 | 符 | 其負向即 **#4**（本輪補列） |
| 12 | 追溯 Req/SWRA、不擴入 sibling、無捏造資料 | 符 | `leaf_id = SWE1-DM-004`；值皆有出處（§3.1）；**亮度值未給故不寫** |
| 13 | Design Method 於步驟定稿後指派 | 符 | 步驟定稿後指派 `狀態轉換`（跨 non-Hot → Hot） |
| 14 | 四欄各行無行尾句號 | 符 | 機器檢查 0（§五） |
| 15 | UI 標籤用 `"…"` 非 `[…]` | 符 | `"Screen is Hot. Display brightness has been reduced."`；四欄內方括號 0（§五） |
| 16 | `specification_reference` 列出所有直接驗證之節 | 符 | `{4820282}`（DISP_HOT 通知，ER 2）＋`{4820289}`（門檻與 RVC 前提，PC／step 1） |
| 17 | 來源規格勝過索引匯出；門檻為 spec 具體值 | 符 | 門檻取 CFTS 本文而非 SYS2 匯出（SYS2 r30–r34 無溫度值）；`degrees C` 依 `{4820289}` 之寫法 |

### 4.2 #4（`SWE1-DM-004` 邊界負向）

| # | 項 | 判定 | 依據 |
|---|---|---|---|
| 1 | Test Set | 符 | 同 #1 |
| 2 | tc_title | 符 | **10 字**；sibling token `Temperature at 85 degrees C`；與 #1／#3 皆相異（§五） |
| 3 | PC | 符 | `below 85 degrees C` 為 `{4820289}` 之 non-Hot 側；RVC 項同 #1 |
| 4 | Input Test Data | 符 | `NA` |
| 5 | 步驟／禁用動詞／Final Step | 符 | `Raise`／`Read`／`Read`；lint A 檢查 0 |
| 6 | 步驟長度與意圖層級 | 符 | 三步皆單一動作；step 2／3 為 record 型（不預判結果） |
| 7 | setup 片語 | NA | 同 #1 |
| 8 | CLI | NA | 無 |
| 9 | baseline | NA | 本條驗「不發生」，前後同態 |
| 10 | 1:1、可觀測、無情態 | 符 | **3:3**（§五） |
| 11 | 無 FP／FF；supported 配負向 | 符 | **本條即 #1 之負向**；`split_flag = True`，`split_reason` 記 §8.3 boundary 軸 |
| 12 | 追溯、無捏造 | 符 | `85` 為 spec 明載之邊界（`<= 85` 側），非推論 |
| 13 | Design Method 後指派 | 符 | `邊界值分析 (BVA)` |
| 14 | 行尾句號 | 符 | 0（§五） |
| 15 | UI 標籤 | NA | 本條 ER 為「無 popup」，不含 UI 標籤；四欄內方括號 0 |
| 16 | `specification_reference` | 符 | 僅 `{4820289}` —— 該邊界之唯一出處 |
| 17 | 門檻為 spec 具體值 | 符 | `> 85` / `<= 85` 逐字；**ER 2 只寫否定，不寫 raw 值**（R-DM48、DR-DM9） |

### 4.3 #3（`SWE1-DM-005` 回復）

| # | 項 | 判定 | 依據 |
|---|---|---|---|
| 1 | Test Set | 符 | 同 #1 |
| 2 | tc_title | 符 | **11 字**；sibling token `Temperature falls back to non-Hot` |
| 3 | PC | 符 | 兩項皆為進入本條前之狀態（Hot、背光已關），非動作（§五） |
| 4 | Input Test Data | 符 | `NA` |
| 5 | 步驟／禁用動詞／Final Step | 符 | `Read`／`Lower`／`Read`／`Touch`；step 4 承載觸控之驗證 |
| 6 | 步驟長度與意圖層級 | 符 | 四步皆單一動作 |
| 7 | setup 片語 | NA | 同 #1 |
| 8 | CLI | NA | 無 |
| 9 | **baseline** | **符** | step 1／ER 1 即 §5.6 之 before 側（回復須有前後對照） |
| 10 | 1:1、可觀測、無情態 | 符 | **4:4**（§五） |
| 11 | 無 FP／FF | 符 | 本條為 #1 之回復側；其負向（未降溫則不回復）屬 DR-DM10 之時序範圍，本輪不寫 |
| 12 | 追溯、無捏造 | 符 | 三條出處俱在；**未寫 `[DISP_ON]` 之 raw 值**（DR-DM9） |
| 13 | Design Method 後指派 | 符 | `狀態轉換`（Hot → non-Hot） |
| 14 | 行尾句號 | 符 | 0（§五） |
| 15 | UI 標籤 | NA | 無 UI 標籤 |
| 16 | `specification_reference` | 符 | `{4820287}`（DCSD 送 `[DISP_ON]`）＋`{4820288}`（HU 恢復）＋`{4820290}`（背光與觸控）—— 三者皆為本條步驟直接驗證者 |
| 17 | 來源規格勝過索引匯出 | 符 | `85 deg C` 依 `{4820290}` 之逐字寫法（**與 #1／#4 之 `degrees C` 不同係規格自身不一致，本層不統一**） |

### 4.4 三條共通之「未取」

| 項 | 未取之物 | 理由 |
|---|---|---|
| `estimated_test_time` | 空 | 036 母本 B 欄「辨識但不寫入」（`feature.yaml` 註記） |
| `vehicle_models` | 空 | 同上，Q 欄 |
| `remarks` | 空 | 無須註記者 |
| `tc_id` | `null` | 編號屬 036 母本，未寫回 |
| ER 中之 raw 值（`[DISP_OFF]`／`[DISP_ON]`） | 未寫 | R-DM48；DR-DM9 未結 |
| 亮度降低之數值 | 未寫 | 規格未給（canon §8.4.1） |

---

## 五、`lint036.py` 全文輸出（整批，附母體）

### 5.1 母體與方法

| 項 | 值 |
|---|---|
| 受檢母體 | `features/display/generated/pilot-01.json` 之 `tcs`，**3 筆** |
| 受檢方式 | 三筆寫入 036 母本之**拋棄式複本**（scratchpad），對該複本執行 lint |
| profile | `display`（P 採 R-1 v3；另跑 Q／R／T） |
| 036 母本 sha256（前） | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| 036 母本 sha256（後） | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` |
| 寫回母本 | **否**（`write_back.written = false`） |

**母本前後同 SHA** —— lint 之受檢對象是複本，母本未被觸碰。

### 5.2 輸出全文

```text
# lint036 報告：lint_scratch.xlsx

- 來源：`/private/tmp/claude-501/-Users-peihe-Work-Projects-TC-Generator/e90244b2-6851-4dfb-8775-8cb1bd4f77d3/scratchpad/lint_scratch.xlsx`（唯讀）
- 資料列數：3
- sheet：`Test Case Specification 測試用例規範`（header 第 9 列）
- L 閾值：50 tokens
- profile：`display`（P 採 R-1 v3；另跑 Q／R／T）

## 違規統計

計數口徑：**行計為主**（違規記錄數，粒度見「粒度」欄），**附列計**（涉及之相異資料列數）。兩者不可互相加總。

| 檢查 | 項目 | 行計 | 列計 | 粒度 | 校準 |
| --- | --- | ---: | ---: | --- | --- |
| A | 禁用動詞 (proc) | 0 | 0 | 每次命中 | 已校準 |
| B | ER 情態詞 (er) | 0 | 0 | 每次命中 | 已校準 |
| C | hedge (test_item 括號下半) | 0 | 0 | 每次命中 | 已校準（R-6b 範圍：Media 錨值 1→0） |
| D | PC 違規 (pre) | 0 | 0 | 每次命中／每編號行 | 已校準 |
| E | proc/er 編號行數不對齊 | 0 | 0 | 每列 | 已校準 |
| F | 方括號佔位 (proc) | 0 | 0 | 每次命中 | 已校準 |
| G | Test Set 空值 | 0 | 0 | 每列 | 已校準（詞彙表外值待接入） |
| H | ER 模糊語 (er) | 0 | 0 | 每次命中 | 已校準 |
| I | test_item 括號下半缺失 | 0 | 0 | 每列 | 已校準 |
| I-sibling | 同 Requirement ID 括號行逐字重複 | 0 | 0 | 每列 | 未校準（M15） |
| J | 行首大寫 | 0 | 0 | 每行 | 已校準（行計口徑） |
| K | CJK 字元 | 0 | 0 | 每列每欄 | 已校準（分級待 R-5） |
| L | test_item 上半過長 (>50 tokens) | 0 | 0 | 每列 | 已校準（閾值待 R-3） |
| M | 空欄三態 | 0 | 0 | 每列每欄 | 已校準 |
| N | 行尾多餘句號 | 0 | 0 | 每行 | 已校準 |
| P | 訊號寫法不合 R-1 v3 | 0 | 0 | 每次命中 | 未校準（R-1 v3，21 包改寫；profile 專屬） |
| Q | 不可見字元（NBSP／全形空格／行尾空白） | 0 | 0 | 每行每欄 | 未校準（R-10(a)，21 包新增） |
| R | Pre-Condition 版面（未編號行／多條件並列） | 0 | 0 | 每行 | 未校準（R-9(a)，21 包新增） |
| T | PENDING 說明非英文 | 0 | 0 | 每次命中 | 未校準（R-14，21 包新增） |
| U | PENDING 佔位（四欄全掃，含 ER 側） | 0 | 0 | 每次命中 | 計數用（A-PM16：ER 側原不受任何檢查覆蓋） |

**總計：行計 0**（列計不加總——同一列可觸發多項檢查）

## 明細

```

**二十項檢查行計皆 0；「明細」節為空。**
`I-sibling`（同 Requirement ID 括號行逐字重複）為 0 一項須具名：
#1 與 #4 同為 `SWE1-DM-004`，其 test_item 括號下半分別為
`(Warning stage on crossing the Hot threshold — …)` 與
`(Boundary at the Hot threshold — 85 degrees C is defined as non-Hot, …)`
—— **非逐字重複**，故 0 為實測而非母體為空所致。

### 5.3 canon 側之機器檢查（lint 未涵蓋者）

```text
population: features/display/generated/pilot-01.json, tcs = 3

--- stop condition 54: unresolved value labels in expected_result ---
  hits = 0

--- stop condition 55: action verbs in pre_conditions ---
  hits = 0

--- tc_title: word count (canon 4.3: 2-14) and distinctness ---
  TC#1 words=8 :: Hot threshold exceeded → thermal warning popup displayed
  TC#2 words=10 :: Temperature at 85 degrees C → Hot state not entered
  TC#3 words=11 :: Temperature falls back to non-Hot → backlight on and touch enabled
  distinct = 3 of 3

--- test_item upper half token count (lint L threshold 50) ---
  TC#1 tokens=34
  TC#2 tokens=20
  TC#3 tokens=16

--- procedure / expected_result 1:1 (canon 6) ---
  TC#1 proc=3 er=3 match=True
  TC#2 proc=3 er=3 match=True
  TC#3 proc=4 er=4 match=True

--- canon 11: trailing period on any line of the four fields ---
  hits = 0

--- canon 11: square-bracket UI labels in the four fields ---
  hits = 0

--- input_test_data values ---
  TC#1 'NA'
  TC#2 'NA'
  TC#3 'NA'
```

停止條件 54（ER 中未解析之值標籤）與 55（PC 中之動作動詞）**皆 0**。
`tc_title` 三條 8／10／11 字，**3 of 3 相異**。`test_item` 上半
34／20／16 tokens，皆遠低於 L 檢查之 50 閾值。Procedure ↔ ER
**3:3、3:3、4:4**。

### 5.4 綁定檢查（R-G23，產出前執行）

```text
# reference binding check (R-G23)
feature.yaml: /Users/peihe/Work_Projects/TC_Generator/features/display/feature.yaml
entries: 11

| key | file | declared | actual | verdict |
|---|---|---|---|---|
| a03_report | `Display_Management_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx` | `ab3198e81fb21d21…` | `ab3198e81fb21d21…` | MATCH |
| cfts_doc | `R1LR_Atl-H_26PI1.5 Mar Release-Cabin_CFTS_020 ICS and DCSD _20260310-1533.docx` | `8696d1f596e33677…` | `8696d1f596e33677…` | MATCH |
| dbc_b | `PDT27_E2A_R1_BHCAN2.dbc` | `46cb73f3db62ac9f…` | `46cb73f3db62ac9f…` | MATCH |
| dbc_fd | `PDT27_E2A_R1_FDCAN8.dbc` | `2a86c4bf3e670d71…` | `2a86c4bf3e670d71…` | MATCH |
| lid | `Logical Identifiers and CAN Mapping v1_78.xlsx` | `a01e1679c706cd45…` | `a01e1679c706cd45…` | MATCH |
| popup_list | `Pop Up List HMI R1 (26PI).xlsx` | `ff47b7be63e5824c…` | `ff47b7be63e5824c…` | MATCH |
| popup_priority_matrix | `Pop Up List Priority Matrix HMI R1 SR24 1A (May 3 2021).pdf` | `dc078763c67b5238…` | `dc078763c67b5238…` | MATCH |
| proxi | `PROXI_HDCC27_R3_20250424.xlsx` | `e7c2020f01c3d58d…` | `e7c2020f01c3d58d…` | MATCH |
| sys2_export | `SYS2_CFTS_020_DISP_TCH_ICS_20260616_All_HW_System_Accepted & Released.xlsx` | `421c8eef3f5cb01a…` | `421c8eef3f5cb01a…` | MATCH |
| sys3_sysad | `SYS3_CFTS_020_display_FM-WI-FSM-011-A01_System Architectural Design_SYSAD_v1.0.docx` | `be9c97af0211a703…` | `be9c97af0211a703…` | MATCH |
| workbook_master | `FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT STLA Test Case Specification & Result_SWQT_20260817_ext.xlsx` | `6372fb6be02f48dc…` | `6372fb6be02f48dc…` | MATCH |

**11 of 11 match.**
```

本輪之產出用到 `cfts_doc`（§一之逐字）、`popup_list`（`PU0517`／`PU0130`）、
`workbook_master`（lint 複本之來源）三項，皆 MATCH。

---

## 六、未驗項分流（A／B，R-G29）

### A 類 —— 阻斷交付，須先解

| 編號 | 項 | 阻斷什麼 | 索取中 |
|---|---|---|---|
| A1 | **組 A 與組 B 何者為本架構之準** | `SWE1-DM-005` 之關閉側全部 TC | DR-DM10 (a) |
| A2 | `{4820283}` 警示階段之時長／終止準據 | 原 #2；`PU0130` | DR-DM10 (b) |
| A3 | `[DISP_OFF]`／`[DISP_ON]`／`[DISP_NORMAL]` 之 raw 值 | 現行 ER 只驗行為不寫值；007／008 之訊號欄 | DR-DM9 |
| A4 | `popup_priority.tsv`（既有 A1） | `SWE-DM-006` | DR-DM2 |
| A5 | `sysad_allocation.tsv`（既有 A2） | 全 8 leaf 之追溯欄 | DR-DM3 |

> A1／A2 為本輪新增。A4／A5 沿用 `BACKLOG.md` 之既有 A1／A2，
> **編號於 `BACKLOG.md` 內不變**，此處僅為本節之序。

### B 類 —— 不阻斷交付，記明即可

| 編號 | 項 | 為何不阻斷 |
|---|---|---|
| B1 | `{CFTS013-XXX}` 之實際條號 | 其所在條為 `Radio:noSys`，不適用本專案；登記為規格瑕疵（A-DM33），非本批之障礙 |
| B2 | `{CFTS013-967}` 與 DR-DM4 之三號不同 | 同上，出現於 Multi-stage 節 |
| B3 | multi-stage 分級門檻（DR-DM4） | 單級 85 °C 行為可獨立驗；分級為另一組 TC |
| B4 | 亮度降低之數值 | #1 之 ER 只驗 popup 之顯示與停留時間，不驗亮度；缺值不使該 TC 不可執行 |
| B5 | `degrees C` 與 `deg C` 之寫法不一致 | 規格自身之寫法差異；本層逐字沿用，不統一 |
| B6 | DTC `B1429-00` 之 mature／de-mature 時間門檻 | `{4820289}`／`{4820290}` 逐字為 `after the … time thresholds are met`，未給值；**本批之 TC 未驗 DTC**，故不阻斷 |

> B6 為本節之新登記。`{4820289}` 之四項動作中「設 DTC」一項本批未取，
> 理由即在此 —— **未取而非漏取**，故記於 B 而不留白。

---

## 七、建議之 commit 訊息與 pathspec（**未執行**）

```bash
git add \
  features/display/generated/pilot-01.json \
  features/display/ANOMALIES.md \
  features/display/DATA_REQUESTS.md \
  features/display/docs/INDEX.md \
  features/display/docs/handoff/21_pilot01_rev2.md \
  features/display/docs/upstream/21_pilot01_rev2.md
```

```text
feat(display): pilot-01 rev2 — protective shutdown deferred, boundary TC added

- defer the protective-shutdown TC: four verification paths (clause group A,
  group B, the multi-stage clauses and the pop-up list) all fail to give an
  observable criterion separating the warning stage from the OFF stage
- open DR-DM10 (which of the two contradictory clause groups governs, the
  warning-stage duration, and the {CFTS013-XXX} placeholder)
- record A-DM33: 1.11.2.2 carries two mutually exclusive shutdown flows both
  declared applicable to R1H / Atlantis High
- move thermal thresholds into pre_conditions, set input_test_data to NA
- add the boundary negative TC (85 degrees C stays non-Hot per {4820289})
- lint036 --profile display: all twenty checks report zero
```

> **`batches/pilot-01/batch_context.md` 不入 pathspec** ——
> `features/display/.gitignore` 已將 `batches/` 排除。
> 036 母本未變更，亦不入。

---

## 八、本包是否仍有該驗而未驗者 —— 獨立判斷

**有三項。**

1. **`framework.md` 之 Test Set 分群未經本輪複驗。**
   §9 第 1 項判「符」之依據是 `framework.md` 現有之 Layer 2 四組，
   而該四組建於 19 輪、其後未再對照 037。**本輪只驗了「TC 與
   framework 一致」，未驗「framework 與 037 一致」。** 前者為真不蘊涵後者。

2. **`4 (DISP_HOT)` 之 raw 值未於本輪重新解析。**
   該值取自 20 輪之 `signal_resolution.py` 產出。本輪只確認綁定 sha256 未變
   （§5.4），**未重跑解析鏈**。綁定未變則解析結果應同 —— 但「應同」是推論，
   不是量測。

3. **#4 之「No popup is shown」無正面出處。**
   `{4820289}` 只說越過門檻時做四件事，**未說未越過門檻時不做**。
   ER 3 之「無 popup」係自「觸發條件未成立」推得，屬合理推論而非逐字。
   本層判其可寫（否則一切負向條皆不可寫），**但記明它與 ER 1／ER 2 之
   證據強度不同** —— 後兩者有逐字支撐，ER 3 沒有。

> 第 3 項是本包最接近「越界」之一處。記明而不移除，因為
> §9 第 11 項要求 supported 配負向；移除它會使 #1 缺負向而違反該項。
> **兩者不可兼得時，選擇留下並揭露。**
