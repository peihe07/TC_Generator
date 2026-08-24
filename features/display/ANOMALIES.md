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

各錨之存在數（非互斥）：含 `$signal$` 43 列、含 `[value]` 34 列、
有 heading 祖先 80 列、Melco 命中 037 Excluded 1 列（r54）。

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

---

## Assumption markers

None yet. Inline format in generated JSON reasoning: `[ASSUMPTION A-DMnn]`.
