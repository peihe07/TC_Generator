# Project Profile — FW036 / R1L SWE1 Privacy (CFTS022 Privacy Mode, Stellantis newR1L)

> **Approved 2026-08-13, R28-1** — with the three revisions of 下放包 07 §2
> incorporated. Revisions 2 and 3 were open questions (P-4 / P-5) at approval
> time and were ruled the same day by **R30-3 / R30-4**; both are written in
> below. §1's mapping clause carries the **R30-1** correction found by
> B1-GATE-1.

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.
>
> Instantiated from `FW036_R1L_SXM_Profile.md` — the nearest sibling, because
> both are BLANK workbooks on the same FM-WI-FSM-036-A01 revision C template.
> **Structural clauses are inherited; content clauses are not.** SXM and
> Privacy share no spec document and no 037 family, so every SXM delta was
> re-derived rather than carried over. Where a clause below has no SXM
> counterpart, §7 says so explicitly.

## 0. Project identity [ADD]

- Program: Stellantis newR1L; scope 037-A03 Privacy, **10 leaves**
  `SWE1-HMI-PRIVACY_FEATURES-001…010` (version C, approved 2026-02-09)
- Deliverable workbook: FM-WI-FSM-036-A01 **generic blank template**
  `SWQT_20260121`, SHA256 `cd876c202c71e74b…`. There is no Privacy-specific
  workbook and none will be requested — **A-PV01 / R23-1** ruled that producing
  the deliverable from the generic template *is* the final form.
- **Workbook is BLANK** — no legacy region, no done region, no frozen rows.
  Style authority is the fallback chain (canon §2), not a local precedent.
- **Form revision C**, same layout as SXM (A-SX05 precedent): `Estimated Test
  Time` at **Q** shifts design_method → **R**, functional_safety → **S**,
  author → **AA**, remarks → **AH**. Data sheet is `Test Case Specification
  測試用例規範` (no `&Result` suffix).
- `Test Case Framework` sheet: **absent** — the template ships 9 sheets
  (`Cover_old`, `ChangeHistory_old`, `Cover 封面`, `ChangeHistory 修訂履歷`,
  `Product Document 記錄封面頁`, `Test Case Specification 測試用例規範`,
  `Reference`, `QS Suggestion`, `下拉選單`). Verified 2026-08-13. The three Set
  names therefore live in the per-row columns only (framework Part VI,
  Workbook sync) — same outcome as SXM, reached by measuring this instance.
- Author on new rows: `PeiPYHsu`. TC id series: **`NR1L-Privacy-{NNN}`**
  from 001 (R-PV02 — full feature name, mixed case, per the template's own
  sample row `NR1L-AntiTheft-001`; **not** the three-letter form SXM uses).

### 0.1 Template preparation state [ADD]

The template shipped with two residual sample rows. Cleared 2026-08-13 under
**R23-4**, via `backend/xlsx_surgical.py`:

- five cells cleared — D10 / F10 / G10 / S10 / D11 — with their `s=` style
  attributes preserved in place
- **column B untouched**: B10 is the formula `=IF(ISBLANK($D10),"",ROW()-9)`,
  so the row number follows column D automatically. Clearing B would have
  deleted the template's numbering mechanism
- whole-row deletion was rejected: it shifts the DV `sqref` ranges and R10's
  x14 dropdown

First generated TC lands on **row 10**. Prepared workbook and its provenance
are recorded in `features/privacy/DELIVERY.sha256` (ENTRY 001).

**Excel open confirmed — Pei, 2026-08-13, four checks passed (R29-1)**: no
repair prompt, column R dropdown live with the nine `下拉選單` entries, D5 Scope
reads `SWE1_CFTS_022-Privacy_Features`, rows 10–11 cleared with no residual row
number. This is the **first end-to-end confirmation of the zip-level surgical
path** — every prior check was程式層 (48→48 members, DV 4:2→4:2), and no
program-level check can speak for Excel's own file-integrity verdict. R18-3
rule 1 now has evidence at both ends.

## 1. Requirements authority chain [ADD]

- Chain: CFTS022 artifact (`4915xxx`) → 037-A03 leaf (`SWE1-HMI-PRIVACY_
  FEATURES-nnn`) → FW036 TC.
- **spec_mode D** — clause authority is the CFTS022 docx
  (`R1LR_Atl-H_25PI3.5_Privacy_CFTS_022 Functional Specification_20250910_1708`,
  SHA256 `5eb0dd739f00…`).
- **PROF → artifact mapping — look it up, never compute it (R30-1).**
  The 037's `Source Requirement ID` is `SYS-RA-PROF-nnn`. A `−1` offset holds
  for -003…-010, but **that is a local regularity of the SCV block, not a
  rule**: CFTS022's artifact ids are not contiguous (79 numbers are missing
  from the 4914928–4915339 range alone), so arithmetic derivation fails
  wherever a gap is crossed. It failed on exactly the two leaves outside that
  block:

  | leaf | computed (wrong) | actual | how it was settled |
  |---|---|---|---|
  | -001 | `4915022` — **not in the document at all** | **4914955** | **ECU tag.** `4914954` is `ECU=SCCM` with no `R1L-R` in its Radio list; `4914955` is `ECU=ETM, RRM, ICS, DVD, LTM`, `Radio=allSys`. This project's ECU is **LTM** → 4914955. Measured, not read |
  | -002 | `4915159` — splash-screen timing | **4915158** | **clause text.** Both carry LTM in their ECU tag, so the ECU criterion has no discriminating power here; the wake-up/recall wording does |

  All ten mappings were independently re-derived at **B1-GATE-1** and are
  fixed in framework Part VI. This clause is the concrete case §3.5's
  "looked up, never constructed" exists to prevent — the id was constructed,
  in a different document, under the name of a verified regularity.
### 1.1 ECU attribution — tag is distribution, subject is execution [ADD]

**R34-1.** An artifact's `[ECU:…]` tag says which ECUs' specification carries
the clause — its **distribution**. The clause's grammatical subject says who
**performs** the behaviour. **Attribution for verification follows the
subject, not the tag.**

Two conditions, both required:

1. **Necessary** — the ECU tag includes this deliverable's ECU (LTM)
2. **Sufficient** — the trigger or the outcome subject includes this ECU,
   **or** this ECU holds an observable end of the signal chain

(1) true and (2) false → **exclude**, and name the owner in `reasoning`.
A tag listing LTM means "this clause is relevant to us", **not** "we verify
this behaviour".

**Both precedents stay here, because one criterion producing two different
answers is what shows it discriminates:**

| leaf | clause | outcome subject | this ECU's position | result |
|---|---|---|---|---|
| **-005** | 4915170 | AMP ("considered invalid by the AMP") | HU is the **sender** of `$VolumeSCV$` — an observable end of the chain | **kept**, rewritten to output-set closure (R33-1) |
| **-008** | 4915173 | AMP ("the AMP shall recall") | none — the clause never mentions the HU | **excluded**, BLOCKED row (R34-2/3) |

-008 is also the only one of the ten whose ECU tag lists `AMP`
(`ETM, AMP, RRM, LTM`) — but note that it lists `LTM` too, which is exactly
why condition (1) alone cannot decide.

- **SYS3 SYSAD is context-only** (A-PV05 / R23-3): background understanding
  only, **never** a `specification_reference` (canon §10.7 bars analysis and
  design documents). Declared as `context_only` in `feature.yaml`.
- SYS2/SYSRA safety layer does **not** enter the trace chain: the ruled 037
  carries no ASIL/FTTI column (recon 2026-08-13; AMFM R6 / SXM precedent).
- **Need list is not derivable from this 037**: its source column holds
  component/Polarion ids, not document citations. Trace runs through the
  architecture and export files instead (intake 2026-08-13).

## 2. Test Set vocabulary [OVERRIDE — replaces the generic free-form labels]

- Test Group = `Privacy` (column G) and the capability Test Set (column H) from
  framework **Part VI**, on every generated row. `fill_test_group_set: true` —
  ruled under BLANK per canon §2.
- The three Sets are the Part VI table: `Input Monitoring`,
  `Personalization Display`, `Speed-Controlled Volume`.
- **Layer 3 = CFTS022 artifact id**, framework-internal, **never written to the
  workbook**.
- `Speed-Controlled Volume` (8 leaves) is deliberately unsplit. Splitting it by
  restore / signal / adjustment would give 5 Sets over 10 leaves — canon
  §4.1.3's "Test Set column becomes a near-copy of the TC ID column"
  anti-pattern. Workload is handled at BATCH level, never by splitting a Set.
- The two single-leaf Sets are **genuine outliers under §4.2**, not accidents:
  -001 and -002 are the only non-SCV requirements in the feature and share
  neither setup nor UI entry point with SCV. Precedent: AMFM
  `Tuner Availability` (2), SXM `Source Availability` (1).

## 3. FW036 Privacy house style (field rules)

### 3.1 Test Item [OVERRIDE — replaces §4.3 tc_title-only cell content]

Test Item = condensed requirement statement in spec language (modals permitted
**here only**, quoting requirement text). The generic §4.3 tc_title (no modals)
is still produced in output JSON for lint and sibling distinction. Multiple TCs
per leaf append the distinguishing scenario tag.
§6 unchanged for Expected Result: **no modal verbs, ever**.

*Inherited from SXM §3.1 — structural, applies to any FW036 deliverable.*

### 3.2 Pre-Conditions [ADD — Privacy applicability triggers]

Valid spec-trigger Pre-Conditions (§8.5 exception):

**Traced to CFTS022 clause by clause, 2026-08-13 (R35-8), and labelled by
source class per R36-4** — `spec-verbatim` / `spec-derived` / `test-setup`.
**An unlabelled phrase counts as untraced.** The reason the labels exist:
a vocabulary table's authority is *assumed*, not verified — generated rows go
back to the source, the table is only ever quoted. Three of this table's five
original phrases turned out not to occur in CFTS022 at all (R36-3). Every phrase below
either quotes the spec or is flagged as test-setup language that does not. The
table this replaced was drafted in 下放包 04 without tracing, and three of its
five phrases turned out not to appear in CFTS022 at all.

- `spec-verbatim` — **Amplifier presence**: `The amplifier is present` /
  `The amplifier is not present`. **Corrected** — the earlier `An external amplifier is present on
  the vehicle` was wrong twice over: CFTS022 contains **no** occurrence of
  `external amplifier` and **none** of `on the vehicle`. The spec's own forms
  are `the amp is not present` (4915171), `the AMP is present` (4915172) and
  `the amplifier is not present` / `the amplifier is present` (4915174/4915175).
  This is the feature's central configuration axis — six of ten leaves turn on
  it (§4). **Never write `The HU has determined that the amplifier is…`** in a
  Pre-Condition: that asserts an unobservable internal state (R35-3).
- `spec-verbatim` — **Wake-up source**: `The HU wakes up on Interior CAN` (4915168) /
  `The AMP wakes up on the Interior CAN` (4915173, verbatim — **note the
  article `the`**, which the earlier table dropped).
- `spec-verbatim` — **Sleep-mode exit**: `The A&T System exits 'SLEEP MODE'` (4914955).
  **Corrected** — the earlier `The HU has exited Sleep Mode` had the wrong
  subject (the spec says the **A&T System**, not the HU) and the wrong casing
  (the spec quotes `'SLEEP MODE'` in caps). `HU has exited` appears nowhere in
  CFTS022.
- `test-setup` — **not spec wording** — permitted, but flagged as such so
  it is never mistaken for a quotation: `A CAN interface tool is connected`
  (A-PV16), `An audio source is playing over the cabin speakers`,
  `… is set to a state other than its default state`. None of these appear in
  CFTS022; they exist to make the outcome observable.
- `banned` — `HU is powered on` (generic rule): implied by every other trigger,
  and it carries no verification value.


### 3.3 Design Method [OVERRIDE — restricts §12 output strings]

Return exactly one of the **9** dropdown strings from the workbook `下拉選單`
sheet, character-for-character.

- **Authority is `下拉選單!A1:A9`** — nine entries. Two template defects are
  recorded and deliberately not worked around:
  - the DV on R11:R59 points at `$A$1:$A$11`, i.e. two blank options, while R10
    points at `$A$1:$A$9` (A-PV10 / R23-6)
  - `Reference!C9` reads `Pair-wise / N-wise` where `下拉選單!A6` reads
    `Pairwise / t-wise` (A-PV11 / R23-7)
  `Reference` is a descriptive appendix and **does not enter lint**. Both
  defects go upstream with RD-1.
- **Boundary/validity rule (下放包 07 §2 修訂 1)**: -005 (valid vs invalid
  `$VolumeSCV$` values) takes **Equivalence Partitioning**, and this
  **explicitly displaces §12's first-match order**. §12's first row is
  `Invalid input / illegal op → Negative / Invalid`, which -005's negative
  side would otherwise hit first; excluding only `Functional` would leave the
  real competitor unaddressed and the review argument unsettled.
  The reason EP wins: the leaf's verification objective is **the partition
  between valid and invalid classes**, not the handling of one illegal input.
  **If -005 is split into several TCs under §8.2.2, §12 applies to each TC
  on its own**: a TC that only exercises invalid-side handling is
  `Negative / Invalid`; a TC that exercises the partition is
  `Equivalence Partitioning`.

### 3.4 Signal citations [ADD]

**Source class (R36-4): `spec-verbatim`.** Retraced 2026-08-13 —
`$VolumeSCV$` occurs 8 times in CFTS022 and `<Tsend>` 12 times, both in the
exact form used here.

CFTS022 `$SIGNAL$` notation is quoted verbatim in Pre-Condition / Input Test
Data — `$VolumeSCV$`, `<Tsend>`. The profile-scoped §11 exception for
source-quoted tokens applies: square brackets are retained inside quoted signal
values only; author prose still uses `"..."` for UI labels.

*Inherited from SXM §3.4; the token set is Privacy's own.*

### 3.5 Spec Reference [OVERRIDE — replaces §10.7 filename format]

Format: **`CFTS022-{artifact_id}`**, where `{artifact_id}` is the 7-digit
CFTS022 artifact id resolved through the PROF → artifact mapping (§1).

- The id is **looked up, never constructed** — spec_mode D's defining rule.
  The −1 offset is a verified regularity, not a licence to compute an id for a
  leaf whose mapping has not been checked (**-001 / -002 pending**).
- **VF651 external references** carry the platform constraint of §4 below.

**No cite-form mechanism.** SXM needed one (its §3.5 Delta 2) because four of
its leaves cite short-form ids that resolve in no released artefact. Privacy has
no such case: all ten leaves resolve to CFTS022 artifacts directly. If one
appears at P2, it returns to chat — it is **not** inherited by analogy (§7).

### 3.6 Remarks [ADD]

Empty string unless: BLOCKED row, anomaly flag, or documented workaround.

Remarks is **external-facing** (AMFM R10-4): no internal ruling ids, no anomaly
ids (`A-PV…`, `R23-…`). Those belong in `reasoning` / `assumptions`.

No twin-mirror mechanism — SXM's §3.6 Delta 3 exists because eleven of its
leaves are text twins of AMFM clauses. Privacy has no sibling deliverable
sharing a spec document.

### 3.7 Estimated Test Time (column Q) [ADD]

**UNRULED_BLANK**, same as SXM (A-SX05). Revision C's new column has no ruled
fill policy for Privacy either. Left **blank at generation** and reported as a
named blank-by-decision column in the write-back dry-run summary.

Estimating without a source is §8.4-adjacent fabrication; `NA` reads as refusal.
Write-back can fill the column corpus-wide later if an RD-1 answer defines a
rubric.

### 3.8 Functional Safety (column S) [ADD]

**Always `NA`** (R30-3, P-4).

Ruled from corpus, against the analysis layer's own prior recommendation. The
AMFM customer deliverable's 158 hand-written rows carry `NA` in this column
**158/158**; the Privacy blank template's factory sample row S10 was also `NA`
before R23-4 cleared it. Two independent sources, same direction.

The earlier proposal was `UNRULED_BLANK` on the reasoning that `NA` asserts
"no functional-safety requirement" and asserting that without checking the
SYSRA's coverage is §8.4-adjacent. The reasoning was sound and the corpus
overruled it — `framework.md`'s standing rule is to measure the done region
before inventing a rule, and to record the measurement rather than the
intuition when the two disagree (two Home rulings were reversed this way).

This does **not** change §1: the SYSRA still does not enter the trace chain.
`NA` here is the house convention for this column, not a claim derived from
the safety analysis.

### 3.9 Vehicle Model columns (T–Z) [ADD]

**Always blank** (R30-4, P-5). Precedent: AMFM's 158 rows carry **0** values
across its vehicle-model block.

Measured header text of revision C (T8:Z8 is one merged cell,
`Vehicle Model 車型`):

| T9 | U9 | V9 | W9 | X9 | Y9 | Z9 |
|---|---|---|---|---|---|---|
| `HDCC27 Atl-Hi` | `DT27 Atl-Hi` | `VF(ProMaster)637 Atl-Mi` | `Commander (598) Atl-Mi` | `Regengade (5210) Atl-Mi` | `Toro(2261) Atl-Mi` | `Fastack (376) Atl-Mi` |

**None of the seven is HDCC28, which is this project's platform** — the
template's vehicle block stopped at the 27 generation. Registered as
**A-PV15** and raised in RD-1; **do not map a 27-generation column onto the
28 platform**. Same family as A-PV14: there, a VF document from the DT tree
got into `inputs/`; here, the form's own columns did not follow the
generation.

`Regengade (5210)` in X9 appears to be a misspelling of `Renegade`. The
template text is left untouched and the observation goes upstream with RD-1.

## 4. Split policy [ADD]

Generic §8.3 applies. Privacy-specific:

**Source class (R36-4): `spec-verbatim` throughout.** Retraced 2026-08-13 —
`the amp is not present`, `the AMP is present`, `amplifier is not present`,
`amplifier is present`, `shall not change the level`,
`customer selects to change`, `store the new value in memory` and
`personalization entry` all occur in CFTS022 in the forms used here.

**AMP present / not present is a positive/negative pair, never a merge.**
Two pairs exist:

| axis | not present | present |
|---|---|---|
| automatic adjustment | -006 (PROF-172) | -007 (PROF-173) |
| user-initiated change | -009 (PROF-175) | -010 (PROF-176) |

Canon §7 ("an enumerated supported case takes at least one negative TC")
makes each side its own TC. **Merging a pair into one TC with a branching
procedure is forbidden** (§5.2 bars in-procedure branching).

**`Service` / `HMI` is an axis, not a Set boundary** (§8.3). The 037's Sub
Categorization marks -001/-004/-005/-010 as `Service` (signal side) and the
other six as `HMI` (display side). The axis cuts across
`Speed-Controlled Volume` and the labels are classification terms rather than
capability names (§4.2 bars those as Set names). Use it to distinguish siblings
within a Set; never to draw a Set boundary. Precedent: AMFM note 2 (band),
Projection §N.4 (transport axis).

**No absorption mechanism is adopted.** SXM's §4 Delta 5 (R10-2 absorption with
marker `[A-SX08]`) is **not** inherited. Three CFTS022 clauses have no leaf in
this 037 — `4915167` (PROF-168, personalization entry for SCV volume) and
`4915176` / `4915177` (AMP-side compare and store). CFTS022 holds 253
functional requirements while this 037 was allocated 10 leaves, so "no leaf"
most likely means "allocated to another feature's 037". Per canon §8.4.2 and
the asymmetric-error-cost principle, these are **observations, not coverage
gaps**, and **must not be recorded as gaps before P2 verifies allocation**.

## 5. Marker vocabulary [ADD]

Inline in generated JSON `reasoning` / `assumptions`. Prefix is **`A-PV`**, not
the `A-PR` that `new_feature.py` generated from `feature[:2].upper()`
(R-PV02 — the script was deliberately left unchanged).

| marker | meaning | where it appears | leaves |
|---|---|---|---|
| `[BLOCKED-ECU]` | the leaf's clause is performed entirely by another ECU under §1.1 — condition (1) holds, condition (2) does not. The row is produced as a **BLOCKED row rather than omitted**, so the traceability table carries a visible, auditable gap instead of a silent one | **Remarks**, as the opening token | **-008** (only use) |

**`[BLOCKED-ECU]` is the exception to R10-4**, and the exception is narrow.
Remarks is external-facing and normally carries no internal ids; this marker
is there because the customer reading the traceability table needs to know
*why* a leaf has no procedure. Its text names the owning ECU and the open
question — it does not name internal ruling ids beyond the anomaly and RD-1
handles that make the gap followable.

Any other marker still goes in `reasoning` / `assumptions` and **never in
Remarks**. A new marker requires a ruling: creating one at generation time is
a stop-and-report (下放包 09 §2.3).

Prior state, kept for the record: the `[A-PV14]` entry that stood here was
removed when A-PV14 closed (R29-2), and for the whole of B1 this feature had
no marker at all. `[BLOCKED-ECU]` is its first.

## 6. External references — VF651 platform constraint [ADD]

**Source class (R36-4), with one refinement worth stating**: the three-way
`spec-verbatim` / `spec-derived` / `test-setup` split assumes a single spec.
This feature cites two documents, so the labels below name their source.
Retraced 2026-08-13: `{VF651}`, `{CFTS019}`,
`speed controlled audio behavior` and `AMP present configuration requirements`
are **`spec-verbatim` (CFTS022)** — they are the tokens CFTS022's own Note
uses. The variant titles (`LTM Non-Amplified`, `Amplified Audio System`, `ANC`)
do **not** occur in CFTS022; they are **`spec-verbatim` (VF651 filenames)** —
quoted from the other document, not invented here.

`specification_reference` entries pointing at VF651 documents take the
**HDCC28** platform version, without exception. This is where Privacy's
substantive risk sits, so the state of each variant is spelled out:

| variant | state |
|---|---|
| `VF651_V2_R2` (LTM Non-Amplified) | `inputs/` copy `d5813bb7…` **confirmed HDCC28 baseline** (A-PV04 / R23-2) — citable |
| `VF651_V6_R2` (LTM/ETM Amplified) | **swapped to the HDCC28 version** `e20ba7a4…` (177,388 bytes, confirmed R29-2). The former copy `49dd3c31…` came from the DT28 tree and was replaced under R24-2's measure-then-swap procedure — zero differences in the SCV/AMP clauses, so this is a platform-label correction with no substantive impact. **Citable** |
| `VF651_V3_R3` (ETM Non-Amplified) | in `inputs/`, **not cited**. Absence from citations must **not** be read as exclusion — A-PV03 / R-PV01(a) is DEFERRED to P2 re-verification |
| `VF651_V9_R3` / `V11_R3` (ANC) | Not requested (A-PV02). If any leaf turns out to touch an ANC configuration, **stop and report** — do not extend scope |

**Same-name files are identified by hash, never by filename** (R15-5). This is
not a precaution here, it is a necessity: seven of the eight `inputs/` files
have same-name candidates with more than one content in the customer tree, and
V6_R2 has **7 candidates across 6 distinct contents**.

## 7. Escalation — what does NOT carry over [ADD]

The SXM profile's seven deltas were derived from SXM's evidence. Only the
structural ones are inherited here; the content ones are explicitly **not**:

| SXM delta | Privacy |
|---|---|
| 1 — `{doc}-{stla_id}` + HYBRID map | **not inherited** — Privacy has no ReqIF; the mapping is the PROF −1 offset (§1) |
| 2 — R11 cite-form for unresolvable short ids | **not inherited** — no such leaf exists here |
| 3 — twin mirror Remarks | **not inherited** — no sibling deliverable shares a spec |
| 4 — `UNRULED_BLANK` column Q | **inherited** (§3.7) — template-level, not feature-level |
| 5 — R10-2 absorption + `[A-SX08]` | **not inherited** (§4) |
| 6 — three stackable markers | **not inherited** — Privacy has one marker (§5) |
| 7 — R8 not auto-inherited | **inherited as a principle** — see below |

**Nothing from another feature's rulings applies here by analogy.** If a
situation arises that an AMFM or SXM ruling would have covered, it returns to
chat for a Privacy ruling. The clauses above are the complete adopted set.

**Additionally binding, from the cross-feature register**
(`features/amfm/RULINGS.md`):

- **R18-3** — `backend/xlsx_surgical.py` is the only write path; the zip-member
  and DV-count invariant aborts (never warns); a violation is canon §0 item 3
  and escalates to Tier 2
- **R20-5** — Privacy's write_back is built on `xlsx_surgical` from the start.
  **The four existing feature `write_back.py` scripts are quarantined and must
  not be used as a starting point.**
- **R15-2** — a ruling whose outcome is postponement is `DEFERRED`, not
  `PENDING`
- **R22-1** — a hash audit is a present-tense statement; "matches" does not
  imply "was never overwritten"

## 8. Known anomalies register [ADD]

`features/privacy/ANOMALIES.md`, A-PV01 … A-PV14.

At approval: **RESOLVED** A-PV01 / 02(Amplified) / 04 / 05 / 06 / 07 / 08 /
10 / 11 / 12 / 13 / **14**, **CLOSED** A-PV09,
**DEFERRED** A-PV02(ANC) / A-PV03, **PENDING** — **A-PV15 only**
(vehicle-model columns stopped at the 27 generation; RD-1 item).

**A-PV15 blocks nothing.** T–Z are blank under §3.9 regardless of how the
generation question is answered, so B1 and B2 both proceed.

New findings are registered at the moment they are found, with the citing
leaves named — never after the batch that needs them stalls.

## 9. Baseline and delivery integrity [ADD]

Privacy-specific, and the reason it exists is worth stating: on 2026-08-13 four
features' `inputs/` directories and the repo-root `output/` were found empty,
and git had nothing to restore because both paths are gitignored.

- `features/privacy/BASELINE.sha256` — the 8 source files, **tracked**
- `features/privacy/DELIVERY.sha256` — **append-only** ledger of produced
  workbooks, **tracked**; entries are added, never rewritten
- Verify at every session opener and every batch gate, from
  `features/privacy/`:

  ```bash
  shasum -a 256 -c BASELINE.sha256
  shasum -a 256 -c --ignore-missing DELIVERY.sha256
  ```

  Any `FAILED` stops work. `--ignore-missing` is required on the second: the
  ledger accumulates cleaned-up artefacts, and without it they report
  `FAILED open or read`. Tampering still fails and exits 1.
