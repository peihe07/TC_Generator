# PLAYBOOK — Power_Moding (FW036 TC Generation)

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
Claude Code without asking — bounded by the six stop conditions (canon §0):
unresolved lookup, ambiguous segmentation, invariant violation, uncovered
rule, fabrication pressure, done-region-vs-spec contradiction. On a stop:
file it (ANOMALIES/DECISIONS entry with evidence + proposal), continue
elsewhere, and it comes back to chat.

## 2. Handoff packages

**Chat → Claude Code (the "下放包"), assembled before each execution run:**
- This PLAYBOOK + the feature `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; `RULINGS.md` if pre-scaffold rulings exist
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_Power_Moding_Profile.md`
- Kickoff prompt (§5)

**Claude Code → chat (the "上繳包"), returned at each gate:**
- After P1: `RECON.md` + pre-filled `DECISIONS.md`
- After P5 pilot: generated JSONs for the pilot batch + a one-page digest
  (split rationale coverage, anomaly list, distributions)
- After P6: `lint_report` + distributions (priority, design method) +
  placeholder set
- Before P7 write: dry-run summary containing ALL checklist fields
  (canon §6) — a summary missing a field is returned, not approved

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
7. On anything the sources don't state: `[ASSUMPTION A-PMHnn]` marker +
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
  copy+yaml, no shared library (canon §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `Power_ModingHMI/PLAYBOOK.md`、`Power_ModingHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`Power_ModingHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — Power_Moding

> 更新於 2026-08-23（下放包 04）。往返紀錄見 `docs/INDEX.md`。

- [x] **P0 intake complete** — 素材 5 份（4 客戶 ＋ 1 母本工作副本），
      `shasum -c` 全 OK；missing files: **無**（DR-PMH 零筆）
- [x] **P1 recon complete** — `workbook_state:` **BLANK**（R-PMH8）;
      `leaves:` **48**; `targets:` **48**; recon assertion 1/1 PASS
- [ ] **P2 DECISIONS signed** (date: ____) — `DECISIONS.md` 已預填並補入
      8 項 `[RULED]`，**待 Pei 簽核**
- [x] **P3 framework Layer 1/2/3 定版**（2026-08-24，R-PMH36）—— Layer 2
      **8 組定版**，48/48 分配與 granularity（G1–G5 ＋ 五個 must-hit）皆已驗。
      ⚠ profile（`FW036_R1L_PowerModing_Profile.md`）**尚未撰寫**
- [ ] P4 data artifacts built — `outline_map.json`／`uncited_sections.tsv`
      已就緒；A-PMH03（outline 7.1 之 5 leaf）為指名複核項
- [ ] P5 pilot batch ____ reviewed; verdict: ____; corrections: ____
- [ ] P6 all batches generated; lint green; placeholders: ____
- [ ] P7 dry-run approved → v__ tag: ____; submitted: ____; RD-1 sent: ____

### 下一步

**Phase 4（TC 生成）。** Phase 3 之 Layer 1/2/3 已定版（R-PMH36）。
**Phase 4 之唯一前置為 A-PMH13（`SWE1-HMI-PM-028`）之處置** ——
其涉 48 leaf 中之一個，**首批可於不含 `-028` 之情形下先行開批**。
另 profile 尚未撰寫。

### Open rulings

> Q3 **已結清**（R-PMH27，三欄留空）；**Q11 已結清**（R-PMH36，Test Set #2 = `Disclaimer Screen`）。

| 標記 | 事項 | 狀態 |
|---|---|---|
| `[PEI]` Q10 | `Product Document 記錄封面頁` —— 範圍為**一整張分頁**，需增補 11 項 | 否，Phase 7 前 |
| `[PEI]` A-PMH13 | `SWE1-HMI-PM-028` 之處置 —— 擴查後確認為**全案缺口** | 否，Phase 4 前 |
| `[PEI]` | `DECISIONS.md` §6 之 Part N 與 profile `[OVERRIDE]` | Phase 3 |

### Open PENDING anomalies

| 條號 | 主旨 | 複核時點 |
|---|---|---|
| A-PMH03 | SYS1 匯出 outline 7.1 相對 PDF 為重排 | **Phase 4**（5 leaf 指名複核） |
| A-PMH04 | 6 則 outline 為圖片佔位 | **Phase 4**（render 取用時） |
| A-PMH10 | 母本與客戶那份之 design_method DV source 不同 | 不阻斷（實務逸出 0） |
| **A-PMH12** | **`Q` 套用 P0–P3 下拉、`AF` 列舉含前導空白** | **Phase 6／7 之前置阻斷項** |
| A-PMH06 附項 | `new_feature.py` 之 `GITIGNORE` 樣板 | **PENDING-CANON**，本 feature 不改
