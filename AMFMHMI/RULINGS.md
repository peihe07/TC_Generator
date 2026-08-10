# RULINGS — AMFM intake (pre-scaffold)

## R1 — Requirement source (Pei, 2026-08-09)

**Ruling: 以 037-A03 最新版為主** — the SWE1_AMFM FM-WI-FSM-037-A03 report
(102 leaves, `SWE-RA-RAD-*`, dated 20260323, sources = SYSAD architecture
components) is the authoritative requirement basis for TC generation.

Interpretation on record (to be confirmed at Phase 2 sign-off): "A03" refers
to the 037-A03 STLA 報告 file, not to a newer revision of the SWRA-A02
document lineage (no such file is present).

## Consequences — three collisions this ruling creates

### C1 — Workbook Scope field contradicts the ruling
The workbook Scope reads `FM-WI-SW-RAD-SWRA-A02`. Under R1 that is stale and
must be updated to name the 037-A03 (same defect class as Home A-H26, caught
in the same week — the field is evidently copy-managed by hand).
- Action: Scope correction is part of write-back, exactly as Home A-H26.

### C2 — The done region traces the WRONG requirement family
All 158 existing rows (author Wilson) trace `SWE-RAD-*` — the SWRA-A02
family, not the ruled source. Under R1, for traceability purposes the
workbook is effectively **BLANK against the 037-A03's 102 leaves**: zero
rows trace `SWE-RA-RAD-*`.
- Sub-decision C2a (PENDING, Pei): what happens to Wilson's 158 rows?
  (i) keep as-is (legacy region, frozen, excluded from invariants — the
      Home A-H06 scoping trick at 158-row scale), or
  (ii) remove/replace in the regenerated workbook, or
  (iii) re-map: if SWE-RAD reqs correspond to SWE-RA-RAD reqs, re-trace
      them — but the two sets describe DIFFERENT content (user functions
      vs system behaviors), so a clean mapping is unlikely; any partial
      mapping is RD work, not TC-author work (§8.2).
- Style-authority note: whichever way C2a goes, Wilson's rows remain the
  workbook's only style precedent (Test Group/Set filled, TC IDs assigned,
  req-ref embedded in procedure). Style can be borrowed even if
  traceability is not.

### C3 — The SWRA-A02's 57 leaves lose their coverage claim
If the 037-A03 is the source, the 57 `SWE-RAD-*` leaves (with ASIL/FTTI
columns) are no longer the coverage target of THIS workbook.
- Sub-decision C3a (PENDING, Pei): confirm the 57 leaves need no coverage
  here (superseded / covered elsewhere / retired). If any survive as
  requirements, they need a home — otherwise this ruling silently drops
  safety-annotated requirements, which an assessor will ask about.

## Practical next steps under R1

1. feature.yaml `a03_report` → the 037-A03 file (Scope-arbitration in
   intake.py currently picks SWRA-A02 per the stale Scope; override
   manually until the Scope cell is fixed)
2. Trace chain: SWE-RA-RAD → SYSAD components → SYS3 docx (architecture) +
   CFTS024 doc (upstream). spec_reference format is an open Phase 3 item —
   candidates: SYSAD component id, SYS3 section, or CFTS clause (mode D
   lookup). BT profile §3.6 precedent applies.
3. SYS2 export (Sys-RA ids, CFTS024) is the safety-analysis layer; check at
   recon whether any 037-A03 leaf carries a safety attribute requiring it.
4. Recon needs the AM/FM template adaptation (header/columns by text, the
   intake.py v2 approach) before it can survey this 037.

C2a and C3a block nothing at intake/recon time but MUST be ruled before
write-back strategy is designed — they define what "done region" and
"completeness" even mean for this workbook.

## R2 — Workbook base (Pei, 2026-08-09)

**Ruling: 選項 (a)** — the delivered pre-filled instance
`FM-WI-FSM-036-A01 ..._SWQT_CFTS024_Radio_20260129.xlsx` is the working
base for recon and write-back, now placed in `inputs/`. The blank form
(`..._SWQT_20260121.xlsx`, in `forms/`) was considered as an alternative
bootstrap base and rejected for now; it remains available as the layout
reference. C2a (disposition of Wilson's 158 rows within this instance)
stays PENDING and is unaffected by R2.

## R3 — Authorship principle (Pei, 2026-08-09)

**Ruling (verbatim): 「只要是我產的要打PeiPYHsu，完全引用他人的就留著他人的名字」**
— rows Pei generates carry `PeiPYHsu`; rows fully quoted from another
author keep that author's name. Applied to feature.yaml
(`write_back.author_value`, done_region comment). Under R4(i) the frozen
Wilson rows therefore keep `Wilson`.

A-AM05's two prior corrections signed in the same pass:
`done_region.author_value: Arif → Wilson` (selector semantics per R4),
`columns.remarks: AH → AG` (header text is authority).

## R4 — C2a: Wilson 158 rows (Pei, 2026-08-09)

**Ruling: 選項 (i) — 凍結為 legacy region**，並綁一條 RD-1。

- The 158 `SWE-RAD-*` rows stay in the workbook, frozen, excluded from
  coverage/traceability invariants (Home A-H06 scoping at 158-row scale)
- Style authority survives: borrow style, not traceability (A-AM02 note)
- Re-map (iii) rejected: RD work, not TC-author work (§8.2); would resolve
  at most ~1/3 (A-AM03) with per-pair human confirmation
- Replace (ii) rejected for now: organizational cost not assessable inside
  the pipeline; if RD-1 confirms SWRA-A02 formally superseded, downgrade
  to (ii) later is a pure deletion operation — (i) preserves that option
- RD-1 question (the A-AM04 sharpened form): was the 037-A03 authored
  against an earlier SWRA-A02 revision? Is the contiguous tail
  `SWE-RAD-040`…`-045` deferred or deleted? Is SWRA-A02 formally
  superseded? — recorded in `docs/fw036/RD1_questions_amfm.md`

## R5 — C3a: 18 unrepresented SWRA-A02 rows (Pei, 2026-08-09)

**Ruling: 確認本 workbook 不承擔其覆蓋。**

- Safety exposure measured and bounded: all 57 SWRA-A02 rows are ASIL `QM`
  / FTTI `NA`; R1 drops no ASIL-rated requirement (A-AM04)
- Disposition question merges into the R4 RD-1 (same question, two faces)
- A-AM04 resolution condition: RD-1 reply arrives or delivery deadline,
  whichever first

## R6 — DECISIONS remaining [PROPOSED] (Pei, 2026-08-09)

**Ruling: 照案簽。** Includes: SYS2/SYSRA layer not in trace chain (no
ASIL/FTTI attachment point on ruled leaves); style authority = Wilson rows
(style only); spec_reference `<Spec Filename>_{outline}` pending Phase 3
mode-D refinement; batch plan by spec chapter, pilot = smallest coherent
batch; done-region compliance notes (5) frozen, not fixed.

## R7 — Phase 3 framework rulings (Pei, 2026-08-09)

Verbatim: 「Q1-AMFM Q2 能力制 Q3本來就會有多份，如果需要補上我會補上該份spec
重複就是重複 但要標注起來我會自行判斷」

- **Q1 — Test Group = `AMFM`** (overrides the Wilson `Radio` precedent for
  new rows; legacy rows keep `Radio`, frozen). feature.yaml `test_group`
  already reads `AMFM`.
- **Q2 — Test Set = capability scheme** (framework Part III table), not the
  legacy band scheme (`FM`/`AM`/`USB`). Divergence from legacy recorded in
  the profile.
- **Q3 — multi-spec references are expected.** Cite `CFTS024-{stla_id}` /
  `CFTS011-{stla_id}` / `CFTS004-{stla_id}` per the leaf's source; missing
  spec files (CFTS011, CFTS004) will be supplied by Pei when needed —
  registered A-AM06/A-AM07, no leaf blocked, no RD-1 for the files.
  CFTS004 attribution carries `[ASSUMPTION A-AM07]` until the file confirms.
- **Q4 — duplicates stay duplicates, marked.** 037-internal duplicate STLA
  ids and numbering gaps registered as A-AM08; each leaf still gets its own
  TC (§8.2, no consolidation); disposition of each duplicate pair is Pei's
  per-case call at review.

The R6 spec_reference placeholder (`<Spec Filename>_{outline}`) is hereby
refined by R7-Q3 to the per-source `{doc}-{stla_id}` format.

## R8 — VR trigger path out of scope (Pei, 2026-08-10)

**Ruling (verbatim): 「不進去了」** — the VR Command trigger path is NOT
covered by this workbook. Leaves 003 / 009 / 025 / 027 test the HU HMI
main path only; the CFTS clauses' "or a VR Command" alternative belongs
to the CFTS028 (Voice Recognition) delivery. Each affected TC's
`reasoning` notes the delegation (§8.2.1 pattern). Closes the A-AM09 VR
class. Consistent with the 037's own systematic omission of VR wording
(A-AM09 evidence).

## R9 — Leaf 029 spec_reference correction (Pei, 2026-08-10)

**Ruling: 029 → `CFTS024-4872457`.** Evidence: 029's title is the
verbatim body of clause 4872457 (Direct Number Input; similarity 0.909,
vs 0.036 against its declared 4872451), minus exactly the VR wording the
037 systematically omits. The declared id `(4872451)` is a copy error
(4872451 = ICS tune-down, correctly owned by 028). Consequences:
- spec_reference for 029 = `CFTS024-4872457` (overrides the declared id)
- the 028/029 entry in A-AM08 is NOT a duplicate pair — reclassified as
  an upstream id-tail typo; goes to RD-1 (Q-AM2)
- pipeline: `build_stla_map.py` needs a declared-id override entry for
  029 (Claude Code side) so the map and batch context resolve to 4872457

## R10 — Pilot gate rulings (Pei, 2026-08-10)

**Ruling (verbatim): 「都走你建議的」** — all four pilot-gate points adopt
the recommended dispositions:

1. **Config-gate design method = EP** (001/002 and generalized): leaves
   that pairwise/groupwise cover a configuration parameter's value classes
   are Equivalence Partitioning, not Functional. Applies corpus-wide
   (e.g. 064 dual-tuner, 066 `$ANT_TYP$`, 081–085 market config).
   Profile §3.3 amended.
2. **A-AM10 absorption kept, two hard conditions**: (a) every absorbed
   clause id enters `specification_reference` (dual/multi cite per §10.7)
   — 025-02, 027-02, 029 to be fixed; (b) RD-1 Q-AM3 notifies upstream of
   the full unallocated-clause set. Decision test added to Profile §4:
   unallocated + same spec section + elaborates the leaf's cited clause →
   absorb with `[A-AM10]` marker + multi-cite; otherwise → coverage hole
   in reasoning + RD-1.
3. **Suppression branch = independent TC** (026-02/028-02 confirmed, and
   generalized): an "only if X" clause with reachable ¬X yields its own
   suppression TC (different trigger state; §5.2 forbids in-procedure
   branching; §7/§8.3 independent partial failures). Profile §4 amended.
4. **Remarks: external language only**: signed upstream-correction notes
   are allowed in Remarks, phrased for external readers, never internal
   ruling ids. 029's remark rewritten; 025-02/027-02 remarks superseded by
   the (2a) multi-cite; 026-02/028-02 A-AM09 remarks dropped (the cited
   clause itself carries the wording — nothing to explain externally).
   Profile §3.6 amended.

Review notes (classification: note, not defect): 001 step 5 ER softened to
"the seek executes" (seek stop-on-station detail owned by Seek leaves);
A-AM11 formally registered.
