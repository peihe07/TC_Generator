# ANOMALIES — FW036 SXM

Register of ambiguities, spec gaps, and upstream inconsistencies.
Marker format: `[A-SXnn]`. PENDING entries block their batch until a Pei
ruling lands; RESOLVED entries record the ruling verbatim.
Registration is Tier 1 (record + propose); disposition is Tier 2.
File-supply gaps additionally get a row in `DATA_REQUESTS.md`.

---

## [A-SX01] The 11 "untagged" leaves are tagged — the id is not the last token — RESOLVED BY MEASUREMENT (2026-08-10)

- Phase 1 first reported 191 of 202 leaves as carrying a 7-digit id tail, with
  11 apparently untagged (080, 083, 110, 148, 149, 154–158, 182). **That was a
  measurement artefact**: the pattern was anchored to end-of-string, and these
  11 titles carry a trailing marker after the id.
- Re-measured with the anchor removed: **202 / 202 leaves carry exactly one
  7-digit id, and all 202 land on an exact CFTS024 clause anchor.** No leaf
  declares two different ids, and **no id is declared twice** — the corpus has
  no A-AM08-class duplicate pair.
- Consequence: the bracket map covers the whole leaf set, and the id-parsing
  pattern ported from AMFM must accept a trailing marker
  (`[({（]\s*(\d{7})\s*[)}）]` searched, not `…$` matched). Recorded because a
  future re-port of the AMFM regex would silently drop these 11 again.
- The marker itself is a separate question — see A-SX03.

## [A-SX02] Leaf 080 cites CFTS024 clauses in the unresolvable short-id scheme — RESOLVED: R11 cite-form adopted (2026-08-10)

- **Two leaves, not one** — the citation sweep over the built map reports
  `CFTS024-193/195/197` reached by **`SWE-RA-SXM-005` and `SWE-RA-SXM-080`**;
  080 was found by eye first, 005 only after the map existed.
- `SWE-RA-SXM-080` (`CFTS024-4872862`, §1.5.10.2 Play):
  "The Buffer playlist shall be browseable with the functions defined in
  **CFTS024-193, CFTS024-195 and CFTS024-197**.(4872862)(add)"
- Two further cited documents are **not in `inputs/`**, both surfaced by the
  same sweep: `CFTS019-494` / `CFTS019-496` (leaf **107**) and `CFTS020-138`
  (leaf **137**). CFTS019 (Audio Management) is already in `AMFMHMI/inputs/`
  and can be same-source copied if the disposition needs it; CFTS020 has not
  been located. Rows added to `DATA_REQUESTS.md` when a batch needs them.
- Those three ids are the same short-id cross-reference scheme AMFM registered
  as **A-AM15**: CFTS024 cites documents — and itself — with ids that appear
  in no supplied file, including its own 7-digit anchor set. `193`, `195` and
  `197` resolve to nothing in the CFTS024 docx.
- Same class, same disposition available: **R11 cite-form** — quote the token
  verbatim as an additional `specification_reference`, assert the borrowed
  outcome anchored to the citation, and do not test the referenced document's
  own rule surface. Whether R11 is adopted for SXM is a Phase 2 ruling; it is
  not automatically inherited.
- AMFM's resolver already emits these tokens (`data/cross_doc_citations.json`)
  and the same sweep will surface `CFTS024-193/195/197` once the SXM map is
  built with the citation pass enabled.

### Both cited documents are now in `inputs/` — and neither resolves the token (2026-08-10)

- **CFTS019** copied same-source from AMFM (`5a549719…`, byte-identical). Its
  clauses are 7-digit anchors (`486xxxx`); the cited `494` / `496` are not among
  them. AMFM reached the same conclusion for the same document under A-AM15.
- **CFTS020** supplied as `.doc` **and** `.reqifz`. The ReqIF was probed first
  because it is structured: 2,644 spec objects, **every one carrying a 7-digit
  `ReqIF.ForeignID`** (range `4819125–4822056`, disjoint from CFTS024's
  `4872359–4873959`), 2,170 of them with both an outline number and full text.
  So CFTS020 can be ingested as `id → (section, text)` directly, with no
  `.doc → .docx → python-docx` heading-anchor inference — a better path than
  the one AMFM had to use.
  **But the cited `138` appears nowhere**: not as `ReqIF.ForeignID`, not as
  `Source Id`, not as `ReqIF.Name`.
- **Consequence: the A-SX02 upgrade condition is NOT met.** Having the
  documents does not make the short ids resolvable — the scheme is foreign to
  the ReqIF export too, which is now the third independent format (docx, xlsx
  tables, ReqIF) in which these ids fail to appear. That strengthens the
  A-AM15 reading rather than weakening it: the short ids are not a lookup into
  any released artefact.
- Disposition unchanged: **R11 cite-form** — quote the token verbatim, anchor
  the borrowed outcome to it, test only the citing clause. (Adoption was ruled
  the same day — [PEI] entry below; this probe evaluates that ruling's
  **upgrade condition**: NOT met for CFTS020. CFTS019 / CFTS024 `.reqifz`
  probes remain open on the same condition.)

### Upgrade condition — CLOSED on all three groups (2026-08-10)

The remaining two exports were probed the same way. Identifiers in a ReqIF are
attributes, not text conventions, so this is the strongest form the check can
take:

| token group | searched in | result |
|---|---|---|
| `CFTS024-193 / -195 / -197` | CFTS024 ReqIF, **1,604** clauses | **not found** |
| `CFTS019-494 / -496` | CFTS019 ReqIF, **1,989** clauses | **not found** |
| `CFTS020-138` | CFTS020 ReqIF, **2,644** clauses | **not found** |

Fields searched whole: `ReqIF.ForeignID`, `Source Id`, `ReqIF.Name`,
`Reference in Same Module`, `Reference Specification`; then widened to every
attribute, matching the token as a standalone word. The only appearances of
`193` / `195` anywhere in CFTS024 are inside the text of clause `4872862` —
leaf 080's own clause, i.e. the citation itself. `197`, `494`, `496` and `138`
appear nowhere at all.

**The upgrade condition is not met for any group, and no further format
remains to test. The branch is closed; cite-form is final.**

Evidence line for **RD-1 S1**: four independent released formats — docx
paragraph anchors, the CIP xlsx worksheets, the ReqIF attribute sets, and the
037 report — agree that these ids index nothing. The scheme is therefore an
internal authoring key or a stale legacy numbering, not a reference a reader
can follow. Upstream should publish the mapping or restate the references
using the 7-digit clause ids every export already carries.
- **[PEI 2026-08-10: RESOLVED — R11 cite-form adopted for SXM.]** Scope: the
  three short-id groups — `CFTS024-193/195/197` (leaves 005, 080),
  `CFTS019-494/496` (leaf 107), `CFTS020-138` (leaf 137). Treatment per R11:
  quote the token verbatim as an additional `specification_reference`, assert
  the borrowed outcome anchored to the citation, do not test the referenced
  document's own rule surface. **Upgrade condition ruled with it**: if the
  `.reqifz` probe (CFTS020, and by extension CFTS019/024) yields a
  short-id → clause-anchor mapping, the affected citation upgrades from
  cite-form to a resolved reference and R11 becomes the fallback, not the
  disposition. Adoption is by this ruling, not inherited from AMFM.
- Upgrade-condition status (2026-08-10, post-probe): **CFTS020 — NOT met**
  (short id `138` absent from `ReqIF.ForeignID` / `Source Id` / `ReqIF.Name`
  across 2,644 objects; third independent format after docx and xlsx tables).
  Superseded the same day by the "CLOSED on all three groups" section above:
  CFTS019 and CFTS024 probed likewise — all three groups NOT met, no format
  left to test, branch closed, cite-form final.

### B2 checkpoint — first live exercise of the cite-form gates (2026-08-11)

The B1 pilot carried no cite-form leaf, so `cross-reference` and
`cross-reference-anchor` have never fired on real content: they were proven by
unit test only. **B2 (076–086) carries leaf 080**, the first R11 citation to
reach generation (`CFTS024-193/195/197`), and exercises both gates at once —
the token must be accepted under 080 and refused anywhere else, and the ER
must anchor to it.

Directed review at B2, in the same shape as the R10-2 checkpoint on A-SX08
(targeted, not the full ceremony): read 080's `specification_reference`
ordering (own clause first), its ER anchoring phrase, and confirm nothing in
the TC tests the cited document's own rule surface.

## [A-SX03] Eleven leaves carry an `(add)` marker and no Release Version or Status — RESOLVED (2026-08-10)

- The 11 leaves from A-SX01 end with a literal `(add)` after the id tail:
  080, 083, 110, 148, 149, 154, 155, 156, 157, 158, 182.
- The distinguishing evidence is not the marker but the columns beside it:

  | | `(add)` leaves | the other 191 |
  |---|---|---|
  | `Release Version` | **empty** ×11 | `1.00.00` ×191 |
  | `Requirement Status` | **empty** ×11 | `New` ×191 |

- So these rows entered the 037 outside the release process that stamped the
  rest of the sheet. `(add)` most plausibly means "added after the baseline
  export", but the 037 does not say so anywhere.
- Sections touched: §1.5.10.2 Play (1), §1.5.10.3 Rewind (1), §1.5.12.1 Browse
  Presets (1), §1.5.15 Enter or Item Select (2), §1.5.16 SiriusXM Traffic &
  Weather Now (**5**), §1.5.20 HU Satellite Audio Error Displays (1).
  Traffic & Weather is affected disproportionately — 5 of its leaves are
  `(add)` rows.
- Why it matters before generation, not after: if `(add)` marks provisional
  scope, these 11 leaves may be withdrawn or re-versioned upstream, and TCs
  written against them would be rework. **Proposed**: generate them normally
  and mark each affected TC's reasoning `[A-SX03]`, so a later withdrawal is a
  grep rather than an audit. RD-1 asks upstream what the marker means and why
  the two columns are blank.
- **[PEI 2026-08-10: RESOLVED as proposed.]** Generate normally; mark each
  affected TC's reasoning `[A-SX03]`; RD-1 class-2 item (requirement-set
  correction: release columns blank). Rationale ruled with it: the 037 is the
  ruled authority source — a row in it is a leaf, and the completeness
  invariant requires one row per leaf; a contrary upstream answer removes
  rows by grep, changing strings, not content.

## [A-SX04] The same requirement text appears twice in CFTS024, once per band chapter — REGISTERED, not a coverage conflict (2026-08-10)

- Phase 1 first read SXM leaves 110 / 148 / 149 as covering clauses AMFM had
  already shipped test cases for. **Measured, that is not what happens.**

  | SXM leaf | clause | section | AMFM leaf | clause | section | text similarity |
  |---|---|---|---|---|---|---|
  | 110 | `4872901` | §1.5.12.1 Browse Presets | 023 | `4872430` | §1.3.3.1 Browse Category- Presets | **1.000** |
  | 148 | `4872952` | §1.5.15 Enter or Item Select | 047 | `4872506` | §1.3.12 Enter or Item Select | **1.000** |
  | 149 | `4872954` | §1.5.15 Enter or Item Select | 049 | `4872508` | §1.3.12 Enter or Item Select | **1.000** |

- **Different clause ids in different chapters, word-for-word identical text.**
  CFTS024 states these requirements once in the analog tuner chapter and again
  in the satellite chapter. Each feature cites its own chapter's clause, so
  neither deliverable claims coverage of the other's requirement and there is
  no scope conflict to rule on.
- Disposition — **each feature covers its own clause** (ruled, see below): SXM
  generates 110/148/149 against `4872901` / `4872952` / `4872954` in SAT
  context (SAT preset list, SAT genre list), AMFM keeps 023/047/049 as
  delivered. Nothing is withdrawn, nothing is cross-cited.
- **Pre-pilot re-check condition**: the disposition rests on the two clauses
  being identical *today*. Before the pilot batch, re-run the text comparison
  for every SXM leaf whose clause text matches an AMFM clause at ≥0.95 — not
  just these three — and list any pair where the SAT wording has diverged. A
  divergence means the SAT clause carries a behaviour the analog one does not,
  and the TC must follow the SAT clause (§8.6), not AMFM's precedent.
- Upstream item for RD-1: duplicated requirement text under two ids is a
  maintenance hazard — an amendment to one chapter silently leaves the other
  stale.
- **[PEI 2026-08-10: RESOLVED as registered.]** Confirmed: generate all three
  normally, no cross-citation. Remarks format ruled: each of the three rows
  carries `Analog-chapter twin: CFTS024-<analog id> (covered in the AM/FM
  deliverable)` — the analog **clause id**, never AMFM TC ids (TC ids are
  assigned at write-back and shift on any AMFM regen; clause ids are stable
  and self-evident inside CFTS024; both forms pass AMFM's remarks-internal
  gate, the choice is stability). The ≥0.95 comparison output doubles as the
  "CFTS024 cross-chapter twin list" feeding the merged RD-1 FYI. An earlier
  DECISIONS §4 paragraph reading this disposition as "citation rows" was a
  label misread and is voided there.
- **Pre-pilot re-check executed (2026-08-10): condition PASSED, disposition
  unchanged.** All 202 leaves compared; **11 pairs ≥ 0.95**: 9 word-for-word
  identical (1.000) — the known 110/148/149 plus 037↔036 (Preset Save),
  108↔022 (Browse Presets short press), 132↔040 (Scroll), 140/142/143↔
  043/044/045 (Page Up/Down) — and 2 divergent: 020↔4872780/011↔4872413
  (0.9595) and 024↔4872786/026↔4872442 (0.9676), both **band-vocabulary
  adaptation only** (Tuner → Satellite Audio; executed → initiated); no SAT
  clause carries behaviour its analog twin lacks. Per-pair list:
  `docs/twin-list-sxm.md`; raw `data/twin_pairs.json` (re-run before pilot).
- **Extension (chat tier, 2026-08-10, override open)**: the ruled mirror
  Remarks format applies to ALL 11 twin rows — SXM 020, 024, 037, 108, 110,
  132, 140, 142, 143, 148, 149 — each citing its own analog clause id, same
  wording as ruled above. The two vocabulary-adapted pairs follow §8.6 SAT
  wording in TC text (which is what would be written anyway).

## [A-SX05] First feature on form revision C; `Estimated Test Time` has no fill policy — RESOLVED (2026-08-10, DECISIONS §2)

- The scaffold workbook is a copy of the blank form (SHA256 `cd876c20…`),
  which is **revision C**: it inserts `Estimated Test Time (mins)` at **Q**,
  shifting design_method → R, functional_safety → S, the vehicle block →
  T..Z, author → **AA**, remarks → **AH**. Its data sheet is also named
  `Test Case Specification 測試用例規範`, without the `&Result` suffix every
  instance uses.
- **Every FW036 instance shipped so far is revision A/B** — Home, AMFM, and
  the 18 other 036 workbooks found in the project tree. No feature has been
  generated on revision C.
- `recon.py` resolved the column map from header text independently and agreed
  with `feature.yaml` on all 15 fields (zero conflicts), so the layout itself
  is not in doubt. What is undecided is content policy for the new column:
  **no rule says whether `Estimated Test Time` is filled, and by whom.**
  Leaving it blank on 202 rows is visible to the customer; filling it requires
  an estimation basis this pipeline does not have.
- Proposed: leave blank, state it in the dry-run summary as a named
  blank-by-decision column (the AMFM `UNRULED_BLANK` mechanism), and ask
  upstream in RD-1 whether the field is expected from the test author.
- **[PEI 2026-08-10: RESOLVED per DECISIONS §2 ruling.]** Ship on revision C;
  `Estimated Test Time` left blank at generation, named in the delivery cover
  and dry-run summary as blank-by-decision, RD-1 question on the expected
  fill. Estimating without a source is §8.4-adjacent fabrication and `NA`
  reads as refusal; write-back can fill corpus-wide later if the answer
  defines a rubric.

## [A-SX06] "Same version label, different file" — a corpus-wide identification hazard — REGISTERED, RD-1 merge item

- Two independent instances found while assembling SXM inputs:

  | File | Copies | Distinct SHA256 |
  |---|---|---|
  | `SR24 R1 Market Configuration Table **v1.6**.xlsx` | 4 releases (25PI3.5 / 25PI4.5 / 26PI1.5 / 26PI2.5) | **4** — `ae4cf0b9…` / `9efae74f…` / `2e66a6d9…` / `7e865d55…` |
  | `SYS3_SXM_…SYSAD` | 3 dates (20260323 / 20260511 / v0.2_20260629) | 3 — `52d7528f…` / `145ecac1…` / `9acb9eb2…`; sizes 899,697 / 1,023,382 / 1,202,688 bytes |

- The Market Configuration Table is the sharper case: **the version label is
  identical across all four and the content is not**. A pipeline that binds a
  spec value by filename is therefore binding to nothing.
- AMFM already carries the same finding for `CIP_Radio_Tables` across four
  releases (`DATA_REQUESTS` row 1). Three instances make it a class, not a
  coincidence.
- Local policy already applied, no ruling needed to keep working: every
  cross-feature copy is hash-verified on both sides and the hash is recorded
  in `DATA_REQUESTS.md`; the release each file belongs to is stated next to it.
- RD-1 (merged item across AMFM and SXM): ask upstream to version reference
  workbooks by content, or at minimum to change the version label whenever the
  content changes.

## [A-SX07] Leaf 154's title and its declared id describe different clauses — RESOLVED: reading (a) (2026-08-10)

Found by the ported `verify_ids` check on the first map build, not by eye.

| | leaf 153 | leaf 154 |
|---|---|---|
| declared id | `4872961` | `4872962` |
| agreement with the declared clause | — (not flagged) | **0.534** |
| best-matching clause | — | **`4872961` at 0.994** |

- `4872961` (§1.5.16): "…allow selection of a traffic/weather channel **when
  'Jump' button is activated under the 'SiriusXM Setup' feature in 'Settings'
  menu**…"
- `4872962` (§1.5.16): "…allow selection of a traffic/weather channel **within
  the list when Traffic & Weather Category is initiated under SiriusXM Browse
  function**."
- Leaf 154's **title reproduces 4872961's text** — i.e. 153's clause — while
  its **id points at 4872962**, whose behaviour (entry via Browse, not via the
  Jump button) the title never mentions.
- Two readings, and they lead to different test cases:
  (a) **the id is right, the title was copy-pasted from 153.** Under §8.6 the
      clause text is the authority for wording, so 154 covers the Browse entry
      path and the 037 title is the defect. This is the reading the evidence
      favours: 4872962 exists, is unclaimed by any other leaf, and sits in the
      same section.
  (b) the title is right and the id is a copy error, making 154 a duplicate of
      153 — the A-AM08 shape, which AMFM resolved as R9.
- **Not corrected here.** The AMFM precedent (R7-Q4 / R9) is that a declared-id
  correction is a ruling with evidence, implemented as a checked
  `stla_id_overrides` entry — never a pipeline guess. If Pei takes reading (a),
  no override is needed at all: the map already resolves 154 to 4872962 and
  only the TC's Test Item wording follows the clause rather than the title.
- No other suspect in the corpus: 202 leaves, 1 finding, and no id declared
  twice.
- **[PEI 2026-08-10: RESOLVED — reading (a).]** The id is authoritative; the
  title is a copy-paste defect from 153. Basis: §8.6 (source clause text wins)
  plus the three evidence points (4872962 exists, is unclaimed, same
  section). Implementation: no `stla_id_overrides` entry needed — the map
  already resolves 154 → 4872962; the TC's content and Test Item follow the
  4872962 clause text (Browse entry path), the 037 title is treated as the
  defect; reasoning carries `[A-SX07]`. RD-1 class-2 item (title/id mismatch,
  evidence attached). If upstream answers (b), this converts to an R9-shape
  id correction and 154 becomes a duplicate of 153 — single-row impact.
- Note: 154 is also on the A-SX03 `(add)` list, so its reasoning stacks
  `[A-SX03]` + `[A-SX07]` + the §8.6 wording note — ruled into the pilot
  batch (DECISIONS §7 amendment) to validate the marker mechanism on the
  most complex leaf first.

## [A-SX08] 38 CFTS024 §1.5.x clauses reach no leaf — R10-2 ADOPTED (registered and ruled 2026-08-10)

- The 037 allocates 202 leaves against CFTS024 §1.5.x, leaving **38 clauses
  (32 SFR, 6 other) unallocated** — `data/unallocated_clauses.json`. Unlike
  AMFM's distribution, several gaps are **whole sections with zero leaves**:
  §1.5.8, §1.5.12.1.5+, §1.5.18, §1.5.21.1, §1.5.21.2.1.
- **[PEI 2026-08-10: R10-2 ADOPTED for SXM]** (by ruling, not inherited).
  Absorption is legitimate iff (a) same spec section AND (b) the clause
  elaborates the leaf's cited clause. On absorption: `[A-SX08]` marker in
  assumptions AND the absorbed id in `specification_reference` (multi-cite).
  Failing the test → coverage hole in reasoning + RD-1.
- Whole-section gaps cannot pass condition (a) — they have no leaf to
  elaborate. They go to RD-1 (Q-SX) as an allocation-policy question in the
  Q-AM3 wording pattern (ask the policy, do not assert systematic omission),
  and are never silently absorbed.
- Batch-time consequence: each batch's context carries its sections'
  unallocated clauses with scope tags; the decision test runs per clause at
  generation, per the AMFM precedent (R10-2 earned its keep in Seek — the
  same load check applies here at §1.5.1/§1.5.2).
- Checkpoint (chat tier, 2026-08-10): B1 pilot carried NO absorption load —
  §1.5.10/.1/.4 have zero unallocated clauses; the only 3 in-batch (via 154,
  §1.5.16) elaborate nothing and were correctly not absorbed. The `[A-SX08]`
  marker path and the absorption-cite lint gate are therefore UNEXERCISED at
  pilot gate. Ruled fallback: a targeted absorption-only mini-review runs
  after B3 (Seek) and again at B5 (§1.5, 14 clauses — heaviest load),
  scoped to absorption decisions and the gate's first firing; not a full
  pilot ceremony.

## Assumption markers

None registered. Inline format in generated JSON reasoning/assumptions:
`[ASSUMPTION A-SXnn]` or `[A-SXnn]`.


## [A-SX09] Upstream spelling errors are quoted verbatim in Test Item — REGISTERED, RD-1 FYI (2026-08-11)

Pilot review asked whether `Fast Fowarding` in leaf 090's Test Item was a
transcription slip. It is not: the ReqIF export of clause `4872874` carries
that spelling, so the Test Item is a faithful quotation and stays as it is.

Checking the corpus rather than the one clause turns a typo into a class:

| spelling | clauses affected |
|---|---|
| `recieve` (for *receive*) | **36** |
| `continously` (for *continuously*) | **13** |
| `Fowarding` | 1 (`4872874`) |
| `taffic` | 1 (`4872966`, leaf 157) |

AMFM already quotes `recieve` and `continously` verbatim in its delivered test
cases for the same reason — Test Item quotes requirement text (profile §3.1).

Disposition: **quote verbatim, never silently correct.** A corrected quotation
stops matching the source and breaks the reviewer's ability to diff a Test Item
against its clause. Reported to upstream as one RD-1 FYI covering the class,
not four separate items.


## [A-SX10] Leaves 082 and 083 carry identical 037 titles for different clauses — §8.6 applied (2026-08-11)

Found while building the B2 context; the same shape as A-SX07, second instance.

| leaf | declared clause | 037 title says | clause says | agreement |
|---|---|---|---|---|
| 082 | `4872865` | "beginning of the **previous** song" | "beginning of the **current** song" | 0.931 |
| 083 | `4872866` | "beginning of the **previous** song" | "beginning of the **previous** song" | 0.976 |

- **The two titles are byte-identical**; only the id tail and 083's `(add)`
  marker differ. Read from the 037 alone the pair looks like a duplication.
  Read against the clauses it is not: `4872865` is the jump to the start of
  the song currently playing, `4872866` the jump to the song before it.
- 082's title is a copy of 083's. Unlike A-SX07 this needs no ruling on which
  side is right — the declared id is not in question, only the wording, which
  is the plain §8.6 case: **the clause is authority for wording, the title for
  scope.** 082 therefore tests the CURRENT song and 083 the PREVIOUS song.
- Registered rather than merely handled because it changes what 082 verifies,
  and because two instances make the copy-paste a pattern in this 037 rather
  than an isolated slip. Goes to RD-1 with A-SX07 as one requirement-set
  correction item.
- No `[A-SX10]` marker is emitted in generation: the §8.6 wording note the
  pipeline already attaches to 082 records the divergence at the row level.


## [A-SX11] The cited SEEK worksheet classifies Fast Seek SAT, not plain Seek SAT — PENDING

Leaves 009 / 012 / 017 / 020 point at `'CIP_Radio_Tables*'`,
`'SEEK Cancel_Stop Transitions'` for the events that cancel or stop a SAT
seek. Read against the worksheet actually supplied:

| worksheet row | event classifications |
|---|---|
| `SEEK SAT Audio (US Market)` | **`N/A` on all 59 event columns** (only the four VP columns carry `X`) |
| `Fast SEEK SAT Audio (US Market)` | fully classified — 9 `Cancel Seek`, 5 `Stop Seek`, 3 `Continue Seek - No Impact`, plus 20 qualified variants |

So the row that matches the citing clauses' state — the plain Seek Up / Seek
Down state — answers `N/A` for every event, and the classifications the
clauses send the reader to find exist only for the **fast** seek state.

- 012 and 020 are the sharp case: their entire testable content is the
  pointer. 009 and 017 also state their own cancel behaviour in prose, so they
  remain testable from the clause alone.
- Two readings, and the corpus does not settle it: (a) a plain SAT seek is
  channel-indexed and completes with no interruptible window, so `N/A` is
  correct and the classifications belong to fast seek by design; (b) the plain
  row is unfilled. **Asserting (a) would be an inference about the design
  (§8.4.1), so it is not asserted.**
- Generated disposition: 012 and 020 exercise the stop events in the state the
  worksheet does classify, and say so in reasoning. Every event named in their
  Input Test Data is quoted from the `Fast SEEK SAT Audio` row, never from the
  AM/FM row AMFM used.
- RD-1: ask which row governs a plain SAT seek, and whether `N/A` there means
  "cannot be interrupted" or "not yet specified".


## [A-SX12] The ICS knob tune clauses specify a rate with no mapping, and say "frequency" for a channel-indexed source — REGISTERED (2026-08-11)

Leaves 024 and 028 (`4872786` / `4872792`, §1.5.3 / §1.5.4) are the SAT
counterparts of AMFM's ICS knob clauses. Two upstream gaps, both visible only
against the clause text:

1. **The rate has no defined mapping.** The clause says the HU "shall
   increment the tuned frequency **based on the rate** received in the
   `$ICS_KNOB2_VAL$` signal value", with `$ICS_KNOB2_VAL$ = [1 to 63]`, and
   nowhere states what a given value maps to in channels. AMFM registered the
   same gap as **A-AM11** and its TCs assert direction and monotonicity rather
   than a channel count. SXM does the same: the ER states the tuning moves in
   the signalled direction and that a larger `$ICS_KNOB2_VAL$` advances
   further, never a specific number of channels (§8.4.1).
2. **"tuned frequency" on a channel-indexed source.** SAT Audio tunes
   channels, not frequencies; the wording is carried over from the analog
   chapter, where its twin (`4872442`, AMFM leaf 026) says the same thing
   legitimately. The observable under test is therefore the tuned **channel**.
   Recorded rather than corrected — the Test Item quotes the clause verbatim
   (profile §3.1), and only the ER speaks of channels.

Both go to RD-1 with A-SX09 as wording/definition items. No generation is
blocked: the suppression condition the same clauses carry (the function is not
executed while a scroll/list display is up) is fully specified and is tested.


## [A-SX13] The cited "Pre-defined Presets Algorithm" is an empty worksheet — PENDING

Leaf 036 (`4872804`) is a pointer and nothing else: *HU shall implement the
pre-defined presets for SDAR mode per "Pre-defined Presets Algorithm" defined
in 'CIP_ Radio_Tables*'.* Traced through the supplied workbook:

| step | what is there |
|---|---|
| `Preset Defaults- VP3&4`, row 13 | "See the corresponding SDARS Predefined Presets worksheet for X65 Sirius/XM chipsets" |
| ` Predefined Presets -X65 chip  ` | **one cell**: "Note: This applies to all HU (VP1, VP2, VP3, VP4) equipped with X65 Sirius/XM chipset." No table, no algorithm. |
| `History`, rows 4 and 8 | records that the worksheet was *added* for the X65 chipset and that "SXM predefined default tables" were revised |

So the forwarding chain is intact and terminates in a worksheet with no
content. The analog `Preset Defaults- R1` sheet is populated (AM 531 kHz,
FM 87.5 MHz and so on); the SDAR equivalent is not.

- Different failure from A-SX11: there the cited row exists and answers `N/A`;
  here the cited worksheet exists and is empty.
- Generated disposition: the TC verifies what the clause states and the file
  can support — that presets for SDAR mode are pre-populated without the user
  having stored anything — and **does not assert which channels occupy which
  preset numbers**, because that is exactly what the missing algorithm would
  define (§8.4.1). No BLOCKED row: the presence of pre-defined presets is
  observable even when their content is not specified here.
- `DATA_REQUESTS` row added. RD-1: supply the SDARS predefined preset table,
  or confirm the algorithm lives in a document outside the CIP workbook.

## [A-SX14] §1.5's 14 unallocated clauses are supplier-conformance requirements with no leaf — R10-2 test run, all declined (2026-08-11)

The first batch to carry absorption material (B1-B4 had none). The R10-2
decision test was run per clause, as the A-SX08 checkpoint requires.

Condition (a), same spec section: **passes for all 14** — every one is in
§1.5, the section leaf 001 cites.
Condition (b), elaborates the leaf's cited clause: **fails for all 14.**
Leaf 001's clause (`4872752`) is the Channel Art image display. The 14 are:

| group | clauses | what they bind |
|---|---|---|
| Type approval | `4872753`, `4872754` | testing per RX-9835-0011 / SX-9835-0051 |
| Interface and protocol conformance | `4872755`–`4872759`, `4872761` | X65 receiver PDS, EMMA, SXi message spec, SXi UART link layer, antenna/RF, extended metadata |
| Product-level conformance | `4872760`, `4872762` | 360L UX, MFFR, Audio Service UI requirements |
| Album art conformance | `4872763` | four SX album-art documents |
| Configuration / defaults | `4872750`, `4872751` | SXM display and functionality if the chip is equipped; US as the default region without navigation |
| Section preamble | `4872749` | Description artifact |

None elaborates the Channel Art clause. `4872763` is the closest — it is also
about imagery — but it binds **album** art to four supplier specifications,
which is a parallel conformance requirement, not an elaboration of the channel
art display. Absorbing it would claim coverage of documents the corpus does
not hold.

**All 14 recorded as a coverage hole, none absorbed.** Two observations for
RD-1 (Q-SX, allocation-policy wording, not an assertion of omission):

1. The block is coherent: §1.5 allocates one leaf, for Channel Art, and none
   for the eleven supplier-conformance requirements around it. Whether those
   are meant to reach SWE.6 at all is the policy question — they bind the
   implementation to external specifications rather than describing HU
   behaviour, and the corpus holds none of those specifications.
2. **`4872750` is the exception worth naming**: "HU shall provide SXM related
   display and functionality if SXM chip is equipped" is an observable
   configuration gate, the same shape as AMFM's `$AM_Presence$` leaves, and it
   has no leaf. If any of the 14 should have one, it is this.

## [A-SX19] Five clauses carry a VR trigger path their 037 titles also declare — RESOLVED: R8-equivalent adopted, premise amended (2026-08-11)

- Five leaves' cited clauses include a Voice Recognition trigger path
  ("or a VR Command" class wording): leaves 002, 003, 006, 014, 030.
- **Premise amended 2026-08-11 (measured, then re-ruled).** The entry was
  filed on the AMFM A-AM09 premise — titles omit the VR wording the clause
  carries. Measurement over the five leaves contradicts it: **all five 037
  titles contain `or a VR Command` verbatim** (002/003/006/014 as
  `... Steering Wheel Buttons or a VR Command`, 030 as `using the HU HMI or a
  VR Command`). SXM does not continue the A-AM09 pattern; it inverts it — the
  requirement document itself declares the VR scope.
- The measured title/clause divergence is a different defect: **the 037 titles
  truncate at the end of the first sentence**, dropping the second sentence's
  behaviour (state entry, adjacent-channel move, wrap-around). That affects
  more leaves than these five and is asked as Q-SX3 question 3.
- **[PEI 2026-08-11: R8-equivalent ADOPTED for SXM — by ruling, not
  inherited.]** The VR trigger path is excluded from this workbook's scope
  and delegated to the CFTS028 (Voice Recognition) delivery; TCs verify
  touch / hard-key entry paths only. Each affected TC's reasoning notes the
  exclusion citing this ruling; the §8.6 wording note applies (clause states
  it, title omits it).
- Escape hatch as originally ruled — a leaf whose 037 title states VR returns
  for individual ruling — is engaged by the measurement on all five leaves, so
  applied literally it would void the exclusion entirely. **Held, not fired:**
  the exclusion stands as ruled pending the Q-SX3 answer, because the hatch
  exists to catch a title that claims a scope no one else verifies, and
  whether CFTS028 verifies it is exactly what Q-SX3 asks. If CFTS028 does not
  cover these five, the hatch fires and the five leaves return individually.
- RD-1 (Q-SX3): **not an S3 evidence line.** S3 is the "titles systematically
  omit VR wording" class and SXM is counter-evidence to it, so the line is
  filed as its own finding with the measured direction — the 037 declares the
  VR scope and the exclusion removes from test a path the requirement document
  states.
- Implementation: reasoning annotation on the five existing TCs —
  field-level, no regeneration, does not block any batch.


## [A-SX15] Two sections state the favorites delete options, and §1.5.9.2's title does not match its content — REGISTERED (2026-08-11)

Two findings from B7, both about §1.5.9.2.

**1. `4872834` (leaf 055) restates `4872827` (leaf 049).** 049, in §1.5.9.1,
says the 'Fav' button displays the favorites list and that both an individual
delete and a 'Remove All' are allowed. 055, in §1.5.9.2, says the HU provides
an option to delete individual entries and a "delete all" function for the
list. The delete capability is stated twice, in two sections, under two ids.

Unlike A-SX04 this is not a cross-chapter twin: both clauses are SXM's own
§1.5.9.x, so both leaves belong to this delivery and §8.2.2 forbids TC-side
consolidation. Carve applied: **049 owns the 'Fav' button entry path** (its
clause ties the list display to that button), **055 owns the delete options as
a capability of the list** however it was opened. Each cites its own clause.
Reported so a reviewer comparing the two rows sees a ruled carve rather than a
duplication that slipped through.

**2. The section heading is `Activation`; none of its eight clauses is about
activation.** §1.5.9.2 holds the FAV ON AIR background search, match handling,
the on-air list and its 10-second timeout — a continuation of §1.5.9.1
Favorites. The Test Set name in framework Part IV (`Activation`) inherits the
heading, so the workbook's column H will read `Activation` for eight rows
whose subject is favorites alerts.

No local action: Layer 2 names come from the ruled Part IV table and the
heading is the spec's own. Raised for RD-1 — if the heading is a copy error,
the Test Set name should follow the correction rather than the other way round.


## [A-SX16] Two clauses in one section state the All Channels browse list with different field sets — REGISTERED (2026-08-11)

`4872892` (leaf 104) and `4872896` (leaf 106) are both in §1.5.12, both
triggered by "When All Channels browse function is selected", and both state
what the HU displays:

- `4872892`: station number, **long form** station name, **and the genre**
- `4872896`: station number and station name

The second is the first minus the genre, and differs on the name form. Two ids,
one section, one trigger — a reviewer reading the workbook will see two rows
that look like the same test.

Note this is not the A-SX15 shape: there the two clauses were in different
sections. Here they are siblings, which makes a "which section owns it" carve
unavailable.

Carve applied, by the only textual difference that carries a testable
distinction: **104 owns the per-row field content** — that each row shows the
number, the long form name and the genre, tested on a station whose long and
short name forms differ. **106 owns list completeness** — that every available
station appears, tested by comparing the scrolled list against the station set
obtained independently, which 104's field test does not assert.

§8.2.2 forbids consolidating them on the TC side, so the carve is the available
move; it is not a claim that the two clauses were meant to differ this way.

**For RD-1:** if `4872896` is a stale earlier draft of `4872892`, it should be
withdrawn upstream rather than carved. The name form is the substantive
question — one clause says the long form name is displayed and the other says
the station name, and only the first is currently being verified as long form.


## [A-SX17] Paired browse categories carry word-for-word identical requirement text — RESOLVED: carve as registered (2026-08-11)

Three pairs in the browse sections, each pair two clause ids in the same
section whose bodies are identical or differ only in the category name:

| pair | ids | leaves | body |
|---|---|---|---|
| Add Teams / Select Teams | 4872913 / 4872914 | 115 / 116 | **word for word identical** |
| Edit Teams / Edit Selection | 4872915 / 4872916 | 117 / 118 | **word for word identical** |
| Edit Favorites / Edit FAVs | 4872927 / 4872930 | 126 / 129 | same two delete options, 4872930 additionally names the 'Delete All' function |

This is the A-SX16 shape repeated: siblings in one section, so no
section-ownership carve is available. But it is weaker than A-SX16, because
there the two clauses at least differed on content (genre, name form). Here
the *only* difference in the first two pairs is the name of the category the
user selects.

Carve applied: **each TC enters through its own category name**, which is the
sole textual difference and therefore the only distinction that can be tested.
Everything downstream of that entry is necessarily the same, because the
clauses say the same thing.

What this buys: if Add Teams and Select Teams turn out to be two entry points
into one screen, both TCs pass and the execution record shows two rows that
did the same thing from two doors — which is the evidence a reviewer needs.
Consolidating them on the TC side (§8.2.2 forbids it anyway) would have hidden
exactly that.

**For RD-1:** are these genuinely four categories, or two categories that were
renamed and both drafts survived? The delivery currently promises to test four
Game Zone edit/add paths. If two of them do not exist in the HMI, two TCs will
fail for a reason that is a document defect, not a software defect.

- **[PEI 2026-08-11: RESOLVED as registered — 1 照簽.]** Carve on the sole
  textual difference stands (each TC enters through its own category name).
  Remarks format ruled: all six rows (115/116, 117/118, 126/129) carry
  `Same-text sibling: CFTS024-<paired id> (category-name entry is the
  distinguishing token)` — paired clause id, stable and self-evident inside
  CFTS024, same rationale as the A-SX04 twin Remarks. RD-1 question as
  registered (four categories, or two renamed with both drafts surviving).

## [A-SX18] `4872919` restates leaf 120's score-update branch and contradicts it — RESOLVED: 4872918 governs (2026-08-11)

`4872919` (All Score updates, §1.5.12.1.2, unallocated) and leaf 120's clause
`4872918` both describe the single-match score-update flow, and they disagree
on what the resulting screen lists:

- `4872918` (leaf 120): the On Air screen lists **all the games that have score
  updates**
- `4872919` (unallocated): the On Air screen lists **all the games that are
  starting as well as the score updates**

R10-2 condition (a) holds — same section as leaf 120. Condition (b) does not,
and for an unusual reason: the two are not merely hard to observe together,
they cannot both be satisfied by one screen. Absorbing `4872919` into leaf 120
would require the ER to assert two different list contents at once.

Leaf 120's TC-02 therefore tests `4872918` as written — games with score
updates, and explicitly asserts a game without a score update is not listed,
which is the assertion `4872919` would forbid.

**For RD-1:** which listing is correct? The two clauses are 1 apart in id and
adjacent in the document, so one is likely a superseded draft of the other.
Until that is answered, TC-02's negative assertion is the open risk: if
`4872919` is the live requirement, that assertion is wrong.

- **[PEI 2026-08-11: RESOLVED — 2 照簽.]** TC-02 keeps the negative
  assertion per the allocated clause `4872918` (a game without a score update
  is not listed) — §8.6 authority chain: the 037 allocates 4872918, its text
  governs. The R10-2 condition-(b) failure reading is confirmed (one screen
  cannot satisfy both listings). `[A-SX18]` marker on leaf 120's affected
  TC; RD-1 class-2 **expedited** (adjacent ids, likely superseded draft —
  ask which is live). If upstream answers `4872919`, grep the marker and
  amend the one assertion line. The weakened positive-only alternative was
  considered and rejected — it opens a false-pass hole (a list-everything
  screen would pass).


## [A-SX20] "Capability clause plus mechanics clause" is a document-wide pattern, not three incidents — RULED (2026-08-11)

B10 produced three more same-section overlapping pairs, which makes this the
fourth batch running to hit the shape. Rolling it up rather than filing a
fourth incident.

| section | pair | leaves | how they overlap |
|---|---|---|---|
| 1.5.13 | 4872934 / 4872936 | 132 / 134 | one names the Scroll Up/Down function and the one-row step, the other says line-by-line scrolling is allowed while a List is displayed |
| 1.5.14 | 4872943 / 4872944 | 140 / 141 | same shape, page granularity |
| 1.5.15 | 4872951 / 4872956 (and 4872950) | 147 / 150 (146) | one says items may be selected, one says selecting tunes to the associated channel, one says selecting a Channel tunes and plays |

Together with the already-registered instances:

| entry | pairs | shape |
|---|---|---|
| A-SX15 | 1 | across sections (§1.5.9.1 / §1.5.9.2) |
| A-SX16 | 1 | same section, one field set a subset of the other |
| A-SX17 | 3 | same section, bodies identical but for a category name |
| A-SX20 | 3 | same section, capability clause beside mechanics clause |

**Eight pairs across five sections.** The recurring authoring habit is a broad
capability sentence ("the HU shall allow X") filed as its own requirement
alongside the specific clause that says how X behaves. §8.2.2 forbids
consolidating them on the TC side, so every instance costs a carve.

Carve rule applied consistently in B10, and worth ruling as the standing one:
**the capability clause is tested for reach** — it is exercised on a second,
structurally different instance (another kind of list, an item that is not a
channel) to show the capability is not the specific clause's special case —
**and the mechanics clause is tested for its stated detail** (the one-row step,
the full-page replacement, the tune-and-play outcome). That gives each row a
distinct failing condition, which is what makes them two tests rather than one
test written twice.

**For RD-1:** this is a single question with eight instances, not eight
questions. Is the capability sentence intended as a separate verifiable
requirement, or is it section-introductory prose that was allocated an id? If
the latter, eight delivered rows are testing prose.

**RULED (Pei, 2026-08-11) — 照簽, both halves.**

1. **The carve is standing.** Capability clause tested for *reach* (exercised
   on a second, structurally different instance); mechanics clause tested for
   its *stated detail*. Applies to every future instance without re-asking.
2. **Consolidation is rolling.** A new instance of this shape amends this
   entry's table; it does not open a new anomaly id. The RD-1 stays one
   question with N instances.

Escape hatch (i) survives the ruling: an instance where the two clauses
*contradict* rather than overlap is not this shape and returns to chat.
A-SX23 fired it the same day, which is the evidence the hatch is load-bearing
rather than decorative.

No regeneration follows from this ruling — B10's rows were already carved this
way, and the ruling is what makes that the standing rule rather than a
batch-local choice.

## [A-SX21] Absorption and cite-form collide: an absorbed clause's citations have no path — RULED (2026-08-11)

Found by the `cross-reference` gate during B10 generation, not by review.

Leaf 148's clause (`4872952`) says only that the HU enters the Genre Seek
state. The behaviour of that state is in `4872953`, unallocated, same section,
which was absorbed under R10-2. But `4872953` defines the behaviour *by
reference*: "shall behave in the same manner as the Seek Up function described
in Section CFTS024-165, with the exception that only stations matching the
selected Genre shall be considered valid." Same for `4872955` → `CFTS024-177`
on leaf 149.

Writing `CFTS024-165` into the TC's specification_reference failed the gate:
R11's cite-form path is keyed to the tokens **the leaf's own clause writes**,
and this leaf's clause writes none. The gate is right — allowing it would let
any absorption drag arbitrary citations into a leaf's reference list, and R11's
whole point is that a citation is licensed by the citing clause.

Resolved locally by narrowing the ER to the absorbed clause's own contribution:
the two TCs assert that every station the seek or scan lands on belongs to the
selected genre, and do **not** assert that it reaches every station of that
genre — the exhaustiveness is Seek Up's behaviour, reachable only through
`CFTS024-165`.

What that leaves untested: nothing that was previously covered — before the
absorption these two clauses had no test at all, and the genre restriction is
now verified where it was not. But the composition is unruled.

**For chat:** when R10-2 absorbs a clause that itself cites, does the citation
travel with it? Two readings, and the choice is not obvious:
- **It travels.** The absorbed clause is now part of this leaf's scope, so its
  citations are this leaf's citations. Lets the ER anchor the base behaviour.
- **It does not.** R11 licenses a citation by the *allocated* clause writing
  it; absorption is a coverage device and should not extend citation authority.
  This is what the gate currently enforces, and what B10 shipped.

Two leaves are affected today (148, 149). No batch is blocked either way — a
later ruling for "it travels" is an ER line and a reference field on two rows.

**RULED (Pei, 2026-08-11) — 照簽: the citation travels.** An absorbed clause
brings its citations into the absorbing leaf's reference list, subject to the
necessity threshold (DECISIONS Amendment 7): the absorbed clause must itself
write the token, and the token must be necessary to state the behaviour being
verified. The gate reads the absorbed clause's text to license it, so the
three-hop chain leaf → absorbed clause → citation stays checkable.

**Already implemented — no rows change now.** The entry above describes the
B10 state. B11 (`55044b0`) applied the ruled reading ahead of the ruling, when
Amendment 7 fixed the threshold, and B14 left it in place. Verified against the
shipped files rather than assumed:

| | B10 (`1ef267d`) | now |
|---|---|---|
| 148 reference | `CFTS024-4872952; CFTS024-4872953` | `…; CFTS024-165` |
| 148 ER line 3 | "has stopped on more than one station and has returned to the first one" | "has stopped on **every receivable channel of the selected genre**, as defined by CFTS024-165" |
| 149 reference | `CFTS024-4872954; CFTS024-4872955` | `…; CFTS024-177` |
| 149 ER line 3 | "has presented more than one station and has returned to the first one" | "has presented **every receivable channel of the selected genre**, as defined by CFTS024-177" |

So the "one ER line and a reference field on two rows" this entry predicted is
exactly what is in the workbook. Nothing to apply before write-back.


## [A-SX22] Configuration-gate clauses are unallocated document-wide — REGISTERED (2026-08-11)

Third instance, so recording it as a class rather than per-clause.

| clause | section | gate | consequence when the gate fires |
|---|---|---|---|
| 4872750 | 1.5 | source presence | flagged in B5 as the one §1.5 clause worth asking about |
| 4872960 | 1.5.16 | `$Country_Code$` = [Canada] | the traffic and weather Jump function is not displayed at all |

Both are unallocated, both fail R10-2 (b) for the same structural reason: every
leaf in their section is exercised under a configuration in which the gated
feature is present, so no leaf's scenario can observe its absence.

`4872960` is the sharper case — the observable is a whole feature disappearing
in a market the requirement metadata lists (the scope line on these clauses
names NAFTA - Canada), not a field changing.

**For RD-1:** is market-configuration behaviour in scope of this workbook? The
answer is one ruling covering every gate clause, not a decision per clause. If
it is in scope, these clauses need leaves — 037 provides none. If it is not,
they should be recorded as out-of-scope rather than as coverage holes, the same
disposition question the bus-signal clauses raised in B8.


## [A-SX14 addendum] `Description` typing proves the SFR-typed pointer notes are a defect — MEASURED (2026-08-11)

A-SX14 and the B11 decision record both flagged clauses whose text is a pointer
("please refer to …") while their ReqIF artifact type reads `Subsystem
Functional Requirement`. The reading at the time was that this is probably an
authoring defect, but it could not be separated from a house convention where
every clause is typed SFR regardless of content.

B12 settles it. `4872971` is a pointer note of exactly the same shape —
"Please refer to {SX-9845-0008 - SXI Implementation Guide} for more
implementation details on Game Alerts" — and its artifact type is
**`Description`**.

So the document does have a prose type and does use it. The SFR typing on
`4872965`, `4872968` and the A-SX14 clauses is therefore inconsistent with the
document's own practice, not a blanket convention.

Consequence for the delivery: none of those clauses gains or loses a test —
they were already recorded as not testable as written. What changes is the RD-1
framing: the question is no longer "is pointer content meant to be a
requirement?" but "these specific clauses are mistyped; please retype or
rewrite them", which is a smaller and more answerable request.

Also recorded from `4872971`: it cites `SX-9845-0008`, a SiriusXM supplier
document in a third citation scheme (neither the 7-digit STLA form nor the
`CFTSnnn-n` short form). No leaf clause writes it, so R11 offers no path to it
in any case.


## [A-SX23] The skipped-channel table is keyed two ways, and §1.5.19 duplicates twice — PART-RULED: key NOT ruled, goes to RD-1 class-3 (2026-08-11)

Three findings in §1.5.19. The first is a content contradiction, so per the
A-SX20 standing carve's escape hatch (i) it does **not** fold into that class
and returns to chat.

**1. What the skipped-channel table stores — contradiction.**

- `4873277` (leaf 168): "a table of **skipped channel numbers**"
- `4873284` (leaf 175): "the HU shall store the **Service ID** of the selected
  channel to the skipped channel list"

These are different keys with a different observable consequence. If the
line-up is renumbered — which SiriusXM does — a number-keyed skip stays on the
slot and a service-keyed skip follows the content. One of the two behaviours is
wrong, and a parental control that silently unskips explicit content on a
renumber is the failure mode that matters.

Handling this batch: §8.6 authority chain — each leaf is tested against its own
allocated clause. Leaf 175 asserts the discriminating consequence (the skip
follows the service across a renumber). Leaf 168 asserts the table's
*persistence* and deliberately does **not** assert which key it holds, so the
two rows do not contradict each other in the delivered workbook.

**For chat / RD-1:** which key is normative? If it is Service ID, `4873277`'s
wording should be corrected; if it is the channel number, leaf 175's test is
wrong as written and its ER needs replacing, not amending.

**RULED (Pei, 2026-08-11) — 不裁鍵.** The identification key is deliberately
left unruled and goes to RD-1 as an upstream question. This is the correct
call rather than a deferral: choosing between "channel number" and "Service
ID" here would be the TC author deciding a parental-control behaviour that the
requirement document states two ways, and whichever way we chose, half the
delivered evidence would rest on our choice rather than on the spec.

Consequence for the delivery, and why nothing regenerates: the batch-local
handling **already assumes no key**. Leaf 168 asserts the table's persistence
and deliberately does not name the key; leaf 175 asserts the discriminating
consequence its own clause states. The two rows are consistent with each other
under either answer, so both stand as written and the workbook ships without
an unratified key decision embedded in it.

**Evidence read after the ruling (2026-08-11, verbatim clause pull) — the
contradiction is Description prose against an SFR, not two normative clauses
in conflict.** Both clauses sit in CFTS024 §1.5.19 under the same anchor
`4873276`, `resolution: reqif`, and neither appears in
`data/reqif_vs_bracket_diff.json` — the reqif and bracket sides agree, so this
is not an export artefact.

```
4873277  The HU maintains a table of skipped channel numbers which it uses
         to prevent the cabin from selecting channels.
         [Artifact Type:Description]  ECU: RRM, ETM, LTM  Radio: allSys

4873284  When a channel is selected to skip, the HU shall store the Service
         ID of the selected channel to the skipped channel list.
         [Artifact Type:Subsystem Functional Requirement]
         ECU: ETM, RRM, LTM  Radio: allSys, CTS1_2
```

Across the whole section, `4873277` is the **only** Description; the other
seven clauses are Subsystem Functional Requirements:

| leaf | id | artifact type | identification key as written |
|---|---|---|---|
| 168 | 4873277 | **Description** | skipped channel **numbers** |
| 169 | 4873278 | SFR | skipped **channels** (neutral — names no key) |
| 170 | 4873279 | SFR | not applicable |
| 171 | 4873280 | SFR | not applicable |
| 172 | 4873281 | SFR | not applicable |
| 173 | 4873282 | SFR | not applicable |
| 174 | 4873283 | SFR | not applicable |
| 175 | 4873284 | SFR | **Service ID** |

The normative side is therefore consistent: `4873278` maintains a table of
"skipped channels" without committing to a key, and `4873284` fixes the key as
Service ID. Nothing normative says "numbers" — only the Description does.

What this changes, and what it does not:
- **The carve does not move.** 168 still asserts persistence without naming
  the key, 175 still asserts its own clause `4873284` through the renumber
  construction. Both are now backed by the artifact-type hierarchy (an SFR
  outranks a Description) in addition to §8.6, so the handling is firmer than
  when it was ruled, not looser.
- **`[A-SX23]` stays on 175.** A contrary answer is still a single-row ER
  replacement; the failure mechanism is unchanged.
- **The RD-1 disposition is corrected** — class-2 expedited → **class-3
  wording confirmation**, and the question becomes a wording-alignment
  request rather than a behavioural one: *"4873277 (Description) says
  'skipped channel numbers' while the allocated SFR 4873284 stores the Service
  ID. Please align the Description wording with the SFR, or state which is
  normative if the difference is intended."* Ruled in DECISIONS Amendment 9 as
  a correction to Amendment 7 (3), not a reversal of it.

Findings 2 and 3 of this entry (the `Clear All` / `Deselect All` naming carve,
and 169 restating 168) are the A-SX20 shape and are covered by that entry's
standing rule — they are not re-ruled here.

**2. `4873279` / `4873280` (leaves 170 / 171) — the same clause with different
function names.** Both open with the identical sentence about Channel Skip
under 'SiriusXM Setup' and individual selection. `4873279` then adds
`Clear All`; `4873280` adds `Select All` **and** `Deselect All`. `Clear All`
and `Deselect All` describe the same effect under two names — the A-SX17 shape,
inside one section. Carve by the function name each clause writes: 170 owns
`Clear All`, 171 owns `Select All` and `Deselect All`.

**3. `4873278` (leaf 169) restates `4873277` (leaf 168).** Both say the HU
maintains a table of skipped channels used to prevent cabin selection. Carved
under the A-SX20 standing rule: 168 takes the table's maintenance (persistence
across a power cycle), 169 takes the scope of the block (only the skipped SDAR
channel is refused, other channels of the same source are not).

**Cross-batch consequence, already applied.** Leaf 106 (B8) asserts that the
All Channels browse list holds *every* available station. Leaf 173 says Browse
All Channels shall not display skipped channels. 106's assertion is therefore
true only when nothing is skipped, which its pre-conditions did not say. A
pre-condition was backfilled to 106 and its reasoning notes the dependency.
This is the first cross-batch interaction found in this delivery and it argues
for a sweep of completeness-style ERs before delivery.

## [A-SX24] Leaf 177 is an allocated leaf whose clause is a pointer note — REGISTERED (2026-08-11)

`4873290`, allocated to leaf 177, reads in full:

> Please see the HMI logic & flow for the appropriate message to be displayed
> when SAT button is pressed while subscription is inactive.

It states no HU behaviour. B11 and B12 met the same content unallocated, where
the disposition was simply "not testable as written". Here it has a leaf, so
102-of-102-style coverage requires a row: the delivery cannot silently drop an
allocated leaf.

Written to the maximum the clause supports: pressing SAT with the subscription
inactive displays *a* message and does not enter playback, with the
subscription-active case as the control so a permanently displayed message
cannot pass. The message text is not asserted — the clause itself delegates it.

Note the artifact type is `Subsystem Functional Requirement`, which is the
mistyping the A-SX14 addendum identified. This is the first case where that
mistyping has a delivery consequence rather than only a bookkeeping one: it
produced a leaf, and therefore a workbook row that verifies almost nothing.

**For RD-1:** should `4873290` be withdrawn as a note, with leaf 177's coverage
carried by leaf 176 (`4873289`, the no-subscription message and its contents)?
The two are adjacent and 176 is the substantive one.


## [A-SX25] §1.5.21.2 states 18 requirements with no acceptance criterion — REGISTERED (2026-08-11)

The Performance section is qualitatively different from the rest of CFTS024.
Of its 20 leaves, **18 state a property with no threshold, tolerance or
measurement method**, and only two carry a number.

| shape | leaves | what is missing |
|---|---|---|
| "without user-perceivable delay" | 188, 189, 190, 191 | no time threshold; "perceivable" is left to the observer |
| defect-absence over an unbounded window ("shall not flicker", "shall not freeze", "no black screens at any time", "only fully rendered") | 192, 193, 194, 195, 196 | no observation duration, no sampling rate, no operation set |
| "proper" / "consistent" / "harmonized" relative to other HMI elements | 199, 200, 201, 202 | no tolerance in pixels, ratio or colour distance; no list of theme elements |
| intent prose and design statements | 183, 185, 186 | 183 has no `shall`; 186's modal is `should`; 185 quantifies over "any radio function" |
| **has a number** | **197, 198** | — variance not greater than 500 ms, stated in the clause's own NOTE |

**What was done rather than what would have been easy.** No threshold was
invented. Writing "the transition completes within 200 ms" would have produced
tidy, objective-looking rows and would have put an unratified acceptance
criterion into the delivered workbook, where a supplier would be held to it.

Instead each TC fixes what *can* be fixed and leaves the judgement visible:

- a **defined 360L exercise set** is written into the pre-conditions of every
  qualitative test, identically worded, so two testers exercise the same thing;
- defect-absence tests require a **recording reviewed frame by frame**, which
  separates "no defect occurred" from "nobody was watching at that moment";
- delay tests are **repeated five times and compared against each other**, so
  "perceivable" has an internal reference instead of resting on one impression;
- the relative-appearance tests (199–202) capture screens holding both
  360L-drawn and non-360L-drawn elements **in the same frame**, because the
  clauses define the property relatively and a 360L-only screenshot cannot
  decide it;
- 197 and 198, the two that have a number, are measured and subtracted.

**These rows are honest but weak, and they are weak because the requirements
are.** A tester can execute all 18 and a defect can still ship, because the
clauses do not say what failure is.

**For RD-1 — the single highest-value question in this delivery.** Ask for
acceptance criteria on §1.5.21.2:
1. What time bounds the four "user-perceivable delay" clauses (188–191)? A
   number in the clause would make four rows objective at a stroke.
2. Over what duration and operation set are 192–196 to be observed? Absence
   claims need a window.
3. What tolerance applies to "proper", "consistent" and "harmonized"
   (199–202), and what is the list of theme elements for 202?
4. Is 186 (`should` be parameterized) a verifiable requirement at all, or a
   design note? It has no pass criterion of its own and its subject is
   implementation structure, not observable behaviour.

Without answers, §1.5.21.2's 18 rows are the weakest evidence in the workbook
and should be flagged as such at delivery rather than presented as equivalent
to the functional rows.

## [A-SX26] `4873295` is a fully specified display requirement with no leaf — RULED: gap recorded, no leaf invented (2026-08-11)

Found by B13's R10-2 pass over §1.5.20's unallocated clauses, where it was the
only one of four to fail for a reason other than "not an HU-side observable".
Recorded here rather than left in `docs/b13-absorption-decisions.md`, because
RD-1 needs to cite an anomaly entry, not a batch working note.

`4873295` specifies, in one clause: the trigger (a Global Channel Information
update arriving over the air while satellite audio or Travel Link is playing),
the message text (`"Updating Channels Please Wait . . ."`), an audio
consequence (no satellite radio audio during the update), and a persistence
requirement (the message is maintained across SDARS audio and Travel Link
screens). Every part of that is HMI-observable. **No leaf carries it.**

It is the structural twin of leaf 182 (`4873296`) — the PSV update message, the
very next clause in the same section, which does have a leaf. R10-2 (b) fails
against 182 all the same: a GCI update and a PSV update are different
over-the-air events, so 182's scenario cannot produce this message and one test
cannot observe both.

**RULED (Pei, 2026-08-11): record the gap, do not self-supply a leaf.**

No row is written and no leaf id is invented. The delivered coverage claim
stays exactly 202 of 202 *allocated* leaves. A self-supplied leaf would make
the workbook claim coverage of a requirement the 037 never allocated — the one
direction a coverage table must not drift, because a later reconciliation
against the 037 would find a row tracing an id that does not exist upstream,
and the reconciler could not tell an invented leaf from a transcription error.

What ships instead is the statement of the gap. Unlike the bus-signal and
section-prose cases in the same pass, nothing about this clause explains its
absence — which is what makes it the strongest single-clause allocation gap in
the delivery, and stronger stated as a gap than papered over with a row.

**For RD-1:** why does `4873295` have no leaf when `4873296`, its neighbour and
twin, has one? If the omission is an oversight, the 037 needs a leaf and this
delivery needs one more row.

## [A-SX23 addendum] Completeness-ER sweep run across the whole corpus — CLOSED (2026-08-11)

B13 found that leaf 106's "every available station appears" assertion is true
only when nothing is skipped, and argued for a sweep before delivery. The sweep
was run over all 202 leaf files, matching completeness-style ER phrasing.

Seven TCs assert enumeration over a set. Three already carried a
skipped-channel pre-condition (106 after the B13 fix, 171 and 172, whose
subject is the skip list itself). Two more needed it and got it:

- **148, 149** — the Genre Seek and Genre Scan tests assert the sweep reaches
  every receivable channel of the selected genre. A skipped channel cannot be
  selected at all, so a skip inside the genre would break the assertion. A
  pre-condition excluding skips from the selected genre was added to both.

Two need nothing: **121 and 153** enumerate *cities* with traffic data, and the
skip list holds channels, so no interaction exists.

Sweep closed — no completeness assertion in the corpus is now defeatable by the
skip feature.


## [A-SX27] framework Part IV's `Source Availability` Set is named for a gate its only leaf does not contain — REGISTERED, post-delivery canon item (2026-08-12)

Found while checking the premise of a drafted P0 ruling (DECISIONS Amendment
10 item 3, withdrawn). The Set name and the granularity note describe one
thing; the leaf inside describes another.

What Part IV says:

| where | text |
|---|---|
| Part IV Set table | `Source Availability \| 1.5 \| 001 \| 1 \| remaining` |
| Part IV §4.1.3 granularity note | "`Source Availability` (1) is a genuine outlier per §4.2 — **the satellite-source presence gate** shares no setup with any sibling (AMFM `Tuner Availability` precedent)" |

What leaf 001 actually is:

```
SWE-RA-SXM-001   CFTS024-4872752   §1.5 HU Satellite Audio
"HU shall be capable of displaying the Channel Art image for the currently
 tuned channel as required per the HMI specifications. Requirements contained
 in {SX-9845-0166 - Channel Graphics Service Protocol Specification (XM Band)}
 shall be complied with unless otherwise specified by Chrysler."

TC title: Channel art is displayed for the tuned channel
```

§1.5 holds this one leaf and no other, so there is no source-presence clause
anywhere in the Set. The genuine satellite-presence and signal-loss gates are
in §1.5.20 Error Displays — `4873289` (no active subscription, leaf 176),
`4873292` (Acquiring Signal, leaf 179), `4873294` (antenna open/short, leaf
181) — which is a different Set entirely.

Why this is worth an entry rather than a silent fix: the note did not merely
mislabel a box, it was **read as evidence about content** and a priority
ruling was drafted on it. A Set name is a grouping label; it is not authority
for what a leaf requires. The AMFM `Tuner Availability` precedent the note
cites is what makes the name plausible, and that is exactly why it misleads.

**Disposition — post-delivery canon item, nothing shipped changes.**
- The delivered column H value for row 10 stays `Source Availability`. It is
  the Set the leaf was generated under, it is consistent across the workbook,
  and re-labelling one row after write-back would break the Part IV ↔ workbook
  correspondence the Set-gate check verifies (215/215 currently matching).
- Owed at the canon pass: rename the Set to what §1.5 actually holds, or keep
  the name and correct the §4.1.3 granularity note so it no longer asserts a
  presence gate. Either way the note must stop describing content it does not
  contain.
- No leaf is invented and no leaf moves Set (§8.2 discipline, A-AM13 / A-SX26
  precedent).
