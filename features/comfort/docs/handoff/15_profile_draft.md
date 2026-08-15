# 15 — Comfort HMI / profile `[OVERRIDE]` 草案

- 產出層：分析層｜2026-08-15｜對象：Pei（Tier 2 簽署）／執行層（簽署後寫檔）
- 產出目標：`docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`
- 參照：`FW036_R1L_Privacy_Profile.md`（最近之 BLANK／revision C sibling）
- 狀態：**草案，未簽署。** 簽署前 Phase 4 不得開始。

> 依 Privacy profile 之前例：**結構條款可繼承，內容條款不繼承。**
> 下列凡標「繼承」者為結構性，其餘一律就 Comfort 自身證據重新導出。

---

## 0. Project identity [ADD]

- Program：Stellantis newR1L；scope 037-A03 Comfort，**403 leaves**
  `SWE1-HVAC-001…129`（含 34 列 parent 形態之 Functional Requirement，R-C3）
- spec baseline：**SR24 CR24879 (September 25 2023)**（R-C1）。SR25 為
  out-of-scope 參考，不得作為來源
- Deliverable workbook：FM-WI-FSM-036-A01 通用空白範本 `SWQT_20260121`
  （與 Privacy 同一份，65,821 bytes）。**workbook_state = BLANK**
- Test Group = `Comfort`（R-C6）；tc_id = `NR1L-ComfortHMI-{NNN}` 自 001
  （R-C7）；author on new rows = `PeiPYHsu`
- **Form revision C，欄位位移同 Privacy §0**：Q = Estimated Test Time、
  R = design_method、S = functional_safety、AA = author、AH = remarks。
  資料工作表 `Test Case Specification 測試用例規範`
- style authority：**具名 `home`** done region（144 列），
  **`amfm` 具名排除**（DECISIONS.md 已簽）。cross-feature exemplar 一律標
  `style only`；每個字面值須回溯 Comfort 自身 spec 並以 lint 強制

### 0.1 Template preparation state [ADD] —— A-CF07 之處置

範本附帶兩列樣本殘留（第 10–11 列）。**依 Privacy §0.1 之 R23-4 程序處理，
逐字繼承**：

- 以 `backend/xlsx_surgical.py` 清空五格：D10 / F10 / G10 / S10 / D11，
  `s=` style 屬性原地保留
- **B 欄不得動**：B10 為 `=IF(ISBLANK($D10),"",ROW()-9)`，清 B 會刪掉範本
  自己的編號機制
- **不得整列刪除**：會位移 DV 之 `sqref` 與 R10 之 x14 下拉

首筆 TC 落於 **row 10**。備妥之 workbook 與其來源記入
`features/comfort/DELIVERY.sha256`（ENTRY 001）。

**寫回前須經 Pei 於 Excel 實際開啟確認四項**（Privacy R29-1 前例）：無修復
提示、R 欄下拉可用且為九項、D5 Scope 正確、第 10–11 列已清且無殘留列號。
**程式層檢查不能代替 Excel 自身之檔案完整性判定。**

---

## 1. Requirements authority chain [ADD]

- Chain：SR24 spec section → 037-A03 leaf（`SWE1-HVAC-nnn(-nn)`）→ FW036 TC
- **spec_mode A**（SYS1 export）。條文權威為
  `spec-index/cache/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx`
  （70,040 bytes）。**唯一來源**，`inputs/` 不得存副本（R-C11）
- section ↔ parent req_id 為 **1:1 雙射**（129 ↔ 129，上繳 05 實測）
- **條款標籤（`C13.)`／`ICE11.)`／`HVS1.`／`W0.)`）不是唯一鍵**（A-CF13 四項）。
  traceability 一律以 **outline 節次**為鍵；條款標籤僅得出現於 `reasoning`
  與 `test_item` 之敘述
- **全文權威**：`data/section_fulltext.tsv`（129 列，不截斷）。
  `layer3_map.tsv` 之 `section_title` 為導覽欄位，**不得用於判讀**（R-C18）

## 2. Test Set vocabulary [OVERRIDE — 取代泛用自由標籤]

- Test Group（G 欄）= `Comfort`；Test Set（H 欄）取 framework Part N 之
  **15 組**，逐列填入。`fill_test_group_set: true`（BLANK，canon §2）
- **Layer 3 = SR24 outline 節次，framework 內部，永不寫入 workbook**（§4.1.5）
- `specification_reference`（N 欄）依 §10.7 承載 section —— **那是
  traceability 欄位，不是 Layer 3 欄位**，不得因「Layer 3 不入 workbook」
  而留白
- 最大組 `Heated Vented Seats`（59）**刻意不拆**（12 §1 裁定：同一進入路徑）。
  工作量以 BATCH 處理，不以拆 Set 處理

## 3. Comfort house style

### 3.1 Test Item [OVERRIDE — 取代 §4.3 僅 tc_title]
**繼承 Privacy §3.1 / SXM §3.1（結構性）**：Test Item = 以 spec 語言濃縮之
需求陳述，**modal 僅此欄允許**（引用需求原文）。泛用 §4.3 之 tc_title
（無 modal）仍產出於 JSON 供 lint 與 sibling 判別。ER 一律無 modal（§6）。

**簽署前須對 `home` done region 實測比對** —— 該欄形態應與 exemplar 一致，
不得僅以繼承為由採用。

### 3.2 Pre-Conditions [ADD] —— Comfort 之 spec trigger
以下為 §8.5 例外之合法 Pre-Condition 類別，**每一句須標 source class**
（`spec-verbatim` / `spec-derived` / `test-setup`），**未標者視為未追溯**
（Privacy R36-4）：

- **設備配置軸**（本 feature 之主軸，逐節出現）：ATC / MTC、單區 / 雙區 /
  四區、tri-mode 有無、MAX A/C 有無、MAX DEF 有無、独立座椅分區有無、
  加熱方向盤 Multi-Level / Single-Level、Standard vs Multi-Level 座椅
- **機型軸**：R1 Low / R1 High（`14.19` 之 `-02` 為唯一含此條件者）
- **市場／變體軸**：EMEA ICS（ch16 全章）
- **禁用**：`HU is powered on`、`Climate is available`（皆為隱含環境前提）

**每一條配置條件須具名其來源節次**；不得以「某些車輛有此配置」概括
（§8.4.1 禁造值）。

### 3.3 Design Method [OVERRIDE — 限縮 §12 輸出字串]
**繼承 Privacy §3.3**：僅得回傳 workbook `下拉選單!A1:A9` 之九個字串，
逐字元相符。Privacy 所記兩處範本瑕疵（R11:R59 之 DV 指向 `$A$1:$A$11`；
`Reference!C9` 與 `下拉選單!A6` 字串不一致）**同一範本，同樣適用**，
不繞過，隨 RD-1 上報。

### 3.4 Source-quoted tokens [ADD] —— §11 profile-scoped 例外
SR24 條文含下列原文標記，**引用時照錄，不得改寫為 `"..."`**：

| token | 出處 |
|---|---|
| `«Front»`／`«Rear»` | 9.3、9.4.1（法文引號） |
| `15h`、`7/7`、`1-7`、`1-8` | 2.7、16.7、16.8、16.13 |
| `°F/C` | 2.10、16.10 |
| `LEDs (.` | 12.1 —— **明顯誤植，仍照錄**；修正 spec 原文非 TC 作者權限 |

作者自身之敘述（procedure 之按壓目標、非引用之 ER）一律用 `"..."`。
lint 對照 `section_fulltext.tsv` 之來源列驗證保留 token，不逕行禁用。

### 3.5 Spec Reference [ADD] —— 沿用 §10.7 預設格式
格式 `{spec_filename}_{section_id}`，stem 固定為
`SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`
（R-C1）。**不得改寫為 SR25。**

外部 spec 引用（Home Screen HMI L&F，R-C17）另列其自身 section，
**不併入 Comfort stem**，且須寫全名指向 SR24 Post 2A (March 17 2023)
—— cache 內同時存有 SR25 版（上繳 06 §6 之警示）。

### 3.6 Remarks [ADD]
空字串，除非 BLOCKED 列、anomaly 標記或已記錄之 workaround。
**外部可見**（AMFM R10-4）：不得出現內部 ruling id 或 `A-CF…`。

### 3.7 / 3.8 / 3.9 [繼承 Privacy 同編號條款]
- **Q 欄 Estimated Test Time**：`UNRULED_BLANK`，生成時留白並於 dry-run
  摘要列為具名之 blank-by-decision 欄
- **S 欄 Functional Safety**：一律 `NA`（Privacy R30-3；AMFM 158/158 前例）
- **T–Z 欄 Vehicle Model**：一律留白（Privacy R30-4）。
  **A-PV15 同樣適用於 Comfort**：範本七欄止於 27 世代，本專案平台為
  HDCC28，**不得將 27 世代欄位對映至 28 平台**。登為 Comfort 自身 anomaly

## 4. Split policy [ADD]
泛用 §8.3 適用。Comfort 特有：

- **`14.19` 之 8 leaves 已與條文 8 個 bullet 一一對應**（上繳 07 §5），
  037 之拆法與條文結構一致，**不得再合併**
- **R-C19 適用**：ch11／ch12 之 `opens popup` 差異一律以 `expected_result`
  表達，不得寫成不同 procedure 步驟或 pre_conditions
- **SYNC 重疊**：`2.6.1`／`2.11`（及 `16.6.1`／`16.11`）內容重疊而分屬兩組，
  撰寫時須一併閱讀對造節，依 §4.6 判 sibling，必要時輸出 `duplicate_of`
- **ch2 ↔ ch16 之平行節不得互相引用或省略**：兩章條文近似但非等同
  （如 airflow 4 states vs 5 states、`ICE7` 之 MAX DEF 為 ch16 獨有），
  每組 TC 一律回自身節之全文

## 5. Marker vocabulary [ADD]
prefix `A-CF`。**目前無 marker。**

**特別聲明**：16.1、18.2–18.4 四節依 R-C16 為 **RD-1 覆蓋缺口項，
不產生任何 workbook 列**（不同於 Privacy 之 `[BLOCKED-ECU]` 產生 BLOCKED
列）。不指派 tc_id、不入 coverage 分母、不列 BLOCKED。
新增 marker 須先裁決，生成當下不得自行創造。

## 6. 寫回與交付完整性 [繼承 Privacy §9 ＋ 跨 feature 條款]
- `features/comfort/BASELINE.sha256`（來源檔，tracked）與
  `DELIVERY.sha256`（append-only，tracked）；每次 session 開啟與 batch gate
  以 `shasum -a 256 -c` 驗，任何 `FAILED` 停工
- **R18-3**：`backend/xlsx_surgical.py` 為唯一寫入路徑；zip member 與 DV
  count 之 invariant 為 ABORT 級
- **R20-5**：既有四個 feature 之 `write_back.py` 已隔離，**不得作為起點**
- **R22-1**：hash 稽核為現在式陳述，「相符」不蘊含「未曾被覆寫」

## 7. 不繼承者 [ADD]
| Privacy／SXM 條款 | Comfort |
|---|---|
| Privacy §1.1 ECU 歸屬（tag vs subject） | **不繼承** —— Comfort 之 037 無 ECU 欄，spec_mode 亦不同 |
| Privacy §3.5 `CFTS022-{artifact_id}` | **不繼承** —— Comfort 用 §10.7 預設 filename_section 格式 |
| SXM cite-form（R11） | **不繼承** —— 129 節全數解析成功，無短碼 |
| SXM 吸收機制（R10-2） | **不繼承** —— 覆蓋缺口依 R-C16 走 RD-1 |
| Privacy `[BLOCKED-ECU]` marker | **不繼承** —— 見 §5 |
| revision C 之 Q／S／T–Z 處置 | **繼承**（範本層級，非 feature 層級） |

**其他 feature 之裁決不因類比而適用於 Comfort。** 遇 AMFM／SXM／Privacy
裁決可涵蓋之情形，回 chat 取得 Comfort 之裁決。

## 8. Known anomalies [ADD]
`features/comfort/ANOMALIES.md`，A-CF01 … A-CF13（第四項為 `12.1` 之
`LEDs (.`）。**A-CF07 由 §0.1 處置後可結案。**
新發現於發現當下登記並具名引用之節次。

---

## 9. 待 Pei 裁定之三處

| # | 事項 | 分析層建議 |
|---|---|---|
| 1 | §3.1 Test Item 是否繼承（modal 允許於該欄） | 建議繼承，**但簽署前須對 `home` done region 實測比對**，不以繼承為由逕採 |
| 2 | §3.4 之 `«Front»`／`«Rear»` 是否照錄 | 建議照錄（§11 profile-scoped 例外之既有前例：Home A-H10） |
| 3 | §0.1 之 Excel 實開確認由誰執行 | 該步驟 Privacy 由 Pei 執行；Comfort 同 |

---

## 10. 本包產生之新條文清單（自檢）

無新 R-Cnn 條文。本包為 Tier 2 草案，簽署後成為
`docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`。
§9 三項待裁；其餘條款於簽署時一併生效。
