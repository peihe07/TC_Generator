# 上繳包 36 —— 反向涵蓋、涵蓋表之程式化、A-PMH30 定案與 batch 5

- 日期：2026-08-25
- 下放包：[handoff/36_batch5.md](../handoff/36_batch5.md)
- **零寫回工作簿**

---

## 0. 摘要

| 步驟 | 結果 |
|---|---|
| 1 抄錄 | R-PMH136～138 **3/3 逐字相符** |
| 2 `-016` 補具名 | 三結果不拆之依據（§5.7）＋ §8.2.2 不觸發之理由已入 `reasoning` |
| 3 涵蓋表程式化 | `desc_coverage.py` 已建；**其首跑即查出我自己寫錯之一筆**；**must-hit 曾偽陽，已改真** |
| **4 反向涵蓋首跑** | **⚠ 停止條件 7 觸發 —— `無依據` 1 處（`-004` ER3），未自行改** |
| 5 `-003` 之修正 | ER4 補斷言「逾時等同 Accept」，4:4 |
| 6 A-PMH30 揭露登記 | 二例入「已知未決清單」之一節 |
| 7 batch 5 | **10 條 TC 自 10 leaf**，lint **32/32**；**`-040` 之 PC 含 `Gear is not in Reverse`** → 停止條件 9 未觸發 |
| 停止條件 8 | **未觸發** —— 程式化結果與 35 包人讀表逐列相符（§3.3） |

---

## 1. 條文抄錄核對表

| 條號 | 主旨 | 字數 | handoff SHA256 | RULINGS **讀回** | 命中 | 相符 |
|---|---|---|---|---|---|---|
| R-PMH136 | 反向涵蓋 | 433 | `0c48178345281323` | `0c48178345281323` | 1 | ✅ |
| R-PMH137 | 037 自身重複時之涵蓋認定 | 697 | `32cb7496eddb0e80` | `32cb7496eddb0e80` | 1 | ✅ |
| R-PMH138 | 第二次解凍 —— 涵蓋表之程式化 | 592 | `bac5e5f237cf40f5` | `bac5e5f237cf40f5` | 1 | ✅ |

---

## 2. 步驟 2 —— `-016` 之補具名（不改內容）

```
⚠ **三個結果不拆之依據（36 包 §二，canon §5.7）** —— 本條斷言三事：維持喚醒 <= 2.5 分（ER6）、60 秒後 popup 關閉（ER4）、無其他 popup 則 radio 關機（ER5）。**三者為同一觸發（IGN OFF ＋ 有 popup 待顯示 ＋ 使用者不互動）之連續後果**，屬同一驗證單位，依 §5.7 不拆。**§8.2.2 之壓力測試於此不觸發** —— 該條所禁者為**兩個獨立分支**之部分失效落在同一判定上；**本處三者為一條時序鏈上之三點**，其前一點不成立則後一點無從觀測，**非獨立**。
```

---

## 3. 步驟 3 —— `desc_coverage.py`（R-PMH138 之解凍）

### 3.1 四項要求之實作

| 要求 | 實作 |
|---|---|
| (a) 切分 | 自 `layer3_sections.tsv` 之 `requirement_description` 讀，`SPLIT` 產生候選；**`SPLIT_REVIEW` 為人讀覆寫之處，現為空** —— **其空值為複核之結果，非未做**（已於檔內具名） |
| (b) 正向 | `FORWARD`：55 項，`未涵蓋` 者依 **R-PMH137** 分 `未涵蓋-重複`／`未涵蓋-部分` |
| (c) 反向 | `REVERSE`：144 項，含第三類 **`測試執行`**（R-PMH97 之二分，**不需 DESC 依據**） |
| (d) must-hit | 二項，見 §3.4 |

**程式所驗者**：判定之**存在**、其**可解析**、其所指之 ER **確實存在**。
**不驗其正確** —— 該限度已列於 `LIMITS`。

### 3.2 ⚠ 其首跑即查出我自己寫錯之一筆

```
⚠ SWE1-HMI-PM-010|1 —— 所指之 `-036` ER3 不存在（該條僅 2 條 ER）
```

**我在人讀表裡把 `-036` 之涵蓋寫成 ER3，而該條只有 2 條 ER。**
**35 包之人讀表沒有攔到它，因為人讀表不會回頭去數 ER。** 已改為 ER2。

### 3.3 與 35 包人讀表之逐列比對（停止條件 8）

| 項 | 35 包人讀 | 36 包程式 |
|---|---|---|
| 斷言數 | 42（30 leaf） | **55（40 leaf）** —— 其差為 batch 5 之 10 leaf／13 斷言 |
| 未涵蓋 | 2（`-001-01` A1、`-003` A2） | **3** —— 前二者相同，**第三者為 `-012` A3**（告別音跨螢幕同步） |
| 差異之判斷 | —— | **以程式為準** |

**第三者之差異須具名**：35 包之人讀表將 `-012` A3 標為
「`-009` ER4（**只涵蓋啟動音側**）」並於註記載「告別音側未涵蓋」——
**其於「涵蓋」欄記為已涵蓋，於「註」欄記為未涵蓋**。
**程式不容許此一兩可**，故改記 `未涵蓋-部分`。
**以程式為準** —— 其為同一事實之較嚴表述，非新發現。

**除此之外逐列相符 → 停止條件 8 未觸發。**

### 3.4 ⚠ must-hit 錨點 (1) 曾偽陽，已改真

```
=== R-PMH138(d) —— 兩項錨點 ===

  (0) 現況：正向不可解析 0、反向無依據 1  ← **現況之 1 處無依據為實測所得（`-004` ER3），非錨點**
  (1) 刪去 `-016` 之 ER4 → 正向新增一筆且指名其 leaf：True   [('SWE1-HMI-PM-018-01|2', '所指之 `-016` ER4 不存在（該條僅 3 條 ER）'), ('SWE1-HMI-PM-018-01|3', '所指之 `-016` ER5 不存在（該條僅 3 條 ER）')]
  (2) 於 `-035` 增一條 DESC 所無之 ER → 反向報無依據：True   （1 → 2）

============================================================
錨點 (1) True；錨點 (2) True

```

**原判準為「輸出中含 `016` 或 `ER4`」** —— 而現況本就有一筆不可解析
（§3.2 之 `-036` ER3 筆誤），**其使錨點在未攔到任何東西時亦報 `True`**。

**改為**：須較基準線**新增**，且**每一新增之筆須同時指名 `-016` 所掛之 leaf 與 `-016`**。

> **一個錨點在它所要攔的東西之外另有一個常在之失敗時，它會一直是綠的。**
> 這與 31 包之 `record`／`read` 為同一形態：**判準太寬，而其寬處剛好被別的東西填滿。**

---

## 4. ⚠ 步驟 4 —— 反向涵蓋首跑：**`無依據` 1 處，停止條件 7 觸發**

```
=== 正向：DESC 之每一斷言 × 其 leaf 之 TC 集合（R-PMH133）===
  leaf = **40**；斷言 = **55**；**未涵蓋 = 3**；**未判定／不可解析 = 0**

  SWE1-HMI-PM-001-01 A1  **未涵蓋-重複**  `-028` ER1（掛 `SWE1-HMI-PM-006-01`）—— R-PMH137
      When driver door is closed, the system plays a 3-second startup animation.
  SWE1-HMI-PM-003 A2  **未涵蓋-重複**  `-004` ER2（掛 `SWE1-HMI-PM-001-05`）—— R-PMH137
      No timeout is provided for Maserati applications, see CFTS009.
  SWE1-HMI-PM-012 A3  **未涵蓋-部分**  `-009` ER4 只涵蓋啟動音側；**告別音側未涵蓋（A-PMH23，`DR-PMH8` Q3）**
      Sounds will sync amongst all supported vehicle displays.

=== 反向：TC 之每一 ER 斷言 × 其 leaf 之 DESC（R-PMH136）===
  ER 斷言 = **144**；**無依據 = 1**

  **-004 ER3** —— **其依據在他 leaf** —— `-001-05` 之 DESC 只載「無逾時、須手動按 Accept」，**未載按下之後之結果**；`The last mode screen is displayed` 之依據在 `-001-04` 之 DESC（`press Accept to go directly to last mode screen`）。**其形態為 canon §8.4.2 之範圍捏造。**
      逐字：The disclaimer screen is removed and the last mode screen is displayed

=== 本檢查未涵蓋之範圍（R-PMH52）===
  - **切分仍以句末標點為候選** —— 一句內含二斷言者（如 `-009-01` 之三個後果）計為一項；其是否應再切屬人讀，本檔只承載其結果
  - **`FORWARD`／`REVERSE` 之值為人讀所寫** —— 本檔驗其存在與可解析，**不驗其正確**
  - **反向之 `測試執行` 類不需 DESC 依據**（R-PMH97 之二分）—— 其為測試員之行為或資料蒐集；**該分類本身為人讀，錯分即漏檢**
  - **未涵蓋-重複 之認定依 R-PMH137** —— 其行為由他 leaf 之 TC 涵蓋；**本檔不驗該他 leaf 之 TC 是否真涵蓋它**
  **以上各項本檢查一律不看** —— 其全綠不含關於該等項之任何資訊。
```

### 4.1 `-004` ER3

| | |
|---|---|
| 逐字 | `The disclaimer screen is removed and the last mode screen is displayed` |
| 其 leaf | `SWE1-HMI-PM-001-05` |
| 該 leaf 之 DESC | `Exception: For Maserati applications, the system provides no timeout (per CFTS009); the user must manually press Accept.` |
| 問題 | **DESC 只載「無逾時、須手動按 Accept」，未載按下之後之結果** |
| 該結果之依據 | **`-001-04`** 之 DESC：`press Accept to go directly to last mode screen` |
| 形態 | **canon §8.4.2 之範圍捏造**（斷言了他 leaf 所有之內容） |

**我未自行改**（下放包步驟 4 逐字：「發現任一 `無依據` 即停並上呈」）。

**其修正有二路，皆須裁**：
(甲) **刪去 ER3** —— 則 `-004` 只驗「無逾時」而不驗其離開路徑；
(乙) **維持並承認其跨 leaf** —— 則 R-PMH136 須加一款（「其依據在他 leaf 而該他 leaf 為
其上位或例外之本體者，不計為捏造」）。

> ⚠ **`-004` 之 DESC 以 `Exception:` 起首** —— 其在文義上就是 `-001-04` 之例外，
> **故 (乙) 有其道理**；**惟 R-PMH136 現行條文不容許之。**

### 4.2 反向之其餘 143 項

| 類 | 數 |
|---|---|
| 有 DESC 依據（`A1`／`A2`／`A3`） | **117** |
| **`測試執行`**（R-PMH97 之二分，不需依據） | **26** |
| **`無依據`** | **1** |

---

## 5. 步驟 5 —— `-003` 之修正（R-PMH133；依 R-PMH135 不計輪數）

```
1. Read the screen and record that the disclaimer screen is displayed
2. Press no hard key and no "Accept" button until the screen changes
3. Read the screen and record the screen reached after the timeout
4. Check that the timeout reached the same screen as pressing "Accept"
---
1. The disclaimer screen is displayed with the "Accept" button
2. No user input is given while the disclaimer screen times out
3. The last mode screen is displayed
4. The timeout has the same effect as pressing "Accept"
```

其 `reasoning` 已記明：該語義之來源為 037 之 DESC，
**其於 PDF `SU1.)` 中不存在**；**13 包當時之不斷言合於當時之判準**。

---

## 6. 步驟 6 —— A-PMH30 二例之交付揭露登記

依 R-PMH137 ＋ R-PMH132(b)，二例入「已知未決清單」之一節，
其節名為「**已被驗證，其未涵蓋僅為追溯之位置**」：

| 例 | 其行為由何者涵蓋 |
|---|---|
| `SWE1-HMI-PM-001-01` A1（門關閉 → 3 秒動畫） | `-028` ER1（掛 `SWE1-HMI-PM-006-01`） |
| `SWE1-HMI-PM-003` A2（Maserati 無逾時） | `-004` ER2（掛 `SWE1-HMI-PM-001-05`） |

**撰寫要求**：載明「該行為已被驗證」，**使讀者不致將 `未涵蓋` 讀成 `未驗證`**。

---

## 7. 步驟 7 —— batch 5（10 條／10 leaf）

### 7.1 拘束之逐項落實

| 拘束 | 落實 |
|---|---|
| (a) `source_clause` 取自 PDF | 十條 origin 為 `spec_pdf p10`（8 條）／`spec_pdf p11`（2 條） |
| (b) 產出後即跑涵蓋表 | **已跑** —— batch 5 之 13 斷言全數入 §4 之表，**未涵蓋 0、無依據 0** |
| (c) 限定逐條具名 | 本批僅 **1 條有限定**（`-047`，其所對之 ER 已具名）；**其餘九條逐條導出之結果為「無素材與其取相反值」，故無限定** |
| (d) **`-040` 之 PC 含 `Gear is not in Reverse`** | ✅ **停止條件 9 未觸發**（實測其 pre_conditions 第 2 項） |

### 7.2 本批無一 leaf 須拆，其理由

`-038`（`Screen Off` 與 `HU Power button`）、`-041`（`ACC or RUN`）、
`-045`（`SOS` 與 `ASSIST`）、`-044`（`soft control or hard control`）
**皆為同一等價類之多個成員（規格以 `and`／`or` 並列而給同一結果）**，
**非兩個獨立分支**，故不依 §8.2.2 拆分 —— **其與 batch 4 之「門被移除」條同一處置**。

`-039`（PITA5 之三後果）與 `-040`（PITA6 之二後果）**依 §5.7 不拆**（同一觸發之連續後果）。

### 7.3 一條 P0 —— 本 feature 至今唯一

`-045`（SOS／ASSIST 使電源回復）判 **P0**：其為緊急呼叫之電源回復路徑，
**失效直接影響求救**。其與其餘各條之 P1 **不同級而不矛盾**（R-PMH59）。

### 7.4 十條之全文

#### `NR1L-DisclaimerScreen-038` — Screen Off and power button selections are ignored during the backup camera

- **leaf**：`SWE1-HMI-PM-019`　**Test Set**：`Power Off Behavior`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`PITA4: Screen Off and HU Power button selections shall be ignored while backup cam is being shown.`
- **軸**：等價類：倒車影像中之被忽略輸入（對 -039 之倒車影像顯示本身）

**pre_conditions**

```
1. The backup camera is being shown on the screen
2. The head unit is on
```

**test_procedure**

```
1. Press the Screen Off hard key and read the screen
2. Press the HU Power button and read the screen
3. Check that neither selection changed the screen
```

**expected_result**

```
1. The screen still shows the backup camera after the Screen Off key press
2. The screen still shows the backup camera after the HU Power button press
3. Neither selection had any effect
```

#### `NR1L-DisclaimerScreen-039` — Backup camera shows during Power Button Off without cancelling that state

- **leaf**：`SWE1-HMI-PM-020`　**Test Set**：`Power Off Behavior`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`PITA5: If backup cam needs to be shown during Power Button OFF state, then it shall be shown. This shall not cancel Power Button Off state. Once the backup cam is dismissed, the Power Button Off state shall be reinstated.`
- **軸**：謂詞：倒車影像期間之電源狀態（對 -038 之輸入被忽略）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. The vehicle is able to request the backup camera
```

**test_procedure**

```
1. Put the vehicle into reverse so that the backup camera is requested
2. Read the screen and record the power state
3. Dismiss the backup camera and read the power state
4. Check that the Power Button Off state was reinstated
```

**expected_result**

```
1. The backup camera is shown
2. The radio remains in Power Button Off state while the camera is shown
3. The backup camera is dismissed
4. The Power Button Off state is reinstated
```

#### `NR1L-DisclaimerScreen-040` — HVAC pop-ups display temporarily during Power Button Off state

- **leaf**：`SWE1-HMI-PM-021`　**Test Set**：`Power Off Behavior`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`PITA6: HVAC pop-ups shall be temporarily displayed during Power Button Off state. Any interactions with the popups shall not cancel Power Button Off state.`
- **軸**：謂詞：HVAC popup 於關機狀態（對 -041 之點火轉換觸發）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. The vehicle gear is not in Reverse
3. The HVAC hard controls are available
```

**test_procedure**

```
1. Adjust an HVAC hard control and read the screen
2. Interact with the pop-up shown and read the power state
3. Check that the Power Button Off state was not cancelled
```

**expected_result**

```
1. An HVAC pop-up is displayed temporarily
2. The radio remains in Power Button Off state after the interaction
3. The Power Button Off state is not cancelled
```

#### `NR1L-DisclaimerScreen-041` — HVAC pop-ups display when the ignition moves from off to ACC or RUN

- **leaf**：`SWE1-HMI-PM-022-01`　**Test Set**：`Power Off Behavior`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`PITA6.1: If radio is in Power Button Off state upon going from ignition in OFF position to ignition in ACC or RUN, HVAC popups shall display on the screen.`
- **軸**：觸發：點火自 OFF 轉 ACC/RUN（對 -040 之 HVAC 硬控操作）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. The ignition is in the OFF position
```

**test_procedure**

```
1. Turn the ignition from OFF to ACC or RUN
2. Check that the HVAC pop-ups are displayed on the screen
```

**expected_result**

```
1. The ignition moves from OFF to ACC or RUN
2. The HVAC pop-ups are displayed on the screen
```

#### `NR1L-DisclaimerScreen-042` — Phone call pop-ups can be displayed over Power Button Off state

- **leaf**：`SWE1-HMI-PM-024-01`　**Test Set**：`Power Off Behavior`　**dm**：功能測試 (Functional based ; no specific technique)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`PITA9: Phone call popups can be displayed over Power Button Off state.`
- **軸**：事件：來電 popup 之顯示（對 -043 之忽略、-044 之通話結束）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. A phone is paired and able to receive a call
```

**test_procedure**

```
1. Place an incoming call to the paired phone
2. Check that the phone call pop-up is displayed over the Power Button Off state
```

**expected_result**

```
1. An incoming call arrives at the paired phone
2. The phone call pop-up is displayed over the Power Button Off state
```

#### `NR1L-DisclaimerScreen-043` — Ignoring a phone call pop-up returns to Power Button Off state

- **leaf**：`SWE1-HMI-PM-024-02`　**Test Set**：`Power Off Behavior`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`Ignoring a Phone call popup returns to the Power Button Off state.`
- **軸**：事件：忽略來電 popup（對 -044 之接聽後通話結束）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. A phone call pop-up is displayed over that state
```

**test_procedure**

```
1. Ignore the phone call pop-up
2. Check that the radio returned to Power Button Off state
```

**expected_result**

```
1. The phone call pop-up is ignored
2. The radio returns to Power Button Off state
```

#### `NR1L-DisclaimerScreen-044` — Answered call returns to Power Off state when it ends without screen change

- **leaf**：`SWE1-HMI-PM-024-03`　**Test Set**：`Power Off Behavior`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`If a call is answered either by soft control or hard control and the user does not change screens during the phone call, the head unit will return to Power Off State upon the call ending.`
- **軸**：事件：接聽後通話結束（對 -043 之忽略）

**pre_conditions**

```
1. The radio is in Power Button Off state
2. A phone call pop-up is displayed over that state
```

**test_procedure**

```
1. Answer the call by soft control and do not change screens
2. End the call and read the power state
3. Check that the head unit returned to Power Off state
```

**expected_result**

```
1. The call is answered and no screen is changed during the call
2. The call ends
3. The head unit returns to Power Off state
```

#### `NR1L-DisclaimerScreen-045` — SOS and ASSIST can turn the head unit power back on

- **leaf**：`SWE1-HMI-PM-025`　**Test Set**：`Power Off Behavior`　**dm**：等價劃分 (Equivalence Partitioning, EP)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p10`）：`PITA10: SOS and ASSIST can turn head unit power back on.`
- **軸**：等價類：緊急呼叫鍵之電源回復（本批唯一之 P0）

**pre_conditions**

```
1. The head unit power is off
2. The SOS and ASSIST controls are available in the vehicle
```

**test_procedure**

```
1. Press the SOS control and read the head unit power state
2. Return the head unit to power off and press the ASSIST control
3. Check that each control turned the head unit power back on
```

**expected_result**

```
1. The head unit power turns back on after the SOS control is pressed
2. The head unit power turns back on after the ASSIST control is pressed
3. Both controls turn the head unit power back on
```

#### `NR1L-DisclaimerScreen-046` — Off Road Plus press does not wake the head unit when already in Off Road

- **leaf**：`SWE1-HMI-PM-027`　**Test Set**：`Off Road Plus`　**dm**：狀態轉換 (State Transition Testing)　**pri**：P1　**限定**：無
- **`source_clause`**（`spec_pdf p11`）：`OFF1.) If vehicle is in Off Road state prior to pressing Off Road+ hard control head unit will not initiate wake up (Power Button On).`
- **軸**：事件：Off Road 狀態下之 Off Road+ 按壓（對 -047 之 app 啟動）

**pre_conditions**

```
1. The vehicle is in Off Road state
2. The head unit is in Power Button Off state
```

**test_procedure**

```
1. Press the Off Road Plus hard control
2. Check that the head unit did not initiate wake up
```

**expected_result**

```
1. The Off Road Plus hard control is pressed
2. The head unit does not initiate wake up and stays in Power Button Off state
```

#### `NR1L-DisclaimerScreen-047` — Head unit is muted when an app is launched from Power Off state

- **leaf**：`SWE1-HMI-PM-029`　**Test Set**：`Off Road Plus`　**dm**：功能測試 (Functional based ; no specific technique)　**pri**：P1　**限定**：**有**
- **`source_clause`**（`spec_pdf p11`）：`OFF3.)Head unit is muted when launching app from Power Off State.`
- **軸**：事件：自關機狀態啟動 app（對 -046 之 Off Road+ 按壓）

**pre_conditions**

```
1. The head unit is in Power Off state
2. An app that can be launched from that state is available
```

**test_procedure**

```
1. Do not press the Mute key
2. Launch the app from Power Off state
3. Read the head unit audio state
4. Check that the head unit is muted
```

**expected_result**

```
1. No Mute key press occurs
2. The app is launched from Power Off state
3. The head unit audio state is recorded
4. The head unit is muted
```


---

## 8. 五批 lint ＋ 檢查總表 ＋ **解凍已恢復之聲明**

```
batch01 32/32   batch02 32/32   batch03 32/32   batch04 32/32   batch05 32/32
--limit-must-hit 通過   --final-step-must-hit 通過
verdict_form 0 failure  check_granularity --self-test 通過
desc_coverage exit 1（反向無依據 1，為設計）  desc_coverage --must-hit 通過
```

**新增檢查程式 1**（`desc_coverage.py`）—— **其為 R-PMH138 所授權之第二次解凍**，
範圍嚴格限於「涵蓋表之程式化承載」，**未及其餘**。

> **聲明**：R-PMH138 之解凍**用畢**，自本包結束起 **apparatus 恢復凍結**；
> **追溯維度維持封閉為三項**（R-PMH134）。

---

## 9. 未結 DR —— **4 筆**

| DR | 狀態 | 阻斷 |
|---|---|---|
| `DR-PMH5` | `SENT` 2026-08-25 | `-023` 停手 |
| `DR-PMH6` | `SENT` 2026-08-25 | 否（`-040` 之倒車缺口已入其 Q1） |
| `DR-PMH7` | `SENT` 2026-08-25 | 矩陣四列 ＋ L160 |
| `DR-PMH8` | **`DRAFT`（8 問）** | 否 —— **其載 R-PMH112 之更正，未發出期間該不符持續存在** |

---

## 10. 本包是否仍有該驗而未驗者 —— **有**

1. **反向表之 144 項中，117 項之依據是機器以詞重疊挑的，我只人讀了 25 項低重疊者。**
   **高重疊不等於正確** —— 一條 ER 可能與某斷言用詞相近而其實驗的是另一件事。
   **其偽陰未量測。**
2. **`測試執行` 之 26 項是我用一條正規式分出來的。** 分錯即該項永遠不會被要求 DESC 依據
   —— **其為本檔之最大單一漏檢面，已列於 `LIMITS`。**
3. **batch 5 之十條未經任何人讀覆核。** 前四批之中四批皆在 lint 全綠後被判產出面須改。
   **R-PMH120 給每批二輪。**
4. **`-042`／`-045` 之 `can` 措詞（許可式 vs 強制式）我斷言其發生，未開 DR。**
   `DR-PMH8` 已有八問，**我判其不值再增一問 —— 該判斷未經裁定**。
5. **`-044` 之 `hard control` 一路未驗**（其與 soft control 同結果，故未另立條）——
   **與 `-038`／`-045` 之處置一致，惟三者皆是「同結果故不拆」之推定**，
   **規格未言其實作為同一路徑。**
6. **`-039`／`-040` 之三／二後果依 §5.7 不拆，而其 pass/fail 之歸因未經 §8.2.2 之壓力測試逐條書面化**
   —— 我於 `-039` 寫了理由，**`-040` 只寫了 R-PMH80(a) 之限定而未寫不拆之理由**。

---

## 11. 建議之 commit（**未執行**）

```
feat(power_moding): package 36 — reverse coverage, desc_coverage.py, A-PMH30 closed, batch 5
```

pathspec（**13 路徑**）：

```
features/power_moding/DECISIONS.md
features/power_moding/RULINGS.md
features/power_moding/docs/INDEX.md
features/power_moding/docs/handoff/36_batch5.md
features/power_moding/docs/upstream/36_batch5.md
features/power_moding/generated/batch01.json
features/power_moding/generated/batch03.json
features/power_moding/generated/batch05.json
features/power_moding/scripts/check_table.py
features/power_moding/scripts/desc_coverage.py
features/power_moding/scripts/gen_batch01.py
features/power_moding/scripts/gen_batch03.py
features/power_moding/scripts/gen_batch05.py
```

### 11.1 R-G6 之揭露表

| 項 | 揭露 |
|---|---|
| 寫回工作簿 | **無** |
| **停止條件 7** | **觸發** —— 反向 `無依據` 1 處，**未自行改**，二路皆須裁 |
| 停止條件 8／9 | 未觸發（人讀表逐列相符；`-040` 之 PC 含 `Gear is not in Reverse`） |
| apparatus | **第二次解凍已用畢並恢復凍結**；新增程式 **1**（其為授權範圍內），新增 lint 檢查項 **0** |
| 自查 | **人讀表之一筆筆誤由程式攔下**；**must-hit 錨點 (1) 曾偽陽，已改真** |
| DR 之發出 | **執行層未發出任何一封**；`DR-PMH8` 維持 `DRAFT`（8 問） |
| 他 feature／`docs/runtime/`／`new_feature.py` | **未觸** |
