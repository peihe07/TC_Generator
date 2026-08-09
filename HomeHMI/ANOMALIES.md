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

---

## Assumption markers

None yet. Format when needed: inline `[ASSUMPTION A-Hnn]` in the generated
JSON `reasoning` field, linking back to an entry here.
