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

## A-DM5 — 037 `SWE1 Requirements` 表頭含不規則空白  [PENDING]

實測表頭原始字串含尾空格與雙空格：`'SWE-Requirement ID '`、
`'Requirement  Title'`、`'Requirement  Description'`、`' Impact'`、
`'Verification Method '` 等。以逐字字串查欄名者全數落空。

- 證據：`scripts/recount_037.py` 之 columns (RAW, repr) 節
- 影響：任何以精確欄名取欄之實作
- 提案處置：本 feature 之欄名比對一律先 `" ".join(str(s).split())`

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

## A-DM10 — SYS2 無指向 CFTS 條號之錨，mode D 之 spec_reference 無 id 橋樑  [PENDING]

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

## A-DM11 — R-DM7 覆蓋落差：80 列母體中 58 列無對應  [PENDING]

以 SYS2 `Category` 正規化為 `functional requirement` 之 80 列為母體，逐列
標記可否對應到 8 個 SWE-DM leaf：

| 依據 | 列數 |
|---|---|
| id（037 Traceability 之 `Sys-RA-Feature-ID(s)`） | 0 |
| Melco（037 Excluded 分頁明列排除之 HW 項） | 1 |
| Description 文字（共通 token ≥3） | 22 |
| 無 | 57 |

無對應合計 58 列（含上表之 Melco 1 列）。另：`SWE-DM-004`（Thermal
Management）、`SWE-DM-005`（Thermal Protection）、`SWE-DM-007`（RVC
Management）之文字依據命中列數均為 **0**。

- 證據：`scripts/coverage_map.py`、`data/coverage_sys2_vs_swe_dm.tsv`
- 說明：文字分數為機械 bag-of-words 重疊，是**搜尋輔助**；門檻 3 只決定
  列印時的顯示，不是對應之裁定
- 提案處置：本表為 R-DM7 所要求之**揭露**。範圍之裁定屬 Tier 2
  （下放包 01 Q2），執行層不裁定

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-DMnn]`.
