# Project Profile — FW036 / R1L SWE1 SXM (SiriusXM 360L SAT Only, Stellantis newR1L)

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.
>
> Instantiated from `FW036_R1L_AMFM_Profile.md` plus the seven-item delta
> signed in `features/sxm/DECISIONS.md` §6. Where a clause below is unchanged from
> the AMFM profile it is because the two features share one spec document
> (CFTS024) and one 037 template family — **not** because it was inherited
> without checking. Each delta cites its source ruling.

## 0. Project identity [ADD]

- Program: Stellantis newR1L; scope 037-A03 SXM, 202 leaves `SWE-RA-SXM-001…202`
- Deliverable workbook: FM-WI-FSM-036-A01 `SWQT_SXM_20260810`
- **Workbook is BLANK** — no legacy region, no done region, no frozen rows.
  Style authority is the fallback chain (DECISIONS §4), not a local precedent.
- **Form revision C** (A-SX05): first feature on this layout. `Estimated Test
  Time` at **Q** shifts design_method → R, functional_safety → S, author →
  **AA**, remarks → **AH**. The data sheet is `Test Case Specification
  測試用例規範`, without the `&Result` suffix every A/B instance uses.
  `Test Case Framework` sheet: **absent** (verified 2026-08-10, 9 sheets) →
  the 14 Set names live in the per-row columns only (framework Part IV,
  Workbook sync).
- Author on new rows: `PeiPYHsu`.

## 1. Requirements authority chain [ADD]

- Chain: CFTS024 §1.5.x clause (STLA id) → SYSAD_SXM components → 037-A03 leaf
  → FW036 TC.
- **HYBRID ingestion (DECISIONS §1, implemented)** — three sources, each
  authoritative for exactly one thing:
  - **ReqIF** (`…CFTS 024…20250910_1224.reqifz`, SHA256 `325dba60…`) — clause
    id and clause text. Identifiers are attributes (`ReqIF.ForeignID`), so no
    typographic inference is involved.
  - **docx** (`…20250910_1239.docx`, SHA256 `e5c12e9e…`) — the printed section
    number (heading text) **and the scope metadata line**
    (`[Artifact Type:…] [ECU:…] [Market:…] [Radio:…] [EE Architecture:…]`).
    The ReqIF carries none of these: every scope attribute is empty on all
    1,604 exported objects, and absorption decisions turn on those tags.
  - **bracket lookup** — nothing. Retained as a **fail-loud verifier**: a
    disagreement with the ReqIF placement raises `BuildError` and aborts the
    build. It is never downgraded to a warning.
  - Dual-path status at wiring: **202/202** agreement on section, clause text
    and scope metadata.
- spec_mode D. The SiriusXM 360L SAT Only HMI L&F (PDF + SYS1 export) is the
  **figure and flow source** (mode C role), never the citation source
  (framework Part IV).
- Version baseline: SR24 1A (SAT Only). The 26PI2.5 full-360L file is
  reference-only — it is a different scope, not a newer revision
  (DECISIONS §1).
- SYS2/SYSRA safety layer does NOT enter the trace chain: the 037-A03 carries
  no ASIL/FTTI column (DECISIONS §3, AMFM R6 precedent).

## 2. Test Set vocabulary [OVERRIDE — replaces the generic free-form labels]

- Test Group = `SXM` (column G) and the capability Test Set (column H) from
  framework **Part IV**, on every generated row. `fill_test_group_set: true` —
  ruled under BLANK per canon §2 (DECISIONS §4).
- The 14 Sets are the Part IV table. Layer 3 (CFTS024 printed section numbers)
  is framework-internal and **never written to the workbook**.
- `Instant Replay` (30) and `Browse` (39) are deliberately unsplit: transport
  buttons are sub-actions of one capability, browsed category is a data axis
  (§8.3). Workload is handled at BATCH level (B1–B14), never by splitting a Set.

## 3. FW036 SXM house style (field rules)

### 3.1 Test Item [OVERRIDE — replaces §4.3 tc_title-only cell content]

Test Item = condensed requirement statement in spec language (modals permitted
HERE ONLY, quoting requirement text). The generic §4.3 tc_title (no modals) is
still produced in output JSON for lint and sibling distinction. Multiple TCs
per leaf append the distinguishing scenario tag.
§6 unchanged for ER: no modal verbs, ever.

### 3.2 Pre-Conditions [ADD — SXM applicability triggers]

Valid spec-trigger Pre-Conditions (§8.5 exception) include:
- Source state: `The HU Satellite Audio source is selected on the Cabin Output
  Channel` (the CFTS's standing trigger phrase for §1.5.x — the SAT counterpart
  of AMFM's HU Tuner phrasing)
- Subscription / activation state where the clause names it (§1.5.9.2)
- Replay-buffer state: `A replay buffer has been established on the tuned
  channel` for §1.5.10.x — the transport buttons are undefined without it
- `HU is powered on` remains banned (generic rule)

### 3.3 Design Method [OVERRIDE — restricts §12 output strings]

Return exactly one of the 9 dropdown strings from the workbook `下拉選單`
sheet, character-for-character (verified present on revision C). §12 mapping
logic unchanged.
- **Config-gate rule (AMFM R10-1, adopted)**: leaves that pairwise/groupwise
  cover a configuration parameter's value classes are Equivalence Partitioning
  on every side of the partition, not Functional.

### 3.4 Signal / CAN citations [ADD]

CFTS `$SIGNAL$ = [value]` notation is quoted verbatim in Pre-Condition / Input
Test Data; the profile-scoped §11 exception for source-quoted tokens applies
(square brackets retained inside quoted signal values only; author prose still
uses `"..."` for UI labels).

### 3.5 Spec Reference [OVERRIDE — replaces §10.7 filename format]

**Delta 1 of 7 — `{doc}-{stla_id}` + HYBRID pointer** (DECISIONS §1/§4).

Format: `{doc}-{stla_id}` where `{doc}` = `CFTS024` and `{stla_id}` is the
7-digit id taken from the leaf's 037 Requirement Title — never constructed by
guess. All 202 leaves resolve to an exact CFTS024 clause anchor (A-SX01).

- The id is **searched for, not anchored to end-of-string**: 11 titles carry a
  trailing `(add)` marker after the id (A-SX01/A-SX03). An end-anchored pattern
  silently drops exactly those 11 and reports a clean 191/202.
- The clause a `spec_reference` names is resolved through the HYBRID map
  (`data/stla_to_cfts.json`, `resolution: reqif`), never by reading the docx
  ad hoc.

**Delta 2 of 7 — R11 cite-form** (A-SX02, ruled for SXM on its own evidence,
not inherited).

Four leaves cite other documents in a short-id scheme that resolves in **no**
released artefact — docx, CIP xlsx, ReqIF attribute sets and the 037 all
negative, upgrade branch CLOSED:

| leaf | token(s) |
|---|---|
| 005, 080 | `CFTS024-193`, `CFTS024-195`, `CFTS024-197` |
| 107 | `CFTS019-494`, `CFTS019-496` |
| 137 | `CFTS020-138` |

Handling — **cite-form, not absorption**:
- cite the token **verbatim** as a second `specification_reference`, after the
  leaf's own clause (`CFTS024-4872862; CFTS024-193`)
- the ER **may** assert the borrowed outcome, anchored to the citation
  (`…, as defined by CFTS024-193`); an unanchored assertion is forbidden — it
  reads as this leaf's own verified behaviour
- the cited document's **rule surface is out of scope**: which conditions
  qualify, the specification of the behaviour itself
- cite-form claims **no coverage** of the cited requirement: no `[A-SX08]`
  marker, and it does not enter the absorption gate

**Ported lint gates** (from the AMFM implementation, same names):
- `cross-reference` — a short-form token is accepted only under the leaf whose
  clause actually writes it (membership from the citation sweep), so the
  3-digit form cannot become a hole in the `CFTSnnn-nnnnnnn` format check
- `cross-reference-anchor` — a cited token with no ER line anchoring to it fails
- cite-form citations are **excluded** from the absorption multi-cite count

### 3.6 Remarks [ADD]

Empty string unless: BLOCKED row (none expected), anomaly flag, documented
workaround, or a twin mirror note.

**Delta 3 of 7 — twin mirror Remarks, 11 rows** (A-SX04).

Eleven SXM leaves are ≥0.95 text twins of AMFM §1.3.x clauses under **different
clause ids in a different chapter** — CFTS024 states the requirement once per
band family, so there is no coverage conflict and nothing is cross-cited. Each
of these rows carries, verbatim:

```
Analog-chapter twin: CFTS024-<analog id> (covered in the AM/FM deliverable)
```

| SXM leaf | SAT clause | analog clause |
|---|---|---|
| 020 | 4872780 | 4872413 |
| 024 | 4872786 | 4872442 |
| 037 | 4872805 | 4872475 |
| 108 | 4872899 | 4872429 |
| 110 | 4872901 | 4872430 |
| 132 | 4872934 | 4872493 |
| 140 | 4872943 | 4872499 |
| 142 | 4872945 | 4872500 |
| 143 | 4872946 | 4872501 |
| 148 | 4872952 | 4872506 |
| 149 | 4872954 | 4872508 |

- **Clause id only, never an AMFM TC id.** TC ids are assigned at write-back
  and shift on any AMFM regeneration; clause ids are stable and resolvable
  inside CFTS024 without the other workbook.
- Remarks stays **external-facing** (AMFM R10-4): no internal ruling or anomaly
  ids. `A-SX04` belongs in reasoning, not here.
- 020 and 024 differ from their twins only in band vocabulary
  (`Tuner` → `Satellite Audio`, `executed` → `initiated`); §8.6 gives the SAT
  wording authority, which is what the TC uses anyway.

### 3.7 Estimated Test Time (column Q) [ADD]

**Delta 4 of 7 — UNRULED_BLANK** (A-SX05, DECISIONS §2).

Revision C's new column has **no ruled fill policy**. It is left **blank at
generation** and reported as a named blank-by-decision column in the write-back
dry-run summary — the AMFM `UNRULED_BLANK` mechanism, not the
`INTENTIONALLY_BLANK` list, because blank here is a pending answer rather than
a convention.

Estimating without a source is §8.4-adjacent fabrication, and `NA` reads as
refusal. Write-back can fill the column corpus-wide later if the RD-1 answer
defines a rubric.

## 4. Split policy [ADD]

Generic §8.3 applies. SXM-specific:
- wrap-around and other boundary behaviour is a **boundary TC of the clause it
  bounds**, not an independent function (AMFM Profile §4 precedent)
- an "only if X" clause with reachable ¬X yields its own **suppression TC**
  (different trigger state; §5.2 forbids in-procedure branching)

**Delta 5 of 7 — R10-2 absorption ADOPTED, marker `[A-SX08]`** (framework
Part IV note 5).

Decision test, per unallocated clause: **(a) same spec section AND (b) the
clause elaborates the leaf's cited clause** → absorb, with
- `[A-SX08]` in the parent's `assumptions`, naming the absorbed clause id, and
- the absorbed id added to `specification_reference` (multi-cite).

Failing either condition → **coverage hole recorded in reasoning + RD-1**, never
a silent absorption. **Whole-section gaps cannot pass (a)** — §1.5.8,
§1.5.12.1.5+, §1.5.18, §1.5.21.1, §1.5.21.2.1 have no leaf to elaborate; they go
to RD-1 Q-SX as an allocation-policy question in the Q-AM3 wording pattern (ask
the policy, do not assert systematic omission).

Each batch's context carries its sections' unallocated clauses **with their
scope tags**, so the test is run per clause at generation.

## 5. Marker vocabulary [ADD]

**Delta 6 of 7 — three markers, stackable** (A-SX03 / A-SX07 / A-SX08).

Inline in generated JSON `reasoning` / `assumptions`:

| marker | meaning | leaves |
|---|---|---|
| `[A-SX03]` | the leaf entered the 037 outside the release process — `(add)` after the id tail, `Release Version` and `Requirement Status` both empty | 080, 083, 110, 148, 149, 154–158, 182 |
| `[A-SX07]` | the 037 title and the declared id describe different clauses; **content follows the clause**, the title is the upstream defect | 154 |
| `[A-SX08]` | an unallocated same-section clause was absorbed under R10-2 | per absorption |

They stack: **leaf 154 carries `[A-SX03]` + `[A-SX07]`** and, being a §8.6
wording divergence as well, also gets the standard wording note. It is in the
B1 pilot precisely so the marker mechanism is exercised on the hardest row
first.

Markers live in reasoning/assumptions. **Never in Remarks** (external-facing,
R10-4).

## 6. Escalation — what does NOT carry over [ADD]

**Delta 7 of 7 — R8-equivalent is NOT auto-inherited** (DECISIONS §6).

AMFM's R8 ruled the VR Command trigger path out of scope for that workbook.
That ruling is **not** inherited here. The first SXM clause that grants a VR
Command (or equivalent alternative trigger path) **stops and returns to chat**
for a ruling — it is not silently delegated to another deliverable by analogy.

Same rule for any other AMFM ruling not listed in this profile: if a situation
arises that an AMFM ruling would have covered, it returns to chat. The seven
deltas above are the complete set of adopted decisions.

## 7. Known anomalies register [ADD]

`features/sxm/ANOMALIES.md`, A-SX01 … A-SX08, all RESOLVED at Phase 3 sign-off.
Batch-time markers are §5 above. New findings are registered there at the
moment they are found, with the citing leaves named — never after the batch
that needs them stalls.
