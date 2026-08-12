# DECISIONS — SXM (FW036)

Pre-filled by recon.py. Markers per FEATURE_ONBOARDING §4; an
unsigned sheet blocks Phase 4+. `[PROPOSED]` untouched at
sign-off = binding as proposed.

> Re-running `recon.py` regenerates this file and drops the hand-added items
> below. Re-apply them from RECON.md's "Recon extras" section if that happens.

## 1. Intake
- spec_mode: [AUTO] A — **CHALLENGED, see below; do not sign as-is**
- spec text layer: [AUTO] text-layer: 112110 chars (both PDFs probe 100% of pages)
- source files: [AUTO] 9 present (SHA256 in RECON.md)

- **spec line — [PEI 2026-08-10: D main line (CFTS024 clause ids) + A as the
  second source — signed as proposed]**. intake.py proposed `A` from the presence of a SYS1
  export. The 037 disagrees: **202 of 202 leaf titles carry a 7-digit id and
  all 202 land on an exact CFTS024 clause anchor** in §1.5.x — the same
  mechanism AMFM uses on §1.3.x of the same document. (The first Phase 1 pass
  reported 191/202; the 11 "misses" were an end-of-string anchor in the
  extraction pattern, not untagged leaves — A-SX01.) Under `A` the
  spec_reference would be a SYS1 outline number while the requirement text is
  quoting CFTS024 clauses. If ruled `D`: `spec_reference_template` becomes
  `{doc}-{stla_id}`, AMFM's bracket-map script is reusable nearly as-is, and
  the SYS1 export/PDF become the figure and flow source (mode C role) rather
  than the citation source.
- CFTS024 clause ingestion — **[PEI 2026-08-10: HYBRID]**. Ruling text:
  「CFTS024 條款來源 = ReqIF 屬性直讀；印刷章節編號 = docx 標題解析
  (HEADING_RE 保留)；bracket map = 驗證器，雙路徑逐 leaf 全量比對；
  驗證器不一致 = fail-loud ABORT（比照 write-back invariant，不是警告）
  ——不一致代表某份匯出已變動，屬 escalation trigger，回 chat 裁，
  不得弱化。」Scope: removes only the CFTS024-side paragraph-anchor
  inference (PARA_ANCHOR_RE, monotonic-anchor invariant, bisect lookup, the
  "clause = text to next marker" assumption); **037-side title parsing is
  outside this ruling** — the A-AM01 (fullwidth brackets) and A-SX01
  (trailing markers) guards stay exactly where they are. Evidence gate
  passed before ruling: id presence 202/202; clause text 202/202 identical;
  printed numbering reproduced 202/202 via the ReqIF-tree-ancestor →
  docx-heading join (`SXMHMI/docs/reqif-vs-docx.md`; reader
  `SXMHMI/scripts/reqif_reader.py`; sources `.reqifz` 325dba60… /
  6a5b81a5…, same 25PI3.5 release as the docx, 15-minute export gap).
- **version baseline — [PEI 2026-08-10: SR24 1A (SAT Only) stays the spec
  line; the 26PI2.5 file is reference-only — signed as proposed]**. RD-1
  addition ruled with sign-off: ask upstream whether the full 360L document
  will spawn its own 037 leaf set, so the streaming surface is recorded as an
  upstream scoping fact, not a local omission. The two files are not two revisions of one
  document: SAT-only 85pp (May 2021) vs full 360L 230pp (SR24 Post 2A, Dec
  2021); 19 exact page-title matches, 211 pages only in the newer file, 21
  baseline pages with no counterpart. Its change log carries one CR. Ruling the
  newer file in widens the surface to 360L streaming features the 037 carries
  no leaves for, and breaks alignment with the SYS1 export. **If Pei rules the
  other way this is not a re-run but a re-scope** — the 037 leaf set has to be
  re-checked against the wider document first.
- missing document — [PEI 2026-08-10: RESOLVED — the file exists, it was not
  supplied at intake]. Three versions found at `…/02_Project_R1LR/9_ASPICE/
  03_SYS.3 System Architectural Design/Radio/`: `SYSAD_20260323`,
  `SYSAD_20260511`, `SYSAD_v0.2_20260629`. Ruling: copy
  `SYS3_SXM_FM-WI-FSM-011-A01 系統架構設計 System Architectural
  Design_SYSAD_v0.2_20260629.docx` into `inputs/` (same batch and version
  format as AMFM's SYS3). Three same-line versions coexisting goes to RD-1 as
  an observation item (Market Config v1.6 precedent). First row of
  `SXMHMI/DATA_REQUESTS.md` at creation.

## 2. Workbook survey
- workbook_state: [AUTO] BLANK
- form layout revision: [AUTO] C (has Estimated Test Time)
- column mapping: [AUTO] 15 fields resolved from header text
- done segments: [AUTO] none
- ambiguous rows: [AUTO] none
- draft disposition: [PEI 2026-08-10: discard & regenerate — signed as proposed]
  The 2 "draft" rows are the blank form's own template rows (`D10`/`D11` =
  `xxx`), not authored content; they are cleared at write-back.
- **form layout — [PEI 2026-08-10: ship on revision C — signed]**. Estimated
  Test Time fill policy ruled with sign-off: **left blank at generation**,
  noted in the delivery cover, and raised as an RD-1 question on the expected
  fill — estimating without a source is §8.4-adjacent fabrication, and `NA`
  reads as refusal. Write-back can fill the column corpus-wide later if the
  answer defines a rubric. This workbook is a scaffold
  copy of the blank form (SHA256 `cd876c20…`), which is revision C: it adds
  `Estimated Test Time` at **Q** and shifts design_method → R, functional_safety
  → S, the vehicle block → T..Z, author → **AA**, remarks → **AH**. Every
  instance shipped so far (Home, AMFM, and the 18 other 036 workbooks in the
  project tree) is revision A/B. Two things to weigh: no feature has been
  generated on revision C before, and the new `Estimated Test Time` column has
  no ruled fill policy — blank on 202 rows is visible to the customer.
- **workbook filename — [PEI 2026-08-10: `…_SWQT_SXM_20260810.xlsx` — signed
  as proposed]**. AMFM's
  instance is `…_SWQT_CFTS024_Radio_20260129`; SXM's spec line is not a single
  CFTS, so the feature name is used. Rename before delivery if the customer
  expects a CFTS-keyed name.
- F column (test case id): [PEI 2026-08-11: `NR1L-{abbr}-{NNN}` — SXM uses
  `NR1L-SXM-{NNN}`, zero-padded 3-digit, monotonically increasing within
  the group (§10.3). Scope ruled (a): the format applies to SXM and all
  subsequent deliveries; the delivered AMFM workbook keeps
  `newR1L-AMFM-{NNN}` frozen — its output hash is sealed in tag
  fw036-amfm-regen-v1 and re-keying would reopen a closed delivery. The
  prefix difference across the family is recorded in RD-1 as an FYI line.]
- O column (status): [PEI 2026-08-11: `NEW` — uppercase, per the workbook's
  dropdown values.]
- design-method vocabulary: [AUTO] 9 exact strings from 下拉選單

## 3. Coverage
- 037 leaves: [AUTO] 202
- safety attributes: [PEI 2026-08-10: signed as proposed — ruled source
  carries no ASIL/FTTI column; the SYS2/SYSRA safety layer does not enter the
  trace chain (AMFM R6 precedent)]
- regen targets: [AUTO] 202 (list in recon.json)
- covered nowhere: [AUTO] 202 ['SWE-RA-SXM-001', 'SWE-RA-SXM-002', 'SWE-RA-SXM-003', 'SWE-RA-SXM-004', 'SWE-RA-SXM-005', 'SWE-RA-SXM-006', 'SWE-RA-SXM-007', 'SWE-RA-SXM-008'] … +194 more (full list in data/recon.json) — ANOMALIES entries required
- workbook req_ids absent from 037: [AUTO] done=0 (none) draft=1 ['xxx'] — ANOMALIES + RD-1 required; scope the write-back traceability invariant to regen rows only

## 4. Style bindings
- style authority: [PEI 2026-08-10: fallback chain — signed, no done region]
- test item shape: [PEI 2026-08-10: standard §4.3 tc_title — signed]
- test group/set columns: [PEI 2026-08-10: FILL per framework Part N — signed]
- exemplar source: [PEI 2026-08-10: **AMFM done region** (same document
  family, same `{doc}-{stla_id}` format), marker `cross-feature: style only`;
  every literal re-traced to the SXM spec line, enforced as lint (A-026
  precedent) — signed]
- author on new rows: [PEI 2026-08-10: PeiPYHsu — signed]
- spec_reference: [PEI 2026-08-10: `{doc}-{stla_id}` e.g. `CFTS024-4872752` —
  signed; §1 spec line ruled D, so the outline variant lapses]
- cross-document short-id citations: [PEI 2026-08-10: R11 cite-form adopted
  for SXM — scope and upgrade condition recorded verbatim in A-SX02; carries
  into the Phase 3 profile as an [OVERRIDE] clause]
- **cross-feature overlap — [PROPOSED: option (i), each feature covers its own
  clause; no cross-citation]**. Measured after the first Phase 1 pass: SXM
  110/148/149 and AMFM 023/047/049 carry word-for-word identical text
  (similarity 1.000) but **different clause ids in different chapters** —
  `4872901`/`4872952`/`4872954` in §1.5.x against `4872430`/`4872506`/`4872508`
  in §1.3.x. CFTS024 simply states these requirements once per band family, so
  neither deliverable claims the other's clause and there is nothing to
  arbitrate. Pre-pilot condition attached in A-SX04: re-run the comparison
  across all 202 leaves at ≥0.95 and list any pair where the SAT wording has
  diverged, since option (i) rests on the two clauses staying identical.
  **[PEI 2026-08-10, amended same day: generate all three normally — no
  cross-citation.]** A-SX04 measurement shows 110/148/149 cite their OWN
  §1.5.x clause ids (4872901 / 4872952 / 4872954); the AMFM twins are
  different ids in §1.3.x — never a coverage conflict. SXM generates the
  three as SAT-context TCs tracing their own clauses; AMFM keeps 023/047/049
  as delivered; nothing withdrawn, nothing cross-cited. The earlier
  "citation rows" wording in this entry misread the registered disposition
  label and is VOID. Remarks on each of the three rows:
  `Analog-chapter twin: CFTS024-<analog id> (covered in the AM/FM
  deliverable)` — clause id only, never AMFM TC ids (TC ids are assigned at
  write-back and shift on any AMFM regen; clause ids are stable and
  self-evident inside CFTS024). Pre-pilot whole-corpus ≥0.95 text comparison
  stands, its output repositioned as the "CFTS024 cross-chapter twin list"
  feeding the merged RD-1 FYI.

## 5. Split & scope
- split_mode: [PEI 2026-08-10: standard — signed as proposed]

## 6. Framework & profile
- Test Set table (Part N): [PEI 2026-08-10: SIGNED — framework.md Part IV
  (14 Sets, 202/202; Instant Replay/Browse unsplit per §4.2, Favorites/
  Activation split, Source Availability outlier); batch plan B1–B14]
- profile [OVERRIDE] clauses: [PEI 2026-08-10: delta list signed —
  `{doc}-{stla_id}` + HYBRID pointer; R11 cite-form (4 leaves) + ported
  lint gates; twin mirror Remarks (11 rows, external language); Estimated
  Test Time UNRULED_BLANK; [A-SX03]/[A-SX07]/[A-SX08] markers; Test
  Group/Set FILL; R8-equivalent NOT auto-inherited — first VR-wording
  occurrence returns to chat. Claude Code instantiates
  `FW036_R1L_SXM_Profile.md` from the AMFM profile + this delta]
- R10-2 absorption: [PEI 2026-08-10: ADOPTED for SXM — ruling verbatim in
  framework Part IV note 5 and ANOMALIES A-SX08; marker `[A-SX08]`;
  whole-section gaps → RD-1 Q-SX allocation-policy question]

## 7. Execution
- batch plan: [PEI 2026-08-10: group 202 targets by spec chapter — signed;
  pilot batch = §1.5.10.x Instant Replay / Pause / Fast Forward (19 leaves):
  mid-sized, state-machine dense, best early exposure of style and split
  drift. Amended same day: pilot ADDITIONALLY includes leaf 154 — it stacks
  three markers ([A-SX03] + [A-SX07] + §8.6 wording note), so the marker
  mechanism is validated on the most complex leaf first]

---

## Sign-off

- Reviewed by: PeiPYHsu  Date: 2026-08-10
- Overridden items: §1 SYSAD (ABSENT → resolved; copy v0.2_20260629 into
  inputs/); §2 form layout (Estimated Test Time policy added: blank +
  delivery note + RD-1 question); §4 cross-feature overlap (ruled option i,
  citation rows, with pilot-front context re-check condition)
- Ruling notes: directive「照簽/改裁」(chat, 2026-08-10) — all [PROPOSED]
  items signed as proposed; the three items above carry the 改裁 content.
  Recorded by Claude (analysis layer) on Pei's directive; ruling text
  expanded from the chat recommendation table.
- Amendment (2026-08-10, second pass): post-recon-extras rulings — A-SX03
  generate + mark; §4 cross-feature entry corrected (generate normally, no
  cross-citation — the "citation rows" text was a label misread, now void;
  Remarks carry the analog clause id, not AMFM TC ids); A-SX07 reading (a);
  pilot scope + leaf 154. Rulings recorded verbatim in ANOMALIES.md.
- Amendment (2026-08-10, third pass): A-SX02 ruled — R11 cite-form adopted
  for SXM with reqifz upgrade condition (§4 entry added). All anomalies now
  RESOLVED; no PENDING items remain ahead of Phase 3.
- Amendment (2026-08-10, fourth pass): CFTS024 clause ingestion ruled HYBRID
  (§1 entry) — directive「混合」: ReqIF clause source + docx printed
  numbering + bracket map as fail-loud validator; CFTS024-side scope only.
  A-SX02 upgrade branch closed the same day (six tokens absent from all
  three ReqIF exports — fourth independent format; cite-form final).
- Amendment (2026-08-10, fifth pass): Phase 3 signed — framework Part IV
  (Test Group SXM, 14 Sets, B1–B14), profile delta list, R10-2 adoption
  (§6 entries; ANOMALIES A-SX08). Phases 0–3 complete; Phase 4 wiring +
  B1 pilot assembly cleared (Tier 1).
- Amendment (2026-08-11, sixth pass): VR trigger path ruled — R8-equivalent
  ADOPTED for SXM (A-SX10): VR wording excluded from workbook scope,
  delegated to the CFTS028 delivery; touch/H-K paths only; title-states-VR
  escape hatch; five affected TCs get reasoning annotations (field-level,
  no batch blocked). This supersedes the §6 profile clause "first VR-wording
  occurrence returns to chat" — the first occurrence returned, and this is
  the ruling. B5 §1.5 absorption mini-review recorded in A-SX08 follow-on:
  14/14 not absorbed, coverage holes to RD-1 Q-SX, `4872750` named as the
  configuration-gate exception.
- Amendment (2026-08-11, seventh pass): delivery-chain rulings, directive
  「1 照簽 2 照簽 3 照簽 4 照簽」— (1) A-SX20 standing carve + rolling
  register; escape hatches: (i) content-contradiction pairs return to chat
  (fired once: A-SX23 finding 1), (ii) cross-section pairs stay A-SX15-type.
  (2) A-SX21 citation travels on NECESSITY threshold only — full R11
  treatment, token co-listed with the absorbed clause id (three-hop chain
  visible in the deliverable), cross-reference gate exception keyed to that
  co-listing (A-H10 validation shape); 148/149 threshold evaluation before
  write-back, expected to pass and gain one ER line + reference pair.
  (3) A-SX23 key NOT ruled locally — shipped carve stands (168 persistence
  without asserting the key, 175 per its own clause 4873284), `[A-SX23]`
  marker on 175, RD-1 class-2 expedited framed by the renumber-unskip
  failure mode; a contrary answer is grep + wholesale ER replacement on one
  row. (4) 4873295 coverage hole, NO self-added leaf (§8.2 discipline,
  A-AM13 precedent), RD-1 Q-AM3 wording. Sequencing ruled: write_back
  first; RD-1 assembly by chat on final numbers; §1.5.21.2 weakness note +
  UNRULED_BLANK into the delivery cover. Cross-reference correction: the
  sixth-pass label "A-SX10" for the VR ruling now lives at A-SX19 after
  renumbering; A-SX10 is the 082/083 title finding.
- Amendment (2026-08-11, eighth pass): repo reorganisation RATIFIED after
  the fact (directive「追認」). The 2026-08-10 rename ruling scoped the
  change to AMFM only, leaving HomeHMI / mediaHMI / SXMHMI and the
  `<Feature>HMI` scaffold convention untouched; the reorganisation executed
  on 2026-08-11 moved all four features to `features/{amfm,home,media,sxm}`
  and added `archive/`. That exceeded the ruling. Pei ratifies the executed
  state rather than reverting — the delivery chain is mid-flight and a
  second move costs more than it returns. Consequences ruled with the
  ratification: (a) the "AMFM only" scope ruling is SUPERSEDED, not
  violated-and-standing; (b) the `<Feature>HMI` scaffold convention in
  `intake.py` / `new_feature.py` is now inconsistent with the on-disk
  layout — a follow-up canon pass owes the naming and the
  FEATURE_ONBOARDING wording; (c) reorganisation acceptance evidence is
  still owed and NOT waived by this ratification: three-category
  reference-sync grep report, 923 green, and the Project operating-charter
  path re-sync (its `<Feature>HMI/PLAYBOOK.md` pointers are stale).
- Amendment (2026-08-11, ninth pass): F/O column rulings recorded in §2
  above, and A-SX23's RD-1 disposition corrected on new evidence.
  (1) **F column ruled, scope (a)** — `NR1L-{abbr}-{NNN}`, SXM instance
  `NR1L-SXM-{NNN}`. Applies to SXM and every subsequent delivery; the
  delivered AMFM workbook keeps `newR1L-AMFM-{NNN}` frozen because its
  output hash is sealed in tag `fw036-amfm-regen-v1`. The family-level
  prefix difference is an RD-1 FYI line, to be added to the AMFM RD-1
  class F when the SXM submission is issued: *"This delivery uses
  newR1L-AMFM-{NNN}; subsequent deliveries in the same programme (starting
  with SXM) use NR1L-{abbr}-{NNN}. Same project, format revised after this
  workbook was sealed."* Implemented as `write_back.tc_id_format` in
  `feature.yaml` + `assign_tc_ids` in `write_back.py`; the ruling also
  removes the `NR1L-AntiTheft-001` template residue from F10, which
  previously survived only because F was left unwritten.
  (2) **O column ruled** — `NEW`, uppercase, per the workbook's dropdown
  values. Already the shipped value (`tc_ref_id_value`); recorded so it is
  a ruling rather than a default.
  (3) **A-SX23 — a correction to Amendment 7 (3), not a reversal.** The
  ruling body stands unchanged: the identification key is still NOT ruled
  locally, the shipped carve stands (168 asserts persistence without
  naming the key, 175 asserts its own clause `4873284` through the
  renumber construction), and the `[A-SX23]` marker stays on 175 — a
  contrary answer is still a single-row ER replacement, so the mechanism is
  untouched. What changes is the RD-1 disposition, on evidence read out of
  the §1.5.19 artifact types after the ruling was made: `4873277` is the
  section's only **Description**; the seven others are **Subsystem
  Functional Requirements**, and the normative pair does not conflict —
  `4873278` says "skipped channels" without naming a key, `4873284` fixes
  it as Service ID. The contradiction is Description prose against an SFR,
  not two normative clauses. Consequences: **class-2 expedited → class-3
  wording confirmation**, and the question is re-put as a wording-alignment
  request rather than a behavioural one — *"4873277 (Description) says
  'skipped channel numbers' while the allocated SFR 4873284 stores the
  Service ID. Please align the Description wording with the SFR, or state
  which is normative if the difference is intended."* The carve is harder
  under this evidence, not softer: artifact-type hierarchy (SFR over
  Description) now backs it alongside §8.6. Evidence table filed in
  ANOMALIES A-SX23.
- Amendment (2026-08-12, tenth pass): dry-run return — directive「好裁」,
  three items, taken as adopting the chat recommendations verbatim.
  (1) Marker notation unified to bracket form [A-SXnn] across the whole
  workbook. The report showed A-SX23 at 0/9 and A-SX07 at 1/2, while
  Amendments 7(3)/9 rule that the [A-SX23] marker sits on 175 — the ruled
  grep handle did not exist. Markers exist to be grepped when upstream
  answers; mixed notation makes the next reader miss nine rows. Convert all
  nine A-SX23 rows and leaf 153's A-SX07 to bracket form; this also settles
  the earlier open question (全域行文 vs 全部轉括號) as 全部轉括號.
  (2) --date pin recorded as a delivery condition: without --date the writer
  falls back to date.today() and the output hash drifts daily, silently
  voiding the reproducibility claim. The delivery cover AND the tag
  annotation must state that a re-run requires --date 2026-08-12.
  (3) **WITHDRAWN before execution, premise incorrect — no P0 ruled yet.**
  The item as drafted raised leaf 001 to P0 on the ground that it is "the
  satellite-source availability gate". It is not: `CFTS024-4872752` (§1.5)
  requires the HU to display the **Channel Art image** for the tuned
  channel, and §1.5 holds that single leaf. The error came in two steps —
  the clause was not read before drafting, and the framework Part IV Set
  name `Source Availability` was taken as evidence of content (see the new
  ANOMALIES entry: the Part IV granularity note calls that Set "the
  satellite-source presence gate" while the leaf inside it is Channel Art).
  Withdrawn rather than corrected in place, because the drafted judgement
  criterion was also wrong: "failure makes the whole batch untestable"
  describes a **pre-condition**, not §10.2 priority — under it any
  pre-condition clause would earn P0. The framework's own rule governs
  instead: *priority follows the verification target, not the feature's
  importance*, and a chapter may legitimately contain no P0 — rebalancing
  to "earn" one is expressly forbidden. Replacement route ruled: a
  directed rubric scan for rows whose ER asserts **audio output** (§10.2),
  results returned to chat for a per-row decision. Leaf 001 stays P1.
  (3b) **P0 ruled on the rubric scan (2026-08-12, same pass).** The scan
  found 96 of 215 rows carrying playback vocabulary in their ER and 70
  whose clause itself requires playback or audio; those were sorted by
  what the row actually verifies, and the sort — not a count — is the
  ruling's basis. **22 rows raised to P0**: the rows whose verification
  target IS audio output, so that a failure means no audio, audio not
  muted where the clause requires muting, or playback not resuming at the
  point the clause fixes. Fourteen are Instant Replay (`SWE-RA-SXM-064`,
  `066`, `067`, `068`, `069`, `070`, `071`, `075`, `076`, `084`, `086`,
  `089`, `091`, `092`), and the rest are `062` (tune to the channel
  carrying the favourite), `146`-01 (select from list → tunes and plays),
  `157` (replay the latest T&W broadcast), `178` and `181` (cabin audio
  muted on audio-not-present / antenna fault), and `183`, `190`, `191`
  (no gap in audio; 360L entry and exit). Deliberately NOT raised, each
  for a stated reason rather than by omission: **tune-and-play tails**
  (13 leaves / 18 rows — `002 003 004 006 009 014 017 024 028 030 039 056
  159`) assert "the channel reached is playing" but verify that the HU
  tuned to the RIGHT channel; a failure means the wrong station, not
  silence — the same shape as the framework's `SWE1-MEDIA-INT-022-02`
  worked example, which is P1. **Tone and confirmation-sound rows**
  (`051 057 107 127 167`) verify whether an alert should sound, not the
  audio chain. **Playback-position, playlist and display rows**
  (`063 073 077 078 079 080 081 085 088 090 093 101 122 156 158 179 182
  198`) verify displacement in seconds, list contents or a message
  condition. `146`-02 is excluded although its leaf is raised: that row
  verifies a Satellite Category selection restriction and asserts no
  audio. A narrower "audio completely absent" reading (8 rows) was
  considered and rejected — it is narrower than the rubric's own words
  and would put Instant Replay's pause/resume outside the core, and
  narrowing the rubric needs a rubric basis, which does not exist.
  Consequence: write_back re-run at `--date 2026-08-12`; priority
  distribution **P0=22, P1=181, P2=12**; the delivered digest is now
  `7b6e760d524fb79e3e4f7cafb43be4b2c945d64b9063abb3974a5e9737538a02` and
  it supersedes `903114576ac0dec7…` everywhere that was recorded.
