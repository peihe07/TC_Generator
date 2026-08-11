# Project Profile — FW036 / R1L SWE1 Home HMI (Stellantis newR1L)

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.

## 0. Project identity [ADD]

- Program: Stellantis newR1L; scope FM-WI-FSM-037-A03-N1L-SWE1 Home HMI
- Deliverable workbook: FMWIFSM036A01 (`SWQT_Home_20260720`); author on new
  rows: `PeiPYHsu`
- Requirement IDs: `SWE1-HMI-HOME-NNN[-NN]` from the 037 report — never
  invented, never renumbered
- Done region = the 144 rows authored by `Arif` (three interleaved segments;
  see features/home/RUNBOOK.md). Done region is style authority, NOT factual
  authority; its content is frozen byte-for-byte.

## 1. Requirements authority chain [ADD]

- Chain: SYS1 Polarion export (Home Screen HMI Logic and Flow, SR24 Post 2A)
  → 037 SWRA decomposition → FW036 TC.
- Spec TEXT authority is the SYS1 export; the PDF supplies figures and layout
  tables. On PDF↔SYS1 wording conflict, SYS1 wins; flag the delta in
  ANOMALIES.md.
- External referenced specs (Pop Up List; Phone HMI for the 055-03 phone-side
  exception; Last Mode Table for 076–090) follow §8.4.2: never absorb their
  rules; BLOCKED placeholder when the file is missing. The Last Mode Table is
  present under a different release label (A-H03) — 076–090 are NOT blocked.

## 2. Test Set vocabulary [OVERRIDE — replaces workbook Test Set output]

- Workbook columns G (Test Group) and H (Test Set) are left **EMPTY** on every
  row, matching the done region. The framework Test Sets
  (docs/fw036/framework.md, Home section) exist for batching, lint grouping,
  and coverage analysis only — they are never written to the workbook.

## 3. FW036 Home house style (field rules)

### 3.1 Test Item [OVERRIDE — replaces §4.3 tc_title-only cell content]

- Done-region precedent: the Test Item cell carries the requirement's shall-
  sentence (037 Requirement Description essence), e.g. row 10:
  `The system shall configure the default Home Screen for 8.4" displays with
  two 50% widgets. ...`
- New rows follow the same shape: Test Item = condensed requirement statement
  in spec language (modals permitted HERE ONLY, as it quotes requirement
  text). The generic §4.3 tc_title (no modals, 3 shapes) is still produced in
  the output JSON for lint/sibling-distinction, but the workbook cell gets
  the requirement-statement form. When one req yields multiple TCs, append
  the distinguishing scenario tag to the statement so sibling rows differ.
- §6 still applies unchanged to ER: no modal verbs there, ever.

### 3.2 Pre-Conditions [ADD — Home motion-state clarification]

- `The vehicle is in motion` / `The vehicle is not in motion` are spec
  trigger conditions (HSD2/HSS2 family) → valid Pre-Conditions per §8.5
  exception.
- Screen size and radio type (`The vehicle is equipped with a 12" Portrait
  display`, `R1 High radio`) are spec-defined applicability triggers → valid.
- `HU is powered on` remains banned (generic rule; no BT-style waiver here —
  the done region does not use it).

## 3.3 Design Method [OVERRIDE — restricts §12 output strings]

Return exactly one of the 9 dropdown strings from the workbook 下拉選單
sheet, character-for-character (e.g.
`功能測試 (Functional based ; no specific technique)`,
`狀態轉換 (State Transition Testing)`, `負向測試 (Negative / Invalid)` …).
§12 mapping logic unchanged; only the output string format is fixed.
Done-region uses Functional exclusively — do not force-match this; assign
per §12 truthfully.

### 3.4 Popup citations [ADD]

- Any popup behavior cites the Pop Up List by ID and field:
  `as defined by PU0091 String/Popup Message` (also PU0942, PU1274, PU1291).
- Popup display text, button set ([OK, X] / [Undo, X] / [OK, Cancel]) and
  timeout come verbatim from the Pop Up List row — never from the Home spec's
  paraphrase, never invented.

### 3.5 Spec Reference [OVERRIDE — replaces §10.7 filename format]

Exactly the done-region format:
`Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023)_{outline}`
where `{outline}` is the SYS1 Outline Number resolved via
`data/spec_id_to_outline.tsv`. Unresolvable section → ANOMALIES.md entry +
reference pending; never construct an outline number by guess.
Last Mode TCs (076–090) use that spec's ACTUAL file name plus its List Item
number, per the A-H03 ruling:
`Last Mode Table HMI Logic and Flow R1 SR24 1A (August 2 2021)_{n}`.
This deliberately differs from 037's `R1L-R` label — the reference must name
a document the tester can locate.

### 3.6 Remarks [ADD]

Empty string unless: BLOCKED row (reason + anomaly id, e.g. A-H03), RD-1
flag (A-H01 / A-H02), or a documented workaround. Red highlight downstream
is a manual convention.

## 4. Split policy [ADD]

- `standard` split mode. Follow Arif's granularity precedent where the done
  region establishes one (e.g. 001-01~03 screen-size handling): 037 sub-id
  is the unit; do not explode per-screen-size beyond 037's own split.
- §5.7 held firmly: motion-lockout pattern (grey-out + popup on press) is one
  trigger with consequential outcomes → ONE TC, multi-line ER — unless 037
  itself splits them into sub-ids (e.g. 052-01/052-02), in which case §8.2.1
  wins and each sub-id keeps its own TC.

## 5. Home step-writing conventions [ADD]

- Motion simulation: `Drive the vehicle above the speed threshold` /
  `Bring the vehicle to a standstill` — bench CAN alternative allowed as the
  two-line `$` command format (§5.4) when the bench profile requires it.
- Widget interactions name the on-screen element with `"..."` labels exactly
  as the spec figures render them: `"Add Widget"`, `"Add Page"`,
  `"Delete Pages"`, `"Reorder Pages"`, `"My Edit Pages"`, `"Select a Widget"`,
  `"Done"`, `"Cancel"`, `"Undo"`.
- Layout verification steps state the observable geometry from the spec
  table (`two 50% widgets`, `one 50% + two 25% vertical`), never `correct
  layout`.

## 6. Blocked placeholder [ADD]

- BLOCKED rows keep the req row: Test Item = requirement sentence,
  Procedure/ER = `BLOCKED - see Remarks`, Priority and Design Method blank,
  Remarks = reason + anomaly id.
- No standing blocks as of 2026-08-09. All Step-0 rulings are closed:
  066 parent (A-H01) and 055-03 (A-H02) get placeholder rows with delegation
  Remarks; B7 (A-H03) generates normally. The blocked-placeholder format
  above stays defined for any block found during generation.

## 7. Known anomalies register [ADD]

A-H01 066 parent/child duplication; A-H02 055-03 pure-reference req;
A-H03 Last Mode spec release-label mismatch (resolved — not missing);
A-H04 BSP struck-through text out of scope; A-H05 done-region 13 rows blank
priority (recorded, not fixed); A-H06 035 in FW036 but absent from 037;
A-H07 HSD5.6 grey-out assumption; A-H08 quoted popup text is exempt from the
ER modal-verb ban; A-H09 020/021 attribute to CarPlay Template.
Details and dispositions live in `features/home/ANOMALIES.md`.
