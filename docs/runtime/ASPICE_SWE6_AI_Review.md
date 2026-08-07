## 0. Purpose
Audit existing TCs against SWE.6 (deterministic, reproducible, auditable, traceable, no FP/FF). Input = a batch of TCs from an Excel workbook (`Test Case Specification 測試用例規範` sheet, typically 50–600 rows). Output = a Three-Tier Findings Report.

This version (v2.2) restructures review around the **reviewer's actual decision order**: did the team decompose the Requirement correctly first; only then is it worth checking whether each TC aligns with the Req; only after that does individual TC writing quality matter. Detection patterns and worked examples live in `backend/review_engine.py`; this doc is the human summary.

**v2.2 changes** (vs v2.1): schema cleanups surfaced during validation runs. §6.7 clarifies how multi-Req-ID TCs participate in §6.1–§6.5 (each Req group runs decomposition independently using the spec句 segment matching the corresponding `[REQ-ID]` tag). §7 opener adds explicit format rule for `evidence_req_spec` in multi-Req-ID scenarios. §9.2 `stub` rule extended to mark §6.6 (omit) and §6.7 (optional).

**v2.1 changes** (vs v2): §6.6 (Tier 1 not executable) raised from Info to Major — represents traceability failure, not housekeeping. §6.7 added (Multi-Req-ID in single TC) — handles cells where `Requirement or Design ID` carries multiple newline-separated Req IDs. §8.3.6 added (fabricated value Tier 3 fallback) — catches fabricated values when Tier 2 §7.4 is skipped due to §6.6.

## 1. Language Policy
Real-world TCs are mixed-language. Review tolerates this:

- **Findings** (`issue` / `reasoning` / `suggestion_note`): Traditional Chinese.
- **Rewrites** (`original` / `revised`): match the source language of the field. Chinese TC → Chinese rewrite. English TC → English rewrite. Mixed → keep the dominant language. Never translate. Goal is a drop-in replacement reviewer can paste back.
- **Tier 1** rewrites and stubs follow the same rule: scope-level findings about a Req group use the same language as the affected TCs.
- No emoji.

## 2. Core Principles (judgement basis)
- One TC = one verification objective; flow multi-step, validation single
- Final Step owns validation; represents Test Item executably
- TC reflects Req / SWRA; no vague wording, no hidden assumptions
- **Req decomposition determines coverage; TC writing only determines reproducibility.** Tier ordering reflects this.
- **Reviewer stance:** flag what is wrong + why + how to fix. Every `revised` MUST be traceable to a specific rule violation. Do not silently rewrite style preferences.

## 3. Three-Tier Review Model

| Tier | Scope | Question | Max Severity | Halts later tiers? |
|---|---|---|---|---|
| **Tier 1 — Decomposition** | Per Requirement ID group | "Did the team decompose this Req into the right set of TCs?" | Critical | No. Tier 2/3 still runs; batch summary prioritizes Tier 1. |
| **Tier 2 — Alignment** | Per TC × its Req spec | "Does this TC actually verify what the Req says?" | Critical | No. |
| **Tier 3 — Writing Quality** | Per TC internal | "Is this TC written per SWE.6 writing rules?" | Major | No. |

Tier 1 emits `per_req_findings`; Tier 2 and Tier 3 emit `per_tc_findings`. The two arrays are independent — a Tier 1 Critical does not duplicate into per-TC findings, and Tier 3 findings on a TC under a Tier-1-failed Req are still emitted normally.

When `batch_summary.reasoning` is written, it MUST address Tier 1 first. Reviewer should resolve Tier 1 before fixing Tier 3 issues, because new TCs added to fix decomposition will need their own Tier 3 review.

## 4. Severity Rubric (FIXED — do not reinterpret)

Severity is determined by detection pattern and Tier, not reviewer feel. Each Tier has a hard ceiling:

| Severity | Tier 1 examples | Tier 2 examples | Tier 3 examples |
|---|---|---|---|
| **Critical** | Missing supported/negative pair; missing boundary axis; supported-only enumeration without unsupported counterpart; spec句引用不一致 | Final Step launches test tool but never reads result; Test Item describes outcome NOT in Req spec; fabricated numeric value not in Req | (none — Tier 3 caps at Major) |
| **Major** | Sibling-axis ambiguous; **Tier 1 not executable (no English spec句 in group)**; **Multi-Req-ID single TC** | ER misses part of Req's stated outcome; Pre-Cond contradicts Req's trigger; Procedure trigger differs from Req's trigger | Forbidden verb / guessing tone; Pre-Cond contains action; design_method missing or inconsistent; tc_title >14 words or no distinguishing token; **fabricated value with no Specification Reference (Tier 2 skipped fallback)** |
| **Minor** | (none — Tier 1 caps at Major for §6.6/§6.7; Critical for coverage gaps) | (none — Tier 2 doesn't deal with style) | tc_title sentence-shape where scenario tag is clearer; Pre-Cond states system default; ER numbering anomaly (`1.1.` `2.2.`); step numbering duplication |
| **Info** | (none in v2.1) | (rare) | Multi-language collision in Test Item; minor whitespace |

When a TC triggers multiple patterns, emit one finding per pattern at its own severity. Never collapse findings to "lift" severity. **No systemic auto-suppression** — even if 100% of TCs share a violation, every TC still gets its own finding.

## 5. Workflow

1. **Parse workbook** — locate `Test Case Specification 測試用例規範` sheet; identify header row (typically row 9); extract data rows where `Test Case ID` is present.
2. **Group by Requirement ID** — primary key for Tier 1 grouping. **Multi-Req-ID handling:** if `Requirement or Design ID` cell contains multiple newline-separated Req IDs (e.g. `SWE1-PROJ-212\nSWE1-PROJ-213`), the TC is registered under EACH Req ID for Tier 1 grouping AND a Tier 1 §6.7 finding is emitted on the TC. Tier 1 §6.1–§6.5 still run independently per Req ID using whichever spec句 segment applies.
3. **Tier 1 (per Req group):**
   - 3a. **Extract Req spec句** — scan Test Item fields in the group; find the first English sentence containing `shall` / `must` / `should` (case-insensitive). For multi-Req-ID TCs, match by the `[REQ-ID]` tag in Test Item if present (e.g. `[SWE1-PROJ-212]\nAudio input sensitivity MUST...`); otherwise use the whole Test Item.
   - 3b. **Cross-check spec consistency** — if multiple TCs in the group carry English spec句 and they differ materially, emit Critical finding (`§6.5`).
   - 3c. **If no spec句 found** — mark group as `tier1_skipped`, emit one Major finding (`§6.6`); skip Tier 2 spec-comparison rules but still run Tier 3 (with §8.3.6 as fabricated-value fallback) on the TCs.
   - 3d. **Decomposition checks** — apply `§6.1` ~ `§6.4` to determine missing TC axes.
4. **Tier 2 (per TC):** apply `§7.1` ~ `§7.5` using the Req spec句 from Tier 1 as the reference.
5. **Tier 3 (per TC):** apply `§8.1` ~ `§8.5`. When the TC's Req group is `tier1_skipped`, additionally apply `§8.3.6` (fabricated value fallback).
6. **Emit Findings Report** per `§9` contract; `batch_summary.reasoning` orders Tier 1 first.

## 6. Tier 1 — Requirement Decomposition

**Scope:** one Req ID group at a time. Output: `per_req_findings`.

### 6.1 Missing supported/negative pair (Critical)
- Detect: Req spec句 contains binary phrasing — `supports / supported`, `enabled / valid format`, `if ... allow`, `permitted` — but the TC group only has TCs covering the affirmative path (no unsupported / disabled / invalid sibling).
- Suggestion: provide a stub for the missing negative TC with `test_item`, `pre_conditions`, `test_procedure_outline`. Stub language matches the dominant language of existing TCs in the group.

### 6.2 Missing boundary axis (Critical)
- Detect: Req spec句 mentions a numeric limit / threshold / range / count — `up to N`, `at least N`, `within N seconds`, `maximum N` — but TCs only test mid-range values, not `=limit`, `limit±1`, or `=0`.
- Suggestion: list missing boundary cases with one-line rationale each.

### 6.3 Missing enumeration coverage (Critical)
- Detect: Req spec句 enumerates supported items (`A2DP`, `HFP`, `AVRCP`; or `USB-A`, `USB-B`; or `MP3`, `WAV`, `FLAC`) — TC group covers only a subset.
- Suggestion: list each missing enumerated item.

### 6.4 Sibling axis ambiguous (Major)
- Detect: Req group has 2+ TCs that read identically except for trivial wording, AND no `Test Item` carries an explicit distinguishing token (no scenario tag like `Cold boot`, `USB-A-1 port`, `unsupported device`).
- Suggestion: rewrite Test Items in scenario-tag shape so the differentiating axis is named.

### 6.5 Spec句 inconsistent across siblings (Critical)
- Detect: 2+ TCs in the group carry different English `shall / must / should` sentences. This means TCs in the same Req group cite different spec versions — traceability is broken.
- Suggestion: identify the canonical spec句 (typically the longest / most detailed) and flag others for reconciliation. Do NOT auto-rewrite — reviewer must confirm which version is current.

### 6.6 Tier 1 not executable (Major)
- Detect: no TC in the group carries an English spec句 with `shall / must / should`. Tier 1 cannot anchor decomposition checks; Tier 2 spec-comparison rules will all skip for this group.
- Severity: **Major** — this represents a traceability failure (the team cannot demonstrate which Req句 each TC verifies). Not "housekeeping".
- Suggestion: locate the canonical Req spec from upstream (Polarion / SWRA) and paste into Test Item of at least one TC in the group. Tier 3 §8.3.6 (fabricated-value fallback) will run on TCs in this group as compensation.

### 6.7 Multi-Req-ID in single TC (Major)
- Detect: the TC's `Requirement or Design ID` cell contains multiple Req IDs separated by newline (e.g. `SWE1-PROJ-212\nSWE1-PROJ-213`), OR the Test Item uses bracket tags like `[SWE1-PROJ-212]` and `[SWE1-PROJ-213]` to delimit multiple spec句 segments within one cell.
- Severity: **Major** — violates §2 "One TC = one verification objective". A single TC verifying two Reqs cannot give an unambiguous pass/fail per Req when only one fails.
- Exception (still flag, but note in `suggestion_note`): when the same physical test run produces both measurements simultaneously through one tool (e.g. PCTS-MT1 producing both sensitivity and distortion in one execution). In this case, splitting may not be operationally feasible.
- Suggestion: prefer splitting into separate TCs (one per Req), even if the procedures share setup. If splitting is genuinely infeasible due to test-tool coupling, rewrite Test Item as a compound objective with both Req IDs explicitly named, AND ensure ER has separate observable outcomes per Req — `1. <Req-A outcome>; 2. <Req-B outcome>`.

**Group participation rule:** when this TC is the sole occupant or contributes to a Req group:
- The TC is registered under EACH of its constituent Req IDs for §6.1–§6.5 grouping purposes.
- Each Req group runs §6.1–§6.5 **independently** using only the spec句 segment matching that Req ID's `[REQ-ID]` tag in Test Item (or, if no tag exists, the entire Test Item).
- Tier 1 findings emitted on each Req group treat the multi-Req-ID TC as one of the group members but do not duplicate the §6.7 finding (which is recorded once, see schema below).
- **Heuristic for measurement-class spec句:** if the spec句 contains specific numeric thresholds (e.g. `RMS of 2500`, `< 1%`, `100 Hz to 4000 Hz`) and the Req group contains only the multi-Req-ID TC, §6.2 (boundary axis missing) is highly likely to fire because boundary cases require additional dedicated TCs.

**Schema:** this finding is recorded once in `per_req_findings` with `req_id` set to the comma-joined Req IDs (e.g. `"SWE1-PROJ-212, SWE1-PROJ-213"`) and `scope_tcs` listing the offending TC ID. Do not duplicate this finding under each constituent Req group.

## 7. Tier 2 — TC ↔ Requirement Alignment

**Scope:** one TC at a time, compared against the Req spec句 extracted in Tier 1. Output: `per_tc_findings`.

If the Req group is `tier1_skipped`, Tier 2 rules `§7.1`–`§7.5` are all skipped for TCs in that group. Tier 3 still runs.

**`evidence_req_spec` format rules:**
- Single-Req TC: quote the Req spec句 verbatim (the same句 extracted in Tier 1 step 3a).
- Multi-Req-ID TC (§6.7): when a Tier 2 finding concerns BOTH Reqs (e.g. §7.5 Final Step covers both PROJ-212 sensitivity AND PROJ-213 distortion), use bracket-tagged segments — `[SWE1-PROJ-212] <spec句 A>\n[SWE1-PROJ-213] <spec句 B>`. When the finding concerns only ONE Req, quote only that Req's segment and leave the other untouched (record only one finding under that Req's perspective).
- Empty `evidence_req_spec`: not allowed for Tier 2 findings. If the spec句 is unavailable (e.g. tier1_skipped group), the finding belongs in Tier 3 (typically §8.3.6 fallback), not Tier 2.

### 7.1 Test Item describes outcome not in Req spec句 (Critical)
- Detect: Test Item's outcome clause references a behavior, signal, or UI element that does not appear in the Req spec句 and does not appear in the broader Req context.
- Example: Req says "the HU shall prompt the user to continue the pairing process" but Test Item describes "automatic projection launch with no prompt" — wrong feature.
- Suggestion: rewrite Test Item to describe the Req's stated outcome; if the test target is intentionally a derived behavior, it needs its own Req ID.

### 7.2 ER does not cover Req's stated outcome (Major / Critical)
- Detect: Req spec句 enumerates outcome elements (`dialog with Confirm and Cancel buttons`, `connect AND launch projection`, `disconnect A2DP AND HFP`); ER only covers a subset.
- Severity: **Major** if at least one element is covered; **Critical** if ER addresses none of the Req's outcome elements.
- Suggestion: enumerate every observable element from the Req spec句; rewrite ER to include all.

### 7.3 Pre-Cond contradicts or duplicates Req trigger (Major)
- Detect: Req spec句 specifies a trigger ("when user selects to pair", "if user requests to connect", "when HU loses connection"); Pre-Cond states this trigger as already-true rather than the upstream state.
- Example: Req trigger = "when user selects to pair" → Pre-Cond should describe pre-pairing state (`Bluetooth ready`, `device discoverable`); not `device is paired`.
- Suggestion: replace target-state Pre-Cond with upstream state; move the trigger action into Test Procedure step 1.

### 7.4 Fabricated numeric value not traceable to Req or spec ref (Critical)
- Detect: Procedure or ER contains specific numbers — durations (`等待 5 秒`, `wait 5s`), repetition counts (`5 次`, `10 times`), file sizes, retry counts, timeouts — that:
  - Do NOT appear in Req spec句, AND
  - Do NOT appear in `Specification Reference` column.
- Heuristic regex: `(\d+)\s*(秒|s|sec|分鐘|min|次|times|小時|hours)` in Procedure or ER, with the number absent from Req spec句 and Specification Reference.
- Exception: domain constants (BT PIN `0000`, HTTP `200 OK`).
- Suggestion: replace with `<value defined in spec>` placeholder, OR add a citation to Specification Reference, OR remove the constraint if not Req-driven.

### 7.5 Final Step launches tool but never reads result (Critical)
- Detect: Procedure's last step's main verb is `執行 / Run / Execute / 啟動 / 開始 / 點選 ... 開始` followed by a test tool / suite name (`PCTS-MT1`, `PCTS-PT1`, `Facets-XXXX`, `ATS`, `PCTS-NavigationStatusTests`), AND no subsequent step reads the tool's verdict (`確認 / 對照 / 結果符合 / Pass`).
- This is the implicit-deferral variant of `§8.3.5` — the TC appears to execute but verification is silently delegated to whoever reads the tool log.
- Suggestion: append a verification step — `N+1. Confirm <tool> result report shows <pass criteria>` / `N+1. 確認 <工具> 結果報告為 <通過條件>`.

## 8. Tier 3 — TC Writing Quality

**Scope:** single TC, internal consistency only. Output: `per_tc_findings`.

### 8.1 Test Item

- **§8.1.1** Length out of range (>14 words EN or ~35 chars ZH) — Major
- **§8.1.2** Modal / hedge wording (`should`, `properly`, `應該`, `如預期`, `成功地`) — Major
- **§8.1.3** Multi-language collision (English spec + ZH explanation + ZH-traditional rewrite + EN tag in one cell) — Info
- **§8.1.4** Sibling-distinction token missing (Test Item identical to siblings under same Req) — Major *(if Tier 1 §6.4 didn't already flag at the group level)*
- **§8.1.5** No English spec句 nor traceable Req description — Critical *(only if `Requirement ID` is also blank; otherwise this becomes Tier 1 §6.6 at group level)*

### 8.2 Pre-Condition

- **§8.2.1** Action verb (EN: `Insert / Press / Connect / Open / Tap / Launch / Send / Configure`; ZH: `插入 / 按下 / 點擊 / 開啟（作為動作）/ 啟動 / 傳送 / 設定 / 執行 / 連線（作為動作）`; sequence words: `依次 / 先後 / 依序`) — Major
- **§8.2.2** Verification verb (`Check / Verify / Confirm / Observe / 檢查 / 確認 / 查看 / 觀察 / 是否`) — Major
- **§8.2.3** System default (`HU is powered on`, `車機已開機`, `System has booted`) — Minor
- **§8.2.4** Feature-under-test stated as ready — Critical *(circular, produces FP)*
- **§8.2.5** Bound to specific instance not capability (`存在 pixel 裝置`, `iPhone 14`) — Minor; rewrite as capability (`手機支援 Android Auto`)

### 8.3 Test Procedure

- **§8.3.1** Forbidden verb / guessing tone as main verb (EN: `observe / see if / check whether / verify / watch / monitor / inspect`; ZH: `觀察 / 查看 / 檢視 / 看看 / 是否 / 確認是否 / 留意`) — Major
- **§8.3.2** Step lacking executable content (question form, `是否可以...`, `should be able to...`) — Major
- **§8.3.3** Single-step procedure (only 1 numbered step) — Major
- **§8.3.4** Step numbering duplication (`5` and `5.` both exist) or ambiguous self-reference (`步驟3.6.9` instead of `步驟 3、6、9`) — Minor
- **§8.3.5** Final Step has no check target (pure action without `Check that ... / 確認 ...` clause) — **Critical**
- **§8.3.6** Fabricated numeric value, Tier 2 fallback (Major)
  - **Detect:** Procedure or ER contains specific numbers — durations (`等待 5 秒`, `wait 5s`), repetition counts (`5 次`, `10 times`), file sizes, retry counts, timeouts; AND `Specification Reference` is empty.
  - **Heuristic regex:** `(\d+)\s*(秒|s|sec|分鐘|min|次|times|小時|hours)` in Procedure or ER, with the number absent from any spec句 (if available).
  - **When this fires:** only when Tier 2 §7.4 cannot fire — i.e. the TC's Req group is `tier1_skipped` (§6.6 triggered) so there is no Req spec句 to compare against. Otherwise §7.4 takes precedence.
  - **Severity rationale:** Major rather than Critical, because without a Req spec句 we cannot prove the value is fabricated — only that it has no documented source. Reviewer must verify against upstream spec.
  - **Exception:** domain constants (BT PIN `0000`, HTTP `200 OK`).
  - **Suggestion:** add `Specification Reference` citation for the value, OR replace with `<value defined in spec>` placeholder, OR remove the constraint if not derived from any spec.

Note: §8.3.5 covers explicit "no check"; the implicit "tool launched but result unread" variant is `§7.5` (Tier 2). §8.3.6 is the fallback for §7.4 when the Req group lacks a spec句 — never both fire on the same value.

### 8.4 Expected Result

- **§8.4.1** Vague outcome (`正常 / 如預期 / works correctly / properly / successfully`) — Major
- **§8.4.2** Step↔ER count mismatch (cannot align 1:1) — Major
- **§8.4.3** Numbering anomaly (`1.1.` `2.2.` double-numbering, gaps, blank bullets) — Minor

### 8.5 Priority and Design Method

- **§8.5.1** Priority outside `P0 / P1 / P2 / P3` (e.g. `P4`, `High`, `Medium`, `Low`, `NA`, blank) — Major
- **§8.5.2** Design Method missing — Major
- **§8.5.3** Design Method inconsistent with Procedure shape (e.g. `BVA` but no boundary tested; `Scenario` with only 1–2 steps) — Major

## 9. Output Contract

### 9.1 Top-level shape

```json
{
  "batch_meta": {
    "source_file": "<filename>",
    "sheet": "Test Case Specification 測試用例規範",
    "total_tcs": 602,
    "total_req_groups": 87,
    "reviewed_at": "<ISO8601>"
  },
  "per_req_findings": [ /* §9.2 — Tier 1 only */ ],
  "per_tc_findings":  [ /* §9.3 — Tier 2 + Tier 3 */ ],
  "batch_summary":    { /* §9.4 */ }
}
```

### 9.2 Per-Req finding (Tier 1)

```json
{
  "req_id": "SWE1-PROJ-071-001",
  "tier": 1,
  "rule_ref": "§6.1",
  "severity": "Critical",
  "scope_tcs": ["TC-PROJ-071-001-001", "TC-PROJ-071-001-002", "TC-PROJ-071-001-003"],
  "issue": "Req spec句 為支援 / 不支援的二元判定，本群組已含支援案例與拒絕案例，但缺少『裝置不支援』的負向 TC",
  "evidence_req_spec": "the HU shall determine if the device supports wireless projection",
  "suggestion_note": "建議新增 TC：手機不支援 CarPlay → 配對時不彈出 CarPlay 對話方塊",
  "stub": {
    "test_item": "不支援 CarPlay 功能 → 配對時不彈出 CarPlay 連線確認對話方塊",
    "pre_conditions": "1. 手機不支援 CarPlay 功能\n2. 手機與車機藍牙處於可配對狀態\n3. 裝置從未連線過",
    "test_procedure_outline": "1. 開啟車機藍牙搜尋並選擇手機進行配對\n2. 在手機和車機上完成配對操作\n3. 確認車機螢幕未彈出 CarPlay 連線確認對話方塊"
  }
}
```

Field rules:
- `req_id`: from workbook
- `tier`: always `1`
- `rule_ref`: must cite a §6.x rule
- `scope_tcs`: list of TC IDs in the affected Req group
- `evidence_req_spec`: exact quote of the Req spec句 used as anchor (English, from Test Item)
- `stub`: required for §6.1 / §6.2 / §6.3; optional for §6.4 / §6.5 / §6.7; omit for §6.6
- `stub` language matches dominant language of existing TCs in the group

### 9.3 Per-TC finding (Tier 2 + Tier 3)

```json
{
  "tc_id": "TC-PROJ-072-001-001",
  "row": 16,
  "overall_verdict": "fail | pass_with_issues | pass",
  "findings": [
    {
      "tier": 2,
      "field": "test_procedure",
      "step_index": 4,
      "rule_ref": "§7.5",
      "severity": "Critical",
      "issue": "Final Step 為「觀察是否建立連線」，僅問句無檢查目標，將判定推給測試人員",
      "evidence": "4.觀察是否建立連線",
      "evidence_req_spec": "the HU shall connect to and launch Projection for the newly paired device",
      "original": "4.觀察是否建立連線",
      "revised": "4.確認車機與手機建立 CarPlay 無線連線\n5.確認 CarPlay 投屏介面自動啟動並顯示為前景",
      "suggestion_note": "Req spec句 同時要求 connect 與 launch 兩個動作，原 Final Step 兩者皆未驗證；拆為兩個獨立檢查步驟"
    },
    {
      "tier": 3,
      "field": "design_method",
      "rule_ref": "§8.5.2",
      "severity": "Major",
      "issue": "缺少測試用例設計方法",
      "original": "",
      "revised": "Scenario / Use Case",
      "suggestion_note": "本 TC 為跨藍牙 + 投屏的端到端流程，含 5 步驟，符合 §15 Scenario / Use Case 條件"
    }
  ]
}
```

Field rules:
- `tier`: `2` or `3` per finding (one TC may carry findings from both)
- `evidence_req_spec`: required for Tier 2 findings (the Req sentence used for comparison); omit for Tier 3
- `overall_verdict`: `fail` if any Critical (Tier 2 or 3); `pass_with_issues` if any Major/Minor; `pass` if only Info or none
- All other fields per v1 §7.2

### 9.4 Batch summary

```json
{
  "verdict_counts": { "pass": 0, "pass_with_issues": 12, "fail": 590 },
  "tier_summary": {
    "tier1": {
      "req_groups_total": 87,
      "req_groups_with_critical": 18,
      "req_groups_skipped": 7,
      "top_rules": [
        { "rule_ref": "§6.1", "count": 12, "title": "Missing supported/negative pair" },
        { "rule_ref": "§6.4", "count": 9,  "title": "Sibling axis ambiguous" },
        { "rule_ref": "§6.6", "count": 7,  "title": "Tier 1 not executable (no English spec句)" },
        { "rule_ref": "§6.7", "count": 35, "title": "Multi-Req-ID in single TC" }
      ]
    },
    "tier2": {
      "tcs_with_critical": 84,
      "top_rules": [
        { "rule_ref": "§7.5", "count": 47, "title": "Final Step launches tool but never reads result" },
        { "rule_ref": "§7.4", "count": 31, "title": "Fabricated numeric value" }
      ]
    },
    "tier3": {
      "tcs_with_findings": 602,
      "top_rules": [
        { "rule_ref": "§8.3.1", "count": 534, "title": "Forbidden verb / guessing tone" },
        { "rule_ref": "§8.5.2", "count": 602, "title": "Design Method missing" },
        { "rule_ref": "§8.3.6", "count": 14,  "title": "Fabricated value (Tier 2 fallback)" }
      ]
    }
  },
  "reasoning": "<繁中 4-6 句，必須先談 Tier 1，再 Tier 2，最後 Tier 3>"
}
```

`reasoning` ordering rule:
1. **Tier 1 first** — 整體拆解品質、缺哪些覆蓋面、哪幾組 Req 拆得不完整
2. **Tier 2 next** — 對齊度問題、Critical 集中區
3. **Tier 3 last** — 寫作層的系統性違規（即便數量大，優先序在後）
4. 結尾建議修正順序（先 Tier 1 → 補完後重審 → 再處理 Tier 2/3）

## 10. Self-Check (before emitting each finding)

1. `tier` matches the rule's section (§6 → tier 1, §7 → tier 2, §8 → tier 3)
2. `rule_ref` cites an actual section — no invented rules
3. `severity` ≤ Tier ceiling (Tier 1 ≤ Critical, Tier 2 ≤ Critical, Tier 3 ≤ Major)
4. Tier 2 findings include `evidence_req_spec`; for multi-Req-ID TCs, format per §7 opener (bracket-tagged segments when finding spans both Reqs)
5. `evidence` is an exact quote from the source — no paraphrase
6. `revised` is in the same language as `original`
7. `revised` actually fixes the cited rule — does not introduce new violations
8. For Tier 1 §6.1 / §6.2 / §6.3, `stub` is provided
9. Tier 1 findings on a Req group do NOT duplicate as Tier 2/3 findings on every TC in the group
10. **§7.4 and §8.3.6 are mutually exclusive on the same numeric value** — never both fire. §8.3.6 fires only when the TC's Req group is `tier1_skipped`.
11. **§6.7 (multi-Req-ID) is recorded once in `per_req_findings`** with `req_id` set to the comma-joined list and `scope_tcs` containing only the offending TC ID. The TC is registered under EACH constituent Req ID for §6.1–§6.5 grouping, but the §6.7 finding itself is NOT duplicated under each constituent Req group.

## 11. Final Rule
Reviewer's job is to flag and propose, in the order that matters: decomposition → alignment → writing. Tier 1 findings shape what TCs should exist; Tier 2 findings verify each TC actually verifies the Req; Tier 3 findings polish the writing. Batch summary always leads with Tier 1. Per-TC findings continue regardless of Tier 1 status, so reviewers retain visibility into individual TC quality even when the Req group needs restructuring.
