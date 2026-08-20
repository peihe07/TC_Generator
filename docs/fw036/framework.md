# Test Case Framework — STLA FW036 (SWE.6)

Covers Test Groups **Media** (Part I, below), **Home** (Part II), **AMFM**
(Part III), **SXM** (Part IV), **Projection** (Part V), **Privacy**
(Part VI), and **Time and Date** (Part VII, end of file). The cross-cutting rulings in Part I (orphan routing/attribution, lint vs
traceability, assumption markers, priority, anchors-as-style, blocked-parent
proportion) apply to ALL Test Groups.

## Part I — Media HMI

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

## The three-layer gate: lint, human review, done region as arbiter

Carried forward from the Home run (2026-08-09) and intended to be reused
as-is on the next feature. The layers catch different classes of defect and
none of them substitutes for another:

1. **`lint_tcs.py` catches mechanical deviation** — malformed references,
   step/ER mismatches, illegal dropdown values, unexplained divergence from
   037. Cheap, exhaustive, and runs on every batch.
2. **Human review catches judgement deviation** — scope, splitting, whether a
   TC's objective is the one the requirement actually asserts. The Home pilot
   review found a real defect (bracket-token notation, A-H10) inside a corpus
   that was already lint-clean. No rule would have surfaced it, because the
   question was "which notation is authoritative here", not "is this
   well-formed".
3. **The done region arbitrates** — when layers 1 and 2 disagree, or when a
   rule is proposed on intuition, the frozen human-authored rows are the
   evidence. Two Home rulings were *reversed* by measuring them: the
   trailing-period rule (28% of lines, so not a convention — A-H11) and the
   Input Test Data convention (blank, not `NA`). Both would have shipped as
   plausible-sounding rules had they not been checked against the corpus.

The practical instruction: **do not add a lint rule from intuition.** Measure
it against the done region first, and if the region contradicts it, record the
measurement rather than the rule.

## Lint being green does not mean traceability is correct

Row-level linting checks each TC against the writing rules. It structurally
cannot check whether a row points at a requirement that exists — such a row is
well-formed in every respect the linter can see.

This is not hypothetical. Five parents were generated with TCs numbered `-01`,
`-02`, `-03` under a leaf 037 only defines as `-01`. §8.2.2 permits several TCs
per sub-id, but they **share** that sub-id; incrementing it invents a
requirement. All 277 TCs passed lint at the time. Only reconciling the written
req_ids against the leaf list caught it.

Two gates now exist because of it, and they are deliberately redundant:

- `unknown-req-id` in `lint_tcs.py` — fails any TC whose req_id is not a leaf.
- `assert_traceable_and_complete` in `write_back.py` — aborts the write unless
  the set of written req_ids equals the set of leaves exactly, in both
  directions.

The second is the one that matters for the deliverable: a missing leaf produces
no row at all, so nothing exists for a row-level rule to inspect.

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

> ### ⛔ NEVER `openpyxl` + `wb.save()` on a form workbook (R-G3, global)
>
> `openpyxl` silently **drops the `x14` data-validation extension** on load
> ("Data Validation extension is not supported and will be removed") and does
> not write it back. On a rev C workbook that extension IS the `design_method`
> dropdown on column R.
>
> Measured on the 036 master `…_SWQT_20260817_ext.xlsx` (A-UP09, 2026-08-17,
> on a copy outside the repo; the master's SHA was identical before and after):
>
> | | before save | after save |
> |---|---|---|
> | `<x14:dataValidation>` nodes | **1** | **0** |
> | its `<xm:sqref>` | `R10:R1411` | *(gone)* |
> | legacy DV (`P10:Q1411`, `T10:Z1411`, `AF10:AF1411`) | 3 | **3, survive** |
> | zip members | **48** | **47** |
> | sheet count | 9 | 9 |
> | column B formula, last row | 1411 | 1411 |
>
> **The damage is selective, and that is what makes it dangerous**: sheet
> count, row count, formula ranges and the other three DVs are all unchanged
> and exactly one zip member disappears — it reads as a harmless repackage,
> and any check that compares sheets / rows / formulas stays green. A
> workbook that has lost its R-column dropdown still opens, still looks
> right, and fails the reviewer's confirmation (profile §0.1 item 2).
>
> **Use `backend/xlsx_surgical.py`, which patches the sheet XML in place and
> leaves every other zip member byte-identical.** Its `surgical_save` reports
> the differing members and the DV counts, so "nothing else moved" is
> measured rather than assumed.

**`Test Case Framework` sheet — rev A/B only (R-U10).** rev C, the current
official form, has no such sheet (9 sheets; rev A/B have 10). The sheet was a
Media-era workflow artefact, not an STLA form requirement, so on rev C the
Test Set vocabulary lives in column H alone and this section's sync step does
not apply. Keep the step for rev A/B workbooks.

For a rev A/B workbook, the sheet (single column A, values at rows 5–14) must
gain:

- A15: `Preset Management`
- A16: `Media Widget`

Either edit the two cells by hand, or splice them:

```python
import openpyxl
from backend.xlsx_surgical import surgical_save

src = "FMWIFSM036A01_..._MediaHMI_20260625.xlsx"
out = "output/FMWIFSM036A01_framework_updated.xlsx"

wb = openpyxl.load_workbook(src)          # load is fine; it is save that destroys
ws = wb["Test Case Framework"]
ws["A15"] = "Preset Management"
ws["A16"] = "Media Widget"

report = surgical_save(wb, src, out)      # patches sheet XML only
assert report["differing"] == [           # every other member byte-identical
    m for m in report["differing"] if m.endswith(".xml")]
print(report["dv_counts"])                # DV counts must match the source
```

(The write-back pipeline copies the workbook anyway, so doing this once on the
source copy is enough.)

---

## Part II — Home HMI

Deliverable workbook: FMWIFSM036A01 `SWQT_Home_20260720`; RD source
FMWIFSM037A03-N1L-SWE1 Home HMI (140 leaf FRs); spec authority SYS1 export of
Home Screen HMI Logic and Flow R1 SR24 Post 2A (March 17 2023). Execution
plan: `features/home/RUNBOOK.md`; profile:
`docs/runtime/profiles/FW036_R1L_Home_Profile.md`.

**Workbook divergence from Media**: the Home done region (144 rows by Arif)
leaves Test Group / Test Set columns EMPTY and the `Test Case Framework`
sheet unpopulated. New rows follow that convention — the Test Sets below are
batching / lint-grouping / coverage vocabulary only and are never written to
the Home workbook (Profile §2).

### Layer 1 — Test Group

- `Home` (workbook column left blank; framework-internal name)

### Layer 2 / Layer 3 — Test Sets and their spec sections

| Test Set | RD range | Spec sections (Layer 3) | Status |
|---|---|---|---|
| Default Layout | 001-01~03 | HSD1 | done region |
| Widget Edit | 002~010 series | HSD2.x, HS10 | done region |
| Page Management | 011~019, 022~031 series | HSD4~HSD7.x | done region |
| CarPlay Template | 020, 021, 032, 033, 034 | HSD5.6, HSD5.7, HSD8.4, HSD8.5, HSD8.6 | remaining |
| Shortcuts Edit | 048-01~06, 049-01/02, 050, 051 | HSS4, HSS4.1~4.3 | remaining |
| Shortcuts Lockout | 052-01/02, 053 | HSS2, HSS4.4, HSS5 | remaining |
| Shortcut Exclusion | 054, 055-01~03, 056, 057 | HSS6, HSS6.1, HSS6.2, HSS7 | remaining |
| Shortcut Availability | 058, 059-01~04, 060 | HSS8, HSS9, HSS10 | remaining |
| Shortcut Actions | 061 | SW7, SW7.1 (actions table) | remaining |
| Navigation Shortcuts | 062~071 (incl. 066/-01/-02) | SNS1~SNS10 | remaining |
| Brand Pages | 072, 073, 074 | BSP1, BSP2, BSP3/BSP4 | remaining |
| Screen Locking | 075 | BSP4 (outline 11.5) | remaining |
| Last Mode | 076~090 | Last Mode Table L&F List Items 1~331 (external spec, §8.4.2) | remaining |

Ruled by Pei 2026-08-09: **020/021 attribute to CarPlay Template**, not
Default Layout. Both describe CarPlay layout rules (HSD5.6 the additional
12" Portrait layout options, HSD5.7 the CarPlay area constraints); RD files
them under the layout chapter, but attribution follows capability, not
location — the same principle as the Media `Presets` ruling in Part I.
Batching is unaffected: both were already in B1.

### Granularity check

Done-region Sets (Widget Edit, Page Management) carry the bulk; remaining
Sets are small because Home is a smaller module (140 leaves total vs Media's
450). Single-req Sets (Shortcut Actions, Screen Locking) are genuine
outliers per §4.2, accepted.

### Home anomalies

A-H01…A-H08 — register and dispositions in `features/home/ANOMALIES.md`.
**All Step-0 rulings are closed as of 2026-08-09; every Set including Last
Mode is generation-ready.** A-H03 resolved: the Last Mode spec is present in
`inputs/` under a different release label, and all 15 leaf `_{n}` suffixes
resolve to List Items in its table.

### Workbook sync

None. The Home `Test Case Framework` sheet stays empty by done-region
convention.

---

## Part III — AMFM (CFTS024 Radio)

Deliverable workbook: FM-WI-FSM-036-A01 `SWQT_CFTS024_Radio_20260129`; RD
source 037-A03 (102 leaf FRs, `SWE-RA-RAD-*`, per RULINGS R1); spec_mode D
— spec authority is the CFTS024 docx (R1LR Atl-H 25PI3.5, 20250910) plus
two external CFTS docs (below); SYS3 SYSAD supplies architecture context.
Execution plan: `features/amfm/RUNBOOK.md`; profile:
`docs/runtime/profiles/FW036_R1L_AMFM_Profile.md`; rulings R1–R7 in
`features/amfm/RULINGS.md`.

**Layer 2 derivation note (§4.1.2 degenerate case)**: the 037's
Categorization / Sub-Categorization columns are `Functional / NA` on all
102 leaves — the RD grouping axis carries zero information, so the
§4.1.2 intersection degenerates to the spec's own structure. The usable
axis: every 037 Requirement Title ends with the source STLA id
`(48xxxxx)`, and CFTS024 headings carry `{id}` anchors monotonic in doc
order, so each leaf maps mechanically to its bracketing CFTS section.
85/102 leaves resolve inside CFTS024; 17 resolve to external CFTS docs
(CFTS011 evidenced by SYS3 §4.4.2 c.3; CFTS004 attribution is an
assumption until the file arrives — A-AM06/A-AM07).

**Legacy region**: 158 rows by Wilson trace the superseded `SWE-RAD-*`
family and are FROZEN (R4, option i) — excluded from coverage and
traceability invariants. Their band-based Test Set scheme (`FM`/`AM`/`USB`)
is NOT adopted for new rows (R7-Q2); their `Radio` Test Group value stays
on their own rows only (R7-Q1).

### Layer 1 — Test Group

- `AMFM` (workbook Test Group column value on new rows: `AMFM`; legacy rows
  keep `Radio`, frozen)

### Layer 2 / Layer 3 — Test Sets and their spec sections

Layer 3 = CFTS section numbers (or external doc tag); framework-internal
only — NEVER written to the workbook.

| Test Set | Spec sections (Layer 3) | Leaves (SWE-RA-RAD-) | n | Status |
|---|---|---|---|---|
| Tuner Availability | CFTS024 1.3 (AM presence gate) | 001–002 | 2 | remaining |
| Seek | CFTS024 1.3.1, 1.3.2 | 003–013 | 11 | remaining |
| Browse | CFTS024 1.3.3, 1.3.3.1, 1.3.3.2 | 014–024 | 11 | remaining |
| Tune | CFTS024 1.3.4, 1.3.5, 1.3.6 | 025–030 | 6 | remaining |
| Presets | CFTS024 1.3.7, 1.3.8 | 031–039 | 9 | remaining |
| List Navigation | CFTS024 1.3.10, 1.3.11, 1.3.12 | 040–051 | 12 | remaining |
| RDS Features | CFTS024 1.3.13, 1.3.13.1, 1.3.13.2 | 052–063 | 12 | remaining |
| Station List | CFTS024 1.3.14 | 064–080 | 17 | remaining |
| Market Configuration | CFTS024 1.12.1.3.1.5, 1.12.2.2.1 | 081–085 | 5 | remaining |
| Engineering Mode | CFTS011 (external — A-AM06) | 087, 089–096 | 9 | remaining |
| Diagnostics | CFTS004 DIDs (external, attribution assumed — A-AM07) | 097–104 | 8 | remaining |

Total 102 = full leaf set. Numbering gaps 086/088 exist in the 037 itself
(A-AM08), not in this allocation.

### Granularity check

Sets range 2–17 leaves; all pass the §4.1.3 filter test. `Tuner
Availability` (2) is a genuine outlier per §4.2 — the AM-presence
configuration gate shares no setup pattern with any sibling set.

### AMFM notes

1. **Duplicate STLA ids inside the 037** (A-AM08, marked per R7-Q4, Pei
   judges per pair at review): 087/094 share 4942534; 089/095 share
   4942540; 090/096 near-identical text; 028/029 share 4872451. Each leaf
   still receives its own TC (§8.2 — no consolidation); sibling
   `distinguishing_axis` must name the delta or declare `duplicate_of`.
2. Leaves 001–080 predominantly apply to BOTH AM and FM bands — band is a
   split axis (§8.3) inside a TC family, not a Test Set boundary. This is
   why the legacy band scheme could not carry the capability structure.
3. External-doc leaves (Engineering Mode, Diagnostics) generate normally:
   their 037 titles carry self-contained requirement text (blocked-parent
   proportion test — Part I). Only the spec_reference doc anchor waits on
   file supply.

### Workbook sync

The AMFM `Test Case Framework` sheet is empty (Wilson convention differs
from Media: G/H columns filled per row, framework sheet unused). Leave the
sheet empty; the capability Test Sets live in the H column of new rows and
in this file.

---

## Part IV — SXM (SiriusXM 360L SAT Only)

Ruled by Pei 2026-08-10 (directive「照簽/改裁」, Phase 3 sign-off): Test
Group `SXM`; the 14-Set table below including the Instant-Replay/Browse
no-split and the Favorites/Activation split; batch plan B1–B14 with pilot
B1; R10-2 absorption ADOPTED for SXM (note 5).

Deliverable workbook: FM-WI-FSM-036-A01 `SWQT_SXM_20260810` (form revision
C — first feature on it, A-SX05); RD source 037-A03 SXM (202 leaf FRs,
`SWE-RA-SXM-*`, 20260406); spec_mode D — clause authority is CFTS024
§1.5.x via the HYBRID ingestion ruling (DECISIONS §1: ReqIF attribute
direct-read for clause text, docx heading parse for printed section
numbers, bracket map as fail-loud validator). The SiriusXM 360L SAT Only
HMI L&F (PDF + SYS1 export) is the figure/flow source (mode C role), not
the citation source. Execution plan: `features/sxm/RUNBOOK.md`; profile:
`docs/runtime/profiles/FW036_R1L_SXM_Profile.md` (to instantiate);
rulings in `features/sxm/DECISIONS.md` + `features/sxm/ANOMALIES.md` (A-SX01–07 all
RESOLVED).

**Layer 2 derivation note**: same degenerate case as AMFM — the 037's
Categorization column is `Functional` on all 202 leaves, so the §4.1.2
intersection collapses to the spec's own §1.5.x structure. The mapping is
mechanical and total: 202/202 leaf ids land on exact CFTS024 clause
anchors (A-SX01), leaf ids are near-contiguous within each section, and
section boundaries are natural batch boundaries
(`features/sxm/docs/leaf-sections-sxm.md`).

**Workbook state**: BLANK — no legacy region. Style authority = fallback
chain; exemplars from the AMFM done region, `cross-feature: style only`,
every literal re-traced to the SXM spec line (DECISIONS §4).

### Layer 1 — Test Group

- `SXM` (workbook Test Group column value on all rows — BLANK workbook,
  FILL ruled; value ruled 2026-08-10, matches the 037 prefix `SWE-RA-SXM`)

### Layer 2 / Layer 3 — Test Sets and their spec sections

Layer 3 = CFTS024 printed section numbers; framework-internal only —
NEVER written to the workbook.

| Test Set | Spec sections (Layer 3) | Leaves (SWE-RA-SXM-) | n | Status |
|---|---|---|---|---|
| Source Availability | 1.5 | 001 | 1 | remaining |
| Seek | 1.5.1, 1.5.2 | 006–021 | 16 | remaining |
| Tune | 1.5.3, 1.5.4, 1.5.5 | 002, 003, 022–031 | 12 | remaining |
| Presets | 1.5.6, 1.5.7 | 004, 032–038 | 8 | remaining |
| Favorites | 1.5.9, 1.5.9.1 | 005, 039–054 | 17 | remaining |
| Activation | 1.5.9.2 | 055–062 | 8 | remaining |
| Instant Replay | 1.5.10, 1.5.10.1–1.5.10.4 | 063–092 | 30 | remaining |
| Browse | 1.5.11, 1.5.12, 1.5.12.1, 1.5.12.1.1–1.5.12.1.4 | 093–131 | 39 | remaining |
| List Navigation | 1.5.13, 1.5.14, 1.5.15 | 132–150 | 19 | remaining |
| Traffic & Weather | 1.5.16 | 151–158 | 8 | remaining |
| Game Alert | 1.5.17 | 159–167 | 9 | remaining |
| Parental Skip | 1.5.19 | 168–175 | 8 | remaining |
| Error Displays | 1.5.20 | 176–182 | 7 | remaining |
| Performance | 1.5.21.2, 1.5.21.2.2–1.5.21.2.7 | 183–202 | 20 | remaining |

Total 202 = full leaf set; count reconciles per section against
`leaf-sections-sxm.md`.

### Granularity check (§4.1.3)

- All Sets pass the filter test (meaningful cluster, not one TC, not the
  workbook).
- `Source Availability` (1) is a genuine outlier per §4.2 — the
  satellite-source presence gate shares no setup with any sibling (AMFM
  `Tuner Availability` precedent).
- **`Instant Replay` (30) and `Browse` (39) are deliberately NOT split.**
  §4.2: sub-actions of one capability share one Set. The transport buttons
  (Pause/Play/Rewind/FF) are sub-actions of the replay-buffer capability
  with one shared setup (live audio → buffer established); the browsed
  category (All Channels / Presets / Genre / Game Alerts / Traffic–Weather
  / Favorites) is a data axis (§8.3) inside the Browse capability — the
  same reasoning as AMFM note 2 (band is a split axis, not a Set
  boundary). Splitting either by button or by category would be the
  too-granular anti-pattern. Generation workload is handled at BATCH
  level instead (below). Watch-rule: if a later RD cycle grows either Set,
  revisit here first.

### Batch plan (generation batches ≠ Test Sets)

Ruled base (DECISIONS §7): group by spec chapter; pilot = §1.5.10 +
1.5.10.1 + 1.5.10.4 Instant Replay / Pause / Fast Forward (19 leaves)
**plus leaf 154** (triple-marked; pilot validates the marker mechanism).
Large Sets split across batches without splitting the Set:

| Batch | Sections | Leaves | n |
|---|---|---|---|
| B1 (pilot) | 1.5.10, 1.5.10.1, 1.5.10.4 (+154) | 063–075, 087–092, 154 | 20 |
| B2 | 1.5.10.2, 1.5.10.3 | 076–086 | 11 |
| B3 | 1.5.1, 1.5.2 | 006–021 | 16 |
| B4 | 1.5.3–1.5.5 | 002, 003, 022–031 | 12 |
| B5 | 1.5, 1.5.6, 1.5.7 | 001, 004, 032–038 | 9 |
| B6 | 1.5.9, 1.5.9.1 | 005, 039–054 | 17 |
| B7 | 1.5.9.2 | 055–062 | 8 |
| B8 | 1.5.11–1.5.12.1.1 | 093–112 | 20 |
| B9 | 1.5.12.1.2–1.5.12.1.4 | 113–131 | 19 |
| B10 | 1.5.13–1.5.15 | 132–150 (154 in B1) | 19 |
| B11 | 1.5.16 | 151–153, 155–158 | 7 |
| B12 | 1.5.17 | 159–167 | 9 |
| B13 | 1.5.19, 1.5.20 | 168–182 | 15 |
| B14 | 1.5.21.2.x | 183–202 | 20 |

(154 sits in §1.5.16 but generates in B1 per the pilot ruling; B11
carries the remaining seven Traffic & Weather leaves. B10's count includes
146–150 §1.5.15.)

### SXM notes

1. **Cross-chapter twins (A-SX04)**: 11 SXM leaves (020, 024, 037, 108,
   110, 132, 140, 142, 143, 148, 149) are ≥0.95 twins of AMFM §1.3.x
   clauses — each generates normally against its OWN §1.5.x clause in SAT
   context; Remarks carry `Analog-chapter twin: CFTS024-<analog id>
   (covered in the AM/FM deliverable)`. Two pairs (020, 024) differ only
   in band vocabulary; §8.6 SAT wording applies.
2. **R11 cite-form leaves (A-SX02)**: 005, 080 (`CFTS024-193/195/197`),
   107 (`CFTS019-494/496`), 137 (`CFTS020-138`) — token quoted as second
   spec_reference, borrowed outcome anchored, cited rule surface untested.
   Upgrade branch CLOSED (four-format negative).
3. **`(add)` leaves (A-SX03)**: 080, 083, 110, 148, 149, 154–158, 182
   generate normally with `[A-SX03]` in reasoning. §1.5.16 carries 5 of
   its 8 leaves on this list — B11 review reads them together.
4. **Leaf 154 (A-SX07)**: content follows clause `4872962` (Browse entry
   path); the 037 title is the defect; reasoning stacks `[A-SX03]` +
   `[A-SX07]`.
5. **Unallocated clauses**: 38 CFTS024 §1.5.x clauses (32 SFR) reach no
   leaf (§1.5.8, §1.5.12.1.5+, §1.5.18, §1.5.21.1, §1.5.21.2.1 own
   whole-section gaps; list in `data/unallocated_clauses.json`).
   **R10-2 ADOPTED for SXM (Pei, 2026-08-10; A-SX08)**: absorption iff
   (a) same spec section AND (b) the clause elaborates the leaf's cited
   clause; on absorption — `[A-SX08]` marker + the absorbed id in
   specification_reference (multi-cite); failing the test → coverage hole
   in reasoning + RD-1. Whole-section gaps cannot pass (a) and go to RD-1
   Q-SX as an allocation-policy question (Q-AM3 wording pattern), never
   silently absorbed.

### Workbook sync

BLANK workbook, FILL ruled (DECISIONS §4): Test Group `SXM` and the Part
IV Test Set values go in columns G/H on every generated row. Whether
revision C carries a `Test Case Framework` sheet is verified at
feature.yaml wiring (Tier 1); if present, populate it with the 14 Set
names, else per-row columns suffice (AMFM precedent).

---

## Part V — Projection

> Feature: `Projection`（R-P1）· workbook_state: `FULL_REFINE`
> 起草：分析層 2026-08-12 · 依據 canon §4.1 三層框架
> 狀態：**可簽版**，其中 §N.2 兩個 Set 為暫定（見 §N.5）

---

## N.0 本 Part 的特殊性

Projection 是本 repo 唯一非 regen 的 feature。`NR1L_GEN1(HDCC)_Ver_20260813.xlsx`
已有 559 列 TC、涵蓋 171 條 037 leaf 中的 164 條，並在五個 build 上執行過，
**387/559（69%）至少有一個 build 留有 Pass/Fail 紀錄**。

因此 workbook 的 `Test Group` 與 `Test Set` 兩欄依 profile §6 **全部凍結**，
可編輯者僅 `Pre-Conditions (I)` 與 `Test procedure (K)`。

**本 Part 記錄的是真實三層結構，不是 workbook 欄位的現狀。** 兩者分岔之處
以對映表回指，不改欄。這是 `FULL_REFINE` 的必然代價；後人不得將分岔誤讀為
「框架未清理」。

---

## N.1 Layer 1 — Test Group

**單值：`Projection`**

= spec 文件標題、= R-P1 之 feature 名，canon §4.1.1 無判斷餘地。

workbook `Test Group` 欄現有 10 值，為繼受之凍結產物，**係三個維度被壓進
一欄**（A-PJ06）：

| 混疊維度 | 欄內值 | 列數 |
|---|---|---|
| 功能域 | Device Manager / Audio Management / Media Player / GPS / Touch | 192 / 31 / 23 / 30 / 57 |
| 投屏協定（實為軸，見 §N.4） | Carplay Wired and Wireless / Android Auto Wired and Wireless | 60 / 58 |
| 傳輸（實為軸，見 §N.4） | Bluetooth / WiFi | 53 / 51 |
| 硬體特性標籤 | SSE / ECNR | 4 |

10 × 18 = 180 格僅 46 格非零，稀疏度即維度混疊之結果。**不改欄**。

---

## N.2 Layer 2 — Test Set

### 判準（合併版）

單一指標皆不足以判定。以下三者**滿足其一**即為乾淨叢集：

1. **RD 側集中** — 037 Sub Categorization 主導比例 ≥ 67%
2. **軸解釋** — 跨 Test Group 之分布可由 §N.4 之軸完全解釋
3. **Layer 3 同父章或同入口** — R-P24（同父章）或 R-P25（跨父章但共享 UI 入口）

判準存在的理由是 `Connection`：RD 側 57%、Layer 3 主導章 65%，兩個單一指標
皆不及格，但跨 TG 全由傳輸軸解釋、餘 19 列全在同父章 `.11` 之下——它是乾淨的。
單用 RD 側指標會誤殺它，單用 TC 側分布會誤放 `HMI Display`。

### 判定表

| 判定 | Test Set | 列 | 依據 |
|---|---|---|---|
| ✅ | Knob | 42 | L3 100% `1.3.2.10.1` |
| ✅ | Voice Recognition | 22 | L3 100% `1.3.2.7` |
| ✅ | Day/Night Mode | 22 | L3 100% |
| ✅ | Cluster Navigation | 12 | L3 100% |
| ✅ | Wireless Coexistence | 4 | L3 100% `1.3.2.11.4` |
| ✅ | Disconnection | 49 | 排除版本章後 L3 87% `1.3.2.11.5` |
| ✅ | Projection Apps | 12 | RD 側 83% |
| ✅ | Pairing | 12 | L3 80% `1.3.2.11.2` |
| ✅ | Projection Detection | 49 | 跨 1 TG |
| ✅ | USB Device | 4 | 跨 1 TG |
| ✅ | Projection Display | 5 | L3 67%（小樣本） |
| ✅ | **Connection** | 61 | 傳輸軸 + 同父章 `.11`（R-P24） |
| ✅ | **Projection Launch** | 65 | 86% 集中 Device Manager；逸出 9 列中 6 列由傳輸軸解釋，Media Player 3 列（4.6%）為邊界個案 |
| ✅ | **Device Manager** | 54 | 共享 UI 入口 96%（52/54）；18 列落 `.11.3` 係 spec 依作用歸章（R-P25） |
| ✅ | Vehicle Signal Forwarding | 22 | 同父章 Location Data 樹 `.10.2`/`.10.3`（R-P24） |
| ⬛ | **Performance** | 10 | **橫切狀態叢集** |
| ✅ | **Projection Audio** | 37 | **乾淨**（R-P33）；涵蓋 97%，CFTS019 `1.3.3.1 Source Priorities` 16 列跨 1 Set + Addendum `3.2.7.2 Audio` 樹 12 列跨 1 Set |
| ❌ | **HMI Display** | 76 | **確定綑綁**（R-P26）；雙來源同向、合併涵蓋 64%，見 §N.2 子叢集 |

### `Performance` — 橫切，不適用 §4.1.3

L3 100% 對到 `1.3.2.11.4 Active Wireless Projection`。**它驗的是「投屏進行中」
這個狀態，而非某個功能**——這解釋了為何它散在 WiFi / Media Player /
Audio Management / Touch 四個 TG 而協定完全一致。

它與其餘 17 個 Set 不同層。**§4.1.3 之「同 Test Set 應共享 setup 與 UI 入口」
健康判準對它不適用**，不得據此判其為綑綁。profile 以 `[ADD]` 承接此例外。

### `HMI Display` — **確定綑綁**（R-P26），三個子叢集

```
44 列  協定軸（CarPlay 22 + AA 22 × Wired+Wireless）
21 列  功能域（Touch 13 + Media Player 8）   ← 42% 逸出，軸解釋不掉
11 列  傳輸（Bluetooth × Wireless）
```

判定門檻即 **42%（HMI Display）vs 4.6%（Projection Launch）**——逸出比例是
綑綁與邊界個案的分界線。

**R-P26（2026-08-12）將本項由暫定收為確定。** 依據為兩份互相獨立的樣本同向：
CFTS085 側 26 列、主導章 38%、跨 3 章節；HUIG 側 30 列、散在 8 子章、跨 4 個
頂層章（`7 Video` / `9 Input devices` / `13 Application status` /
`15 Multi-Display`）。合併涵蓋 49/76 = **64%**，已過半。子叢集拆解維持三分。

子叢集以列號範圍記錄於本 Part，**`Test Set` 欄維持 `HMI Display` 不動**（凍結）。

---

## N.3 Layer 3 — spec 章節分組

**不寫入 workbook**（canon §4.1.5）。推導來源為 workbook 自身的
`Specification Reference` 欄——558/559 列具名引用，比人工分章可靠。

### 粒度：五碼（R-P23）

四碼會把不同能力壓成一格。兩處必須展開：

```
1.3.2.11 Wireless Projection (120)
   .11.2 Pairing to Wireless          27 → Connection 19, Pairing 8
   .11.3 Connecting to Wireless       55 → Connection 35, Device Manager 18
   .11.4 Active Wireless              18 → Performance 10, Wireless Coexistence 4, Projection Launch 4
   .11.5 Disconnecting from Wireless  20 → Disconnection 20 (100%)

1.3.2.10 Vehicle/Location Data (88)
   .10.1 Vehicle Sensor Data          71 → Knob 42, Day/Night Mode 22
   .10.2/.3 Location Data             17 → Vehicle Signal Forwarding 100%
```

四碼相鄰性仍用於 R-P24 之同父章判定。

### 雙閘門結構（R-P31 / R-P32）—— 一半機械、一半人工

Layer 3 的推導單位須通過**兩道互不涵蓋**的閘門：

```
推導單位 → [結構閘門 R-P29]  → [語意閘門 R-P23 / R-P32] → 進入同構檢驗
            跨 Set 數 ≥ 6 排除     界線是否沿功能切分
            機械可算，每輪自動跑    人工讀標題，逐案登記理由
```

| 閘門 | 量什麼 | 判定方式 | 裁決 |
|---|---|---|---|
| 結構 | 界線夠不夠細 | 機械可算 | R-P29 |
| 語意 | 界線切的方向是否為功能 | 人工判定 | R-P23 / R-P32 |

**兩者不得合併，不得以其一涵蓋其二。** 實測證明互不涵蓋：version-track 五章
跨 Set 數為 4/1/1/2/1，**全數通過結構閘門**，只有語意閘門攔得住；SYSAD
`4.6.1`（跨 10 Set）則只有結構閘門抓得到。

> ▎**語意閘門不得自動化**（R-P32）。「標題含 release 標記者排除」之類的字串
> ▎啟發式會誤傷標題含版本標記的真功能章節，且無法涵蓋未預期的非功能切分
> ▎維度。一律人工閱讀，逐案登記**章節 id、列數、切分維度、為何該維度非功能**。

後人若見語意閘門「還沒自動化」，那不是待補的缺口，是刻意的設計。

**已登記之語意性排除**：

| 章節 | 列數 | 切分維度 | 為何非功能 |
|---|---|---|---|
| CFTS085 `1.3.2.14` ~ `1.3.2.18` | 115 | 時間／release（`SR20+` / `SR21+` / `SR22+`） | 按 release 收錄該版新增之認證需求，橫跨功能是構造使然 |

**鑑別力對照**（說明兩閘門各自的必要性）：

| 推導單位 | 服務列 | 跨 Set | 結構閘門 | 語意閘門 |
|---|---|---|---|---|
| CFTS019 `1.3.3.1 Source Priorities` | 16 | **1** | 通過 | 通過 |
| CFTS085 `1.3.2.14 SR20+ …Changes` | 85 | 4 | **通過** | **排除** |
| SYSAD `NRL-154702 4.6.1 需求對映` | 190 | **10** | **排除** | — |

第一列與第三列的鑑別力相差三個數量級。**一個 clause 服務一個 Set 的全部
相關列，就是 Layer 3 該有的形狀。**


### 版本沿革章節排除（R-P23）

`1.3.2.14` ~ `1.3.2.18`（115 列 = CFTS085 引用之 24%）按 release 切分，
必然橫跨功能，**排除於 Layer 2 同構檢驗之外**，另記為 `version-track`。

> ▎ 排除僅在框架推導階段生效。這 115 列的 spec 核對對象仍是那些版本章節。
> ▎「排除於同構檢驗」不等於「沒有 spec 依據」。

### 涵蓋率

> ▎**本 Part 之引用計數一律以「列」為單位**，非以引用行為單位（A-PJ27）。

| | 列數 | 佔比 |
|---|---|---|
| 引 CFTS085 → Layer 3 已解 | 473 | 85% |
| 未引 CFTS085 → Layer 3 未解 | 85 | 15% |

未解 85 列之來源（**逐列計數**，單列可多引）：

| 來源 | 列數 | 佔 85 列 |
|---|---|---|
| **SYS3_PROJ** | **71** | **84%** |
| CarPlay Addendum | 44 | 52% |
| HUIG | 39 | 46% |
| Projection HMI | 11 | 13% |
| CFTS019 | 10 | 12% |

原稿此處作「HUIG 75」，係逐引用行計數被當作逐列使用；巧合在於 HUIG 的行計數
75 與 `HMI Display` 50 + `Projection Audio` 25 之列數和相同，使誤用表面自洽
（A-PJ27）。已依實測更正。

---

## N.4 軸（§8.3 sibling 軸，非層）

| 軸 | 值 | 分布 |
|---|---|---|
| 投屏協定 | CarPlay 212 / Android Auto 198 / 兩者 106 / iPod 5 / 無 38 | 抽自 Test Item + Test Group |
| 傳輸 | Wired / Wireless / 無 | 獨立於協定運作 |

傳輸為獨立軸之證據：`Connection` 固定 `CarPlay+AndroidAuto × Wireless` 那格
16 列，協定變數鎖死，仍分岔為 Bluetooth 13 / WiFi 3。

`SSE / ECNR`（4 列）登記為**硬體特性標籤**，非軸非層。

---

## N.5 暫定項與待辦

### 現況（2026-08-12，HUIG 與 SYSAD 推導後）

| Set | 總列 | Layer 3 涵蓋 | 判定 |
|---|---|---|---|
| HMI Display | 76 | 49（64%，CFTS085 26 + HUIG 30） | ❌ **確定綑綁**（R-P26） |
| Projection Audio | 37 | **36（97%）**，四來源併用 | ✅ **乾淨**（R-P33） |

**兩者皆已定案，§N.2 無暫定項。** `Projection Audio` 的判定翻過三次
（暫定乾淨 → 存疑 → 乾淨），三次都不是改判準而是補證據；真正結案的是
CFTS019 那 16 列落在單一章節，而該來源被 SYSAD 的假集中遮蔽了三輪（A-PJ29）。

**門檻紀律（A-PJ30）**：定案與暫定的分界在**絕對列數**，非百分比。
`Projection Audio` 暫定時 23 列、定案時 36 列；當初 62% 與 `HMI Display`
的 64% 只差 2 個百分點，實質差別是 23 列對 49 列。

### 待辦 —— **全數完成（2026-08-12）**

1. ~~HUIG 4.5 Layer 3 推導~~ —— 完成，見 §N.7
2. ~~SYSAD 推導（R-P28）~~ —— 完成但未能結案（假集中），見 §N.8
3. ~~`Projection Audio` 結案來源改指~~ —— R-P30，改為四來源併用
4. ~~CFTS019 / CarPlay Addendum 推導~~ —— 完成，見 §N.9
5. ~~複驗 §N.2 並關閉 A-PJ06~~ —— **R-P33 定案，A-PJ06 已關閉**

Layer 2 定案：**16 乾淨 + 1 橫切（`Performance`）+ 1 綑綁（`HMI Display`）**。

尚未推導者：Projection HMI（11 列）、Device Manager HMI（75 列）。兩者皆不
影響 Layer 2 判定，屬 Phase 4 需要時再跑。

---

## N.6 對映表 — 真實三層 ↔ 凍結欄

| 真實結構 | workbook 欄 | 處置 |
|---|---|---|
| Layer 1 = `Projection` | `Test Group` 10 值 | 不改欄；混疊維度記於 §N.1 |
| Layer 2 = **16 乾淨 + 1 橫切 + 1 綑綁** | `Test Set` 18 值 | 不改欄；`HMI Display` 子叢集記於 §N.2 |
| Layer 3 = CFTS085 五碼 + 其餘來源 | 無對應欄 | canon §4.1.5，本就不寫入 |
| 協定軸 / 傳輸軸 | 混在 `Test Group` | 不改欄；記於 §N.4 |

**row 562**（`SWE1-PROJ-227` 殘樁，九個 TC 內容欄全空）依 R-P19 刪除，
資料列 559 → 558。不屬框架議題。

---

## N.7 執行層附註 — HUIG Layer 3 推導結果（2026-08-12）

> 本節由執行層於 Part N 落檔同日追加，記錄 §N.5 待辦第 1 項的執行結果。
> **§N.2 的兩個 ⚠️ 判定與 §N.5 的優先順序均受此節影響，待分析層複核後更新。**

### 推導方法（與 CFTS085 不同）

HUIG 是 SYS.1 層產物，`inputs/HUIG 4.5.pdf` 為網頁列印版：**15 頁、無 PDF
outline**，但有完整文字層（389,388 字元、1,926 個 R-ID）。CFTS085 的
`{clause id}` 錨點法不適用。

改採 **R-ID 前綴為章號權威**：`R06-010` → 第 6 章。純以行內標題推導時章號
一致性僅 81%（前幾章的圖說被誤判為標題）；改以 R-ID 前綴約束後，
**1,028 個 R-ID 的章號一致性達 100%**。子章標題僅在章號相符時採用，否則
退回章層。結果存於 `features/projection/data/huig_sections.json`。

workbook 的 HUIG 引用解析：**62 列命中**，未解 R-ID 僅 `R10-250` 一個。

### 對兩個暫定判定的影響

**`HMI Display` —— HUIG 證據使「綑綁」判定更強，非推翻。** 其 30 列 HUIG
引用散在 **8 個子章、橫跨 4 個頂層章**：

```
13.3 Accessing media data 4 · 7 Video 3 · 7.8.2 Reported screen density 3
7.8.1 Codec resolution support 3 · 9.1 Touchscreen 3 · 13.4 Accessing Telephony data 3
7.10 Video focus 3 · 15.2 Video Management 3
→ 頂層章：7 Video / 9 Input devices / 13 Application status and data / 15 Multi-Display
```

CFTS085 樣本說「3 個章節、主導 38%」，HUIG 樣本說「8 個子章、4 個頂層章」。
兩份互相獨立的證據同向。

**`Projection Audio` —— 由「暫定乾淨」轉為存疑。** 11 列 HUIG 引用散在
3 個頂層章：`6 Bluetooth`(5)、`8.2.2 Media stream`(3)、`10.x ASR`(3)。加上
CFTS085 側的 50% / 3 章節，兩份樣本皆不支持「乾淨」。

### 合併涵蓋率（CFTS085 + HUIG）

| Test Set | 總列 | CFTS085 | HUIG | 合併 | 涵蓋率 |
|---|---|---|---|---|---|
| HMI Display | 76 | 26 | 30 | 49 | **64%**（仍未解 27） |
| Projection Audio | 37 | 12 | 11 | 23 | **62%**（仍未解 14） |
| Projection Display | 5 | 3 | 0 | 3 | 60% |
| Pairing | 12 | 10 | 0 | 10 | 83% |
| Vehicle Signal Forwarding | 22 | 21 | 0 | 21 | 95% |
| Connection | 61 | 60 | 0 | 60 | 98% |
| 其餘 12 個 Set | — | — | — | — | **100%** |

### ⚠️ §N.3 與 §N.5 的一個數字需要修正

§N.3 列「未解 85 列之來源：**HUIG 75** / SYS3_PROJ 71 / …」，§N.5 稱
「兩者未解的 75 列**幾乎全部引 HUIG**」。實測不支持：

| 來源 | 出現於 85 列中 |
|---|---|
| **SYS3_PROJ** | **71（84%）** |
| CarPlay Addendum | 44（52%） |
| **HUIG** | **39（46%）** |
| Projection HMI | 11 |
| CFTS019 | 10 |

逐 Set 看更清楚：`HMI Display` 未解 50 列中 SYS3_PROJ 佔 **41（82%）**、HUIG
僅 23（46%）；`Projection Audio` 未解 25 列中 SYS3_PROJ 佔 **25（100%）**、
HUIG 僅 12。「75」應是 `HMI Display 50 + Projection Audio 25` 這個和被誤植
到 HUIG 一欄。

**因此 §N.5 的待辦順序建議調整**：最大的 Layer 3 缺口是
`SYS3_PROJ_FM-WI-FSM-011-A01 SYSAD`（71 列），不是 HUIG。HUIG 已推導完畢仍
留下 27 + 14 列未解，補齊它們要靠 SYSAD 與 CarPlay Addendum。
此項未自行改寫 §N.5，待分析層裁定。

---

## N.8 執行層附註 — SYSAD Layer 3 推導結果（2026-08-12，R-P28）

> 本節由執行層追加，記錄 R-P28 指定之 SYSAD 優先推導的執行結果。
> **結論：機械上成功，但未能結案 `Projection Audio`。** 待分析層複核。

### 推導方法（先探測，未預設）

依 R-P28 之提醒，先探測再決定方法。SYSAD 為 `.docx`，探測結果：

- **無 heading 樣式**（pStyle 僅 `a1` / `af5` 兩種匿名樣式，heading-styled
  段落數 = 0），故 Word outline 法不可用
- **有純文字 outline**：`4.2.1 設計目標與需求對映 …` 形式，共 82 個章節標題
- `NRL-xxxxxx` 內嵌於標題段落，形式為
  `NR1L/NRL-154702NRL-154702 - 4.6.1 設計目標與需求對映`

故採**章節追蹤法**（與 CFTS085 同類），**未套用 HUIG 的 R-ID 前綴法**。

結果：254 個 NRL id 全數對映至章節；workbook 引 SYSAD 之 **500 列中解出 498
列**，未解 NRL id 26 個。存於 `features/projection/data/sysad_sections.json`。

### ⚠️ 但 SYSAD 不能用於同構檢驗

**SYSAD 的 `NRL-xxxxxx` 是章節 id，一節一個，不是需求 id。** 三份來源的
id 性質不同類：

| 來源 | id 性質 | 粒度 |
|---|---|---|
| CFTS085 | 需求條款 id | 85 個 id / 473 列 |
| HUIG | 需求 id（前綴即章號） | 1,028 個 id 可用 / 62 列 |
| **SYSAD** | **章節 id** | **99 個 id / 500 列** |

鑑別力實測 —— 單一個 `NRL-154702`（`4.6.1 設計目標與需求對映`）服務
**190 列、橫跨 10 個 Test Set**，其中含 `HMI Display` 全部 67 列與
`Projection Audio` 全部 37 列。前 5 個 id 覆蓋 1,085 次引用中的 391 次。

一個橫跨 10 個 Set 的章節無法用來區分 Set。且 `4.6` 為
「車輛狀態與導航數據」，與 `HMI Display` / `Projection Audio` 語意亦不相符
——`設計目標與需求對映` 是需求對映表，表內列舉大量跨領域需求。

### 與 §N.3 version-track 的關係：同類、反向

| | version-track（A-PJ26） | 需求對映表（A-PJ29） |
|---|---|---|
| 造成 | **假分散** —— 乾淨叢集看似綑綁 | **假集中** —— 綑綁看似乾淨 |
| 若不處理 | 誤殺 `Disconnection` | 誤放 `HMI Display` |

**假集中比假分散危險。** 假分散讓人多切一刀，成本可回收；假集中讓綑綁通過
檢驗，缺陷留在框架裡。若逕採 SYSAD 結果，`HMI Display` 的 SYSAD 側同構度是
**67/67 = 100% 單一章節**，正好與 R-P26 的定案相反。

### 對 R-P28 前提的影響

R-P28 的前提為「`Projection Audio` 剩餘 14 列的 Layer 3 只可能來自 SYSAD ——
它是唯一能結案的來源」。**此前提不成立**：SYSAD 對該 Set 的全部證據落在一個
橫跨 10 Set 的對映表章節，等同無證據。排除該型章節後，SYSAD 對兩個爭議 Set
的剩餘證據為 `Projection Audio` 4 列（`4.7.2`）、`HMI Display` 0 列。

**`Projection Audio` 的結案來源需重新指定**；CarPlay Addendum（44 列）為
下一個候選。詳見 A-PJ29，**未自行改寫 §N.5 之待辦順序**，待分析層裁定。

---

## N.9 執行層附註 — R-P29 閘門實測 · CFTS019 / CarPlay Addendum 推導（2026-08-12）

> 本節由執行層追加。**§N.2 的 `Projection Audio` ⚠️ 已具備結案條件，
> 但未自行改寫，待分析層裁定。**

### R-P29 鑑別力閘門 — 逐 id 實測，未預設黑名單

門檻：單一推導單位橫跨 Test Set 數 ≥ 6 者排除。五份來源全部逐一計算：

| 來源 | 推導單位數 | 排除 | 觸及列數 |
|---|---|---|---|
| CFTS085（五碼章節） | 25 | **0** | 0 |
| HUIG（章節） | 26 | **0** | 0 |
| CarPlay Addendum（章節） | 18 | **0** | 0 |
| CFTS019（章節） | 1 | **0** | 0 |
| **SYSAD（章節）** | 34 | **2** | 277 |

落入者僅 SYSAD 兩章：`4.6.1 設計目標與需求對映`（197 列 / 跨 **10** Set）、
`4.2.1 設計目標與需求對映`（80 列 / 跨 **6** Set）。

**通則優於黑名單，當場證實**：執行端先前提議排除全部三個
`設計目標與需求對映` 型章節，實為過度排除 —— 第三個 `4.5.1`（11 列 / 跨
3 Set）通過閘門且確有鑑別力。排除清單存於
`features/projection/data/layer3_gate.json`。

### ⚠️ 閘門不涵蓋 §N.3 的 version-track

R-P29 立論「A-PJ26 與 A-PJ29 是同一缺陷的兩種表現」**不成立**。在 R-P23
裁定的五碼粒度下，version-track 五章全部**通過**閘門（`1.3.2.14` 跨 4 Set、
其餘 1~2 Set，皆 < 6）。

兩者是不同機制：R-P29 量的是「界線夠不夠細」（結構、機械可算），R-P23 排除
的是「界線沿著時間而非功能切」（語意、須讀標題）。version-track 確實有鑑別
力，只是切的方向不對。

**§N.3 的 version-track 排除條款須獨立保留**，不得因 R-P29 上線而撤下 ——
撤下則 `Disconnection` 等會重新被誤判（主導章佔比由 87% 掉回 41%）。
詳見 A-PJ31。

### CFTS019 推導（R-P30，先跑）

`.doc` 二進位格式，以 `textutil` 轉純文字後採章節追蹤法（與 CFTS085 同類）。
234 個章節標題、1,965 個 clause 對映。

workbook 僅引用 **2 個 clause id**（`4866445` / `4866450`），16 列全屬
`Projection Audio`，且**兩者落在同一章節**：

```
CFTS019 1.3.3.1  Source Priorities   16 列 / 跨 1 個 Test Set
```

R-P30 的語意判斷完全命中 —— CFTS019 是 Audio Management 的 CFTS，
`Source Priorities` 正是 `Projection Audio` 的核心議題。

### CarPlay Addendum 推導

**方法須另擇**：`.docx` 的章節編號存於 `numPr`，文字層取不到（僅 49 個可解
標題，`3.2.6` 等全部落空）。改用 **PDF 的 320 項 outline**，得 310 個帶編號
章節。97 列引用解出 **72 列，未解 id 0 個**。

這是第三種方法。三份來源各不相同，皆先探測後決定：

| 來源 | 格式 | 方法 |
|---|---|---|
| CFTS085 | `.docx` | 內文 `{clause id}` 錨點 + 章節追蹤 |
| HUIG | `.pdf`（網頁列印版，無 outline） | **R-ID 前綴為章號權威** |
| SYSAD | `.docx`（無 heading 樣式） | 純文字 outline + 章節追蹤 |
| CFTS019 | `.doc` | `textutil` 轉檔 + 章節追蹤 |
| CarPlay Addendum | `.pdf` | **PDF outline**（docx 不可用） |

### `Projection Audio` — 結案條件已具備

排除 SYSAD 後，Layer 3 涵蓋 **36/37 = 97%**（唯一無證據者為 row 521，屬
PCTS/MT1 列）。章節分布：

| 來源 · 章節 | 列數 | 跨 Set |
|---|---|---|
| **CFTS019 `1.3.3.1 Source Priorities`** | **16** | 1 |
| Addendum `3.2.7.2 Audio` 樹（Mixing 5 / Ducking 2 / Main Audio 4 支 / Audio 1） | 12 | 1 |
| Addendum `3.3.3 Resource Management` | 8 | 1 |
| HUIG `6 Bluetooth` | 5 | 2 |
| HUIG `8.2.2 Media stream` | 3 | 1 |
| HUIG `10.x ASR` | 3 | 2 |

依 R-P24（同父章）收斂後，**CFTS019 `1.3.3.1` 16 列 + Addendum `3.2.7.2`
12 列 = 28 列集中在兩個語意明確的音訊章節**，跨 Set 數皆為 1。

先前判為存疑的依據（CFTS085 側 50%/3 章節、HUIG 側 3 個頂層章）是在
**32% 樣本**上作出的；現在涵蓋率 97%，且主要來源高度集中。

**建議**：`Projection Audio` 由 ⚠️ 收為 ✅（乾淨）。依 A-PJ30 之門檻檢查，
絕對列數為 36/37，遠高於當初 23/37 的暫定水位。**未自行改寫 §N.2，待裁。**

若此項收為 ✅，**A-PJ06 即可關閉**，Layer 2 定案為
**16 乾淨 + 1 橫切（Performance）+ 1 綑綁（HMI Display）**。

---

## Part VI — Privacy (CFTS022)

Ruled by Pei 2026-08-13（「可以」）：Test Group `Privacy`；下列三 Set 表；
批次計畫 B1（pilot）/ B2。

Deliverable workbook: FM-WI-FSM-036-A01 空白範本 rev C
`SWQT_20260121`（SHA256 `cd876c202c71e74b…`，A-PV01 / R23-1 裁定以通用
範本產生 Privacy 交付件即為最終形態）; RD source 037-A03
`SWE1_CFTS_022-Privacy_Features.xlsx`（**10 leaf FRs**,
`SWE1-HMI-PRIVACY_FEATURES-001…010`, 版本 C 核准 2026-02-09）;
spec_mode **D** —— clause 權威為 CFTS022 docx
（R1LR Atl-H 25PI3.5, 20250910_1708）。
SYS3 SYSAD 為 **context-only**，不得列入 `specification_reference`
（R23-3，§10.7）。外部參照 VF651（見 Part VI 注 3）。
執行計畫 `features/privacy/RUNBOOK.md`；profile
`docs/runtime/profiles/FW036_R1L_Privacy_Profile.md`（待建）；
rulings `features/privacy/RULINGS.md`（R22–R25）。

**Workbook state**: BLANK —— 無 legacy region。範本殘留樣本列（第 10–11 列）
依 R23-4 以 zip 層外科手術清除五格（D10/F10/G10/S10/D11），B 欄序號公式
`=IF(ISBLANK($D10),"",ROW()-9)` 保留。首筆 TC 落第 10 列，
tc_id `NR1L-Privacy-001` 起算（R-PV02）。
Style authority = fallback chain；跨 feature 樣本僅供形式，
每一 literal 回溯本 feature 之 spec 行。

### Layer 2 derivation note — §4.1.2 的第三種退化

AMFM 與 SXM 的退化是「RD 側分群無資訊」（Categorization 全同值），
Privacy 的退化在另一側：**spec 側沒有章節結構**。

CFTS022 匯出實測 336 個 artifact，型別僅 `Description` 83 +
`Subsystem Functional Requirement` 253，**Heading 型 0 個** —— 這是平鋪
匯出，沒有 TOC 可與 037 分群取交集。故 Layer 3 改用 spec 自身之
**artifact id 區塊**（canon §4.1.1 要求用 spec 自己的 id，非自創標籤）。

RD 側之 Sub Categorization **有兩值**（`Service` 4 筆：001/004/005/010；
`HMI` 6 筆），但它切的是「訊號側 vs 顯示側」，橫跨 Speed-Controlled
Volume，且 `Service` / `HMI` 本身是分類標籤而非能力名稱（§4.2 禁）。
故不作為 Layer 2，改記為軸（見注 2）。

### PROF → CFTS022 artifact 對映（實測，offset = −1）

037 之 Source Requirement ID 為 `SYS-RA-PROF-nnn`，CFTS022 之 artifact
為 `4915xxx`。實測連續 8 筆全中，**offset 恆為 −1**：

| leaf | SYS-RA-PROF | CFTS022 artifact | 條文要旨 |
|---|---|---|---|
| -003 | PROF-169 | 4915168 | HU wakes up on Interior CAN → recall SCV state |
| -004 | PROF-170 | 4915169 | HU wakes up → send `$VolumeSCV$` within `<Tsend>` |
| -005 | PROF-171 | 4915170 | valid signals for `$VolumeSCV$`；其餘視為 invalid |
| -006 | PROF-172 | 4915171 | amp **not** present → HU adjusts output volume |
| -007 | PROF-173 | 4915172 | AMP present → HU shall **not** change level |
| -008 | PROF-174 | 4915173 | AMP wakes up on Interior CAN → AMP recalls SCV state |
| -009 | PROF-175 | 4915174 | no amp + user changes level → HU … |
| -010 | PROF-176 | 4915175 | amp present + user changes level → HU … |

`specification_reference` 據此構成。

**offset −1 是 SCV 區塊之局部規律，不是通則（R30-1）。** 上表八筆全中，
是因為它們同落在一段無缺號的 id 區間內；CFTS022 之 artifact id **不連續**
（4914928–4915339 區間即缺 79 個號），故 `4915000 + PROF − 1` 之算術推定
在任何缺號跨越處都會失準。**id 一律以查得為準，不得以位移構造**
（profile §3.5）。

-001 / -002 兩筆經 B1-GATE-1 獨立重驗後更正（R30-1），且兩筆之判準不同型：

| leaf | 原填（作廢） | 正解 | 判準 |
|---|---|---|---|
| -001 | ~~4915022~~ —— **文件內不存在** | **4914955** | **ECU tag**：4914954 為 `ECU=SCCM`、Radio 清單無 `R1L-R` 亦非 `allSys`；4914955 為 `ECU=ETM, RRM, ICS, DVD, LTM`、`Radio=allSys`。本專案 ECU 為 **LTM** → 4914955。量出來的，非語意判讀 |
| -002 | ~~4915159~~ —— splash screen 計時 | **4915158** | **條文語意**：4915158「Each time the Interior CAN wakes up, the HU shall recall the last known state for the configured set of personalization features to be displayed」對應 leaf 之 restore-on-wake-up；4915159 講的是開機畫面計時。兩者 ECU 皆含 LTM，**ECU tag 在此無鑑別力** |

### 未分配 clause —— 觀察，非覆蓋缺口

三條 HU/AMP 側 clause 在本 037 內無對應 leaf：

- `4915167`（PROF-168）—— HU 顯示 personalization entry 供使用者調整 SCV 音量
- `4915176` / `4915177` —— AMP 接收 `$VolumeSCV$` 後之比對與儲存

CFTS022 共 253 條功能需求而本 037 僅分得 10 片葉子，**「無 leaf」極可能
只代表分配給了其他 feature 之 037**。P2 須查證後方可判定，
**現階段不得記為覆蓋缺口**（canon §8.4.2 / 不對稱錯誤代價）。

### Layer 1 — Test Group

- `Privacy`（workbook Test Group 欄值：`Privacy` —— BLANK workbook，
  FILL 適用；= spec 文件標題、= 037 之 `PRIVACY_FEATURES`）

### Layer 2 / Layer 3 — Test Sets and their spec sections

Layer 3 = CFTS022 artifact id；framework-internal only —— NEVER 寫入 workbook。

| Test Set | Layer 3（CFTS022 artifact） | Leaves | n | Status |
|---|---|---|---|---|
| Input Monitoring | **4914955**（PROF-023） | -001 | 1 | remaining |
| Personalization Display | **4915158**（PROF-160） | -002 | 1 | remaining |
| Speed-Controlled Volume | 4915168–4915175（PROF-169–176，連續） | -003…-010 | 8 | remaining |

合計 10 = 全 leaf set。

### Granularity check（§4.1.3）

- 三個 Set 皆通過 filter test。
- **兩個單葉 Set 為 §4.2 之 genuine outlier**：-001（睡眠退出後恢復輸入
  監測）與 -002（Interior CAN 喚醒後恢復個人化顯示）是整個 feature 中
  僅有的兩條非 SCV 需求，與 SCV 不共享 setup 或 UI 入口。
  先例：AMFM `Tuner Availability`(2)、SXM `Source Availability`(1)。
- **Speed-Controlled Volume (8) 刻意不再細分**。若依 restore / signal /
  adjustment 拆為三組，全 feature 將成 5 Set 配 10 leaf、平均 2 片 ——
  正是 §4.1.3「Test Set 欄變成 TC ID 欄之近似複本」的過granular 反模式。
  先例：SXM `Instant Replay`(30) / `Browse`(39) 之不拆理由同源。

### Batch plan（生成批次 ≠ Test Set）

| Batch | Leaves | n | 內容 | 依賴 |
|---|---|---|---|---|
| **B1（pilot）** | -001, -002, -003, -004, -005 | 5 | 三個 Test Set 各至少一片；SCV 之 restore 與 signal 側 | **無** |
| B2 | -006, -007, -008, -009, -010 | 5 | AMP present / not present 之四條件分支 + AMP 側 recall | **無**（A-PV14 已 RESOLVED，R29-2）|

**pilot 刻意避開 AMP-present 分支**：那五片需引用 V6_R2，而 A-PV14
（`inputs/` 之 V6_R2 來自 DT28 平台樹而非 HDCC28）尚未結案。
如此 pilot 不被任何未決項阻塞，且仍覆蓋全部三個 Test Set。

### Privacy notes

1. **AMP present / not present 是成對的正負分支，不是重複**：
   -006/-007（自動調整側）與 -009/-010（使用者調整側）各構成一對
   present / not-present。依 §7「列舉之支援項必配至少一負向 TC」，
   兩對皆須各自成 TC，不得合併。

2. **Service / HMI 為軸，非 Set**（§8.3）：037 Sub Categorization 將
   -001/-004/-005/-010 標 `Service`（訊號側）、其餘六片標 `HMI`
   （顯示側）。該軸橫跨 Speed-Controlled Volume，可作為同一 Set 內
   sibling 之區辨提示，但不得升為 Test Set 邊界。
   先例：AMFM 注 2（band 是切分軸非 Set 邊界）、Projection §N.4（傳輸軸）。

3. **外部參照 VF651 —— 平台一致性（R24-2）**：`specification_reference`
   之 VF651 來源檔一律取 **HDCC28** 平台版本。
   - `VF651_V2_R2`（LTM Non-Amplified）：`inputs/` 現存 `d5813bb7…`
     已確認為 HDCC28 基線（R23-2）
   - `VF651_V6_R2`（LTM/ETM Amplified）：**已換入 HDCC28 版**
     `e20ba7a4…`（177,388 bytes，R29-2 確認）。原 `inputs/` 之
     `49dd3c31…` 來自 DT28 樹，經 R24-2 先量後換之程序汰換 ——
     SCV/AMP 條款零差異，屬平台標籤更正。**限制解除，B2 可引用**
   - `VF651_V3_R3`（ETM Non-Amplified）：在庫、**不引用**；
     不得因未列而視為已排除（A-PV03 / R-PV01(a)，DEFERRED 至 P2 重驗）
   - ANC 兩變體（V9_R3 / V11_R3）：Not requested（A-PV02）。
     若 P2 發現任一 leaf 觸及 ANC 配置，**停手回報**，不自行擴充

4. **範本層缺陷不修，隨 RD-1 回報上游**：下拉選單 R10 指向 `$A$1:$A$9`
   而 R11:R59 指向 `$A$1:$A$11`（含 2 空選項）（A-PV10 / R23-6）；
   `Reference!C9` 與 `下拉選單!A6` 第 6 條字串不符（A-PV11 / R23-7）。
   lint 之 design_method 權威為 `下拉選單!A1:A9` 九詞條。

5. **舊分頁保留**：`Cover_old` / `ChangeHistory_old` 原樣保留，
   不進 lint、不進 trace、不寫回（A-PV12 / R23-8）。
   佐證：AMFM 已交付件同樣保留該兩頁。

### Workbook sync

BLANK workbook、FILL 適用：Test Group `Privacy` 與 Part VI 之 Test Set
值寫入每一生成列之 G / H 欄。

**欄 S（Functional Safety）一律填 `NA`；車型欄 T–Z 一律留白（R30-3 / R30-4）。**
兩者皆由 AMFM 客戶端已交付件之 158 列人工語料量得：Functional Safety
158/158 全 `NA`，車型欄 S..Y **0/158** 有值。Privacy 空白範本之原廠樣本列
S10 本即為 `NA`，為第二個同向來源。
車型欄之世代落差（範本停在 HDCC27/DT27，本專案為 HDCC28）見 **A-PV15**，
登記後入 RD-1，**不自行對應**。
範本 rev C 是否帶 `Test Case Framework` 分頁，於 feature.yaml 接線時
查證（Tier 1）；若有，填入三個 Set 名稱，否則逐列欄位即足（AMFM 先例）。
---

## Part VII — Time and Date (CFTS015)

Ruled by Pei 2026-08-20: feature 名 `Time Management`、目錄 slug
`time_management`（R-TM1）；workbook Test Group 值 `Time and Date`
（R-TM8 —— 落回 canon §4.1.1 通則，因 BLANK workbook 使既有值優先之
條件永不觸發）。下列七 Set 表經 Pei 2026-08-20 簽核（R-TM17）。

Deliverable workbook: FM-WI-FSM-036-A01 rev C 母本
`…_SWQT_20260817_ext.xlsx`（R-TM5 —— 本 feature 不索取客戶預填件；
交付路徑 `ASW-R2/Time Management/` 實測確無 036，見 A-TM02a）;
RD source `SWE1_Secure_Date&Time.xlsx`（**22 leaf FRs**,
`SWE-RA-TIME&DATE-001…022`）—— **該檔命名不符 037-A03 慣例，身分未定
（A-TM02a，阻塞 D5）**; spec_mode **D** —— clause 權威為 CFTS015 docx
（R1LR Atl-H 25PI3.5, SR26 20250909-1851）; SYS2 export
（`Basic Report`, 227 列）為錨鏈中介。
執行計畫 `features/time_management/RUNBOOK.md`；
rulings `features/time_management/RULINGS.md`（R-TM1–R-TM16）；
anomalies 同目錄 `ANOMALIES.md`（A-TM01–A-TM16）。

**Workbook state**: BLANK —— 無 legacy region、無 done region。
**Style authority: 無。** R-TM10 曾准以 Home done region 為跨 feature 樣式
參照，但其唯一許可來源（Home v2 交付件）經 150 筆 SHA 全域比對確認不在
磁碟上，**R-TM10-A1 全條 SUSPENDED**（A-TM14）。故本 feature 與 SXM／
Privacy 不同：無 fallback chain 可用，TC 生成與 pilot review 一律僅依
條文（§4–§12）與本 feature profile。

**連帶後果（須明記）**：canon §1.1 三層品質結構之第三層（done region
以證據仲裁）在本 feature **不存在**，本 Part 不回復之。reviewer 之發現
不經 done-region check 過濾，分類結果直接成立；pilot 之爭議應預期多於
Home 與 AMFM。

### Layer 2 derivation note — §4.1.2 之第四例退化

與 AMFM／SXM 同型：037 之 `Categorization` 欄實測 **`Functional` 22/22**
（單值），RD 側分群軸零資訊，§4.1.2 之交集退化。

但與 AMFM／SXM 之補救不同。兩者改用「leaf id 機械對映至 spec 章節」，
本 feature **不可行** —— 037 無文件章節引用欄（其 `Source System
Requirement ID` 欄含 `requirement id` 字樣，被 `survey_a03()` 之 forbid
規則排除，`citation column: NOT FOUND` 係「無項可解析」而非「解析失敗」，
A-TM12）。

故 Layer 2 改由 **leaf 標題與 `Requirement Description` 全文之語意軸**
推導，章節僅作外部檢驗。錨鏈另經 SYS2 建立：

```
SWE-RA-nnn → SYS-RA-nnn → CFTS 物件 id → CFTS 章節號
 (037 col2)   (SYS2 col2)   (SYS2 col5)    (docx 標題 {id})
```

實測：SYS2 第 5 欄 227/227 零空白；78 筆被引用 SYS-RA 缺來源物件 id 者
0 筆；docx 88 標題 / 358 物件；71 筆直接可達、5 筆多物件儲存格切分後可達、
**2 筆不可達（A-TM13）**；相異可達章節 **21**。
逐 leaf 對映存於 `features/time_management/data/leaf_to_section_probe.txt`。

### Layer 1 — Test Group

- `Time and Date`（workbook Test Group 欄值 —— BLANK workbook，FILL 適用；
  = spec 文件標題 CFTS_015 Time and Date、= req id family `TIME&DATE`。
  feature 名 `Time Management` 為內部識別，不進工作簿）

### Layer 2 / Layer 3 — Test Sets and their spec sections

Layer 3 = CFTS015 印刷章節號；framework-internal only —— NEVER 寫入 workbook。

| Test Set | 主軸章節（Layer 3） | Leaves (SWE-RA-TIME&DATE-) | n | Status |
|---|---|---|---|---|
| Manual Setting | 1.5.2.3, 1.5.2.6 | 001, 015 | 2 | remaining |
| GPS Sync | 1.3.1.1.3, 1.5.2.4, 1.5.2.5 | 002, 003, 004, 014 | 4 | remaining |
| Master Clock | 1.3.1.1.2, 1.3.1.1.6.2 | 005, 006, 016, 018, 021 | 5 | remaining |
| CAN Transmission | 1.3.1.1.4, 1.5.2.1 | 008, 009, 017, 020 | 4 | remaining |
| Display | 1.3.1.1.1, 1.3.1.1.5, 1.3.1.1.5.1, 1.3.1.1.6.3 | 007, 011, 019 | 3 | remaining |
| Zone and DST | 1.3.1.1.5.3, 1.3.1.1.5.4 | 012, 013 | 2 | remaining |
| Fault Handling | —— 無主軸（見注 2） | 010, 022 | 2 | remaining |

合計 22 = 全 leaf set。

**條件章節不列為任一 Set 之主軸**：`1.5.2.2`（Key Off Status）、
`1.5.2.7`（Output behavior）依 R-TM15 為條件／輸出章節，跨 Set 出現屬預期。

### Granularity check（§4.1.3）

七 Set 範圍 2–5 leaf，皆通過 filter test。**無單葉 Set。**

`Manual Setting`(2)、`Zone and DST`(2)、`Fault Handling`(2) 為三個最小 Set，
皆非 §4.2 之 genuine-outlier 例外而是實質叢集：`Manual Setting` 之兩片呈
時／日結構對稱（`1.5.2.3` Time function setting ／ `1.5.2.6` Date function
setting，同層姊妹節）；`Zone and DST` 之兩片各落單一相鄰姊妹節；
`Fault Handling` 之兩片為同一能力之收送兩端。

**刻意不以時間／日期二分。** 若切為 Time / Date 兩組，`Master Clock` 與
`CAN Transmission` 之每一片都要兩邊各出現一次，Test Set 欄失去索引價值
（§4.1.3「太粗」）。時間與日期在本 spec 共用主控（`1.3.1.1.2` /
`1.3.1.1.6.2` 對稱）、共用傳輸（`1.3.1.1.4` 兼含時日）、共用初始化
（018 跨兩者），是同一能力之兩個資料欄位。
先例同源：AMFM 注 2（band 是切分軸非 Set 邊界）、SXM `Browse`（類別是
資料軸）、Privacy 注 2（Service/HMI 是軸）。

### 相鄰組界線（§8.2.1 —— 寫 TC 時據此避免重複覆蓋）

（五條界線經 Pei 2026-08-20 簽核，R-TM17 + R-TM25）

五處鄰接，由 leaf 描述全文比對浮現（前三處於 02R 定案；第四、五處由執行層以動詞軸橫掃全 22 列發現，R-TM23）：

| 鄰接 | 界線 |
|---|---|
| 004 GPS Fallback ↔ 010 Invalid Data | 004 管 **GPS 來源**不可用時改用內部時鐘；010 管**收到之時間訊號**無效時用最後有效值。觸發源不同 |
| 014 GPS Date/Time Broadcast ↔ 022 SNA Handling | 014 描述含「or SNA if unavailable」，但 **SNA／預設值之送出規則屬 022**；014 只驗 GPS 資料之送出 |
| 018 Default Initialization ↔ 011 Time Format Handling | 018 管 reset／斷電後之時間日期預設值；011 管格式（12H/24H）跨喚醒週期之保存與廣播。兩者皆涉「重開之後」，一者時間值、一者格式 |
| 014 GPS Date/Time Broadcast ↔ 008 Time Transmission / 017 Date Transmission | 014 驗 GPS 來源值送出之正確性（`$GPSDateTm*$` 訊號組內容，1.3.1.1.3 / 1.5.2.5）；008 擁有送出時機與觸發（1.3.1.1.4）、017 擁有日期通道（TELEMATIC_TIME_DATE + TLM LIDs）。**014 不重驗時機與通道；008/017 不重驗 GPS 來源值** |
| 011 Time Format Handling ↔ 008 Time Transmission | 011 驗 `$DateTmFormat$` 跨喚醒週期之保存與重送（物件 4813974，1.3.1.1.5.1）；008 擁有時間**值**之傳輸。**011 不驗時間值送出時機；008 不驗格式保存與重送** |

### Time and Date notes

1. **`Master Clock` 之章節分散是假陽性（R-TM15）**。五片在章節層無共通節，
   021 更孤立於 `1.5.2.2`；但描述之動詞受詞同型 —— maintain internal
   {clock / time signal / calendar / counters}，018 為該內部狀態之初始化。
   `1.5.2.2 Key Off Status` 是**條件章節**（何時）非能力章節（做什麼），
   spec 依敘述情境分章、Layer 2 依能力分組，兩者不同構是預期的。
   **判讀順序固定：先讀 leaf 描述之語意軸，再看章節；章節證據不得單獨
   推翻語意分組。** 同理 020 留在 `CAN Transmission`（描述明寫 via
   TIME_DATE messages），其與 021 共用 `1.5.2.2` 而分屬兩組是正確結果 ——
   時機相同、能力不同。

2. **`Fault Handling` 之章節證據無鑑別力，非「已檢驗通過」**。異常處理在
   本 spec 中散佈於各功能章節之內，不自成一節，故章節對本 Set 既不支持
   也不反對。成組依據為描述語意：010 收端（用最後有效值）、022 送端
   （發 SNA/預設值），同一能力之兩個方向。

3. **A-TM13 使兩片之章節證據殘缺**：005（`#SYS-RA`=2，可解 1）與
   002（=6，可解 4），缺口來自 `SYS-RA-221 → 6151328`、
   `SYS-RA-224 → 6151331` 兩個物件不在 CFTS015 SR26 基線內
   （全檔 `615\d{4}` 零命中；本 spec 物件 id 全為 `481xxxx` 區段）。
   **該兩筆之 `specification_reference` 無章節可寫，不得以鄰近章節填充**
   （§8.4.1）。framework 之定案改以語意軸為據，不依賴該殘缺章節證據。

4. **`1.5.3.*`（ETM）零命中**：21 個可達章節全落 `1.3.1.*` 與 `1.5.2.*`。
   與 A-TM09 之 48 筆 SYS2 FR 覆蓋缺口是否同源**尚未查證，不主張**。

5. **覆蓋稽核分母為 SYS2 之 Functional Requirement 全集 126，非 SWE leaf
   22（R-TM6）**。037 引用 78 筆 FR、48 筆無對應 leaf（61.9%）。
   48 筆之處置為**宣告**非補生成：TC 生成單位仍為 22 片 leaf，不得為缺口
   自行創設 leaf 或分解 SYS2 條文湊覆蓋（§8.2 / §8.4.1），缺口以 RD-1 上問。

### Batch plan（生成批次 ≠ Test Set）

| Batch | Leaves | n | 內容 | A-TM13 曝險 |
|---|---|---|---|---|
| **B1（pilot）** | 001, 003, 006, 007, 008, 010, 012 | 7 | **七個 Test Set 各取一片** | **無** |
| B2 | 002, 004, 005, 014, 016, 018, 021 | 7 | GPS Sync 與 Master Clock 之餘片 | **002 + 005 同批，marker 一併審** |
| B3 | 009, 011, 017, 019, 020 | 5 | CAN Transmission 與 Display 之餘片 | 無 |
| B4 | 013, 015, 022 | 3 | Manual Setting / Zone and DST / Fault Handling 之餘片 | 無 |

合計 22 = 全 leaf set。

**B1 之取樣依據（canon §1.2 分層取樣）**：七片各屬一個 Test Set，
故 pilot 一次檢驗全部七組之 Test Set 值、setup 型態與 UI 進入路徑，
而非只驗一組之內部一致性。**本 feature 無 done region，pilot 是唯一
的人工閘門**（Part VII 已明記第三層不存在），取樣覆蓋面因此比有
done region 之 feature 更重要。

**B2 之集中依據**：002 與 005 是 A-TM13 之全部受影響者，同批生成使其
Remarks 缺口標示與 reasoning 寫法可一次比對，避免兩批各寫一套。
SXM B11 先例（`(add)` leaves 集中一批一起讀）。

### Workbook sync

BLANK workbook、FILL 適用：Test Group `Time and Date` 與 Part VII 之
Test Set 值寫入每一生成列之 G / H 欄。

rev C 無 `Test Case Framework` 分頁（9 分頁；R-U10、FORMS.md 實測），
故逐列欄位即足，無分頁同步步驟。

**欄 D5（範圍 Scope）維持空白** —— 該欄語意為「本工作簿所依據之 037 報告
之文件識別」，值即該 037 檔名去副檔名（R-TM9-A2，據交付路徑三例實測：
`Home-HMI-V0.1` / `AppDrawer-HMI-V0.1` / `PersonalAccount-HMI-V0.1`）。
本 feature 之 037 身分未定（A-TM02a），故無值可填，非暫緩填。
**不得以 feature 名、spec 標題或類推形態組出字串填入。**

**寫回一律走 `backend/xlsx_surgical.py`**（R-G3 全域；母本 R 欄
design_method 下拉為 x14 擴充，openpyxl 存回即摧毀且損壞為選擇性）。
