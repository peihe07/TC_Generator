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

## A-DM24 — 排程提案初版有索引錯位與不成立之互斥宣稱  [RESOLVED，2026-08-25]

`docs/proxi_triage_proposal.md` 初版（下放包 08 §5）之三梯次表兩處錯：

1. **索引錯位**：以 `{i+1: g[i-1][ui]}` 建 PROXI 列號對照，把每一列之
   `Used by NODE(VFXXX)` 接到下一列。`ETM` 之列數因此報 **50**，
   正確索引（`{i: g[i-1][ui]}`）之實測為 **100**。
2. **「互斥且窮盡：69 + 117 + 269 = 446」不成立** —— 三數相加為 **455**。
   第一梯次之 keyword 條件會納入無 PROXI 定義之列，而那些列同時被算進
   第三梯次。**梯次自始不互斥，而我在表下斷言它互斥。**

更正後之互斥分割（`lid_row` 唯一性已驗，四類相加 = 446）：
A 有定義且（ETM ∪ keyword）**107**／B 有定義且皆否 **70**／
C 無定義但 keyword **9**／D 無定義且無 keyword **260**。

- 這是本 feature **第六次**同型缺陷：擷取正確，其後之索引／聚合／
  算術出錯，且輸出「看起來合理」。前五次見 R-G16 與 R-G20 之實例
- **本條與前五次之差別在於：這一次錯的是一個我親手打在表下的斷言**
  （「互斥且窮盡」），而那句話沒有任何程式在檢查它。
  算式之驗證（相加是否等於母體）現已寫入更正後之表
- 提案處置：凡於報告中出現「互斥」「窮盡」「合計」之斷言者，
  其算式須由腳本輸出而非人工斷言（R-G20 之延伸）。屬 Tier 2

## A-DM25 — 四個 feature 之 `RECON.md` 與現況不同步  [PENDING]

選項 D 之回歸須對現有全部 feature 跑 `recon.py`。**改動前**之基準執行
即已改寫下列既有檔（即：它們與其輸入之現況不同步，與本輪改動無關）：

`features/comfort/RECON.md`、`features/privacy/RECON.md`、
`features/vehicle_setting/RECON.md`

另 `comfort`／`privacy` 之 `data/recon_leaf_to_section.tsv` 為本次執行
新產生（原本不存在）。

- 本輪已全數 `git checkout --` 還原，新產生者刪除，
  **未代任何其他 feature 修改或提交**
- 影響：任何以既有 `RECON.md` 為據之陳述，其時效未經確認
- 提案處置：登記。是否重跑並更新該三個 feature 之 `RECON.md`，
  屬各該 feature 之事，不在本 feature 範圍

## A-DM26 — `paths.spec_pdf` 指向 `.docx`；欄名與內容不符  [PENDING]

`feature.yaml` 之欄位名為 `paths.spec_pdf`，而本 feature 之該欄指向
`R1LR_…CFTS_020 ICS and DCSD _20260310-1533.docx` —— **一份 Word 檔，
不是 PDF**。`recon.py` 之 `survey_spec_text_layer()` 其 docstring 亦以
PDF 為前提（其探針依序試 pymupdf 與 `pdftotext`）。

實際上探針對 `.docx` 可用（pymupdf 讀得 854,333 字元），故**功能無誤**，
誤導的是名稱。

- **不改欄名**（會動到所有 feature 之 `feature.yaml` 與所有讀取者）
- 引用該欄時須知其內容未必為 PDF
- 連帶記明字元數之兩個值：pymupdf **854,333**（登記值）／
  python-docx **907,382**（自測，保留）。兩者皆遠超「有無文字層」之
  500 字元門檻，**導出之結論相同**（spec_mode D 成立）。
  全表見 `data/spec_text_layer.tsv`
- 提案處置：登記。欄名之修正屬全域 Tier 2

## A-DM27 — `DECISIONS.new.md` 只呈現 recon 所測之一部分  [PENDING]

下放包 12 步驟 3 之反向比對（合併檔有而 recon 無者）實測 17 項，
逐項判其性質後：

| 判定 | 項數 | 例 |
|---|---|---|
| **recon 有測，只是未列入 `DECISIONS.new.md`** | **10** | `feature.yaml` column conflicts／Categorization 欄與分布／Covered by done region／Parent-child dupes／Authors present／Header row index／Regen-region segments／Draft-region disposition／Missing referenced specs／Priority rubric deviations |
| 自測獨有（recon 不涉及此概念） | 7 | Spec release/version pinned／SYS2 覆蓋落差／Granularity precedent／Known scope carve-outs／Contested attributions／Model assignment／BLOCKED batches |
| **recon 漏測** | **0** | —— |

**停止條件 30 未觸發**：無任何一項為 recon 漏測。

> **更正（2026-08-25，下放包 13 步驟 3，見 A-DM29）**：上表之
> 「10 / 7」係以子字串比對所得，其中兩項映射不成立。更正後為
> **8 項 recon 有測且量同一件事 / 1 項量不同的東西
> （`Missing referenced specs`）/ 8 項自測獨有（含 `Header row index`）**。
> 「停止條件 30 未觸發」之結論不變，但其依據中有兩項是錯的映射。

惟前一類值得登記：那 10 項在 `recon.json` 與／或 `RECON.md` 中**都有**，
只是 `DECISIONS.new.md` 之模板不列它們。即：

> **`DECISIONS.new.md` 不是 recon 之全部量測，是其一個子集。**
> 以它為「管線說了什麼」之唯一依據，會漏掉十項管線確實測過的事實。

- 影響：任何以 `DECISIONS.new.md` 為準之對照（含上輪之合併）都會少這 10 項
- 提案處置：登記。是否擴充 `recon.py` 之 DECISIONS 模板屬全域 Tier 2，
  不在本 feature 可處置之範圍。本 feature 之對照此後一律**兼看
  `RECON.md` 與 `recon.json`**，不以 `DECISIONS.new.md` 為唯一依據

## A-DM28 — 我的漂移警示曾與其自身行為相反（已於本輪修正）  [RESOLVED]

步驟 7 首版實作：偵測到 `spec_text_layer` 之字元數與 sidecar 所記不符時
印出警示「NOT updating the expectation」，**但同一次執行之 `write_meta`
仍以實測值重寫 `expected_chars`** —— 訊息說不採納，程式卻採納了。

實測發現方式：蓄意將期望值改為 `999999` 後連跑兩次，第二次警示消失。

已修正為 `{**現算, **既有}`：既有鍵保留 sidecar 所記，只有從未見過之
抽取器才新增。修正後連跑兩次，**警示兩次皆出現、期望值維持 999999**。

- 這是本 feature 第七次同型缺陷，但形態是新的：**前六次是數字錯，
  這次是「宣稱之行為」與「實際之行為」不一致**。一個會說謊的警示
  比沒有警示更糟 —— 它讓人以為有守衛
- 一般化提案（Tier 2）：凡輸出中含「不會做 X」之宣稱者，
  其測試須含「連跑兩次，第二次仍應出現同一訊息」

## A-DM29 — 上輪之反向比對有兩處映射瑕疵（本輪自查）  [RESOLVED]

R-DM39 要求對 A-DM27 之 10 項逐項比對值。比對時發現**其中兩項之映射
本身不成立**：

| 項 | 上輪之判定 | 本輪查明 |
|---|---|---|
| `Header row index` | 「recon 有測」 | **偽陽性**。我以子字串 `"header"` 掃 `RECON.md`，命中的是 `column mapping: 15 fields resolved from **header** text`。以確切詞組 `"header row"` 重掃為 **0 命中** —— recon **不報**表頭列號 |
| `Missing referenced specs` | 「recon 有測」 | **量的是不同的東西**。recon 之 `outline_misses` = 「leaf 所引之 outline 章節不在受裁匯出中者」；我的 = 「CFTS_020 本文以 `{CFTSnnn-mmm}` 引用之外部文件」。兩者皆存在，但不是同一個量 |

故 A-DM27 之「10 項 recon 有測 / 7 項自測獨有」應更正為
**8 項 recon 有測且量同一件事 / 1 項量不同的東西 / 8 項自測獨有**。

- 成因：上輪之分類以**子字串比對**判斷「recon 有沒有測這個」，
  而子字串會在無關的句子裡命中。與 R-DM13 所禁之 bag-of-words
  同型 —— 我在判斷「兩個概念是不是同一個」時用了非逐字之方法
- **這也使上輪「停止條件 30 未觸發」之結論須重述**：結論仍成立
  （無 recon 漏測），但其依據中有兩項是錯的映射而非正確的判定
- 提案處置：凡判斷「兩份產出是否在講同一件事」者，
  須以確切詞組或欄位鍵比對，不得以子字串。屬本 feature 之實作準則

## A-DM30 — 四個 `reference:` 鍵曾靜默落入 `lint:` 之下  [RESOLVED]

依 R-DM38 將 `inputs/` 四份加入 `feature.yaml` 之 `reference:` 節時，
插入點錯置於檔案末段，四個鍵成了 **`lint:` 之子鍵**。

**YAML 解析無誤、無任何警告**，而 `verify_reference_binding.py` 照常
輸出 **`5 of 5 match.`** —— 一個通過的檢查，檢查的卻不是我以為的東西。

發現方式：以 `yaml.safe_load` 印出 `reference` 與 `lint` 之鍵清單，
見四個鍵在 `lint` 之下。修正後為 **9/9 match**。

- 這與 A-DM28 同一族：**輸出看起來正確**。差別在 A-DM28 是訊息說謊，
  本條是**檢查對象錯了而結果仍是綠的**
- 提案處置：`verify_reference_binding.py` 之輸出已印 `entries: N`；
  本輪之 5 與 9 之差即在該行。**該行是唯一能察覺此錯的線索**，
  應於引用其結果時一併引用，不得只引「N of N match」

## A-DM31 — DR-DM3 所指之 CFTS043 SYSRA 內容為 HVAC，不答本 DR  [PENDING]

`features/display/inputs/SYS2_CFTS043_FM-WI-FSM-035-A02 …SYSRA_CFTS043_V01.xlsx`
係為答 DR-DM3（`SYS-RA-DISP-*` ↔ SYS2 之對應）而指定，**實測不含
Display 之任何 id**。

執行層獨立複驗（未照抄下放包，`openpyxl` 唯讀、三分頁全格掃描）：

| 項 | 實測 |
|---|---|
| 分頁 | `Basic Report`／`Polarion`／`_polarion` |
| 資料列 | **406** |
| `SYS2 Sys-RA-Feature-ID` 為 `SYS-RA-HVAC-{n}` | **405**（另 1 列空） |
| 全檔逐字 `SYS-RA-DISP` | **0** |
| 全檔逐字 `SYS-DISP` | **0** |
| 全檔逐字 `SWE-DM` / `SWE1-DM` | **0 / 0** |
| sha256（前 16 碼） | `1c0b2abf659f4911…` |

> **一處與下放包 15 §2.3 不符**：`Display` 一字之出現次數，
> 下放包記 **477**，本輪實測 **480**。差異為掃描範圍 ——
> 我掃三個分頁之全部儲存格，下放包疑似只掃 `Basic Report`。
> **兩數皆非結論所依**（結論所依為 id 命名空間之 0 命中，該項逐字相符），
> 故不觸發停止條件；記此以免日後被當成同一個量引用。

**該檔為 CFTS_043（HVAC）之技術安全需求分析報告。** `Display` 一字雖
出現數百次，**全部在 Description 之散文中**，與 id 命名空間無關。

處置（依 15 包 §四步驟 4）：
- **不納入 `paths:`／`reference:`／素材台帳，不自其取任何值**
- **DR-DM3 維持 OPEN**，其 `Status` 欄加註本次指定與其實測結果
- 該檔現位於 `features/display/inputs/` 而**不在任何綁定內** ——
  這是本 feature 目前唯一一份「在 inputs/ 卻不受 R-DM38 綁定」之檔，
  其理由正是「不得自其取值」。此例外須隨 A-DM31 一併引用

> 這是本 feature 第二次「檔名看起來對而內容不是」——第一次是 02 輪之
> 037 檔名連字號（R-DM11）。差別在於**這次檔名確實是一份真實存在且
> 相關領域的文件**，只是 CFTS 號不同。若不逐字驗 id 命名空間就收下，
> DR-DM3 會被錯誤結案，而追溯鏈仍然是斷的。

> **敘述修正（下放包 24 §一，2026-08-25）**：`SYS2_CFTSnnn_*` 為
> **SYSRA 分析報告（`FM-WI-FSM-035-A02`）之命名慣例**，
> **`SYS2_` 前綴不應被讀為「SYS2 匯出」**。本檔之表單編號逐字為
> `FM-WI-FSM-035-A02`（見檔名），與 SYS2 匯出（`…_ICS_…All_HW_System_
> Accepted & Released.xlsx`）分屬兩種文件。
>
> **原判定不變**：本檔內容為 HVAC、不答 DR-DM3。上表之實測數字全部維持。
>
> **本層之限定**：修正之依據為下放包 24 對**另一份** CFTS013 檔案之
> 量測（該檔未落磁碟，見上繳 25 §五），本層無法重算其表單編號。
> 惟本項所修正者為**命名慣例之讀法**，而 `FM-WI-FSM-035-A02` 一詞
> **逐字見於本 feature 已持有之 CFTS043 檔名**（`inputs/` 內，
> 綁定外），該處可自證。故採認。

## A-DM32 — 規格側之 `[DISP_OFF]`／`[DISP_ON]` 在 DBC 與 LID 皆不存在  [PENDING]

`DCSD_DISP_STAT` 之值域，兩個權威逐字一致：

| 來源 | 值域 |
|---|---|
| DBC `VAL_`（`PDT27_E2A_R1_BHCAN2.dbc`，`BO_ 1445`） | `0 "OFF" 1 "ON" 2 "BLANK" 3 "RR_CMRA" 4 "DISP_HOT" 7 "SNA"` |
| LID `CAN Mapping` r420 `Format`（Atlantis High） | `0 = OFF 1 = ON 2 = BLANK 3 = RR_CMRA 4 = DISP_HOT 7 = SNA` |

而規格側（CFTS `{4820287}`／`{4820288}`／`{4820289}`／`{4820290}`、
SYS2 r31–r34）逐字寫 `$DCSD_DISP_STAT$=[DISP_OFF]`／`=[DISP_ON]`。

| 標籤 | DBC | LID | 全 DBC 逐字掃描 |
|---|---|---|---|
| `DISP_HOT` | **有**（raw 4） | **有** | BHCAN2 3 次、BHCAN-R4 1 次 |
| `DISP_OFF` | 無 | 無 | **0** |
| `DISP_ON` | 無 | 無 | **0** |
| `DISP_NORMAL` | 無 | 無 | **0 行** |

**這是本 feature 第四個命名落差**，且與前三個都不同型：

| # | 落差 | 型態 | 處置 |
|---|---|---|---|
| 1 | `SWE-DM` vs `SWE1-DM` | 同一文件兩分頁 | A-DM1／R-DM42 |
| 2 | `RVC` vs `Rear View Camera` | 縮寫 | R-DM22 glossary |
| 3 | `DISPLAY_ON` vs `DISP_ON` | 037 vs SYS2/DBC 之**訊號狀態名** | R-DM43（取訊號側） |
| 4 | **`[DISP_OFF]` vs `OFF`** | **規格所引之值標籤 vs 該訊號之實際值標籤** | **本條，未裁** |

R-DM43 之裁定為「以訊號名稱為主」，而**本條之問題不是名稱而是值**：
訊號側確實有一個 raw 0，其標籤是 `OFF`；規格側寫的是 `DISP_OFF`。
把兩者對上需要一個判斷 —— **該訊號只有一個「關」語意之值，
故 `[DISP_OFF]` 幾乎必然指 raw 0** —— 但「幾乎必然」正是本專案
一貫拒絕的東西（R-DM13／停止條件 14／§8.4.1）。

- **影響**：pilot-01 之三條 TC 中，**#2（005 → 顯示關閉）與 #3
  （005 → 回復）皆須引用該對應方能寫出 Expected Result**；
  #1（004 → PU0517 ＋ `DISP_HOT`）之訊號值為 raw 4，**不受影響**
- **本輪未作該對應**，未產出任何 TC（停止條件 46）
**已裁（2026-08-25，R-DM48）**：三途皆不單獨採，改為**按可得性分寫** ——
逐字解得 DBC `VAL_` 者寫入 `= <raw> (<label>)`，解不得者**不寫入訊號值**，
ER 改驗規格所載之可觀察行為，規格側之標籤記入 `reasoning`。
查證面另開 **DR-DM9**（HIGH）；取得並列出處後依 R-DM22 建值標籤 glossary，
屆時得於既有 ER **增列**訊號值（增列不改變行為驗證，不構成回修）。

> 裁定所據之關鍵事實由本輪之實測提供：`[DISP_REAR_CAMERA]` 對
> `RR_CMRA`（raw 3）**證明不存在單純之 `DISP_` 前綴規則** ——
> 六個值裡的規則就不一致，故不可外推。

- 原提案（不裁定）：三途 ——
  (a) 立一條「規格值標籤 ↔ DBC 值標籤」之對照表，形態同 R-DM22 之
      glossary（封閉、逐條有出處、可稽核），本條之三筆即其首批；
  (b) 裁定 ER 一律寫 DBC 側之 `= 0 (OFF)`，規格側寫法只入 `reasoning`；
  (c) 向上游提 DR，請其確認 `[DISP_OFF]` 所指之 raw 值

## A-DM33 — 本架構之 Display Hot 條款有兩組互相矛盾之完整流程；第三組以 ECU 角色切分且其 DCSD 側標為 `noSys`  [PENDING]

21 包 §2.1 要求逐字查 warning 與 OFF 兩階段之區分條件。查證擴及全文後
所見如下（屬性行皆為機器抽取之逐字，見上繳 21 §1）。

### 三組條款與其適用性

| 組 | 節 | 關鍵條之屬性行（逐字） | 對本專案（`R1H`／`Atlantis High`）之適用 |
|---|---|---|---|
| A | `1.11.2.2` `{4820282}`–`{4820288}` | `{4820283}`：`[Radio:R1H, VP5R120, R1M] [EE Architecture:PowerNet, Atlantis High]` | **適用** |
| B | `1.11.2.2` `{4820289}`–`{4820292}` | `{4820289}`：`[Radio:R1H] [EE Architecture:Atlantis High]` | **適用**（且**僅**本專案） |
| C | `1.8.2.5.2` `{4819858}`／`1.15.2.5.2` `{4820947}` Multi-stage | `{4820951}`／`{4819862}`：`[ECU:DCSD] … [Radio:noSys]`；`{4820952}`：`[ECU:ETM, LTM] … [Radio:R1M, R1L-R, R1H, R1L]` | **僅 HU 側適用**；DCSD 側諸條皆 `Radio:noSys`，且 `{4820948}` 逐字為 `The Multi-stage Display Hot algorithm shall not be implemented by the DCSD supplier.` |

### 矛盾之所在（A 對 B）

| 事項 | 組 A | 組 B |
|---|---|---|
| 誰關背光 | **HU 判定後下令**：`{4820283}` HU 送 `$TGW_DISP_STAT$ = [DISP_OFF]` ＋ `$RQ_DISP_INTS$ = [0% Intensity]` → `{4820284}` DCSD 收到才關 | **DCSD 自主**：`{4820289}` 越過門檻即 `Turn off the backlight (both top and bottom portion) and disable touch` |
| 是否有警示階段 | **有**：`{4820283}` 逐字 `When the HU has finished displaying the Display Hot warning screen …` | **無**：`{4820289}` 之四項動作中不含任何警示畫面 |
| 關背光後之 `$DCSD_DISP_STAT$` | `{4820284}`：`shall continue to send $DCSD_DISP_STAT$ = [DISP_HOT]` | `{4820289}`：`Send CAN signal $DCSD_DISP_STAT$=[DISP_OFF]` |

**兩組對同一觸發（越過 85 degrees C）給出互相排斥之後續。**
兩組皆逐字宣告適用於 `R1H` ＋ `Atlantis High`。

### 阻斷 pilot-01 原 #2 之直接原因

原 #2（保護性關閉）之觸發條件與 #1 相同（`> 85`）而結果不同。要能寫出
可執行之步驟，須有「何時看到警示、何時看到關閉」之可觀測準據。查證結果：

1. 走組 A：該準據為 `{4820283}` 之 `has finished displaying the Display Hot
   warning screen and determines that the DCSD display should now be 'Turned Off'`
   —— **該條未給任何時長、門檻或可觀測事件**
2. 走組 B：`{4820289}` 為一無序號時序之動作清單，**未給任一步之時間關係**
3. 走組 C：其 DCSD 側之判定條逐字為
   `When the DCSD determines it wants to turn off it's backlighting
   (see {CFTS013-XXX}), the DCSD shall send $DCSD_DISP_STAT$ = [DISP_OFF].`
   —— 準據指向 **`{CFTS013-XXX}`，規格自身之未填佔位符**；且該條為 `Radio:noSys`
4. 走 Pop Up List：`PU0517` 與 `PU0130` 之 `Timeout` 皆為 `10`，`PU0130` 之
   說明逐字為 `if the screen has not cooled down the display will turn off
   until it has cooled` —— **「未冷卻」之判準與其觀測時點未給**

**四條路徑皆不產生可觀測之區分準據。** 依 21 包 §2.1 分支 3、停止條件 53：
**原 #2 deferred，不以推定之時間值補寫**。

### 未填佔位符（次要發現，仍登記）

`{CFTS013-XXX}` 於本文出現 **5 次**（另有 `{CFTS013-XXXX}` 之 FPDM 版 1 次），
皆為同一句型。其為**已發行規格中的未填欄**，非本 feature 之取材問題。
另 `{4820949}`／`{4819860}` 指向 `{CFTS013-967}`，與 DR-DM4 所列之
`-629`／`-633`／`-952` **皆不同號**。

### 處置

- **原 #2 deferred**；`PU0130` 隨之 deferred
- **DR-DM10 開立**（HIGH）：求 (a) 組 A 與組 B 何者為本架構之準，
  (b) `{4820283}` 之警示階段時長／終止準據，(c) `{CFTS013-XXX}` 之實際條號。
  與 DR-DM4 不併 —— DR-DM4 求既有三個條號之內容，
  **一個尚未編號的條款與一項條款衝突之裁定不在其範圍內**
- 組 A 與組 B 之矛盾**不由本層裁定何者優先**（Tier 2，屬上游文件之內部矛盾）
- 本輪之 TC **只取兩組皆一致之部分**：門檻值（`{4820289}` 之 `> 85` /
  `<= 85`）、`[DISP_HOT]` 之通知（`{4820282}`）、回復行為
  （`{4820287}`／`{4820288}`／`{4820290}`，兩組對回復側無分歧）

> 這是本 feature 第二次「查得比預期多」而改變處置：第一次是 06 輪之
> `_polarion`（四輪未看之分頁其實是值字典）。**兩次都是把搜尋面
> 從指定的一節擴到全文才看見的。**
>
> **本節之初稿曾寫「三組皆適用且互不一致」。** 逐條讀屬性行後改正：
> 組 C 之 DCSD 側為 `Radio:noSys` 且該節自載「不由 DCSD 供應商實作」，
> 故其不構成第三組適用流程。**改正之後結論不變（#2 仍 deferred），
> 但理由改變** —— 阻斷者主要是組 A／B 之矛盾與 `{4820283}` 之無時長，
> 而非 `{CFTS013-XXX}`。依 R-G19，理由與結論分別查證，故分別更正。

---

## A-DM34 — `DISP_HOT` 標籤在不同訊號上是不同 raw 值  [LOW]

22 包步驟 5(b) 之重跑（`dbc_probe.py`，exit 0）所見：

| 訊號 | 訊息 | `VAL_` 中 `DISP_HOT` 之 raw |
|---|---|---|
| `DCSD_DISP_STAT` | `BO_ 1445 DIS_CENTERSTACK`（BHCAN2-R1／BHCAN-R4） | **4** |
| `FPDM_DISP_STAT` | `BO_ 1513 FPDM1` | **3** |
| `TGW_FPDM_DISP_STATSts` | `BO_ 1282 RADIO_B2` | **3** |

FPDM 側之列舉為 `0 "OFF" 1 "ON" 2 "BLANK" 3 "DISP_HOT" 7 "SNA"`，
**少了 DCSD 側的 `3 "RR_CMRA"`**，其後之值遂整體前移一位。

### 為何未污染本批

`signal_resolution.py` 之選定判準為 **`MESSAGE.Signal` 兩半皆相等**
（04 輪之修正，原為「第一個含該訊號名之 DBC」）。若仍用原判準，
此處極可能取到 FPDM 側而寫出 `3 (DISP_HOT)`。

### 意義

**這是 R-DM48「不可外推」之第二個實證。** R-DM48 原以「同一訊號之六個
值裡規則就不一致」立論（`[DISP_REAR_CAMERA]` 對 `RR_CMRA`）；本項更強：
**同一標籤跨訊號亦不一致**。即：值標籤在本專案之 DBC 中**不是全域名稱**，
必須連同訊號一起解析。

### 處置

- **不阻塞**：本批未用到 FPDM 側任何值（004／005 之標的為 DCSD）
- 記入 B 類（上繳 22 §七 B7）
- 若日後有 TC 觸及 FPDM 側（`SWE-DM-001`／`002` 之部分面向可能觸及），
  **須逐訊號重解，不得沿用 004 之 `4 (DISP_HOT)`**

---

## A-DM35 — DR-DM9 之前提有誤：其四個標籤中三個不是 `DCSD_DISP_STAT` 的值  [HIGH]

007／008 之素材勘查（Pei 2026-08-25 指示「走 007／008」）所見。
機器抽取式：對 CFTS_020 全文取 `\$([A-Za-z0-9_]+)\$\s*=\s*\[([^\]]+)\]`
之全部配對，與 `dbc_probe.py` 之 `VAL_` 實測比對。

### DR-DM9 之原文與實測之落差

DR-DM9 問：「`[DISP_OFF]`／`[DISP_ON]`／`[DISP_NORMAL]`／`[DISP_REAR_CAMERA]`
各對應 **`DCSD_DISP_STAT`** 之哪一個 raw 值」。

實測：規格側之 `$DCSD_DISP_STAT$ = [...]` 配對只有
`OFF`／`ON`／`BLANK`／`RR_CMRA`／`DISP_HOT`／`SNA`／`DISP_OFF`／`DISP_ON`。
**`[DISP_NORMAL]` 與 `[DISP_REAR_CAMERA]` 從未出現在 `$DCSD_DISP_STAT$` 上**
—— 兩者是 **`$TGW_DISP_STAT$`（HU 側）** 的值。

即：**DR-DM9 把 HU 側的兩個標籤問到了 DCSD 側的訊號上。**

### 更重要的：`DCSD_DISP_STAT` 之值大多本來就解得

| 規格側標籤 | DBC `DCSD_DISP_STAT` | R-DM48 判定 |
|---|---|---|
| `[OFF]` | `0 "OFF"` | **解得 raw 0** |
| `[ON]` | `1 "ON"` | **解得 raw 1** |
| `[BLANK]` | `2 "BLANK"` | **解得 raw 2** |
| `[RR_CMRA]` | `3 "RR_CMRA"` | **解得 raw 3** |
| `[DISP_HOT]` | `4 "DISP_HOT"` | 解得 raw 4（既知） |
| `[SNA]` | `7 "SNA"` | **解得 raw 7** |
| `[DISP_OFF]`／`[DISP_ON]` | 查無 | **逐字查無**（R-DM48 之原判定僅此二者成立） |

**R-DM48 立條時所據之「六個值裡規則就不一致」仍為真**，但其推論被過度
適用了：`DCSD_DISP_STAT` 之六個 DBC 值中**有六個都能逐字解得**，
解不得的是規格另外用的 `[DISP_OFF]`／`[DISP_ON]` 兩個**別名**。

### 對 007／008 之影響

`{4820xxx}` RVC 諸條之 DCSD 側逐字為
`the DCSD shall send $DCSD_DISP_STAT$ = [RR_CMRA]` 與
`the DCSD shall send $DCSD_DISP_STAT$ = [ON]` ——
**兩者皆解得（raw 3／raw 1），依 R-DM48 得寫入 ER 之訊號值。**

即 **A3（DR-DM9 阻斷 007／008 之訊號欄）之範圍應縮小**：
DCSD 側不受阻，受阻的是 HU 側 `$TGW_DISP_STAT$`。

### HU 側另有一條未走過的路

規格自身在部分段落寫**雙記法**：`DISP_NORMAL / Normal_mode`、
`DISP_REAR_CAMERA / Rear_Camera_Display`、`ON_BLANK / On_blanked_screen`
等 13 組。而 DBC `TGW_DISP_STATSts` 之 `VAL_` 正是
`2 "Normal_mode"`／`7 "Rear_Camera_Display"`／`8 "On_blanked_screen"`。

**即規格自帶了一份 HU 側之對照表**，其右半逐字等於 DBC 標籤。
本層**不逕行採用**（該對照是否為權威、是否全覆蓋，屬 Tier 2），
但其存在使 DR-DM9 之 HU 側部分可能不必外求。

### 處置

- **不改 DR-DM9 之文字**（DR 之措辭屬分析層）；本項為其前提之更正
- 建議分析層重擬 DR-DM9：分成 (a) `[DISP_OFF]`／`[DISP_ON]` 兩個別名
  對 `DCSD_DISP_STAT` 之對應、(b) 規格雙記法對照表是否為權威
- **A3 之阻斷範圍待分析層裁定後縮小**；本層不逕改 `BACKLOG.md`

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-DMnn]`.
