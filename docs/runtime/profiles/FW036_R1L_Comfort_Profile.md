# Project Profile — FW036 / R1L SWE1 Comfort (SR24 Comfort HMI Logic and Flow, Stellantis newR1L)

> **Approved 2026-08-15** — 下放包 `15_profile_draft.md` 之全部條款，
> 加 `16_profile_signed.md` §1 之三項裁定（Pei，2026-08-15：「裁的都是是是是」）。
> 三項皆「照建議」：§3.1 繼承但附實測條件（轉為 **G-1** gate）、§3.4 source
> token 照錄、§0.1 之 Excel 實開確認由 Pei 執行。

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.
>
> Instantiated from `FW036_R1L_Privacy_Profile.md` — 最近之 BLANK／revision C
> sibling。**結構條款可繼承，內容條款不繼承**：凡標「繼承」者為結構性，
> 其餘一律就 Comfort 自身證據重新導出。Comfort 與 Privacy 無共通 spec、
> 無共通 037 家族，故每一處內容差異皆重新推導，見 §7。

---

## 0. Project identity [ADD]

- Program：Stellantis newR1L；scope 037-A03 Comfort，**403 leaves**
  `SWE1-HVAC-001…129`（含 34 列 parent 形態之 Functional Requirement，**R-C3**）
- spec baseline：**SR24 CR24879 (September 25 2023)**（**R-C1**）。
  SR25 為 out-of-scope 參考，**不得作為來源**
- Deliverable workbook：FM-WI-FSM-036-A01 通用空白範本 `SWQT_20260121`
  （與 Privacy 同一份，65,821 bytes，SHA256 `cd876c202c71e74b…`）。
  **workbook_state = BLANK** —— 無 legacy region、無 done region、無凍結列
- Test Group = `Comfort`（**R-C6**）；tc_id = `NR1L-ComfortHMI-{NNN}` 自 001
  （**R-C7**，序號由 generator 指派，LLM 不得自行產生）；
  author on new rows = `PeiPYHsu`
- **Form revision C，欄位位移同 Privacy §0**：Q = Estimated Test Time、
  R = design_method、S = functional_safety、AA = author、AH = remarks。
  資料工作表 `Test Case Specification 測試用例規範`
- style authority：**具名 `home`** done region（144 列），
  **`amfm` 具名排除**（`DECISIONS.md` §4 已簽）。cross-feature exemplar 一律標
  `style only`；**每個字面值須回溯 Comfort 自身 spec 並以 lint 強制**（A-026 教訓）

### 0.1 Template preparation state [ADD] —— A-CF07 之處置

範本附帶兩列樣本殘留（第 10–11 列）。**依 Privacy §0.1 之 R23-4 程序處理，
逐字繼承**：

- 以 `backend/xlsx_surgical.py` 清空五格：**D10 / F10 / G10 / S10 / D11**，
  `s=` style 屬性原地保留
- **B 欄不得動**：B10 為 `=IF(ISBLANK($D10),"",ROW()-9)`，清 B 會刪掉範本
  自己的編號機制
- **不得整列刪除**：會位移 DV 之 `sqref` 與 R10 之 x14 下拉

首筆 TC 落於 **row 10**。備妥之 workbook 與其來源記入
`features/comfort/DELIVERY.sha256`（ENTRY 001）。

**寫回前須經 Pei 於 Excel 實際開啟確認四項**（Privacy R29-1 前例，
16 §1 裁定 3 確認由 Pei 執行）：

1. 無修復提示
2. R 欄下拉可用且為九項
3. D5 Scope 正確
4. 第 10–11 列已清且無殘留列號

**程式層檢查不能代替 Excel 自身之檔案完整性判定。**

---

## 1. Requirements authority chain [ADD]

- Chain：SR24 spec section → 037-A03 leaf（`SWE1-HVAC-nnn(-nn)`）→ FW036 TC
- **spec_mode A**（SYS1 export）。條文權威為
  `spec-index/cache/SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023).xlsx`
  （70,040 bytes）。**唯一來源**，`inputs/` 不得存副本（**R-C11**）
- section ↔ parent req_id 為 **1:1 雙射**（129 ↔ 129，上繳 05 實測）
- **條款標籤（`C13.)`／`ICE11.)`／`HVS1.`／`W0.)`）不是唯一鍵**（A-CF13 四項）。
  traceability 一律以 **outline 節次**為鍵；條款標籤僅得出現於 `reasoning`
  與 `test_item` 之敘述
- **全文權威**：`data/section_fulltext.tsv`（129 列，不截斷）。
  `layer3_map.tsv` 之 `section_title` 為導覽欄位，**不得用於判讀**（**R-C18**）

## 2. Test Set vocabulary [OVERRIDE — 取代泛用自由標籤]

- Test Group（G 欄）= `Comfort`；Test Set（H 欄）取 framework Part N 之
  **15 組**，逐列填入。`fill_test_group_set: true`（BLANK，canon §2）
- **Layer 3 = SR24 outline 節次，framework 內部，永不寫入 workbook**（§4.1.5）
- `specification_reference`（N 欄）依 §10.7 承載 section —— **那是
  traceability 欄位，不是 Layer 3 欄位**，不得因「Layer 3 不入 workbook」
  而留白
- 最大組 `Heated Vented Seats`（59）**刻意不拆**（12 §1 裁定：同一進入路徑）。
  工作量以 BATCH 處理，不以拆 Set 處理

> **Part N 之兩次修正案已生效**（`features/comfort/framework.md`）：
> #15 更名 `Comfort Widget` → `Home Screen Widget`（13 §2）；
> 四節改置 `2.16`／`16.17` → Temperature and Fan 對、`2.14`／`16.14` →
> Anatomy 對（14 §1）。Test Set 之數量與名稱邊界不變。

## 3. Comfort house style

### 3.1 Test Item [OVERRIDE — 取代 §4.3 僅 tc_title]

> **G-1 PASS 2026-08-15**（下放包 17 §1）。本段生效。
> provenance 但書降為腳註，**不再具阻卻效力** —— 見本段末 †。

**繼承 Privacy §3.1 / SXM §3.1（結構性）**：Test Item = 以 spec 語言濃縮之
需求陳述，**modal 僅此欄允許**（引用需求原文）。泛用 §4.3 之 tc_title
（無 modal）仍產出於 JSON 供 lint 與 sibling 判別。ER 一律無 modal（§6）。

**G-1 實測結果**（`features/comfort/scripts/gate_g1_test_item.py`，可重跑）：

| 量測項 | 值 |
|---|---|
| 母體 | `home` done region，Z 欄 == `ArifChen`，**144 列**（assertion PASS） |
| 含 modal | **143 / 144（99.3%）** |
| 不含 modal | 1（row 135 —— 內容為 widget 對照表，非行為陳述） |
| modal 詞頻 | `shall` ×176、`would` ×1 |
| Test Item 長度 | min 83、**中位 273**、max 2657 |
| 形態 | `The system shall …` ＋ 情境括號；**非 tc_title 型短語** |

→ 與 §3.1 所述一致，**§3.1 生效**。

> † **provenance 腳註**（17 §1.1：事實保留，不阻卻判定）：`home` 之 RECON 所測檔
> （`…_Home_20260720.xlsx`，SHA256 `0e72b1ec…`）與 Home v2
> （SHA256 `cfc007f3…`）**皆不在 repo**。本次量測對象為
> `forms/…_Home_20260809.xlsx`（SHA256 `1895fb2a…`），FORMS.md 記其為
> pre-A-H26 build 加四道編修（**D5 / F / G / K / Z**）。
> **I 欄（Test Item）不在該四道之列**，此為「內容未受影響」之論據 ——
> 但該論據來自 FORMS.md 自身之 diff，在 Home v2 缺席下無法交叉驗證。
> 17 §1.1 依 **R-C15**（判準為蘊含，非直接）裁定此不改變判定：可設想之風險
> 為「該副本之 I 欄曾被編修」，然**一次「把 `shall` 引入 144 列中 143 列」
> 之編修並非可信之情形**。證據為真即蘊含結論，縱其來源鏈有一段未經交叉驗證。
>
> **母體選擇器之發現須保留**：`features/home/feature.yaml` 之
> `done_region.author_value` 為 `Arif`，該副本實為 `ArifChen`；以 `Arif`
> 選取得 0 列，而 0 列會產出「全數不含 modal」之空集合結論。母體列數
> assertion 擋下此事 —— 登為 **A-CF14**。

### 3.2 Pre-Conditions [ADD] —— Comfort 之 spec trigger

以下為 §8.5 例外之合法 Pre-Condition 類別，**每一句須標 source class**
（`spec-verbatim` / `spec-derived` / `test-setup`），**未標者視為未追溯**
（Privacy R36-4）：

- **設備配置軸**（本 feature 之主軸，逐節出現）：ATC / MTC、單區 / 雙區 /
  四區、tri-mode 有無、MAX A/C 有無、MAX DEF 有無、独立座椅分區有無、
  加熱方向盤 Multi-Level / Single-Level、Standard vs Multi-Level 座椅、
  **secondary lower screen 之有無**（第九軸，19 §2.1）
- **機型軸**：R1 Low / R1 High（`14.19` 之 `-02` 為唯一含此條件者）
- **市場／變體軸**：EMEA ICS（ch16 全章）
- **禁用**：`HU is powered on`、`Climate is available`（皆為隱含環境前提）

**每一條配置條件須具名其來源節次**；不得以「某些車輛有此配置」概括
（§8.4.1 禁造值）。

**每一個 `pre_conditions` 行須先通過 R-C28 之三問，出處在最前**（24 §4.3）：
先問「該事實在其標註來源節之 `full_text` 有無明文對應」，無則停 ——
那不是落點問題，是 §7 FF 或 §8.4.1。第一問之回答**須具名條文之相關句**，
不得以「合理」「顯然」「恆常如此」代之。
**此為 Phase 4 展開之前置，非預防性建議** —— pilot 之 TC-007 即栽在此處。

**第九軸之 source class 逐節判定，不得跨節套用措辭**（19 §2.1）：讀該節
`full_text`，條文有字面表述者標 `spec-verbatim` 並照錄其措辭；由條文推得者標
`spec-derived`。**不得將 6.3 之 `non-foldable secondary lower screen` 措辭
套用於 13.x** —— 那是另一節的文字（R-C18 同型風險：措辭正確地屬於別處）。

**lower screen 之 stowed／retracted 為執行期狀態，非配置軸**（19 §2.2）。
判定測試：

> 該 TC 之驗證目標，是否就是「螢幕處於該狀態時之行為」？
> 是 → 該狀態為 spec 定義之 trigger condition，入 `pre_conditions`，標 source class
> 否 → 該狀態係為使測試可執行而設置，入 `test_procedure` 之步驟

不得因「寫在 Pre-Condition 比較省事」而上移；亦不得因「它是狀態」而一律歸
Pre-Condition —— §4.4 明禁 step-controlled state。

### 3.3 Design Method [OVERRIDE — 限縮 §12 輸出字串]

**繼承 Privacy §3.3**：僅得回傳 workbook `下拉選單!A1:A9` 之九個字串，
逐字元相符。Privacy 所記兩處範本瑕疵（R11:R59 之 DV 指向 `$A$1:$A$11`；
`Reference!C9` 與 `下拉選單!A6` 字串不一致）**同一範本，同樣適用**，
不繞過，隨 RD-1 上報。

### 3.4 Source-quoted tokens [ADD] —— §11 profile-scoped 例外

SR24 條文含下列原文標記，**引用時照錄，不得改寫為 `"..."`**
（16 §1 裁定 2；前例 Home A-H10）：

| token | 出處 |
|---|---|
| `«Front»`／`«Rear»` | 9.3、9.4.1（法文引號） |
| `15h`、`7/7`、`1-7`、`1-8` | 2.7、16.7、16.8、16.13 |
| `°F/C` | 2.10、16.10 |
| `LEDs (.` | 12.1 —— **明顯誤植，仍照錄**；修正 spec 原文非 TC 作者權限（§8.4.2） |
| `(-, +)` | 13.2 ~ 13.6（6 節）—— 條文自有記法。**依位置分割**（19 §3，不新增例外）：<br>`test_item`（承載需求原文，§3.1）與 ER 中之引用片段 → **照錄 `(-, +)`**<br>`test_procedure` 之按壓目標與非引用之 ER 敘述 → **`"-"` / `"+"`** |

作者自身之敘述（procedure 之按壓目標、非引用之 ER）一律用 `"..."`。
lint 對照 `section_fulltext.tsv` 之來源列驗證保留 token，**不逕行禁用**。

### 3.5 Spec Reference [ADD] —— 沿用 §10.7 預設格式

格式 `{spec_filename}_{section_id}`，stem 固定為
`SYS1_HMI_Comfort_HMI_Logic_and_Flow_R1_SR24_Post_3A_CR24879_(September_25_2023)`
（**R-C1**）。**不得改寫為 SR25。**

外部 spec 引用（Home Screen HMI L&F，**R-C17**）另列其自身 section，
**不併入 Comfort stem**，且須寫全名指向 **SR24 Post 2A (March 17 2023)**
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
  表達，**不得**寫成不同 `test_procedure` 步驟或 `pre_conditions`。
  pilot review 時違反者列 **defect**（非 style-divergence）
- **SYNC 重疊**：`2.6.1`／`2.11`（及 `16.6.1`／`16.11`）內容重疊而分屬兩組，
  撰寫時須一併閱讀對造節，依 §4.6 判 sibling，必要時輸出 `duplicate_of`
- **ch2 ↔ ch16 之平行節不得互相引用或省略**：兩章條文近似但非等同
  （如 airflow 4 states vs 5 states、`ICE7` 之 MAX DEF 為 ch16 獨有），
  每組 TC 一律回自身節之全文

## 5. Marker vocabulary [ADD]

prefix `A-CF`。

### 5.1 `[BLOCKED-SPEC]`（R-C24，2026-08-15 裁定）

**適用**：某 leaf 之全部內容為對外部 spec 之委派或等效性宣告，扣除該委派後
於本 feature 範圍內**無任何可獨立驗證之餘留**者。

**產出 BLOCKED row** —— 不省略、不併入 sibling leaf、**不以複製 sibling 之
procedure 充數**（後者為 §7 之 False Pass：一條會通過但不驗證其 leaf 所要求
之事的 TC，remarks 之標記不會使它停止通過）。

| 欄 | 值 |
|---|---|
| `test_procedure` / `expected_result` | **空** |
| `specification_reference` | 該 leaf 自身之 outline，照常填 |
| Remarks | `[BLOCKED-SPEC]` ＋ 擁有該內容之文件名 ＋ 一句說明何以無餘留 |
| 其餘 | 依 profile 常規 |

Remarks **外部可見**（AMFM R10-4）：不得出現內部 ruling id 或 `A-CF` 編號。

**與 Privacy `[BLOCKED-ECU]` 之區別 —— 不得互相類推**：

| | `[BLOCKED-ECU]`（Privacy） | `[BLOCKED-SPEC]`（本 feature） |
|---|---|---|
| 成因 | 行為由**另一 ECU** 執行 | 行為**可觀察**，但其規範內容由**另一份 spec** 擁有 |
| 本 ECU 有無可觀察端 | **無** | **有**（只是無獨立於 sibling 之內容可驗） |
| 解除條件 | 該行為改由本 ECU 執行，或取得其可觀察指標 | 外部 spec 之內容納入本 feature 範圍，或該 leaf 經 037 改寫 |

**兩者外觀相同（皆無 procedure），成因不同。** 見到空 procedure 時，
須讀 Remarks 之 marker 方知其類別。

**lint 之豁免為具名回報行，不得靜默跳過**（前例：上繳 06 §2.1 之
`and n != "Comfort Widget"`）。`proc-min-steps` 與 `proc-er-1to1` 對
BLOCKED row 之豁免，每次 lint 皆輸出受豁免之 tc_id 清單。

**目前之 `[BLOCKED-SPEC]` 列**：`SWE1-HVAC-080-02`（HMI Core Logic and
Flow requirement N0）、`SWE1-HVAC-081-02`（CFTS044）。

### 5.2 不產生 workbook 列者

**16.1、18.2–18.4 四節依 R-C16 為 RD-1 覆蓋缺口項，不產生任何 workbook 列**
—— 與 `[BLOCKED-SPEC]`／`[BLOCKED-ECU]` **皆不同**：那兩者產生 BLOCKED 列，
本類**連列都不產**（037 未對其產出需求，故無 leaf 可掛）。
不指派 tc_id、不入 coverage 分母、不列 BLOCKED。

新增 marker 須先裁決，**生成當下不得自行創造**。

## 6. 寫回與交付完整性 [繼承 Privacy §9 ＋ 跨 feature 條款]

- `features/comfort/BASELINE.sha256`（來源檔，tracked）與
  `DELIVERY.sha256`（append-only，tracked）；每次 session 開啟與 batch gate
  以 `shasum -a 256 -c` 驗，任何 `FAILED` 停工
- **R18-3**：`backend/xlsx_surgical.py` 為唯一寫入路徑；zip member 與 DV
  count 之 invariant 為 **ABORT 級**
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
`LEDs (.`）。**A-CF07 由 §0.1 處置後可結案** —— 待 Pei 於 Excel 確認四項。
新發現於發現當下登記並具名引用之節次。
