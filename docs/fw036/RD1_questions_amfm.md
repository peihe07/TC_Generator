# RD-1 Questions — AMFM (FW036)

Sent to upstream requirement authors. Attached to RULINGS R4/R5;
resolution condition for A-AM04: reply arrives or delivery deadline,
whichever first.

## Q-AM1 — SWRA-A02 ↔ 037-A03 lineage (from A-AM03 / A-AM04 evidence)

Context: the FW036 CFTS024_Radio workbook's 158 existing rows trace the
`SWE-RAD-*` family (FM-WI-SW-RAD-SWRA-A02, 57 leaves, all ASIL QM / FTTI
NA). The ruled requirement basis (037-A03, 20260323) contains 102
`SWE-RA-RAD-*` leaves; 35 carry near-verbatim SWRA-A02 descriptions in
their Title column (1:1), 61 have no ancestor, and 18 SWRA-A02 rows are
represented nowhere. The 18-row drop is a contiguous tail
(`SWE-RAD-040`…`-045` with sub-items) plus the sub-decomposition of
`SWE-RAD-001`.

Questions:
1. Was the 037-A03 authored against an earlier revision of the SWRA-A02?
2. Is the contiguous tail `SWE-RAD-040`…`-045` (and the `SWE-RAD-001`
   sub-items) deferred to a later release, or deleted?
3. Is FM-WI-SW-RAD-SWRA-A02 formally superseded by the 037-A03 as the
   requirement basis for the CFTS024_Radio FW036 workbook? (The workbook
   Scope field still names the SWRA-A02.)

Status: DRAFT — send at or before delivery (RUNBOOK Phase 7).

## Q-AM2 — 037-A03 internal defects (from A-AM08 / R9 evidence)

Context: mechanical id-vs-clause verification (`build_stla_map.py`,
`verify_ids`) over the 037-A03.

Questions / findings to report:
1. `SWE-RA-RAD-029`'s Requirement Title is the verbatim body of CFTS024
   clause **4872457** (Tune by Direct Number Input, §1.3.6) but its
   declared id tail reads `(4872451)` — the ICS tune-down clause owned by
   `SWE-RA-RAD-028`. Please correct the 037's id tail to `(4872457)`.
   (TC side already generates against 4872457 per ruling R9.)
2. Numbering gaps `SWE-RA-RAD-086` and `-088` — deleted or misnumbered?
3. Same-id variants and text-overlap pairs for awareness (no correction
   requested yet, per-pair review at batch time): 087/094 share 4942534;
   089/095 share 4942540; 090/096 near-identical text with distinct ids;
   **014/015 — 015's clause is a near-subset of 014's first sentence**
   (TC side carved distinct verification targets per R12-1).
4. Artifact-type hygiene: `SWE-RA-RAD-019`'s source clause `4872426` is an
   `[Artifact Type: Description]` item used as a requirement. Generated
   against it per R1 (leaf's own citation); please confirm Description-
   type items are intended requirement carriers or reissue as SFRs.

Status: DRAFT — send with Q-AM1.

## Q-AM3 — CFTS clauses allocated to no leaf (from A-AM10)

Context: the 037-A03 allocates leaves against CFTS024 Description clauses;
some same-section Subsystem Functional Requirements are allocated to no
leaf. Where such a clause elaborates an allocated leaf's clause, the TC
side has absorbed its behaviour into that leaf's TCs (marked, multi-cited)
so the customer-specified behaviour is not left untested.

Known instances (Tune, §1.3.4–1.3.6): 4872440, 4872441 (→ SWE-RA-RAD-025);
4872449, 4872450 (→ SWE-RA-RAD-027); 4872458 (→ SWE-RA-RAD-029). A
full-corpus list follows once the sweep completes.

Questions:
1. Please confirm the absorption reading, or allocate these clauses to
   leaves explicitly in the next 037 revision.
2. If any unallocated clause is intentionally out of scope, please state
   so — the TC side will then retract the corresponding coverage.

Status: DRAFT — send with Q-AM1/Q-AM2.
