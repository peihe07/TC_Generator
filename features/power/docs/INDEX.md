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
| 09 | 2026-08-17 | 補閘與 Phase 4 首批 | [handoff/09_phase4_batch1.md](handoff/09_phase4_batch1.md) | [upstream/09_phase4_batch1.md](upstream/09_phase4_batch1.md) | R-P66 ~ R-P72 | A-PW37 ~ A-PW39 | **部分完成 —— B1/B2/B3 完成；B4 首批 TC 暫停（下放包於 §B4 中斷，§C–§J 全缺）（7 項待裁）** |

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

### lint 現況 —— 七閘（09 包）

`scripts/lint_tcs.py`，`--self-test` 之 **22 個 TC fixture ＋ G46 全數如期**（全為合成）：

| 閘 | 條文 | 檢查 |
|---|---|---|
| G33 | R-P42(a)(b) | spec_reference 命中黑名單／內容逐字引用特徵字串 |
| G37 | R-P1 | `SWE-PM-089` 不得有 TC |
| G38 | R-P2 | tc_id 格式、唯一、單調遞增、無跳號 |
| G39 | R-P8 | priority 值域、不得與 037 Priority 一對一映射 |
| G40 | R-P35 | **（R-P68 改）** 上界每批驗、逐 leaf 驗、114 齊備時驗相等 |
| **G45** | §10.7（R-P66） | `specification_reference` 非空且符 `{spec_filename}_{section_id}` |
| **G46** | R-P69(c) | `feature.yaml` 與裁決條文一致 |

黑名單 `data/unreferenced_anchors.tsv` 814 列（tier 182 / 133 / 499，R-P70 追認）。

### Phase 4 狀態 —— **暫停，非阻斷於閘門**

R-P65 之三項開始條件**已齊備**（08 包 ACCEPT 滿足 (c)）。
**首批未執行，原因為 09 下放包於 §B4 句中中斷、§C–§J 與「上繳包必附」全缺**
（A-PW39）。§A 之七條完整無缺，已逐字抄錄；B1/B2/B3 照做，B4 暫停。
補發後可立即執行。

### `feature.yaml` 已更新（R-P69）

`spec_mode` A→**D**、`test_group` Power→**Power Management**、
`paths.*` 七份素材實際檔名全數填入、新增 `tc_id_format`。

**盤點另查出 A-PW37**：`workbook.columns` 自 `priority` 起全部錯位 ——
應為 priority **Q**、design_method **S**、functional_safety **T**、
author **AB**、remarks **AI**，且原本**完全沒有 `tc_id` 欄**（應為 **F**）。
成因：本 workbook 有兩個 `Estimated Test Time` 欄（A-PW38），
較 Privacy 之 A-PV13 修訂版又多插入一欄。已依實測更新。

### DATA_REQUESTS（live 5 張）

DR-PW1（High，阻斷 `SWE-PM-089`）、DR-PW5（High）、DR-PW6（Medium）、
DR-PW3（Medium）、DR-PW7（Low）。

### 待裁 7 項（見 [upstream/09_phase4_batch1.md](upstream/09_phase4_batch1.md) §七）

- **Q1（阻斷 Phase 4）請補發 09 下放包之 §B4 後半與 §C–§J**
- **Q2（Phase 4 寫回前必須解決）應補設 `workbook.columns` 與 FW036 r9 之一致性閘**
  —— 本次錯位靠盤點偶然查出，非靠閘門；寫回不可逆
- Q3 A-PW37 之欄位更新請覆核
- Q4 A-PW38：兩個標頭逐字相同之 `Estimated Test Time` 欄，何者為權威
- Q5 `done_region.author_value: "Arif"` 是否改為留空（Comfort 之作法）
- Q6 `write_back.fill_test_group_set` 與其註解矛盾
- **Q7 `specification_reference` 之 `{spec_filename}` 實際寫法為何** ——
  G45 繫於此；若猜錯會把每一條合法 TC 判 FAIL

### 長期已知限制（非待辦）

**Layer 3 之邊界由 SYS2 收錄規則決定，非獨立界定。** R-P7 裁定不追 SYS2 收錄規則，
R-P37 停止章節層調查 —— 二者合起來即：本 feature 之規格涵蓋範圍由上游決定。
若日後有人問「為什麼某章沒有 TC」，正確答案是 R-P7，不是 Layer 3。
見 [upstream/05_testset_lock.md](upstream/05_testset_lock.md) §八之一。

### 尚未進入

Phase 4 以降全部未開始。FW036 workbook 為 BLANK（G10），無任何寫回動作發生過。
