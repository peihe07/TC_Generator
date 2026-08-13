# PLAYBOOK — AMFM (FW036 TC Generation)

> ## 寫回常設規則 —— R18-3（2026-08-13，取代 R16-2 凍結令）
>
> R16-2 之全 repo 寫回凍結**已解除**。解除依據：探針對 AMFM 客戶原件與
> FW036 空白範本兩次驗證皆 LOSSLESS，且不再有任何重產動作。
> 代之以下列常設規則，即刻生效、適用全 feature：
>
> 1. `backend/xlsx_surgical.py` 為**唯一**寫回路徑；
>    openpyxl 存檔路徑不得用於任何交付件產出
> 2. 寫回後強制比對輸出與輸入之 zip 成員集合、各 sheet 之
>    classic / x14 DV 計數，不等即 **ABORT**（非 warn）；
>    允許差異者僅限被寫入之 sheet XML 本身
> 3. 該 invariant 之違反屬 canon §0 第三項，升 Tier 2，
>    不得以放寬 invariant 解決
>
> 反向測試（R18-4）：`tests/test_xlsx_surgical_invariant.py` —— 兩種
> 破壞模式皆驗證確實 ABORT。裁決全文：`features/amfm/RULINGS.md` R18。
>
> **本 feature**：v1 不重產、tag 不動；v2 保留於 `output/` 不打 tag、
> 不送出，附掛「尚未經 Excel 實開驗證」標籤（R18-2）—— A-AM18 / A-AM19。

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
- [x] P7 — dry-run run twice (latest 2026-08-10, after the R13 F/O
      rulings), then approved, written and tagged. **Executed; 追認 by Pei
      2026-08-13 (R14-C1).** Delivered artefact and its measurements:
      - output: `output/FM-WI-FSM-036-A01 STLA 測試用例規範與結果_SWQT
        STLA Test Case Specification & Result_SWQT_CFTS024_Radio_20260129.xlsx`
        — **171,631 bytes** (per R14-C7 all file sizes are stated in bytes)
      - SHA256: `da18b5b0ca9ee5794b67a31ddd317b4a23decf9e0e88380a3717f823e45f3f22`
        — sidecar / tag annotation / `shasum -a 256` 實測, three-way identical
      - legacy done-region hash (ordered content, columns D..AG, 158 rows):
        **full length** (R15-4 — the tag annotation carries a 16-char prefix
        truncation, which is archived as-is and not amended; every later
        feature records the full digest)
        `30d9e4c0719a29292ff50123ead1003262652fbb8f301e93bf974fd2ee17f30a`
        — prefix `30d9e4c0719a2929`, continuation `2ff50123…`.
        Re-derived 2026-08-13 against the pristine input, v1 and v2: all
        three agree, and agree with `data/legacy_baseline.json`. Per R15-3
        this proves the region has not drifted since generation; it does not
        prove the hash definition itself is right (same definition, re-run).
      - rows: `LEGACY 10-167 (158 preserved, unmoved)` +
        `REGEN 168-310 (143 appended, 0 placeholder)` = **301 total**
      - coverage: 102 regen req_ids == 102 leaf set, exact
      - lint: **PASS** — 143 TCs, 102 leaf files, 0 findings
      - tag: `fw036-amfm-regen-v1`
      - the `.sha256` sidecar sits in `output/` and is **not committed**
        (root `.gitignore:20` excludes `output/`); the authoritative copy of
        the digest lives in the tag annotation — consistent with Projection
        R-P94 and `FEATURE_ONBOARDING` §6
      - **RD-1 送出待 Pei（Tier 3）** — `docs/fw036/RD1_amfm_submission.md`
        照現稿送出 (R14-C6), with the Q-AM2 item 3 addition made under
        R14-C4-d; `docs/fw036/RD1_questions_amfm.md` kept in step

### Open PENDING

Nothing here may be disposed of in Claude Code — all are Tier 2/3.

**Closed by R14 (Pei, 2026-08-13)** — R8 stands（Pei 追認 2026-08-13,
R14-C2），VR 不進本 workbook；DATA_REQUESTS #4 已關列。

- **087/094 and 089/095 `duplicate_of` — ruled per pair 2026-08-13
  (R14-C4).** Both pairs **keep their two TCs**; the delivered v1 is
  unchanged.
  - **087/094 (R14-C4-a)** — 維持雙 TC. `CFTS011-4942534` enumerates the
    connected / not-connected value classes: 087 verifies the four
    information items displayed in the normal state (Functional), 094 the
    not-connected value class and the frequency field following a retune
    (EP). This is the §8.3 negative / value-class axis, not a manufactured
    difference. **Closed.**
  - **089/095 (R14-C4-b)** — 維持現況，不動 v1. The split itself is sound
    under §8.2.2 (`4942540` binds the sampling side and the update side,
    two independent partial failures), but it is inconsistent with
    090/096, which §5.7 keeps as one TC each. The root of that
    inconsistency is upstream: the 037 allocates two leaves to the MW
    clause and one each to AM and FM. Either side would force a re-issue
    of the already-tagged v1, and the correct cut depends on the upstream
    answer — so it is asked instead (R14-C4-d, Q-AM2 item 3) and revisited
    for v2. **Deferred to upstream, not pending here.**
- **A-AM11** rate-to-frequency-step mapping undefined upstream — ER
  asserts monotonicity only (021, 026, 028). PENDING upstream definition.
  **Status: PENDING → AWAITING_UPSTREAM on the day RD-1 is sent (R14-C5);
  resolution condition = upstream reply or the delivery deadline,
  whichever comes first. Not to be changed before Pei confirms the send.**
- **A-AM12** "intelligent entry" undefined beyond its two dependencies
  (030) — revisit against the Market Configuration vocabulary. Not
  blocking. **Same R14-C5 transition as A-AM11.**
- **A-AM13** fast seek specified but reaching no 037 leaf — coverage hole,
  RD-1 (folds into Q-AM3). **Same R14-C5 transition as A-AM11.**
- **A-AM14** Seek Up / Seek Down decomposed differently upstream —
  allocation-policy question, reported with Q-AM3. **Same R14-C5
  transition as A-AM11.**
- **RD-1, all DRAFT, Tier 3 to send** (`docs/fw036/RD1_questions_amfm.md`):
  - **Q-AM1** SWRA-A02 ↔ 037-A03 lineage (A-AM03/A-AM04): earlier-revision
    authoring, the contiguous `SWE-RAD-040…-045` tail, formal supersession
  - **Q-AM2** 037-A03 internal defects (A-AM08/R9): 029's id tail,
    numbering gaps 086/088, the same-id variant pairs, `SWE-RA-RAD-019`
    Description-type artifact hygiene, and — added under **R14-C4-d** —
    item 5, the per-band leaf allocation asymmetry (AM `4942536` /
    MW `4942540` / FM `4942545`: two leaves for MW, one each for AM and
    FM). **`090/096` belongs here, as FYI rather than a pending ruling**
    (R14-C4-c): both carry an empty `duplicate_of`, their clause ids
    differ, and they sit on different bands' leaves, so §8.2.1 forbids
    merging them across leaves — there is nothing to rule on the TC side.
    Moved out of the `duplicate_of` per-pair item above; the A-AM08
    residual is now 087/094 and 089/095 only.
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
