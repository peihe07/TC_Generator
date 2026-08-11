# PLAYBOOK — AMFM (FW036 TC Generation)

Instantiated at P7 (the feature ran without one — registered as A-AM16).
This is the OPERATIONAL view: who does what, in which tool, with which
handoff artifacts, and the core TC-production loop. Rule authority stays
with `docs/fw036/FEATURE_ONBOARDING.md` and the generic instruction +
profile (`docs/runtime/profiles/FW036_R1L_AMFM_Profile.md`) — on any
conflict, those win. The status board (§6) reflects the actual AMFM run and
is maintained from `RUNBOOK.md`, which stays the feature-fact authority.

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
- This PLAYBOOK + `RUNBOOK.md` (status + feature-specific facts)
- Signed `DECISIONS.md`; rulings in `RULINGS.md`, recorded in `ANOMALIES.md`
- `feature.yaml` (all constants; scripts carry no per-feature literals)
- Profile: `docs/runtime/profiles/FW036_R1L_AMFM_Profile.md`
- Kickoff prompt (§5)

**Claude Code → chat (the "上繳包"), returned at each gate:**
- After P1: `RECON.md` + pre-filled `DECISIONS.md`
- After P5 pilot: generated JSONs for the pilot batch + a one-page digest
  (split rationale coverage, anomaly list, distributions)
- After P6: `lint_report` + distributions (priority, design method) +
  placeholder set
- Before P7 write: dry-run summary containing ALL checklist fields
  (canon §6) — a summary missing a field is returned, not approved

**Standing addition for AMFM (Pei, 2026-08-09)**: at every session opener
(「接手」) and every batch gate, report the outstanding rows of
`DATA_REQUESTS.md` by Urgency and which upcoming batches the missing files
degrade or block. A batch gate summary that omits this check is incomplete.

## 3. The TC production loop (P5/P6 core, one parent per turn)

For each requirement parent, in 037 document order within its batch:

1. **Read** the parent's literal text + its batch context (spec sections,
   sibling rows including the legacy region, exemplars, injected spec
   tables, cross-document citations)
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
7. On anything the sources don't state: `[ASSUMPTION A-AMnn]` marker +
   ANOMALIES entry, or BLOCKED placeholder — never a fabricated value

Placeholders keep the leaf's row (completeness invariant, both
directions): requirement sentence as Test Item, `BLOCKED - see Remarks`,
Remarks = reason + anomaly id. (AMFM shipped none — all 102 leaves have
TCs.)

## 4. The rules that never change per feature

- Three-layer quality: lint (mechanical) → human pilot gate (judgment) →
  done region arbitrates disputes with evidence. Lint-green ≠ done; a
  reviewer finding isn't a defect until it survives the done-region check.
- Done region is style authority, never factual authority; frozen
  byte-for-byte under the state-appropriate hash invariant. (AMFM's is a
  *legacy* region, not a done region — R4: style-borrowable,
  traceability-orphaned, excluded from coverage invariants.)
- Write-back invariants abort, never warn; weakening one is a chat ruling.
- Sequence at delivery: dry-run reviewed → clean-tree commit → `--write`
  (touches no tracked file) → annotated tag `fw036-amfm-regen-vN`
  carrying xlsx SHA256 + legacy-region hash + row summary + lint result.
- The workbook Scope field is the workbook's identity claim — verify it
  matches the ruled requirement source at intake AND before submission
  (AMFM had it wrong: A-AM01, same class as Home A-H26).
- RD-1 at delivery: systemic classes first with class-level remedies;
  every item = anomaly id + evidence + local disposition + requested
  action; the feature never waits on answers.
- What VARIES lives only in `feature.yaml` (paths, columns, done-region
  rule, spec_mode, reference template, lint vocab) and the profile
  ([OVERRIDE]/[ADD] clauses citing what they displace). Scripts are
  copy+yaml, no shared library (canon §5 ruling).

## 5. Kickoff prompt template (paste into Claude Code)

> 讀 `features/amfm/PLAYBOOK.md`、`features/amfm/RUNBOOK.md`、
> `docs/fw036/FEATURE_ONBOARDING.md`、`features/amfm/feature.yaml`、
> `docs/runtime/profiles/FW036_R1L_AMFM_Profile.md`,以及 `features/amfm/RULINGS.md`。
> 目前狀態:{P?,一句話}。本次執行:{任務}。遇到六條停下條款就登記並停,
> PENDING 的子決策({列出})不得自行處置。完成後回報{對應上繳包}。

Current instance (the only remaining Claude Code task):

> 目前狀態:P7,dry-run 已跑第二輪(158+143=301 列,legacy hash
> 30d9e4c0719a2929… 未變,coverage 102/102 exact,placeholders none),
> 待 Pei 批准。本次執行:批准後 — 乾淨 tree commit → `--write` →
> tag `fw036-amfm-regen-v1`(annotation 含 xlsx SHA256、legacy hash
> `30d9e4c0719a2929…`、`158 legacy / 143 regen (0 placeholder) / 301 rows`、
> lint green)。完成後回報 SHA256。

## 6. Status board — AMFM

- [x] P0 intake complete; source files in `inputs/`; spec_mode: **D**
      (CFTS Word document, no Polarion export, no PDF); `feature.yaml`
      filled from template
- [x] P1 recon complete; workbook_state: **FULL** — against the ruled
      source effectively BLANK (R4); leaves: **102**; targets: **102**
      (legacy region: 158 rows / author `Wilson`, covering 0 of 102 —
      A-AM02)
- [x] P2 DECISIONS signed by Pei (2026-08-09; RULINGS R3–R6)
- [x] P3 framework Part III appended (11 capability Test Sets, 102/102
      leaves allocated; R7-Q1/Q2) + AMFM profile written (R7)
- [x] P4 data artifacts built: `data/stla_to_cfts.{json,tsv}` (bracket +
      paragraph map, 102/102 leaves, `--check-batches` green),
      `data/exemplars.json` (Wilson style-only), `batches/*.json` (11);
      misses filed A-AM08 / A-AM09
- [x] P5 pilot reviewed 2026-08-10 — **Tuner Availability + Tune**
      (8 leaves → 13 TCs); verdict: **PASS with corrections (R10)**;
      corrections applied and lint green the same day. Pre-conditions
      R8 (VR out of scope) and R9 (029 → `CFTS024-4872457`) signed
      2026-08-10
- [x] P6 all 11 batches generated: **102 leaves / 143 TCs**, no leaf
      without a file; **lint green** (`scripts/lint_tcs.py`, exit 0);
      placeholders: **none**; P0/P1/P2/P3 = **0/129/14/0**; design
      methods Functional 63, EP 29, BVA 25, Decision Table 14,
      State Transition 11, Scenario 1
- [ ] P7 — dry-run run twice (latest 2026-08-10, after the R13 F/O
      rulings): `LEGACY 10-167 (158 rows, unmoved, hash 30d9e4c0719a2929…
      unchanged)` + `REGEN 168-310 (143 rows, appended)` = 301 data rows;
      coverage 102 regen req_ids == 102 leaf set, exact; placeholders
      none. **Pending: Pei approval → commit → `--write` → tag
      `fw036-amfm-regen-v1` → controlled-document submission → RD-1 send**
      (`docs/fw036/RD1_questions_amfm.md`, Q-AM1/Q-AM2/Q-AM3 still DRAFT;
      `docs/fw036/RD1_amfm_submission.md`)

### Open PENDING

Nothing here may be disposed of in Claude Code — all are Tier 2/3.

- **A-AM09 VR class — scope ruling.** `DATA_REQUESTS.md` row 4 carries
  CFTS028 as 已入 `inputs/` but the VR trigger-path attribution as
  「範圍裁決待下」 (Urgency: Medium). ANOMALIES records **R8**
  (verbatim 「不進去了」) as the ruling that puts VR out of scope for this
  workbook, and 003/009/025/027 were generated on that basis. Confirm R8
  stands and close the DATA_REQUESTS row, or re-open the four leaves.
- **087/094 and 089/095 `duplicate_of` — per-pair ruling (A-AM08,
  R7-Q4).** 087/094 both declare `4942534`, 089/095 both declare
  `4942540`. Each leaf keeps its own TC, `duplicate_of` is set both ways,
  and the two TCs of each pair take different halves of the shared clause
  (087 the four display items / 094 the antenna-not-connected value class;
  089 the display-update side / 095 the input-sampling side). If a pair is
  ruled a true duplicate, the marked TC is the removable one.
  (`090/096` — near-identical text, distinct ids — stays PENDING in the
  same class per A-AM08.)
- **A-AM11** rate-to-frequency-step mapping undefined upstream — ER
  asserts monotonicity only (021, 026, 028). PENDING upstream definition.
- **A-AM12** "intelligent entry" undefined beyond its two dependencies
  (030) — revisit against the Market Configuration vocabulary. Not
  blocking.
- **A-AM13** fast seek specified but reaching no 037 leaf — coverage hole,
  RD-1 (folds into Q-AM3).
- **A-AM14** Seek Up / Seek Down decomposed differently upstream —
  allocation-policy question, reported with Q-AM3.
- **RD-1, all DRAFT, Tier 3 to send** (`docs/fw036/RD1_questions_amfm.md`):
  - **Q-AM1** SWRA-A02 ↔ 037-A03 lineage (A-AM03/A-AM04): earlier-revision
    authoring, the contiguous `SWE-RAD-040…-045` tail, formal supersession
  - **Q-AM2** 037-A03 internal defects (A-AM08/R9): 029's id tail,
    numbering gaps 086/088, the same-id variant pairs, `SWE-RA-RAD-019`
    Description-type artifact hygiene
  - **Q-AM3** CFTS clauses allocated to no leaf (A-AM10): confirm the
    absorption reading or reallocate; 95 unallocated clauses across the
    20 sections the 037 uses
  - Batch-level items already recorded in RUNBOOK for the same send:
    §1.6.1.10 `$5009` title-vs-clause inconsistency; undefined value
    ranges (099 tuner status, 100 carrier-offset unit/encoding, 101 the
    five signal-strength thresholds); undefined "active station" (079);
    `4872515`/`4872524` claimed by no leaf; the `ECU:RRM` /
    `Radio:noSys` scope-tag inconsistency; HD Radio `4872546`/`4872569`;
    the 051/022/034 three-way near-duplicate (same class as Q-AM2);
    CFTS048-1 preset/driver delegation; the A-AM15 citation scheme
    itself; version labels that do not identify content (CIP tables /
    Market Configuration v1.6 — four releases, four hashes)
- Anomaly register: A-AM01…A-AM16. RESOLVED: A-AM01–A-AM10, A-AM15,
  A-AM16. PENDING: A-AM11, A-AM12, A-AM13, A-AM14, plus the A-AM08
  residual pairs above.
