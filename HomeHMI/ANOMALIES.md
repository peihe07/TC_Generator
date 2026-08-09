# ANOMALIES — FW036 Home HMI

Register of ambiguities, spec gaps, and upstream inconsistencies found during
Home HMI TC generation. Machine-searchable marker format: `[A-Hnn]`.
Dispositions marked PENDING require a Pei ruling before the affected batch
runs; RESOLVED entries record the ruling verbatim.

---

## [A-H01] 066 parent/child duplication (RD-1 candidate) — RESOLVED (2026-08-09)

- `SWE1-HMI-HOME-066` (Start Route and Notification Feedback) AND its
  sub-ids `066-01` / `066-02` are ALL marked `Functional Requirement` in 037;
  content is a parent/child decomposition relationship.
- The old draft region covered only -01/-02; the parent 066 had no row.
- **Ruling (Pei)**: 066's content is fully decomposed into -01 (start route)
  and -02 (notification feedback) with no residual content of its own —
  fully-delegated side of the blocked-parent proportion test. 066 gets NO
  independent TC (writing one would duplicate traceability, §8.2.1). Because
  037 marks it Functional Requirement, the completeness invariant still
  requires a placeholder row: Remarks =
  `Covered by 066-01/066-02; RD-1: reclassify 066 as Heading`.
  All TC content traces to -01/-02.
- Affects: batch B5 (unblocked by this ruling).

## [A-H02] 055-03 pure-reference requirement — RESOLVED (2026-08-09)

- `SWE1-HMI-HOME-055-03` text: "Refer to Setting Navigation Shortcuts and
  Phone HMI Logic and Flow for other specific behavior." No testable behavior
  of its own.
- **Ruling (Pei)**: the reference splits in two. "Setting Navigation
  Shortcuts" is the SAME Home spec's SNS section (p.16), whose behaviors are
  owned by sibling leaves 062–071 — sibling delegation per §8.2.1, not an
  external-spec case. Only "Phone HMI Logic and Flow" is a true §8.4.2
  external reference. No independent TC (a reference-integrity TC cannot
  pass the §5.7 single-objective test). Placeholder row: Remarks =
  `Nav-side behaviors owned by 062-071; Phone-side owned by external Phone
  HMI spec. RD-1: confirm Phone project has parallel SWE coverage for
  shortcut exclusion exception`.
- Affects: batch B3 (unblocked by this ruling).

## [A-H03] Last Mode spec release-label mismatch — RESOLVED (2026-08-09)

- `SWE1-HMI-HOME-076` … `-090` (15 leaves) trace to
  `Last Mode Table HMI Logic and Flow R1L-R (August 2 2021)_{n}`.
- The originally recorded disposition (file missing → B7 emits BLOCKED
  placeholder rows) was **wrong**: the file was in `inputs/` all along, under
  a different release label. `inputs/` contains
  `Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021).xlsx`
  (Title sheet: `R1 Last Mode Table`, Spec Release `SR24 1A Post DCR19344`,
  Date **2021-08-02** — the same date as the `R1L-R` label in 037).
- Verified against the file: the `_{n}` suffix is the **List Item** number in
  the 359-row `Last Mode Table` sheet, and all 15 resolve, all with
  `Screen Display Status = HOME`:

  | leaf | item | operation → element | behavior |
  |---|---|---|---|
  | 076 | 1 | From Radio Off (deep sleep / STR), Any Home Screen page | Return to last active Home Screen page |
  | 077 | 35 | From Radio Off (no sleep), Any Screen | Maintain Mode |
  | 078 | 64 | Go to another mode → back, Any Screen | Return to last active Home Screen page |
  | 079 | 155 | Phone interrupt → cancel | Maintain Mode |
  | 080 | 180 | Answer incoming call | Maintain Mode |
  | 081 | 181 | Place call via VR, no Home widget | Go to Phone Current Call/Call Tab |
  | 082 | 182 | Call from Home Screen widget/shortcut | Maintain Mode |
  | 083 | 208 | End call (answered via popup/SWC) | Maintain Mode |
  | 084 | 209 | End VR call, no Home widget | Return to last mode |
  | 085 | 210 | End widget/shortcut call | Maintain Mode |
  | 086 | 236 | Device connected, AutoPlay ON | Maintain page, update media |
  | 087 | 261 | Device connected, AutoPlay OFF | Maintain Mode |
  | 088 | 279 | Device disconnected / source interrupt | Maintain Mode |
  | 089 | 308 | Backup camera interrupt → cancel | Maintain Mode |
  | 090 | 331 | Blind spot view (turn signal) → cancel | Maintain Mode |

- **Ruling (Pei, 2026-08-09): same document.** Independently verified —
  identical date, 15/15 leaves resolve, and each leaf's title matches its
  List Item semantically. The only difference is how the release is labelled
  (037 writes `R1L-R`; the file title writes `R1 SR24 1A`).
- Disposition:
  (a) B7 is **UNBLOCKED** — generate normally, no placeholder rows.
  (b) `spec_reference` uses the **actual file name**, not 037's label:
      `Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021)_{n}`
      where `{n}` is the List Item number. Rationale: the reference must name
      a document the tester can actually locate, which is the intent of
      Profile §3.5. This deliberately diverges from the 037 string.
  (c) RD-1 note asks upstream to confirm `R1L-R` ≡ `R1 SR24 1A Post
      DCR19344`, recorded as residual risk. If upstream denies the
      equivalence, only the `spec_reference` string changes — TC content is
      unaffected, because the content was derived from the table itself.
- Follow-on work: a Last Mode extraction artifact (List Item -> operation /
  screen element / behavior) is now required for the B7 batch context.

## [A-H04] BSP struck-through text out of scope — RESOLVED (2026-08-09)

- Home PDF pp.18–19: Know & Go Hub content in BSP2 (second clause) and
  BSP5 / BSP5.1–5.3 is struck through in the source document.
- Ruling: TCs are written against effective (non-struck) text only. For 073
  (Content Fallback) the effective behavior is "a template with + will
  display"; the Know & Go Hub population path is excluded.

## [A-H05] Done region: 13 rows with blank Priority — RECORDED (no action)

- 13 of Arif's 144 rows have an empty Test Case Priority cell.
- Done region is frozen (content-hash invariant, RUNBOOK Step 4); rows are
  NOT fixed. Recorded here so reviewers see the deviation is pre-existing,
  not introduced by regeneration.

## [A-H06] 035 exists in FW036 but not in 037 — RECORDED (RD-1 candidate)

- 037 numbers `SWE1-HMI-HOME-001` … `-090` with exactly one gap: **035**.
- FW036 done region rows 129–130 nevertheless carry two Arif-authored TCs for
  `SWE1-HMI-HOME-035` ("Loading State and Minimum Dwell", spec outline `4.9`,
  i.e. HSD spec text that genuinely exists).
- So the requirement is real in the spec and covered in the workbook, but the
  SWE requirement row is missing from the analysis report.
- Impact: the RUNBOOK Step 4 completeness invariant "every req_id ∈ 037"
  would fail on Arif's own frozen rows. The invariant is therefore scoped to
  **regen rows only**; 035 is an allow-listed exception.
- Not fixed here: the done region is frozen (content-hash invariant) and 037
  is an upstream controlled document. Raise as an RD-1 question asking the RD
  authors to add the missing 035 row.
- `build_remaining.py` reports it every run under `ORPHAN req_ids`.

## [A-H07] HSD5.6 grey-out clause: CarPlay connection unstated — ASSUMPTION

- HSD5.6 (outline 4.5.6) reads: "…provide two additional layout options …
  Do not provide these options if Apple CarPlay is not currently connected.
  Gray out these options if the user already has a CarPlay layout on one of
  their home screens."
- The third sentence does not restate whether CarPlay must still be connected.
  Read literally, "already has a CarPlay layout" + "not connected" is
  ambiguous: the options are both absent (sentence 2) and greyed out
  (sentence 3).
- Assumption taken by `SWE1-HMI-HOME-020` TC-03: sentence 3 modifies the
  options introduced by sentence 1, so grey-out is only observable while
  CarPlay is connected. Pre-Condition keeps CarPlay connected.
- Marked inline as `[ASSUMPTION A-H07]` in that TC's Remarks. Low risk —
  if the ruling goes the other way only the Pre-Condition changes, not the
  split. RD-1 candidate if a reviewer wants it settled upstream.

## [A-H08] Verbatim popup text collides with the ER modal-verb ban — LINT RULE

- Profile §3.4 requires popup wording verbatim from the Pop Up List. PU1291's
  `String/Popup Message` is `Widget cannot be moved here.` — it contains the
  modal "cannot", which §6 bans from Expected Result.
- Ruling: the ban applies to the TC author's own prose, not to quoted source
  text. `lint_tcs.py` must strip double-quoted spans before running the modal
  check, otherwise every correctly-cited popup TC fails the gate.
- Affects B1 (033, 034 — PU1291) and every later batch citing PU0091 /
  PU0942 / PU1274.

## [A-H09] 020/021 Test Set attribution — RESOLVED (2026-08-09)

- 037 files `SWE1-HMI-HOME-020` (HSD5.6) and `-021` (HSD5.7) under the layout
  chapter, but both describe CarPlay layout rules: the additional 12" Portrait
  CarPlay layout options, and the CarPlay area's placement and control
  constraints.
- Ruling (Pei): attribute both to **CarPlay Template**, not Default Layout.
  Attribution follows capability, not the RD's filing location — the same
  principle as the Media `Presets` ruling (framework.md Part I).
- Framework-internal only: Test Group / Test Set columns stay blank in the
  workbook (Profile §2), so there is no workbook impact. Batching is
  unaffected — 020/021 were already in B1.
- Recorded in `docs/fw036/framework.md` Part II Layer 2/3 table.

## [A-H10] Pop Up List control tokens vs the bracket-label ban — LINT RULE
(amended 2026-08-09 at pilot review)

- Media's linter bans `[...]` and `<...>` in TC text, requiring `"..."` for UI
  labels. Home's done region uses both: 20 of Arif's 144 rows contain tokens
  such as `<X>`, `[OK, X]`, `[Reorder]` — all quoted from the Pop Up List
  (PU0942's message is literally `<X>\nPage added! [Reorder]`).
- Ruling: the tokens are not a defect, they are cited source text. `lint_tcs.py`
  validates them against the cited PU row's String/Popup Message and Exit
  Conditions instead of forbidding them; an unmatched token still fails.
- **`test_item` is exempt from this check and from the PU-citation check.**
  Profile §3.1 makes Test Item the requirement's shall-sentence verbatim, and
  the RD writes its own notation: 033/034's requirement text says
  `OK and [X] to dismiss` where the Pop Up List says `<OK>` / `<X>`. A
  requirement may also name a popup that a given TC does not exercise
  (034-01 tests the allowed swap, not the popup).
- Same family as A-H08: quoted source text is not the author's prose.
- **Pilot-review amendment (Pei, 2026-08-09): the exemption covers ONLY
  verbatim-quote segments in ER (e.g. `with the <OK> and <X> controls, as
  defined by PU1291 String/Popup Message`) and `test_item`. The author's own
  instructions — procedure press-targets and non-quoting ER prose — use
  double-quoted labels per the done region's own precedent (rows 44/45:
  `Press "OK" button to close the popup`). Corpus correction applied:
  `Press <OK>` → `Press "OK"` etc. across all generated TCs; lint enforces
  the narrowed scope.**

## [A-H11] Media's trailing-period rule does not apply to Home — RECORDED

- Media lints "no line ends with a period". Measured against Home's done
  region: 369 of 1298 lines end with a period (28%).
- A 28/72 split is not a convention. The rule is omitted from Home's linter
  rather than enforced against a majority of Arif's own rows.

## [A-H12] SYS1 export drops a sentence from HSS4 — RECORDED (affects 048-04)

- The Home PDF's HSS4 contains a sentence the SYS1 export does not:
  `If there is a custom routine, or a preset routine that has customization,
  show "Edit <name>" within the routine button (see Edit Routine section for
  more information on custom routines).`
- 037's `SWE1-HMI-HOME-048-04` ("Edit Mode: Edit Routines") follows SYS1 and
  therefore says only "the edit state allows the user to edit routines within
  the widget" — the button label and the routine-editing behaviour are absent.
- The referenced "Edit Routine section" is in **neither** document: the Home
  PDF only points at it, and SYS1 has no routine section at all. HSS1.1's
  table likewise defers: "Preset Routines -> Go to Preset Routines page, see
  Preset Routines logic page(s)".
- Disposition: 048-04 is scoped to the **entry point only** — the edit state
  offers a way into routine editing. The routine editing behaviour itself is
  an external-spec case (§8.4.2) and generates nothing here. Same shape as
  A-H02. RD-1: ask upstream to re-export HSS4 completely and to name the
  Edit Routine spec.
- Profile §1 says SYS1 is the text authority; this is an omission, not a
  wording conflict, so nothing is overridden — the missing content simply has
  no SWE requirement to hang a TC on.

## [A-H13] SW06 figure text differs from the specified prompt — RECORDED

- `SWE1-HMI-HOME-048-01` requires the Edit state to show
  `"Press and hold to drag and reorder shortcuts."` Both SYS1 9.5 and the PDF
  text layer agree on that wording.
- The SW06 figure on PDF p.14 renders the screen header as
  `Hold & Drag To Reorder Shortcuts` — different words, different casing.
- Profile §1: SYS1 is the text authority and the PDF supplies figures, so the
  TC asserts the specified wording. Recorded as a source inconsistency, since
  a tester comparing against the figure will see a mismatch.
- RD-1 candidate: ask which string ships.

## [A-H14] lint.popup_ids is not a closed list — RECORDED

- `feature.yaml` originally listed four popups (PU0091, PU0942, PU1274,
  PU1291) — the ones the SYS1 spec text cites BY ID.
- HSS4.1 instead quotes its popup by wording only: `display popup notification
  "Home screen updates saved." [X]`. The Pop Up List does define it —
  **PU0808** (module Home, 5 s timeout, exit `Timeout` / `<X>`).
- Disposition: cite PU0808 in `SWE1-HMI-HOME-049-02` and add it to
  `lint.popup_ids`. Citing the ID gives the tester the timeout and exit
  conditions that the Home spec omits, which is the point of Profile §3.4.
- The list grows per batch as spec wording is matched back to Pop Up List
  rows. It is an allow-list for typo detection, not a coverage claim.

## [A-H15] In-motion popup: spec says "Feature", PU0091 says "Function" — RECORDED

- Four Home spec sections (HSD4, HSD5.2, HSS2, HSS4.4) quote the driver
  lockout popup as `"Feature not available while vehicle is in motion."
  [OK, X]`.
- The Pop Up List has no row with that exact wording AND those controls:
  - **PU0091** (General, description "Driver Lockout: Function") reads
    `Function not available while vehicle is in motion.` with `<X>` / `<OK>`
    — controls match the spec's `[OK, X]`, wording differs by one word.
  - **PU0243** (General) reads `Feature not available while vehicle is in
    motion’` — wording matches, but its description scopes it to *"Editing
    the main category bar"*, a different feature, and it lists no exit
    conditions.
- The done region is itself inconsistent: Arif's rows 36–41 (012-03, same
  spec sentence) quote the spec wording and cite no PU, while rows 44–45
  (012-05) cite PU0091 and quote nothing.
- Disposition for `SWE1-HMI-HOME-052-02`: cite **PU0091** and quote PU0091's
  wording. Profile §3.4 is explicit that popup text comes from the Pop Up
  List and "never from the Home spec's paraphrase", and PU0091 is the only
  candidate whose controls and scope fit. PU0243 is rejected on scope.
- RD-1: ask upstream which string ships, and whether PU0243 is a stale
  duplicate of PU0091.

## [A-H16] SYS1 export drops the HSS6 routines exception — RECORDED (affects 054)

- Home PDF HSS6: "User is not able to set the same shortcut within the same
  Shortcuts widget. **Exception: preset routines and custom routines can be
  duplicated within the same shortcuts widget.**"
- SYS1 outline 9.7 and 037's `SWE1-HMI-HOME-054` description both stop at the
  first sentence.
- Disposition: 054 is written to the SYS1 scope (no duplicates). The routines
  exception generates nothing — there is no SWE requirement to hang it on.
- Second instance of the same defect class as A-H12: the SYS1 re-export is
  truncating HSS sentences. RD-1 should ask for a full re-export of chapter 9
  rather than sentence-by-sentence fixes.

## [A-H17] 037's 056 description is HSS6.1's text — RECORDED (RD-1 candidate)

- `SWE1-HMI-HOME-056` has title "CP/AA Cross-Category Exclusion Exception"
  and HMI Source ID outline **9.7.2** (= HSS6.2), but its Requirement
  Description carries HSS6.1's text verbatim — literally including the
  `HSS6.1)` prefix — duplicating 055-01/-02/-03.
- HSS6.2's real content (AA/CP chosen from Media or Apps is removed from that
  category, remains selectable from the other, and may therefore be
  duplicated) appears in no 037 description at all.
- Disposition: 056 is written against **HSS6.2**, since both the title and the
  outline agree on it and Profile §1 makes SYS1 the text authority. The TC
  Remarks record the divergence from the 037 description.
- RD-1: ask upstream to correct the 056 description.

## [A-H18] SYS1 export drops SW7.1 — RECORDED (affects 061)

- Home PDF p.17 carries `SW7.1) The same behavior will be applied if the
  shortcut is part of a routine, if applicable (exceptions noted in table)`.
- SYS1 has no 9.12.1; outline 9.12 stops at SW7, and 037's
  `SWE1-HMI-HOME-061` description carries the table without SW7.1.
- Disposition: routine-borne shortcuts are out of scope for 061; recorded in
  the parent's `coverage_notes`.
- **Third instance of the same defect class** (A-H12 HSS4, A-H16 HSS6,
  A-H18 SW7.1). All three are chapter 9. The RD-1 question should be a full
  re-export of chapter 9 with a diff against the PDF, not three sentence
  patches — a per-sentence fix leaves the next omission undetected.
  `data/spec_diff.json` compares item CODES only and cannot see a dropped
  sentence inside a section that is otherwise present.
- Evidence that these are defects rather than deliberate filtering: in
  chapter 11 the SYS1 export *correctly* dropped the struck-through Know & Go
  clause from BSP2 and all of BSP5 (verified against the p.19 render, A-H04).
  The chapter 9 sentences carry no strikethrough, so the export had no reason
  to omit them.

## [A-H19] PU1274 String/Popup Message merges both product variants — RECORDED

- The cell reads, line by line: `<X>` / `No Apple CarPlay Android Auto device
  connected.` / `Do you want to connect or pair a device?` / `<OK><Cancel>` /
  `For Apple CarPlay, replace "Android Auto" text with "Apple CarPlay"`.
- Line 2 names both products at once, while the last line is an authoring
  instruction implying the base string should name only Android Auto. No
  vehicle will ever display line 2 as written.
- Disposition for `SWE1-HMI-HOME-059-02`: cite PU1274 by ID and state the
  popup's content and controls, but do NOT quote the composite string. An ER
  quoting it verbatim could never pass, which is worse than not quoting.
  Profile §3.4's verbatim rule presumes a well-formed source row.
- RD-1: ask upstream to split PU1274 into per-variant rows, or to state the
  base string and the substitution separately.

## [A-H20] 070 / 071 are pure supplier references — RESOLVED by A-H02 precedent

- `SWE1-HMI-HOME-070` (SNS9) and `-071` (SNS10) read, in full: "See Navigation
  supplier specifications for naming of shortcuts." / "… for errors
  notifications." Neither states any behaviour of its own.
- Same shape as 055-03, and the A-H02 ruling is directly on point: a
  reference-integrity TC cannot pass the §5.7 single-objective test, so no
  independent TC is written and a placeholder row carries the traceability.
- One difference from 055-03: that one split into sibling delegation plus an
  external spec. These two point wholly at a single external document —
  the Navigation supplier specification, which is not in `inputs/`. Pure
  §8.4.2.
- Applied as a precedent, not as a fresh ruling. Flagged for Pei to confirm
  the extension; nothing is blocked either way, since a contrary ruling would
  only change these two rows.

## [A-H21] 037 records SNS9 at outline 10.8 instead of 10.9 — RECORDED

- `SWE1-HMI-HOME-070`'s title and description are both SNS9 ("naming of
  shortcuts"), but its HMI Source ID suffix is `_10.8`.
- SYS1 outline **10.8 is SNS8** (the iconography rule, already owned by
  `SWE1-HMI-HOME-069`). **SNS9 is at 10.9**, which exists in the export.
- Disposition: 070's `spec_reference` cites **10.9**. Two fields (title,
  description) agree against one (the source id), which is the same judgement
  used for A-H17. The divergence is declared in the TC via
  `spec_reference_override: "A-H21"` — `lint_tcs.py` fails any unexplained
  mismatch, so this is recorded rather than silent.
- RD-1: ask upstream to correct 070's HMI Source ID.

## [A-H22] SNS4 does not exist in the spec — RECORDED (no action)

- The SNS notes run SNS1, SNS2, SNS3, SNS3.1, **SNS5**, SNS6 … SNS10 in both
  SYS1 and the PDF. There is no SNS4.
- No 037 requirement traces to it and no behaviour is missing as a result —
  recorded only so a reviewer counting SNS items does not read the gap as a
  dropped section (the third such omission, A-H18, made that a live concern).

## [A-H23] Navigation screens are supplier-owned placeholders — RECORDED

- PDF p.16 renders the navigation search screen, the search result screen and
  the route notification as grey boxes reading "See Navigation Supplier
  Release for Details".
- Affects `064` (search and save flow), `066-02` (route begun notification)
  and `067` (waypoint notification): their layout, wording and timing are
  owned by the Navigation supplier spec (§8.4.2).
- Disposition: TCs assert only the Home-side observable facts the Home spec
  itself commits to — that the search screen is reached, that the result can
  be saved, that the navigation screen is retained afterwards, and that a
  notification of the stated kind appears. No TC asserts supplier UI detail.
  Recorded in each parent's `coverage_notes`.

## [A-H24] 075's title claims locking; BSP4 states only ordering — RECORDED

- 037 titles `SWE1-HMI-HOME-075` "Home Screen Locking", but the requirement
  text is BSP4 in full: "The first home screen should be the Default Home
  Screen (HSD1) and Branded Pages should follow." Nothing about locking,
  nothing about forbidding a reorder.
- The title's natural reading — that the user cannot move a branded page
  ahead of the Default Home Screen — matters, because HSD7 does let the user
  reorder pages. If that constraint exists, 075 is the only place it could
  live, and it is not written down.
- Disposition: 075 tests the stated ordering only. No reorder attempt is
  included; asserting an undefined constraint would invent a requirement.
- RD-1: ask whether a reorder lock is intended. If yes it needs its own
  requirement text, and a TC becomes writable — this is a coverage gap that
  a green lint cannot detect, exactly the failure mode framework.md Part I
  records.

## [A-H25] Done region's speed value "(more than 8)" is an unsourced constant — RECORDED

- Arif rows 44/45 (and the pilot-following 052-01/-02) write `Set the vehicle
  speed above 0 (more than 8)`. No Home spec section states a numeric speed
  threshold — HSD4 says only "when the speed threshold is reached".
- The generated TCs correctly follow the done-region wording (style
  authority); the "8" is inherited, not fabricated by generation. Its unit
  and origin (bench convention? vehicle config?) are undocumented.
- Recorded so a reviewer does not read the number as spec-sourced. RD-1
  candidate only if a tester needs the authoritative threshold.

---

## Pilot gate — PASSED (Pei, 2026-08-09)

- Scope reviewed: B1 complete (020/021/032/033/034) + stratified samples
  052 (B3), 059 (B4), 066+070 (B5), 075 (B6), 081 (B7) — 11 parents, 20 TCs.
- Verdict: PASS with one corpus-wide mechanical correction (A-H10 amendment,
  popup control notation) before lint. Write-back unlocks after: correction
  applied → lint green → dry-run diff reviewed.
- Retroactive ratifications included: A-H03, A-H09, A-H20 dispositions.

---

## Assumption markers

None yet. Format when needed: inline `[ASSUMPTION A-Hnn]` in the generated
JSON `reasoning` field, linking back to an entry here.
