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

## [A-H03] Last Mode spec missing from inputs — OPEN (blocking)

- `SWE1-HMI-HOME-076` … `-090` (15 leaves) trace to
  `Last Mode Table HMI Logic and Flow R1L-R (August 2 2021)_1`, which is not
  in `inputs/`.
- Disposition: B7 produces BLOCKED placeholder rows only, Remarks =
  `BLOCKED - source spec not available (A-H03)`. Unblock by dropping the
  file into `inputs/` and rerunning Step 1 + B7.
- Action owner: Pei (request file from upstream).

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

---

## Assumption markers

None yet. Format when needed: inline `[ASSUMPTION A-Hnn]` in the generated
JSON `reasoning` field, linking back to an entry here.
