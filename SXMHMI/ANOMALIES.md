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
  CFTS019 and CFTS024 `.reqifz` probes pending — both files exist upstream;
  cite-form stands unless one of them resolves its tokens.

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
