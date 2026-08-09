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
