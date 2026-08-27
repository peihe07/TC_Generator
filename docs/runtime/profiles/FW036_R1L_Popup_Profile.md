# Project Profile — FW036 / R1L SWE1 Popup HMI (Stellantis newR1L)

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.

## 0. Project identity [ADD]

- Program: Stellantis newR1L; scope FM-WI-FSM-037-A03-N1L-SWE1 Popup HMI V0.2
- Feature slug: `popup`; author on new rows: `PeiPYHsu`
- Requirement IDs: `SWE1-POP-002-{mm}` from the 037 report — never invented,
  never renumbered. Heading rows POP-001/POP-002 carry `No TC` ledger marks
  per R-POP5.
- workbook_state = BLANK; no done region. Style authority = fallback chain
  (FO §2.1). Pilot is the only human gate (no done-region third layer).

## 1. Requirements authority chain [ADD]

- Chain: SYS1 Polarion export (Core HMI Logic and Flow, SR24 Post 2A,
  section 5 only) → 037 SWRA decomposition → FW036 TC.
- Spec TEXT authority is the SYS1 export (spec_mode A); the PDF is scanned,
  no text layer — figures only (spec_mode C).
- `forms/Pop Up List HMI R1 (26PI).xlsx` (Main A1 `SR24 Post 2A CR25802`)
  is ADMITTED source material (R-POP6, Pei 2026-08-27), referenced in place
  via feature.yaml `paths.popup_list`. It supplies VALUES for fields the
  spec explicitly delegates to it (GP4: timeout; touch-outside enablement;
  multi-task exceptions). This is §8.4.2-compliant because the current Reqs
  cite the document by name — do NOT absorb Pop Up List rules beyond the
  delegated fields.
- `Pop Up List Priority Matrix ... SR24 1A` in forms/ is NOT admitted
  (R-POP7, two releases behind baseline); queue/priority stays out of scope
  (R-POP2, RD-1 upreport).

## 2. Pop Up List citations [ADD]

- Any value taken from the Pop Up List cites the PU id and field, e.g.
  `as defined by PU0092 Exit Conditions`. Timeout values, exit conditions,
  popup text and button sets come VERBATIM from the cited PU row — never
  from paraphrase, never invented (IN §8.4.1).
- **Notation exception (IN §11 profile-scoped clause, activated here;
  precedent Home A-H10 / R-POP6):** tokens quoted verbatim from a cited
  Pop Up List row — control notation such as `<OK>`, `<X>`, `[OK, X]` —
  retain the source's notation inside quote segments of ER and inside
  `test_item` requirement text. Lint validates retained tokens against the
  cited PU row instead of banning them. The author's own prose (procedure
  press-targets, non-quoting ER lines) always uses `"..."` double quotes.

## 3. Design Method [OVERRIDE — restricts IN §12 output strings]

Return exactly one of the 9 dropdown strings from the workbook 下拉選單
sheet, character-for-character. IN §12 mapping logic unchanged; only the
output string format is fixed. (Home §3.3 precedent; vocabulary is
[AUTO]-extracted in RECON.md.)

## 4. Spec Reference [ADD — clarification, NO override of IN §10.7]

- Format per IN §10.7(b), values verbatim from 037 `HMI Source ID`:
  `SYS1_HMI_Core_HMI_Logic_and_Flow_R1_SR24_Post_2A_(February_2_2023)_{5.5|5.6}`
- SWE1-POP-002-02-derived TCs list BOTH `_5.5` and `_5.6`, one per line,
  ascending, prefix restated per line (R-POP8). All other leaves: single
  `_5.6`. No CFTS family in this feature.
- Unlike bed_lowering (R-BLM5/A-BLM4), both anchors here are upstream
  official column values — no override needed.

## 5. Known anomalies register [ADD]

A-POP1 extraction collision (fixed, ratified R-POP9); A-POP2 Pop Up List /
Priority Matrix found in repo (dispositions R-POP6/R-POP7); A-POP3 `_5.5`
leaf-coverage via -002-02 dual anchor (R-POP8); A-POP4 lint skip-number
prefix gap (R-POP10). Details in `features/popup/ANOMALIES.md`.
