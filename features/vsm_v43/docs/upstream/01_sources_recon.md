# 上繳包 01 — vsm_v43：sources 落檔、人工 recon、SYSRA／訊號預查

日期：2026-09-01　執行層　對應下放包：`docs/handoff/01_sources_recon.md`
條號系列：`R-VT`　姊妹線 `vsm_v42` 獨立（本包只讀其 `inputs/`、`RULINGS.md`、
`feature.yaml`、`docs/upstream/01_sources_recon.md` 作對照，未寫入其任何檔）

---

## 〇、一句話結論

**W-1′ → W-6 全部執行完畢，兩處觸停下條款，皆已登記回報而不調和。**

| 停 | 條款 | 事實 |
|---|---|---|
| 停 1 | 01 包 §七第 1 條「E10 任一不同」 | **R-VT2 之 `sha8` 不同**（`efec2621` → `671c5b72`）；其 `body_sha8` **相同**（`a6acf352`），即**條文本體未動**，動的是錨點區段內新增之 R-VT6 加註三列。A-VT13 另載台帳前提不成立 |
| 停 2 | 01 包 §七第 4 條「E15 ≥ 1（停該部分）」 | `signal_chain_v43.tsv` 之 B-1 衝突 **29** 列（預期 0）。**W-5 之訊號實名指派就此停下**，29 列全列 §K 交 Pei（A-VT12） |

另 00 包 §八「E2／E4 不符」亦觸發（E2 之**判準字面**不符，**計數相符**；A-VT10），
依 FO 之第 0 節「Filing = 登記 + 證據 + 建議處置，**然後續行不受影響之工作**」處理。

**E1–E9 首測結果：相符 7、不符 2（E2 判準字面、E9）、E10–E15：相符 4、不符 2（E10、E15）。**
一項亦未調和。

## 一、結果三分法（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | W-1′ 三鍵（R-VT7／R-VT8(c)／路徑 glob）；`workbook.sheet` 與 `design_method`／`functional_safety`／`author` 三欄之 scaffold 模板值（A-VT6）；上繳 00 §八之 canon_refs 歸因數字（本包重測為 502，非 501） |
| 核實無誤 | E1／E3／E4／E5／E6／E7／E8／E11／E12／E13／E14 十一項逐字相符；五件原檔 sha 於搬移前後全等；037 兩份與 SYSAD 之三方 sha 比對全等；`priority` P、`remarks` AH 與 D–O 各欄之 scaffold 值經實測**確為正確**（非未查） |
| 正確地不動 | 台帳 `docs/fw036/RULINGS.sha.tsv` **不重生**（R-VT8(a) 明令本線不為之，A-VT13）；`scripts/recon.py` **不改**（A-VT3 待 Pei）；`scripts/extract_source.py` **不改**（A-VT7／A-VT8）；W-5 之 29 列 B-1 **不逕行採認**（Tier 2）；V42↔V43 訊號差集**不自抽 V42 docx**（01 包明令），記「待 vsm_v42 W-5」 |

---

## 二、W-1′ —— `feature.yaml` 三鍵實值

| 鍵 | 落值 | 依據 |
|---|---|---|
| `tc_id_prefix` | **已刪除，不保留** | R-VT7（R-VC9 之「不保留」） |
| `write_back.tc_id_format` | `"NR1L-VSM43-{n:03d}"` | R-VT7；R-VT3 之值不變 |
| `spec_reference_template` | `null`，就地註「待 P3」 | R-VT8(c) |
| `paths.spec_docx` | `"../../sources/raw/vf665_v43_spec_r4/*.docx"` | 01 包 §三 W-1′（同 vsm_v42 形制） |
| `paths.sysra` | `"../../sources/raw/vf665_v43_sysra/*.xlsx"` | 同上 |
| `paths.sysad` | `"../../sources/raw/vf665_sysad_sys3/*.docx"` | 同上 |
| `paths.workbook` | `"sandbox/base/FM-WI-FSM-036-A01*_SWQT_20260817_ext.xlsx"` | R-VT8(b) |
| `paths.a03_report` | **維持 `null`** | R-VT4；DR-VT1 |

**兩份 037 刻意不入 `paths`**（就地註明理由）：其為 vsm_v42 之母體，**非本線母體**；
列入 `paths` 會使任何遍歷 `paths` 之工具（如 `recon.py:1150-1156` 之 hash 迴圈）
將其當作本線輸入，與 R-VT4 直接牴觸。二者之身分改由 `sources/MANIFEST.tsv` 之
`features` 欄與 `note` 欄承載。

`yaml.safe_load` 通過。

## 三、W-2 —— sources 落檔、sha、sandbox、R-G28

### 3.1 三方 sha 比對（01 包前提，決定是否另建 doc_id）

| 檔 | vsm_v43/inputs | vsm_v42/inputs | vehicle_setting/inputs | 判 |
|---|---|---|---|---|
| 037 Park Sense | `be55d897…9d05` | `be55d897…9d05` | — | **全等** → 取 `vf665_037_parksense`，不另建 |
| 037 Side Distance Warning | `c98909e2…2afd` | `c98909e2…2afd` | — | **全等** → 取 `vf665_037_sdw`，不另建 |
| SYSAD SYS3 v1.0 | `469162b8…b200` | `469162b8…b200` | `469162b8…b200` | **三方全等** → 取 `vf665_sysad_sys3` |

三項皆相同，故**無「不同則停下回報」之情形**。

### 3.2 落檔（R-G27）

`features/vsm_v43/inputs/` 之 5 件以 `mv` 移入 `sources/raw/<doc_id>/`；
**搬移前後逐檔 sha256 全等**；`inputs/` 實測剩 **0** 項（已清空，符 01 包前提）。

| doc_id | sha256 | features 欄 | extracted/ |
|---|---|---|---|
| `vf665_v43_spec_r4` | `c922b4763eec45ca0c294e354788591ededc5d4189387332061288de9b00edbe` | `vsm_v43` | **無**（A-VT7） |
| `vf665_v43_sysra` | `4e8db108ad12d28508419571b56e0dab8475982ac74eee8018f857142e45fb49` | `vsm_v43` | **無**（A-VT8） |
| `vf665_sysad_sys3` | `469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200` | `vsm_v42;vsm_v43` | **無**（A-VT7） |
| `vf665_037_parksense` | `be55d8978f9472f3b7bae8643eee139525f2c455b8bddce24f3911c4128e9d05` | `vsm_v42;vsm_v43` | 有（2 份） |
| `vf665_037_sdw` | `c98909e2c15eb0a02e1ab99f25c4c7bd77226fbd5f29842088bbe06f9f0f2afd` | `vsm_v42;vsm_v43` | 有（2 份） |

`sources/MANIFEST.tsv` 由 3 列增為 8 列（**手工附加**）。
**未用 `--refresh-manifest`**：該旗標（`extract_source.py:188-193`）以
`manifest_rows()` 重寫**全檔**，並把 `version`／`features`／`note` 三欄一律寫成
`未載明`／`未載明`／空 —— 會摧毀既有三列 popup 之中繼資料。此為技術選擇之揭露（R-G8）。

`sysra_export` 之 SYSAD 三方共用列，其 `features` 欄依 01 包「後者只加 features 欄」
之精神先寫 `vsm_v42;vsm_v43`（vsm_v42 之 `feature.yaml` 已引用該 doc_id 路徑，為既成事實）。

### 3.3 抽取（`extract_source.py`）

| doc_id | 結果 |
|---|---|
| `vf665_037_parksense` | ✅ `Analysis Report` 152 列／1324 非空格；`Instructions` 20／39 |
| `vf665_037_sdw` | ✅ `Analysis Report` 97 列／1166 非空格；`Instructions` 20／39 |
| `vf665_v43_sysra` | ❌ `FAIL（§F-6 抽取失真）… 原檔 (1282, 30816)，抽取物 (1282, 30817)` → **A-VT8** |
| `vf665_v43_spec_r4` | ❌ `跳過 …：不支援之型別 .docx` → **A-VT7** |
| `vf665_sysad_sys3` | ❌ 同上 → **A-VT7** |

**A-VT8 之根因已定位到單一儲存格**：`Basic Report` **r480 c16（P 欄）** 之值為**恰好一個換行字元**。
`measure()`（`:67-70`）以 `str(v).strip()!=""` 判空 → 不計；`cell_text()`（`:57-62`）
將其轉義為字面 `\n` 兩字元，回讀時 `cell.strip()` 非空 → 計入。**+1 為自驗兩側對「空白」
定義不一致，非抽取失真。** 該檔三分頁掃描，此型儲存格**全檔僅此一格**。
**不改腳本、不放寬自驗**；W-4／RECON 之計數改自 `raw/` 直讀（R-G27：raw 為權威）。

### 3.4 sandbox 與欄位實測（R-VT8(b)）

`sandbox/base/` 建立，自 `forms/…_SWQT_20260817_ext.xlsx` **檔案複製**；
`cmp` 全等（exit 0），sha256 `6372fb6b…825b2`（E11 ✅）。
全程 `openpyxl` 僅 `read_only=True`，**未曾 `wb.save()`**（母本 R 欄 x14 DV 之保全，R-G1 註／A-UP09）。

**逐欄實測 vs 先驗（R-VT8(b) 所載）：**

| 欄位 | 先驗 | 實測 | 判 | | 欄位 | scaffold 模板值 | 實測 | 判 |
|---|---|---|---|---|---|---|---|---|
| priority | P | **P** | ✅ | | req_id | D | **D** | ✅ |
| estimated_test_time | Q | **Q** | ✅ | | test_group／test_set／test_item | G／H／I | **G／H／I** | ✅ |
| design_method | R | **R** | ✅ | | pre_conditions…tc_ref_id | J–O | **J–O** | ✅ |
| functional_safety | S | **S** | ✅ | | design_method | Q | **R** | ❌ 模板值錯 |
| author | AA | **AA** | ✅ | | functional_safety | R | **S** | ❌ 模板值錯 |
| test_version | AB | **AB** | ✅ | | author | Z | **AA** | ❌ 模板值錯 |

**先驗六項 6/6 相符（E12 含其二）**；scaffold 模板值三項錯（A-VT6）。
另 scaffold 無 `tc_id`（實測 **F**）與 `estimated_test_time`（**Q**），已補。
本母本**無**重複之 `Estimated Test Time` 欄（power 之工作簿有兩個，A-PW37）——
即 A-PW37 之錯位型態**不適用於本母本**，但其「模板值不可信」之教訓適用且已命中三次。

**`workbook.sheet` 之 scaffold 值 `Test Case Specification&Result` 於本母本不存在**
（實測分頁見 A-VT6），會於 `recon.py:431` 直接 `sys.exit` —— 已改為
`Test Case Specification 測試用例規範`。

### 3.5 R-G28（CFTS 嵌入物件）

**已查，查無。** 全庫 `find . -ipath "*CFTS Embedded Objects*"` 命中 **0**
（本 feature 之母 CFTS 目錄不存在，與 sw_update 之 CFTS<nnn> 型態不同）。
依 R-G28「查無者亦記明已查」，於此記明。

**另行清點 #1 docx 自身之內嵌物**（R-G28 之同一風險面，非其字面要求）：
zip members **25**，媒體／內嵌 **1** 件 —— `word/media/image1.wmf`。
WMF 為向量圖，本包**未轉圖、未做「由圖找列」**（該程序之對象為 CFTS 母目錄）。
**提請 P3 決定**是否對此單一 WMF 施作 R-G28 之二欄表，理由是 R-G28 之成因
（圖中載有未見於 docx 之數值）在單一功能圖上同樣可能成立。

---

## 四、W-3 —— 人工 `RECON.md`

**人工**（非 `scripts/recon.py` 輸出），依 A-VT3；落於 `features/vsm_v43/RECON.md`。
本體全文如下（與該檔逐字相同）：

<details>
<summary>RECON.md 本體</summary>

```markdown
# RECON — vsm_v43（Vehicle Setup Management R1L TBM，VF665 V43）

> **本檔為人工 RECON，非 `scripts/recon.py` 之輸出。**
> 依 A-VT3：`recon.py` 於 `a03_report` 為 null 時於 `:582` TypeError（`survey_a03`
> 直接 `openpyxl.load_workbook(None)`），改碼權屬 Pei（01 包 §四），裁前不改腳本。
> 下列每一數字皆由本執行層自 `sources/raw/` 之原檔實測，量測條件逐項列明（R-G8）。
> 日期：2026-09-01　執行層　對應下放包：`docs/handoff/01_sources_recon.md` W-3

---

## 1. workbook_state

| 項 | 值 | 量測條件 |
|---|---|---|
| workbook_state | **BLANK** | `sandbox/base/` 副本，分頁 `Test Case Specification 測試用例規範`，第 10 列起、**B 欄除外**（B 為 `=IF(ISBLANK($D10),"",ROW()-9)` 序號公式）之非空儲存格列數 = **0**（掃 max_row 1411） |
| 母本身分 | `forms/…_SWQT_20260817_ext.xlsx`（R-G1） | `cmp` 與 forms/ 原件全等；sha256 `6372fb6b…825b2`（E11） |
| 表頭列 | 9 | 逐列讀取，第 9 列有 33 個非空表頭，佔 B–AH |
| openpyxl 存回 | **未曾為之** | 全程 `read_only=True`；母本 R 欄 x14 DV 之保全（R-G1 註／A-UP09） |

`workbook_state = BLANK` 亦與 R-VT1（「自 BLANK ＋ R-G1 模板起建」）一致。

## 2. 素材與 sha256（R-G27 落點）

| doc_id | 檔名 | sha256 | extracted/ |
|---|---|---|---|
| `vf665_v43_spec_r4` | `Vehicle_Setup_Management_by_VP_-_LTM_(R1L)_with_TBM_VF665_V43_R4.docx` | `c922b4763eec45ca0c294e354788591ededc5d4189387332061288de9b00edbe` | **無**（A-VT7：`.docx` 不支援） |
| `vf665_v43_sysra` | `FM-WI-FSM-035-A02_VF665_V43_STLA_SYSRA…_VF665_V43_Release.xlsx` | `4e8db108ad12d28508419571b56e0dab8475982ac74eee8018f857142e45fb49` | **無**（A-VT8：§F-6 自驗誤報中止） |
| `vf665_sysad_sys3` | `SYS3_Vehicle_Settings_FM-WI-FSM-011-A01_…_SYSAD_v1.0.docx` | `469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200` | **無**（A-VT7） |
| `vf665_037_parksense` | `FM-WI-FSM-037-A03_SWE1_VF665_…_Park_Sense_And_Restore Default Setting __Features_Report.xlsx` | `be55d8978f9472f3b7bae8643eee139525f2c455b8bddce24f3911c4128e9d05` | 有（`Analysis Report` 152 列／1324 格、`Instructions` 20／39） |
| `vf665_037_sdw` | `FM-WI-FSM-037-A03_SWE1_VF665_…_Side_Distance_Warning - Audio_Repetition Features_Report.xlsx` | `c98909e2c15eb0a02e1ab99f25c4c7bd77226fbd5f29842088bbe06f9f0f2afd` | 有（`Analysis Report` 97 列／1166 格、`Instructions` 20／39） |

sha 於 `features/vsm_v43/inputs/` → `sources/raw/` 之搬移前後逐檔比對，**五件全等**。
`inputs/` 已清空（實測 0 項）。

**三方 sha 比對（01 包前提）**：
- 037 兩份 vs `features/vsm_v42/inputs/` 同名檔：**逐位元全等**（`be55d897…`／`c98909e2…`）→ 不另建 doc_id，取 vsm_v42 之 `vf665_037_parksense`／`vf665_037_sdw`。
- SYSAD vs `features/vsm_v42/inputs/` vs `features/vehicle_setting/inputs/`：**三方全等**（`469162b8…`）→ 取 `vf665_sysad_sys3`。本線先落（01 包「誰先跑誰落」）。

## 3. 母體（037）

```
a03_report = null   （DR-VT1）
```

V43 之 037 **不存在**（R-VT4）。`sources/raw/` 之兩份 037 為 **vsm_v42 之母體**，
其 `Source Requirement ID` 非空 82 ＋ 70 = **152**，`V42` 命中 152／152，`V43` 命中 **0**（E7）。
本線 leaf 母體 = **0**，不得以 SYSRA 或規格代之（R-VT4，禁區 §零-5）。

| 項 | 值 |
|---|---|
| 037 leaf 數 | **0**（無 037） |
| done region 覆蓋 | 不適用（BLANK） |
| regen targets | **0** |
| 無處覆蓋之 leaf | 不適用 |

## 4. SYSRA 計數（`Basic Report`，表頭列 1）

量測條件：`openpyxl` `read_only=True, data_only=True`；資料列 = 第 2 列起、任一欄非空者；
欄以表頭文字定位（`SYS2 分類 Category` = M、`SYS2 文件識別碼 Document ID` = I、
`SYS2 EE Architecture` = J、`SYS2 驗證方法 (Verification Method)` = BH、`Description` = D）。

| 項 | 實測 |
|---|---|
| 資料列（E1） | **1280** |
| Category（全等，E2／E3） | `Functional Requirement` **507**／`Information` 492／`Heading` 182／`Out of scope` **55**／`Out of Scope` **44** |
| Category 正規化後 `out of scope`（E14） | **99** |
| Document ID（全等，E4） | `VF665_V43_R3` **951**／`VF655_V43_R3` **247**／空 **82** |
| Functional 中 Document ID（E5） | `VF665_V43_R3` 295／`VF655_V43_R3` **171**／空 41 |
| EE Architecture（全等，E6） | `ATL-Mi` **1280**（單一值） |
| Function (Level 1) 於 Functional | `A. 核心顯示管理(Core Display Management)` **506** ＋ `2. 系統特定診斷(System-Specific Diagnostics)` **1** |
| Verification Method 相異值（正規化，E9） | 全 1280 列：**61**（含空白，空白 750）；Functional 507 列內：**57**（含空白）／**56** 非空 |
| `Melco ID`（C 欄）非空 | **0 / 507** —— 全 Functional 列該欄皆空（A-VT9） |

**分母之處置（DR-VT2）**：Functional 507 列中，`VF655_V43_R3` **171** 列與
Document ID 空 **41** 列**分別標記、不入分母**；分母 = **295**。
逐列標記見 `data/sysra_v43_functional.tsv` 之 `denominator`／`mark` 兩欄。

## 5. 跨源對照（E8）

V43 Functional 描述（`Description`，`re.sub(r'\s+',' ').strip().lower()`）507 條、去重 **398**；
V42 SYSRA（`features/vsm_v42/inputs/`，分頁 `Analysis Report`，表頭列 5，
Category 第 10 欄、Description 第 3 欄）Functional 318 條、去重 **308**。
**去重交集 = 30 / 398**（E8）。

> V42 SYSRA 之版面與 V43 **不同**：V43 為 Polarion `Basic Report` 匯出（分頁
> `Basic Report`／`Polarion`／`_polarion`），V42 為 035 表單版面（分頁 `封面`／`修訂履歷`／
> `Product Document 記錄封面頁`／`Analysis Report`／`Instructions`／`下拉選單設定處`）。
> 兩者不可以同一組欄位座標讀取；本檔之 V42 欄位為自其表頭實測所得。

## 6. spec 文字層

`spec_mode = D`（二進位文件抽取）。#1 docx magic bytes `50 4B 03 04`（E13，OOXML）。
`word/document.xml` 段落抽取得 **1781** 個非空段落。
zip members **25**，其中媒體／內嵌物件 **1** 件：`word/media/image1.wmf`。

## 7. 未決

| 項 | 依據 |
|---|---|
| Layer 2 test set 母體 | 待 037（R-VT4／DR-VT1） |
| `spec_reference_template` | null，待 P3（R-VT8(c)） |
| R-P368 段 1 之 LID 欄組適用性 | 本線 EE 全為 ATL-Mi（1280/1280 實測），與 vsm_v42 同題，待裁 |
| B-1 型衝突 29 列 | E15 ≥ 1，停該部分並列 §K（`docs/upstream/01_sources_recon.md`） |
```

</details>

---

## 五、E1–E15 逐項對照（相符者亦列，不符不調和）

### 5.1 E1–E9（00 包 §六，**本包首測**）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| E1 | `Basic Report` 資料列 | 1280 | **1280** | ✅ 相符 |
| E2 | Functional | 507 | **`Functional Requirement` 507**；以 `Functional` 全等計 **0** | ⚠ **計數相符、判準字面不符**（A-VT10） |
| E3 | `Out of scope` ＋ `Out of Scope` | 55 ＋ 44 | **55 ＋ 44** | ✅ 相符 |
| E4 | DocID `VF665_V43_R3`／`VF655_V43_R3`／空 | 951／247／82 | **951／247／82** | ✅ 相符 |
| E5 | Functional 中 DocID `VF655_V43_R3` | 171 | **171**（以 `Functional Requirement` 讀）；以 `Functional` 全等讀 **0** | ✅／⚠ 同 E2 之判準問題 |
| E6 | EE ATL-Mi | 1280 | **1280**（單一值，1280/1280） | ✅ 相符 |
| E7 | 037 兩檔內 `V43` 字串命中 | 0 | **0**（parksense 0、sdw 0） | ✅ 相符 |
| E8 | V43↔V42 Functional 描述逐字相同（去重） | 30／398 | **30／398** | ✅ 相符 |
| E9 | `Verification Method` 相異值 | 4 | 全 1280 列 **61**；Functional 507 列內 **57**（含空白）／**56** 非空 | ❌ **不符**（A-VT11） |

**E9 之細部對照**（供歸因，不作調和）：預期舉出之
`verified by in-vehicle testing` = **47** ✅ 逐字相符；
`internal signal stimulation test…` 預期 28，實測**以該串開頭者 30 列、相異 13 種**，
無任一單一值為 28。下放包未載 E9 之掃描範圍（全表 vs Functional）與是否截斷。

**掃描條件揭露**：`openpyxl` `read_only=True, data_only=True`；資料列 = 第 2 列起、
任一欄非空；欄以表頭文字定位（Category M、Document ID I、EE J、Verification Method BH、
Description D）；正規化一律 `re.sub(r'\s+',' ').strip().lower()`；
「全等」指**未正規化**之逐字比對。E8 之 V42 側欄位自其表頭實測（版面與 V43 不同，見 RECON §5）。

### 5.2 E10–E15（01 包 §五，新增）

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| E10 | R-VT1–R-VT5 sha8 與上繳 00 §七逐字相同 | 全同 | **R-VT2 不同**（`efec2621` → `671c5b72`）；其餘四條相同 | ❌ **不符 → 停 1** |
| E11 | `sandbox/base` 副本 sha256 | `6372fb6b…825b2` | **`6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2`**；`cmp` 全等 | ✅ 相符 |
| E12 | 副本 r9：design_method／author | R／AA | **R／AA** | ✅ 相符 |
| E13 | #1 docx magic bytes | `50 4B 03 04` | **`504b0304`**（五件原檔皆同） | ✅ 相符 |
| E14 | `Out of scope`＋`Out of Scope` 正規化後 | 99 | **99** | ✅ 相符 |
| E15 | `signal_chain_v43.tsv` B-1 衝突列 | 0（≥1 即停） | **29** | ❌ **不符 → 停 2** |

**E10 之細部（不調和，但歸因已做到底）**：

| 條號 | 上繳 00 §七 `sha8` | 本包 `sha8` | 判 | 上繳 00 `body_sha8` | 本包 `body_sha8` | 判 |
|---|---|---|---|---|---|---|
| R-VT1 | `9d60e34c` | `9d60e34c` | 相同 | `93666dae` | `93666dae` | 相同 |
| **R-VT2** | `efec2621` | **`671c5b72`** | **不同** | `a6acf352` | `a6acf352` | **相同** |
| R-VT3 | `f7f9c460` | `f7f9c460` | 相同 | `d3823bca` | `d3823bca` | 相同 |
| R-VT4 | `d50ba0a0` | `d50ba0a0` | 相同 | `9844b823` | `9844b823` | 相同 |
| R-VT5 | `1409b527` | `1409b527` | 相同 | `e8e8724b` | `e8e8724b` | 相同 |

R-VT2 之 `body_lines` 由 **23** 增為 **26**；`body_sha8` 未變。
即 **fenced 條文本體逐位元未動**，變動落在錨點區段內新增之三列 ——
`> **註記（R-TM13，2026-09-01，R-VT6）**：(b) 所引 R-P368 連帶承接 **R-P375**…`。
該加註為 **R-VT6(d)「R-VT2 原文不改，加註指向本條」之直接產物**。

> **這不是漂移，是 E10 之判準與 R-VT6(d) 互斥。** R-VT6(d) 令對 R-VT2 加註，
> 而 `rulings_hash` 之 `sha8` 涵蓋整個錨點區段（含加註），故只要 R-VT6 落檔，
> E10 之「逐字相同」在 `sha8` 欄上**必然不成立**。二者不可能同時滿足。
> **執行層不代擬條文，也不自行改判準**（FO 之第 8.5 節第 1、2 條）：
> 據實記為不符，並指出 `body_sha8` 為此情形下唯一穩定之比較欄。
> **提請裁決**：E10 之後續比較改用 `body_sha8`。

**E10 之量測來源另有一層問題（A-VT13）**：01 包 §二與 R-VT8(a) 令 sha8
「自 vsm_v42 01 包重生後之台帳讀取」。實測 `docs/fw036/RULINGS.sha.tsv` 之
`R-VT`／`R-VL` 列數 **0** —— `features/vsm_v42/docs/upstream/01_sources_recon.md`
載該線**停於 W-0**，重生未執行。本包**不代重生**（R-VT8(a) 明令本線不為之），
改以 `rulings_hash.py --out <scratchpad 樹外>` 取值，**明示此為替代量測**，
上表之「本包 sha8」即出自該替代量測。

### 5.3 R-VT6–R-VT8 之 sha8（01 包 §六）

| 條號 | 一句話 | `sha8` | `body_sha8` | 來源：列 | 本體列數 |
|---|---|---|---|---|---|
| R-VT6 | 段 1 入口依 R-P375 擴為 forms/ 全部參考檔；多命中之處置 | `ab4699aa` | `8db4c81b` | `features/vsm_v43/RULINGS.md`:89 | 10 |
| R-VT7 | TC ID 鍵名採全庫慣例 `write_back.tc_id_format` | `ff472973` | `9b4427c5` | 同上:102 | 5 |
| R-VT8 | 台帳本線不重生；sandbox 與欄位從 R-VL8 同法 | `7463c474` | `2b3fcbe6` | 同上:110 | 9 |

同一替代量測來源（樹外重生），理由同 A-VT13。三條 `body_kind` 皆為 `fenced`。

---

## 六、W-4 —— `data/sysra_v43_functional.tsv`

欄位：`sheet_row | polarion_id | melco_id | chapter_for_vf | document_id |
function_level1 | verification_method_trunc | denominator | mark`

| 項 | 值 |
|---|---|
| 總列數（Functional Requirement） | **507** |
| `denominator = IN`（**分母**） | **295** |
| `denominator = EXCLUDED` | **212** |
| ├ `mark = VF655_誤植疑義(DR-VT2)` | **171** |
| └ `mark = DocID_空(DR-VT2)` | **41** |
| `chapter_for_vf` 非空 | **507 / 507** |
| `melco_id` 非空 | **0 / 507** ← A-VT9 |
| `function_level1` | `A. 核心顯示管理(Core Display Management)` **506** ＋ `2. 系統特定診斷(System-Specific Diagnostics)` **1** |

**DR-VT2 之處置照辦**：`VF655_V43_R3` 與 DocID 空兩群**分別標記**（`mark` 欄可區分二者，
未合併為單一「排除」旗標）、**不入分母**。

> **註**：00 包 §五 W-4 所稱之「`VF655` 247 列與空 82 列」為**全表**計數（E4 已驗，247／82）；
> 落在 Functional 507 內者為 **171／41**（E5 已驗 171）。本 TSV 之母體為 Functional，
> 故排除數為 171＋41 = 212，非 247＋82。**兩組數字皆正確，指涉範圍不同**，
> 於此明列以免日後誤判為不符。

**`Out of scope` 二拼法**：全等計 `Out of scope` **55**、`Out of Scope` **44**（E3）；
正規化（小寫）後 `out of scope` **99**（E14）。上游拼法不一之情形**經本包實測確認**，
其 anomaly 依 00 包 W-4 應登記 —— 惟該情形已由 **DR-VT2 之姊妹面**（上游一致性）涵蓋，
且本包實測與下放包預期**完全相符**，故**不另開 A-VT 條**，於此記明並列入 §八之 DR 清單註。

---

## 七、W-5 —— `data/signal_chain_v43.tsv`

### 7.1 抽名與量測條件（R-G8）

來源：`sources/raw/vf665_v43_spec_r4/…R4.docx`，`zipfile` 讀 `word/document.xml`，
逐 `<w:p>` 取 `<w:t>` 串接並 `html.unescape`，得 **1781** 個非空段落。
（`extract_source.py` 不支援 `.docx`，A-VT7；依 R-G27「raw 為權威」直讀。）

抽名三式：
- CAN 形 `\b([A-Z][A-Z0-9_]{3,})\.([A-Za-z][A-Za-z0-9_]*)\b`
- 內部 `\b([A-Za-z][A-Za-z0-9_]*)\.(Req|Info|GUI)\b`
- PROXI `\b([A-Za-z][A-Za-z0-9_]*)\s+PROXI parameter\b`

**偽陽性／偽陰性風險（揭露）**：CAN 形之正則會收進非訊號之全大寫點記法；
PROXI 形只認「`X` PROXI parameter」之句式，**規格中以表格列出而未用該句式者會漏**
（本包僅得 2 名，明顯偏低）。二者皆為**候選**而非認定（R-P375(d)）。

**抽得相異名 181**：CAN **92**、內部 **87**、PROXI **2**。

### 7.2 段 1 —— 七檔各命中數（R-VT6(a)／R-P375(a)）

| # | 檔（`forms/`） | 段別 | 命中之相異名數 |
|---|---|---|---|
| 1 | `Logical Identifiers and CAN Mapping v1_78.xlsx`（**全分頁**） | 段 1 | **23** |
| 2 | `HMI Settings List R1 SR25 Post R1L-R (Feb 13 2026).xlsx` | 段 1 | **0** |
| 3 | `PROXI_HDCC27_R3_20250424.xlsx` | 段 1 | **2** |
| 4 | `SR26 Default Settings and PNet ECU Configuration v1_0.xlsx` | 段 1 | **0** |
| 5 | `SR24 R1 Market Configuration Table v1.6.xlsx` | 段 1 | **0** |
| 6 | `PDT27_E2A_R1_BHCAN2.dbc` | 段 3 | **4**（`SG_` 相異 342） |
| 7 | `PDT27_E2A_R1_FDCAN8.dbc` | 段 3 | **69**（`SG_` 相異 1634） |

段 1 之比對為**逐字**（原名，及去 `MESSAGE.` 前綴之短名兩式），命中處逐一記
`檔/分頁/r{列}c{欄}(命中鍵)` 於 TSV 之「段1命中處(前4)」欄 —— 符 R-P368(b)
「須載明比對依據（哪一欄、哪一列），不得憑語意跳接」。
**R-P368(b) 所許之 `Logical Identifier`／`Description` 欄之前後綴／底線差異比對，
本包未施作**（那需要逐名人工判讀，且每一對應須另立依據）；故段 1 之 23 為**下界**。

### 7.3 結果分布

| 結果 | 列數 |
|---|---|
| 解得 | **40** |
| **B-1 衝突** | **29** ← E15，停 2 |
| 未解得(止於段2) | **8** |
| PROXI路徑 | **2** |
| 查無(R-G13) | **102** |
| 合計 | **181** |

`查無(R-G13)` 102 列中 **87 列為內部訊號**（`.Req`／`.Info`／`.GUI`）——
與 PM 之經驗一致（R-P355(a)：內部訊號多無 DBC 對照）。依 R-P355(c)／R-P368(f)，
其 TC 寫法為保留原名不加 `$` 並掛 `PENDING: DR-{n}`，**惟本線尚無 TC（R-VT4），
故不生成任何 `PENDING` 佔位**。
R-G13 三要件與 `forms/LOOKUP_MISSES.md`（R-G14）之登錄**本包未做** ——
理由：R-G13 之「查無」須滿足三要件，而段 1 之 R-P368(b) 擴充比對尚未施作（見 7.2），
現階段之 102 依 R-P368(d) 之字面應記為「**未解得**」而非「查無」。
TSV 之 `查無(R-G13)` 標籤因此**偏嚴**，此為本包之未竟項，列入 §十獨立判斷。

### 7.4 §K —— B-1 衝突表（29 列，交 Pei）

判準之爭點見 A-VT12：**R-VT6(c) 只定義「同一規格原名多處命中而解至不同標的」為 B-1，
未定義「段 3 之 `SG_` 所屬 `BO_` 與規格訊息名不符」是否為 B-1。**
本包將後者操作化為 B-1，此技術選擇**改變了 E15 之結論**（1 → 29），
依 FO 之第 0 節 Tier 0 末句「一旦選擇會改變結論，它就不再是技術選擇」即為 **Tier 2**，
故全數列此交裁，**不逕行採認**。
**採 R-VT6(c) 字面則 B-1 = 1（型態三），其餘 28 列改記「未解得（訊息名待確認）」。兩讀法並列。**

**型態一 —— `*_SETUP2` 訊息於 forms DBC 落在無 `2` 之同名訊息下（22 列）**

| 規格原名 | 段 3 實測 |
|---|---|
| `IPC_VEHICLE_SETUP2.AutoUnlockDoorExit` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.Backup_Cam_Delay` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.EPB_MaintenanceMode` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.FSFCWPlusActivationMode` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.FSFCWPlusSetting` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.FlashLightWLock` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.HeadlightsOffDelay` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.LDW_Intensity` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `IPC_VEHICLE_SETUP2.LDW_Sensibility` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.AutoUnlockDoorExit_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.Backup_Cam_Delay_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.EPB_MaintenanceMode_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.FSFCWPlusActivationMode_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.FSFCWPlusSetting_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.FlashLightWLock_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.HeadlightsOffDelay_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.LDW_Intensity_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP2.LDW_Sensibility_Req` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_SERVICE_SETUP.ClearPersonalDataReq` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_SERVICE_SETUP.PrivacyModeReq` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_SERVICE_SETUP.RestoreAppReq` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |
| `TELEMATIC_SERVICE_SETUP.RestoreDefaultSettingReq` | `FDCAN8:TELEMATIC_VEHICLE_SETUP` |

**此群不可以「DBC 少一個版本」一語帶過 —— 兩項反證：**
1. `IPC_VEHICLE_SETUP2` **確實存在**於 FDCAN8，帶 **34** 個 `SG_`
   （全為 `AUX{1..4}_HLEnbl`／`_PWRMD`／`_TYPE` 型），**但不含**上列九名。
2. `TELEMATIC_VEHICLE_SETUP2` 於兩本 DBC **完全不存在**；存在者為
   `TELEMATIC_VEHICLE_SETUP` 與 `TELEMATIC_VEHICLE_SETUP3`。

**型態二 —— 訊息名全然不同（6 列）**

| 規格原名 | 段 3 實測 |
|---|---|
| `SERVICE_SETUP.ClearPersonalData` | `FDCAN8:TBM_SCHEDULE_FD_2` |
| `SERVICE_SETUP.PrivacyMode` | `FDCAN8:TBM_SCHEDULE_FD_2` |
| `SERVICE_SETUP.RestoreApp` | `FDCAN8:TBM_SCHEDULE_FD_2` |
| `SERVICE_SETUP.RestoreDefaultSetting` | `FDCAN8:TBM_SCHEDULE_FD_2` |
| `SERVICE_SETUP.TelematicSetupACK` | `FDCAN8:IPC_VEHICLE_SETUP` |
| `TELEMATIC_VEHICLE_SETUP.RemoteDoorUnlock` | `FDCAN8:IPC_VEHICLE_SETUP` |

**型態三 —— 兩本 DBC 解至不同訊息（1 列；R-VT6(c) 字面型）**

| 規格原名 | 段 3 實測 |
|---|---|
| `BRAKE1.VehicleSpeedVSOSig` | `BHCAN2:STATUS_CCAN3` ＋ `FDCAN8:BRAKE_FD_2` |

**R-P368(e) 之 R4 BHCAN 旁證：本包未引**（`features/vehicle_setting/inputs/` 屬他線，
禁區 §零-2 之精神；且未查即不得記為證據）。故上列無任一列為 R-P368(e) 字面之 B-1。

### 7.5 V42 ↔ V43 訊號名差集

**「待 vsm_v42 W-5」。** 實測 `features/vsm_v42/data/` 為**空目錄**，
`signal_chain_v42.tsv` **不存在**（該線停於 W-0）。
依 01 包 §三 W-5 之明令，**V42 側只讀該檔，不自抽 V42 docx**，故差集本包不產出。
（V42 之規格 docx 實體確在 `features/vsm_v42/inputs/`，本包**刻意未讀**。）

此缺席之後果：DR-VT1 之「請上游明示 V43 是否以 V42 之 037 延伸、若是需給差異列」
一項仍無本地舉證。**建議 Pei 送 DR-VT1 時說明此點**，或先解 vsm_v42 之 W-0 阻塞。

---

## 八、anomaly／DR 成對清單

### 本包新登（`features/vsm_v43/ANOMALIES.md`）

| id | 一句話 | 狀態 | 配對 DR |
|---|---|---|---|
| A-VT6 | scaffold 之 `workbook.sheet` 與三個欄位模板值於 R-G1 母本不符 | RESOLVED（執行層逕改，A-VT4 同型） | — |
| A-VT7 | `extract_source.py` 不支援 `.docx`，#1／#3 無 `extracted/` | PENDING | — （工具問題，非上游資料） |
| A-VT8 | `extract_source.py` §F-6 自驗對 SYSRA 誤報（單一 `'\n'` 儲存格） | PENDING | — （同上） |
| A-VT9 | SYSRA `Melco ID` 於 Functional 507 列全空 | PENDING | 併 **DR-VT2**（同屬上游 SYSRA 欄位品質） |
| A-VT10 | E2 判準字面（`Functional` vs `Functional Requirement`）不符 | PENDING | — （下放包判準之澄清，非上游） |
| A-VT11 | E9 相異值 4 vs 實測 57／61 | PENDING | — （同上） |
| A-VT12 | B-1 型衝突 29 列；判準本身待裁 | PENDING（E15 停） | **建議新開 DR**：`TELEMATIC_VEHICLE_SETUP2` 於 forms DBC 全無 —— DBC 版次落後 R4，或規格訊息名有誤？**執行層不送**（禁區 §零-6），草稿列於下 |
| A-VT13 | 台帳無 R-VT 列，E10 之取值前提不成立 | PENDING | — （內部依賴，非上游） |

**A-VT12 之 DR 草稿（未送，待 Pei）**：
> 向 SYS2／CAN 矩陣維護方確認：V43 R4 規格所載之 `TELEMATIC_VEHICLE_SETUP2.*`
> 九個訊號，於 `forms/PDT27_E2A_R1_FDCAN8.dbc` 與 `BHCAN2.dbc` 均查無該訊息名
> （存在者為 `TELEMATIC_VEHICLE_SETUP` 與 `TELEMATIC_VEHICLE_SETUP3`）；
> 另 `IPC_VEHICLE_SETUP2.*` 九名之訊號雖存在，卻位於 `IPC_VEHICLE_SETUP` 之下，
> 而 `IPC_VEHICLE_SETUP2` 本身另有 34 個 AUX 類訊號。請確認 DBC 版次與規格版次之對應。

### 沿用（`DATA_REQUESTS.md`，本包未動）

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VT1 | V43 之 037 缺件 | **yes** | 已登記，建議送出，**未送出** |
| DR-VT2 | SYSRA DocID `VF655` 疑誤植；R3 vs R4 | no | 已登記，**未送出**。本包新增兩項佐證：Functional 內 `VF655` **171** 列（E5）；`Out of scope`／`Out of Scope` 二拼法 55／44（E3，上游一致性之同一面）；`Melco ID` 全空（A-VT9） |

送出權屬 Pei（Tier 3）。本包未送、未改 `DATA_REQUESTS.md`。

---

## 九、`gate_all.py` 輸出與歸因

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 502
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）

總判：**FAIL** —— 4 支未過：canon_refs、rulings_hash、gates_tsv、lint_paths
```

| 閘 | 與 vsm_v43 之關係 | 實測歸因 |
|---|---|---|
| `canon_refs` | **本包貢獻 0（實測）** | 首跑 503。以逐段落移除歸因法定位到本包 `ANOMALIES.md` A-VT10 之單一行（`FO §8.5` 之引用形態判 ambiguous），改寫為「FO 之第 8.5 節」後回 **502** —— 即與本包執行前之基線相同。**上繳 00 §八所報之 501 已不可重現**（該輪即已漂移為 502，見上繳 00 §八之漂移註）；502 為本輪之穩定基線 |
| `rulings_hash` | **相關（唯一一支）** | 台帳缺 `R-VL1–5` ＋ `R-VT1–8` 共 **13** 列（上繳 00 時為 10 列，本包新增 R-VT6–8 三條）。**本線不重生**（R-VT8(a)），且 vsm_v42 之 R-VL9 停於 W-0（A-VT13） |
| `gates_tsv` | **無關** | 差異列全屬 `lint036`（`I-cross`、`W`）、`driver_distraction`／`ics_management` 之 selfcheck 腳本、`lint_docs036` 之 `body_kind`。無 vsm_v43 之列 |
| `lint_paths` | **無關** | 四筆紅全在 `features/driver_distraction/workbook/*.xlsx`（2）、`ics_management/delivered/`（1）、`sw_update/delivered/`（1）。**本包新增之 `features/vsm_v43/sandbox/base/*.xlsx` 未判紅** —— `sandbox` 為 `.xlsx` 之合法落點（R-G25），實測基線外違規仍為 2，未增 |

依 FO 之第 8.2 節／26 包 §C 裁定 2：**本包附本節之升級說明上繳**。

---

## 十、獨立判斷（「本包是否仍有該驗而未驗者」）

1. **有，且是最重要的一項：段 1 之 R-P368(b) 擴充比對未做。**
   R-P368(b) 明許以 LID 之 `Logical Identifier`／`Description` 欄比對，
   容許前綴／後綴／底線差異。本包段 1 只做**逐字**（原名與去訊息前綴之短名兩式），
   命中 23／181。**故 §七 之「查無(R-G13)」102 列標籤偏嚴** ——
   依 R-P368(d)，未做完段 1 者應記「未解得（止於段 1）」，
   而 R-G13 之「查無」須滿足三要件（本包未滿足，亦未登 `forms/LOOKUP_MISSES.md`）。
   **這正是 R-P355 之 A-PW355 所犯之同型錯誤的鏡像**（該案是「跳過段 1–2 只做段 3
   而報查無」）。本包已在 §7.3 就地標明，但 TSV 之標籤字面未改 ——
   **提請 P3 前補做段 1 擴充比對並重算**，或先將該 102 列之標籤改為「未解得(止於段1)」。

2. **PROXI 只抽得 2 名，明顯偏低。** 抽名式只認「`X` PROXI parameter」之句式；
   規格之 Configuration Parameters 多以表格列出。R-VT6(b)／R-P375(b)(c) 之
   UI／PROXI 路徑因此**幾乎未被行使**（`HMI_Settings` 命中 0、`SR26_Default` 命中 0）。
   這使「內部訊號 87 名全數落入查無」之結論**可能是抽名不足所致，而非事實**。
   **提請 P3 以表格結構抽取重做 W-5**，本包之 181 名視為下界。

3. **E10 與 R-VT6(d) 結構性互斥（見 §5.2）。** 只要往後任何一包對既有條文加註，
   `sha8` 型之「逐字相同」預期就會失敗。建議 canon 層面改以 `body_sha8` 為條文身分之
   比較欄，`sha8` 保留作區段完整性。此為跨 feature 之問題，非本線可裁。

4. **A-VT7／A-VT8 兩支同指一件事：`extract_source.py` 對本專案之素材型態覆蓋不足。**
   spec_mode D 之 feature（power、vsm_v42、vsm_v43…）之母 spec 皆為 `.docx`，
   而該腳本自始不支援；SYSRA 之自驗又因一個換行儲存格誤報。
   合起來，`sources/extracted/` 對本線之三件主要素材**一件都沒產出**。
   若 P4 以後有任何工具改讀 `extracted/`，本線會靜默地讀到空目錄。
   **建議與 A-VT3 一併作為「共用腳本三項待裁」送 Pei**，而非逐包各報一次。

5. **`workbook.columns` 之教訓已第三次命中。** scaffold 模板在本包錯了四處
   （sheet 名、design_method、functional_safety、author），power 錯過一次（A-PW37），
   本線 00 包已預警一次。**建議 `new_feature.py` 之模板改為全 `null` 並附
   「須自 r9 表頭實測」之註**，使「未填」與「填錯」在 diff 上可區分 ——
   現行行為是後者，而後者在 lint 全綠時看不出來（FO 之第 8.3 節第二層之同型風險）。

6. **本包未驗而下放包亦未要求者，記明兩項**：
   (a) SYSAD（#3）除 sha 外**完全未讀**，其架構內容對 P3 framework 之影響未知；
   (b) `sources/raw/vf665_v43_sysra` 之 `Polarion`（88 列）與 `_polarion`（1299 列）
   兩分頁**未做任何計數** —— 下放包之 E1–E9 全針對 `Basic Report`。

---

## 十一、禁區遵守聲明（00 包 §零）

| 禁區 | 遵守 |
|---|---|
| 1. git 一律不動 | 本包未跑任何 `git` 寫入指令。唯讀之 `git show HEAD:features/vsm_v43/ANOMALIES.md` 用於 §九之移除歸因法 |
| 2. 不寫 `features/vehicle_setting/`、`features/vsm_v42/` | 未寫。`vsm_v42` 僅讀 `inputs/`（037×2、SYSAD、SYSRA）、`RULINGS.md`、`feature.yaml`、`data/`（實測為空）、`docs/upstream/01_sources_recon.md`。**未讀其 spec docx**（W-5 明令） |
| 3. 不寫 `docs/runtime/profiles/` | 未寫 |
| 4. 不改寫 `sources/raw/` 原檔 | **新增五個 doc_id 目錄並置入原檔**（W-2 明令之落檔），**未改寫任何既有檔**；五件之 sha 於搬移前後全等 |
| 5. 不以 SYSRA 或規格代 037 建 leaf 母體或生成 TC | 未建、未生成。`generated/`、`batches/` 為空；`data/` 僅二份預查 TSV，其標題與內文皆標明「非母體」 |
| 6. 不自行送 DR | 未送。A-VT12 之 DR 僅列**草稿**於 §八，未寫入 `DATA_REQUESTS.md` |

本包寫入之檔：
- `features/vsm_v43/`：`feature.yaml`（改）、`ANOMALIES.md`（改）、`RECON.md`（新）、
  `data/sysra_v43_functional.tsv`（新）、`data/signal_chain_v43.tsv`（新）、
  `sandbox/base/…_ext.xlsx`（新，母本複本）、`docs/upstream/01_sources_recon.md`（新）
- 共用：`sources/raw/`（新增 5 目錄 5 檔）、`sources/extracted/`（新增 2 目錄 4 檔）、
  `sources/MANIFEST.tsv`（附加 5 列）

`docs/fw036/`、`docs/runtime/`、`scripts/`、`forms/` 之任何檔**未寫入**。

---

## 十二、下一步（阻塞順序）

1. **Pei 裁 §七之 §K（29 列 B-1）與 A-VT12 之判準** —— 停 2 之解除條件
2. **Pei 裁 E10 之比較欄改用 `body_sha8`**（或確認 R-VT6(d) 之加註不算漂移）—— 停 1 之解除條件
3. **共用腳本三項一併裁**：A-VT3（`recon.py` null guard）、A-VT7（`.docx` 抽取）、A-VT8（§F-6 判空）
4. 澄清 A-VT10（E2 判準）與 A-VT11（E9 掃描範圍）後重測該二項
5. 解 vsm_v42 之 W-0 阻塞 → 台帳重生（A-VT13）→ 本線 sha8 改自台帳讀取；
   並使 `signal_chain_v42.tsv` 產出 → 本線補 V42↔V43 差集
6. 補做段 1 之 R-P368(b) 擴充比對與 PROXI 表格抽取，重算 W-5（§十-1、§十-2）
7. P3：framework Layer 1 鎖定、profile `FW036_R1L_VSM_V43_Profile.md`、`spec_reference_template` 定案
8. 037 到齊 → 母體建檔 → Layer 2 裁 → P4
