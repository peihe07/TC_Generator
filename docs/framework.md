# Test Case Framework — STLA Media HMI (SWE.6)

Project-wide Test Set definition per docs.md §4.1. Established from the SWE.1
analysis report (FMWIFSM037A03) and the Media HMI spec section structure
(SYS1 R1LL outline, aligned with Media_HMI_Logic_and_Flow_R1_SR24_Post_2A
July 25 2023). A new RD MUST map to a Test Set listed here; if no fit, update
this file first, then the workbook `Test Case Framework` sheet.

Ruled by Pei 2026-08-05: `Preset Management` split from `Presets` (§4.1.2
granularity target); `Media Widget` added for ch23; `SWE1-MEDIA-PLA-062`
overridden from Source Selection to Source Tab. Machine-readable mapping:
`tcgen_package/data/section_to_testset.json`.

## Coverage rule — orphan sub-sections

037 does not allocate a leaf to every SYS1 sub-section. Orphan sub-sections are
handled in **two layers**, and the layers answer different questions.

### Layer A — routing (which batch sees the text)

A sub-section with no leaf of its own is routed into the batch context of its
nearest **leaf ancestor**. A sub-section that IS itself a remaining leaf stays
with its own parent and must not be pulled upward. 10 of the 158 remaining leaf
sections are affected. Implemented in `make_batch_context.py`; see
`tcgen_package/ANOMALIES.md` A-001.

### Layer B — attribution (whether it enters that leaf's TC scope)

**Routing is not attribution.** Layer A decides which batch *sees* an orphan's
text; it does not decide that the orphan elaborates the ancestor leaf.

Decision test — *"is this text explaining how the ancestor leaf holds, or is it
asserting something the ancestor leaf never said?"*

- **Elaborates the ancestor** → in scope. Write TCs for it under the ancestor's
  req_id (§8.2.2 allows several TCs per sub-id).
- **Independent behaviour, parallel to a sibling leaf** → **context-only**. Do
  not generate TCs, do not attach it to a sibling leaf (§8.2.1), and record the
  gap in the tracker for RD-1 (A-008 logic — no req_id means no workbook row to
  write against).

Worked examples of each:

- **In scope (A-001):** 11.3.1 is a leaf whose own text is only the abstract
  *"label may change based on connected drive type"*; the testable behaviour
  lives in the unallocated 11.3.1.1 / 11.3.1.1.1, which explain exactly how
  that leaf holds. Both are in scope for SWE1-MEDIA-PLA-062.
- **Context-only (A-020):** 17.1 is a leaf asserting a *layout* rule (MPB1,
  "Playing Tab shows one full bank at a time"). Its orphans MPB1.7 / MPB1.8.x
  are preset-button *label* rules — siblings of MPB1.5 / MPB1.6, which have
  their own leaves (RAD-066/067/068). Attaching them to RAD-061-01 would record
  label requirements as a layout requirement, so they generate nothing and go
  to the tracker instead.

## When an unresolved spec question needs an `assumption` marker — and when it does not

A marker is a retrieval handle for **rework**. It belongs on a TC only if a
ruling could invalidate that TC. Two ways of handling an open question look
similar and are not:

- **A bet → marker.** The TC's verification target depends on which reading is
  right. `SWE1-MEDIA-RAD-070-03` verifies a "Presets Shown" indicator that APP1
  places in one container and the screenshots place in another; if the
  screenshot wins, the TC verifies an object that is not there. Marked (A-021),
  scoped to that one req_id.
- **Scope convergence → no marker.** The ambiguous element is kept *out* of the
  verification target, so the TC holds under every reading.
  `SWE1-MEDIA-COM-065-02` is scoped to a USB track list, sidestepping the
  Presets/All Stations conflict (A-012). `SWE1-MEDIA-INT-030-01` verifies that
  a popup opens and lists presets, and deliberately says nothing about the
  Edit Presets button whose presence is disputed (A-030).

Test: *"if the ruling goes the other way, does this TC change?"* Yes → marker,
scoped to the affected req_ids only. No → no marker; record the reasoning in the
tracker instead. Over-marking is not free: a marker that never needs rework
dilutes the retrieval set the ruling is supposed to produce.

Related: markers follow the **rework target**, not the parent that raised the
question — A-012 is marked on COM-061, not on COM-065 which found it.

## Priority follows the verification target, not the feature's importance

A TC's priority is set by **what fails to be detected when the TC fails**, not
by how important the underlying feature is. The temptation runs the other way:
a display requirement about a play/pause control looks like it deserves the
priority of playback itself.

Worked example (ruled 2026-08-07): `SWE1-MEDIA-INT-022-02` verifies that the
Media Widget *displays* a play/pause control. Failing it means a button is
missing from a widget — not that audio stopped. The widget's actual playback
behaviour is explicitly delegated by 23.1 ("Refer to the Media - Mixed Presets
and playing Tab HMI sections for complete logic"), so the P0 lives in ch5/ch9,
where the done region already covers it. INT-022-02 is P1.

Consequence to accept rather than correct: **a whole chapter may legitimately
contain no P0**. ch23 Media Widget has none, because every one of its leaves
verifies display or navigation and its audio behaviour is delegated elsewhere.
Do not rebalance a chapter to "earn" a P0.

## Anchors are style authority, not fact authority

Curated anchors (`tcgen_package/anchors.json`) and done-region exemplars supply
**form**: step shape, ER phrasing, how a scenario tag reads, which judgement
calls a Test Set needs. They do not establish **fact**. A UI label, a numeric
limit, a state name — those come from the spec, and only from the spec.

The rule exists because the done region violated it and generation followed.
MN2 makes the Media Tab Button label tier-dependent (`"Playing"` on R1 High,
`"Playing: Source"` on R1 Low); the done region uses *both* forms across
different TCs; generation anchored on a sample containing only the first, and
76 TCs inherited an unverified fact. See `ANOMALIES.md` A-026.

Practical consequence: when an anchor supplies a literal — a quoted label, a
number, an enumerated value — trace it to its spec clause before reusing it. If
the spec makes it conditional, the anchor cannot tell you which condition holds.

## Blocked-parent rule — delegation proportion

A missing referenced artefact (an absent Pop Up List id, a missing table) does
**not** by itself block a parent. What matters is how much of the leaf's
content was delegated to the missing thing:

- **Fully delegated → BLOCKED.** The clause *is* the reference and carries no
  content of its own. `SWE1-MEDIA-COM-051` (13.2): the entire requirement reads
  *"SMP1) See Pop Up List: PU0996"*, and PU0996 does not exist. Writing a TC
  would mean inventing the popup wholesale (§8.4), so the parent emits no TC,
  carries a `blocked` marker, and still gets a workbook row whose Remarks make
  the hole visible.
- **Self-contained, reference is supplementary → generate.** The clause states
  its own testable content and the reference only adds detail no leaf asks for.
  `SWE1-MEDIA-RAD-070` (18.1): APP1 names every element the five leaves verify
  (3 banks per page, indicator, metadata, X) and merely cites PU0997 for
  popup-spec detail. The parent generates normally; the reasoning states what
  the missing reference does and does not affect.

Test: *"does the missing artefact carry content that a leaf asks us to
verify?"* Yes → BLOCKED. No → generate, and bound the impact in reasoning.

## Layer 1 — Test Group

- `Media` (workbook Test Group column value: `MediaHMI`)

## Layer 2 / Layer 3 — Test Sets and their spec sections

Layer 3 (spec chapters / code prefixes) is framework-internal only — NEVER
written to the workbook.

| Test Set | Spec sections (Layer 3) | Code prefixes | Status |
|---|---|---|---|
| General Anatomy | ch4 Media Notes (anatomy subset) | MN | done region |
| Playing Tab | ch5 Playing Tab; ch6 Source Specific Button Bank (display subset) | PT, SS | done region |
| Source Tab | ch10 Source Tab; ch12 Pinned Sources Bank; 11.3.1 USB label (PLA-062 override) | ST, PSB, USB | ch12 remaining |
| Browse Tab | ch14 Browse Tab; ch19 USB Folder Browse; ch20 USB/Disc Folder Filtering; (hist.: ch9 Tracks popup TCs) | BT, FB, FF | mostly remaining |
| Source Selection | ch10 (selection flow subset); ch11 Sources Notes (BTSA); ch13 Source Secondary Menu Pop up | SS, BTSA, SMP | ch11/13 remaining |
| Metadata | ch6 (metadata subset); ch7 Metadata | MD | done region |
| Tuning Controls | ch8 Tuning Controls | TC | done region |
| Play Controls | ch9 Play Controls; ch22 AutoPlay Setting | PC, AP | ch22 remaining |
| Presets | ch4 (preset notes subset); ch16 Mixed Presets; ch17 Mixed Presets Bank | PRE, MPB | ch16/17 remaining |
| Preset Management | ch18 All Presets Pop up (add / overwrite / rearrange / delete, Edit Presets) | APP | NEW — all remaining |
| Audio Settings | ch21 Audio Settings | SA | all remaining |
| Media Widget | ch23 Media Widget (Home screen widget) | MW | NEW — all remaining |

## Granularity check (§4.1.2 target: ~10–50 RD parents per Set)

Remaining-parent load after the split: Browse Tab ~50 (ch14+19+20, watch this
one — if it grows next RD cycle, split Folder Browse out), Presets ~30,
Preset Management ~19, Audio Settings ~19, Media Widget ~15, others < 15.
All within target.

## Known anomalies (tracker items, not blockers)

1. One done-region `Playing Tab` TC traces to a ch23 (Media Widget) leaf —
   review whether it should move to `Media Widget` in a later pass.
2. Done-region `Browse Tab` TCs trace to ch9 leaves (Tracks list popup, which
   the spec files under Play Controls). Historical classification kept;
   ch14 Browse work proceeds under Browse Tab regardless.

## Workbook sync

`Test Case Framework` sheet (single column A, values at rows 5–14) must gain:

- A15: `Preset Management`
- A16: `Media Widget`

Either edit the two cells by hand, or run:

```python
import openpyxl
wb = openpyxl.load_workbook("FMWIFSM036A01_..._MediaHMI_20260625.xlsx")
ws = wb["Test Case Framework"]
ws["A15"] = "Preset Management"
ws["A16"] = "Media Widget"
wb.save("output/FMWIFSM036A01_framework_updated.xlsx")
```

(The write-back pipeline copies the workbook anyway, so doing this once on the
source copy is enough.)
