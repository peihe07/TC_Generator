# 上繳包 08 —— T16a–c 修訂、十七項自檢、R-DD11~13、DR-DD7

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`10_pilot_review.md` §八（T16a–c、T-抄、T-登）
- 本輪**未改 profile**（§2.5／§2.6 由分析層自辦）、**未寫回工作簿、未執行 git**
- 共用路徑：**未寫入一字**

> **本輪最重要的一句**：自檢從 13 檢（下放包 §6.2 清單）換成
> **IN §9 十七項為骨幹 ＋ 追加項，共 22 檢**。
> 上一輪不是「檢得不夠仔細」，是**檢的清單本身少了六個問題**——
> 換骨幹之後，同一份 TC 就被問出了 D1／D2／D3／D5／D6。

---

## 1. T16a —— 六項缺陷之修訂，逐處標所依 IN 條文

### 1.1 修訂總表

| # | 缺陷 | 所依 IN 條文（逐字依據）| 修訂 | 影響 |
|---|---|---|---|---|
| **D1** | PC 首行含系統預設＋待測前提 | **§4.4 Forbidden**：`system defaults (HU is powered on.)`／`feature under test as premise (Dealer Mode is accessible.)` | 刪除該行 | 4 TC |
| **D1'** | PC3 為 step 可控狀態 | **§4.4 Forbidden**：`step-controlled state`；**§4.4 Self-test**：`requires do / check / confirm → NOT a Pre-Condition` | 刪除，導航併入 Procedure | 4 TC |
| **D2** | ITD 與 Procedure 重複同值 | **§4.5**：`Do not duplicate the same value across Pre-Condition, Input Test Data, and Procedure`；SWC 基準 `Input Test Data 以 NA 為常態` | 一律 `NA` | 4 TC |
| **D3** | 禁用動詞 `check whether` | **§5.1 Forbidden verbs**；**§5.5**：`Include ACTION + check target` | 四則末步一律 `check that …` | 4 TC |
| **D4** | design_method 未依首合原則 | **§12 first-match**：`State A → State B` 序在 `Scenario` 前；tie-break `Scenario = ≥3 steps crossing features` | `-001` 改狀態轉換 | 1 TC |
| **D5** | `test_item` 方括號 | **不改 TC**（改即違 R-S4 逐字）；profile §2.5 已補 R-DD12 | 僅改自檢判準 | 0 TC |
| **D6** | ER 含推導與重複斷言 | **§6**：ER observable；**§5.5**：Final Step owns validation | `-001` ER1 去推導、ER2 改述步驟直接結果 | 2 TC（見 1.3）|
| **§5.2** | 步驟長度逾限（本輪自檢新查出）| **§5.2 A**：`Target length: ≤ 12 words`；**B**：`≤ 18 words` | 六個步驟改寫 | 4 TC |

### 1.2 D1 —— PC3 之逐則覆核（下放包 §二 D1「併查」所命）

| leaf | 原 PC3 | 判 | 依據 | 處置 |
|---|---|---|---|---|
| `-009` | `The Phone screen is displayed and "Pairing (1st time)" is offered on it` | **step 可控** | §4.4 Self-test：進入該畫面須 *do* | 刪；導航併入 Procedure 步驟 2 `Open the Phone screen and select …` |
| `-010` | `The Phone screen is displayed and "Pairing (1st time)" can be started` | **step 可控且與步驟 1 重複** | 同上；步驟 1 之 baseline 正是在驗「可啟動」 | 刪 |
| `-011` | `The menu-bar configuration view … can be opened` | **step 可控** | 同上；步驟 1 即 `Open …` | 刪 |
| `-012` | 同 `-011` | **step 可控** | 同上 | 刪 |

**PC2 留**（下放包所命），四則皆餘一項：

```
1. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)
```

**§8.5 之決定測試**（「是 TC 直接驗證之觸發條件，還是隱含環境穩定前提？」）：

- `-011`：**是觸發條件** —— 037 AC1 逐字 `the state becomes RESTRICTED while
  the user is using a restricted feature`，其「becomes」蘊含轉換前之未受限態
- `-010`／`-012`：**是觸發條件** —— AC2 所注入之故障即「該訊號停送」，
  故「該訊號正在送」是被移除的那個前提本身
- `-009`：**較弱** —— 其 AC1 未言轉換，僅言在受限態下之存取。
  該行之作用為界定步驟 1 所改變之訊號源（§4.5-1 環境資料）。
  **依下放包「PC2 留」照留，但此為四則中唯一非嚴格觸發條件者，記之。**

### 1.3 D6 —— 修訂範圍比下放包所列多一處

下放包 D6 列 `-001` 之二處。**`-003` 之 ER2 含逐字相同之推導語句**：

```
… and 5.0097 MPH, the first representable step at or above the 5 MPH threshold
```

**一併修**。二則改後皆為：

```
The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]
```

> 只修下放包點名的那一處，會留下一則同病而未修的。**同一判準應施於全體。**

`-001` ER2／ER3 之去重（§5.5 Final Step owns validation）：

| | 修訂前 | 修訂後 |
|---|---|---|
| ER2 | `The "Pairing (1st time)" entry does not act as an available control and the pairing flow does not start` | `The Phone screen is displayed and the "Pairing (1st time)" entry is selected` |
| ER3 | `The pairing flow is not entered and the Phone screen stays as it was before the attempt` | `The pairing flow does not start and the Phone screen stays as it was before the attempt` |

**ER2 現僅述步驟 2 之直接結果，終局判定歸 ER3。**

### 1.4 §5.2 —— 本輪自檢新查出之步驟長度違規

十七項自檢新增第 6 項（§5.2）後，**六個步驟逾限**。逐處：

| leaf | 步 | 原字數 | 修訂 | 現字數 |
|---|---|---|---|---|
| `-009` | 1 | 13 | 去 `and keep the message cycling`，改採 profile §3 之 template 逐字 | **8** |
| `-010` | 1 | 13 | `Start "Pairing (1st time)" from the Phone screen, then leave it` | **11** |
| `-010` | 2 | 16 | 去訊號名重述（訊息名已足以識別）| **11** |
| `-011` | 2 | 15 | 去 `While that view is still open`（步驟順序已蘊含）＋去 `continuously` | **8** |
| `-012` | 1 | 13 | `Open the "Reconfigurable menu bar" configuration view, then leave it` | **10** |
| `-012` | 2 | 16 | 同 `-010` 步驟 2 | **11** |

現行字數（一般步 ≤12／末步 ≤18）：

```
newR1L-DD-001 [8, 9, 13]    newR1L-DD-002 [11, 11, 14]
newR1L-DD-003 [9, 8, 12]    newR1L-DD-004 [10, 11, 13]
```

> `-009` 步驟 1 改後恰為 **profile §3 之寫法 template 逐字**
> （`Send the signal $…$ = <raw> (<km/h>)`）—— 收字數與合 profile 同時達成。

### 1.5 D4 —— §12 首合序之逐則覆核

| leaf | 觸發 | §12 首合命中 | 方法 |
|---|---|---|---|
| `-009` | 車速 0 → 129 跨門檻 | `State A → State B transition` | **狀態轉換**（原為情境，**已改**）|
| `-010` | 停送訊息 → 逾時 | `Simulated fault (disconnect, timeout)` | 基礎故障注入（序在狀態轉換**之前**，不變）|
| `-011` | 使用中跨門檻 | `State A → State B transition` | 狀態轉換（不變）|
| `-012` | 停送訊息 → 逾時 | `Simulated fault` | 基礎故障注入（不變）|

`-009` 原取情境之否定依據（§12 tie-break 逐字）：
`Scenario = ≥3 steps crossing features` —— **本則為單一 feature 之存取嘗試**。

### 1.6 D5 —— 不改 TC

profile §2.5（R-DD12）已由分析層落檔，**例外已啟用**。
**TC 一字未動**；改的是自檢第 15 項之判準（見 §2.3）。

---

## 2. T16b —— 自檢對 IN §9 十七項全跑

### 2.1 骨幹之更換

| | 上一輪 | 本輪 |
|---|---|---|
| 骨幹 | 下放包 §6.2 八項 | **IN §9 十七項** |
| 下放包 §6.2 | 全部 | **附掛於對應之 IN 項下（額外，非全部）** |
| 檢數 | 13 | **22**（17 項 ＋ 5 追加）|
| 結果 | 13 PASS | **20 PASS ／ 2 N/A ／ 0 FAIL** |

### 2.2 十七項對 IN 條文之落點

| IN §9 | 條文 | 本輪狀態 | 上一輪是否問過 |
|---|---|---|---|
| 1 | §4.1／§4.2 Test Set | PASS | 否 |
| 2 | §4.3.1 test_item 兩段式 | PASS | 部分（僅 token 與子串）|
| 3 | **§4.4／§8.5 Pre-Condition** | PASS | **否 → D1 之成因** |
| 4 | **§4.5 Input Test Data** | PASS | **否 → D2 之成因** |
| 5 | **§5.1 禁用動詞／§5.5 Final Step** | PASS | **否 → D3 之成因** |
| 6 | **§5.2 步驟長度** | PASS | **否 → §1.4 六處之成因** |
| 7 | §5.3 標準片語 | **N/A** | 否 |
| 8 | §5.4 CLI 格式 | **N/A** | 否 |
| 9 | §5.6 Baseline | PASS | 否 |
| 10 | §6 ER 1:1／可觀察 | PASS | 部分（僅 1:1）|
| 11 | §7 FP／FF | PASS | 否 |
| 12 | §8.1／§8.2／§8.4 | PASS | 部分（僅 §8.4.2 禁詞）|
| 13 | **§12 Design Method** | PASS | **否 → D4 之成因** |
| 14 | §11 行尾句號 | PASS | 是 |
| 15 | **§11 方括號（含 test_item）** | PASS | **部分 → D5 之成因**（上輪只掃四欄）|
| 16 | §10.7 spec_reference | PASS | 是 |
| 17 | §8.6／§8.7 | PASS | 否 |

**六個「否」欄，恰對應六個缺陷。**

### 2.3 兩處 carve-out 之實作

**R-DD12(c)** —— `test_item` 之方括號**以「是否為 037 逐字」為判準**：

```python
for m in re.finditer(r"\[[^\]]*\]", upper):
    if m.group(0) not in SRC[k][3]:          # 比對 037 c3 原文
        brk.append((tc["tc_id"], "test_item 上半", m.group(0), "非 037 逐字"))
for m in re.finditer(r"\[[^\]]*\]", lowerp):
    brk.append((..., "R-DD12(b)：例外僅及上半"))   # 下半一律禁
```

四則上半之 `[Normal]`／`[Exception]` **經比對確為 037 逐字**，放行；
下半與四欄之方括號**一律禁**，唯 `[ASSUMPTION A-DDn]` 為 R-DD12(b) 所許。

**R-DD11** —— 行尾句號**移除引號段後**再判：

```python
stripped = re.sub(r'"[^"]*"', "", s).rstrip()
if stripped.endswith("."):  ...   # 移除引號後仍以句點結尾者，方為違規
```

`-003` ER3 末字元為 `"`，其內之句點屬 HMI spec p4 原字串 → **合規**。

### 2.4 兩項 N/A 之理由（不得以 N/A 掩蓋未查）

| 項 | 理由 |
|---|---|
| 7（§5.3）| 本 feature **未定義 project-level setup 常數**（`feature.yaml` 無該鍵）—— 無適用對象，非未查 |
| 8（§5.4）| 4 則皆為 HMI 操作與匯流排施加，**無 CLI 步驟**（掃 `$ ` 命中 0）|

### 2.5 三項判斷性檢之依據（非純字串比對，故載明）

- **第 9 項（§5.6 Baseline）**：`-010`／`-012` 由步驟 1 建立 before；
  `-009`／`-011` 之 before **載於 PC**（訊號 0），且其 **ER 不比對已記錄值**，
  故不需記錄步驟。**此為判斷，非量測。**
- **第 11 項（§7）**：FP 之配對義務以「有無列舉式支援項」為前提 ——
  本 4 leaf 無 format／device／protocol 之列舉，**無配對對象**。
- **第 12 項（§8.4.1 造值）**：以「Procedure／ER 內之全部數值 token」為母體，
  對照白名單 `{1,2,3（編號）, 129, 8.0625, 0, 0.0000}`。
  實測母體 `['1','129','2','3','8.0625']`，**逾白名單者 0**。

---

## 3. T16c —— reasoning 之實質同一補記

`newR1L-DD-004` 之 `reasoning` 末段新增（依下放包 §四）：

> **本列與 newR1L-DD-002 之驗證目標實質相同** —— 依 IN §4.6 之等價判準
> （same trigger + outcome + input + verification target）四者皆同，
> 其區別僅在取樣 feature 與追溯 ID，而取樣 feature 係作者所選、非 spec 所定。
> 二列皆保留係追溯要求（每 leaf 須有 TC），
> **不得以取樣 feature 之不同偽稱為不同之驗證目標**；成因見 A-DD7／DR-DD7。

`newR1L-DD-002` 亦加一句互指，使二列可對讀而不必先讀 `-004`。

---

## 4. 修訂後 4 TC 全文

### newR1L-DD-001 —— `SWE1-RA-Driver_Distraction-009`（P0）

> 上半出處：037 Analysis Report r17 c3 (Requirement Description)；模式 `excerpt(Case..Then)`；25/50 token

```json
{
  "tc_id": "newR1L-DD-001",
  "req_id": "SWE1-RA-Driver_Distraction-009",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "Case [Normal]the user attempts to access a restricted feature in the lockout table\nThen DD Service outputs RESTRICTED and HMI prevents access to the feature\n(Access attempt on \"Pairing (1st time)\" with the speed signal held at the lock threshold)",
  "pre_conditions": "1. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Open the Phone screen and select \"Pairing (1st time)\"\n3. Read the Phone screen and check that the pairing flow has not started",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. The Phone screen is displayed and the \"Pairing (1st time)\" entry is selected\n3. The pairing flow does not start and the Phone screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915108",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：速度達上鎖門檻時，Lockout Table 所列之受限 feature 其存取被阻 —— 斷言錨取 profile §2.1 觀察面 A（存取阻擋），取樣 feature 具名為 \"Pairing (1st time)\"。關鍵情境條件：$STATUS_CCAN3.VehicleSpeedVSOSig$ 由 0 送至 raw 129（8.0625 km/h＝5.0097 MPH），該值為 profile §3.1 依 R-DD7(c) 所定之上鎖側第一個可表示格，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 之 AC1 只有一條常態路徑（施加受限狀態 → 存取被阻），無獨立可分之部分失效（IN §8.2.2 未成立）。刻意略過：解鎖方向（raw 77／78）屬 -013／-015，門檻下側 raw 128 之不應鎖屬 BVA 之另一半，本列不擴入（IN §8.2.1）；p7 黃標三項（Player / RSE、Messaging、SRT Options）不取樣，Embedded NAV 系（含 Destination Entry）因僅適用 LATAM 亦不取。設計方法依 IN §12 首合原則取狀態轉換 —— 觸發為車速由 0 跨越門檻之 A→B 轉換，於 Scenario 之前命中；且 §12 tie-break 之 Scenario 判準為「≥3 steps crossing features」，本列為單一 feature 之存取嘗試，不合。"
}
```

### newR1L-DD-002 —— `SWE1-RA-Driver_Distraction-010`（P1）

> 上半出處：037 Analysis Report r18 c3 (Requirement Description)；模式 `full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-002",
  "req_id": "SWE1-RA-Driver_Distraction-010",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and \"Pairing (1st time)\" is retried after the timeout)",
  "pre_conditions": "1. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Start \"Pairing (1st time)\" from the Phone screen, then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Select \"Pairing (1st time)\" again and check that the pairing flow does not start",
  "expected_result": "1. The \"Pairing (1st time)\" pairing screen is shown, and the Phone screen is displayed again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. The \"Pairing (1st time)\" pairing flow does not start and the Phone screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915108",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取，斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：失效形態取「匯流排逾時」而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，而本列 AC2 逐字為 `the signal simulation tool stops transmitting a vehicle message`，其驗證方法欄亦書 `After the signal timeout`，故為停送非送 SNA。步驟 1 先確認該 feature 在訊號正常時可啟動，否則步驟 3 之「不可啟動」分不出「fail-safe 生效」與「本來就不可用」（IN §5.6 基準）。刻意略過：SNA（raw 8191）之路徑本列不涵蓋 —— 037 本列未書該形態，寫入即造值。另：本列與 newR1L-DD-004 之驗證目標實質相同（見該列 reasoning 與 A-DD7／DR-DD7）。"
}
```

### newR1L-DD-003 —— `SWE1-RA-Driver_Distraction-011`（P0）

> 上半出處：037 Analysis Report r19 c3 (Requirement Description)；模式 `excerpt(Case..Then)`；25/50 token

```json
{
  "tc_id": "newR1L-DD-003",
  "req_id": "SWE1-RA-Driver_Distraction-011",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "Case [Normal]the state becomes RESTRICTED while the user is using a restricted feature\nThen DD Service reports RESTRICTED and HMI displays the driver-distraction lockout notification\n(Lockout notification raised while \"Reconfigurable menu bar\" is being edited)",
  "pre_conditions": "1. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open the menu-bar configuration view for \"Reconfigurable menu bar\"\n2. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n3. Read the screen and check that the Standard Lockout Popup is displayed",
  "expected_result": "1. The menu-bar configuration view for \"Reconfigurable menu bar\" is displayed and accepts editing input\n2. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n3. The Standard Lockout Popup is displayed, showing \"Feature not available while the vehicle is in motion.\"",
  "spec_reference": "CFTS022-4915109",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：受限 feature 使用中而車速跨越門檻時，HMI 呈現 lockout 通知 —— 斷言錨取 profile §2.2 觀察面 B，字串逐字取 HMI spec p4。關鍵情境條件：與 -009 之別在於**施加順序** —— 本列先進入 feature 再跨門檻，故設計方法取狀態轉換；raw 129 同 profile §3.1，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 之 AC1 只有一條轉換路徑，無獨立可分之部分失效。刻意略過：通知關閉後之後續行為、以及 popup 之逾時形態，037 本列未書，不擴入；取樣 feature 取 \"Reconfigurable menu bar\"（Menu Bar 列，非黃標、非 NAV 系），與同源之 -012 一致，使 -118 家族之二列可對讀。"
}
```

### newR1L-DD-004 —— `SWE1-RA-Driver_Distraction-012`（P1）

> 上半出處：037 Analysis Report r20 c3 (Requirement Description)；模式 `full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-004",
  "req_id": "SWE1-RA-Driver_Distraction-012",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and \"Reconfigurable menu bar\" is retried after the timeout)",
  "pre_conditions": "1. The vehicle is stationary and $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open the \"Reconfigurable menu bar\" configuration view, then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open the menu-bar configuration view again and check that it does not open",
  "expected_result": "1. The menu-bar configuration view for \"Reconfigurable menu bar\" is displayed and accepts editing input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. The menu-bar configuration view does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915109",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "reasoning": "驗證目標：訊號逾時之 fail-safe 對 -118 家族之取樣 feature 同樣使其不可存取，斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：形態同 -010 取匯流排逾時，依 profile §3.2 逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書停送與 signal timeout。**本列之 037 Requirement Description 與 -010 逐字全等**（見 A-DD7），其 Then 句書 `HMI keeps the corresponding feature locked` 而非 -118 之通知面；本 TC 依原文斷言存取阻擋，**不代上游改寫為通知**（IN §8.4.2）。區別二列者為取樣 feature 與 spec_reference，非斷言內容。**本列與 newR1L-DD-002 之驗證目標實質相同** —— 依 IN §4.6 之等價判準（same trigger + outcome + input + verification target）四者皆同，其區別僅在取樣 feature 與追溯 ID，而取樣 feature 係作者所選、非 spec 所定。二列皆保留係追溯要求（每 leaf 須有 TC），**不得以取樣 feature 之不同偽稱為不同之驗證目標**；成因見 A-DD7／DR-DD7。"
}
```

---

## 5. 十七項自檢輸出（機器逐字）

```
====================================================================================
pilot 自檢 —— IN §9 十七項全跑 ＋ 追加項（下放包 10 §八 T16b）
====================================================================================
[PASS]   1 §4.1/§4.2        Test Set 名詞片語、能力層級、無 Test Group 前綴、拼寫一致
         {'Lockout Enforcement'}；4 則同一值
[PASS]   2 §4.3.1           test_item 兩段式：上半 verbatim ≤50tok；下半存在且為英文；無 modal
         009: 上半子串 ✓/25tok、下半 有、中文 無、modal 無；010: 上半子串 ✓/47tok、下半 有、中文 無、modal 無；011: 上半子串 ✓/25tok、下半 有、中文 無、modal 無；012: 上半子串 ✓/47tok、下半 有、中文 無、modal 無
[PASS]  2b §4.3.1           同一 Requirement ID 衍生之列，括號下半不逐字相同
         無重複
[PASS]   3 §4.4/§8.5        Pre-Condition 僅狀態／環境；無系統預設、待測前提、動作、step 可控狀態
         0 命中；4 則各 1 項（訊號源，§4.5-1 環境資料）
[PASS]   4 §4.5             Input Test Data 歸屬正確；重複值移入 PC／Procedure 或設 NA
         4 則皆 NA=True；回指 無；跨欄重複 無
[PASS]   5 §5.1/§5.5        步驟無禁用動詞；Final Step 含 ACTION ＋ check target（preferred verb）
         禁用動詞 0 命中；末步缺 `check that` 無
[PASS]   6 §5.2             步驟長度：一般 ≤12 字、Final ≤18 字（含 action+check target）
         字數 {'newR1L-DD-001': [8, 9, 13], 'newR1L-DD-002': [11, 11, 14], 'newR1L-DD-003': [9, 8, 12], 'newR1L-DD-004': [10, 11, 13]}
[N/A ]   7 §5.3             標準 setup 片語逐字重用
         本 feature 未定義 project-level setup 常數（feature.yaml 無該鍵）—— 無適用對象
[N/A ]   8 §5.4             CLI／tooling 步驟採 description + `$` 指令格式
         4 則皆為 HMI 操作與匯流排施加，無 CLI 步驟
[PASS]   9 §5.6             before／after 需要時建立 baseline
         009: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；010: 步驟 1 建立 before（feature 可啟動）✓；011: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；012: 步驟 1 建立 before（feature 可啟動）✓
[PASS]  10 §6               Procedure↔ER 1:1；ER 可觀察；ER 無 modal
         步驟 {'newR1L-DD-001': 3, 'newR1L-DD-002': 3, 'newR1L-DD-003': 3, 'newR1L-DD-004': 3}／ER {'newR1L-DD-001': 3, 'newR1L-DD-002': 3, 'newR1L-DD-003': 3, 'newR1L-DD-004': 3}；modal 無；非觀察語句 無
[PASS]  11 §7               無 FP／FF：含 setup／transition，不假設隱藏狀態；列舉支援項配負向
         FF：010／012 之 fail-safe 皆先建立正常態再注入故障，未假設隱藏狀態；FP：本 4 leaf 無列舉式支援項（無 format／device／protocol 之列舉），無配對義務
[PASS]  12 §8.1/§8.2/§8.4   追溯 Req/SWRA；不擴入 sibling；無造值；無範圍捏造
         req_id 形制 True；§8.4.2 禁詞 0 命中；數值母體 ['1', '129', '2', '3', '8.0625']，逾 profile §3.1／編號者 無
[PASS]  13 §12              Design Method 於 procedure 定稿後指派，且合 first-match 序
         009/011 觸發為 A→B 狀態轉換，於 Scenario 前命中；010/012 為 simulated fault（停送＋逾時），於 State Transition 前命中；皆為下拉選單實值 True
[PASS]  14 §11 + R-DD11     四欄 numbered item 無作者所書之行尾句號（引號內字串之終端標點保留）
         0 違規
[PASS]  15 §11 + R-DD12(c)  UI 標籤用 `"..."`；方括號僅限 037 逐字之 test_item 上半與 A-DD6 marker
         0 違規；test_item 上半之 `[Normal]`／`[Exception]` 經比對為 037 逐字（R-DD12(a)）；單引號／角括號 無
[PASS]  16 §10.7            spec_reference 列出所驗之每一 spec 節；一行一 ObjectID、無串接
         009=CFTS022-4915108／010=CFTS022-4915108／011=CFTS022-4915109／012=CFTS022-4915109
[PASS]  17 §8.6/§8.7        門檻為 spec 溯源之具體值；相似操作於 ER 具名區辨；來源規格勝於索引匯出
         門檻具名 raw True（profile §3.1 依 R-DD7(c)）；A-DD6 marker True；ER 取樣具名 True
[PASS]   + §11              多行欄位無行首／行尾空白，空行為真空行
         0 違規
[PASS]   + profile §2.3     ER 不含 RESTRICTED／NOT_RESTRICTED／Locked／Unlocked
         0 命中
[PASS]   + §10.2            priority 為 P0–P3 且合 profile §4
         009=P0／010=P1／011=P0／012=P1
[PASS]   + §10.5            test_procedure 至少 2 個編號步驟
         {'newR1L-DD-001': 3, 'newR1L-DD-002': 3, 'newR1L-DD-003': 3, 'newR1L-DD-004': 3}
====================================================================================
RESULT: PASS 20 ／ N/A 2 ／ FAIL 0　（共 22 檢）
```

---

## 6. T-抄 —— R-DD11／R-DD12／R-DD13

```
=== T-抄 逐字元核對（下放包 10）===
  R-DD11: 來源 426 字元；落檔 1 次；逐字元差異 0
  R-DD12: 來源 570 字元；落檔 1 次；逐字元差異 0
  R-DD13: 來源 487 字元；落檔 1 次；逐字元差異 0
  索引：現行 13（應 13）／留存 1（應 1）
  圍籬外註（舊 3 行不回修）：3
RESULT: PASS
```

出處註在圍籬內（下放包 08 §八-4 之制），**未另加圍籬外註**。
R-DD6 v1／R-DD7／R-DD8 之舊三行依該條不回修，仍為 3 行。

---

## 7. T-登 —— DR-DD7

| 項 | 動作 | 結果 |
|---|---|---|
| **DR-DD7** | **建檔** | DRAFTED；§四文稿逐字 **1112 字元，落檔 1 次** |
| **A-DD7** | **連結 DR-DD7** | 條目新增「處分（下放包 10 §四）—— 立 DR-DD7」節，狀態改 `PENDING（待 DR-DD7）` |
| 摘要表 | 新增一列 | 標的 037 作者／Leaves `-010`／`-012`／Anomaly 欄掛 **A-DD7** |

A-DD7 之 Tier 分際已寫入台帳：**執行層 Tier 1 登記，DR-DD7 為其 Tier 2 處置。**

---

## 8. 未結 DR 清單（DD1–DD7）

| DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|
| **DR-DD1** | DRAFTED（未發送）| `-025`~`-028`（4）| **凍結**，不入任何批次 |
| **DR-DD2** | DRAFTED（未發送）| `-021`~`-024`（4）| 不阻斷；保留 `$PARK_BRK_EGD$` |
| **DR-DD3** | ANSWERED-PENDING-CONFIRM | `-017`~`-028`（12）| 不阻斷；值 `91`，標 A-DD5 |
| **DR-DD4** | DRAFTED（未發送）| 9 列書 MPH 者 | 不阻斷；raw 邊界標 A-DD6 |
| **DR-DD5** | DRAFTED（未發送）| `-017`~`-024`（8）| **不入 pilot**（有無施加路徑）|
| **DR-DD6** | DRAFTED（未發送）| `-017`~`-024`（8）| **不入 pilot**（值如何對應）|
| **DR-DD7** | **DRAFTED（本輪新建，未發送）** | `-010`／`-012`（2）| **不阻斷**；二 TC 皆保留 |

**七筆皆未發送。** 獨立組：DD1／DD3 不可互抵；DD5／DD6 不可互抵。

### 阻斷疊圖

```
-001 ~ -002  (2)   無阻斷
-003 ~ -008  (6)   -003/-005/-007 帶 A-DD6
-009 ~ -012  (4)   **pilot 已修訂**；-009/-011 帶 A-DD6；-010/-012 另掛 A-DD7／DR-DD7
-013 ~ -016  (4)   -013/-015 帶 A-DD6
-017 ~ -024  (8)   A-DD5 ＋ DR-DD5 ＋ DR-DD6（+DR-DD2 於 021-024）→ 不入 pilot
-025 ~ -028  (4)   A-DD1 凍結 ＋ A-DD5
```

---

## 9. 獨立自評

### 9.1 我做對的

- **換骨幹，不是補檢項。** 下放包說「自檢擴充：對 IN §9 十七項全跑」。
  最省事的做法是在原本 13 檢後面追加幾條缺的。**我把骨幹整個換成十七項，
  §6.2 的八項改成附掛** —— 這樣下次下放包再漏列什麼，骨幹仍在。
- **N/A 有理由，且理由可查。** 第 7、8 項是真的沒有適用對象，
  不是「懶得查」。§5.4 那項還實際掃了 `$ ` 才敢寫 N/A。
- **D6 多修了一處。** 下放包點名 `-001` 兩處，但 `-003` ER2 有逐字相同的推導句。
  只修被點名的，會留下一則同病未修的。
- **判斷性的檢，明說它是判斷。** 第 9、11、12 項不是純字串比對，
  §2.5 逐項寫出依據。**把判斷偽裝成量測，比不做還糟。**

### 9.2 我做糙的

- **§5.2 六處逾限是我自己上輪寫出來的。** 這輪加了長度檢才發現。
  上輪我甚至在 reasoning 裡引了 §5.2 談步驟角色，**引了條文卻沒照它檢**。
- **`-009` 的 PC 我留得不乾脆。** §1.2 已載明它是四則中唯一非嚴格觸發條件者，
  依下放包「PC2 留」照留 —— 但我心裡知道 `-009` 那一則按 §8.5 的決定測試
  是偏「隱含環境穩定前提」的。**照令留，並把疑點寫明**，而不是自作主張刪掉。

### 9.3 我拒絕做的

- **不改 `test_item`**（D5）。profile §2.5 已啟用例外，改 TC 即違 R-S4 逐字。
- **不把 §5.2 的字數判準改寬。** 一度想把 `(8.0625 km/h)` 算成 1 個 token
  ——那是把尺改短來讓東西合格。**改的是步驟，不是尺。**

### 9.4 一件我原本會漏的

第 15 項的方括號檢，上一輪標籤誠實寫了「掃描範圍為四欄」，
**所以它沒說謊，但它也沒發現 D5。** 這輪把 `test_item` 納入後，
如果沒有 R-DD12(c) 的 carve-out，四則會**全部 FAIL**（`Case [Normal]` 是 037 逐字）。

**即：把檢查範圍擴大，同時必須把例外一起帶進來，否則會製造四個假陽性**
——而假陽性最常見的下場是被關掉，然後真的違規也一起不檢了。

---

## 10. 量測條件揭露（R-G8）

### 10.1 本包所書比率之分子與分母

| 計數 | 分子 | 分母 |
|---|---|---|
| 22 檢：PASS 20／N/A 2／FAIL 0 | 各判別之檢項數 | 本輪自檢共 22 項（IN §9 十七項 ＋ 追加 5）|
| 六個「否」對應六缺陷 | §2.2 表中「上一輪是否問過 = 否」之項數 | IN §9 十七項 |
| §5.2 逾限 6 處 | 字數 > 該角色上限之步驟數 | 4 TC × 3 步 = **12 個步驟** |
| 上半 25／47 token | 去編號後之空白 token 數 | 上限 50（R-3）|
| `-010` vs `-012` 相異 2 欄 | `str(a[j]) != str(b[j])` 之欄數 | 037 `Analysis Report` 全 **20** 欄 |
| 數值母體 5 個 | Procedure＋ER 內之數值 token（去重）| 白名單 7 個（`1,2,3,129,8.0625,0,0.0000`）|

### 10.2 字數之計法（§5.2 檢之判準）

**去除編號前綴後之空白 token 數**（`re.sub(r"^\d+\.\s*", "", item).split()`）。
故：

- `$STATUS_CCAN3.VehicleSpeedVSOSig$` 計 **1**
- `(8.0625 km/h)` 計 **2**（含空白）
- `"Pairing (1st time)"` 計 **3**

**IN §5.2 未定義 word 之計法。** 本計法對含單位與帶引號標籤之步驟**偏嚴**
（同一語意之步驟字數會比英文散文高）。**若 §5.2 另有計法，本項結果會不同。**

### 10.3 各檢之界線

- **第 3 項（§4.4）**為**黑名單**比對（5 條正則），非窮舉 §4.4 之全部形態。
  未列於黑名單之違規形態**掃不到**。
- **第 12 項之造值檢**母體為 Procedure＋ER，**不含 `test_item` 與 `reasoning`**。
  上半為 037 逐字，本不應以造值判；reasoning 不入工作簿。
- **第 15 項之 037 逐字比對**以 `in SRC[k][3]` 為之（子串比對）。
  若某方括號 token 恰為 037 他處之子串而非本 leaf 之，**會被誤放行**。
  本輪四則之 `[Normal]`／`[Exception]` 皆確在該 leaf 之 c3 內。
- **第 14 項之引號剝除**以 `"[^"]*"` 為之。**巢狀引號或未成對之引號會誤判**；
  本輪四則之引號皆成對。

### 10.4 檔與開啟方式

| 標的 | 檔 | 開啟 |
|---|---|---|
| 037 | `features/driver_distraction/inputs/DD_SWE1_0807_EN.xlsx` | `openpyxl`, `read_only=True`, `data_only=True` |
| profile | `docs/runtime/profiles/…Profile.md` | **唯讀**（取 §2.3／§2.5／§2.6 之判準）|
| IN | `docs/runtime/PROJECT_INSTRUCTION.md` | **唯讀**（§4.4／§4.5／§5.1／§5.2／§5.5／§5.6／§7／§8.5／§9／§11／§12）|
| 工作簿 | `workbook/driver_distraction_00.xlsx` | **本輪未開** |

### 10.5 本輪未量測者

- **修訂後之 TC 未經工作簿寫回驗證** —— 拘束「不寫回」，
  故欄位是否為工作簿所接受，本輪仍無從得知（同上繳 07 §9.5）。
- **`-013` 以後之 leaf** —— 非本輪範圍。
- **IN §10.1 之鍵名二制**（`tc_title`／`specification_reference`／`split_flag`／
  `split_reason` vs 本產物之 `test_item`／`spec_reference`）**仍未裁**，
  本輪照既有 pilot 形制辦。**上繳 07 §10-5 已列，本輪未獲回覆。**
- **`-009` 之 PC 依 §8.5 是否應刪** —— 見 §1.2 末段，照令留並記疑點。

---

## 11. 待分析層者

| # | 事項 | 現況 |
|---|---|---|
| 1 | `RULINGS.md` 是否改標題錨點體例（5 feature／148 條）| 上繳 07 §10-1，未獲回覆；下放包 10 §七-1 已轉 Pei |
| 2 | `RULINGS.sha.tsv` 由誰重生 | 同上，§七-2 |
| 3 | **輸出鍵名二制**（IN §10.1 vs pilot 形制）| 上繳 07 §10-5 提出，**本輪仍未裁** |
| 4 | **`-009` 之 PC 依 §8.5 之嚴格判準是否應刪** | 照令留，疑點見 §1.2 |
| 5 | **§5.2 之 word 計法** | IN 未定義；本輪計法見 §10.2，偏嚴 |
| 6 | 修訂後 4 TC 之審查 | 22 檢 20 PASS／2 N/A／0 FAIL |

**組 3 之 pilot 已依 D1–D6 修訂完畢；`-013` 以後待令。**
