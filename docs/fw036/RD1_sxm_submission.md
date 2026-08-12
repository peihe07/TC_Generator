# RD-1 — SXM (FW036 SiriusXM 360L SAT Only) — Submission Draft v1

- Workbook: `FM-WI-FSM-036-A01 …_SWQT_SXM_20260810.xlsx` (form revision C;
  ChangeHistory revision D), SHA256 `7b6e760d524fb79e…7538a02`
- Requirement basis: `SWE1_SXM_FM-WI-FSM-037-A03 … SWRA_20260406` — 202
  leaves, 202/202 covered, 215 rows
- Spec line: CFTS024 §1.5.x, clause text read from the ReqIF export, printed
  section numbers from the docx (DECISIONS §1 HYBRID ruling)
- Prepared: 2026-08-12 (analysis layer). Sending is Tier 3 (Pei).
- Ordering per FEATURE_ONBOARDING §7: systemic classes first, then
  requirement-set questions, then wording confirmations, then FYI. Every item
  carries the anomaly id, one-line evidence, the disposition already taken
  locally, and the requested upstream action. **Class-2 items marked
  EXPEDITED carry a live risk in a delivered assertion** — a late answer
  costs a rework, not a footnote. No item blocks delivery: every disposition
  is built so that a contrary answer changes strings, not content.

---

## 1. Systemic defects (class-level remedies requested)

### S1 — Cross-reference short-id scheme resolves nowhere [A-SX02]
- Evidence: six cross-reference tokens — `CFTS024-193/195/197` (leaves 005,
  080), `CFTS019-494/496` (leaf 107), `CFTS020-138` (leaf 137) — resolve in
  none of the four independent released formats we hold: docx paragraph
  anchors, the CIP table workbooks, the ReqIF exports of CFTS019 / CFTS020 /
  CFTS024 (1,989 / 2,644 / 1,604 clause objects, all id and reference
  attributes searched), and the 037 itself. `193`/`195` occur only inside the
  body of clause `4872862` — the citing clause itself. The AM/FM delivery
  reports the same class (37 tokens), so this is a document-family property.
- Disposition taken: cite-form — the borrowed outcome is asserted in the ER
  anchored to the verbatim token; the cited document's own rule surface is
  not tested; the token is carried as an additional specification reference.
- Requested action (class remedy): publish the short-id ↔ current-anchor
  mapping, or re-issue cross-references in the 7-digit anchor scheme. Either
  answer upgrades our citations mechanically.

### S2 — 037 Requirement Titles are truncated at the first sentence [A-SX19]
- Evidence: measured across the VR-bearing leaves (002, 003, 006, 014, 030),
  each title ends at the close of its clause's first sentence and drops the
  second sentence's behaviour — state entry, adjacent-channel move,
  wrap-around. The truncation is positional, not selective, so it is not
  confined to these five.
- Note the direction differs from the AM/FM S3 class: there, titles omitted
  wording the clause carried. Here the cut is structural.
- Disposition taken: TCs are generated from clause text, so no behaviour was
  lost; titles are treated as non-normative labels.
- Requested action (class remedy): regenerate titles from full clause text at
  the next 037 revision, or state that titles are non-normative summaries.
  Per-title patches would leave the next truncation undetected.

### S3 — Version labels do not identify content [A-SX06; merged AM/FM + SXM]
- Evidence: `SR24 R1 Market Configuration Table v1.6.xlsx` is byte-different
  in all four releases under one unchanged label (4 distinct SHA256);
  `CIP_Radio_Tables_v6.7.xlsx` likewise; the SXM SYSAD has three files on one
  document line with three hashes.
- Disposition taken: every reference document is release-pinned and
  hash-recorded at intake; cross-feature copies are hash-verified both sides.
- Requested action: version by content — change the label whenever the
  content changes, or publish per-release digests.

---

## 2. Requirement-set questions

### Q-SX2 — Which score-update listing is live, 4872918 or 4872919? [A-SX18] — **EXPEDITED**
- Evidence: two adjacent clauses in §1.5.12.1.2 describe the same
  single-match score-update flow and disagree on the resulting screen.
  `4872918` (allocated to leaf 120) lists all games that have score updates;
  `4872919` (unallocated) lists games that are starting as well as the score
  updates.
- Disposition taken: §8.6 — the 037 allocates `4872918`, so its text governs;
  leaf 120's second TC asserts that a game without a score update is not
  listed. The positive-only formulation was rejected: a screen listing
  everything would satisfy it (false-pass hole).
- Questions: (1) which clause is live — is `4872919` a superseded draft?
  (2) if `4872919` is live, is `4872918` withdrawn, and should the On Air
  screen list starting games and score updates together?
- Why expedited: the answer changes a delivered assertion. The row carries an
  `[A-SX18]` marker, so an amendment is a grep and a one-line edit.

### Q-SX3 — VR trigger path: the 037 titles declare it [A-SX19] — **EXPEDITED**
- Evidence: five leaves (002, 003, 006, 014, 030) carry a Voice Recognition
  trigger path in their clauses, and **all five 037 titles state
  `or a VR Command` verbatim**.
- Disposition taken: the VR path is excluded from this workbook and delegated
  to the CFTS028 (Voice Recognition) delivery — re-ruled knowingly after the
  measurement above, on the ground that CFTS028 owns the VR requirements and
  authoring VR tests here risks double coverage of another delivery's scope.
- Questions: (1) is the VR trigger path for these five behaviours verified by
  the CFTS028 delivery, and under which requirement ids? (2) if it is not,
  the VR path is verified nowhere — should these leaves carry a VR test case
  in this workbook after all?
- Why expedited: if the answer is (2), five rows gain a test case. The rows
  carry `[A-SX19]`.

### Q-SX4 — §1.5.21.2 Performance: acceptance criteria requested [A-SX25]
- **This is the highest-value question in this delivery.** Of the section's
  20 leaves, **16 state a property with no threshold, tolerance or
  measurement method, 3 are partial, and exactly 1 is fully determinate**:

  | criterion | shape | leaves | n |
  |---|---|---|---|
  | usable | concrete behaviour, determinate pass condition | 184 | 1 |
  | partial | bound stated, measurement method absent | 197, 198 | 2 |
  | partial | threshold named but never valued | 187 | 1 |
  | none | "without user-perceivable delay" | 188–191 | 4 |
  | none | defect-absence over an unbounded window | 192–196 | 5 |
  | none | "proper" / "consistent" / "harmonized", relative to other HMI elements | 199–202 | 4 |
  | none | intent prose and design statements | 183, 185, 186 | 3 |

- Disposition taken: no threshold was invented. Writing "completes within
  200 ms" would have produced tidy rows and placed an unratified acceptance
  criterion into a delivered workbook a supplier would be held to. Instead
  each TC fixes what can be fixed and leaves the judgement visible: a defined
  360L exercise set is written identically into every qualitative test's
  pre-conditions; defect-absence tests require a frame-by-frame recording
  review, separating "no defect occurred" from "nobody was watching";
  delay tests are repeated five times and compared against each other;
  the relative-appearance tests capture 360L-drawn and non-360L-drawn
  elements in the same frame; `197`/`198` are measured and subtracted.
- Questions:
  1. What time bounds the four "user-perceivable delay" clauses (188–191)?
  2. Over what duration and operation set are 192–196 to be observed?
     Absence claims need a window.
  3. What tolerance applies to "proper", "consistent" and "harmonized"
     (199–202), and what is the list of theme elements for 202?
  4. Is 186 ("should be parameterized") a verifiable requirement or a design
     note? It has no pass criterion and its subject is implementation
     structure, not observable behaviour.
  5. What is the value of `T<OD Response>` (leaf 187)? The clause makes the
     buffering notification depend on its expiry and no clause in the section
     assigns it a value, so the row cannot state when "late" begins.
  6. For the 500 ms variance in `197`/`198`: over which set of user
     operations is it computed, how many samples, and between which two
     events is timing started and stopped? The bound exists; the population
     does not.
- Consequence if unanswered: these rows are honest but weak, and weak because
  the requirements are — a tester can execute all of them and a defect can
  still ship, because the clauses do not say what failure is.

### Q-SX5 — Is market-configuration behaviour in scope of this workbook? [A-SX22]
- Evidence: two configuration-gate clauses are unallocated —
  `4872750` (§1.5: SXM display and functionality provided if the SXM chip is
  equipped) and `4872960` (§1.5.16: if `$Country_Code$ = [Canada]` the Jump
  function is not displayed at all). Both fail the absorption test for the
  same structural reason: every leaf in their section is exercised under a
  configuration in which the gated feature is present, so no leaf's scenario
  can observe its absence. `4872960` is the sharper case — a whole feature
  disappears in a market the requirement metadata itself names.
- Disposition taken: recorded as coverage holes; no leaf invented.
- Question: is market-configuration behaviour in scope here? One ruling
  covers every gate clause. If in scope, these clauses need leaves — the 037
  provides none. If not, they should be recorded as out-of-scope rather than
  as coverage holes.

### Q-SX6 — Leaf 177's clause is a pointer note [A-SX24]
- Evidence: `4873290`, allocated to leaf 177, reads in full: a request to see
  the HMI logic & flow for the message shown when SAT is pressed while the
  subscription is inactive. It states no HU behaviour, yet it is typed as a
  Subsystem Functional Requirement and therefore produced a leaf.
- Disposition taken: the 202/202 coverage claim does not permit silently
  dropping an allocated leaf, so the row is written to the maximum the clause
  supports — pressing SAT with the subscription inactive displays a message
  and does not enter playback, with the subscription-active case as control
  so a permanently displayed message cannot pass. The message text is not
  asserted; the clause itself delegates it.
- Question: should `4873290` be withdrawn as a note, with leaf 177's coverage
  carried by leaf 176 (`4873289`, the no-subscription message and its
  contents)? The two are adjacent and 176 is the substantive one.

### Q-SX7 — Why does 4873295 have no leaf when its twin 4873296 does? [A-SX26]
- Evidence: `4873295` specifies, in one clause, a trigger (a Global Channel
  Information update arriving over the air while satellite audio or Travel
  Link is playing), the message text, an audio consequence, and a
  persistence requirement across SDARS and Travel Link screens. All of it is
  HMI-observable. No leaf carries it. Its structural twin `4873296` (the PSV
  update message, the next clause in the same section) does have a leaf, and
  cannot absorb it: a GCI update and a PSV update are different over-the-air
  events, so one test cannot observe both.
- Disposition taken: gap recorded, no leaf invented. A self-supplied leaf
  would make the workbook claim coverage of a requirement the 037 never
  allocated — the one direction a coverage table must not drift, because a
  later reconciliation could not distinguish an invented leaf from a
  transcription error.
- Question: is the omission an oversight? If so the 037 needs a leaf and this
  delivery needs one more row.

### Q-SX9 — Allocation policy for clauses that reach no leaf [A-SX08]
- Evidence: 38 CFTS024 §1.5.x clauses (32 SFR) reach no leaf. Several gaps
  are whole sections with zero leaves — §1.5.8, §1.5.12.1.5+, §1.5.18,
  §1.5.21.1, §1.5.21.2.1. The distribution is uneven, so this is asked as an
  allocation-policy question, not asserted as systematic omission.
- Disposition taken: where an unallocated clause elaborates an allocated
  leaf's cited clause in the same section, its behaviour is absorbed into
  that leaf's TCs, marked `[A-SX08]` and multi-cited. Whole-section gaps
  cannot pass that test — they have no leaf to elaborate — and are recorded
  as holes, never silently absorbed.
- Questions: (1) please confirm the absorption reading, or allocate these
  clauses to leaves explicitly in the next 037 revision. (2) if any clause is
  intentionally out of scope, please state so — the TC side will retract the
  corresponding coverage.

---

## 3. Wording confirmations (answer changes strings, not content)

### Q-SX1 — Four Game Zone categories, or two renamed with both drafts surviving? [A-SX17]
- Evidence: three clause pairs in §1.5.12.1.2 / §1.5.12.1.4 carry bodies that
  are identical or differ only in the category name — Add Teams / Select
  Teams (`4872913`/`4872914`), Edit Teams / Edit Selection
  (`4872915`/`4872916`), Edit Favorites / Edit FAVs (`4872927`/`4872930`,
  the latter additionally naming `Delete All`).
- Disposition taken: no section-ownership carve is available between
  same-section siblings, so each TC enters through its own category name —
  the sole textual difference. The six rows carry
  `Same-text sibling: CFTS024-<paired id>` in Remarks.
- Questions: (1) are the paired names two distinct categories in the HMI, or
  one category renamed with both drafts left in the document? (2) if a pair
  is one category, which name is live and should the other be withdrawn?
- Consequence if unanswered: the delivery promises to test four Game Zone
  add/edit paths and two Favorites edit paths; if any does not exist, that
  row fails on a document defect, not a software defect.

### Q-SX8 — Align 4873277's Description wording with SFR 4873284 [A-SX23]
- Evidence: in §1.5.19, `4873277` (the section's only Description) says the
  HU maintains a table of skipped **channel numbers**, while the allocated
  SFR `4873284` stores the **Service ID**. The normative pair does not
  conflict: `4873278` says "skipped channels" without naming a key. The
  contradiction is Description prose against an SFR.
- Disposition taken: the key is not ruled locally — that would override an
  allocated clause's own text by inference. Leaf 168 asserts persistence
  without naming the key; leaf 175 follows `4873284` through a renumber
  construction. The row carries `[A-SX23]`.
- Question: please align the Description wording with the SFR, or state which
  is normative if the difference is intended.

---

## 4. FYI — no action requested

- **F1**: CFTS024 states requirements in both the analog (§1.3.x) and
  satellite (§1.5.x) chapters under distinct ids. A full-corpus sweep finds
  **11 twin pairs at ≥0.95 similarity — 9 word-for-word identical, 2
  differing only in band vocabulary** ("Tuner" → "Satellite Audio"). Each
  deliverable covers its own chapter's clause; the eleven SXM rows carry
  `Analog-chapter twin: CFTS024-<analog id>` in Remarks. Noted because an
  amendment to one chapter silently leaves its twin stale.
- **F2**: rows whose interpretation rests on an open question carry a bracket
  marker in the reasoning field — `[A-SX03]` (11 rows: leaves added outside
  the release process, blank Release Version and Status), `[A-SX07]` (2),
  `[A-SX08]` (5, absorbed clauses), `[A-SX18]` (2), `[A-SX19]` (5),
  `[A-SX23]` (9). They exist so that an upstream answer is a grep and a
  scoped edit rather than a re-derivation.
- **F3**: `Estimated Test Time` (column Q) is left blank on all 215 rows.
  Form revision C introduced the column and no fill policy exists; estimating
  without a source would put an unratified number into the deliverable.
  Please state the expected fill and we will populate it corpus-wide.
- **F4**: source clauses carry recurring spelling errors which our Test Items
  quote verbatim — `recieve`, `continously`, `Fowarding`, `taffic`.
  Quotations are kept faithful so a Test Item can be diffed against its
  clause; silent correction would break that. A spelling pass at the next
  CFTS revision would be welcome.
- **F5**: this workbook uses `NR1L-SXM-{NNN}` in the Test Case ID column; the
  earlier AM/FM delivery in the same programme uses `newR1L-AMFM-{NNN}`. Same
  project — the format was revised after that workbook was sealed and its
  delivered ids were left unchanged.
- **F6**: **delivery flag** — the 19 non-determinate Performance rows
  (16 with no acceptance criterion, 3 partial) are the weakest evidence in
  this workbook and should be read as such rather than as equivalent to the
  functional rows. Leaf 184 is explicitly excluded from this flag: it is an
  ordinary functional requirement with a determinate pass condition that sits
  in §1.5.21.2 by section-assignment accident.
- **F7**: reproducibility — re-running the writer reproduces the delivered
  SHA256 only when the run is pinned with `--date 2026-08-12`; without it the
  writer falls back to the current date and the digest drifts.

---

Attachments: unallocated-clause list with scope tags (Q-SX9, Q-SX5, Q-SX7);
§1.5.21.2 leaf classification table (Q-SX4); cross-chapter twin list (F1);
version/hash table (S3).
