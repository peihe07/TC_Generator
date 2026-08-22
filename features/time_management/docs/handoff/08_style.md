# 下放包 08 — 交付件實測：functional_safety、D5、樣式常數

分析層 → 執行層。往返編號 `08`。對應上繳 `docs/upstream/08_style.md`。

Pei 於 2026-08-22 授權分析層查閱既有交付件。**本包之全部依據為實測**，
受測物：

```
/Users/peihe/Work/02_Project_R1LR/10_Reviewing/00_TestCase/ASW-R2/
User Profiles/FM-WI-FSM-036-A01 …_SWQT_UserProfiles_20260820.xlsx
```

選用理由：**最近一次交付**（2026-08-20），且為 rev C 版面
（實測 34 欄，S = Functional Safety、R = Design Methods、AA = Author，
與 FORMS.md 之母本對映逐項一致）。資料列 **189**。

**Home 之複本不採為本包依據** —— A-TM14 已載其身分不可判定
（兩份同名、SHA 相異），且其 D5 為 A-H26 之缺陷值本身。

---

## 1. `functional_safety` —— **`NA`**，189/189 單值

```
S 欄值分佈：Counter({'NA': 189})
```

**全 189 列同值，無例外。** A-TM24 之來源 2（既定慣例）由實測取得。

```
R-TM57（分析層裁定，2026-08-22，依 Pei 授權之交付件實測）—— functional_safety

CONST_FUNCTIONAL_SAFETY = "NA"

依據：交付件 UserProfiles_20260820 之 S 欄 189/189 皆為 `NA`，單值無例外。

此 `NA` 為 canon §8.4.3 所稱之「確認不適用」，非缺件佔位 ——
Time and Date 與 User Profiles 同屬 HMI 功能，無功能安全需求分派
（037 之 Categorization 欄實測 22/22 皆 `Functional`，無任何 safety 分類；
且 SYS2 與 037 皆無 ASIL / FTTI 欄，04Z-A2 §2 已實測）。
兩條獨立證據同向。

A-TM24 轉 RESOLVED。write_back 之 unresolved 檢查於此項不再攔截。
```

## 2. **D5 Scope —— 實測為空，我先前的訂正錯了**

```
C5: '範圍 Scope：'
D5: None
```

**最近一次交付件之 D5 為空。**

這推翻了 `05Z` §2.1 之 R-TM9-A2 處置訂正（我依 canon §8.4.3 將 D5 由
「維持空白」改為填 `PENDING: DR-{n}`）。

**兩項理由使我認為應回到「維持空白」**：

1. **canon §8.4.3 之射程為 TC 資料欄，非表頭欄。** 該節之語境為
   「欄位無法填寫」，其列舉與判準皆指逐列之 TC 欄位；D5 為工作簿層之
   單一表頭格，逐列規則不當然及之。
2. **唯一可測之正確交付實例為空。** 兩個 D5 樣本中，Home 之複本為
   A-H26 之缺陷值（指向另一 feature 之 037），UserProfiles 為空 ——
   **即「有值」那個實例正是被判定為錯的那個。**

```
R-TM58（分析層裁定，2026-08-22）—— D5 維持空白，撤回 PENDING 佔位

R-TM9-A2 之處置訂正（05Z §2.1，將 D5 改填 `PENDING: DR-{n}`）**撤回**。
D5 依原裁定**維持空白**。

依據：
1. 交付件 UserProfiles_20260820 之 D5 實測為空（C5 標籤 `範圍 Scope：`
   存在，值格為 None）
2. canon §8.4.3 之射程為逐列 TC 資料欄，非工作簿層之表頭格
3. 兩個可測樣本中，有值者（Home 複本）即 A-H26 之缺陷值本身

**A-TM02a 不因此結案** —— 037 之身分仍未定，仍隨 RD-1 上問；
但其「阻塞 D5」之性質解除，D5 空白為交付先例所支持之狀態。

lint 之 B1（`lint_d5_scope`）判準隨之改回：**D5 為空即通過**，
不再要求 `PENDING: DR-` 佔位。其存在意義改為「偵測 D5 被誤填」——
若 D5 非空且非合法 037 檔名，報 A-H26 同型缺陷。
```

**同批實測另得（供交叉驗證）**：`D2 Project Name = 'newR1L'`、
`J5 Date = '2025/10/17'`、`C3 Reviewer` 與 `C4 Purpose` 之值格皆空。

## 3. 樣式常數 —— 三項可用、兩項不可用、**兩項不得抄**

### 3.1 可用（與 canon 一致，直接沿用）

| 項 | 交付件實測 | canon | 處置 |
|---|---|---|---|
| `tc_id` | `NR1L-UserProfiles-001` … `-189` | §10.3 | **R-TM32 之 `NR1L-TimeAndDate-{n:03d}` 獲第二個實例佐證** |
| Input Test Data | `NA` 159/189（84%） | §4.5 | 沿用；非 NA 者為真實資料集（`Preference u…`、`Fault inject…`）|
| Pre-Conditions | 逐條編號、一條一行、無句尾句點 | §11、R-9 | 沿用 |
| ER | 逐條編號對應步驟、無句尾句點<br>（`1. Driver Profile A is active`）| §6、§11 | 沿用 |
| design_method | **中英雙語**：`功能測試 (Functional based ; no specific technique)`、`狀態轉換 (State Transition Testing)` 等 6 種 | §12 | **重要** —— 我方 lint 讀母本 `下拉選單`，須確認其為同一雙語字串，非純英文 |
| priority | P0 38 / P1 66 / P2 71 / P3 14 | §10.2 | 值域相符；**分佈不移植**（分佈屬內容裁決）|

### 3.2 不可用（既有常數對本 feature 無一適用）

交付件之高頻步驟為 `Open the "All Profiles" tab`(15)、
`Open the "Edit Profile" tab`(10)、`Activate Valet Mode`(6)、
`Activate Driver Profile B`(5) —— **全部為 User Profiles 專屬 UI**。

`ENTER_DEALER_MODE` / `ENTER_ENG_MODE` / `SCREEN_OFF` / `ENTER_APP_DRAWER`
亦與 Time and Date 之情境無交集。

**故本 feature 之步驟常數須自擬**，此與 R-TM10-A1 無關 ——
不是不准抄，是**沒有可抄的**。§3.4 為擬定之常數表。

### 3.3 **不得抄之兩項 —— 交付件與 canon 牴觸**

**(a) 彎引號**：交付件用 `“All Profiles”`（U+201C / U+201D），
canon §11 明訂 UI 標籤用直雙引號 `"..."`，並明列 `'...'`（單引號）、
`<...>`、`[...]` 為禁用。彎引號未在禁用列舉中，但亦非 §11 所示之形式。

**(b) `check whether` 作主要動詞**：交付件有
`Read the screen and check whether the popup is displayed`（7 次）。
**canon §5.1 明列 `check whether` 為禁用主要動詞**
（`observe`、`observe whether`、`see if`、`check whether`、
`confirm whether`、`verify` …），因其把判斷推給測試者。
§5.1 之正解為 `Check that <具體可觀察目標>`。

```
A-TM25（PENDING，Tier 2 —— 呈 Pei）

既有交付件（UserProfiles_20260820）與 canon 有兩處牴觸：

(a) UI 標籤用彎引號 `“…”`（U+201C/U+201D）；canon §11 示直雙引號 `"…"`
(b) `check whether` 作主要動詞 7 處；canon §5.1 明列其為禁用主要動詞

**本 feature 依 canon**（(a) 直引號、(b) `Check that <具體目標>`），
理由：canon 為規則之權威來源，交付件為其套用之結果，
結果與規則牴觸時以規則為準（§8.6 之同一位階原則）。

**但此使本 feature 之交付件與既有交付件在此二處外觀不同**，
審閱者可能視為不一致。**呈 Pei 知悉**；若 Pei 認為應與既有交付件一致，
則須反向修改 canon 或立 feature profile 之 [OVERRIDE]，
不得由本 feature 逕自偏離 canon。

**不建議回頭修改既有交付件** —— 已交付，且 (b) 涉 7 條 TC 之措辭。
```

### 3.4 本 feature 之步驟常數表（**[PROPOSED]，待 Pei 過目**）

依 canon §5.1–5.3 自擬。全部為 Time and Date 情境專屬，
與既有專案常數無重疊（§3.2）。

```python
# features/time_management/scripts/tm_constants.py  [PROPOSED]
# 依 canon §5.3；本 feature 專屬，與既有專案常數無交集（08 §3.2 實測）

SET_TIME_MANUAL   = 'Open the "Time and Date" settings and set the time manually'
SET_DATE_MANUAL   = 'Open the "Time and Date" settings and set the date manually'
GPS_SYNC_ON       = 'Set "Sync Time with GPS" to ON'
GPS_SYNC_OFF      = 'Set "Sync Time with GPS" to OFF'
BATTERY_RECONNECT = 'Disconnect and reconnect the vehicle battery'
KEY_OFF           = 'Turn the ignition to OFF'
KEY_ON            = 'Turn the ignition to ON'
CAN_SLEEP         = 'Wait until the CAN bus enters sleep'
CAN_WAKE          = 'Wake the CAN bus'
GPS_LOST          = 'Remove the GPS antenna to make the GPS signal unavailable'
GPS_RESTORE       = 'Reconnect the GPS antenna to restore the GPS signal'
READ_HU_TIME      = 'Read the time shown on the HU display and record it'
READ_IPC_TIME     = 'Read the time shown on the IPC display and record it'
```

**設計說明**（供 Pei 判斷）：

- 全部為 **動作 + 目標**，無禁用動詞（§5.1）；`READ_*` 用 `Read … and
  record it`，`record` 為 §5.1 之 preferred verb
- 直雙引號（§11、A-TM25(a)）
- 無句尾句點（§11）
- `GPS_LOST` 之措辭為**物理操作**而非「使 GPS 不可用」之抽象敘述 ——
  §5.1 要求可執行
- **未含 Final Step 措辭** —— 該類須逐 TC 依驗證目標寫（§5.5），
  不宜常數化

**ER 樣板不擬常數** —— canon §6 要求 ER 與步驟 1:1 且描述具體可觀察結果，
樣板化會誘導套用而非依實際結果撰寫。**只沿用其形式慣例**
（逐條編號、無句尾句點、無 modal verb）。

---

## 4. 指令

### T0

```bash
cd /Users/peihe/Work_Projects/TC_Generator
```

### T1 — `RULINGS.md`：追加 R-TM57 / R-TM58

標題行 `## R-TM57 — functional_safety = "NA"`、
`## R-TM58 — D5 維持空白，撤回 PENDING 佔位`，內文為 §1 / §2 之區塊全文。

R-TM9-A2 之 `05Z` 訂正段**依 R-TM13 加刪除線保留**，其下加註指向 R-TM58。

**增量**：`## R-TM` **+2**；`## A-TM` **+1**（A-TM25）；`## G-TM` **0**。

### T2 — `ANOMALIES.md`

- **A-TM24 轉 RESOLVED**，條末追加 R-TM57 之依據摘要
- **A-TM25 新增**，內容為 §3.3 之區塊全文，索引追加：

```markdown
| A-TM25 | 既有交付件與 canon 兩處牴觸（彎引號、check whether） | PENDING | Tier 2（呈 Pei）|
```

### T3 — `write_back.py`：填入 `CONST_FUNCTIONAL_SAFETY`

`CONST_FUNCTIONAL_SAFETY = "NA"`（R-TM57），撤除其 `TODO(R-TM10-A1)` 標記。
**red-green**：綠向 —— unresolved 檢查不再攔；紅向 —— 暫改回 `None`
應仍攔（證明該檢查未被削弱）。

### T4 — `lint_tcs.py`：B1 判準改回（R-TM58）

`lint_d5_scope` 由「未含 `PENDING: DR-` 即報」改為
「**D5 為空即通過；非空且非合法 037 檔名形態即報**」。

**red-green**：綠向 —— D5 為空不報；紅向 —— D5 填入
`FM-WI-FSM-037-A03-N1L-SWE1-AppDrawer-HMI-V0.1 STLA 報告`
（他 feature 之 037，即 A-H26 形態）應報。

### T5 — design_method 雙語字串核對（§3.1 之「重要」項）

讀母本 `下拉選單` 分頁 `$A$1:$A$9`，與交付件 R 欄實測之六種值比對：

```
功能測試 (Functional based ; no specific technique)
狀態轉換 (State Transition Testing)
負向測試 (Negative / Invalid)
情境 / 用例 (Scenario / Use Case Testing)
邊界值分析 (Boundary Value Analysis, BVA)
基礎故障注入 (Fault Injection Lite)
```

**逐字比對**（R-TM31：列出兩側全集，不只計數）。母本應有 9 條，
交付件用到 6 種 —— 確認交付件之 6 種**逐字**屬母本 9 條之子集。
不符即回報並停：那代表我方 lint 之 design_method 詞彙表取錯來源。

### T6 — `tm_constants.py`（**待 Pei 過目後才建**）

**本包不建**。§3.4 為 [PROPOSED]，待 Pei 過目。
執行層於上繳中就該表提出**技術面**意見（措辭是否可執行、是否有遺漏之
高頻情境），不就內容是否恰當表態 —— 後者屬 Pei。

### T7 — 驗證（R-TM31 列明細；R-TM46 增量）

```bash
grep -n '^## R-TM5[78]' features/time_management/RULINGS.md
grep -n '^| A-TM24\|^| A-TM25' features/time_management/ANOMALIES.md
grep -n 'CONST_FUNCTIONAL_SAFETY' features/time_management/scripts/write_back.py
grep -rn 'TODO(R-TM10-A1)' features/time_management/scripts/   # 逐處列出並判定各自依據
python3 features/time_management/scripts/lint_tcs.py --self-test
python3 features/time_management/scripts/build_batch_context.py --self-test
```

### T8 — 上繳

`docs/upstream/08_style.md`。依 R-TM54 三分列未驗清單。
須含 T7 全部輸出、T3/T4 之 red-green、T5 之雙語字串逐字比對、
T6 之技術面意見。

### 不得執行者

- 不動 git（除非 Pei 直接指示）
- **不生成任何 TC**
- **不建 `tm_constants.py`**（待 Pei 過目）
- 不修改既有交付件（A-TM25 明列不建議）
- 不改 `backend/`、不改 canon、不改 `docs/fw036/framework.md`
- 不將 022 加入 `BOUNDARY_SIGNALS`（R-TM55）
- 不杜撰 CAN 網段
- 不碰 `features/vehicle_setting/`
- 不送出 RD-1

---

## 5. 呈報 Pei

1. **A-TM25 —— 交付件與 canon 兩處牴觸**（彎引號、`check whether`）。
   本 feature 依 canon，但外觀會與既有交付件不同。若你要求一致，
   須改 canon 或立 profile `[OVERRIDE]`，不得由本 feature 逕自偏離。
2. **§3.4 之步驟常數表**待你過目。全部為 Time and Date 專屬 ——
   既有常數（Dealer Mode / Eng Mode / Screen Off / App Drawer）
   與本 feature 無交集，**不是不准抄，是沒有可抄的**。
3. RD-1 Q-TM1–3 + N-TM1 已備齊，送出屬你。

**A-TM24 與 R-TM10-A1 兩項阻塞，本包後皆解除**（前者裁定 `NA`，
後者證實無適用之既有常數而改自擬）。**B1 之啟動只等 §3.4 過目。**

## 6. 本包產生之新條文清單（自檢 —— R-TM14）

| 編號 | 形態 | 區塊 | 指令段指派 |
|---|---|---|---|
| R-TM57 | 分析層裁定，functional_safety = NA | §1 | ✅ T1 + T3 |
| R-TM58 | 分析層裁定，D5 維持空白（撤回訂正）| §2 | ✅ T1 + T4 |
| A-TM24 → RESOLVED | anomaly 結案 | §1 | ✅ T2 |
| A-TM25 | anomaly，PENDING，Tier 2 | §3.3 | ✅ T2 |
| 步驟常數表 | [PROPOSED]，待 Pei | §3.4 | ⏸ T6（不建）|

分析層本包未動 git、未改任何腳本、未改 canon、未改交付件。
交付件之讀取為唯讀複本解析，來源檔未被開啟寫入。
