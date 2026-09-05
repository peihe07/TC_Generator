# PLAYBOOK — Popup (FW036 TC Generation)

Copied into every feature directory by `new_feature.py`. This is the
OPERATIONAL view: who does what, in which tool, with which handoff
artifacts, and the core TC-production loop. Rule authority stays with
`docs/fw036/FEATURE_ONBOARDING.md` (phases, tiers, workbook_state,
spec_mode) and the generic instruction + feature profile — on any conflict,
those win. Check off and annotate this file as the feature progresses; it
doubles as the feature's status board.

---

## 0. The working model

**Analysis happens in the Claude Project (chat). Execution happens in
Claude Code.** The two never blur:

- Chat is where evidence is weighed, options are surfaced, and Pei rules.
  Nothing in chat writes the workbook.
- Claude Code is where scripts run, files change, and gates enforce.
  Nothing in Claude Code rules on scope, style authority, or anomaly
  dispositions — it registers and proposes, then continues unaffected work.
- Every handoff is a FILE, not a memory: chat's output is signed
  documents (DECISIONS, RULINGS, profile, digests recorded into
  ANOMALIES/RUNBOOK); Claude Code's output is generated artifacts plus
  reports (RECON, lint_report, dry-run summary) that come BACK to chat for
  the next ruling. If it wasn't written down, it didn't happen.

## 1. Flow at a glance

```
 CHAT (analysis)                      CLAUDE CODE (execution)
 ──────────────────                   ──────────────────────
 P0  dump files, read INTAKE.md   →   intake.py [--scaffold]
 P1                                   recon.py → RECON + DECISIONS(pre-filled)
 P2  rule on [PROPOSED]/[PEI],    →
     sign DECISIONS
 P3  draft framework Part N +     →   (commit docs)
     profile with Claude, approve
 P4                                   adapt scripts per feature.yaml,
                                      build data artifacts
 P5  review pilot digest in chat, →   generate PILOT batch only, report
     rule corrections
 P6                                   remaining batches → lint green
 P7  review dry-run summary,      →   commit → --write → tag
     approve --write;
     draft RD-1 with Claude;
     submit (Pei only)
```

Chat touchpoints are exactly five: DECISIONS sign-off, framework/profile
approval, pilot review, dry-run approval, delivery. Everything else runs in
Claude Code without asking — bounded by the six stop conditions (FO §0):
unresolved lookup, ambiguous segmentation, invariant violation, uncovered
rule, fabrication pressure, done-region-vs-spec contradiction. On a stop:
file it (ANOMALIES/DECISIONS entry with evidence + proposal), continue
elsewhere, and it comes back to chat.

## 2. Handoff packages

**Chat → Claude Code (the "下放包"), assembled before each execution run:**
- This PLAYBOOK + the feature `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; `RULINGS.md` if pre-scaffold rulings exist
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_Popup_Profile.md`
- Kickoff prompt (§5)

**Claude Code → chat (the "上繳包"), returned at each gate:**
- After P1: `RECON.md` + pre-filled `DECISIONS.md`
- After P5 pilot: generated JSONs for the pilot batch + a one-page digest
  (split rationale coverage, anomaly list, distributions)
- After P6: `lint_report` + distributions (priority, design method) +
  placeholder set
- Before P7 write: dry-run summary containing ALL checklist fields
  (FO §6) — a summary missing a field is returned, not approved

## 3. The TC production loop (P5/P6 core, one parent per turn)

For each requirement parent, in 037 document order within its batch:

1. **Read** the parent's literal text + its batch context (spec sections,
   sibling rows including the done region, exemplars, popup/table rows)
2. **Scope** — before writing anything: check sibling reqs (do not absorb
   what a sibling owns, §8.2.1); check external references (do not absorb
   other specs' rules, §8.4.2); check the RD sub-id structure (one sub-id
   may need several TCs, §8.2.2 — never the inverse)
3. **Split** along genuine axes only (trigger / input / boundary / mode /
   environment, §8.3); one verification objective per TC (§5.7): one
   trigger's consequential outcomes = one TC with multi-line ER
4. **Write** fields per the generic instruction + profile overrides;
   reuse standard snippets verbatim; every literal (label, number, popup
   text, state name) traces to THIS feature's spec — cross-feature
   exemplars lend shape, never facts
5. **Reason** (繁中, 2–5 sentences): objective, key conditions, why this
   split, what was deliberately delegated and to whom
6. **Self-check** against the §9 list; emit; the generator assigns TC ids
7. On anything the sources don't state: `[ASSUMPTION A-POnn]` marker +
   ANOMALIES entry, or BLOCKED placeholder — never a fabricated value

Placeholders keep the leaf's row (completeness invariant, both
directions): requirement sentence as Test Item, `BLOCKED - see Remarks`,
Remarks = reason + anomaly id.

## 4. The rules that never change per feature

- Three-layer quality: lint (mechanical) → human pilot gate (judgment) →
  done region arbitrates disputes with evidence. Lint-green ≠ done; a
  reviewer finding isn't a defect until it survives the done-region check.
- Done region is style authority, never factual authority; frozen
  byte-for-byte under the state-appropriate hash invariant.
- Write-back invariants abort, never warn; weakening one is a chat ruling.
- Sequence at delivery: dry-run reviewed → clean-tree commit → `--write`
  (touches no tracked file) → annotated tag `fw036-{feature}-regen-vN`
  carrying xlsx SHA256 + done-region hash + row summary + lint result.
- The workbook Scope field is the workbook's identity claim — verify it
  matches the ruled requirement source at intake AND before submission
  (two independent features had it wrong in one week).
- RD-1 at delivery: systemic classes first with class-level remedies;
  every item = anomaly id + evidence + local disposition + requested
  action; the feature never waits on answers.
- What VARIES lives only in `feature.yaml` (paths, columns, done-region
  rule, spec_mode, reference template, lint vocab) and the profile
  ([OVERRIDE]/[ADD] clauses citing what they displace). Scripts are
  copy+yaml, no shared library (FO §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `PopupHMI/PLAYBOOK.md`、`PopupHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`PopupHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — Popup

- [x] P0 intake complete（上繳包 01，2026-08-27）；三件投遞檔 sha 實測，
  xlsx 2/2 與下放包指紋相符；PDF 為真 PDF 1.5／21 頁／**無文字層**
  → spec_mode **A+C**。落 `sources/raw/` 三個 doc_id
  （`popup_037_v0_2`／`core_hmi_lf_sys1`／`core_hmi_lf_pdf`），
  `MANIFEST.tsv` 3 列。**未走 `intake.py`**（來源已具名，直接落 `sources/`，
  下放包 §六-3 之指示）。missing files: DR-POP1／DR-POP2 未結，
  惟 `forms/` 內有候選件待裁（**A-POP2**）
- [x] P1 recon complete；workbook_state: **BLANK**；leaves: **5**；
  targets: **5**；assertions 4/4 PASS；`RECON.md`＋`DECISIONS.md`
  ＋`data/recon.json`＋`data/recon_leaf_to_section.tsv` 已產
- [x] P2 DECISIONS signed (date: **2026-08-27**, PeiPYHsu)。§6 兩筆 [PEI]
      由 Pei 回填；[PROPOSED] 8 筆未動即照案生效；Sign-off 由執行層轉錄，
      值由 Pei 指定
- [x] P3 framework Part N + profile approved ——
      `features/popup/framework.md`（LOCKED）＋
      `docs/runtime/profiles/FW036_R1L_Popup_Profile.md`（3,813 B）
- [x] P4 data artifacts built —— `data/popup_list_candidates.tsv`（345 列，
      帶來源 sha ＋ baseline）；`paths.popup_list` 接線（R-POP6）
- [ ] P5 pilot batch **全量一批（上繳包 02）** reviewed; verdict: ____;
      corrections: ____
      —— 已生成 **4 條**（`newR1L-POP-001`～`-004`），lint **21 項全 0**，
      `PENDING:` 佔位 0。`-002-05` 觸發 §八 升級**停下不生成**（A-POP8）；
      `-002-02` device 軸判定不拆（A-POP7）。
      **本 feature 無 done region，pilot review 是唯一人工閘，無第二道**
- [ ] P6 all batches generated; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____
- Open PENDING: **A-POP6／A-POP7／A-POP8**（A-POP1～A-POP5 已 RESOLVED）；
  R-POP5 [DEFAULT] 待 Pei 追認；DR-POP2／DR-POP3 已登記未送出
  （**DR-POP1 已 RESOLVED**，R-POP6）

### 工作簿

- 起建自 R-G1 母本（`forms/…_SWQT_20260817_ext.xlsx`，
  sha256 `6372fb6be02f48dc…`），落
  `sandbox/base/`（R-G64：xlsx 只准在此改）。**位元組相同之複製**，
  未以 openpyxl 開啟寫入（R-G3）
- 版面為 **Revision C**（Q = Estimated Test Time）——
  design_method/functional_safety/author 較 Revision A/B 右移一欄
  （R／S／AA，非 Q／R／Z）
- **`R10:R1411` 之設計方法下拉為 x14 擴充**（`下拉選單!$A$1:$A$9`）——
  `openpyxl` 讀不到，`save()` 會靜默刪除（**A-POP5**）。
  本 feature 之工作簿寫入一律走 `backend/xlsx_surgical.surgical_save`
- pilot 輸出：`sandbox/pilot01/`（4 列 × 15 欄，60 格），
  來源 `sandbox/base/` 之 sha 跑後未變
