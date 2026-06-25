# M1 — Stage 7 Scorecard 勘查筆記

> 唯讀勘查結果(只讀原有 repo,未寫入)。對應 `M1_CLAUDE_CODE_PROMPT.md` 第一步。
> 日期 2026-06-25。

## 0. 重要前提:目前沒有任何 findings.json

`output/` 與 `output-modern/` 皆空,全 repo 找不到 `findings*.json`。
→ prompt 的「交付」步驟(對現有 findings.json 跑 `--scorecard` 貼回 baseline)**目前無法執行**,因為沒有 baseline 資料。
→ 取得辦法見文末「待決 B」。

## 1. findings.json 實際 schema(§9,取自 review_engine.review_workbook + ASPICE_SWE6_AI_Review §9)

頂層:
- `batch_meta`: `source_file` / `sheet` / **`total_tcs`** / **`total_req_groups`** / `reviewed_at`
- `per_req_findings[]`(Tier 1):`req_id` / `tier=1` / `rule_ref(§6.x)` / `severity` / `scope_tcs[]` / `issue` / `evidence_req_spec` / `suggestion_note` / `stub?`
- `per_tc_findings[]`(Tier 2+3):`tc_id` / `row` / **`overall_verdict` (fail|pass_with_issues|pass)** / `findings[]`
  - 每個 finding:`tier` / `field` / `rule_ref` / **`severity`** / `issue` / `evidence` / `evidence_req_spec?(Tier2)` / `original` / `revised` / `suggestion_note`
- `batch_summary`:`verdict_counts{pass,pass_with_issues,fail}` / `tier_summary{tier1,tier2,tier3}` / `reasoning`

## 2. 七項 KPI 的來源可算性(逐項核對)

| KPI | 來源 | 可算? | 說明 |
|---|---|---|---|
| **first_pass_rate** | findings | ✅ 直接 | (total_tcs − 帶 Critical/Major finding 的 TC 數) / total_tcs。分母用 `batch_meta.total_tcs`,分子數 `per_tc_findings` 中含 Critical/Major 的 tc_id(零 finding 的 TC 不會出現在清單,用 total 反推) |
| **design_method_accuracy** | findings | ✅ 代理 | 不正確 = 被 §8.5.2(method 缺)或 §8.5.3(method 與 procedure 不符)標記的 TC;正確率 = (total_tcs − 被標數)/total_tcs |
| **requirement_coverage** | findings **不足** | ⚠️ None | findings 只看「已存在的 TC」分組,看不到「產 0 TC 的需求」。需 source 需求清單(parser/job rows)才算得出。→ 退化 None,報告標「缺需求母體」 |
| **traceability_completeness** | 需 `traceability` 輸入 | ⚠️ 視輸入 | findings 不帶 per-TC spec 對應狀態(`evidence_req_spec` 只在部分 Tier2 finding)。需 spec_matcher 的 per-TC 對應結果另外餵入(介面已有 `traceability` 參數)。無 → None |
| **field_completeness** | 需 `validation` 輸入 | ⚠️ 視輸入 | 真正的 Stage 5 完整性要 `validator.validate_row` 輸出(介面已有 `validation` 參數)。findings 只有零星結構訊號,不等於完整性。無 → None |
| **avg_decompose_depth** | 需 `decompose_meta`(Stage 3) | ❌ None | Stage 3 尚未提供每需求步數 → 優雅退化 None,不影響 gate(與 prompt 預期一致) |
| **reality_gap_rate** | 需 Stage 6 reality-gap 標記 | ❌ None | Stage 6 強化尚未實作 → None(與 prompt 預期一致) |

**結論:** 介面契約 `compute_scorecard(findings, validation, traceability, decompose_meta)` 的四個分離輸入正好對應上述——findings 只夠算 2 項(first_pass_rate、design_method_accuracy 代理),其餘需各自的輸入;2 項目前必然 None。**不捏造,缺來源即 value=None。**

## 3. 對映計畫(實作時)

- `compute_scorecard` 嚴格照分子/分母表;`denominator==0` 或來源缺 → `value=None`、`passed=None`、不 gate。
- `gate_passed` = 所有「有門檻且有 value」的 KPI 皆 passed。
- 門檻只 gate:first_pass_rate(0.80)、requirement_coverage(1.00)、traceability_completeness(0.95)、field_completeness(0.98)。
- `scorecard.json` 欄位順序固定(供趨勢比較)。
