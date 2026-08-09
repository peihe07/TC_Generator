# Requirement-family overlap — 037-A03 vs SWRA-A02

- new report: `SWE1_AMFM_FM-WI-FSM-037-A03 STLA 報告_SWRA STLA Report_SWRA_20260323.xlsx` — 102 requirement rows
- old report: `FM-WI-SW-RAD-SWRA-A02.xlsx` — 57 requirement rows
- alignment axis (discovered): **037-A03.title ↔ SWRA-A02.description**

Axis scores (count of near-verbatim matches; the axis is discovered,
not assumed — see the module docstring for why that matters here):

| new field | old field | strong matches |
|---|---|---|
| title | description | 35 ← |
| title | title | 0 |
| description | title | 0 |
| description | description | 0 |

## Result

| | count | of |
|---|---|---|
| 037-A03 leaves with a near-verbatim ancestor (≥0.85) | **35** | 102 |
| 037-A03 leaves with a plausible ancestor (0.6–0.85) | 6 | 102 |
| 037-A03 leaves with no ancestor (<0.6) — new work | **61** | 102 |
| SWRA-A02 rows that are a leaf's near-verbatim ancestor | 35 | 57 |
| SWRA-A02 rows represented only by a paraphrase | 4 | 57 |
| SWRA-A02 rows represented nowhere — **dropped by the ruling** | **18** | 57 |

Mapping shape: 35 strong matches consume 35 distinct SWRA-A02 rows — 1:1.

## Candidate ancestry (037-A03 → SWRA-A02, ≥0.6)

Screening output. Every row is a candidate for human confirmation,
never a mapping.

| 037-A03 | SWRA-A02 | similarity |
|---|---|---|
| SWE-RA-RAD-077 | SWE-RAD-036 | 0.991 |
| SWE-RA-RAD-039 | SWE-RAD-013 | 0.989 |
| SWE-RA-RAD-032 | SWE-RAD-010 | 0.984 |
| SWE-RA-RAD-041 | SWE-RAD-014 | 0.984 |
| SWE-RA-RAD-042 | SWE-RAD-015 | 0.983 |
| SWE-RA-RAD-065 | SWE-RAD-025 | 0.980 |
| SWE-RA-RAD-045 | SWE-RAD-017 | 0.979 |
| SWE-RA-RAD-044 | SWE-RAD-016 | 0.979 |
| SWE-RA-RAD-079 | SWE-RAD-038 | 0.978 |
| SWE-RA-RAD-037 | SWE-RAD-012 | 0.977 |
| SWE-RA-RAD-023 | SWE-RAD-008 | 0.975 |
| SWE-RA-RAD-074 | SWE-RAD-033 | 0.974 |
| SWE-RA-RAD-022 | SWE-RAD-007 | 0.971 |
| SWE-RA-RAD-036 | SWE-RAD-011 | 0.971 |
| SWE-RA-RAD-076 | SWE-RAD-035 | 0.970 |
| SWE-RA-RAD-015 | SWE-RAD-002 | 0.969 |
| SWE-RA-RAD-080 | SWE-RAD-039 | 0.969 |
| SWE-RA-RAD-047 | SWE-RAD-018 | 0.968 |
| SWE-RA-RAD-049 | SWE-RAD-019 | 0.968 |
| SWE-RA-RAD-071 | SWE-RAD-031 | 0.967 |
| SWE-RA-RAD-075 | SWE-RAD-034 | 0.967 |
| SWE-RA-RAD-050 | SWE-RAD-020 | 0.966 |
| SWE-RA-RAD-016 | SWE-RAD-003 | 0.964 |
| SWE-RA-RAD-017 | SWE-RAD-004 | 0.964 |
| SWE-RA-RAD-051 | SWE-RAD-021 | 0.963 |
| SWE-RA-RAD-018 | SWE-RAD-005 | 0.962 |
| SWE-RA-RAD-024 | SWE-RAD-009 | 0.962 |
| SWE-RA-RAD-078 | SWE-RAD-037 | 0.957 |
| SWE-RA-RAD-063 | SWE-RAD-024 | 0.955 |
| SWE-RA-RAD-066 | SWE-RAD-026 | 0.950 |
| SWE-RA-RAD-067 | SWE-RAD-027 | 0.950 |
| SWE-RA-RAD-070 | SWE-RAD-030 | 0.940 |
| SWE-RA-RAD-072 | SWE-RAD-032 | 0.938 |
| SWE-RA-RAD-020 | SWE-RAD-006 | 0.884 |
| SWE-RA-RAD-062 | SWE-RAD-023 | 0.881 |
| SWE-RA-RAD-068 | SWE-RAD-028 | 0.836 |
| SWE-RA-RAD-069 | SWE-RAD-029 | 0.785 |
| SWE-RA-RAD-014 | SWE-RAD-001 | 0.764 |
| SWE-RA-RAD-060 | SWE-RAD-024 | 0.688 |
| SWE-RA-RAD-021 | SWE-RAD-008 | 0.623 |
| SWE-RA-RAD-061 | SWE-RAD-022 | 0.616 |

## SWRA-A02 rows represented nowhere in 037-A03

These are what the ruling drops. If any is still a live requirement
it needs a home, or the coverage claim is lost silently.

`SWE-RAD-001-01` `SWE-RAD-001-02` `SWE-RAD-001-03` `SWE-RAD-001-04` `SWE-RAD-001-05` `SWE-RAD-001-06` `SWE-RAD-040` `SWE-RAD-040-001` `SWE-RAD-040-002` `SWE-RAD-040-003` `SWE-RAD-041` `SWE-RAD-041-001` `SWE-RAD-041-002` `SWE-RAD-041-003` `SWE-RAD-042` `SWE-RAD-043` `SWE-RAD-044` `SWE-RAD-045` 
