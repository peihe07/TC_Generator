# G156 —— 腳本產物之三類判類（R-P227）

> **判類先於任何重跑**（R-P227）；本腳本**只讀不跑**。
> (a) 現況型：重跑並比對有效（R-P220 適用）
> (b) 非決定性：比對實質內容而非位元組
> **(c) 時點相依：一律不得重跑** —— 其現時性由「產生時點 ＋ 其後之異動紀錄」判定

## 計數（產物 68）

| 類 | 數 |
|---|---|
| (a) 現況型 | **52** |
| (b) 非決定性 | **4** |
| **(c) 時點相依（不得重跑）** | **12** |

## (c) 時點相依 —— 逐份及其時點語義

| 產物 | 時點語義 |
|---|---|
| `b1_before16.json` | 16 包**修補前**之批次資料快照，供 G113 驗證條件重現用 |
| `b1_before17.json` | 17 包修補前之快照，同上 |
| `b2_before13.json` | 13 包修補前之快照 |
| `b2_before15.json` | 15 包修補前之快照 |
| `b2b3_writeback_path.json` | 寫回路徑於當時之實測座標 |
| `b3_before14.json` | 14 包修補前之快照 |
| `b3_dryrun.json` | 16 包 dry-run 寫回之當時結果 |
| `b4_batch2_snapshot.md` | 檔首自載「第二批之**現行狀態快照**」——其 SHA256 取自 23 包當下（R-P175 已裁其不可重建） |
| `b4_material.md` | 語義為「**產生當時**待產出者為何」——其排除清單取自當時之 `generated/`；今全部已產出，重跑必得空集 |
| `b5_material.md` | 同上；31 包重跑實得「納入 0 leaf」，逐字原文全失 |
| `edit_integrity_baseline.json` | G108 之**基準**快照（7 檔 163 符號）——其用途即為與現況比對，重跑即等於重設基準 |
| `final_tc_id_map.tsv` | 臨時號 → 最終號之對照，取自指派當時 |

## (b) 非決定性

| 產物 | 依據 |
|---|---|
| `b3_er_restatement.md` | 詞頻表含同計數者，其排序隨語料插入序而異（31 包實測 `front` / `rear` 互換，數值全同） |
| `b5_residual_sample.md` | 以 `random` 抽樣；種子已載，惟母體隨批次成長而變 |
| `b8_b9_b12_scans.md` | G131 之抽樣以 `random.Random(26)` 為之，其母體隨批次成長而變 |
| `g150_design_method.md` | 抽樣以 `random.Random(31)` 為之，母體隨批次而變 |

## (a) 現況型（52）

`b1_column_crosscheck.md`、`b1_dangling_refs.md`、`b1_swepm008.md`、`b1_tc_framework_sheet.md`、`b1_template_diff.md`、`b2_anchor_state.md`、`b2_cfts010_ole.md`、`b2_false_positive.md`、`b2_uncovered_chapters.md`、`b2_v2_uncovered_chapters.md`、`b3_anchor_attributes.md`、`b3_dangling_rule_check.md`、`b3_embedded_objects.md`、`b3_swepm025_triggers.md`、`b3_sys3_crosscheck.md`、`b4_089_row_material.md`、`b4_ee_architecture.md`、`b4_final_step.md`、`b4_precond_verbs.md`、`b4_signals_calibration.md`、`b4_swepm025_material.md`、`b5_arif_final_step.md`、`b5_column_entropy.md`、`g103_layer3.md`、`g113_buckets.md`、`g113_or_branch.md`、`g114_layer3_full.md`、`g117_multivalue_sets.md`、`g121_reconciliation.md`、`g136_pattern_variants.md`、`g137_reasoning_assessment.md`、`g142_precond_state.md`、`g145_gate_triggers.md`、`g155_design_method_rejudge.md`、`g156_product_classes.md`、`g28_vcvm_quality.md`、`g94_source_clause.md`、`g99_anchor_set.md`、`item_to_chapter.json`、`layer3_full.tsv`、`leaf_batch_reconciliation.tsv`、`leaf_main_chapter.json`、`leaf_testset.tsv`、`multi_chapter_leaves.md`、`reverse_coverage_001-power-down.md`、`reverse_coverage_002-timeout-settings.md`、`reverse_coverage_003-power-state-a.md`、`reverse_coverage_004-power-state-b.md`、`reverse_coverage_005-startup-display.md`、`sampling_for_review.md`、`sys3_chapters.md`、`unreferenced_anchors.tsv`

判類依據：語義為「現況為何」——其輸入為當下之 `generated/` 或素材，重跑並比對有效。

## 判類有疑義者

**無** —— 66 份皆能自其檔首宣告或產生腳本之定義判定。
若日後新增產物之語義不明，依 R-P227 **一律跳過並上繳，不得試跑**。
