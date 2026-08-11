# Test Case Framework — STLA FW036 (SWE.6)

Covers Test Groups **Media** (Part I, below), **Home** (Part II), **AMFM**
(Part III), and **SXM** (Part IV, end of file). The cross-cutting rulings in Part I
(orphan routing/attribution, lint vs traceability, assumption markers,
priority, anchors-as-style, blocked-parent proportion) apply to ALL Test
Groups.

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
