# G136 —— 字串樣式變體檢查（R-P201(c)）

## 1. `SWE-PM-014` 之獨立重掃（B4 明令）

| leaf | 容忍空白之樣式命中 | 嚴格樣式命中 | 原文之逐字形態 |
|---|---|---|---|
| `SWE-PM-014` | **1** | 0 | `Brand_Configuration _2` |
| `SWE-PM-026` | **1** | 1 | `Brand_Configuration_2` |
| `SWE-PM-053` | **1** | 1 | `Brand_Configuration_2` |
| `SWE-PM-054` | **1** | 1 | `Brand_Configuration_2` |
| `SWE-PM-101` | **1** | 1 | `Brand_Configuration_2` |

**`SWE-PM-014` 實測：容忍空白之樣式命中 1、嚴格樣式命中 0，原文形態為 `Brand_Configuration _2`。**

**即 R-P201 之訂正經執行層獨立重掃確認** —— 26 包之「0 次」係掃描樣式未涵蓋空白變體所致，`source_clause` 確實載有該參數，**§8.4.2 未越界**。

## 2. 逐腳本之變體涵蓋情形

| 腳本 | 空白 | 大小寫 | 全半形 | 依據 |
|---|---|---|---|---|
| `build_reconciliation.py` | 不適用 | 不適用 | 不適用 | 以 TSV 欄位值精確比對，無樣式匹配。 |
| `g113_buckets.py` | **已涵蓋** | **已涵蓋** | 不適用 | `_STRIP_RES` 三式明訂大小寫敏感與否（27 包前已因 `Door` 內之 `or` 訂正過邊界）；`ILLUSTRATIVE_RE` 用 `re.I`。 |
| `lint_tcs.py` | **已涵蓋** | 部分 | 未涵蓋 | G82 於 27 包加 `_fold_ident()` 摺除識別子內之空白（R-P201(c)）；`ENV_STABILITY_RE` / `PRECOND_ACTION_RE` / `MISREAD_TERMS` 用 `re.I` 故大小寫已涵蓋，而 `ER_PROPER_RE` **刻意大小寫敏感**（其判準即為「大寫識別子」，不得放寬）；全半形未處理 —— 語料為英文規格，全形字元僅見於引號（`“”`），而引號不參與標的比對。 |
| `or_branch_coverage.py` | **已涵蓋** | **已涵蓋** | 不適用 | `GLUED_OR_RE` 專為黏連（缺空白）而設；`OR_TOKEN_RE` 明列大小寫二式；`LEFT_STOP_RE` / `RIGHT_STOP_RE` 用 `re.I`。比對對象為連接詞，非全形。 |
| `renumber_tc_ids.py` | 不適用 | 不適用 | 不適用 | 只重寫 `tc_id`，無樣式匹配。 |
| `reverse_coverage.py` | **已涵蓋** | **已涵蓋** | **已涵蓋** | `normalize()` 轉 NBSP / thin space；`words()` 一律 `.lower()` 後詞幹化。 |
| `scan_clause_patterns.py` | **已涵蓋（27 包修正）** | **已涵蓋** | 未涵蓋 | 原 `APPLICABILITY` 為逐字比對而未摺空白，`Brand_Configuration_2` 無法命中原文之 `Brand_Configuration _2`。27 包加 `_fold()`（R-P201(c)）—— **修正方向為增加發現（對執行層不利），依 R-P187 自行修正並回報**：G132 之 leaf 數 **40 → 40 不變**（`SWE-PM-014` 原已由 `Jeep` / `LTM High` 命中），惟其命中詞由 2 增為 3。比對時 `.lower()` 故大小寫已涵蓋；全半形未處理。 |
| `verify_multivalue_sets.py` | **已涵蓋** | **已涵蓋** | 未涵蓋 | `as_set()` 去空白並 `casefold()`（R-P173(a)）。全半形未處理。 |
| `verify_reasoning.py` | 不適用 | 不適用 | 不適用 | 只量長度與非空，無字串樣式比對。 |
| `verify_source_clause.py` | **已涵蓋** | 不適用 | **已涵蓋** | `normalize()` 摺連續空白並轉 NBSP / thin space；**大小寫刻意不正規化**（R-P125(a) 明令「不做大小寫正規化 —— 那些差異是真差異」）。 |

**未列入判定之腳本（37）**：`assess_reasoning.py`、`assign_final_tc_id.py`、`audit_pattern_variants.py`、`build_anchor_attributes.py`、`build_arif_final_step.py`、`build_b1.py`、`build_b2.py`、`build_b3.py`、`build_b4_b5.py`、`build_b4_material.py`、`build_b4_signals.py`、`build_b5_material.py`、`build_blacklist.py`、`build_dangling.py`、`build_dangling_rulecheck.py`、`build_er_restatement.py`、`build_false_positive.py`、`build_final_step.py`、`build_layer3.py`、`build_ole_census.py`、`build_precond_verbs.py`、`build_residual_sample.py`、`build_swepm025_triggers.py`、`build_template_diff.py`、`build_testsets.py`、`build_vcvm.py`、`check_edit_integrity.py`、`dryrun_write_back.py`、`extract_textlayer.py`、`gen_batch04.py`、`gen_batch05.py`、`gen_batch06.py`、`verify_anchor_set.py`、`verify_gates.py`、`verify_gates_03.py`、`verify_layer3.py`、`verify_writeback_path.py`
—— 皆為建表 / 產生器類（`build_*` / `gen_*` / `dryrun_*`），其字串比對僅用於自身之欄位鍵名，不涉規格原文之樣式匹配。
