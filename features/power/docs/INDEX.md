# Power — 往返索引

> 依 R-P96（Projection 立，跨 feature 適用）。每次往返一列。
> 由**執行層**於上繳時更新；分析層下放時不寫本檔。
> 建立：2026-08-17（上繳包 01）

---

## 1. 索引

| NN | 日期 | 主題 | 下放 | 上繳 | 產生之裁決 | 產生之異常 | 結果 |
|---|---|---|---|---|---|---|---|
| 01 | 2026-08-17 | Phase 0 intake（開案） | [handoff/01_intake.md](handoff/01_intake.md) | [upstream/01_intake.md](upstream/01_intake.md) | R-P1 ~ R-P8（該包步驟 5 未執行，於 02 包補抄） | A-PW01 ~ A-PW07（同上） | **停於步驟 2：素材台帳 7 份中 3 份雜湊不符（4 項待裁）** |
| 02 | 2026-08-17 | 素材重新定基（rebaseline） | [handoff/02_rebaseline.md](handoff/02_rebaseline.md) | [upstream/02_rebaseline.md](upstream/02_rebaseline.md) | R-P9 ~ R-P14；R-P3 撤回改立 R-P3′ | A-PW07 撤回；A-PW08 ~ A-PW11 | **停於步驟 7：§E leaf 分布重算不符；G6 / G12 亦不符（6 項待裁）** |
| 03 | 2026-08-17 | framework 定版所需輸入（B1/B2/B3 ＋ 四道補閘） | [handoff/03_framework_inputs.md](handoff/03_framework_inputs.md) | [upstream/03_framework_inputs.md](upstream/03_framework_inputs.md) | R-P15 ~ R-P23 | A-PW12 ~ A-PW16；A-PW03/04/05 複驗 | **PASS —— 十一步全完成，§D 十八項無 MISMATCH（8 項待裁）** |
| 04 | 2026-08-17 | framework 定版（Layer 3 全集、R-P16 撤回、SYS3 交叉比對） | [handoff/04_framework_lock.md](handoff/04_framework_lock.md) | [upstream/04_framework_lock.md](upstream/04_framework_lock.md) | R-P24 ~ R-P32；R-P16 撤回 | A-PW17 ~ A-PW20；A-PW05 訂正、A-PW03 加註、A-PW06 複驗 | **PASS —— 十四步全完成，§D 二十二項無 MISMATCH（8 項待裁）** |
| 05 | 2026-08-17 | Test Set 定版與判讀單位訂正 | [handoff/05_testset_lock.md](handoff/05_testset_lock.md) | [upstream/05_testset_lock.md](upstream/05_testset_lock.md) | R-P33 ~ R-P41（**R-P35 §E 定版**、**R-P36 條文不可變**） | A-PW21 ~ A-PW25；A-PW23 框架訂正 | **PASS —— 十二步全完成，G21–G27 無 MISMATCH（8 項待裁）** |
| 06 | 2026-08-17 | 錨點層範圍上界與懸空參照 DR | [handoff/06_scope_boundary.md](handoff/06_scope_boundary.md) | [upstream/06_scope_boundary.md](upstream/06_scope_boundary.md) | R-P42 ~ R-P51（**R-P42 錨點層範圍上界**） | A-PW26 ~ A-PW29 | **PASS —— 十二步全完成，G28–G31 無 MISMATCH；發 DR-PW5/6/7（6 項待裁）** |
| 07 | 2026-08-17 | Phase 4 前置閘門與量測工具強化 | [handoff/07_phase4_gates.md](handoff/07_phase4_gates.md) | [upstream/07_phase4_gates.md](upstream/07_phase4_gates.md) | R-P52 ~ R-P59（**R-P52 R-P42 執行期閘門**） | A-PW30 ~ A-PW32 | **PASS —— 九步全完成，G32–G36 無 MISMATCH；lint 就位（6 項待裁）** |
| 08 | 2026-08-17 | lint 閘門補齊與偽陽性量測 | [handoff/08_lint_parity.md](handoff/08_lint_parity.md) | [upstream/08_lint_parity.md](upstream/08_lint_parity.md) | R-P60 ~ R-P65（**R-P65 Phase 4 開始條件**） | A-PW33 ~ A-PW36 | **PASS —— 九步全完成，G37–G44 無 MISMATCH；lint 五閘就位（7 項待裁）** |
| 09 | 2026-08-17 | 補閘與 **Phase 4 首批** | [handoff/09_phase4_batch1.md](handoff/09_phase4_batch1.md) | [upstream/09_phase4_batch1.md](upstream/09_phase4_batch1.md) | R-P66 ~ R-P72 | A-PW37 ~ A-PW42 | **PASS —— 九步全完成；首批 9 條 TC 產出、真實檔案 lint 全閘 PASS（8 項待裁）** |
| 10 | 2026-08-17 | 欄位對應交叉驗證與首批 pilot 回覆 | [handoff/10_column_verify.md](handoff/10_column_verify.md) | [upstream/10_column_verify.md](upstream/10_column_verify.md) | R-P73 ~ R-P78 | A-PW43 ~ A-PW47 | **PASS —— 九步全完成；A-PW40 經第二來源佐證成立；首批 9→10 條全閘 PASS（8 項待裁）** |
| 11 | 2026-08-17 | 範本全屬性比對與首批全文覆核 | [handoff/11_template_verify.md](handoff/11_template_verify.md) | [upstream/11_template_verify.md](upstream/11_template_verify.md) | R-P79 ~ R-P85 | A-PW48 ~ A-PW52 | **PASS —— 十步全完成；Power DV 座標正確；查出 B 欄無編號公式（8 項待裁）** |
| 12 | 2026-08-17 | pilot 修正與閘門補強 | [handoff/12_pilot_fixes.md](handoff/12_pilot_fixes.md) | [upstream/12_pilot_fixes.md](upstream/12_pilot_fixes.md) | R-P86 ~ R-P95 | A-PW53 ~ A-PW58 | **PASS —— 十二步全完成；`Test Case Framework` 分頁實測為空、不與 §E 衝突；十條四項系統性違規全修；新增 G63–G72，G67 覆蓋率 88%** |

---

## 2. 現況

### framework 已定版

**§E 定版：Power State 63 / Startup Display 24 / Branding and Theme 16 /
Timeout Settings 8 / Power Down 3 = 114**（＋ `SWE-PM-089` 留空 = 115）。
依 **R-P35**；標題已改為「已定版（R-P35）」。
兩條待裁 leaf 已由 **R-P33**（`SWE-PM-008` → Power State）與
**R-P34**（`SWE-PM-057` → Timeout Settings）裁定。
逐 leaf 指派見 `data/leaf_testset.tsv`；驗證 `scripts/build_testsets.py`（G21/G22 PASS）。

Layer 3 全集（R-P24）：`data/layer3_full.tsv`，140 列、46 個相異章節。

### 已完成

- **素材已驗明並就位**（G0 = 7/7，五包一致）。
- **裁決台帳**：`RULINGS.md` 含 **R-P1 ~ R-P41**，編號連續無缺
  （R-P3 撤回改立 R-P3′；R-P16 由 R-P25 撤回）。
  `ANOMALIES.md` 含 **A-PW01 ~ A-PW25**（A-PW07 撤回）。
- **R-P36「裁決條文不可變」已首次適用**（G27 PASS）——
  三處加註，原文 SHA256 完全相同。此後一切訂正走註記。
- **B2 v2 已重做**（R-P38）：判讀單位改為「被引用之錨點 vs leaf」。
  九章 31 個錨點中僅 18 個被引用；**§1.6.2.1.15.1 判定由「部分涵蓋」改為「涵蓋」**。
- **嵌入物件已清點**（R-P39）：CFTS009 **零嵌入物件** ——
  `…inline.rtf WrapperResource` 是**懸空參照**，所指資源未隨文件匯出。
  合計 **31 處 / 16 章**。
- **EE Architecture 已量測**（R-P40）：238 個被引用 item 全帶此欄，
  無一落在兩世代之外；14 個為單世代專屬。
- **可重現腳本**（皆純讀取）：`extract_textlayer.py`、`build_layer3.py`、
  `build_testsets.py`、`build_b1.py`、`build_b2.py`、`build_b3.py`、
  `build_b4_b5.py`、`verify_gates_03.py`、`verify_gates.py`。

### 閃點現況

PASS：G0–G16、G13b、G18、G19、G20、**G21、G22、G23、G27**
已填空：**G24**（31 處懸空參照 / 16 章）、**G25**（EE Architecture 值域）、
**G26**（相異值 = 1 者 3 欄、≥ 100 者 4 欄）
已停止：**G17**（R-P37，自 06 包移除）
已移除：G11（R-P14(b)）、G6（R-P18 拆為 G6a/G6b）

**無 MISMATCH。**

### Phase 4 —— 首批已產出並已修正（10 條）

`features/power/generated/batch_001_power_down.json` —— **10 條 TC，3 個 leaf**
（`SWE-PM-071/072/073`，Test Set `Power Down`），tc_id `001`–`010` 連號。

依 §8.2.2 拆分：071→**4**（F1 後 Standby / Bench 再拆）、072→2、073→4。
priority **P0 ×3 / P1 ×5 / P2 ×2**（依測項內容判定，R-P8）。

**12 包四項修正（R-P86 ~ R-P89），修正前之違規率**：
`req_id` 加後綴 **10/10**、Procedure↔ER 不符 **10/10**、
環境穩定性前提 **6/10**、`input_test_data` 跨欄重複 **5/10**（A-PW53 / A-PW54）。
現全數修正：`req_id` 去後綴（G69 **10/10**）、proc↔ER 全 1:1、
六條移除環境前提、五條改 `NA`。TC 數與 leaf 數不變（修正非拆分，G70）。
**真實檔案 lint：`exit=0`、阻斷類 PASS、R-P42(b) 0 觸發，0.22 秒。**

**惟：十條之技術正確性（是否真的測到 071/072/073 所要求之行為）迄今無人覆核。**
本包所修四項皆為形式規則。見 [upstream/12_pilot_fixes.md](upstream/12_pilot_fixes.md) §七之一。

### 範本全屬性 —— 已比對（R-P79）

10 包已以 Comfort + Privacy 之已交付件佐證 `workbook.columns`（A-PW40 成立）。
11 包再比對 r9 以外之六項屬性：

- **DV：Power 之四條逐條落在自身正確欄位**（`Q` priority、`U–AA` 車型、
  x14 `S` design_method、`AG` Test Result）—— **未沿用 Comfort 座標**
- **公式：Power 0 / Comfort 592 / Privacy 11** ——
  **Power 之 B 欄無自動編號公式**（另二者帶 `IF(ISBLANK($D10),"",ROW()-9)`）。
  寫回時 No.# 欄不會自動填入 → **寫回前唯一須先裁者**
- Power 獨有：多一個 `Test Case Framework` 分頁、合併 `D5:F5`、
  條件式格式 `H10:H145` colorScale
- A-PW52：Power 之 DV 覆蓋不齊（三欄僅 2–4 列）

### A-PW46 之前提有誤（11 包 B2）

Comfort **並未決定填車型欄**：其 profile §3.9 明訂「T–Z 一律留白（Privacy R30-4）」、
`write_back.py` 將 T–Z 列入 `NEVER_WRITE`、baseline 該欄非空數為 0、
全 Comfort 腳本無一呼叫 `.save()`。
**已交付件之 466 個 `1` 非由其管線產生**（A-PW51，來源不明）。
二 feature 之政策實為一致（皆留白）。Power 依 R-P54 / R-P81 維持留白。

### Power profile 已建立（R-P82）

`docs/runtime/profiles/FW036_R1L_Power_Profile.md` ——
Power 原為八個 feature 中唯一無 profile 者（A-PW49）。
G50 之方括號豁免已改為**引用 profile §3.1 / §3.2**，
並以 `PROFILE_PATH.exists()` 為條件；G59 雙向實測。

### lint 現況 —— 十五閘

G33（R-P42 a/b）、G37（R-P1）、G38（R-P2）、G39（R-P8）、G40（R-P35）、
G45（§10.7）、G46（feature.yaml）、G50（§11，12 包併入表格檢查）、G51（§4.4）、
**G63（§6 Procedure↔ER 1:1）、G64（§4.4/§8.5 環境穩定性前提）、
G65（§4.5 input_test_data 歸屬）、G66（B 欄非空列數 = TC 列數，僅合成驗證）、
G71（workbook.columns 對 r9 實測標頭）、G72（profile §2/§3.3/§3.4/§3.7）**。

G64 之詞彙依 R-P88 取自 canon 逐字原文（§4.4 之 `HU is powered on.`、§8.5），
非憑印象；偽陽性 0。G71 使 A-PW40 之人工盤點升格為機械檢查。

**G51 之動詞判準已改以經驗基礎導出**（R-P83）：自 Comfort + Privacy 之已交付
`test_procedure` 取行首動詞，人工清單漏列 12 個；對 1823 行已交付 `pre_conditions`
之偽陽性**二者皆為 0**，故採聯集（32 個動詞）。

**findings 已分流**（R-P76）：R-P42(b) 之觸發列為「待人工裁決類」，**不使 exit=1**。
`--self-test`：**35 個 TC fixture ＋ G46 皆如期**。

**G67 profile 條款閘門覆蓋率 = 15 / 17 = 88%**（20 條中 3 條不可機械檢查）。
未覆蓋之 2 項（§3.6 estimated_time 留白、§3.8 車型欄留白）**須待寫回方能檢查**。

### 寫回狀態 —— 已知阻斷條件全部解除

R-P73（欄位對應）、R-P79（範本全屬性）、**R-P92（`Test Case Framework` 分頁）**
之阻斷條件皆已解除；R-P90（B 欄）已明寫裁定、G66 已實作。
**執行層回報：本包未再發現任何新的寫回阻斷條件；開放與否為分析層之裁決。**

寫回包設計提醒（非阻斷）：G66 迄今僅合成驗證；G67 未覆蓋之 2 項恰只能在寫回時補齊；
Power 之 `NEVER_WRITE` 須與 `feature.yaml` 逐欄對讀，勿重蹈 Comfort O 欄之矛盾（A-PW57）。

### DATA_REQUESTS（live 5 張，皆不阻斷首批）

DR-PW1（High）、DR-PW5（High）、DR-PW6（Medium）、DR-PW3（Medium）、DR-PW7（Low）。

### 11 包 8 項待裁 —— 12 包已結 6 項

| # | 事項 | 12 包處置 |
|---|---|---|
| Q1 | `B` 欄之處置 | **已裁（R-P90）**，G66 已實作（僅合成驗證）|
| Q2 | `Test Case Framework` 分頁未讀 | **已讀（R-P92 / G68）—— 非空儲存格 0，不衝突** |
| Q3 | colorScale `H10:H145` 之語義 | **未查**，依 R-P95 登記不阻斷，可與寫回並行 |
| Q4 | A-PW51 是否回報 Comfort | **已回報（R-P94）** —— `features/comfort/ANOMALIES.md` A-CF-EXT-01 |
| Q5 | §11 表格檢查補入 G50 | **已補（R-P93）**，fixture 實際觸發 |
| Q6 | profile 條款無閘門對應 | **已補 G71 / G72（R-P91）**，覆蓋率 88% |
| Q7 | Power 範本 DV 覆蓋不齊 | **登記不阻斷（R-P95）** —— 三欄依 profile 皆留空 |
| Q8 | 首批 10 條之全文覆核 | **形式面已覆核並修正；技術正確性仍未覆核**（見下）|

### 12 包新提之待驗（執行層獨立判斷，見 [upstream/12_pilot_fixes.md](upstream/12_pilot_fixes.md) §七）

- **十條之技術正確性從未被任何人覆核** —— 本包所修四項全為形式規則，這是最大缺口
- **G66 從未真正失敗過**（僅合成），依 G33 標準其「可能失敗」未獲證明
- **G64 詞彙之完備性未驗** —— 有 canon 基礎，但未證明無第三類形態
- `Test Case Framework` 為何存在、為何 Power 獨有 —— 未查，不臆測
- **A-PW58 為第四次「合成 fixture 過而真實資料抓到問題」**（首次方向為誤殺）——
  新增五閘中僅 G63 / G65 見過真實資料

### 長期已知限制（非待辦）

**Layer 3 之邊界由 SYS2 收錄規則決定，非獨立界定。** R-P7 裁定不追 SYS2 收錄規則，
R-P37 停止章節層調查 —— 二者合起來即：本 feature 之規格涵蓋範圍由上游決定。
若日後有人問「為什麼某章沒有 TC」，正確答案是 R-P7，不是 Layer 3。
見 [upstream/05_testset_lock.md](upstream/05_testset_lock.md) §八之一。

### 尚未進入

Phase 4 以降全部未開始。FW036 workbook 為 BLANK（G10），無任何寫回動作發生過。
