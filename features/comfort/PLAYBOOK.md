# PLAYBOOK — Comfort (FW036 TC Generation)

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
- Profile: `docs/runtime/profiles/FW036_R1L_Comfort_Profile.md`
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
7. On anything the sources don't state: `[ASSUMPTION A-COnn]` marker +
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

> 讀 `ComfortHMI/PLAYBOOK.md`、`ComfortHMI/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`ComfortHMI/feature.yaml`、
> profile,以及 `RULINGS.md`(如存在)。目前狀態:{P?,一句話}。
> 本次執行:{P1 recon / P4 data build / P5 pilot batch 只做 {batch} /
> P6 其餘批次 / A-Hnn 工單}。遇到六條停下條款就登記並停,PENDING 的
> 子決策({列出}) 不得自行處置。完成後回報{對應上繳包}。

## 6. Status board — Comfort — **CLOSED**

**結案裁定：Pei，2026-08-17** —— 「交付了就這樣結束 不要繼續了」。
分析層與執行層皆不再開新作業。

### 6.1 結案之狀態（下放包 93 §4）

| | |
|---|---|
| 交付物 | **`…_Comfort_20260817_itemfmt.xlsx`（`97e469fe…`，175,236 bytes）**，在 `ComfortHMI/` 夾內（**ENTRY 031，2026-08-17 第二版交付**：J 欄去 source class 標籤、I 欄改兩段式）。**前一版 `…_20260816_extdocs.xlsx` 仍在夾內待 Pei 移除** |
| 交付說明 | `Comfort_HMI_delivery_note.md`（**`71ac5a94…`，6,551 bytes**），同夾 —— 訂正版已於 2026-08-17 09:24 就位，實測相符（**ENTRY 029**）|
| 台帳 | `DELIVERY.sha256` 至 **ENTRY 031**（028／031 為 `delivered`，029 為 `delivered-amended`，030 為本版之寫回）|
| 語料 | **434 列 / 383 之 403（95.0%）**；marker 列 **4 條** |
| 未涵蓋 | **20 個單位無列、2 個有列而未全測** |
| 未答問題 | **22 個**（RD-1，final 2026-08-17，回覆去向留白；**其送達屬 Pei，非本 pipeline 之待辦**）|
| 基線 | **SR24 CR24879**，交付說明已標明；夾內 SR25 兩檔依 Pei 裁定留置 |
| lint | **54 道全綠，0 finding** |
| 條文 | **R-C1 ～ R-C45**（含修訂共 **50** 條）|
| 往返 | **handoff 93 ／ upstream 72** |

### 6.2 已知而未處理者（供日後查考，**不再動作**）

1. ~~**交付物與語料差一欄**（`-382` 之版本名）~~ —— **已消解**：
   2026-08-17 之第二版交付（ENTRY 030／031）為全量重寫，已帶入 SR25。
   **那個「下次」還是來了** —— 它由一件無關之事（I／J 兩欄改版）帶來，
   而不是由原訂之途徑。
2. **`019-02`／`-03` 之缺口理由於交付說明中偏粗**：實為「**找到而不得用**」
   （`16.13` 逐項列出，而 §8.2.1 禁跨章移植），說明中寫成「找不到」。
3. **A-CF23**：spec 內以圖承載之內容讀不到（037 之 52 處、`15.1` 之 chart）。
4. **DR #36**：通用空白範本本體未擴充；Comfort 用之 ext 母本已擴充
   （`forms/…_SWQT_20260816_ext.xlsx`）。

### 6.3 結案前之階段紀錄（存查）

- [x] P0 intake ／ P1 recon ／ P2 DECISIONS ／ P3 framework ＋ profile
- [x] P4 data artifacts ／ P5 pilot ／ P6 全批次生成，lint green
- [x] P7 寫回 ENTRY 004–026、Excel 四項確認（Pei，2026-08-17）、
      交付 ENTRY 027–029
