# Test Case Framework — STLA Media HMI (SWE.6)

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

037 does not allocate a leaf to every SYS1 sub-section. A sub-section with no
leaf of its own belongs to the batch of its nearest **leaf ancestor**, and its
text is in scope for that ancestor's TCs. A sub-section that IS itself a
remaining leaf stays with its own parent and must not be pulled upward.

Example: 11.3.1 is a leaf whose own text is only the abstract *"label may
change based on connected drive type"*; the testable behaviour lives in the
unallocated 11.3.1.1 / 11.3.1.1.1, so both fall under 11.3.1's parent
(SWE1-MEDIA-PLA-062). 10 of the 158 remaining leaf sections are affected —
see `tcgen_package/ANOMALIES.md` A-001; implemented in
`make_batch_context.py`.

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
