# 上繳包 02 — vsm_v42：W-0～W-6 全數執行

日期：2026-09-01　執行層：Claude Code　對應下放包：`docs/handoff/02_sources_recon.md`

## 結果分類（FO 之第 8.4 節）

| 分類 | 內容 |
|---|---|
| 改對了 | W-0 台帳重生（E17′ 過）；W-1′ 四鍵；W-2 sandbox 副本＋欄位逐欄回填＋sources 落檔＋`inputs/` 清空；W-3 recon；W-4 `leaves.tsv`；W-5 `signal_chain_v42.tsv`；W-6 五條新 anomaly ＋ DR-VL1 實數 |
| 核實無誤 | E1–E25 之 23 項相符（E23′ B-1 = 0；E19–E22、E24、E25 全過）；A-VL1／A-VL3 之解除條件逐項實測後轉 RESOLVED |
| 正確地不動 | 037×2 與 SYSAD 三檔與 `vsm_v43` 已落者 sha 全等 → **不重落**；`--refresh-manifest` **未用**（手工附加 2 列）；台帳於 W-0 後**不再重生**（R-VT11／R-VT12 於本包執行中落地，見第 11 節丁）；`scripts/` 一律未改（02 包第 4 節「裁前不改」） |

**總判：本包七步全數完成，無停下條件觸發。**

---

## 0. W-0 台帳重生（R-VL9／判準 R-VL10(b)）

前置：`git status --short docs/fw036/RULINGS.sha.tsv` → **空（乾淨）**。
Pei 於本包執行前入庫 commit **`b6668f4`**，含三檔：`RULINGS.sha.tsv`、
`FEATURE_ONBOARDING.md`、`RULINGS_LEDGER.md`。

> **入庫範圍之判定（執行層先行查證後回報）**：單獨提交 `RULINGS.sha.tsv` 不可行 ——
> 其待入庫列含 `R-G42`，而該條**錨點只在 working 版 `FEATURE_ONBOARDING.md`**，
> `HEAD` 版無（`git show HEAD:… | grep -cE "^#{2,4} *R-G42"` → 0；working → 1）。
> 只提交台帳會登記一條正文不在庫之條文。`R-G29` HEAD 已有；
> `R-ICS45`–`R-ICS58` 之錨點檔 `features/ics_management/RULINGS.md` 已入庫且乾淨。

重生：`python3 scripts/rulings_hash.py` → 寫入 683 錨點（group 10／report 12／
ruling 652／superseded 9），來源 19 檔。

### E17′ 判準（性質，非數值）

| 判準 | 實測 | 判 |
|---|---|---|
| 新增列之 `ruling_id` 全數 ∈ {`R-VL*`, `R-VT*`} | **21 列全數符合**（非 R-VL/R-VT 之新增列 = **0**） | **過** |
| 修改列 | **0** | **過** |
| 刪除列 | **0** | **過** |
| 條數（觀測值，非門檻） | R-VL **11**（R-VL1–R-VL11）＋ R-VT **10**（R-VT1–R-VT10）＝ **21** | 觀測 |

新增列逐一：`R-VL1 R-VL2 R-VL3 R-VL4 R-VL5 R-VL6 R-VL7 R-VL8 R-VL9 R-VL10 R-VL11`
`R-VT1 R-VT2 R-VT3 R-VT4 R-VT5 R-VT6 R-VT7 R-VT8 R-VT9 R-VT10`。

> R-VL10(b) 之改判**當場即生效用**：上繳 01 之數值判準「14」在本包執行時已是 21，
> 若仍用數值判準則本包會第三度停在 W-0。

### E18′ —— `body_sha8` 逐條比對（R-VL10(a)）

| 條號 | 上繳 00 第 9 節／上繳 01 第 9 節所報 `body_sha8` | 本包自台帳讀出 | 判 | `sha8`（觀測值） |
|---|---|---|---|---|
| R-VL1 | `5897969a` | `5897969a` | **同** | `2a3dd0b6` |
| R-VL2 | `01c67a04` | `01c67a04` | **同** | `582d0c6d` |
| R-VL3 | `e306aa75` | `e306aa75` | **同** | `ec287e40` |
| R-VL4 | `08cea35e` | `08cea35e` | **同** | `49be4fb8` |
| R-VL5 | `1de01344` | `1de01344` | **同** | `482a6990` |
| R-VL6 | `7321474a` | `7321474a` | **同** | `bba2d813` |
| R-VL7 | `afb452ed` | `afb452ed` | **同** | `30ba05fa` |
| R-VL8 | `3c02775c` | `3c02775c` | **同** | `762824c8` |
| R-VL9 | `5a0230ee` | `5a0230ee` | **同** | `67a2d29b` |

**9／9 逐字相同，E18′ 過。** R-VL2 之 `sha8` 仍為 `582d0c6d`（加註後之現值，非漂移）。

### R-VL10／R-VL11 之 sha8（第 6 節上繳要求）

| 條號 | **`body_sha8`** | `sha8`（觀測值） | body_kind | 行 |
|---|---|---|---|---|
| R-VL10 | **`6ced1b1f`** | `b78694ad` | fenced | 165 |
| R-VL11 | **`13a4dfcd`** | `7689b41c` | fenced | 178 |

十一條 R-VL 皆為 `fenced` 本體（R-G29 之要求），無 `section` 型。

---

## 1. W-1′ —— `feature.yaml` 四鍵實值

| 鍵 | 值 | 依據 |
|---|---|---|
| `tc_id_prefix` | **已刪除**（`'tc_id_prefix' in yaml` → `False`） | R-VL7 |
| `write_back.tc_id_format` | `"NR1L-VSM42-{n:03d}"` | R-VL7（R-VL3 之值不變） |
| `done_region.author_value` | `null`（Python `None`） | R-VL8(c) |
| `spec_reference_template` | `null`，附註「待 P3 裁（VF 類母件之 IN §10.7 型態未定）」 | R-VL11(c) |

---

## 2. W-2 —— sandbox、欄位、sources 落檔

### 2.1 sandbox/base（R-VL8(a)）

`features/vsm_v42/sandbox/base/` 建立，自 `forms/` 之 R-G1 母本以 `cp` 落副本。

| 項 | 實測 | 判 |
|---|---|---|
| `cmp` 母本 ↔ 副本 | exit 0（全等） | **E19 過** |
| 副本 sha256 | `6372fb6be02f48dc3a3e091a60d2e2b3cf26d8704c27e25d79b7c9516fb825b2` | 與 E19 所載**逐字相同** |
| zip members | 48 | 完整（R-G1 註：openpyxl 存回會使其變 47） |
| `x14:dataValidation` | **1** | 完整（R 欄 design_method 之擴充下拉未毀） |

**自始未以 openpyxl 存回該副本**（本包對它只做 `read_only=True` 之讀取）。

### 2.2 欄位逐欄實測 vs 先驗（R-VL8(b)）

自副本分頁 `Test Case Specification 測試用例規範` 第 9 列逐格讀取（openpyxl
`read_only=True, data_only=True`，取非空值），**非沿用上繳 01 對母本之測值**。

| 先驗（R-VL8(b)） | 副本實測 | 判 |
|---|---|---|
| sheet `Test Case Specification 測試用例規範` | 分頁清單第 6 個，逐字相同 | **相符** |
| priority = P | `P9 = 'Test Case Priority\n測試用例優先級別'` | **相符** |
| estimated_test_time = Q | `Q9 = 'Estimated Test Time (mins)…'` | **相符** |
| **design_method = R** | `R9 = 'Test Case Design \nMethods\n測試用例設計方法'` | **相符（E20 過）** |
| functional_safety = S | `S9 = 'Functional Safety\n功能安全'` | **相符** |
| **author = AA** | `AA9 = 'Test Case Author\n測試案例作者'` | **相符（E20 過）** |
| test_version = AB | `AB9 = 'Test Version\n測試版號'` | **相符** |

回填 `feature.yaml` 之全集（21 ＋ 7 ＋ 5 = 33 鍵）：

- `columns`（21）：`no` B／`polarion_id` C／`req_id` D／`testrail_id` E／**`tc_id` F**／
  `test_group` G／`test_set` H／`test_item` I／`pre_conditions` J／`input_test_data` K／
  `test_procedure` L／`expected_result` M／`spec_reference` N／`tc_ref_id` O／
  `priority` P／**`estimated_test_time` Q**／`design_method` R／`functional_safety` S／
  `author` AA／`test_version` AB／`remarks` AH　（粗體二鍵為 R-VL11(b) 所增）
- `variant_columns`（7）：T HDCC27 Atl-Hi／U DT27 Atl-Hi／**V `VF(ProMaster)637 Atl-Mi`（本線）**／
  W Commander (598)／X Regengade (5210)／Y Toro(2261)／Z Fastack (376)
- `execution_columns`（5）：AC Test Vehicle (Bench)／AD Test Period／AE Tester／
  AF Test Result／AG Defect ID

**scaffold 模板三處錯值已全數不採**：`sheet` `Test Case Specification&Result`（該名不存在）、
`design_method` `Q`（實為 R；Q 是 estimated_test_time）、`author` `Z`（實為 AA；
**Z 是車型欄 `Fastack (376) Atl-Mi`** —— 若沿用，作者名會寫進車型欄）。

### 2.3 sources 落檔（R-G27／R-VL11(a)）

**新落 2 個 doc_id**（以 `mv`，非 cp+rm）：

| doc_id | 檔名 | mv 前 sha256 | mv 後 sha256 | 判 |
|---|---|---|---|---|
| `vf665_v42_spec_r6` | `Vehicle_Setup_Management_by_VP_-_LTM_(R1_Low)_VF665_V42_R6.docx` | `148956e9ccf77620dbc0e500971d7c8a59bf19352b88e4eed2b0cf4c8416ba99` | 同左 | **全等** |
| `vf665_v42_sysra` | `FM-WI-FSM-035-A02_VF665_V42_STLA 技術安全需求分析報告_SYSRA STLA Vehicle Setup Management Requirement Analysis Report_SYSRA_VF665_V42_Released.xlsx` | `72411efdd597482bc1b3bb394dbba002107feb27dca33bd6934b46008668994c` | 同左 | **全等** |

**既有 3 個 doc_id —— sha 比對後不重落**（02 包第 3 節之條件分支「相同 → 不重落」）：

| doc_id | `sources/raw/` 既有 sha256 | 本線 `inputs/` 同名檔 sha256 | 判 |
|---|---|---|---|
| `vf665_037_parksense` | `be55d8978f9472f3b7bae8643eee139525f2c455b8bddce24f3911c4128e9d05` | 同左 | **相同** |
| `vf665_037_sdw` | `c98909e2c15eb0a02e1ab99f25c4c7bd77226fbd5f29842088bbe06f9f0f2afd` | 同左 | **相同** |
| `vf665_sysad_sys3` | `469162b81bf3101855089feb87b4a155d4ce867860c194d65d2a901bad08b200` | 同左 | **相同（E21 過）** |

三者之 MANIFEST `features` 欄實測已含 `vsm_v42`（值為 `vsm_v42;vsm_v43`，
分隔符為 **`;`** 非 `,`）。三檔於 `cmp` 全等**重新確認後**自 `inputs/` 刪除
（刪前重算，不憑先前之 sha）。

**MANIFEST 手工附加 2 列，`--refresh-manifest` 未使用**（02 包明令；其會重寫全檔並
抹掉既有 `version`／`features`／`note`）。附加後資料列 8 → **10**。

| 檢 | 預期 | 實測 | 判 |
|---|---|---|---|
| **E24** `inputs/` 於 W-2 後 | 0 項 | **0**（`ls -A` 與 `find -mindepth 1` 二法皆 0） | **過** |
| **E25** MANIFEST 含 `vsm_v42` 之列 | 5 | **5**（`vf665_sysad_sys3`／`vf665_037_parksense`／`vf665_037_sdw`／`vf665_v42_spec_r6`／`vf665_v42_sysra`） | **過** |

### 2.4 `sources/extracted/`

- `vf665_v42_sysra`：`extract_source.py --doc-id vf665_v42_sysra` → **6 份 tsv**
  （封面 30 行／修訂履歷 17／Product Document 記錄封面頁 16／
  **Analysis Report 1045 行、非空格 15,640**／Instructions 53／下拉選單設定處 78）。
  **§F-6 誤報型（A-VT8）未觸發**，無座標可記。
- `vf665_v42_spec_r6`：`extract_source.py` 不支援 `.docx`（A-VT7），依 02 包
  自 raw 直讀 `word/document.xml`，產 `document_paragraphs.tsv`（1,744 段，非空 1,631）
  與 `document_tables.tsv`（6 表 40 列）。
  > **抽取自驗（R-VT11 型）**：初版 `<w:t[^>]*>` 之正規式會誤匹 `<w:tab .../>`，
  > 致 57／59／61 等段落內容變成 XML 屬性字串。已改為 `<w:t(?: [^>]*)?>` 並重產；
  > 誤版之 `.txt` 已刪除，未流入下游。**此為本包自查所得，非下放包所指**。

### 2.5 E22 與 R-G28

| 檢 | 實測 |
|---|---|
| **E22** `#1` docx magic bytes | `50 4B 03 04`（`xxd -l 4` → `504b 0304`）→ **OOXML，過** |
| zip members | **25**；頂層分布 `[Content_Types].xml` 1／`_rels/` 1／`word/` 9／`docProps/` 3／`[trash]/` 2／`customXml/` 9 |
| **`word/embeddings/`** | **0 項** |
| **`word/media/`** | **1 項** = `image1.wmf`（498,222 bytes） |
| `word/charts/`／`word/drawings/` | 0 項／0 項 |

**「由圖找列」**：`image1.wmf` 以 `r:embed="rId5"` 嵌於**段落 60**，
其上一段（59）為標題 `Functional Diagram` ——
**即該節之內容全在圖內，docx 文字層於該處為空**。
以 `soffice --convert-to svg` 轉為向量 SVG（文字仍為文字），自 `<tspan>` 依 y／x
座標還原為 **240 行**，落 `sources/extracted/vf665_v42_spec_r6/media/image1_text.tsv`
（另存 `image1.svg`／`image1.png`／`image1.wmf`）。
該 240 行於 W-5 為第四來源，**單獨貢獻 158 個訊號名**。
逐圖二欄表以 `signal_chain_v42.tsv` 之 `sources` 欄含 `diagram` 取代（可篩）。
詳見 **A-VL9**。

---

## 3. W-3 recon

`python3 scripts/recon.py --feature features/vsm_v42 --root .` →
`recon complete: state=BLANK, leaves=68, sections=0, targets=68`，exit 0。

- `RECON.md` 產出；11 個 `paths.*` 鍵全數解析成功，逐檔 sha256 列於其 Inputs 段。
- `workbook_state`：**BLANK**（R-VL1 之預期）；form layout revision **C**（有 Estimated Test Time）。
- **`leaves=68` 為 recon 代表檔（Park Sense）之數，非本線母體**；母體 128 見第 4 節。
  該落差已寫入 `DECISIONS.md` 之執行層附註，避免簽核時被讀成母體。
- `DECISIONS.md`：recon 產出 `DECISIONS.new.md`（A-TM15：不覆寫既有）。
  原 `DECISIONS.md` 為 `new_feature.py` 空白模板、**無任何人為編輯**，
  故以 recon 預填本取代並附執行層附註，`DECISIONS.new.md` 移除。**未簽。**

---

## 4. W-4 leaf 母體與跨源對帳

`features/vsm_v42/data/leaves.tsv`，**152 列**（不含表頭），13 欄。

| tc_status | 列數 |
|---|---|
| `leaf`（Functional Requirement） | **128** |
| `No TC — Heading` | **23** |
| `UNCATEGORIZED` | **1** |

跨源對帳（每一 `Source Requirement ID` 於 SYSRA `Sys-RA-Feature-ID` 是否命中）：

| 項 | 實測 |
|---|---|
| 128 Functional leaf 之命中 | **128／128（E16 過）**，未命中 **0** |
| 命中列之 SYSRA `分類 Category` 回查 | Functional Requirement **127**／**Heading 1** |
| 離群列 | `SWE1-VC-SurroundCameraGridlines-063` → `Sys-RA-VF665_V42_VSM-857`（→ **A-VL7**） |
| SYSRA `Sys-RA-Feature-ID` 重複者 | **0** |

**DR-VL1 實數回填**：被 037 覆蓋之 SYSRA Functional = **127**；
未覆蓋 = 318 − 127 = **191**（原估「約 190」）。已寫入 `DATA_REQUESTS.md`。

`leaves.tsv` 逐列另帶 `sysra_category`／`sysra_chapter_for_vf`／
`sysra_ee_architecture`／`sysra_doc_id` 四欄，供 A-VL6／A-VL7 直接篩出。

---

## 5. W-5 訊號解析預查

### 5.1 抽名（三式 ＋ 表格 ＋ 圖）

四來源、五類形，去重後合計 **251 名**：

| 來源 | 貢獻名數（去重後） |
|---|---|
| `spec_paras`（docx 段落 1,744） | 228 |
| **`diagram`（WMF → SVG → 240 行）** | **158** |
| `037_desc`（兩份 037 `Requirement Description`） | 46 |
| `spec_tables`（`<w:tbl>` 6 表 40 列） | 11 |

| 類別 | 名數 | 例 |
|---|---|---|
| CAN（`MESSAGE.Signal`） | **107** | `TELEMATIC_VEHICLE_SETUP.PamAlertMode_Req`、`IPC_VEHICLE_SETUP.LanguageSelection` |
| `.Req` | **69** | `Auto_High_Beam_Enable.Req`、`Distance_Unit_Setting.Req` |
| `.Info` | **37** | `TLM_Vehicle_Setup_Menu.Info`、`EPB_MaintenanceMode_Active.Info` |
| `.GUI` | **2** | `TLM_Display.GUI`、`Server_App.GUI` |
| PROXI | **36** | `Cornering_Light`、`Rain_Sensor`、`Half_Torque_Sensibility` |

> PROXI 之抽取採三式：`"<Name>" PROXI parameter`（規格主用式）、`PROXI parameter(s) <Name>`、
> `<Name> PROXI parameter`。**只用 `PROXI\s+<Name>` 單式會漏掉絕大多數**
> —— 規格之寫法是名稱在前。此為 02 包「不只認『X PROXI parameter』句式」之落實。

### 5.2 段 1 —— forms 七檔各命中數（R-VL6(a)／R-P375(a)）

比對式（**掃描條件揭露**）：逐字 ／ 逐字（去 `.Req`_`.Info`_`.GUI` 後綴）／
擴充（忽略底線、空白、大小寫；`len(正規化值) > 3` 之守門）。

| 檔／分頁 | 涉及訊號名數 |
|---|---|
| `PROXI_HDCC27_R3` `Format` | **36** |
| LID `CAN Mapping`（名稱欄 A/B/C ＋ **`Atlantis High` 欄組 Z**） | **9** |
| LID `Proxi & Configuration`（A/B/C → P） | **6** |
| `HMI Settings List R1 SR25` `Settings` | **2** |
| **LID `637MCA Specific Signals`（名稱欄 A/B/C ＋ Signal Name D）** | **0** |
| `SR26 Default Settings and PNet ECU Configuration` `Default Parameters` | **0** |
| `SR24 R1 Market Configuration Table` `Market Config - R1` | **0** |

### 5.3 R-VL6(c) 之二欄組實測（不自選、不合併）

| 欄組／分頁 | 命中名數 |
|---|---|
| `Atlantis High` 欄組（LID `CAN Mapping`） | **9** |
| `637MCA Specific Signals` 分頁 | **0** |
| **兩者皆命中** | **0** |

**結論**：R-VL2 末段所留之「段 1 應取何欄組」在本線為**空問題** ——
637MCA 分頁（22 列，E15）與本線 251 個訊號名**無任何交集**。
**本包不自選、不合併，據實登記**（A-VL8）。

### 5.4 擴充比對（R-P368(b)）之施作與一次自我撤回

嚴格比對之外，另算「前綴／後綴差異」候選：**89 個訊號名**有寬鬆候選而無嚴格命中，
存於 tsv 之 `loose_n`／`loose` 兩欄，**不驅動結果**（R-P375(d)：命中即候選，非認定）。

> **本包一次自我撤回，據實登出**：曾將「正規化後互為子字串」直接當作段 1 命中並
> 驅動段 2，結果產生 **68 筆 B-1 衝突**（CAN 形 60 筆）——
> 其為 R-P368(b) 明禁之**語意跳接**（子字串包含不是「前綴／後綴差異」，是無界比對）。
> 該版**已撤**，改為嚴格／寬鬆分欄。若未撤，E23′ 會假性判紅 68 筆並停下 W-5。

### 5.5 結果分布

`features/vsm_v42/data/signal_chain_v42.tsv`，**251 列**、11 欄
（`name`／`kind`／`sources`／`seg1_n`／`seg1`／`seg2`／`seg3`／`result`／`result_detail`／`loose_n`／`loose`）。

| 結果 | 總 | CAN(107) | Req(69) | Info(37) | GUI(2) | PROXI(36) |
|---|---|---|---|---|---|---|
| 解得 | **35** | 33 | 0 | 1 | 0 | 1 |
| 未解得(止於段1) | **105** | 0 | 68 | 33 | 2 | 2 |
| 未解得(止於段2) | **48** | 47 | 1 | 0 | 0 | 0 |
| 查無(R-G13) | **0** | 0 | 0 | 0 | 0 | 0 |
| **B-1 衝突** | **0** | 0 | 0 | 0 | 0 | 0 |
| 訊息名不符(R-13) | **27** | 27 | 0 | 0 | 0 | 0 |
| UI路徑(R-P375b) | **1** | 0 | 0 | 1 | 0 | 0 |
| PROXI路徑(R-P375b/c) | **35** | 0 | 0 | 2 | 0 | 33 |

**「查無(R-G13)」為 0**：其須三要件皆滿足並登 `forms/LOOKUP_MISSES.md`（R-G14）；
本包無任何名滿足，故 **`forms/LOOKUP_MISSES.md` 未新增任何列**。
段 1 擴充比對已做，故未命中者一律記「未解得(止於段1)」而非「查無」（02 包明令）。

### 5.6 「解得 35」之內部拆分（**本包主動拆，交分析層裁**）

| 細分 | 數 | 意義 |
|---|---|---|
| **三段皆過**（段 1 亦命中） | **3** | `PrivacyMode.Info` → `TBM_SCHEDULE_FD_2.PrivacyMode`；`IPC_VEHICLE_SETUP.LanguageSelection`（LID `CAN Mapping` Z1111 逐字）；`Country_Code` |
| 段 1 未命中，段 2 = 規格原名本身已為 `MESSAGE.Signal` 形，段 3 於 DBC 逐字查得 | **32** | 依 R-P368(a) **字面**不得寫 `$...$`（三段未皆過）；依其**意旨**（DBC 實名為準）則可 |

同理「訊息名不符(R-13) 27」全為段 1 未命中者。
**本包不自行認定**，`result_detail` 欄可完整篩出兩類。裁決請求見 A-VL8。

### 5.7 §K 衝突表

| 規格原名 | 命中處 A | 解得 A | 命中處 B | 解得 B | 交 Pei 之問 |
|---|---|---|---|---|---|
| （空） | | | | | |

**本表為空之語意是「已查、查無衝突」**（W-5 已執行；E23′ = 0），
**不是上繳 01 之「未查」**。

---

## 6. 預期數字逐項對照（E1–E25）

**掃描條件揭露**：037 兩檔分頁 `Analysis Report`，parksense 表頭列 **7**、sdw 表頭列 **8**，
母體＝`SWE-Requirement ID` 非空之列；`Categorization` 為 F 欄、`Source Requirement ID` 為 B 欄。
SYSRA 分頁 `Analysis Report`，表頭列 **5**，資料列＝任一欄非空；
`分類 Category` 為第 10 欄（J）、`EE Architecture` 第 7 欄（G）、`文件識別碼 Document ID` 第 6 欄（F）。
全等比對一律 `str.strip()` 後逐字（**註**：Python `str.strip()` 亦去 `\xa0`，
故 00 包所述「含 `\xa0` 前導之變體」在本測法下與其正規形合併，見第 6 節末）。

| # | 項 | 預期 | 實測 | 判 |
|---|---|---|---|---|
| E1 | #3 有 SWE id 列數 | 82 | **82** | **相符** |
| E2 | #4 有 SWE id 列數 | 70 | **70** | **相符** |
| E3 | Functional leaf 合計 | 128 | **128**（68 ＋ 60） | **相符** |
| E4 | Heading 合計 | 23 | **23**（13 ＋ 10） | **相符** |
| E5 | `Categorization` 空列 | 1 | **1**（parksense，`SWE1-VC-IntelligentSpeedLimiterwithConfirmation-051`） | **相符** |
| E6 | Functional Source ID 去重 | 128 | **128**（兩檔交集 **0**） | **相符** |
| E7 | SYSRA 資料列 | 1040 | **1040** | **相符** |
| E8 | SYSRA Functional | 318 | **318**（另 Information 557／Heading 109／Out of Scope 56） | **相符** |
| E9 | SYSRA Functional 之 EE 空 | 112 | **112**（另 ATL-Mi 206） | **相符** |
| E10 | SYSRA DocID `VF665_V42_P637MCA` | 791 | **791**（另空 249） | **相符** |
| E11 | 037 描述內 CAN 訊號名（`[A-Z_]+_VEHICLE_SETUP\d*\.\w+`，不去重） | 71 ＋ 70 | **71 ＋ 70** | **相符** |
| E12 | 037 描述內 `PROXI`（不分大小寫） | 48 ＋ 23 | **48 ＋ 23** | **相符** |
| E13 | 037 描述內 `\$[A-Za-z_]+\$` | 14 ＋ 16 | **14 ＋ 16** | **相符** |
| E14 | LID `CAN Mapping` 三詞命中列 | 65 | **65** | **相符** |
| E15 | LID `637MCA Specific Signals` 非空列 | 22 | **22** | **相符** |
| E16 | 037 之 E3 ↔ E8 命中 | 128 | **128／128**，未命中 0 | **相符** |
| E17′ | W-0 diff 性質 | 全 ∈{R-VL*,R-VT*}／修改 0／刪除 0 | **符合**（21 列，非 R-VL/R-VT 之新增 0） | **過** |
| E18′ | R-VL1–R-VL9 `body_sha8` | 逐字相同 | **9／9 相同** | **過** |
| E19 | sandbox 副本 sha256 ＋ cmp | `6372fb6b…825b2`，cmp 全等 | **逐字相同；cmp exit 0** | **過** |
| E20 | 副本 r9 design_method／author | R／AA | **R／AA**（另 5 項先驗亦全中） | **過** |
| E21 | #5 SYSAD sha256 = `469162b8…` | 相同 | **相同** | **過** |
| E22 | #1 docx magic bytes | `50 4B 03 04` | **`50 4B 03 04`** | **過** |
| E23′ | B-1 衝突列 | 0 | **0** | **過** |
| — | 觀測值：`訊息名不符(R-13)` 列數 | （觀測） | **27** | 觀測 |
| E24 | `inputs/` 於 W-2 後 | 0 項 | **0** | **過** |
| E25 | MANIFEST 含 `vsm_v42` 之列 | 5 | **5** | **過** |

**E1–E25 全數相符／過，無不符項。**

> **一項量測條件之揭露（非不符）**：00 包第 3 節記 037 之 `Verification Method`
> 有「三種值（含 `\xa0` 前導之變體）」。本包以 `str.strip()` 正規化後實測為
> **兩種非空值**（`1. Peer review…5. System Validation` 96 列；
> `1. Software Validation…3. Integration test.` 32 列）＋ 空字串 14 ＋ `None` 10。
> Python 之 `str.strip()` 會去除 `\xa0`（其 `isspace()` 為真），故該變體與其正規形
> **在本測法下合併**。此為**測法差異，非資料差異**；若分析層要保留變體之可見性，
> 須改用 `strip(' \t\r\n')`。**本包不改判，據實揭露。**

---

## 7. W-6 —— anomaly 與 DR

### 新開 anomaly（五條，A-VL5–A-VL9）

| 編號 | 標題 | 阻塞 | 成對 DR |
|---|---|---|---|
| A-VL5 | 037 之 1 列 `Categorization` 為空 | no | 無（併 DR-VL1 或另開，待裁） |
| A-VL6 | SYSRA Functional 318 中 112 列 `EE Architecture` 為空（與 DocID 空之 112 為同一批） | no | 無（同上） |
| A-VL7 | 037 一 Functional leaf 之 Source ID 於 SYSRA 為 `Heading` | no | 無（同上） |
| A-VL8 | 段 1 對本線 CAN 名幾近全不命中；`637MCA Specific Signals` 命中 0 | **是（對 TC 之 `$...$` 書寫）** | 無 |
| A-VL9 | 母 spec 之 Functional Diagram 為 WMF 圖，訊號名不在文字層 | no | 無 |

**五條皆未成對開 DR**，理由同 A-VL1／A-VL3 之已裁可型：
DR 送出權屬 Pei（禁區第 6 條），執行層代擬 DR 違 FO 第 8.5 節之一。
**A-VL5／A-VL6／A-VL7 三者實為同一上游詢問之三面**（037 與 SYSRA 之標註完整性），
建議併入 DR-VL1 一次送出，或開 DR-VL2 統包 —— **交分析層裁，本包不自擬**。
**這是刻意之不成對，非漏做。**

### 轉 RESOLVED（二條）

| 編號 | 解除依據 |
|---|---|
| A-VL1 | 原檔 5 件到齊並落 `sources/raw/`，`inputs/` 清空 0 項（E24）。**附記落差**：原檔實際投遞於 `features/vsm_v42/inputs/` 而非 R-VL5 所定之 `_intake/Vehicle_Setup_VF665/`（該投遞區至今仍 0 files）；R-VL5 是否改寫交分析層 |
| A-VL3 | Pei 入庫 `b6668f4` 後台帳乾淨；E17′／E18′ 依 R-VL10 之新判準雙過 |

### 未結 DR

| DR | 項目 | 阻塞 | 狀態 |
|---|---|---|---|
| DR-VL1 | V42 SYSRA Functional 318 列中 **191** 列無 037 覆蓋（實數已回填） | no | 已登記，未送出 |

本包**未送出任何 DR**（禁區第 6 條）。

---

## 8. 獨立判斷：本包是否仍有該驗而未驗者

1. **有一項，且已在本包補做**：docx 文字抽取之正規式誤匹 `<w:tab>`（第 2.4 節）。
   下放包未指示自驗，是 R-VT11 之型態於本線之重演；本包自查後重產，誤版未流入下游。
2. **有一項未做，且指得出理由**：Functional Diagram 之**拓樸**（方塊與連線之流向）
   未被文字化 —— 訊號**名**已得 158 個，**誰送給誰**未得。
   若 TC 需驗因果方向（R-P353 之上游事件 → 下游效果），須另讀圖。
   本包**不臆測方向**（IN §8.4.1）。已記於 A-VL9。
3. **一項量測面之提醒**：E11 之 regex `[A-Z_]+_VEHICLE_SETUP\d*\.\w+` 只認
   `*_VEHICLE_SETUP*` 家族；W-5 之 CAN 抽名沿用同族式，故
   **非 `_VEHICLE_SETUP` 家族之 CAN 訊號（如 `STATUS_*`、`TBM_*`）不在 107 之內**，
   除非它們另以 `.Req`/`.Info` 形或於 LID 解出而入表。
   若母體之 TC 需驗此類訊號，抽名範圍須擴 —— **交分析層裁，本包不自行擴**。
4. **一項在本包範圍外但已具名**：`recon.py` 產出之 `DECISIONS.new.md` 第 3 行
   含裸 `§4`（`FEATURE_ONBOARDING §4`），為 canon_refs 之 ambiguous 來源，
   與 `new_feature.py` skeleton 之裸 `§3` 同型。已併入第 11 節甲之清單，
   屬 02 包第 4 節「共用腳本一裁」之範圍，**裁前不改**。

---

## 9. `python3 scripts/gate_all.py` 輸出

```
PASS      exit 0   lint_docs036     docs_structure：PASS（台帳＋power 之 DR／ANOMALIES）
**FAIL**  exit 1   canon_refs       FAIL: unresolved + ambiguous = 503
**FAIL**  exit 1   rulings_hash     FAIL: docs/fw036/RULINGS.sha.tsv 與現行條文不符
**FAIL**  exit 1   gates_tsv        FAIL: docs/runtime/GATES.tsv 與現行閘登錄不符
**FAIL**  exit 1   lint_paths       FAIL: 基線外違規 + delivered 不符 = 4
PASS      exit 0   lint_delivery_spec PASS: 基線外判紅 0（掃 4 檔，基線 4 列）
```

### 升級說明（FO 第 8.2 節）

**(甲) `canon_refs` 503** —— 逐檔逐行歸因（`--emit-waiver` 落 scratchpad，
**未寫入 repo 之 waiver 表**），全表中路徑含 `vsm_v42` 者 **3 列**：

| source | target | line | 歸屬 |
|---|---|---|---|
| `features/vsm_v42/ANOMALIES.md` | ruling `R-G40` | 62 | **分析層**所寫之 A-VL2 內 |
| `features/vsm_v42/RUNBOOK.md` | section `§3` | 9 | **`new_feature.py` skeleton** |
| `features/vsm_v42/DECISIONS.new.md` → 現為 `DECISIONS.md` | section `§4` | 3 | **`recon.py` 模板**（新見，第 8 節第 4 項） |

上繳 01 所自改之 `00_intake_recon.md` `§9` 一列**已不復見**。
餘 500 之組成不變（unresolved 之 target 全為 `R-G31`–`R-G41`，
站點集中於 `docs/fw036/RULINGS_LEDGER.md` 與 `features/display/`）。

**(乙) `rulings_hash`** —— **本包 W-0 已重生且當時為綠**；其後轉紅之原因逐列可指：

| 新增列 | 來源 | 落地時點 |
|---|---|---|
| `R-VT11` | `features/vsm_v43/RULINGS.md:155` | **本包 W-0 之後** |
| `R-VT12` | `features/vsm_v43/RULINGS.md:170` | 同上 |

差異**恰 2 列、全為新增、修改 0、刪除 0，且全為姊妹線**。
**本包不再重生**：02 包第 3 節明定 W-0 為「本包首步、只做一次」；
於 W-6 之後再跑一次即把姊妹線在本包執行期間之落檔一併吸收，
正是 R-VL9 之前提所欲避免之交疊，且姊妹線仍在動、重生後隨時再紅。
> **結構性問題，具名交分析層**：R-VL9 定「vsm_v43 之包不再重生」，
> 而兩線同時在跑時，**任一包之 W-0 都會被對方之後續落檔追平**。
> 本包已是第二次遇到（上繳 01 為 14→21，本包為 21→23）。
> 建議：台帳重生改為**兩線皆完工後由 Pei 跑一次**，或 `rulings_hash --check`
> 對 `R-VL*`／`R-VT*` 之新增列改為告警而非判紅。

**(丙) `gates_tsv`** —— 與本線無關，先在。差異列全為 sw_update／driver_distraction／
ics_management 之閘與 canon `body_kind` 列。`features/vsm_v42/scripts/` 為空。

**(丁) `lint_paths` = 4** —— 與本線無關，先在，四筆與上繳 00／01 逐字相同。
**本線本包新增之 xlsx 為 `sandbox/base/` 一本，落點合法**（`sandbox` 在白名單內），
未進入該四筆。

**結論**：四支之中**三支先在於本線之外**（甲之 500、丙、丁），
一支（乙）為姊妹線於本包執行期間落檔所致之 2 列落後。
**無一支肇因於本包之寫入。**

---

## 10. 本包之寫入清單

| 檔／目錄 | 動作 |
|---|---|
| `docs/fw036/RULINGS.sha.tsv` | W-0 重生（**唯一一次**，R-VL9 授權） |
| `features/vsm_v42/feature.yaml` | W-1′ 四鍵 ＋ W-2 欄位 33 鍵回填 |
| `features/vsm_v42/sandbox/base/…_ext.xlsx` | 自 forms 母本 `cp`（cmp 全等） |
| `sources/raw/vf665_v42_spec_r6/`、`sources/raw/vf665_v42_sysra/` | 自 `inputs/` `mv` |
| `sources/extracted/vf665_v42_spec_r6/`（3 tsv ＋ media 4 檔）、`sources/extracted/vf665_v42_sysra/`（6 tsv） | 抽取產物 |
| `sources/MANIFEST.tsv` | 手工附加 2 列 |
| `features/vsm_v42/inputs/` | **清空**（5 件：2 件 `mv` 走、3 件 cmp 全等後刪） |
| `features/vsm_v42/RECON.md`、`data/recon.json`、`data/recon_leaf_to_section.tsv` | recon 產出 |
| `features/vsm_v42/DECISIONS.md` | 以 recon 預填本取代空白模板 ＋ 執行層附註（未簽）；`DECISIONS.new.md` 移除 |
| `features/vsm_v42/data/leaves.tsv` | W-4，152 列 |
| `features/vsm_v42/data/signal_chain_v42.tsv` | W-5，251 列 |
| `features/vsm_v42/ANOMALIES.md` | A-VL5–A-VL9 新增；A-VL1／A-VL3 轉 RESOLVED |
| `features/vsm_v42/DATA_REQUESTS.md` | DR-VL1 實數 191 回填 |
| `features/vsm_v42/docs/upstream/02_sources_recon.md`、`docs/INDEX.md` | 本上繳 ＋ 索引 |

**未動**：`scripts/`（02 包第 4 節「裁前不改」）、`docs/runtime/GATES.tsv`、
`docs/fw036/CANON_REFS_WAIVER.tsv`、`forms/`（含 `LOOKUP_MISSES.md`，**未新增列**）、
`features/vsm_v43/`、`features/vehicle_setting/`、`docs/runtime/profiles/`、
`_intake/`、`features/vsm_v42/docs/handoff/`、`features/vsm_v42/RULINGS.md`。
**git**：本包未執行任何 git 寫入指令（`status`／`diff`／`show`／`log` 為唯讀，
用於 W-0 前置與歸因）。

---

## 11. 待 Pei／分析層之六項

1. **A-VL8（阻塞 TC 書寫）**：段 1 未命中而段 3 於 DBC 逐字查得之 **32 名 CAN 訊號**，
   可否寫 `$MESSAGE.Signal$`？若否，其處置（`PENDING: DR-VL{n}` 或保留原名不加 `$`，
   R-P368(f)）。另 27 名「訊息名不符(R-13)」同須裁。
2. **A-VL5／A-VL6／A-VL7 併為一 DR 或分開**（三者同為 037／SYSRA 標註完整性）。
3. **台帳重生之結構問題**（第 9 節乙）：兩線並行時 W-0 必被追平。
   建議改為兩線完工後由 Pei 跑一次，或 `--check` 對 `R-VL*`/`R-VT*` 新增列改告警。
4. **R-VL5 之投遞區**：原檔實際落 `features/vsm_v42/inputs/`，
   `_intake/Vehicle_Setup_VF665/` 至今 0 files。R-VL5 是否改寫。
5. **共用腳本一裁**（02 包第 4 節五項）新增第 6 項：
   `recon.py` 之 `DECISIONS` 模板第 3 行裸 `§4` → `FEATURE_ONBOARDING.md §4`。
6. **W-5 抽名範圍**（第 8 節第 3 項）：非 `_VEHICLE_SETUP` 家族之 CAN 訊號
   是否納入抽名；以及 Functional Diagram 之**流向**是否需另讀圖（A-VL9）。
