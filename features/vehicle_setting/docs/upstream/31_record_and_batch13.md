# 上繳 31 —— record 子句之處置、batch13、交付本樣式比對

執行層寫入。依據：`docs/handoff/56_review_round34.md` §4（35 輪指令）。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔（六節先留空） | ✅ |
| D-2 | 逐字轉錄 R-VS54 入 RULINGS.md | ✅ |
| D-3 | profile 增列 56 包 §2 之三項 | ✅ |
| D-4 | A-VS107 關閉；A-VS105／A-VS106 標已更正；R-VS35 兩數 | ✅ |
| D-6 | 骨架 ⬜／✅ 對照各節實際內容 | ✅ |
| **W-95** | 42 處 record 子句之處置（依 56 包 §2） | ✅ 42/42，錨點可失敗 |
| **W-91** | batch13 —— 10 條 | ❌ **交付 0** —— 見 §2.2，**升級條件命中** |
| **W-97** | 交付本其餘四欄之樣式比對 | ✅ 不一致 **2** 欄，升級**未命中** |

---

## 1. 預期 vs 實測（相符者亦列出）

| # | 預期 | 實測 | 判 |
|---|---|---|---|
| 1 | W-95(1)：42 處逐處判有無後續引用 | **無引用 22／用於比較 20**，合計 42 | 相符 |
| 2 | W-95(2)：無引用者刪除 record 子句 | 22 處改為 `Read … and check that it is <值>` ＋ ER `<X> reads <值>` | 相符 |
| 3 | W-95(3)：有引用者命名並改 ER | 20 處命名（`*_initial` 等）；改寫後具名 record 步驟 **30**（本輪 20 ＋ 34 輪既有 10） | 相符 |
| 4 | W-95 後：`record` 而無變數名者為 0 | **0**（改寫前 42） | PASS |
| 5 | W-95 後：`recorded in step N` 者為 0 | **0**（改寫前 27 行） | PASS |
| 6 | W-95(4)：錨點須可失敗 | **新版 0 項／錨點（改寫前舊版）69 項**，十一批中十批之錨點命中（batch12 無 TC，不適用） | PASS，可失敗 |
| 7 | W-95：不得順帶改動非訊號書寫之欄位 | 九欄逐條比對，變動 **0 處** | 相符 |
| 8 | W-95：訊號斷言不受影響 | 149 處 `<MSG>.<Sig> = <raw> (<label>)` **逐字相同** | 相符 |
| 9 | §9 十七項自檢（機械化部分） | 十一批 **0 項** | 相符（**惟須連同 #6 之錨點讀，R-VS54**） |
| 10 | DBC 值表核對（L-VS2／R-VS39） | 0 不符；錨點於舊版命中 | 相符 |
| 11 | W-91 之池：`generatable = 108`，扣已交付 76，**餘 32** | **餘 36** | **不符** → §2.1 |
| 12 | W-91：batch13 交付 10 條 | **交付 0** | **不符** → §2.2；**升級條件「W-91 交付 < 5」命中** |
| 13 | W-97(1)：四欄逐欄列交付本形態與本 feature 形態 | 四欄全列，見 §3.3 | 相符 |
| 14 | W-97(2)：不一致者逐項列出，**不自行對齊** | 不一致 **2 欄**（`design_method`／`priority`），未對齊 | 相符 |
| 15 | W-97(3)：`test_item` 之上下段結構（R-VS6）於交付本是否存在 | **存在**，285/286 = **99.7%** | 相符 |
| 16 | W-97 之升級門檻：不一致欄位 ≥ 3 | **2** | 升級**未命中** |
| 17 | A-VS105 之更正是否成立（D-4） | `writability_driver.py --diff` 得 W0 129／W1 2／W2 106，**逐 leaf 不一致 0** | 相符 |

## 2. 不符項目（不自行調和）

### 2.1 池數 32 vs 36 —— 指令之減法未扣掉「已交付但不在池內」者

35 輪指令載「`generatable = 118`，扣已交付 76，餘 42」（54 包）與
「`generatable = 108`，扣已交付 76，**餘 32**」（56 包）。

實測：`generatable = yes` **108** 條中，**已交付之 76 條只有 72 條在池內**，
另 4 條已交付而現判 `generatable = no`：

| leaf | 現行 writable |
|---|---|
| `SWE1-VC-LeftFrontHeatedSeat-014` | W2（A-VS108，DR-15） |
| `SWE1-VC-RightFrontHeatedSeat-031` | W2（A-VS108，DR-15） |
| `SWE1-VC-SwitchLHD/RHDConfiguration-012` | W2 |
| `SWE1-VC-ThirdRowHeadrestDump-038` | W2 |

故 108 − 72 = **36**，非 108 − 76 = 32。**本層未調和** ——
差額 4 與 A-VS108 之「已交付 2 條經 pilot #2 而後被重生產物判 W2」同源。

### 2.2 W-91 交付 0 —— 池 36 逐 leaf 全數不可寫

**升級條件「W-91 交付 < 5」命中。以下為逐 leaf 之判定，不自行繞道。**

| 類 | 數 | 判 | 登記 |
|---|---:|---|---|
| 斷言目標訊號不在基線 DBC | **33** | L-VS2 必 FAIL | **A-VS110**／**DR-25** |
| 條文自帶值而 token 為 DR-15 標的 | **1** | `guard` 未被呼叫，實際應攔 | **A-VS111** |
| 節定義式前言，無可測內容 | **1** | W-87 之四式未涵蓋 | **A-VS109** |
| 「all other signal values」須跨條文取值，該 token 為 DR-8 標的 | **1** | 跨條文引入屬裁定事項 | **A-VS112** |
| **合計** | **36** | **可寫 0** | |

**33 條之細節**（A-VS110／DR-25）：其 `THEN` 賦值目標為
`TELEMATIC_VEHICLE_SETUP.FL_HS_Cmd_Tlm`(11)／`.FR_HS_Cmd_Tlm`(11)／
`TELEMATIC_VEHICLE_SETUP2.FL_VS_Cmd_Tlm`(11)，
三者於基線兩檔之 `SG_` 命中**各為 0**。
該 33 條之 `EE Architecture` 皆為 `Atlantis Mid`。

**三者同時成立**：依 R-VS19″ 在母體內；依 R-VS51(2) 其值域取 LID `Atlantis`
欄組且**確有值域**（列 763，`0 = Heated_seat_off` … `3 = Heated_seat_high`）；
而依 R-VS9(1)′ ＋ L-VS2，**訊號拼寫以 DBC 為權威而 DBC 沒有它**。

**未採之三路，逐一具名**：
1. 以 `Atlantis High` 之對稱訊號（列 762 `TELEMATIC_VEHICLE_SETUP3.FL_HS_Tlm`）
   代之 —— **跨列引入**，與 A-VS103 之處置一致，屬裁定事項
2. 略去訊號斷言、只驗 HMI 顯示 —— **驗證目標即該命令訊號**，略去則該 leaf 無 TC 可言
3. 放寬 L-VS2 —— 其為 R-VS9(1)′ 之配套 lint，執行層不得自裁

### 2.3 W-95 之 42 處中，1 處不是值之記錄

`SWE1-VC-ScreenOFF-051` 步驟 1 原為
`Start a bus trace on CAN-B and record the frames carrying TGW_DISP_STAT` ——
其 `record` 指**匯流排 trace 之錄製**，非 R-VS52(2) 所指之「記錄一個值供後續比較」。

**A-VS107 之 42 為形態計數，此 1 處為其偽陽性。**
本層之處置：改寫為 `… that captures the frames …`（ER 同步改 `is capturing`），
**去其與 record 子句之措辭衝突，不改其語意**。列此以免 42 之組成被誤讀。

### 2.4 W-95 之 22 處中，1 處之值非原 ER 所載

`SWE1-VC-ThirdRowHeadrestDump-038` 步驟 2 之原 ER 為
`The state of the virtual "Rear View Camera" button is recorded` —— **未載值**。
其餘 21 處之原 ER 皆自帶值（`is selectable`／`is displayed as off` 等），
刪除 record 子句只是去掉後半句。

本處改為 `not selectable`，其依據為**該 leaf 自身之 tc_title 與條文**
（`selectable only at ignition run`）—— 即「only at RUN」之反面。
**此為推論而非轉錄**，列此供覆核；若判其為造值，退回原形態並改列為
「無值可寫，維持記錄形態」，本層不自行決定。

## 3. 結果三分法（canon §8.4）

### 3.1 已驗且相符

- W-95 之全部四項驗收（§1 之 #4／#5／#6／#7）
- §9 十七項自檢之機械化部分：十一批 0 項，**且錨點於舊版命中 69 項**
- DBC 值表核對：149 處訊號斷言逐字未動、L-VS2／R-VS39 0 不符
- A-VS105 之更正：驅動與產物逐 leaf 不一致 **0**
- W-97(3)：`test_item` 之兩段結構於交付本存在（99.7%）

### 3.2 已驗而不符 —— 已於 §2 逐項說明，未調和

- 池數 32 vs **36**（§2.1）
- W-91 交付 **0**（§2.2）—— **升級條件命中**
- `design_method`／`priority` 兩欄與交付本不一致（§3.3）—— **未自行對齊**（禁區）

### 3.3 W-97 —— 四欄逐欄之實際形態（**只列，不對齊**）

| 欄 | SWC 0708 交付本（286 列） | 本 feature（76 條） | 判 |
|---|---|---|---|
| `test_item` | 兩段結構 285/286（99.7%）；以 `)` 收尾 285/286；含 `$var$` 179/286（62.6%）；平均 6.74 行 | 兩段 76/76（100%）；以 `)` 收尾 76/76；含 `$var$` 45/76（59.2%）；平均 3.00 行 | **一致**（行數差源於來源條文長度，非樣式） |
| `pre_conditions` | 編號清單 285/286（99.7%）；平均 4.45 項 | 編號清單 76/76（100%）；平均 2.83 項 | **一致**（項數差非樣式） |
| `design_method` | **受控下拉選單，9 值，形態為 `中文 (English)`**：`功能測試 (Functional based ; no specific technique)` 48／`決策表 (Decision Table Testing)` 70／`負向測試 (Negative / Invalid)` 50／`基礎故障注入 (Fault Injection Lite)` 20／`狀態轉換 (State Transition Testing)` 86／`邊界值分析 (Boundary Value Analysis, BVA)` 10／`情境 / 用例 (Scenario / Use Case Testing)` 1／空 1 | **純英文，5 值**：`State Transition` 50／`Decision Table` 4／`Functional Based` 12／`Equivalence Partitioning` 5／`Negative / Invalid` 5 | **不一致** |
| `priority` | `P0` 27／`P1` 190／`P2` 68／空 1 | `P1` 64／`P2` 12 —— **無 P0** | **不一致** |

**`design_method` 之不一致不只是樣式**：交付本該欄為 `下拉選單` 分頁所定之
**受控值域**（9 值），本 feature 之 5 值皆為其英文半段之改寫。
五者於該值域中皆有逐字對應項：

| 本 feature | 交付本之受控值 |
|---|---|
| `State Transition` | `狀態轉換 (State Transition Testing)` |
| `Decision Table` | `決策表 (Decision Table Testing)` |
| `Functional Based` | `功能測試 (Functional based ; no specific technique)` |
| `Equivalence Partitioning` | `等價劃分 (Equivalence Partitioning, EP)` |
| `Negative / Invalid` | `負向測試 (Negative / Invalid)` |

**對映為一對一且無歧義，惟本層不自行套用** —— 35 輪禁區逐字為
「不得自行對齊 W-97 所發現之樣式差異（屬交付形式，Pei 裁）」。

`priority` 之 `P0` 缺項同理待裁：其可能是本 feature 確無 P0 級項，
亦可能是分級判準與交付本不同。**本層未改任一條之 priority。**

### 3.4 未驗

- W-97 只比四欄。交付本之 `Test Group`／`Test Set`／`Specification Reference`／
  `Test Case Reference ID`／`Estimated Test Time`／`Functional Safety`
  ＋ 五個 `Atl-Mi` 車型欄未比 —— **35 輪只令比四欄，未擅自擴大**
- §9 十七項中不可機械化之七項（capability 判斷／trigger vs 環境前提／
  snippet 適用性／FP-FF／上游分解／方法適配／來源優先）本輪未逐條人讀 ——
  W-95 只動 procedure／ER 之 record 子句，未動判斷層；惟此為**未驗**，不記為相符

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 項 | 條件 |
|---|---|
| 批次來源 | 各 batch 之**最新版**：`batch01_v4`／`02_v2`／`03_v3`／`04_v4`／`05_v2`／`06_v2`／`07_v2`／`08_v3`／`10_v2`／`11_v2`／`12_v2`，合計 **76 條**（batch09 不存在） |
| 本輪產出 | 同名 `_v{n+1}`（`batch01_v5` … `batch12_v3`），**原版全數保留** |
| record 之偵測式 | procedure 逐行 `\brecord\b(?!ed)`（動詞形，排除 `recorded`）；引用之偵測式 `recorded in step \d+`；具名之偵測式 `record\b[^\n]*\bas\s+[A-Z][A-Za-z0-9_]*` |
| 替換之保護 | 每一逐字替換於該 TC 之 `test_procedure` ＋ `expected_result` 內 **assert 恰命中一次**；0 次跳過（helper 之選擇性分支）、>1 次即 raise |
| 錨點（R-VS54） | 各批之**改寫前版本**，與新版同批執行（`scripts/selfcheck_anchored.py`），錨點回報 0 項即 exit 2 |
| 池之判定 | `docs/reports/generatable.tsv` 之 `generatable == yes`，扣除十一批之 `leaf_id` 聯集 |
| DR 交叉 | `dr_conflict.conflict(token, value)` 逐 (token, 值) 跑；token 取自 `writability_driver.clause_pairs()` 之三形態 |
| DBC 存在性 | 兩檔以 `latin-1` 讀，`^\s*SG_\s+(\w+)` 取全部 signal 名，**區分大小寫**比對 |
| 交付本 | `…SWQT_SWC_20260708.xlsx` 之 `Test Case Specification 測試用例規範` 分頁，**自第 10 列起、B 欄非空**者為資料列，得 **286** 列；欄位取 H(8)／I(9)／O(15)／Q(17) |
| 受控值域 | 同檔 `下拉選單` 分頁，9 值 |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 內容 | 成對之 DR |
|---|---|---|
| **A-VS109** | `PHEVFeatures-017` 為節定義式前言，W-87 之四式未涵蓋 `This section defines` | 無（判準之範圍問題，非素材缺） |
| **A-VS110** | 剩餘池 33 leaf 之斷言目標訊號不在基線 DBC，L-VS2 必 FAIL | **DR-25**（型 B，素材缺件） |
| **A-VS111** | `guard_new_conclusion()` 僅在「值需演繹」之路徑上被呼叫，條文自帶值者完全不過閘 | 無（閘之範圍問題） |
| **A-VS112** | `FeaturesEnableCriteria-023` 之「all other signal values」須跨條文取值，該 token 為 DR-8 標的 | **DR-8′**（已在簿，未送出） |

**R-VS35 之兩數**：**本輪新增 4 筆**（A-VS109／110／111／112）；
**登記簿現有 111 個相異 id**（`ANOMALIES.md`）。差額 0。
DR：本輪新增 **1**（DR-25）；登記簿現有 **17 個相異 id**（`DATA_REQUESTS.md`）。差額 0。

**A-VS109／A-VS111／A-VS112 三者同型**，且與 A-VS106（34 輪）、
`guard()` 之靜默直通（32 輪）、W-87 之前言判定（31 輪）同型 ——
**判準以形態列舉，形態一變即靜默脫落，而其輸出與「通過」不可分辨。**
R-VS54 立於本輪之前一輪，本輪一次撞到三個新實例。
**三者皆未由本層修補**：修補會改變全量分級，須先過 R-VS44 之交叉，
且依 R-VS54 其修法須附必命中之錨點。

## 6. 獨立判斷：本包是否仍有該驗而未驗者

**有，四項：**

1. **W-95 改寫後未過 pilot review。** 42 條之 procedure／ER 形態變了，
   §9 之機械化部分過了，但 canon §1.2 之 pilot 是唯一能揭露內容層缺陷之關卡。
   本輪改動集中於「刪一個子句」與「命名一個變數」，風險低於 34 輪之全量改寫，
   惟 **§2.4 之 1 處（`ThirdRowHeadrestDump-038` 判 `not selectable`）確為推論**，
   建議與 pilot #3 一併覆。

2. **A-VS109／111／112 三者之修法未做，故 `generatable = 108` 這個數字現在是虛的。**
   其至少虛增 1（A-VS109）、應扣 1（A-VS111 之 DR-15 標的）。
   `writability.tsv` 之驅動雖已可重現（R-VS53 已達成），
   **但「可重現」不等於「判準完整」** —— 本輪三個實例皆為驅動忠實地重現了
   一個範圍不足之判準。R-VS53 解決的是稽核性，不是正確性。

3. **`writability`／`generatable` 未含「訊號存在於基線 DBC」一項。**
   A-VS110 之 33 條被判 W0／yes，而其 TC 一寫出來就會被 L-VS2 打掉。
   **分級與 lint 對「可寫」之定義不一致**，這不是本輪之偶發，
   是兩者從未對過。建議下輪將 L-VS2 之存在性檢查併入驅動（並附錨點）。

4. **W-97 只比了四欄。** 交付本另有 12 欄未比，其中
   `Test Group`／`Test Set`／`Specification Reference` 三者直接進交付物。
   本輪依指令未擴大，惟「外觀一致性」之訴求若成立，其範圍不會只到四欄。

**本輪無「該驗而漏驗」之作業項** —— 三項作業（W-95／W-91／W-97）皆執行，
W-91 之結果為 0 是判定結果，不是未執行。

---

### D-6 骨架對照

| 節 | 骨架要求 | 本包 |
|---|---|---|
| §1 | 預期 vs 實測，相符者亦列 | ✅ 17 列，相符 12／不符 3／PASS 3 皆列 |
| §2 | 不符項目，不自行調和 | ✅ 四項（2.1–2.4），皆未調和 |
| §3 | 三分法 | ✅ 已驗相符／已驗不符／未驗 三段俱全 |
| §4 | 掃描條件揭露 | ✅ 10 列，含偵測式逐字 |
| §5 | 新開 anomaly 與 DR 成對 | ✅ 4 anomaly／1 新 DR，R-VS35 兩數已列 |
| §6 | 獨立判斷 | ✅ 四項，含「本輪無漏驗作業項」之明說 |
