# ANOMALIES — FW036 Display HMI

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-DMnn]`. PENDING entries block their batch until a
Pei ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.

本輪（下放包 01+02，Phase 0/1）全部為**登記**，無一裁定。證據皆為執行層
於 `features/display/inputs/` 之複本上獨立重算所得，重算腳本見
`features/display/scripts/`。

---

## A-DM1 — 037 二分頁對同一物件使用兩套 id 寫法  [PENDING]

`SWE1 Requirements` r8–r15 之 `SWE-Requirement ID ` 為 `SWE-DM-001…008`；
`SYS2 Traceability` r2–r9 之 `SWE1 ID` 為 `SWE1-DM-001…008`。二者之
`Requirement Title` 逐列相同，故為同一物件之兩種寫法。

- 證據：`scripts/recount_037.py`（8/8 符合 `^SWE-DM-\d{3}$`；Traceability
  分頁全 8 列列印於輸出）
- 影響：`feature.yaml` 之 `req_id` 欄形態未定（下放包 01 Q3）
- 提案處置：向上游反映二分頁不一致；`req_id` 之形態依 Q3 由 Pei 裁定。
  執行層不推定二者等同（R-DM3）

## A-DM2 — 037 所引之 `SYS-RA-DISP-*` 在 SYS2 released 版 0 命中  [PENDING]

`SYS2 Traceability` 之 `Sys-RA-Feature-ID(s)` 為 `SYS-RA-DISP-001…008`。
SYS2 `Basic Report` 333 資料列中，`SYS2 Sys-RA-Feature-ID` 含 `DISP` 者
**0 列**；以 8 個值逐一比對亦 **0 命中**。

- 證據：`scripts/recount_sys2.py`（ids containing 'DISP': 0）、
  `scripts/coverage_map.py`（id-basis hits: 0）
- 影響：037 → SYS2 之追溯鏈在本素材組內無 id 橋樑；連帶使 spec_reference
  之查找無法由 id 導出（見 A-DM10）
- 提案處置：登記，不推定 `SYS-RA-DISP-001 ↔ SYS-RA-DM-001`（R-DM3 明文
  禁止）。以 DR-DM3 向上游索對應表或含 DISP id 之 SYS2 版本

## A-DM3 — `Source NRL ID(s)` 8/8 為空，而 Excluded 分頁反有 id  [PENDING]

`SYS2 Traceability` 之 `Source NRL ID(s)` 欄 8 列全空；同檔
`Excluded NRLs (HW-only)` 分頁之 `NRL ID` 欄卻有 8 個值 —— 且該 8 值經實測
為 Melco ID 而非 NRL ID（R-DM4，本輪 8/8 於 SYS2 `SYS2 Melco ID` 之 99 個
token 中命中，已複驗）。

- 證據：`scripts/recount_037.py`、`scripts/recount_sys2.py`
- 影響：037 之 NRL 追溯欄無內容，排除項反而有追溯值，方向相反
- 提案處置：向上游反映；不影響本輪，因 R-DM4 已解 Excluded 分頁之語意

## A-DM4 — SYS2 `Category` 欄大小寫變體 8 列  [PENDING]

`SYS2 分類 Category` 之逐字分布含 `Functional requirement` 1 列與
`Out of scope` 7 列。任何以逐字比對實作之 gate 會少算此 8 列
（Functional Requirement 母體 79 vs 正規化後 80）。

- 證據：`scripts/recount_sys2.py` 之「case-variant rows」節，列號為
  r314（`SYS2-RA-313`）、r23/r24/r25/r27/r64/r70/r81（`SYS-RA-DM-*`）
- 影響：覆蓋母體大小、任何 Category 篩選
- 提案處置：本 feature 所有 Category 篩選一律先正規化大小寫，並於腳本
  明示；向上游反映欄值未正規化

---

### 升級（2026-08-24，下放包 06 步驟 9）：匯出檔自帶之值字典證明何者為正典

SYS2 之 `_polarion` 分頁（368 非空列，四輪未看）**是欄位合法值之字典**，
涵蓋 341 個欄位。`SYS2 分類 Category` 之合法值逐字為五個：

```
Heading / Information / Functional Requirement /
Non Functional Requirement / Out of scope
```

以此為準複驗 `Basic Report` 之 333 列實際用值：

| 實際值 | 列數 | 是否在字典中 |
|---|---|---|
| `Out of Scope` | **116** | **否** |
| `Information` | 85 | 是 |
| `Functional Requirement` | 79 | 是 |
| `Heading` | 45 | 是 |
| `Out of scope` | 7 | 是 |
| `Functional requirement` | **1** | **否** |

**共 117 列（35%）之 Category 值不在該匯出檔自己的合法值清單中，且
違規的是多數拼法** —— `Out of Scope` 116 列違規，合法之 `Out of scope`
只有 7 列。

三項後果：

1. 本條原提案「一律正規化大小寫」**得到逐字之權威依據**，不再只是
   執行層之便宜行事：字典說 `Out of scope` 才是合法值。
2. **`Non Functional Requirement` 是合法類別但 0 列**。R-DM7 之覆蓋母體
   （`Functional Requirement` 80 列）因此可確認**未遺漏 NFR** —— 此前
   無人驗過這件事。
3. 向上游反映之內容應改為「值未依 `_polarion` 字典校驗」，而非
   「大小寫不一致」—— 後者聽起來像格式瑕疵，前者是資料校驗缺口。

#### 結清（2026-08-25，下放包 07 §1.3 / 步驟 9，R-G17）

上繳 06 §10 第 4 項所留之待辦「`_polarion` 之其餘 340 個欄位字典完全
未用」**不存在，本項結案**。分析層更正、執行層獨立複驗：

`_polarion` r4 起之 367 個資料列中，**第一欄含 `:` 者才是欄位列舉字典**：

| 類別 | 列數 | 相異鍵 |
|---|---|---|
| 欄位列舉字典（鍵含 `:`） | 27 | **2** |
| 工作項連結列（鍵無 `:`，如 `NR1L/NRL-163104`） | 340 | 340 |

兩個字典之鍵尾段為 `SYS2 分類 Category` 與 `Type`，而
**`Basic Report` 之 81 個欄名中能與字典鍵對上者恰為此 2 個**。逐欄校驗：

| 欄 | 字典值數 | 實際用值數 | 違規列數 |
|---|---|---|---|
| `SYS2 分類 Category` | 5 | 6 | **117 / 333** |
| `Type` | 22 | 1（`SYS2_System Requirements Analysis` ×333） | **0** |

**可校驗之欄只有兩個，兩個都已校驗完畢。** 誤把 340 列工作項連結當成
欄位字典，會產生一個做不完的待辦（R-G17 明文警示此點）。

## A-DM5 — 037 `SWE1 Requirements` 表頭含不規則空白  [PENDING]

實測表頭原始字串含尾空格與雙空格：`'SWE-Requirement ID '`、
`'Requirement  Title'`、`'Requirement  Description'`、`' Impact'`、
`'Verification Method '` 等。以逐字字串查欄名者全數落空。

- 證據：`scripts/recount_037.py` 之 columns (RAW, repr) 節
- 影響：任何以精確欄名取欄之實作
- 提案處置：本 feature 之欄名比對一律先 `" ".join(str(s).split())`

**適用範圍擴及 036 母本（2026-08-24，下放包 03 §2.2）**：036 母本
`Test Case Specification 測試用例規範` 分頁 r9 之表頭，其分隔符為**換行**
而非空格，33 欄皆然 —— 例：`'No.#\n序號'`、
`'Test Case Design \nMethods\n測試用例設計方法'`、`'HDCC27\nAtl-Hi\n'`
（尾隨換行）、`'Specification Reference \n規格參考'`（尾空格＋換行）。

上繳包 02 §6.4 之表頭清單標為 `(raw)` 卻印正規化後之值，會使讀者誤以為
036 表頭乾淨。`scripts/probe_036.py` 已改為 `repr()` 輸出，全欄見上繳包
03 §3。SYS2 側之同類情形為欄名帶雙語括號尾綴（見 `recount_sys2.py` 之
`col()` 前綴回退）。

> 三份素材之表頭皆不可逐字取欄。此為本 feature 之通則，非個案。

## A-DM6 — 037 `Excluded NRLs` 分頁之 `Sys-RA-Feature-ID` 欄 8/8 為空  [PENDING]

該分頁四欄中，`Sys-RA-Feature-ID` 欄 8 列全為 `None`，故排除項亦無法
回指 SYS2 之 feature id，只能靠 Melco ID。

- 證據：`scripts/recount_037.py` 之 Excluded NRLs 全列輸出
- 提案處置：登記；與 A-DM2 併同向上游反映追溯欄空置

## A-DM7 — scaffold 之 `feature.yaml` 模板與 R-G1 母本不符（1 分頁名 + 3 欄）  [PENDING]

`scripts/new_feature.py` 之模板宣告 `sheet: "Test Case Specification&Result"`
與 `design_method: Q` / `functional_safety: R` / `author: Z`。R-G1 母本
（`…_SWQT_20260817_ext.xlsx`）之實測為分頁
`Test Case Specification 測試用例規範`，且欄位為 `design_method: R` /
`functional_safety: S` / `author: AA` —— 母本在 Q 欄多一欄
`Estimated Test Time (mins)`，其後整體右移一格；`author` 之模板值 Z 欄
實際為 `Fastack (376) Atl-Mi`（車型欄）。

- 證據：`scripts/probe_036.py`（15 鍵中 12 鍵 MATCH，3 鍵 MISMATCH，
  並列出各鍵之表頭候選欄）
- 影響：**若照模板寫回，author 會寫進車型欄、design_method 會寫進
  預估測試時間欄**。本輪已於 `feature.yaml` 改為實測值
- 提案處置：模板之修正屬全域（影響此後每個新 feature），Tier 2；
  本輪只登記與在本 feature 之 `feature.yaml` 內更正

## A-DM8 — `recon.py` 於 037 分頁名處中止  [PENDING]

`python3 scripts/recon.py --feature features/display` 以
`KeyError: 'Worksheet Analysis Report does not exist.'` 中止，失敗點為
`scripts/recon.py:568`（`survey_a03()` 內 `ws = wb["Analysis Report"]`）。

- 影響：**RECON.md / DECISIONS.md / `data/recon.json` 本輪未產出**
- 提案處置：依 R-DM5(b) 不修腳本。修法（新增分頁簽章或由 feature.yaml
  指定分頁名）屬 Tier 2，見下放包 01 Q5

## A-DM9 — `intake.py` need-list 之理由與 R-DM5(c) 所述不同  [PENDING]

R-DM5(c) 預期腳本回報「不可推導（`Source Requirement ID` 欄為 Polarion id
而非 `name_{section}` 文件引用）」。實際輸出為
`NO requirement report found — cannot derive the need list`。

該句非空清單、有說明，故未達 R-DM5(c) 之登記門檻；惟其理由是
sniffer 未認出 037（R-DM5(a) 之下游效應），非欄位語意。**故 need list
「不可推導」一事本輪等同未經檢驗**。

- 提案處置：登記為理由失真；Q5 修 sniffer 後須重跑並複核 need list

## A-DM10 — SYS2 無指向 CFTS 條號之錨，mode D 之 spec_reference 無 id 橋樑  [**拆條**：a 已 RESOLVED／b 仍 PENDING]

canon §3 之 mode D 要求 spec_reference 為**查得**。實測：

- CFTS 本文可抽出 outline id 184 個相異（其中 182 個可由 Heading 樣式
  取得），故 CFTS 側有可用索引
- SYS2 之 `SYS2 文件識別碼 Document ID` 為逐列遞增之 Polarion 文件 id
  （`SR26_20260310-1533` … `-1778`，另 78 列為 `SR26_20250813-1632`），
  **不是 CFTS 條號**
- SYS2 `Melco ID` 之 99 個 token 在 CFTS 本文中逐字命中者僅 1 個，且該
  token 為 `NA`（非 id）
- 加上 A-DM2（037→SYS2 id 0 命中），自 SWE-DM leaf 走到 CFTS 條號的
  三段鏈路每一段都無 id 橋樑

- 證據：`scripts/probe_spec_mode.py`
- 影響：Phase 4 之 spec_reference 目前只能靠文字比對定位條號
- 提案處置：登記；spec_reference 之取得方式屬 Tier 2

---

### 拆條（2026-08-24，下放包 04 §3.4／步驟 7）

以上原文依 R-TM13 保留，不刪除、不改寫。本條實含兩件事，分列處置：

#### A-DM10a — 訊號側之 id 橋樑　**[RESOLVED]**

原條所述「SYS2 之 `$Signal$` 無法接到任何外部定義」一節**已解**。
橋樑為 LID `CAN Mapping` 分頁（R-DM17 之三段解析鏈）。

執行層獨立重算（`scripts/signal_resolution.py`，
`data/signal_resolution.tsv`）：

| 項 | 實測 |
|---|---|
| FR 母體之 `$Signal$` | 15 |
| 於 LID `Logical Identifier` 欄逐字查得者 | **15 / 15** |
| 解出之 `MESSAGE.Signal` 值（多值逐值一列） | 26 |
| 其中於 DBC 查得 `SG_` 者 | **24 / 26** |
| 至少解得一列之 `$Signal$` | **14 / 15** |

> **R-DM21 之補註（2026-08-24）**：上表各數字所止之段 —— 段 1（SYS2 →
> LID）**15/15**；段 2（LID → CAN 名）解出 **26** 個 `MESSAGE.Signal`；
> 段 3（CAN 名 → DBC）**24/26 列、14/15 個訊號**。
> 本條之「已解」指段 1 與段 2 之橋樑已建立，**不表示段 3 已全數備齊**。

**惟下放包 04 §3.4 之「15 個 `$Signal$` 全數解得」須加限定**：該陳述在
**LID 階段**成立（15/15），在 **DBC 階段**不成立 ——
`CCDMF_RQ_DISP_INTS` 之 CAN 名 `RADIO_B4.CCDMF_RQ_DISP_INTS` 在兩本 DBC
皆無此 `SG_`，而訊息 `RADIO_B4` 本身存在於 BHCAN2-R1，故屬 R-G13 三要件
齊備之真查無（`forms/LOOKUP_MISSES.md` M-1、DR-DM5）。

同時撤回之誤讀（依下放包 04 §3.4 第 1、2 點）：
`TGW_DISP_STAT` → `TGW_DISP_STATSts` 之 `Sts` 尾綴**不是規格錯誤**，
`ICS*` 系列在 DBC 0 命中**不是缺漏** —— 二者皆為「以 LID 名查 CAN 名」
之必然結果。

#### A-DM10b — 章節側之 id 橋樑　**[PENDING]**

SWE-DM leaf → CFTS 條號之橋樑**仍不存在**。本輪未有任何進展：
CFTS 側之 184 個 outline id 與 037 之 8 個 leaf 之間，沒有任何逐字錨。
spec_reference 之取得方式仍為 Tier 2 未決，`feature.yaml` 之
`spec_reference_template` 維持 `null`。

## A-DM14 — BHCAN2 與 BHCAN-R4 為不同資料庫，且顯示訊號之收發節點相反  [PENDING]

`forms/PDT27_E2A_R1_BHCAN2.dbc`（`46cb73f3…`）與
`features/vehicle_setting/inputs/PDT27_E2A_R4_BHCAN.dbc` 之訊號名集合
三分（相異名，逐字，`scripts/dbc_probe.py`）：

| | 數 |
|---|---|
| 兩者皆有 | 310 |
| 僅 BHCAN-R4 有 | **573** |
| 僅 BHCAN2-R1 有 | 32 |

**故二者非版次關係，是不同的資料庫。** 573 個只在舊檔存在之訊號名，其在
新架構下之地位（移除／改名／移至他匯流排）本輪不推定。

三個顯示訊號之位元定義與 `VAL_` 列舉**兩本逐字相同**，但**節點相反**：

| 訊號 | 訊息 | BHCAN2-R1 | BHCAN-R4 |
|---|---|---|---|
| `DCSD_DISP_STAT` | `BO_ 1445 DIS_CENTERSTACK` | tx=**SGW**，rx=`ETM,LTM` | tx=**DCSD**，rx=`SGW` |
| `RQ_DISP_INTS` | `BO_ 1283 RADIO_B3` | tx=**ETM**，rx=`SGW` | tx=**SGW**，rx=`DCSD` |
| `TGW_DISP_STATSts` | `BO_ 1500 TELEMATIC_DISPLAY2` | tx=**ETM**，rx=`SGW` | tx=**SGW**，rx=`DCSD` |

> 下放包 04 §3.2 只列 tx。本輪一併實測 rx（`SG_` 行末之接收節點清單），
> **rx 亦隨之改變**，方向與 tx 一致地對調。

**發送節點決定 TC 該寫「送出」還是「觀察」**，故此差異非中繼資料。

- 提案處置：登記。**何者適用於本專案未裁定** —— 二選一需要專案之
  EE 架構配置為據，不在手上四份素材內

## A-DM15 — BHCAN2 含四個 FPDM 顯示訊號，而 037 與 SYS2 皆未提及 FPDM  [PENDING]

「僅 BHCAN2 有」之 32 個訊號名中，四個與顯示直接相關（逐字複驗，
`scripts/dbc_probe.py`）：

| 訊號 | 訊息 | tx | rx | VAL_ / 格式 |
|---|---|---|---|---|
| `FPDM_DISP_STAT` | `BO_ 1513 FPDM1` | FPDM | ETM | `0 OFF 1 ON 2 BLANK 3 DISP_HOT 7 SNA` |
| `TGW_FPDM_DISP_STATSts` | `BO_ 1282 RADIO_B2` | ETM | FPDM | 同上五值 |
| `FPDM_RQ_DISP_INTS` | `BO_ 1282 RADIO_B2` | ETM | FPDM | `63\|8@0+ (0.5,0) [0\|100] "%"`，`255 SNA` |
| `CameraDisplaySts` | `BO_ 1283 RADIO_B3` | ETM | Vector__XXX | `0 Default 1 View_1 … 7 View_7` |

`FPDM_*` 為 `DCSD_*` 之平行族：值域 `OFF/ON/BLANK/DISP_HOT/SNA` 與
`DCSD_DISP_STAT` 相同（惟 `DCSD_DISP_STAT` 另有 `3 RR_CMRA`，FPDM 族無），
`FPDM_RQ_DISP_INTS` 之格式與 `RQ_DISP_INTS` 逐字相同（`0.5 %/bit`、
`0–100`、`255 SNA`）。四者在 BHCAN-R4 皆不存在。

**037 與 SYS2 皆未提及 FPDM**（兩檔全文逐字查 `FPDM` 為 0）。
這是新素材帶進來的問題，不是既有缺漏。

- 提案處置：登記。**不推定其是否在本 feature 範圍內** —— 若 FPDM 為
  本專案之另一顯示裝置，則 8 個 leaf 之涵蓋面須重議；若非本專案配備，
  則其存在於 DBC 中不生影響。二者皆需專案配置為據

## A-DM16 — LID `Proxi & Configuration` 分頁含顯示相關組態旗標  [PENDING]

下放包 04 步驟 11 之停手觸發條件為「LID `Proxi & Configuration` 分頁與
本 feature 之**訊號**有關聯」。逐字測試：15 個 SYS2 `$Signal$` 在該分頁
**0 命中**，故該條件**未逐字成立**，本輪未停手、未解析 PROXI。

惟以關鍵字（`DISP`／`DCSD`／`RVC`／`Camera`／`Display`）掃描該 449 列分頁，
命中 23 列，其中四列與 Display 之 leaf 明顯相鄰：

| LID 列 | Logical Identifier | Function |
|---|---|---|
| r51 | `DCSD_cfg` | DCSD Present |
| r64 | `DSP_SK_PRSNT` | Display off soft key present |
| r131 | `NetCfg_DCSD` | （無 Function 文字） |
| r170 | `RVC_SK_PRSNT` | Rear Camera soft key present |

`DSP_SK_PRSNT` 對應 SWE-DM-001 之 Screen Off 行為、`RVC_SK_PRSNT` 對應
SWE-DM-007／008 之 RVC 行為、`DCSD_cfg` 決定 DCSD 是否存在 —— 形態上像是
TC 之**前置條件**來源。

- 證據：LID `Proxi & Configuration` 449 列 × 31 欄之逐列 regex 掃描
- **本輪未做任何 PROXI 解析**（步驟 11 明文禁止無據之工），僅登記相鄰性
- 提案處置：請裁示步驟 11 之觸發是否應由「與訊號有關聯」放寬為
  「與 leaf 之前置條件有關聯」。若是，則 PROXI 解析應排入下一輪；
  若否，本條轉為記錄性條目

---

### 裁示與執行結果（2026-08-24，R-DM20 / 下放包 05）

觸發**已放寬**為「與任一 leaf 之前置條件、可用性條件、或配備有無相關者」，
PROXI 解析自下放包 05 起 in scope。本輪之解析結果
（`scripts/proxi_candidates.py`、`data/proxi_candidates.tsv`）：

| anchor_kind | 列數 |
|---|---|
| `leaf_phrase`（leaf 片語逐字命中） | **0** |
| `cfts_usage`（`Primary CFTS Usage` 逐字含 `CFTS020`） | 1 |
| `proxi_param`（於 PROXI `Format` 逐字查得定義） | 176 |
| `none` | 269 |
| 合計 | 446 |

三個起點之逐字查詢結果：

| LID | Atlantis Signal Name | PROXI 列 | 值域 |
|---|---|---|---|
| r51 `DCSD_cfg` | `CAN node 31 (DCSD)` | **r37** | `0 = Absent 1 = Present` |
| r170 `RVC_SK_PRSNT` | `Rear_View_Camera` ／ `Rear_View_Camera_Soft_Button` | **r401、r494** | 兩者皆 `0 = Absent 1 = Present` |
| r63 `DSP_SK_PRSNT` | `Display_OFF_SoftKey_Prsnt` | **查無** | — |

**`related_leaf` 全部為空。** leaf 片語在 446 列中 0 命中 —— 與
`SWE-DM-007`／`008` 在覆蓋對照中候選為 0 同因：037 之 leaf 標題用
`RVC`／`Display RVC Handling`，而 LID／PROXI 用 `Rear_View_Camera`。
逐字比對接不上，依停止條件 14 不得猜。

`cfts_usage` 僅 1 列（r95 `Head_Unit_Screen_Size`），且該欄 **378/446 為空**
—— **其未載 `CFTS020` 不構成「與本 feature 無關」之證據**（R-G13 第 (3)
要件之反面）。

**未寫入任何 TC 欄位**（R-DM20 末段）。

## A-DM17 — LID 之 PROXI 側名稱與 Logical Identifier 不同名，且 `_Prsnt` 尾綴不一致  [PENDING]

R-G13 之教訓在 PROXI 上重演一次：LID `Proxi & Configuration` 之左欄是
Logical Identifier，PROXI `Format` 分頁用的是另一組名稱，其對應關係載於
LID 之 `Atlantis & Atlantis High` 欄組 `Signal Name`（該欄組之 `CAN` 欄
值為 `PROXI`）。

本輪之實測差距：

| 查詢鍵 | 於 PROXI `Format` 逐字查得之列數 |
|---|---|
| Logical Identifier（首版作法） | 70 / 446 |
| ＋ `Atlantis Signal Name`、`Object Text`（含多值逐值拆分） | **177 / 446** |

即：**以 LID 名直接查 PROXI 會漏掉 107 列（60%）**，與
「以 `ICSPowerButton` 查 DBC」為同一型錯誤。

另查出一處逐字不等而語意疑似同一者：LID r63 `DSP_SK_PRSNT` 之 PROXI 側名
為 `Display_OFF_SoftKey_Prsnt`，而 PROXI `Format` r692 之參數名為
**`Display_OFF_SoftKey`**（少 `_Prsnt` 尾綴）。同分頁另有
`FCW_Soft_Button`(r436)／`Rear_View_Camera_Soft_Button`(r494)／
`Glove_Box_Soft_Button`(r803) 等同類參數，**皆無 `_Prsnt` 尾綴**。

- **本輪不認定二者為同一物**（下放包 05 §六第 14 條：不逐字即不得猜），
  已依 R-G13 登記為 `forms/LOOKUP_MISSES.md` M-3，並開 DR-DM6
- 提案處置：請上游確認 `Display_OFF_SoftKey_Prsnt` 與
  `Display_OFF_SoftKey` 是否為同一參數。若是，則屬 LID 之命名不一致，
  應反映給 LID 維護者；若否，則 PROXI 缺該參數



## A-DM11 — R-DM7 覆蓋落差（**2026-08-24 更正；原結論撤回**）  [PENDING]

### 撤回之內容

本條原載「以 bag-of-words token 重疊為依據，80 列母體中 58 列無對應，
`SWE-DM-004`／`005`／`007` 命中 0 列」。**該結論撤回。**

撤回理由（下放包 03 §3.1，分析層以關鍵字直查 SYS2 `Description` 發現）：
SYS2 r30 之 Heading 為 `Multi-stage' DCSD Display Hot Algorithm`，其子列
r31–r34 為 Display Hot 之狀態機需求，與 `SWE-DM-004`／`005` 之
Requirement Title 所稱之 `Hot Algorithm` **逐字同名**。而原啟發式將
r31／r32 判給 `SWE-DM-001`、r34 判給 `SWE-DM-003`、r33 判為「無」——
**同時產生偽陽性與偽陰性，且兩者互為因果**：列被錯配到相鄰 leaf，
被搶走的 leaf 於是顯示 0。

原方法之產物依 R-TM13 保留於
`data/coverage_sys2_vs_swe_dm.RETRACTED.tsv`（檔頭已加註廢止），不刪除、
不再引用。方法本身由 **R-DM13 廢止**。

> 致誤之方法為下放包 01 R-DM7 所指定（「Description 文字」列為三種依據
> 之一），分析層已於下放包 03 §4.2 自陳「方法是我指定的」。執行層之
> 責任在於：上繳 02 §11 第 3 項雖自陳其為啟發式，**低估了嚴重性** ——
> 只說了精度不足，未察覺它會把結論指向相反方向。

### 更正後之陳述（錨定法，R-DM13）

母體不變：SYS2 `Category` 正規化為 `functional requirement` 之 **80 列**。
錨一律逐字，無錨即記無錨（`scripts/coverage_map.py`，全表見
`data/coverage_sys2_vs_swe_dm.tsv`）：

| anchor_kind（最高優先之現存錨） | 列數 |
|---|---|
| signal（`$NAME$`） | 43 |
| value（`[VALUE]`） | 1 |
| heading | 36 |
| melco | 0 |
| none | 0 |

各錨之存在數（非互斥）：含 `$signal$` 43 列、含 `[value]` **54** 列、
有 heading 祖先 80 列、Melco 命中 037 Excluded 1 列（r54）。

> **`[value]` 之數字定案（2026-08-24，R-DM18；R-DM16 全條廢止）**
>
> 判準為「寬式 `\[([^\]]+)\]` 擷取後**扣除 token 中含 `:` 者**」。
> 冒號是 Polarion 匯出 metadata 之逐字標記，非規格值。實測：
>
> | 項 | 值 |
> |---|---|
> | 寬式相異 token | **59** |
> | 含 `:`（metadata） | 43 |
> | 不含 `:` | **16** |
> | 其中 `kind=value` | **13** |
> | 其中 `kind=document` | 3 |
> | 至少含一個不含 `:` token 之 FR 列 | **35** |
> | 含 `[value]`（扣除後）之列數 | **33** |
>
> **「44」撤回。** 該數字並非擷取有誤，而是**聚合有誤**：上輪把 token
> 以逗號串進 TSV 欄再以逗號切回統計，而 token 本身可含逗號
> （`[Radio:R1M, VP5R120, R1H]`），切碎後去重才得 44。擷取無論正規化
> 與否皆為 59（已複驗）。TSV 之分隔符已改為 ` ¦ `。
>
> 三種舊定義（9／13／44）**全部丟棄 `[current non-zero value]`**
> （出現 8 次，為 `$RQ_DISP_INTS$` 之值）。依 canon §8.4.1，來源模糊即
> 保留模糊；丟掉它，TC 寫到該處就會有人去填一個來源未載之具體數字。
>
> `values_narrow_REPEALED` 欄依 R-TM13 保留供稽核，**其定義已廢止，
> 不得作為值域來源**。

`candidate_leaf`（**候選，非裁定**；依 R-DM12 引用時須連同 `anchor_kind`）：

| leaf | 候選列數 |
|---|---|
| SWE-DM-004（Thermal Management） | 4（r31–r34） |
| SWE-DM-005（Thermal Protection Management） | 4（r31–r34） |
| 其餘六個 leaf | 0 |
| 有候選之列 / 無候選之列 | 4 / 76 |

r31–r34 之候選依據為 heading 錨逐字含 leaf 片語 `'Hot Algorithm'`；該片語
同時出現於 004 與 005 之 Requirement Title，故兩者並列為候選，不擇一。

### 仍站得住之覆蓋陳述

**只有一句**：以 id 為據之對應為 **0 列**（A-DM2，逐字比對）。
「58 列無對應」已撤回；「76 列無候選」為錨定法之輸出，其意義是
**「無逐字錨可連到 leaf」**，不等於「不屬於本 feature 範圍」。

### 錨定法本身之兩項限制（本輪實測，須併同引用）

1. **heading 錨在 r72 退化。** SYS2 之 45 個 Heading 中，`r72
   2.2 Serializer Touch Interrupt PIN Definition` 一個節點底下掛了 231 列，
   其中 **48 列為 FR —— 佔母體 80 列之 60%**。該 heading 之文字與顯示行為
   無關，故對這 48 列而言 heading 錨存在但無鑑別力。
   （另：r62 為 `2.3 LVDS Interface`、r72 為 `2.2 …`，編號逆序，該匯出之
   Heading 層級疑似已被壓平。）
2. **RVC 之縮寫不逐字。** 037 用 `Display RVC Handling`／`RVC Management`
   （`SWE-DM-007`／`008`），SYS2 之 heading 用 `Rear Camera Events`／
   `Rear Camera Interrupts`。`RVC` → `Rear View Camera` 之展開**不是逐字
   比對**，依下放包 03 §七第 10 條不得作為錨，故二 leaf 之候選為 0。
   **這是方法之界線，不是「SYS2 無 RVC 需求」之發現** —— 兩者不可混同。

- 提案處置：本表為 R-DM7 所要求之揭露。範圍之裁定屬 Tier 2（Q2），
  依下放包 03 §4.2 **於本條之限制 1、2 有處置前不提交裁定**

## A-DM12 — 036 母本 B 欄為公式欄，前輪完全未報告  [PENDING]

036 母本 `Test Case Specification 測試用例規範` 分頁之 B 欄（`No.#\n序號`）
為公式欄。本輪以 `data_only=False` 實測 B10–B1411：

- **1402/1402 逐列符合 `=IF(ISBLANK($D{row}),"",ROW()-9)`**，$D 之列號逐列
  遞增且與所在列一致，不符 0 列
- B 欄為該分頁資料列中**唯一**含公式之欄（全 34 欄逐格掃描）
- `data_only=True` 讀 B10 得快取值 `1`，B11 起為 `None` —— 即快取為
  **陳舊值**：D10 目前為空，公式應回傳 `""`，快取卻仍存 `1`

上繳包 02 全文未提及 B 欄之存在與其公式。`workbook_state` 判 `BLANK`
不受影響（canon §2 step 1 之判準為 Test Item／TC ID，非 B 欄），但寫回時
若對 B 欄賦值，將摧毀 1402 列之公式，序號改為死值。

- 證據：本輪之 `data_only=False` 全欄掃描
- 提案處置：依 **R-DM15**，寫回一律不觸碰 B 欄；`feature.yaml` 已補註。
  另註：因快取陳舊，任何以 `data_only=True` 讀 B 欄判斷「該列是否已填」
  之實作會誤判 r10

## A-DM13 — CFTS_020 引用 8 份外部 CFTS 文件，一份未在手上  [PENDING]

判讀基準 CFTS_020 之本文以 `{CFTSnnn-mmm}` 形式引用外部條號。本輪全文
清點：相異外部文件 **8 份**（`CFTS004`／`009`／`010`／`013`／`019`／
`022`／`033`／`044`；另有指向自身之 `CFTS020-*`）。引用次數較高者：
`CFTS019-723`×12、`CFTS009-722`×9、`CFTS033-2111`×7、`CFTS013-629`×6、
`CFTS013-633`×5、`CFTS013-967`×5、`CFTS044-656`×5、`CFTS013-952`×4。

其中兩份已知直接擋住 R-DM8 之缺值：`CFTS009-722`（Splash/Disclaimer
時段，DR-DM1）與 `CFTS013-629`／`-633`／`-952`（Display Hot 演算法本體，
DR-DM4）。其餘六份之影響本輪**未逐一評估**。

- 證據：`scripts/hot_behaviour_join.py` 之併讀輸出；CFTS_020 本文全文
  regex 清點
- 影響：spec_mode D 之判讀基準本身是一份會外指的文件；BLOCKED 之預估
  不能只看手上四份
- 提案處置：登記；DR-DM4 開立。其餘六份之影響待 Phase 2 逐一評估

## A-DM18 — 037 八條描述皆無具體值、無訊號、無外部引用；且八條皆為併句  [PENDING]

037 八條 `Requirement Description` 全文逐條精讀（`scripts/read_037_leaves.py`，
連續四輪積欠，本輪清償）之結構性實測：

| 項 | 八條之實測 |
|---|---|
| 數值＋單位（門檻之形態） | **0 / 8**（逐條皆 0 處） |
| `$Signal$` token | **0 / 8** |
| 外部文件／id 引用（`{CFTSnnn-mmm}` 等） | **0 / 8** |
| 句號後缺空格之併句（`x.Y`） | **8 / 8**（每條恰 1 處） |

三項後果：

1. **R-DM8 原只列四處缺值（003/004/005/006），實際為八條全無具體值。**
   001／002／007／008 之描述同樣只有抽象語句（如「manage display
   operative states as DISPLAY_ON and DISPLAY_OFF based on system
   operational requests and **timeout conditions**」—— timeout 之值未載）。
2. **R-DM14／R-DM17 之「037 不含訊號層資訊」得到全稱之證實**：
   八條之 `$Signal$` token 皆為 0，非僅抽樣。
3. **八條皆為兩句併寫**（如 `...timeout conditions.The software shall...`），
   任何以句號斷句之實作會把兩句併為一句。八條之第二句多為「回復／
   還原」語意（restore／resume／ensure），併句會使該語意附著於第一句之
   條件之下。

另記一項命名落差：037 用 `DISPLAY_ON`／`DISPLAY_OFF`（001、002 兩條），
而 SYS2 與 DBC 側為 `DISP_ON`／`DISP_OFF`。**逐字不等**，且不屬 R-DM22
之縮寫並列形態（無 `(...)` 並列可引），故 glossary 無法建條目。

- 證據：`scripts/read_037_leaves.py` 之八條全文輸出
- 提案處置：登記。R-DM8 之缺值清單是否自四處擴為八條，屬 Tier 2；
  `DISPLAY_ON` ↔ `DISP_ON` 之對應同樣不得由執行層推定

## A-DM19 — glossary 錨解開 SYS2 側，但解不開 PROXI 側（阻塞點不同）  [PENDING]

R-DM22 之縮寫錨在兩處之效果**相反**：

| 標的 | 錨施用前 | 錨施用後 |
|---|---|---|
| SYS2 覆蓋對照（80 列 FR 母體） | `SWE-DM-007`／`008` 候選各 **0** | 各 **12**（r37/41/42/44/45/52/53/54/213/217/219/226） |
| PROXI 對照（446 列） | `related_leaf` 全空 | **仍全空**（`glossary_phrase` 0 命中） |

成因：SYS2 之 `Description` 逐字寫 `Rear View Camera`（空格），
展開後相符；而 LID／PROXI 寫 **`Rear_View_Camera`（底線）**，
逐字檢查該分頁：`Rear View Camera` 0 次、`Rear_View_Camera` 2 次。

依 **R-DM22(c)**「展開後仍不逐字相符者，即為不相符，不得再放寬一層」，
執行層**未**加入底線↔空格之正規化。

- 影響：PROXI 之 leaf 對應仍為 0，`DCSD_cfg`／`RVC_SK_PRSNT` 雖已查得其
  PROXI 列與值域，卻仍接不到任何 leaf
- 提案處置：請裁示是否另立一條「分隔符正規化」之錨（底線／連字號／
  空格互換）。該正規化與縮寫表同屬**封閉且可稽核**之逐字規則，
  非相似度；但其開放與否屬 Tier 2，執行層不自行採用

## A-DM20 — PROXI `Checked by NODE(CHECK)` 欄近乎全空；`Used by NODE` 可用但缺專案 VF 之鍵  [PENDING]

上繳 05 §9 第 4 項自陳未用之兩欄，本輪實測（母體 1,058 個參數列）：

| 欄 | 非空 | 相異值 | 形態 |
|---|---|---|---|
| `Used by NODE(VFXXX)` | **500 / 1058** | 311 | `BSM (VF381_V1); TBM (VF684_V3);` —— 節點名 + 括號內之 VF 清單，分號分隔 |
| `Checked by NODE(CHECK)` | **6 / 1058** | 4 | `All nodes (1,4)`／`IPC(2), BCM(2)`／`DMSM (6)` |

判定：

- **`Checked by NODE(CHECK)` 不可用** —— 6/1058 之覆蓋率下，其空值不帶
  任何資訊（R-G13 之涵蓋範圍要件反面）。
- **`Used by NODE(VFXXX)` 結構上可用，但缺一把鑰匙**：要判「某參數是否
  適用於本專案」，須先知道**本專案是哪一個 VF**。該資訊不在四份素材內。

本 feature 三個已查得之 PROXI 列，其 `Used by`：

| PROXI 列 | 參數 | Used by NODE(VFXXX) |
|---|---|---|
| r37 | `CAN node 31 (DCSD)` | `TBM (VF684_V3); ECC (VF123_V1, VF727_V3, VF727_V1); LTM (VF169_V2, VF727_V3); ETM (VF169_V3, VF727_V3, VF727_V1);` |
| r401 | `Rear_View_Camera` | `ETM (VF230_V1, VF551_V3, VF551_V4, VF169_V3, VF617_V6, VF561_V3); LTM (...)` |
| r494 | `Rear_View_Camera_Soft_Button` | `LTM (VF664_V2); ETM (VF664_V3);` |

三列皆含 **`ETM`** —— 而 `ETM` 正是 BHCAN2 中本 feature 三個顯示訊號之
發送節點（A-DM14）。此為**觀察**，不是「本專案為 ETM 架構」之認定。

> 另記：r401 之清單含 `VF230_V1`，而 `features/vehicle_setting/` 之產出
> 檔名為 `_vf230_*`。**執行層不推定 VF230 即本專案之 VF** —— 那是跨
> feature 之推定，且 vehicle_setting 之 VF 未必等於 Display 之 VF。

- 提案處置：開 `DR-DM7` 索本專案之 VF 代碼（或其 PROXI 實例檔）。
  取得後 `Used by NODE(VFXXX)` 即可用於篩選，本輪之 446 列母體可望大幅收斂

## A-DM21 — `"Analysis Report"` 寫死於 5 處；Q5-B 只解到其中 1 處  [PENDING]

Q5 定案 B（R-DM24）之目的為使 `recon.py` 可跑。本輪實作覆寫機制並完成
回歸後實測：**目的未達成**，且成因已定位。

`"Analysis Report"` 這個分頁名在共用腳本中**寫死於 5 處**：

| 位置 | 用途 | Q5-B 是否觸及 |
|---|---|---|
| `scripts/intake.py:63` | `SHEET_SIGNATURES` 之判準 | **是**（由覆寫繞過） |
| `scripts/intake.py:114` | `_swra_profile()` 讀分頁 | 否 |
| `scripts/intake.py:311` | `cited_documents()` 讀分頁 | 否 |
| `scripts/recon.py:568` | `survey_a03()` 讀分頁 | 否 |
| `scripts/compare_req_families.py:41` | `SHEET` 常數 | 否 |

實測二事：

1. **依 R-DM24 之條文所載 `kind: a03_report`**：覆寫生效、
   `kind_source: override` 正確標記，但下游邏輯完全未被驅動 ——
   need list 仍輸出 `NO requirement report found`。原因是
   `a03_report` 是 `feature.yaml` 之 paths 鍵，而 `intake.py` 之 kind
   詞彙為 `swra_report`（`KIND_TO_YAML` 將後者映至前者）。
2. **若改為 `kind: swra_report`**（即真正能驅動下游者）：
   `intake.py` **當場崩潰**於 `cited_documents()` 之
   `wb["Analysis Report"]`（`intake.py:311`），與 `recon.py:568` 同型。

即：**繞過分類器之後，緊接著就撞上同一個假設的第二個實例。**

`recon.py --feature features/display` 本輪重跑，仍失敗於
`recon.py:568` `KeyError: 'Worksheet Analysis Report does not exist.'`，
與上繳 02 之失敗點逐字相同。依 R-DM24 末段未修 `recon.py`。

- 本輪保留條文所載之 `kind: a03_report`（不崩潰、標記正確），
  **未自行改為 `swra_report`** —— 那會改變條文所指定之值
- 提案處置：Q5 之選項 B 需要擴充其授權範圍（及於 `cited_documents()`
  與 `survey_a03()` 之分頁名來源），或改採另一形態。**屬 Tier 2，
  執行層不裁定。** 本輪之覆寫機制本身完好且已回歸驗證，可保留

## A-DM22 — `anchor_kind` 無論優先序如何都無法顯示候選之來源  [PENDING]

R-DM26 將 heading 由第三位降至倒數第二，理由是其 80/80 之存在性會遮蔽
其下所有錨。調整後實測：**`glossary_phrase` 仍為 0**。

成因已量明：**16 個產生候選之列（heading 錨 4 列 + glossary 錨 12 列）
全部同時含 `$signal$`**，而 `signal` 在新舊優先序中皆居首。

| 產生候選之錨 | 列 | 其 `anchor_kind` |
|---|---|---|
| heading | r31–r34 | signal ×4 |
| glossary | r37/41/42/44/45/52/53/54/213/217/219/226 | signal ×12 |

故 `anchor_kind` 分布在 R-DM26 前後皆為 `signal 43 / heading 37`。

**這不是優先序放錯位置，是兩欄在回答不同的問題**：
`anchor_kind` 答「這列帶有哪些證據」，`candidate_from` 答「是什麼把它
連到 leaf」。一個欄位無法同時承載兩者。

- R-DM26 之調整仍應保留：heading 之 100% 存在性確實不宜居高位，
  且該調整使 `melco` 得以在 heading 之前現身（本輪母體中 melco 僅 1 列
  且該列亦為 signal，故未顯現）
- 提案處置：引用時一律以 **`candidate_from`** 為準（R-DM12／R-DM26 已
  規定兩欄並列不合併）。是否要在 `anchor_kind` 之外再立一欄
  「最高優先之**產生候選**之錨」，屬 Tier 2

## A-DM23 — TSV 檔頭之 `#` 註解行使標準 `csv.DictReader` 讀不到表頭  [PENDING]

R-DM25(d) 要求正規化之定義逐字寫入產出檔之檔頭，我於上輪以 `#` 起首之
註解行實作。本輪讀回 `data/proxi_candidates.tsv` 時，
`csv.DictReader` **把第一行註解當成表頭**，得到 0 筆可用資料
（欄名變成 `# R-DM25 正規化之定義：…`）。

- 影響：`features/display/data/` 下唯一帶註解行者為
  `proxi_candidates.tsv`（3 行）；另 `coverage_sys2_vs_swe_dm.PRE_GLOSSARY.tsv`／
  `.PRE_PRIORITY.tsv`／`coverage_sys2_vs_swe_dm.RETRACTED.tsv`／
  `leaf_value_gaps.tsv` 亦各有註解行。現行之讀取者（本 feature 之腳本）
  皆自行處理，但**任何以預設方式讀 TSV 之消費者會靜默取到錯誤欄名**
- 這與 R-G16 同型：**擷取正確、序列化正確，讀回那一步錯**，
  且錯得「看起來像空資料」而非報錯
- 提案處置二選一，屬 Tier 2：
  (a) 註解行保留，於 `FORMS.md` 或 canon 明定「本專案之 TSV 得以 `#`
      起首之註解行開頭，讀取者須略過」，並在每個讀取點落實；
  (b) 註解移出資料檔，改置於同名 `.meta.md`，資料檔只有表頭與資料。
  **執行層不自行擇一** —— 這會影響此後所有 feature 之 TSV 慣例

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-DMnn]`.
