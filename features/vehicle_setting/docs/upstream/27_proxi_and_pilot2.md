# 上繳 27 —— PROXI 值域併入、(b) 路複查、pilot #2 清單、batch11／12

執行層寫入。依據：`docs/handoff/49_proxi_adoption.md` §3。canon §8.2 六節。

| 項 | 內容 | 狀態 |
|---|---|---|
| D-1 | 依 R-VS18 先建本檔 | ✅ |
| D-2 | 轉錄三條 | ✅ |
| D-3 | `INPUTS.sha256` 16 檔 | ✅ **全數 OK** |
| D-4 | A-VS93／A-VS77 關閉；DR-22′ 撤回 | ✅ |
| D-5 | 依 R-VS35 列兩數 | ✅ 見 §5.1 |
| **W-83** | (b) 路複查 ＋ PROXI 併入 | ⚠ **升級：W2 轉出僅 7 < 40** |
| **W-84** | pilot #2 review sheet | ✅ **15 條，1,063 行** |
| **W-85** | batch11 ＋ batch12 | ⚠ **升級：交付合計 1 < 12** |

---

## 1. 預期 vs 實測（相符者亦列出）

### 1.1 D-3 —— `INPUTS.sha256` 全檔驗證

**16 檔逐檔 `shasum -a 256 -c` 全數 `OK`**，含本輪補入之
`PROXI_HDCC27_R3_20250424.xlsx`（`e7c2020f…`）。

### 1.2 W-83(1) —— 15 對逐對標路徑，(b) 路人讀 **14 / 14 通過**

| 路徑 | 對數 |
|---|---:|
| **(a) 縮寫**（自動採用） | **1**（`ESS_ENG_ST/ENS_DSBL`） |
| **(b) 共享實詞**（須人讀） | **14** |
| (c) 來源別名對 | 0 |

**(b) 路 14 對逐對人讀結果：14 / 14 通過。**

| 型 | 對數 | 理由 |
|---|---:|---|
| **分隔符差異** | **12** | `Vented Seat High / VS_HI` vs DBC `Vented_seat_high` —— **同一值，僅空白與底線之別**；`VentedSeatFL`／`FR` 之 High／Low／Off 各兩至三種寫法 |
| **語意核心逐字相符** | **2** | `HSW_Stat` 之 `Heated steering wheel off / HSW_OFF` → `OFF`（值域 {OFF, ON}）；`DriverSide` 之 `Right Drive` → `Right Side`（40 包已裁） |

**驗收：`IGN_OFF → IGN_LK` 不在採用表內** ✅
**升級條件「(b) 路對有半數以上未通過人讀」未命中**（0 / 14 未通過）。

### 1.3 W-83(2) —— `W2 → W0` 之 8 條逐條人讀，**8 / 8 通過**

八條皆為通風座椅之狀態值條文（`4858367`／`4858386`／`4858387`／`4858389`／
`4858398`／`4858417`／`4858418`／`4858420`），其值直接命中
`FL/FR_VS_STATSts` 之 DBC `VAL_`。**無退回 W2 者。**

### 1.4 W-83(3)(4) —— PROXI 值域併入與全量重跑

三個待解值**全數命中**：

| 值 | raw | 命中方式 |
|---|---:|---|
| `Front Seats` | **1** | 逐字 |
| `Present` | **1** | 逐字 |
| `One Level` | **0** | **R-VS39 補充**（`one`→`1`），於 {`1 level`,`2 levels`,`3 levels`} 唯一 |

| 級 | 28 輪 | **29 輪** |
|---|---:|---:|
| W0 | 101 | **108** |
| W1 | 2 | **2** |
| W2 | 134 | **127** |

28 × 29 交叉：`W0→W0` 101／`W1→W1` 2／**`W2→W0` 7**／`W2→W2` 127。

**因 R-VS49 而由 W2 轉出者：7。⚠ 升級條件命中**（「< 40」）。**追因見 §2.1。**

### 1.5 W-83(5) —— 閘之同步

`DR-22′` 已撤回，其閘移除；`VC_HdRstPrsnt` **改掛 DR-22（B3 類）**。
實測：`Cooled_Seats/Front Seats` 與 `Heated_Steering_Wheel/Present` 皆 `write`；
`VC_HdRstPrsnt/Present` 仍 `DR-CONFLICT`。

### 1.6 W-84 —— pilot #2 review sheet

| 項 | 值 |
|---|---:|
| 母體（未 review） | **68** |
| 非空交叉格（Layer 2 × design_method） | **12** |
| 分層抽樣 | **12**（各格取其 reqid 最小者，**無須補足**） |
| 必檢 | **3** |
| **合計** | **15** |
| 產出 | `docs/reports/pilot2_sheet.md`，**1,063 行** |

交叉格矩陣已列於 sheet 內，**抽法可複現**。

### 1.7 W-85 —— batch11／batch12

| 項 | 值 |
|---|---:|
| 池（W0∪W1 ∧ delegate 可用 ∧ 未用） | **11** |
| 過 `guard()` | **7**（4 條由 DR-15 攔下） |
| 扣除 26 輪已判 2 條 | **5** |
| **其中適用性前言（無可測內容）** | **4** |
| **batch11 交付** | **1** |
| **batch12 交付** | **0**（池已空） |

**⚠ 升級條件命中**（「兩批交付合計 < 12」，實測 **1**）。

**累計交付 75 → 76 條。**

## 2. 不符項目（不自行調和）

### 2.1 ⚠ **「DR-22′ 影響 79 leaf」是錯的 —— 實為 8 條**

R-VS49 併入後 W2 轉出僅 **7**。追因：

| 項 | 值 |
|---|---:|
| **全母體中引用該四參數之 leaf** | **8** |
| 其中經 R-VS49 轉出者 | 7（另 1 條因他因仍 W2） |

**「79」之來源為 21 輪之 `quoted_form_risk` 標記** ——
其把**引號形態下全部未解 token 所影響之 leaf** 一併計入（79 條），
而**該 79 條中僅 8 條涉及 PROXI 參數**。

A-VS77／DR-22′ 沿用該數而未回查其組成，**24／25／26 三輪之
「DR-22′ 為單一最大解鎖」之判斷因而失準**。

**真正之大宗**：

| token | leaf |
|---|---:|
| `FL_HS_Cmd_Tlm` | 17 |
| `FR_HS_Cmd_Tlm` | 16 |
| `FL_VS_Cmd_Tlm` | 14 |
| `FR_VS_Cmd_Tlm` | 14 |
| **四者合計** | **61** |
| `Hybrid_Type` | 11 |
| `HeatedSeatFL`／`FR` | 各 8 |
| `EngRun_Stat` | 7 |

**`*_Cmd_Tlm` 四者於 LID 記為 `NOT_IN_DBC`（`TELEMATIC_CLIMATE_SETUP` 之訊號）。**
**DR-21 之影響應以此重估；DR-22′ 之撤回不改變產能。** → **A-VS95**

### 2.2 ⚠ **「值可解」不等於「有可測內容」**

經 R-VS49 轉出之 7 條中，**4 條為適用性前言**：

```
4859376  Following requirements are valid only if PROXI parameter Heated_Seats == "Front Seats" OR "Front and Rear Seats".
4859400  同上
4859438  同上（Cooled_Seats）
4859464  同上（Cooled_Seats）
```

**其僅界定後續條文之適用範圍，自身無觸發亦無可觀察之結果。**
與 13 輪判為 (c) 之 `4859399`／`4859463`（`applicable for R1 Low only…`）**同型**。

**分級器看得見「值是否可解」，看不見「條文是否有可測內容」** ——
**與 A-VS76 同源**（B4 之偵測盲區，26 輪已記為「掃描偵測不到 B4」）。

四者移出 batch11，故 batch11 僅交付 **1** 條。→ **A-VS96**

### 2.3 pilot #2 之分層有兩格空缺，其成因須記明

| Layer 2 | Decision Table | Equivalence Partitioning | Functional Based | Negative / Invalid | State Transition |
|---|---:|---:|---:|---:|---:|
| Common Features | 2 | 1 | **10** | 2 | **18** |
| **Heated Seat** | — | — | — | — | **4** |
| Heated Steering Wheel | — | 1 | — | 1 | 9 |
| Vented Seat | — | 2 | — | 2 | 16 |

**`Heated Seat` 一列僅 State Transition 一格非空（4 條）。**
成因：Heated Seat 之 88 個 leaf 中，可生成者早已耗盡於 batch01–03，
其餘皆卡於 `*_Cmd_Tlm`／`HeatedSeatFL`／`FR`（§2.1）。

**故 pilot #2 對 Heated Seat 之覆蓋僅 1 條（`TwoStagesHeatedSeat-057`）** ——
**該 Layer 2 佔母體 37%，而其在抽樣中之權重為 1/12。**
**分層抽樣之代表性受產能分布所限，非抽法之缺陷。**

## 3. 結果三分法（canon §8.4）

| 分類 | 項目 |
|---|---|
| **改對了** | R-VS48′／R-VS49／R-VS39 補充轉錄；`INPUTS.sha256` 補入 PROXI 檔（16 檔全 OK）；`spec_variables.tsv` 增 `proxi_values`／`proxi_source` 兩欄並併入四參數值域；`norm()` 加入數詞↔數字；`bus_domain()` 讀入 `proxi_values`；`dr_conflict.py` 移除 DR-22′ 之閘並改掛 DR-22；A-VS93／A-VS77 關閉、DR-22′ 標撤回；**`pilot2_sheet.md` 15 條**；`batch11.json` 1 條 0 違規 |
| **核實無誤** | (b) 路 14/14 人讀通過且 `IGN_OFF → IGN_LK` 不在表內；`W2→W0` 8 條 8/8 通過人讀；三個待解值全數命中（`One Level` 經 R-VS39 補充）；pilot #2 之 12 非空格恰足 12 條 |
| **正確地不動** | **未為湊足 batch11 之數而撰寫四條適用性前言**；**未援引 PROXI 表之其餘參數**（R-VS49 限四參數）；**未調和「79 vs 8」**；**未把 DR-15 攔下之 4 條寫入批次**；v1/v2/v3 保留 |

## 4. 本輪實際使用之掃描條件（canon §5a 條 1／2／4／5）

| 對象 | 條件 |
|---|---|
| D-3 | `shasum -a 256 -c INPUTS.sha256`，16 行逐檔比對 |
| **R-VS39 補充** | `norm()` 於空白正規化與 casefold 後，以 `\b(one\|two\|three\|four\|five)\b` 替換為 `1`~`5` |
| **PROXI 值域之併入** | `spec_variables.tsv` 增 `proxi_values` 欄（`N = label` 以 `\|` 分隔）；`bus_domain()` 以 `^\s*(\d+)\s*=\s*(.+)$` 解析並取 `norm(label)` 入值域 |
| W-83(1) 路徑判定 | `unique_target()` 依 (a)→(b)→(c) 順序測，回傳首個**恰一命中**之路徑名 |
| **(b) 路之人讀判準** | 逐對列 v 與目標 d 之**實詞集合**，確認 v 之語意核心在 d 中確有對應；分隔符差異者（`vented seat high` vs `vented_seat_high`）逕予通過 |
| W-84 分層 | Layer 2（`test_set`）× `design_method`；格內排序鍵為該 TC `specification_reference` 中之**最小 7 位數**；非空格各取第一者 |
| W-85 選 leaf | `W0 ∪ W1` ∧ `delegate ∉ {pending, blocked}` ∧ 未用 ∧ 有 reqid，**再逐條以 `guard()` 掃其條文之全部 (token, 值)** |

## 5. 新開 anomaly 與 DATA_REQUESTS（成對）

| anomaly | 配對 DR | 內容 |
|---|---|---|
| **A-VS95** | **DR-21** | 「DR-22′ 影響 79 leaf」為錯，實為 8；真正大宗為 `*_Cmd_Tlm` 四者共 61 leaf。⚠ 升級 |
| **A-VS96** | — | 四條適用性前言無自身可測內容；「值可解 ≠ 有可測內容」 |

**A-VS93 依 R-VS48′ 關閉；A-VS77 依 R-VS49 關閉。**
**DR-22′ 撤回**（R-VS49），原文保留加註。**無新開 DR。**

### 5.1 依 R-VS35 之登記簿核對

| 簿 | 本輪新增 N | 登記簿現有 M |
|---|---:|---:|
| `ANOMALIES.md` | **2**（A-VS95／96） | **95**（相異編號；最大號 A-VS96，缺 `A-VS02`） |
| `DATA_REQUESTS.md` | **0 新開**；DR-22′ **撤回** | 未結 **12**（13 − 1） |

§5 表列 2 筆，登記簿逐筆核對皆在，**差額 0**。

**分析層側核對（48／49 包）**：二包開立 anomaly **0 筆**、DR **0 筆**；**差額 0**。

### 5.2 產能現況

| 項 | 28 輪 | **29 輪** |
|---|---:|---:|
| W0 | 101 | **108** |
| W1 | 2 | **2** |
| W2 | 134 | **127** |
| `generatable = yes` | 80 | **87** |
| **已交付 TC** | 75 | **76** |
| 池（過閘後，扣已判） | — | **0** |

**產能再度歸零。** 其解不在 DR-22′（已撤回），而在 **DR-21 之 `*_Cmd_Tlm` 四者（61 leaf）**。

## 6. 獨立判斷：本包是否仍有該驗而未驗者 —— **有，三項**

1. **`*_Cmd_Tlm` 四者之 LID 記載未逐列複查。**
   §2.1 指其為最大阻塞（61 leaf），其於 `can_signal_map.tsv` 記為
   `NOT_IN_DBC`（`TELEMATIC_CLIMATE_SETUP.FL_HS_Cmd_Tlm_Req` 等）。
   **惟本輪未回查 LID 原表**，確認其是否另有 Atlantis High 欄組之對映、
   或其 `Format` 欄是否如 PROXI 四參數般為轉指。
   **該回查是目前最可能再度恢復產能之路徑**，其規模為 DR-22′ 之 **7.6 倍**。

2. **A-VS96 之四條適用性前言，其在母體中之總數未量。**
   已知形態為 `Following requirements are valid only if …`。
   **全文尚有幾條同型未掃** —— 其直接影響「W0 = 108」中有多少實為不可寫。
   與 A-VS76（B4 盲區）合併計算，**W0 之數可能虛高**。

3. **pilot #2 之 sheet 已產出，惟其 15 條中 `Heated Seat` 僅 1 條。**
   §2.3 已記其成因為產能分布。
   **若 pilot #2 之結論用於推論全母體之品質，該偏斜須計入** ——
   Heated Seat 佔母體 37%（88/237），而其在抽樣中佔 1/15。
