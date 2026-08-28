# 上繳包 23 —— batch 1 材料、欄位台帳清帳、DR-SU2 二段化

- 日期：2026-08-28
- 方向：執行層 → 分析層
- 對應下放：`docs/handoff/24_batch1_material.md`
  （SHA256 `7d1d8e26f93d82e357c207b00249e158a858a58ffc181701233bf9d3e56397f6`，127 行）
- **未結 DR：2 筆**（DR-SU1；DR-SU2 確認進度 **5/105**）
- 新腳本：`scripts/batch1_material.py`

## 本輪四個主結果

1. **T37a 之停止條件未觸發**：35 本已掃之簿於 `AB`–`AG` **六欄皆空**，
   **R-SU28 v3 三之裁定成立**。
2. **§六.6 之答案：`Silent Update` 9 列中有 1 列屬 105 列（`179`）** ——
   batch 1 **會**撞上 R-SU29(c) 之 PENDING。
   但**pilot 之 4 列（`175`／`176`／`177`／`183`）無一屬 126 內部列** ——
   **pilot 完全避開了兩個難類，而把唯一的 105 列留給了 batch 1**。§7.1。
3. **欄位台帳清帳：未定 21 → 5 欄**（037 歸零、SYS1 剩 3、036 剩 2）。
4. **最後 5 欄中有 3 欄是同一件事**：036 之 `C`（`Requirement or Design ID
   (Polarion)`）之值，其來源即 SYS1 之 `ID`／`_polarion` ——
   `vehicle_category` 於該欄實填 `NRL-171043`，與 SYS1 之 `NRL-168414` 同源。§4.1。

---

## 1. T37e —— T-抄 核對結果

| 條 | 字元數 | 字面一致 | sha256[:12] |
|---|---:|:--:|---|
| R-SU28 v3 | 918 | **OK** | `d4980a3770c6` |
| R-SU30 | 484 | **OK** | `2681034b1b6b` |

二條逐字 append，**既有 45 個條文區塊未受影響** ✅（現 47 塊）。
索引表現行 **30 條**（R-SU28→**v3**、新增 R-SU30）；
留存 **17 條**（新增 `R-SU28`(v2)）。與下放包 24 §五 T37e 所定之數一致。

`PLAYBOOK.md` §7 追加 **(24)**「滾動清單須分二段」，
判準為**「一個清單若會成長，就問它最多會長到多少 —— 答不出上界，
讀者只能用當前值估規模，而那必然低估」**。

---

## 2. T37b —— `Silent Update` 9 列之 VC／VM（本輪核心）

- 用途：分析層起草 batch 1 時依 **R-SU27(a)** 取其觀測面候選
- 其 Description 全文與路徑 A 前 5 候選**已備於 `docs/upstream/17_pilot_material.md` §2**，本節不重複傾印

| # | 037 列 | 標題 | 126 內部列？ | **105 列？** | `Verification Method` |
|---:|---|---|:--:|:--:|---|
| 1 | `SWE1-FOTA-175` | Execute Silent Update Without User | — | — | `Integration Test` |
| 2 | `SWE1-FOTA-176` | Restrict Silent Session Notificati | — | — | `Unit Test / Integration Test / System Test` |
| 3 | `SWE1-FOTA-177` | Restrict Opt-Out and Deferral Opti | — | — | `Unit Test / Integration Test / System TestHMI ` |
| 4 | `SWE1-FOTA-179` | Start Silent Update Download Autom | **✅** | **⚠ 是** | `Integration Test` |
| 5 | `SWE1-FOTA-180` | Optionally Suppress Download Confi | — | — | `Unit Test / Integration Test / System TestHMI ` |
| 6 | `SWE1-FOTA-181` | Start Silent Update Installation I | **✅** | — | `Integration Test` |
| 7 | `SWE1-FOTA-182` | Optionally Suppress Deployment Con | — | — | `Unit Test / Integration Test / System TestHMI ` |
| 8 | `SWE1-FOTA-183` | Display Silent Update Completion a | — | — | `Integration Test` |
| 9 | `SWE1-FOTA-184` | Apply Silent Update to All Session | — | — | `Integration Test` |

- 屬 126 內部列者：**2** —— `179`、`181`
- **屬 105 列者：1** —— `179`

### 逐列全文


---

#### 1. `SWE1-FOTA-175` — Execute Silent Update Without User Interaction

- 分類：非內部列｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Assess update metadata validation handling received from SWMC for Silent Update classification.
>
> Verify automatic background execution behavior when the update type is identified as Silent Update.
>
> Inspect Silent Update processing flow during background update execution.
>
> Ensure the SW Update HMI is not triggered for progress indications, update prompts, or customer-facing interaction during Silent Update execution.
>


---

#### 2. `SWE1-FOTA-176` — Restrict Silent Session Notifications to Safety-Required Cases

- 分類：非內部列｜`Verification Method`：`Unit Test / Integration Test / System Test`

**`Verification Criteria` 全文**：

> Review SW Update HMI interaction behavior during active Silent Update sessions.
>
> Analyze notification handling flow while Silent Update execution is in progress.
>
> Validate that customer-facing update progress notifications remain suppressed throughout the Silent Update session.
>
> Check that user notifications are permitted only when required for safety-related conditions or mandatory system behavior.
>


---

#### 3. `SWE1-FOTA-177` — Restrict Opt-Out and Deferral Options in HMI

- 分類：非內部列｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Evaluate SW Update HMI behavior when the assigned update service is active and available.
>
> Inspect user interaction flow presented during mandatory update handling scenarios.
>
> Verify that opt-out and update deferral selections are restricted within the SW Update HMI.
>
> Ensure the assigned update service does not expose user options to reject, postpone, or defer the update process.
>


---

#### 4. `SWE1-FOTA-179` — Start Silent Update Download Automatically

- 分類：**105 列**（內部列且 VC 亦無外部面）｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Inspect Download Descriptor metadata transfer handling between the SWMC and WiFi Update Service after update availability confirmation.
>
> Assess DD metadata analysis behavior for Silent Update classification detection.
>
> Validate automatic deployment package download request generation when Silent Update metadata is identified.
>
> Review SWMC interaction flow during automatic deployment package download initiation for Silent Update processing.
>


---

#### 5. `SWE1-FOTA-180` — Optionally Suppress Download Confirmation Screen

- 分類：非內部列｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Analyze Silent Update handling behavior during deployment package download preparation.
>
> Verify that the SW Update HMI does not display a download confirmation screen for Silent Update sessions.
>
> Review automatic deployment package download request handling initiated through the WiFi Update Service.
>
> Ensure deployment package download begins through SWMC without requiring any customer interaction.
>


---

#### 6. `SWE1-FOTA-181` — Start Silent Update Installation Immediately After Download

- 分類：**126 內部列**（但 VC 有外部面）｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Assess deployment package download completion notification handling for update packages classified as Silent Update.
>
> Monitor communication flow between the SWMC and WiFi Update Service after successful download completion.
>
> Validate installation precheck initiation behavior immediately following deployment package download completion.
>
> Review automatic deployment startup processing for Silent Update packages without additional interaction flow.
>


---

#### 7. `SWE1-FOTA-182` — Optionally Suppress Deployment Confirmation Screen

- 分類：非內部列｜`Verification Method`：`Unit Test / Integration Test / System TestHMI Validation Testing`

**`Verification Criteria` 全文**：

> Review deployment handling behavior for update packages categorized as Silent Update.
>
> Check that the SW Update HMI does not present a deployment confirmation screen during Silent Update processing.
>
> Evaluate automatic deployment initiation flow for downloaded Silent Update packages.
>
> Confirm deployment execution proceeds without requiring customer interaction or approval actions.
>


---

#### 8. `SWE1-FOTA-183` — Display Silent Update Completion and What's New Details

- 分類：非內部列｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Validate deployment completion reporting from the Update Engine and SW Updater Manager for Silent Update sessions.
>
> Track retrieval of “What’s New” information associated with the successfully deployed package metadata.
>
> Analyze notification handling between the WiFi Update Service/USB Update Service and the SW Update HMI after successful deployment.
>
> Ensure the SW Update HMI displays the update success indication together with the corresponding “What’s New” details for the completed update.
>


---

#### 9. `SWE1-FOTA-184` — Apply Silent Update to All Session Flows

- 分類：非內部列｜`Verification Method`：`Integration Test`

**`Verification Criteria` 全文**：

> Examine Silent Update execution rule handling across update check, deployment package download, and installation processing flows.
>
> Verify Silent Update behavior throughout all supported update session stages.
>
> Assess SW Update HMI interaction suppression during Silent Update operation execution.
>
> Confirm customer-facing prompts, confirmation screens, progress indications, and interaction flows are not triggered unless safety-related conditions require user notification.
>


---

## 3. T37a —— `AB`–`AG` 六欄之實測佐證（**停止條件未觸發**）

> **若任一本有填值，即停並回報 —— R-SU28 v3 三之裁定失效。**

掃描範圍：`features/*/delivered`／`output`／`sandbox/*` 之 xlsx，共 **41** 本。

| feature | 簿 | 資料列 | AB Test Version | AC Test Vehicle (Bench) | AD Test Period | AE Tester | AF Test Result | AG Defect ID |
|---|---|---:|---|---|---|---|---|---|
| power | `delivered/pm_29.xlsx…` | 390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 |
| bed_lowering | `output/FM-WI-FSM-036-…` | 151 | 空×151 | 空×151 | 空×151 | 空×151 | 空×151 | 空×151 |
| comfort | `output/FM-WI-FSM-036-…` | 466 | 空×466 | 空×466 | 空×466 | 空×466 | 空×466 | 空×466 |
| display | `output/FM-WI-FSM-036-…` | 24 | 空×24 | 空×24 | 空×24 | 空×24 | 空×24 | 空×24 |
| popup | `output/FM-WI-FSM-036-…` | 5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 |
| power_moding | `output/FM-WI-FSM-036-…` | 51 | 空×51 | 空×51 | 空×51 | 空×51 | 空×51 | 空×51 |
| power_moding | `output/FM-WI-FSM-036-…` | 51 | 空×51 | 空×51 | 空×51 | 空×51 | 空×51 | 空×51 |
| power_moding | `output/FM-WI-FSM-036-…` | 51 | 空×51 | 空×51 | 空×51 | 空×51 | 空×51 | 空×51 |
| privacy | `output/FM-WI-FSM-036-…` | 11 | 空×11 | 空×11 | 空×11 | 空×11 | 空×11 | 空×11 |
| sxm | `output/FM-WI-FSM-036-…` | 215 | 空×215 | 空×215 | 空×215 | 空×215 | 空×215 | 空×215 |
| time_management | `output/FM-WI-FSM-036-…` | 59 | 空×59 | 空×59 | 空×59 | 空×59 | 空×59 | 空×59 |
| user_profiles | `output/FM-WI-FSM-036-…` | 189 | 空×189 | 空×189 | 空×189 | 空×189 | 空×189 | 空×189 |
| user_profiles | `output/FM-WI-FSM-036-…` | 189 | 空×189 | 空×189 | 空×189 | 空×189 | 空×189 | 空×189 |
| user_profiles | `output/FM-WI-FSM-036-…` | 189 | 空×189 | 空×189 | 空×189 | 空×189 | 空×189 | 空×189 |
| vehicle_category | `output/FM-WI-FSM-036-…` | 126 | 空×126 | 空×126 | 空×126 | 空×126 | 空×126 | 空×126 |
| popup | `pilot01/FM-WI-FSM-036-…` | 5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 |
| power | `b02/pm_batch2.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b02/pm_remediated.…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b02/pm_work.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b10/pm_10a.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b10/pm_10a5.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b10/pm_10a5b.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b10/pm_base.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b16/pm_16.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b17/pm_17.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b18/pm_18.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b19/pm_19.xlsx…` | 284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 | 空×284 |
| power | `b25/pm_25.xlsx…` | 407 | 空×407 | 空×407 | 空×407 | 空×407 | 空×407 | 空×407 |
| power | `b26/pm_26.xlsx…` | 390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 |
| power | `b27/pm_27.xlsx…` | 390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 |
| power | `b28/pm_28.xlsx…` | 390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 |
| power | `b29/pm_29.xlsx…` | 390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 | 空×390 |
| sw_update | `pilot01/FM-WI-FSM-036-…` | 5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 |
| sw_update | `pilot02/FM-WI-FSM-036-…` | 5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 |
| sw_update | `pilot03/FM-WI-FSM-036-…` | 5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 | 空×5 |

**實掃 35 本含 TC 分頁且有資料列者。**

### ✅ 六欄於全部已掃之簿**皆為空**

**R-SU28 v3 三之裁定成立**（其依據為欄位語意，本項為其實測佐證）。

> ⚠ **「皆為空」不蘊含「應為空」** —— 亦可能全部漏填。本項只證明**本 feature 之留空與既有實務一致**，不證明該六欄不需填（同上繳包 21 §4.1 對 `T`–`Z` 之記明）。

---

## 4. T37c —— `SOURCE_COLUMNS.md` 清帳

| 素材 | 欄數 | 已用 | 不用 | **未定** | 本輪變動 |
|---|---:|---:|---:|---:|---|
| 037 `AnalysisReport_FULL` | 18 | 8 | **10** | **0** | 欄 14 定案不用（**037 歸零**） |
| SYS1 `Basic Report` | 7 | 2 | **2** | **3** | 欄 1／5 常數欄不用 |
| 036 母本 TC 分頁 | 33 | 17 | **14** | **2** | `AB`–`AG` 六欄 + `T`–`Z` 七欄不用 |
| **合計** | **58** | **27** | **26** | **5** | **21 → 5**（−16） |

與下放包 24 §五 T37c 所推之「21 − 1 − 2 − 6 − 7 = 5」**相符**。

### 4.1 最後 5 欄之角色陳報（**陳報事實，不裁定**）

| 來源 | 欄 | 值之形態（實測） | 由誰填／何時填 |
|---|---|---|---|
| **036** | `C` `Requirement or Design ID (Polarion)` | 母本 BLANK。**35 本中僅 `vehicle_category` 一本有填**（126 列全填，unique 66），值形如 `NRL-171043` | 產出端；其值須有來源 |
| **036** | `E` `Test Case ID (TestRail)` | 母本 BLANK。**35 本實測全空** | TestRail 匯入後回填，屬測試管理端 |
| **SYS1** | 0 `ID` | `NRL-168414` …（unique 120） | 上游 Polarion 匯出 |
| **SYS1** | 4 `SYSRE_HMI_Source ID` | `SYS1_HMI_..._1`／`_1.1`（unique 120） | 上游 Polarion 匯出 |
| **SYS1** | 6 `_polarion` | `NR1L/NRL-168414`（unique 120） | 上游 Polarion 匯出 |

### 4.2 ⚠ 五欄中有三欄是同一件事

036 之 `C` 欄標頭為 **`Requirement or Design ID (Polarion)`**，
而 `vehicle_category` 於該欄實填 **`NRL-171043`** ——
其形態與 **SYS1 欄 0 `ID`（`NRL-168414`）**、
**欄 6 `_polarion`（`NR1L/NRL-168414`）同源**。

**即：SYS1 之三個識別碼欄，正是 036 `C` 欄所要之值的來源。**
五個未定欄實為**一組**：一個消費端（`C`）+ 三個供給端（SYS1 之 0／4／6）
+ 一個獨立者（`E`，屬測試管理端）。

**本 feature 之特殊處（陳報，不裁）**：R-SU11 已裁
「Layer 3 主軸為 CFTS_57；SYS1 不作章對章橋接，其接點為 HMI 87 列」。
故 sw_update 之 037 列**是否有對應之 Polarion id、
以及該對應是否經 SYS1 之 120 列可得，未查**。
`C` 欄能否填、該不該填，取決於該對應之存在與否 —— **屬分析層之裁定。**

---

## 5. T37d —— DR-SU2 之二段台帳（R-SU30）

`DATA_REQUESTS.md` 之 DR-SU2 已改二段：

| 段 | 定義 | 現況 |
|---|---|---:|
| **(a) 已確認段** | 已由分析層逐列判定、觀測後果取不到。**此段方為 DR 之實際標的** | **5 列**（`363`–`367`） |
| **(b) 未確認之母群** | 符合同一語形條件但**尚未逐列判定**者 | **105 列**（含 (a)） |
| **確認進度** | (a)/(b) | **5 / 105（5%）** |

表頭之 `Status` 欄改為 `**OPEN**｜**確認進度 5 / 105**` ——
**把上界寫進表頭本身，不藏在註解裡**（上繳包 22 §7.1 之建議，本輪落地）。

### 5.1 未結 DR 清單（2 筆，含確認進度）

| # | 事項 | 狀態 | 確認進度 | Urgency | 阻斷 |
|---|---|---|---|---|---|
| **DR-SU1** | 靜默期間之安全相關通知條件清單 | OPEN | — （單列標的） | High | `newR1L-SU-003` 三欄 PENDING（lint U=3） |
| **DR-SU2** | 105 列於系統測層級之觀測手段 | OPEN | **5 / 105（5%）** | High | 初始 5 列；**上界 105 列（母體 34%）** |

> **DR-SU2 之進度為 5%，不得被陳述為「已盤點完成」**（R-SU30(d)）。

---

## 6. 待分析層確認之事項（非 DR）

| # | 事項 | 出處 |
|---:|---|---|
| 1 | **`C` 欄能否填** —— 取決於 sw_update 之 037 列有無對應之 Polarion id（**未查**） | §4.2 |
| 2 | **`E` 欄之歸屬**（疑屬測試管理端，35 本全空） | §4.1 |
| 3 | **SYS1 欄 0／4／6 之裁定** —— 其為 `C` 之供給端，與 #1 連動 | §4.2 |
| 4 | **`179` 於 batch 1 之處置** —— 其屬 105 列，將撞上 R-SU29(c) 之 PENDING | §7.1 |

---

## 7. 獨立自評

### 7.1 §六.6 所問：9 列若有列屬 105，batch 1 就會撞上 PENDING；若全不屬，是否意味 pilot 避開了最難的部分

**兩個都成立 —— 而且是同一件事的兩面。**

**(甲) 9 列中有 1 列屬 105 列：`SWE1-FOTA-179`。**

故 **batch 1 會撞上 R-SU29(c)**：`179`（Start Silent Update Download
Automatically）為內部列，且其 `Verification Criteria` 亦無外部面。
撰寫其 TC 時須依 R-SU25(c) 求其可觀測後果；取不到即掛 `PENDING`
並入 DR-SU2 之已確認段（進度將由 5/105 變 6/105）。

**(乙) 而 pilot 之 4 列，一列都不屬。**

| 批 | 037 列 | 屬 126 內部列 | 屬 105 列 |
|---|---|---:|---:|
| **pilot（下放包 19／20 所選）** | `175`、`176`、`177`、`183` | **0 / 4** | **0 / 4** |
| batch 1（其餘 5 列） | `179`、`180`、`181`、`182`、`184` | **2 / 5**（`179`、`181`） | **1 / 5**（`179`） |
| 合計 9 列 | | 2 / 9（22%） | 1 / 9（11%） |
| 全母體 | | 126 / 311（41%） | 105 / 311（34%） |

**三層低估，逐層放大**：

1. **`Silent Update` 這一組本身就低於母體** —— 105 類佔比 11% vs 母體 34%，
   **不到三分之一**。
2. **pilot 在該組內又只取了非內部列** —— 4 列全部避開，**0%**。
3. 於是 **pilot 之 5 個 TC，其撰寫從未遭遇過本 feature 最大的那個問題**
   （105 列佔母體 34%），**而那 5 個 TC 正是用來校準撰寫方法的**。

**這正是 pilot 之選樣偏誤在 TC 撰寫面之具體形態**：
下放包 19 §四之選樣理由為
「Service 型基準／GT 列／HMI 限制型／HMI 顯示型」——
**四個軸皆為「TC 之形態」，無一軸為「可觀測性」**。
可觀測性當時尚未被指認為問題（R-SU25 是下放包 20 才立的），
**故這不是選樣之疏失，是問題被發現得比選樣晚。**

**但其後果仍在**：pilot 所驗證之撰寫方法（R-SU25(c) 之三個作法 ——
版本號變化／畫面內容記錄／設定移入 Pre-Condition）
**只在有可觀測面的列上被試過**。
**它們對 105 列是否夠用，pilot 一列都沒有測到。**

**能誠實說的是**：`179` 將是**第一個真正的測試** ——
不是測 TC 寫得對不對，是測 **R-SU25(c) 之作法在無觀測面之列上能不能用**。
若 `179` 也能取得可觀測後果，那 105 之上界會鬆動；
若取不到，DR-SU2 就有了第一個非 `Telematics Client` 之樣本。

### 7.2 本輪之方法有無「答不到卻看似答到」之處

**有，在 §3 之「35 本皆空 ✅」。**

那個 ✅ 是本輪唯一一個停止條件之通過，讀起來像
「`AB`–`AG` 不填之裁定已被驗證」。**它不是。**

R-SU28 v3 三之拘束是「**若實測顯示既有交付本於該六欄有填值，本項即失效**」
—— 即該實測是一個**否證器**，不是驗證器。**它通過只代表沒被否證。**

**而「35 本皆空」有一個完全對稱的替代解釋**：
六本正式交付本 + 29 本工作簿**全部都漏填了**。
本 feature 之產出與它們一致，只證明**從眾**，不證明正確。
我已在 §3 之末逐字記明此點（同上繳包 21 §4.1 對 `T`–`Z` 之記明）。

**更要緊的是掃描範圍**：35 本中**只有 6 本是 `delivered/` 或 `output/`**，
其餘 29 本是 `sandbox/`（其中 17 本屬同一 feature 之同一系列迭代）。
**「35 本」聽起來像 35 個獨立證據，實際上獨立之 feature 只有 12 個**
—— 這與上繳包 12 之「獨立觀測」是同一個問題，
**而我這次是在自己的證據上犯它**。

### 7.3 一項我做了而下放包未要求的事

**§4.2 —— 陳報 5 欄之角色時，順手比對了它們的值形態，發現三欄同源。**

T37c 只令「該 5 欄之角色須陳報：各欄在交付流程中由誰填、何時填、
本 feature 是否需要」。逐欄填三格即完成。

我另做的是**把值印出來對照** ——
036 `C` 之 `NRL-171043`（vehicle_category 實填）
與 SYS1 `ID` 之 `NRL-168414`、`_polarion` 之 `NR1L/NRL-168414`
**是同一種識別碼**。

於是那 5 欄不再是「五個各自待裁的欄」，而是
**一個消費端 + 三個供給端 + 一個獨立者** ——
**裁定它們必須一起裁，且只有一個實質問題**：
「sw_update 之 037 列有沒有對應之 Polarion id」。

**記明此事之理由**：R-SU26(a) 令全覽記「值之型態摘要」，
而我上一包在 SYS1 那三欄只寫了「自由文字，unique 120」——
**unique 數說明不了它是什麼**。
若當時印了一個實例（`NRL-168414`），這個同源關係在上一包就會被看見。
**型態摘要之「型態」必須包含一個實例，否則它只是一個計數。**
