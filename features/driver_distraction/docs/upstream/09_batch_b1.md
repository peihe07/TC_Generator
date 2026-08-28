# 上繳包 09 —— T-抄（18 錨點）、T18a／T18b／T18c（批次 B1）

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放包：`12_batch_b1.md` §七
- 本輪**未寫回工作簿、未執行 git**；產物置 `generated/`
- 共用路徑：**未寫入一字**；**T17b 維持停止**（待 popup 線，§二）

> **三件事**：
> **T-抄 18 錨點 ✓**，且既有 14 條之 `sha8` **全數未變**（§1.3）。
> **T18b 剔除 `-001`／`-002`** —— 但剔除的理由**不是**下放包所預期的「掃出新訊號」，
> 是**一個 `$…$` token 都沒有**（§3.2）。B1 = 10 leaf。
> **A-DD7 遠不止 2 leaf** —— 系統性量測得 **4 組、11/28 leaf**，
> 而 DR-DD7 之文稿只問其中 2 個（§5）。

---

## 1. T-抄 —— R-DD14／R-DD15／R-DD16／R-DD17

### 1.1 逐字元核對

| 條號 | 來源 | 字元數 | 落檔 | 逐字元差異 |
|---|---|---|---|---|
| R-DD14 | 包 11 §一（**前輪漏列**）| 674 | 1 次 | **0** |
| R-DD15 | 包 12 §三 | 334 | 1 次 | **0** |
| R-DD16 | 包 12 §三 | 458 | 1 次 | **0** |
| R-DD17 | 包 12 §三 | 489 | 1 次 | **0** |

索引：**現行 17 ／ 留存 1**；檔內 `## R-DD` 錨點 **18**。

四條係**與錨點一併落檔**（依 R-DD14 之體例），非先落後補。

### 1.2 停止條件 2（數值已更新為 18）—— 工具試跑

```
$ python3 scripts/rulings_hash.py --target features/driver_distraction/RULINGS.md --out <scratch>
寫入 …：18 錨點（ruling 18），來源 1 檔

重複 ruling_id 1 組（其中本體不同 1 組）：
  R-DD6: …RULINGS.md:121 與 …RULINGS.md:201（**本體不同**）
```

**18 = 17 現行 ＋ 1 留存 ✓**

### 1.3 ⚠ 一項未被要求但值得報的回歸

本輪新增四條之後，**既有 14 條之 `sha8` 逐一比對，全數未變**：

| 條 | 上輪 | 本輪 | | 條 | 上輪 | 本輪 |
|---|---|---|---|---|---|---|
| R-DD1 | `a9b76e4b` | `a9b76e4b` | | R-DD8 | `5dca74aa` | `5dca74aa` |
| R-DD2 | `da3cd8ec` | `da3cd8ec` | | R-DD6 v2 | `a5cbaf9c` | `a5cbaf9c` |
| R-DD3 | `cc7aea6c` | `cc7aea6c` | | R-DD9 | `965b6d4c` | `965b6d4c` |
| R-DD4 | `8d4f36bf` | `8d4f36bf` | | R-DD10 | `6f601dd1` | `6f601dd1` |
| R-DD5 | `75513f31` | `75513f31` | | R-DD11 | `872344f4` | `872344f4` |
| R-DD6 v1 | `f28ee265` | `f28ee265` | | R-DD12 | `42ddd946` | `42ddd946` |
| R-DD7 | `f33ed793` | `f33ed793` | | R-DD13 | `d46f4c85` | `d46f4c85` |

新增四條：`R-DD14 590f1cdc`／`R-DD15 b344ee36`／`R-DD16 85588cb1`／`R-DD17 a9ecb4c1`。

> **行號全部位移了（41→45 起），而 `sha8` 一個都沒變。**
> 這正是 R-DD14(c)「標題文字不入雜湊」與工具本體定義之驗證 ——
> 也是 §1.1 全域拘束（歸因鍵須為內容雜湊，不得為識別名）之正面例證：
> **位移不是改寫，sha 分得出來，行號分不出來。**

---

## 2. T-登 —— 索引留存列並列 `sha8`

依 §四-9：

```
| 條號版本 | 已被取代於 | `sha8`（v1／v2）| 其所載之失效值 |
| `R-DD6`（v1） | R-DD6 v2（下放包 08 §二）| **v1 `f28ee265`** ／ v2 `a5cbaf9c` | … |
```

並於表上加註同 id 之成因（工具正則不將 ` v1` 併入 id）、二列皆收錄無資料遺失、
以及**故以雜湊可辨**之理由（承 §1.1 拘束）。

---

## 3. T18b —— 訊號涵蓋掃描

### 3.1 掃描結果（母體：12 leaf ×全 20 欄）

| leaf | `$…$` token |
|---|---|
| `-001`／`-002` | **（無）** |
| `-003`~`-008` | `Speedometer` |
| `-013`~`-016` | **（無）** |

- **已涵蓋**：`$Speedometer$` 1 個 → profile §3「解除 —— `STATUS_CCAN3.VehicleSpeedVSOSig`」
- **未涵蓋**（profile §3 五項之外）：**0 個**
- profile §3 五項中本 12 leaf 未用及者：`Country_Code`／`PARK_BRK_EGD`／`PresentGear`／`VC_Trans_Equipped`

### 3.2 ⚠ token 掃描是錯的工具 —— `-001`／`-002` 之真正問題

**若只看掃描結果，B1 = 12 leaf，`-001`／`-002` 不必剔除** ——
它們沒有掃出「未涵蓋的訊號」，因為它們**一個 `$…$` token 都沒有**。

下放包 §6.1 之預期是「若掃出新訊號，該二 leaf 不入 B1」。
**實測是更麻煩的一種：沒有可掃之物。**

回讀 037 原文（`r9`／`r10`）：

```
-001  When the vehicle exits Body OFF sleep, DD Service provides Lock Out State
      initialization and state notification capabilities
      Method: Use a signal simulation tool that supports the **Body OFF power sequence**
              to trigger sleep and wake-up

-002  When the DD process is terminated during Body OFF sleep, DD Service provides
      cold-start state initialization capability after wake-up
      Method: … enter Body OFF sleep, **terminate the DD process in the test environment**,
              and then trigger wake-up
```

**其激勵為「Body OFF 電源時序」與「終止 DD process」** ——

| | `-001`／`-002` |
|---|---|
| `$…$` token | **無** |
| profile §3 五項中之對應 | **無** |
| 可供 R-DD5／R-DD6 v2 四庫查對之**具名識別碼** | **無** —— 037 未給任何 LID／訊號名 |

**「沒有 token」不等於「profile §3 涵蓋」。** 二者是不同的事：

- `-013`~`-016` 也沒有 `$…$` token，**但其 Method 逐字書 `send a speed above 5 MPH`
  與 `stop transmitting the message`** —— 激勵即速度訊號，**由 `$Speedometer$` 承載**，
  只是 037 在該四列改以散文表述
- `-001`／`-002` 之激勵**不是任何訊號**，是電源域事件與程序生命週期

**故剔除 `-001`／`-002`。**

### 3.3 ⚠ 一項下放包未預期之後果 —— 四庫查對亦無從進行

§6.1 云剔除者「另循 R-DD5／R-DD6 v2 之四庫查對流程，查無者登 DR」。

**四庫查對之輸入是一個具名識別碼**（如 `$PARK_BRK_EGD$`）。
`-001`／`-002` **037 未給任何名** —— 無從查起。

**執行層未臆造** —— 未把 `Body OFF` 猜成某個 PROXI 參數或 CAN 訊號，
亦未去 LID 搜 `Body`／`Sleep`／`Power` 之近似名（那是 R-13 所禁之代換）。

**待分析層**：`-001`／`-002` 之處置應為
（甲）向上游索取其激勵之具名識別碼後再查四庫、
（乙）逕登 DR 問「Body OFF 電源時序如何於台架施加」、或
（丙）判為台架能力問題而非訊號問題。**三者性質不同，非執行層可裁。**

### 3.4 B1 範圍

```
剔除：-001／-002（2 leaf）
B1  ：-003 -004 -005 -006 -007 -008 -013 -014 -015 -016（**10 leaf**）
```

合下放包 §6.2 之第二種情形。

### 3.5 ⚠ 更正下放包 §6.2-4 之一處

> 「**解鎖方向**（`-005`／`-013` 之 ≤3 MPH）用 raw **77**」

**`-013` 不是解鎖方向。** 實測（037 全欄 MPH 字樣）：

| leaf | MPH 字樣 | 方向 | 037 逐字 |
|---|---|---|---|
| `-005` | `3 MPH` | **解鎖** | `speed decreases from above 3 MPH to 3 MPH or below` |
| **`-013`** | **`5 MPH`** | **上鎖** | Method：`send a speed above 5 MPH or another RESTRICTED condition` |
| `-007` | `5 MPH` | 上鎖 | `speed increases from below 5 MPH to 5 MPH or above` |
| `-015` | `5 MPH` | 上鎖 | 同 `-013` |
| `-003` | `3 MPH`＋`5 MPH` | **雙向** | `outputs the restriction state according to the 5/3 MPH rule` |

**故 `-013` 用 raw 129（上鎖側），非 77。** 用 77 者為 `-005`（單向）與 `-003`（雙向之下半段）。

---

## 4. T18a —— pilot 之最終修訂

| # | 修訂 | 依據 |
|---|---|---|
| T18a-1 | 四則 PC 改為 `1. The signal $…$ is transmitted on the bus at 0 (0.0000 km/h)` | **R-DD17** |
| T18a-2 | 四則補 `split_flag: false`／`split_reason: "NA"` | **R-DD16(b)** |

**寫回器未拒受** —— 本輪不寫回，故 R-DD16(c) 之情形未發生；**未刪任何鍵**。

自檢第 3 項之判準已含 R-DD17 之形式（正則 `^\d+\. The signal \$[\w.]+\$ is transmitted
on the bus at \d+ \([\d.]+ km/h\)$`），另新增 R-DD16(b) 一檢 → **23 檢**。

### 4.1 ⚠ 自檢第 9 項曾因 R-DD17 而 FAIL —— 是檢查器過時，不是 TC 缺陷

第 9 項（§5.6 baseline）以字面 `"transmitted at 0"` 判 `-009`／`-011` 之 before 態。
R-DD17 把該行改為 `… is transmitted **on the bus** at 0 …`，**字面不再命中**，
於是二則報 FAIL。

**改的是檢查器之字面（改為 `"at 0 (0.0000 km/h)"`），不是 TC。**
記此以免日後被讀為「pilot 一度不合格」。

pilot 修訂後：**23 檢 —— 21 PASS ／ 2 N/A ／ 0 FAIL。**

---

## 5. A-DD7 之擴大量測 —— **不是 2 leaf，是 11 leaf**

T18b 讀 037 原文時順帶所得。以「除 c0 leaf id、c1 source 外之 **18 欄**」為鍵，
對**全 28 leaf** 分組，逐字全等之組：

| 組 | leaf | 各自之 source | AC |
|---|---|---|---|
| 1 | `-004`／`-006`／`-008`（**3**）| `-114`／`-115`／`-116` | AC2 速度輸入逾時 |
| 2 | `-010`／`-012`／**`-014`／`-016`**（**4**）| `-117`／`-118`／`-120`／`-121` | AC2 訊號停送逾時 |
| 3 | `-018`／`-020`（2）| `-125`+`-126`／`-125`+`-127` | AC2（HK 段）|
| 4 | `-022`／`-024`（2）| `-125`+`-128`／`-125`+`-129` | AC2（HK 段）|

**4 組，11 / 28 leaf（39%），全部為 AC2。**
對照：**AC1 各列皆隨其 source 分化**（`-009` vs `-011` 差 4 欄，含 Description 與 VC）。

**A-DD7 初登時記為 2 leaf，實為組 2 之 4 leaf 中的 2 個。** 台帳已擴充。

### 5.1 DR-DD7 之文稿範圍窄於本量測

`DR-DD7` 之文稿（下放包 10 §四，逐字，DRAFTED 未發送）**只問 `-010` 與 `-012`**。
同一問題另涉 **9 個 leaf**。

**執行層不改該文稿**（改之即非所擬之版本）。**是否擴大其範圍屬分析層。**
若不擴大，`-004`／`-006`／`-008`／`-014`／`-016`（**皆在本輪 B1 之內**）
之同一形態將無 DR 承載。

> 本輪 B1 之 10 則中，**5 則出自這個形態**。它們的 `reasoning` 各自載明了
> 「與其他 AC2 列逐字全等、區別僅在取樣 feature 與追溯 ID」，
> 但**台帳上只有 2 個 leaf 被 DR 問到**。

---

## 6. T18c —— 批次 B1（10 TC）

**產物**：`generated/batch_b1.json`　**生成器**：`scripts/gen_batch_b1.py`
**自檢**：`scripts/selfcheck_tcs.py`（骨幹共用，產物由 `SC_ARTIFACT` 指定）

### 6.1 上半之擷取

| leaf | 037 全文 token | 模式 | 落檔 token |
|---|---|---|---|
| `-003` | 63 | `excerpt(Case..Then)` | 35 |
| `-013` | 62 | `excerpt(Case..Then)` | 29 |
| 其餘 8 則 | 44–47 | `full` | 44–47 |

生成器對每則 `assert 摘句 in 原文`，非子串即中止。

### 6.2 取樣 feature —— 一個 Requirement 家族一個

**黃標三項與 NAV 系皆已排除**（黃標以 PDF 填色實測，嚴格區間）：

| 家族 | leaf | 取樣 feature | p7 列 |
|---|---|---|---|
| `-114` | `-003`／`-004` | `"Reconfigurable menu bar"` | top=356（Menu Bar）|
| `-115` | `-005`／`-006` | `"Edit phone book (speller input)"` | top=291（Phone）|
| `-116` | `-007`／`-008` | `"DND Customize auto reply message"` | top=317（DND）|
| `-120` | `-013`／`-014` | `"Player Song, artist, title, etc. (speller search)"` | top=330（Player）|
| `-121` | `-015`／`-016` | `"Pairing (1st time)"` | top=304（Phone）|

**`-013`／`-015` 之取樣與 pilot 相異 ✓**（§6.2-3）；p7 列已於各則 reasoning 載明。

**一個家族一個取樣**，使該家族之 AC1／AC2 可對讀。
**取樣之相異不作為驗證目標之區辨**（下放包 10 §四明文）。

`Database Entry - License Key Entry`（p7 top=252，非黃標）**保守未取** ——
其緊接 NAV 區塊之末，是否屬 NAV 系（地圖資料庫授權）未經確認。**未查即不取。**

### 6.3 §6.2 六項拘束之對照

| 拘束 | 落實 |
|---|---|
| 1 自檢骨幹為 IN §9 十七項 | ✓ 23 檢（17 ＋ 追加 6），下放包所列為額外 |
| 2 用及 §3.1 raw 者標 A-DD6 | ✓ `-003`／`-005`／`-007`／`-013`／`-015` 皆標；自檢改為**由 procedure 是否含 raw 129／77 推導**，非以 leaf 號硬編 |
| 3 `-013`／`-015` 取樣依 p7、與 pilot 相異、reasoning 載明 p7 列 | ✓ §6.2 |
| 4 解鎖用 raw 77；BVA 另一側不擴入 | ✓ `-005`／`-003` 用 77；`128`／`78` 未出現（自檢第 12 項之數值白名單）。**`-013` 之方向已更正，見 §3.5** |
| 5 priority 依 profile §4，不因批次重判 | ✓ P0＝`-007`／`-013`／`-015`；其餘 P1。自檢由 profile §4 之 P0 集合推導 |
| 6 只生成、不寫回、不 git | ✓ |

### 6.4 一項拆分判斷 —— `-003` 未拆

`-003` 之 037 文書 `5/3 MPH rule`，VC 二項（5 MPH 受限、3 MPH 解除）。

**未拆，`split_flag: false`。** 依 IN §5.7：
「One trigger → multiple consequential outcomes belong in ONE TC」——
此處為**同一速度監看能力**之二個後果，以四步序列（0→129→77）於一則內涵蓋。

**個別方向另有其 source**：`-007`（`-116`，上鎖）、`-005`（`-115`，解鎖）
各自成 TC。三者不重複 —— `-003` 驗**規則整體**，另二者驗**各自之單向轉換**。

### 6.5 未取任意中間值 —— §8.4.1

`-005` 之 037 書「from **above 3 MPH**」、`-007` 書「from **below 5 MPH**」。
**profile §3.1 只給 129 與 77 二個 spec 溯源之格**。

- `-005` 起始取 **129**（8.0625 km/h＝5.0097 MPH，確在 3 MPH 之上）
- `-007` 起始取 **77**（4.8125 km/h＝2.9903 MPH，確在 5 MPH 之下）

**未另擇一個「3 至 5 MPH 之間」的值** —— 那個值無 spec 來源，寫入即造值。

### 6.6 B1 自檢結果

**23 檢 —— 21 PASS ／ 2 N/A ／ 0 FAIL。**

過程中第 6 項（§5.2）曾 FAIL 三處：`B004`／`B006`／`B008` 之步驟 1
為 14／14／16 字（長標籤所致）。

**依 R-DD15(d) 改步驟，不改尺** —— 步驟 1 由
`Open {feat} and confirm it accepts input, then leave it` 收為 `Open {feat}, then leave it`，
baseline 之「before 態」改由 ER1 承載（`… is displayed and accepts input`）。
現行字數全部合格。

---

## 7. 修訂後 pilot 四則

### newR1L-DD-001 —— `SWE1-RA-Driver_Distraction-009`（P0／Lockout Enforcement）

> 上半：037 Analysis Report r17 c3 (Requirement Description)；`excerpt(Case..Then)`；25/50 token

```json
{
  "tc_id": "newR1L-DD-001",
  "req_id": "SWE1-RA-Driver_Distraction-009",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "Case [Normal]the user attempts to access a restricted feature in the lockout table\nThen DD Service outputs RESTRICTED and HMI prevents access to the feature\n(Access attempt on \"Pairing (1st time)\" with the speed signal held at the lock threshold)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Open the Phone screen and select \"Pairing (1st time)\"\n3. Read the Phone screen and check that the pairing flow has not started",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. The Phone screen is displayed and the \"Pairing (1st time)\" entry is selected\n3. The pairing flow does not start and the Phone screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915108",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：速度達上鎖門檻時，Lockout Table 所列之受限 feature 其存取被阻 —— 斷言錨取 profile §2.1 觀察面 A（存取阻擋），取樣 feature 具名為 \"Pairing (1st time)\"。關鍵情境條件：$STATUS_CCAN3.VehicleSpeedVSOSig$ 由 0 送至 raw 129（8.0625 km/h＝5.0097 MPH），該值為 profile §3.1 依 R-DD7(c) 所定之上鎖側第一個可表示格，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 之 AC1 只有一條常態路徑（施加受限狀態 → 存取被阻），無獨立可分之部分失效（IN §8.2.2 未成立）。刻意略過：解鎖方向（raw 77／78）屬 -013／-015，門檻下側 raw 128 之不應鎖屬 BVA 之另一半，本列不擴入（IN §8.2.1）；p7 黃標三項（Player / RSE、Messaging、SRT Options）不取樣，Embedded NAV 系（含 Destination Entry）因僅適用 LATAM 亦不取。設計方法依 IN §12 首合原則取狀態轉換 —— 觸發為車速由 0 跨越門檻之 A→B 轉換，於 Scenario 之前命中；且 §12 tie-break 之 Scenario 判準為「≥3 steps crossing features」，本列為單一 feature 之存取嘗試，不合。"
}
```

### newR1L-DD-002 —— `SWE1-RA-Driver_Distraction-010`（P1／Lockout Enforcement）

> 上半：037 Analysis Report r18 c3 (Requirement Description)；`full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-002",
  "req_id": "SWE1-RA-Driver_Distraction-010",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and \"Pairing (1st time)\" is retried after the timeout)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Start \"Pairing (1st time)\" from the Phone screen, then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Select \"Pairing (1st time)\" again and check that the pairing flow does not start",
  "expected_result": "1. The \"Pairing (1st time)\" pairing screen is shown, and the Phone screen is displayed again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. The \"Pairing (1st time)\" pairing flow does not start and the Phone screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915108",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取，斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：失效形態取「匯流排逾時」而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，而本列 AC2 逐字為 `the signal simulation tool stops transmitting a vehicle message`，其驗證方法欄亦書 `After the signal timeout`，故為停送非送 SNA。步驟 1 先確認該 feature 在訊號正常時可啟動，否則步驟 3 之「不可啟動」分不出「fail-safe 生效」與「本來就不可用」（IN §5.6 基準）。刻意略過：SNA（raw 8191）之路徑本列不涵蓋 —— 037 本列未書該形態，寫入即造值。另：本列與 newR1L-DD-004 之驗證目標實質相同（見該列 reasoning 與 A-DD7／DR-DD7）。"
}
```

### newR1L-DD-003 —— `SWE1-RA-Driver_Distraction-011`（P0／Lockout Enforcement）

> 上半：037 Analysis Report r19 c3 (Requirement Description)；`excerpt(Case..Then)`；25/50 token

```json
{
  "tc_id": "newR1L-DD-003",
  "req_id": "SWE1-RA-Driver_Distraction-011",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "Case [Normal]the state becomes RESTRICTED while the user is using a restricted feature\nThen DD Service reports RESTRICTED and HMI displays the driver-distraction lockout notification\n(Lockout notification raised while \"Reconfigurable menu bar\" is being edited)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open the menu-bar configuration view for \"Reconfigurable menu bar\"\n2. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n3. Read the screen and check that the Standard Lockout Popup is displayed",
  "expected_result": "1. The menu-bar configuration view for \"Reconfigurable menu bar\" is displayed and accepts editing input\n2. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n3. The Standard Lockout Popup is displayed, showing \"Feature not available while the vehicle is in motion.\"",
  "spec_reference": "CFTS022-4915109",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：受限 feature 使用中而車速跨越門檻時，HMI 呈現 lockout 通知 —— 斷言錨取 profile §2.2 觀察面 B，字串逐字取 HMI spec p4。關鍵情境條件：與 -009 之別在於**施加順序** —— 本列先進入 feature 再跨門檻，故設計方法取狀態轉換；raw 129 同 profile §3.1，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 之 AC1 只有一條轉換路徑，無獨立可分之部分失效。刻意略過：通知關閉後之後續行為、以及 popup 之逾時形態，037 本列未書，不擴入；取樣 feature 取 \"Reconfigurable menu bar\"（Menu Bar 列，非黃標、非 NAV 系），與同源之 -012 一致，使 -118 家族之二列可對讀。"
}
```

### newR1L-DD-004 —— `SWE1-RA-Driver_Distraction-012`（P1／Lockout Enforcement）

> 上半：037 Analysis Report r20 c3 (Requirement Description)；`full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-004",
  "req_id": "SWE1-RA-Driver_Distraction-012",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and \"Reconfigurable menu bar\" is retried after the timeout)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open the \"Reconfigurable menu bar\" configuration view, then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open the menu-bar configuration view again and check that it does not open",
  "expected_result": "1. The menu-bar configuration view for \"Reconfigurable menu bar\" is displayed and accepts editing input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. The menu-bar configuration view does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915109",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：訊號逾時之 fail-safe 對 -118 家族之取樣 feature 同樣使其不可存取，斷言錨取 profile §2.1 觀察面 A。關鍵情境條件：形態同 -010 取匯流排逾時，依 profile §3.2 逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書停送與 signal timeout。**本列之 037 Requirement Description 與 -010 逐字全等**（見 A-DD7），其 Then 句書 `HMI keeps the corresponding feature locked` 而非 -118 之通知面；本 TC 依原文斷言存取阻擋，**不代上游改寫為通知**（IN §8.4.2）。區別二列者為取樣 feature 與 spec_reference，非斷言內容。**本列與 newR1L-DD-002 之驗證目標實質相同** —— 依 IN §4.6 之等價判準（same trigger + outcome + input + verification target）四者皆同，其區別僅在取樣 feature 與追溯 ID，而取樣 feature 係作者所選、非 spec 所定。二列皆保留係追溯要求（每 leaf 須有 TC），**不得以取樣 feature 之不同偽稱為不同之驗證目標**；成因見 A-DD7／DR-DD7。"
}
```

---

## 8. 批次 B1 —— 10 則全文

### newR1L-DD-B001 —— `SWE1-RA-Driver_Distraction-003`（P1／Speed Threshold Judgment）

> 上半：037 Analysis Report r11 c3 (Requirement Description)；`excerpt(Case..Then)`；35/50 token

```json
{
  "tc_id": "newR1L-DD-B001",
  "req_id": "SWE1-RA-Driver_Distraction-003",
  "test_group": "Driver Distraction",
  "test_set": "Speed Threshold Judgment",
  "test_item": "Case [Normal]vehicle speed changes within the valid range\nThen DD Service outputs the restriction state according to the 5/3 MPH rule, and HMI can control the corresponding features based on the state output by DD\n(Both boundaries of the 5/3 MPH rule, exercised in one sequence)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Select \"Reconfigurable menu bar\" and check that it does not open\n3. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 77 (4.8125 km/h)\n4. Select \"Reconfigurable menu bar\" again and check that it opens",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. \"Reconfigurable menu bar\" does not open and the screen stays as it was before the attempt\n3. The vehicle-speed signal is carried on the bus at raw 77, which is 4.8125 km/h [ASSUMPTION A-DD6]\n4. \"Reconfigurable menu bar\" opens and its view is displayed",
  "spec_reference": "CFTS022-4915105",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：037 本列之 `5/3 MPH rule` —— 其 VC 二項分別為 5 MPH 之受限與 3 MPH 之解除，**同一能力之二個後果**，依 IN §5.7 歸一條 TC，不拆。關鍵情境條件：raw 129 與 raw 77 皆取 profile §3.1（R-DD7(c)），標 [ASSUMPTION A-DD6]；取樣 feature 取 \"Reconfigurable menu bar\"（p7 top=356（Menu Bar 列）），非黃標、非 NAV 系。**未取「above 3 MPH」之任意中間值** —— profile §3.1 只給 129 與 77 二個 spec 溯源之格，另擇一值即造值（IN §8.4.1）；raw 129（5.0097 MPH）本身即在 3 MPH 之上，足以起算。刻意略過：BVA 之另一側（raw 128／78）037 未書，不擴入（IN §8.2.1）；個別方向之轉換分由 `-007`（上鎖）與 `-005`（解鎖）依其各自 source 承載。"
}
```

### newR1L-DD-B002 —— `SWE1-RA-Driver_Distraction-004`（P1／Speed Threshold Judgment）

> 上半：037 Analysis Report r12 c3 (Requirement Description)；`full`；45/50 token

```json
{
  "tc_id": "newR1L-DD-B002",
  "req_id": "SWE1-RA-Driver_Distraction-004",
  "test_group": "Driver Distraction",
  "test_set": "Speed Threshold Judgment",
  "test_item": "AC2:\nWhen DD Service can no longer obtain a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed-input timeout monitoring and fail-safe restriction capability\nCase [Exception]the speed input is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED after the input timeout\n(Fail-safe: the speed message is stopped and the menu-bar view is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Reconfigurable menu bar\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Reconfigurable menu bar\" again and check that it does not open",
  "expected_result": "1. \"Reconfigurable menu bar\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Reconfigurable menu bar\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915105",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Reconfigurable menu bar\"（p7 top=356（Menu Bar 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-114`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B003 —— `SWE1-RA-Driver_Distraction-005`（P1／Speed Threshold Judgment）

> 上半：037 Analysis Report r13 c3 (Requirement Description)；`full`；46/50 token

```json
{
  "tc_id": "newR1L-DD-B003",
  "req_id": "SWE1-RA-Driver_Distraction-005",
  "test_group": "Driver Distraction",
  "test_set": "Speed Threshold Judgment",
  "test_item": "AC1:\nWhen DD Service receives a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed monitoring, restriction-state judgment, and state notification capabilities\nCase [Normal]vehicle speed decreases from above 3 MPH to 3 MPH or below\nThen DD Service sets the Lock Out State to NOT_RESTRICTED\n(Unlock at the 3 MPH boundary, approached from above)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 77 (4.8125 km/h)\n3. Select \"Edit phone book (speller input)\" and check that it opens",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h, above the 3 MPH threshold [ASSUMPTION A-DD6]\n2. The vehicle-speed signal is carried on the bus at raw 77, which is 4.8125 km/h [ASSUMPTION A-DD6]\n3. \"Edit phone book (speller input)\" opens and its view is displayed",
  "spec_reference": "CFTS022-4915106",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：車速自 3 MPH 之上降至 3 MPH 或以下時，受限解除 —— 斷言錨取 profile §2.1 觀察面 A，取樣 feature \"Edit phone book (speller input)\"（p7 top=291（Phone 列））。關鍵情境條件：解鎖側取 raw **77**（4.8125 km/h＝2.9903 MPH），為 profile §3.1 依 R-DD7(c) 所定之 ≤3 MPH 側第一個可表示格，標 [ASSUMPTION A-DD6]。起始值取 raw 129 而非任意「3 MPH 以上」之值 —— 後者無 spec 來源，寫入即造值。一條 TC 即足：037 本列只有一條解鎖路徑。刻意略過：raw 78（不應解）為 BVA 之另一側，037 未書，不擴入（§8.2.1）；037 VC 第 2 項之 `\"Lock Out State\" variable to \"Unlocked\"` 依 profile §2.3 不得入 ER，改以 HMI 之可及性承載。"
}
```

### newR1L-DD-B004 —— `SWE1-RA-Driver_Distraction-006`（P1／Speed Threshold Judgment）

> 上半：037 Analysis Report r14 c3 (Requirement Description)；`full`；45/50 token

```json
{
  "tc_id": "newR1L-DD-B004",
  "req_id": "SWE1-RA-Driver_Distraction-006",
  "test_group": "Driver Distraction",
  "test_set": "Speed Threshold Judgment",
  "test_item": "AC2:\nWhen DD Service can no longer obtain a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed-input timeout monitoring and fail-safe restriction capability\nCase [Exception]the speed input is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED after the input timeout\n(Fail-safe: the speed message is stopped and the phone book is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Edit phone book (speller input)\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Edit phone book (speller input)\" again and check that it does not open",
  "expected_result": "1. \"Edit phone book (speller input)\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Edit phone book (speller input)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915106",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Edit phone book (speller input)\"（p7 top=291（Phone 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-115`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B005 —— `SWE1-RA-Driver_Distraction-007`（P0／Speed Threshold Judgment）

> 上半：037 Analysis Report r15 c3 (Requirement Description)；`full`；46/50 token

```json
{
  "tc_id": "newR1L-DD-B005",
  "req_id": "SWE1-RA-Driver_Distraction-007",
  "test_group": "Driver Distraction",
  "test_set": "Speed Threshold Judgment",
  "test_item": "AC1:\nWhen DD Service receives a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed monitoring, restriction-state judgment, and state notification capabilities\nCase [Normal]vehicle speed increases from below 5 MPH to 5 MPH or above\nThen DD Service sets the Lock Out State to RESTRICTED\n(Lock at the 5 MPH boundary, approached from below)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 77 (4.8125 km/h)\n2. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n3. Select \"DND Customize auto reply message\" and check that it does not open",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 77, which is 4.8125 km/h, below the 5 MPH threshold [ASSUMPTION A-DD6]\n2. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n3. \"DND Customize auto reply message\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915107",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：車速自 5 MPH 之下升至 5 MPH 或以上時，受限生效 —— 斷言錨取 profile §2.1 觀察面 A，取樣 feature \"DND Customize auto reply message\"（p7 top=317（DND 列））。關鍵情境條件：上鎖側取 raw **129**（8.0625 km/h＝5.0097 MPH），為 profile §3.1 之 ≥5 MPH 側第一個可表示格，標 [ASSUMPTION A-DD6]；起始值取 raw 77（2.9903 MPH）—— 其為 profile §3.1 中唯一低於 5 MPH 之 spec 溯源格。一條 TC 即足：037 本列只有一條上鎖路徑。刻意略過：raw 128（不應鎖）037 未書，不擴入（§8.2.1）。"
}
```

### newR1L-DD-B006 —— `SWE1-RA-Driver_Distraction-008`（P1／Speed Threshold Judgment）

> 上半：037 Analysis Report r16 c3 (Requirement Description)；`full`；45/50 token

```json
{
  "tc_id": "newR1L-DD-B006",
  "req_id": "SWE1-RA-Driver_Distraction-008",
  "test_group": "Driver Distraction",
  "test_set": "Speed Threshold Judgment",
  "test_item": "AC2:\nWhen DD Service can no longer obtain a valid $Speedometer$ value through CarPropertyService\nAnd DD Service provides speed-input timeout monitoring and fail-safe restriction capability\nCase [Exception]the speed input is unavailable\nThen DD Service sets the Lock Out State to RESTRICTED after the input timeout\n(Fail-safe: the speed message is stopped and the auto reply editor is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"DND Customize auto reply message\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"DND Customize auto reply message\" again and check that it does not open",
  "expected_result": "1. \"DND Customize auto reply message\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"DND Customize auto reply message\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915107",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"DND Customize auto reply message\"（p7 top=317（DND 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-116`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B007 —— `SWE1-RA-Driver_Distraction-013`（P0／Lockout Enforcement）

> 上半：037 Analysis Report r21 c3 (Requirement Description)；`excerpt(Case..Then)`；29/50 token

```json
{
  "tc_id": "newR1L-DD-B007",
  "req_id": "SWE1-RA-Driver_Distraction-013",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "Case [Normal]HMI has selected the applicable lockout table and judgment Type for the All architecture\nThen DD Service outputs RESTRICTED and HMI locks features marked L/O in the table\n(Lockout of a table entry sampled from the Player row)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Select \"Player Song, artist, title, etc. (speller search)\" and check that it does not open",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. \"Player Song, artist, title, etc. (speller search)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915112",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：受限態下，Lockout Table 標 `L/O` 之 feature 被鎖 —— 取樣 \"Player Song, artist, title, etc. (speller search)\"，所據為 HMI spec p7 top=330（Player 列），**非黃標（黃標三項為 Player / RSE、Messaging、SRT Options，以 PDF 填色實測定位）、非 NAV 系（p7 註記逐字 `Embedded NAV for R1L is applicable to LATAM region only`）**。關鍵情境條件：037 本列之 Method 逐字 `send a speed above 5 MPH`，故取 profile §3.1 之上鎖側 raw 129，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**不逐一遍歷表列全部 feature** —— 037 本列未要求窮舉，以具名單一樣本承載（profile §2.1 禁泛稱，未禁單樣本）；解鎖方向與 BVA 另一側不擴入（§8.2.1）。"
}
```

### newR1L-DD-B008 —— `SWE1-RA-Driver_Distraction-014`（P1／Lockout Enforcement）

> 上半：037 Analysis Report r22 c3 (Requirement Description)；`full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-B008",
  "req_id": "SWE1-RA-Driver_Distraction-014",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and the player search is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Player Song, artist, title, etc. (speller search)\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Player Song, artist, title, etc. (speller search)\" again and check that it does not open",
  "expected_result": "1. \"Player Song, artist, title, etc. (speller search)\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Player Song, artist, title, etc. (speller search)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915112",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Player Song, artist, title, etc. (speller search)\"（p7 top=330（Player 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-120`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

### newR1L-DD-B009 —— `SWE1-RA-Driver_Distraction-015`（P0／Lockout Enforcement）

> 上半：037 Analysis Report r23 c3 (Requirement Description)；`full`；44/50 token

```json
{
  "tc_id": "newR1L-DD-B009",
  "req_id": "SWE1-RA-Driver_Distraction-015",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC1:\nWhen the signal simulation tool sends vehicle signals that change the Lock Out State to RESTRICTED\nAnd DD Service provides restriction-state judgment and notification, and HMI provides feature lockout\nCase [Normal]DD Service outputs RESTRICTED and HMI locks features marked L/O in the table\n(Lockout of a table entry sampled from the Phone row)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Send the signal $STATUS_CCAN3.VehicleSpeedVSOSig$ = 129 (8.0625 km/h)\n2. Select \"Pairing (1st time)\" and check that it does not open",
  "expected_result": "1. The vehicle-speed signal is carried on the bus at raw 129, which is 8.0625 km/h [ASSUMPTION A-DD6]\n2. \"Pairing (1st time)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915115",
  "tc_ref_id": "NEW",
  "priority": "P0",
  "design_method": "狀態轉換 (State Transition Testing)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：受限態下，Lockout Table 標 `L/O` 之 feature 被鎖 —— 取樣 \"Pairing (1st time)\"，所據為 HMI spec p7 top=304（Phone 列），**非黃標（黃標三項為 Player / RSE、Messaging、SRT Options，以 PDF 填色實測定位）、非 NAV 系（p7 註記逐字 `Embedded NAV for R1L is applicable to LATAM region only`）**。關鍵情境條件：037 本列之 Method 逐字 `send a speed above 5 MPH`，故取 profile §3.1 之上鎖側 raw 129，標 [ASSUMPTION A-DD6]。一條 TC 即足：037 本列只有一條常態路徑。刻意略過：**不逐一遍歷表列全部 feature** —— 037 本列未要求窮舉，以具名單一樣本承載（profile §2.1 禁泛稱，未禁單樣本）；解鎖方向與 BVA 另一側不擴入（§8.2.1）。"
}
```

### newR1L-DD-B010 —— `SWE1-RA-Driver_Distraction-016`（P1／Lockout Enforcement）

> 上半：037 Analysis Report r24 c3 (Requirement Description)；`full`；47/50 token

```json
{
  "tc_id": "newR1L-DD-B010",
  "req_id": "SWE1-RA-Driver_Distraction-016",
  "test_group": "Driver Distraction",
  "test_set": "Lockout Enforcement",
  "test_item": "AC2:\nWhen the signal simulation tool stops transmitting a vehicle message required for DD judgment\nAnd DD Service provides signal-timeout fail-safe behavior, and HMI applies lockout for RESTRICTED\nCase [Exception]a required vehicle signal is unavailable\nThen DD Service outputs RESTRICTED and HMI keeps the corresponding feature locked\n(Fail-safe: the speed message is stopped and pairing is retried)",
  "pre_conditions": "1. The signal $STATUS_CCAN3.VehicleSpeedVSOSig$ is transmitted on the bus at 0 (0.0000 km/h)",
  "input_test_data": "NA",
  "test_procedure": "1. Open \"Pairing (1st time)\", then leave it\n2. Stop transmitting the message \"STATUS_CCAN3\" and let the signal timeout elapse\n3. Open \"Pairing (1st time)\" again and check that it does not open",
  "expected_result": "1. \"Pairing (1st time)\" is displayed and accepts input, and the previous screen is shown again after leaving it\n2. The message \"STATUS_CCAN3\" is no longer present on the bus and the signal timeout window has elapsed\n3. \"Pairing (1st time)\" does not open and the screen stays as it was before the attempt",
  "spec_reference": "CFTS022-4915115",
  "tc_ref_id": "NEW",
  "priority": "P1",
  "design_method": "基礎故障注入 (Fault Injection Lite)",
  "functional_safety": "NA",
  "author": "PeiPYHsu",
  "split_flag": false,
  "split_reason": "NA",
  "reasoning": "驗證目標：DD 判定所需之車輛訊號消失時，fail-safe 使受限 feature 仍不可存取 —— 斷言錨取 profile §2.1 觀察面 A，取樣 \"Pairing (1st time)\"（p7 top=304（Phone 列））。關鍵情境條件：失效形態取**匯流排逾時**而非 SNA —— profile §3.2 明定逐 leaf 依 037 AC2 原文定，本列 AC2 逐字書 `stops transmitting`／`stop updating`，其 Method 亦書 `After the … signal timeout`，故為停送非送 SNA（raw 8191）。步驟 1 先確認訊號正常時該 feature 可用，否則步驟 3 之「不可用」分不出 fail-safe 生效與本來就不可用（IN §5.6 基準）。**本列之 037 原文與其他 AC2 列逐字全等**（A-DD7 之擴大量測：4 組、11/28 leaf）——本列源自 `-121`，其區別僅在取樣 feature 與追溯 ID，**不得以取樣 feature 之不同偽稱為不同之驗證目標**（下放包 10 §四）。刻意略過：SNA（raw 8191）路徑 037 本列未書，寫入即造值。"
}
```

---

## 9. 自檢輸出（機器逐字）

### 9.1 B1（`SC_ARTIFACT=batch_b1.json`）

```
====================================================================================
TC 自檢 —— IN §9 十七項全跑 ＋ 追加項（骨幹；產物由 SC_ARTIFACT 指定）
====================================================================================
[PASS]   1 §4.1/§4.2        Test Set 名詞片語、能力層級、無 Test Group 前綴、拼寫一致
         {'Lockout Enforcement', 'Speed Threshold Judgment'}；4 則同一值
[PASS]   2 §4.3.1           test_item 兩段式：上半 verbatim ≤50tok；下半存在且為英文；無 modal
         003: 上半子串 ✓/35tok、下半 有、中文 無、modal 無；004: 上半子串 ✓/45tok、下半 有、中文 無、modal 無；005: 上半子串 ✓/46tok、下半 有、中文 無、modal 無；006: 上半子串 ✓/45tok、下半 有、中文 無、modal 無；007: 上半子串 ✓/46tok、下半 有、中文 無、modal 無；008: 上半子串 ✓/45tok、下半 有、中文 無、modal 無；013: 上半子串 ✓/29tok、下半 有、中文 無、modal 無；014: 上半子串 ✓/47tok、下半 有、中文 無、modal 無；015: 上半子串 ✓/44tok、下半 有、中文 無、modal 無；016: 上半子串 ✓/47tok、下半 有、中文 無、modal 無
[PASS]  2b §4.3.1           同一 Requirement ID 衍生之列，括號下半不逐字相同
         無重複
[PASS]   3 §4.4/§8.5 + R-DD17 Pre-Condition 僅狀態／環境；無系統預設、待測前提、動作、step 可控狀態；訊號源行合 R-DD17 之形式（只書訊號源，不兼述環境）
         0 命中；4 則各 1 項且皆合 R-DD17 之形式（§4.5-1 環境資料）
[PASS]   4 §4.5             Input Test Data 歸屬正確；重複值移入 PC／Procedure 或設 NA
         4 則皆 NA=True；回指 無；跨欄重複 無
[PASS]   5 §5.1/§5.5        步驟無禁用動詞；Final Step 含 ACTION ＋ check target（preferred verb）
         禁用動詞 0 命中；末步缺 `check that` 無
[PASS]   6 §5.2             步驟長度：一般 ≤12 字、Final ≤18 字（含 action+check target）
         字數 {'newR1L-DD-B001': [8, 11, 8, 10], 'newR1L-DD-B002': [7, 11, 12], 'newR1L-DD-B003': [8, 8, 11], 'newR1L-DD-B004': [9, 11, 14], 'newR1L-DD-B005': [8, 8, 13], 'newR1L-DD-B006': [9, 11, 14], 'newR1L-DD-B007': [8, 15], 'newR1L-DD-B008': [11, 11, 16], 'newR1L-DD-B009': [8, 11], 'newR1L-DD-B010': [7, 11, 12]}
[N/A ]   7 §5.3             標準 setup 片語逐字重用
         本 feature 未定義 project-level setup 常數（feature.yaml 無該鍵）—— 無適用對象
[N/A ]   8 §5.4             CLI／tooling 步驟採 description + `$` 指令格式
         4 則皆為 HMI 操作與匯流排施加，無 CLI 步驟
[PASS]   9 §5.6             before／after 需要時建立 baseline
         003: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；004: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；005: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；006: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；007: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；008: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；013: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；014: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；015: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟；016: before 由 PC 載明（訊號 0）✓，ER 不比對已記錄值，故不需記錄步驟
[PASS]  10 §6               Procedure↔ER 1:1；ER 可觀察；ER 無 modal
         步驟 {'newR1L-DD-B001': 4, 'newR1L-DD-B002': 3, 'newR1L-DD-B003': 3, 'newR1L-DD-B004': 3, 'newR1L-DD-B005': 3, 'newR1L-DD-B006': 3, 'newR1L-DD-B007': 2, 'newR1L-DD-B008': 3, 'newR1L-DD-B009': 2, 'newR1L-DD-B010': 3}／ER {'newR1L-DD-B001': 4, 'newR1L-DD-B002': 3, 'newR1L-DD-B003': 3, 'newR1L-DD-B004': 3, 'newR1L-DD-B005': 3, 'newR1L-DD-B006': 3, 'newR1L-DD-B007': 2, 'newR1L-DD-B008': 3, 'newR1L-DD-B009': 2, 'newR1L-DD-B010': 3}；modal 無；非觀察語句 無
[PASS]  11 §7               無 FP／FF：含 setup／transition，不假設隱藏狀態；列舉支援項配負向
         FF：010／012 之 fail-safe 皆先建立正常態再注入故障，未假設隱藏狀態；FP：本 4 leaf 無列舉式支援項（無 format／device／protocol 之列舉），無配對義務
[PASS]  12 §8.1/§8.2/§8.4   追溯 Req/SWRA；不擴入 sibling；無造值；無範圍捏造
         req_id 形制 True；§8.4.2 禁詞 0 命中；數值母體 ['1', '129', '2', '3', '4', '4.8125', '5', '77', '8.0625']，逾 profile §3.1／編號者 無
[PASS]  13 §12              Design Method 於 procedure 定稿後指派，且合 first-match 序
         009/011 觸發為 A→B 狀態轉換，於 Scenario 前命中；010/012 為 simulated fault（停送＋逾時），於 State Transition 前命中；皆為下拉選單實值 True
[PASS]  14 §11 + R-DD11     四欄 numbered item 無作者所書之行尾句號（引號內字串之終端標點保留）
         0 違規
[PASS]  15 §11 + R-DD12(c)  UI 標籤用 `"..."`；方括號僅限 037 逐字之 test_item 上半與 A-DD6 marker
         0 違規；test_item 上半之 `[Normal]`／`[Exception]` 經比對為 037 逐字（R-DD12(a)）；單引號／角括號 無
[PASS]  16 §10.7            spec_reference 列出所驗之每一 spec 節；一行一 ObjectID、無串接
         003=CFTS022-4915105／004=CFTS022-4915105／005=CFTS022-4915106／006=CFTS022-4915106／007=CFTS022-4915107／008=CFTS022-4915107／013=CFTS022-4915112／014=CFTS022-4915112／015=CFTS022-4915115／016=CFTS022-4915115
[PASS]  17 §8.6/§8.7        門檻為 spec 溯源之具體值；相似操作於 ER 具名區辨；來源規格勝於索引匯出
         門檻具名 raw True（profile §3.1 依 R-DD7(c)）；A-DD6 marker True；ER 取樣具名 True
[PASS]   + §11              多行欄位無行首／行尾空白，空行為真空行
         0 違規
[PASS]   + profile §2.3     ER 不含 RESTRICTED／NOT_RESTRICTED／Locked／Unlocked
         0 命中
[PASS]   + §10.2            priority 為 P0–P3 且合 profile §4
         003=P1／004=P1／005=P1／006=P1／007=P0／008=P1／013=P0／014=P1／015=P0／016=P1
[PASS]   + §10.5            test_procedure 至少 2 個編號步驟
         {'newR1L-DD-B001': 4, 'newR1L-DD-B002': 3, 'newR1L-DD-B003': 3, 'newR1L-DD-B004': 3, 'newR1L-DD-B005': 3, 'newR1L-DD-B006': 3, 'newR1L-DD-B007': 2, 'newR1L-DD-B008': 3, 'newR1L-DD-B009': 2, 'newR1L-DD-B010': 3}
[PASS]   + R-DD16(b)        輸出 split_flag／split_reason；未拆者 false／"NA"
         缺鍵 無；值不合 無；鍵名依 R-DD16(a) 用 test_item／spec_reference（既有寫回形制）
====================================================================================
RESULT: PASS 21 ／ N/A 2 ／ FAIL 0　（共 23 檢）
```

### 9.2 pilot 回歸（`SC_ARTIFACT=pilot_group3.json`）

```
====================================================================================
TC 自檢 —— IN §9 十七項全跑 ＋ 追加項（骨幹；產物由 SC_ARTIFACT 指定）
====================================================================================
[PASS]   1 §4.1/§4.2        Test Set 名詞片語、能力層級、無 Test Group 前綴、拼寫一致
         {'Lockout Enforcement'}；4 則同一值
[PASS]   2 §4.3.1           test_item 兩段式：上半 verbatim ≤50tok；下半存在且為英文；無 modal
         009: 上半子串 ✓/25tok、下半 有、中文 無、modal 無；010: 上半子串 ✓/47tok、下半 有、中文 無、modal 無；011: 上半子串 ✓/25tok、下半 有、中文 無、modal 無；012: 上半子串 ✓/47tok、下半 有、中文 無、modal 無
[PASS]  2b §4.3.1           同一 Requirement ID 衍生之列，括號下半不逐字相同
         無重複
[PASS]   3 §4.4/§8.5 + R-DD17 Pre-Condition 僅狀態／環境；無系統預設、待測前提、動作、step 可控狀態；訊號源行合 R-DD17 之形式（只書訊號源，不兼述環境）
         0 命中；4 則各 1 項且皆合 R-DD17 之形式（§4.5-1 環境資料）
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
[PASS]   + R-DD16(b)        輸出 split_flag／split_reason；未拆者 false／"NA"
         缺鍵 無；值不合 無；鍵名依 R-DD16(a) 用 test_item／spec_reference（既有寫回形制）
====================================================================================
RESULT: PASS 21 ／ N/A 2 ／ FAIL 0　（共 23 檢）
```

---

## 10. T18b 掃描原始輸出

```
==============================================================================
T18b —— 訊號涵蓋掃描（B1 前置）
==============================================================================
母體：037 `Analysis Report` 之 leaf 001~008、013~016（**12 leaf**），**全 20 欄**逐格掃 `$...$`。
比對標的：profile §3 之五項。

------------------------------------------------------------------------------
逐 leaf 之 `$...$` token
------------------------------------------------------------------------------
  -001 (037 r9): （無 $…$ token）
  -002 (037 r10): （無 $…$ token）
  -003 (037 r11): ['Speedometer']
  -004 (037 r12): ['Speedometer']
  -005 (037 r13): ['Speedometer']
  -006 (037 r14): ['Speedometer']
  -007 (037 r15): ['Speedometer']
  -008 (037 r16): ['Speedometer']
  -013 (037 r21): （無 $…$ token）
  -014 (037 r22): （無 $…$ token）
  -015 (037 r23): （無 $…$ token）
  -016 (037 r24): （無 $…$ token）

------------------------------------------------------------------------------
已涵蓋（profile §3 五項之內）：1 個
------------------------------------------------------------------------------
  $Speedometer$  —— profile §3：解除 —— STATUS_CCAN3.VehicleSpeedVSOSig
      出現於 leaf：['003', '004', '005', '006', '007', '008']

------------------------------------------------------------------------------
**未涵蓋**（profile §3 五項之外）：0 個
------------------------------------------------------------------------------
  無

------------------------------------------------------------------------------
profile §3 五項中，本 12 leaf 未用及者：['Country_Code', 'PARK_BRK_EGD', 'PresentGear', 'VC_Trans_Equipped']

==============================================================================
B1 範圍判定（§6.2）
==============================================================================
  因**未涵蓋訊號**而剔除：無
  因**profile §3 標 SUSPENDED**而剔除：無
  **剔除合計**：無（0 leaf）
  **B1 範圍**：['001', '002', '003', '004', '005', '006', '007', '008', '013', '014', '015', '016']（12 leaf）
```

> **注意此輸出之末段判定「B1 範圍 = 12 leaf」** ——
> 那是**純 token 掃描**之結論，**已由 §3.2 之原文回讀推翻**。
> 保留原樣以示：**工具說 12，人讀 037 說 10。**
> 若只交這份輸出而不回讀原文，`-001`／`-002` 就會進批次。

---

## 11. 未結 DR 清單（DD1–DD7）

| DR | 狀態 | Leaves | 阻斷 |
|---|---|---|---|
| **DR-DD1** | DRAFTED（未發送）| `-025`~`-028`（4）| **凍結** |
| **DR-DD2** | DRAFTED（未發送）| `-021`~`-024`（4）| 不阻斷 |
| **DR-DD3** | ANSWERED-PENDING-CONFIRM | `-017`~`-028`（12）| 不阻斷；標 A-DD5 |
| **DR-DD4** | DRAFTED（未發送）| 9 列書 MPH 者 | 不阻斷；標 A-DD6 |
| **DR-DD5** | DRAFTED（未發送）| `-017`~`-024`（8）| 不入批次 |
| **DR-DD6** | DRAFTED（未發送）| `-017`~`-024`（8）| 不入批次 |
| **DR-DD7** | DRAFTED（未發送）| **文稿只問 `-010`／`-012`**；實測涉 11 leaf | 不阻斷；**範圍待裁**（§5.1）|

**七筆皆未發送。** 另 `-001`／`-002` 之處置（§3.3）**尚無 DR 承載** —— 待分析層定其性質。

### 11.1 阻斷疊圖（本輪後）

```
-001 ~ -002  (2)   **B1 剔除** —— Body OFF 電源域，無具名識別碼；四庫查對無從進行（§3.3）
-003 ~ -008  (6)   **B1 已生成**；-003/-005/-007 帶 A-DD6；-004/-006/-008 屬 A-DD7 組 1
-009 ~ -012  (4)   pilot 已修訂；-010/-012 屬 A-DD7 組 2
-013 ~ -016  (4)   **B1 已生成**；-013/-015 帶 A-DD6；-014/-016 屬 A-DD7 組 2
-017 ~ -024  (8)   A-DD5 ＋ DR-DD5 ＋ DR-DD6（+DR-DD2 於 021-024）；-018~-024 另屬 A-DD7 組 3/4
-025 ~ -028  (4)   A-DD1 凍結 ＋ A-DD5
```

**已生成 14 TC**（pilot 4 ＋ B1 10）／28 leaf。

---

## 12. T17b —— 維持停止

依 §二，**popup 線 commit 並重生前不續行**。本輪未重跑第 5 步歸因，
**亦未觸及 `docs/fw036/RULINGS.sha.tsv`**。

> ⚠ 一項狀態變化：上輪 commit 後觀察到該 tsv **已成 modified**（他線所為）。
> 本輪未查其內容 —— **查了也不改判定**（解除之條件是 popup 線 commit 並重生，
> 非該檔一時之狀態）。**待其定稿。**

**本線之 18 列已可被任何一次重生正確收錄，無時序要求。**

---

## 13. 獨立自評

### 13.1 我做對的

- **沒有信任自己的掃描結果。** T18b 的 token 掃描給出「12 leaf，0 未涵蓋，
  不必剔除」—— 那是照下放包 §6.1 的字面問法問出來的答案。
  **回讀 037 原文才看到 `-001`／`-002` 的激勵根本不是訊號。**
  §10 保留了那份會誤導的機器輸出，並在旁邊寫明它為何錯。
- **A-DD7 是量出來的，不是猜出來的。** 讀 `-014`／`-016` 時覺得眼熟，
  就寫了一個以 18 欄為鍵的分組，得到 4 組 11 leaf。
  **「眼熟」不是結論，分組才是。**
- **`-013` 的方向查了。** 下放包 §6.2-4 把它列為解鎖方向；照抄會給它 raw 77，
  而 037 的 Method 逐字寫 `send a speed above 5 MPH`。
- **自檢從硬編改為推導。** 上一輪的期待值（design_method／spec_reference／
  priority／A-DD6 標記）全是按 leaf 號硬編的，換一批 leaf 就失效。
  本輪改為由 037 之 AC 別、profile §1 對照表、profile §4 之 P0 集合、
  以及 procedure 是否含 raw 值推導 —— **pilot 回歸仍 21 PASS，B1 直接可用。**

### 13.2 我做糙的

- **自檢第 9 項因 R-DD17 而假 FAIL**（§4.1）。改 TC 形制時沒有同步想到
  哪些檢是用字面比對咬著那個形制的。**改形制要連檢查器一起看。**
- **B1 步驟 1 三處超字數**是我寫的時候沒算。長標籤（8 token）撐爆 12 字上限
  這件事，pilot 那輪就該學到。

### 13.3 我拒絕做的

- **不臆造 `-001`／`-002` 的施加路徑。** 037 沒給名，就沒得查四庫。
  去 LID 搜 `Body`／`Sleep`／`Power` 的近似名是 R-13 所禁之代換。
- **不改 DR-DD7 之文稿**去涵蓋新測到的 9 個 leaf —— 那是待發送的逐字稿。
- **不取 `Database Entry - License Key Entry`** 作取樣。它非黃標，取了會過檢，
  但它緊接 NAV 區塊之末，是否屬 NAV 系未經確認。**未查即不取。**
- **不改 §5.2 的尺**（R-DD15(d)），改步驟。

### 13.4 一件我原本會漏的

`-003` 我差點拆成兩則（上鎖一則、解鎖一則）——**拆了會過檢**，
`split_flag: true` 加個理由就行。

但那樣產出的兩則，會與 `-007`（`-116`，上鎖）和 `-005`（`-115`，解鎖）
**幾乎重複** —— 而那兩者各有自己的 source。
**`-003` 的 source `-114` 要驗的是「5/3 規則作為一個整體」**，
拆開反而把它驗沒了。§5.7 的「one trigger → multiple outcomes」正是這件事。

---

## 14. 量測條件揭露（R-G8）

### 14.1 本包所書比率之分子與分母

| 計數 | 分子 | 分母 |
|---|---|---|
| 18 錨點 | 工具對本檔解析出之 `ruling` 列數 | 本檔圍籬條文 18（17 現行 ＋ 1 留存）|
| 既有 14 條 sha8 未變 | 上輪 tsv 與本輪 tsv 之 `sha8` 相同者 | 上輪之 14 條 |
| A-DD7：4 組／11 leaf | 以 18 欄為鍵、組內 ≥2 之組數／其涵蓋之 leaf 數 | 037 全 **28** leaf |
| `$…$` 已涵蓋 1／未涵蓋 0 | 相異 token 數 | 12 leaf ×全 20 欄之全部 `$…$` 命中 |
| B1 = 10 leaf | 未被剔除者 | T18b 母體 12 leaf |
| 已生成 14 TC | pilot 4 ＋ B1 10 | 037 全 28 leaf |
| B1 自檢 21 PASS／2 N/A／0 FAIL | 各判別之檢項數 | 23 檢（IN §9 十七項 ＋ 追加 6）|
| §5.2 超限 3 處 | 字數 > 該角色上限之步驟數 | B1 全部步驟 **29 個**（10 則，步數 4/3/3/3/3/3/2/3/2/3）|

### 14.2 界線

- **`$…$` token 之擷取正則為 `\$([^$\s]+)\$`** —— 若 037 以其他記法表述識別碼
  （如裸名、方括號），**掃不到**。`-013`~`-016` 即為此類（散文表述），
  本輪由回讀原文補上；**`-017` 以後未以本法覆核**（非本輪範圍）。
- **A-DD7 之分組鍵為「除 c0／c1 外之 18 欄」之 `str()` 值**，未做正規化 ——
  全形／半形、前後空白之差一律計為不同。**故本法可能低估**（漏掉「幾乎相同」者），
  不會高估。
- **黃標偵測**同上繳 07 §9.4：依賴 rect 填色；黃 rect 只覆蓋類別欄，
  以垂直區間認定整類不適用，**該讀法仍未經上游確認**。
- **`-003` 之 63 token 與 `-013` 之 62 token** 以 `str.split()` 計（R-DD15(a)）。
- **自檢之 `_ALL` 對照表以 `037 列 = 8 + leaf 號` 建**，
  本輪對 `-003`~`-016` 逐一驗證相符；**`-017` 以後未驗**。

### 14.3 檔與開啟方式

| 標的 | 開啟 |
|---|---|
| `RULINGS.md`／`ANOMALIES.md`／`generated/*.json` | **本輪寫入**（皆私有路徑）|
| 037／HMI spec PDF／profile／IN | **唯讀** |
| `docs/fw036/RULINGS.sha.tsv` | **未開**（T17b 停止）|
| 工作簿 | **未開** |

### 14.4 本輪未量測者

- **`-001`／`-002` 之激勵於四庫中之對應** —— 無具名識別碼，無從查（§3.3）。
- **`-017`~`-028`** —— 非本輪範圍。
- **B1 十則未經工作簿寫回驗證** —— 拘束「不寫回」，
  `split_flag`／`split_reason` 是否為寫回器所受（R-DD16(c)）本輪無從得知。
- **`Database Entry - License Key Entry` 是否屬 NAV 系** —— 未查，故未取（§6.2）。

---

## 15. 待分析層／Pei

| # | 事項 | 現況 |
|---|---|---|
| 1 | `RULINGS.md` 體例（其餘 4 feature，**144 條**）| 未代改；本 feature 已轉換 |
| 2 | tsv 重生之解除 | **T17b 維持停止**，待 popup 線 commit 並重生 |
| 3 | **`-001`／`-002` 之處置** | **無 DR 承載**；三案（甲索取具名識別碼／乙逕登 DR／丙判為台架能力）見 §3.3 |
| 4 | **DR-DD7 之範圍** | 文稿只問 2 leaf，實測涉 **11**；5 則在本輪 B1 內（§5.1）|
| 5 | 下放包 §6.2-4 之 `-013` 方向 | **已更正為上鎖**（§3.5）；B1 據更正值生成 |
| 6 | B1 十則之審查 | 23 檢 21 PASS／2 N/A／0 FAIL |
| 7 | `-017` 以後之批次 | 待令；其阻斷見 §11.1 |
