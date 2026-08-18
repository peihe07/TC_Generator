# G176 —— 文字樣式謂詞之形態稽核（R-P250）

> **本檔只出量測，不改任何謂詞。** 其產出為 37 包之處置清單。
> 語料分四類（TC 六欄 / `source_clause` / 識別子 / 檔案路徑）——
> **謂詞須以其自身之輸入為語料**；取其命中最多之一類為準。
> 空白摺疊**保留換行**，否則行首錨定之謂詞必然變動（量測方式之假象）。

## 一、彙總（82 個謂詞）

| 項 | 數 |
|---|---|
| **四類語料皆命中 0 —— 取不到已知應命中實例** | **7** |
| **大小寫敏感** —— 未帶 `re.I` 而加之後命中數上升 | **9** |
| **空白敏感** —— 摺疊空白後命中數變動 | **21** |

## 二、四類語料皆命中 0 者（R-P250：**不得使用**）

| 模組 | 謂詞 |
|---|---|
| `build_b1` | `PD_RE` |
| `build_b2` | `PD_RE` |
| `build_layer3` | `PD_RE` |
| `lint_tcs` | `SOURCE_CLASS_RE` |
| `verify_gates` | `PD_RE` |
| `verify_gates_03` | `PD_RE` |
| `verify_layer3` | `PD_RE` |

## 三、大小寫敏感者

> 加 `re.I` 後命中數上升，即語料中存在該謂詞抓不到之大小寫變體。
> **上升不等於應改** —— 部分謂詞刻意區分大小寫（如 `rejudge_priority` 之 `CAN` 避開英文字 “can”）。逐一裁決屬 37 包。

| 模組 | 謂詞 | 語料 | 現行 | 加 `re.I` | 增幅 |
|---|---|---|---|---|---|
| `lint_tcs` | `ER_PROPER_RE` | 文字層 | 31324 | 128707 | **+97383** |
| `audit_precond_state` | `MODE_RE` | 文字層 | 12538 | 69022 | **+56484** |
| `build_template_diff` | `COL_RE` | 文字層 | 96746 | 151772 | **+55026** |
| `reverse_coverage` | `NAMED_RE` | 文字層 | 37005 | 69327 | **+32322** |
| `build_residual_sample` | `GLUE_RE` | 文字層 | 130 | 7022 | **+6892** |
| `or_branch_coverage` | `GLUED_OR_RE` | 文字層 | 2 | 2408 | **+2406** |
| `reverse_coverage` | `SPLIT_RE` | 文字層 | 5103 | 5842 | **+739** |
| `lint_tcs` | `SPEC_PARAM_RE` | 文字層 | 5246 | 5286 | **+40** |
| `or_branch_coverage` | `OR_TOKEN_RE` | 文字層 | 956 | 958 | **+2** |

## 四、空白敏感者

| 模組 | 謂詞 | 語料 | 現行 | 摺疊後 |
|---|---|---|---|---|
| `assign_final_tc_id` | `REQ_NUM_RE` | 識別子 | 367 | 0 |
| `audit_precond_state` | `MODE_RE` | 文字層 | 12538 | 12423 |
| `audit_precond_state` | `QUOTED_RE` | 文字層 | 2000 | 2004 |
| `build_er_restatement` | `NUM_RE` | TC | 1770 | 0 |
| `build_precond_verbs` | `LEAD_RE` | TC | 1770 | 0 |
| `build_swepm025_triggers` | `TRIGGER_RE` | TC | 49 | 1 |
| `confirm_row4` | `COND_RE` | 文字層 | 2620 | 2640 |
| `extract_textlayer` | `SEC_RE` | 文字層 | 460 | 0 |
| `g113_buckets` | `ILLUSTRATIVE_RE` | 文字層 | 32 | 46 |
| `lint_tcs` | `PRECOND_ACTION_RE` | TC | 422 | 0 |
| `lint_tcs` | `SENTENCE_SPLIT_RE` | 文字層 | 14027 | 13987 |
| `lint_tcs` | `SPEC_REF_ITEM_RE` | 識別子 | 264 | 0 |
| `lint_tcs` | `TC_ID_RE` | 識別子 | 264 | 0 |
| `or_branch_coverage` | `GLUED_OR_RE` | 文字層 | 2 | 8 |
| `rejudge_axis` | `BOUNDARY_RE` | 文字層 | 140 | 146 |
| `rejudge_axis` | `MODE_RE` | 文字層 | 2574 | 2616 |
| `rejudge_design_method` | `NO_TRANSITION_RE` | 文字層 | 98 | 144 |
| `rejudge_design_method` | `POSITIVE_RE` | 文字層 | 488 | 611 |
| `reverse_coverage` | `NAMED_RE` | 文字層 | 37005 | 37003 |
| `reverse_probe_rows` | `PARAM_RE` | 文字層 | 1893 | 1941 |
| `scan_clause_patterns` | `ENUM_RE` | 文字層 | 2654 | 2169 |

## 五、逐一

| 模組 | 謂詞 | 主語料 | 命中 | 加 `re.I` | 摺疊空白 | 已帶 `re.I` |
|---|---|---|---|---|---|---|
| `assign_final_tc_id` | `REQ_NUM_RE` | 識別子 | 367 | 0 | 0 | 否 |
| `audit_precond_state` | `BENCH_RE` | TC | 532 | 532 | 532 | 是 |
| `audit_precond_state` | `MODE_RE` | 文字層 | 12538 | 69022 | 12423 | 否 |
| `audit_precond_state` | `QUOTED_RE` | 文字層 | 2000 | 2000 | 2004 | 否 |
| `build_anchor_attributes` | `ATTR_RE` | 文字層 | 13996 | 13996 | 13996 | 否 |
| `build_b1` | `PD_RE` | TC | 0 | 0 | 0 | 否 |
| `build_b1` | `PM_RE` | 文字層 | 1260 | 1260 | 1260 | 否 |
| `build_b2` | `PD_RE` | TC | 0 | 0 | 0 | 否 |
| `build_b2` | `PM_RE` | 文字層 | 1260 | 1260 | 1260 | 否 |
| `build_b4_b5` | `EE_RE` | 文字層 | 2034 | 2034 | 2034 | 否 |
| `build_b4_signals` | `TOKEN_RE` | 文字層 | 140392 | 140392 | 140392 | 否 |
| `build_dangling` | `WRAPPER_RE` | 文字層 | 62 | 62 | 62 | 是 |
| `build_dangling_rulecheck` | `RESOURCE_RE` | 文字層 | 62 | 62 | 62 | 是 |
| `build_er_restatement` | `NUM_RE` | TC | 1770 | 0 | 0 | 否 |
| `build_er_restatement` | `WORD_RE` | 文字層 | 136282 | 136282 | 136282 | 否 |
| `build_layer3` | `PD_RE` | TC | 0 | 0 | 0 | 否 |
| `build_layer3` | `PM_RE` | 文字層 | 1260 | 1260 | 1260 | 否 |
| `build_precond_verbs` | `LEAD_RE` | TC | 1770 | 0 | 0 | 否 |
| `build_precond_verbs` | `WORD_RE` | 文字層 | 147670 | 147670 | 147670 | 否 |
| `build_residual_sample` | `GLUE_RE` | 文字層 | 130 | 7022 | 130 | 否 |
| `build_swepm025_triggers` | `TRIGGER_RE` | TC | 49 | 2 | 1 | 否 |
| `build_template_diff` | `COL_RE` | 文字層 | 96746 | 151772 | 96746 | 否 |
| `confirm_row4` | `COND_RE` | 文字層 | 2620 | 2620 | 2640 | 是 |
| `extract_textlayer` | `REQ_RE` | 文字層 | 1052 | 1052 | 1052 | 否 |
| `extract_textlayer` | `SEC_RE` | 文字層 | 460 | 0 | 0 | 否 |
| `g113_buckets` | `ILLUSTRATIVE_RE` | 文字層 | 32 | 32 | 46 | 是 |
| `lint_tcs` | `ANCHOR_ID_RE` | 文字層 | 3385 | 3385 | 3385 | 否 |
| `lint_tcs` | `BAD_BRACKET_RE` | 文字層 | 15204 | 15204 | 15204 | 否 |
| `lint_tcs` | `BAD_QUOTE_RE` | 文字層 | 37 | 37 | 37 | 否 |
| `lint_tcs` | `DATA_TOKEN_RE` | 文字層 | 130786 | 130786 | 130786 | 否 |
| `lint_tcs` | `ENV_STABILITY_RE` | 文字層 | 64 | 64 | 64 | 是 |
| `lint_tcs` | `ER_ACTOR_RE` | TC | 536 | 536 | 536 | 是 |
| `lint_tcs` | `ER_PROPER_RE` | 文字層 | 31324 | 128707 | 31324 | 否 |
| `lint_tcs` | `ER_WORD_RE` | 文字層 | 136282 | 136282 | 136282 | 否 |
| `lint_tcs` | `FINAL_STEP_INTENT_RE` | TC | 264 | 264 | 264 | 是 |
| `lint_tcs` | `IDENT_SPACE_RE` | 文字層 | 7587 | 7587 | 7587 | 否 |
| `lint_tcs` | `PRECOND_ACTION_RE` | TC | 422 | 0 | 0 | 是 |
| `lint_tcs` | `PRECOND_BEHAVIOUR_RE` | 文字層 | 988 | 988 | 988 | 是 |
| `lint_tcs` | `QUOTED_SPAN_RE` | 文字層 | 387 | 387 | 387 | 否 |
| `lint_tcs` | `SENTENCE_SPLIT_RE` | 文字層 | 14027 | 14027 | 13987 | 否 |
| `lint_tcs` | `SIGNAL_BRACKET_RE` | 文字層 | 22 | 22 | 22 | 否 |
| `lint_tcs` | `SOURCE_CLASS_RE` | TC | 0 | 0 | 0 | 否 |
| `lint_tcs` | `SPEC_PARAM_RE` | 文字層 | 5246 | 5286 | 5246 | 否 |
| `lint_tcs` | `SPEC_REF_ITEM_RE` | 識別子 | 264 | 0 | 0 | 否 |
| `lint_tcs` | `TABLE_RE` | 文字層 | 4 | 4 | 4 | 是 |
| `lint_tcs` | `TC_ID_RE` | 識別子 | 264 | 0 | 0 | 否 |
| `lint_tcs` | `TEST_QUANTITY_RE` | 文字層 | 134 | 134 | 134 | 是 |
| `lint_tcs` | `TIME_EQUALITY_RE` | 文字層 | 186 | 186 | 186 | 是 |
| `lint_tcs` | `TIME_TOKEN_RE` | 文字層 | 734 | 734 | 734 | 是 |
| `or_branch_coverage` | `GLUED_OR_RE` | 文字層 | 2 | 2408 | 8 | 否 |
| `or_branch_coverage` | `LEFT_STOP_RE` | 文字層 | 10689 | 10689 | 10689 | 是 |
| `or_branch_coverage` | `OR_TOKEN_RE` | 文字層 | 956 | 958 | 956 | 否 |
| `or_branch_coverage` | `RIGHT_STOP_RE` | 文字層 | 10689 | 10689 | 10689 | 是 |
| `rejudge_axis` | `BOUNDARY_RE` | 文字層 | 140 | 140 | 146 | 是 |
| `rejudge_axis` | `MODE_RE` | 文字層 | 2574 | 2574 | 2616 | 是 |
| `rejudge_axis` | `TIMING_RE` | 文字層 | 740 | 740 | 740 | 是 |
| `rejudge_axis` | `TOKEN_RE` | 文字層 | 149628 | 149628 | 149628 | 否 |
| `rejudge_axis` | `TRIGGER_RE` | 文字層 | 2939 | 2939 | 2939 | 否 |
| `rejudge_design_method` | `BENCH_RE` | TC | 526 | 526 | 526 | 是 |
| `rejudge_design_method` | `COND_RE` | TC | 1770 | 1770 | 1770 | 否 |
| `rejudge_design_method` | `NO_TRANSITION_RE` | 文字層 | 98 | 98 | 144 | 是 |
| `rejudge_design_method` | `POSITIVE_RE` | 文字層 | 488 | 488 | 611 | 是 |
| `rejudge_design_method` | `ROW1_RE` | 文字層 | 2 | 2 | 2 | 是 |
| `rejudge_design_method` | `ROW2_RE` | 文字層 | 32 | 32 | 32 | 是 |
| `rejudge_design_method` | `ROW5_RE` | TC | 28 | 28 | 28 | 是 |
| `rejudge_design_method` | `ROW6_RE` | TC | 20 | 20 | 20 | 是 |
| `rejudge_design_method` | `STEP_RE` | TC | 1770 | 1770 | 1770 | 否 |
| `rejudge_priority` | `BENCH_RE` | TC | 247 | 247 | 247 | 是 |
| `rejudge_priority` | `COSMETIC_RE` | 文字層 | 2202 | 2202 | 2202 | 是 |
| `reverse_coverage` | `NAMED_RE` | 文字層 | 37005 | 69327 | 37003 | 否 |
| `reverse_coverage` | `SPLIT_RE` | 文字層 | 5103 | 5842 | 5103 | 否 |
| `reverse_probe_rows` | `PARAM_RE` | 文字層 | 1893 | 1893 | 1941 | 否 |
| `reverse_probe_rows` | `REMOVE_RE` | 文字層 | 18 | 18 | 18 | 是 |
| `scan_clause_patterns` | `ENUM_RE` | 文字層 | 2654 | 2169 | 2169 | 是 |
| `verify_axis` | `BASE_RE` | 識別子 | 367 | 367 | 367 | 否 |
| `verify_gates` | `PD_RE` | TC | 0 | 0 | 0 | 否 |
| `verify_gates` | `PM_RE` | 文字層 | 1260 | 1260 | 1260 | 否 |
| `verify_gates_03` | `PD_RE` | TC | 0 | 0 | 0 | 否 |
| `verify_gates_03` | `PM_RE` | 文字層 | 1260 | 1260 | 1260 | 否 |
| `verify_layer3` | `ITEM_RE` | 文字層 | 3839 | 3839 | 3839 | 否 |
| `verify_layer3` | `PD_RE` | TC | 0 | 0 | 0 | 否 |
| `verify_layer3` | `PM_RE` | 文字層 | 1260 | 1260 | 1260 | 否 |
