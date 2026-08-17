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

### 閘門現況（06 包）

PASS：G0–G16、G13b（46）、G18–G23、G27、**G31**
基線／填空：**G24**（二份 CFTS 皆零嵌入物件；31 處懸空參照 / 16 章）、
**G25**（EE Architecture）、**G26**（相異值）、
**G28**（VC 單欄 2/115 不可執行、VM 0/115、**二欄合觀 0/115**）、
**G29**（懸空參照影響 2 錨點 / 9 leaf / 1 Test Set）、**G30**（CFTS010 上界 = 0）
**已移除**：G17（R-P37，自 06 包起）、G11（R-P14(b)）、G6（R-P18 拆分）

### DATA_REQUESTS（live 5 張）

| DR | Urgency | 摘要 |
|---|---|---|
| DR-PW1 | High | `SWE-PM-089` 上游來源 —— 阻斷該 leaf |
| DR-PW5 | High | §1.6.2.1.4 之否定需求由誰承接（範圍內而未涵蓋） |
| DR-PW6 | Medium | 31 處懸空 `WrapperResource` —— 影響 `SWE-PM-001`–`009` 九個 leaf |
| DR-PW3 | Medium | `4942087` 歸屬 —— 不阻斷 |
| DR-PW7 | Low | VC 欄品質（2 筆）—— 不阻斷 |

### 待裁 6 項（見 [upstream/06_scope_boundary.md](upstream/06_scope_boundary.md) §九）

- **Q1（最重）Phase 4 lint 是否增設 R-P42 執行期閘門** ——
  A-PW27 之 13 個未被引用錨點即現成黑名單；現況條文有而執行期驗證無
- Q2 B1 之歸屬規則是否需獨立驗證（31/31 之 100% 歸屬率可疑）
- Q3 A-PW29：EE Architecture 分布與 R30-3/R30-4（車型欄留白）之併存
- **Q4 §六之檔案損傷請覆核** —— `01_intake.md` 除本包三處改動外應無其他變動
- Q5 G28–G30 之基線是否寫回腳本成為回歸閘
- Q6 三張 DR 之 Urgency 判定是否認可

### 長期已知限制（非待辦）

**Layer 3 之邊界由 SYS2 收錄規則決定，非獨立界定。** R-P7 裁定不追 SYS2 收錄規則，
R-P37 停止章節層調查 —— 二者合起來即：本 feature 之規格涵蓋範圍由上游決定。
若日後有人問「為什麼某章沒有 TC」，正確答案是 R-P7，不是 Layer 3。
見 [upstream/05_testset_lock.md](upstream/05_testset_lock.md) §八之一。

### 尚未進入

Phase 4 以降全部未開始。FW036 workbook 為 BLANK（G10），無任何寫回動作發生過。
