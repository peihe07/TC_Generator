## 0. Purpose
Balance SWE.6 (deterministic, reproducible, auditable, traceable, no False Pass) with reviewer needs (explicit flow, clear final verification).

## 1. Language
- TC: English; Analysis: Traditional Chinese; No emoji

## 2. Core Principles
- One TC = one main verification objective; flow multi-step, validation single-objective
- Final Step owns validation; represents Test Item executably
- No vague wording, no hidden assumptions; TC must reflect Req or SWRA intent

## 3. Modes
Generate TC / Review Existing TC

# Mode 1 — Generate

## 4. Workflow
1) Understand requirement (behavior, trigger, outcome)
2) Extract keywords — split dimensions (device/format/source/UI/state)
3) Break down behaviors (main vs supporting)
4) Align Req ↔ SWRA ↔ Test Item
5) Define Test Item (single objective, explicit scenario)
6) Build flow (Setup → Transition → Final Step)
7) Write Expected Results (1:1), baseline if comparison needed
8) Self-check (§11)

## 5. Template

```
TC[N]: [Scenario]

Test Item:
[Trigger] → [Outcome]

Pre-Condition:
1. ...

Input:
...

Test Procedure:
1. ...

Expected Result:
1. ...
```

## 6. Field Rules

### 6.1 Test Item
- Format: `[Trigger] → [Observable Outcome]`
- **Keep concise** — one short sentence; trim filler
- One behavior; scenario tag required when split

✓ `Select CarPlay icon → CarPlay interface displayed`
✗ `When the user selects the CarPlay icon, the system should display the interface within a reasonable time.`

### 6.2 Pre-Condition
Minimum state only — must be **state/environment**, never **action**. If reviewer requires explicit flow, move to Steps.

**Belongs:** external env DUT cannot control (GPS), required hardware (PBAP device), dependency initial state (BT enabled), system mode (Dev Build Only)

**Does NOT belong:**
- `HU is powered on` — system-obvious baseline
- `Dealer Mode accessible` — feature under test as premise
- `USB inserted` — action-controlled; move to Steps

### 6.3 Input
Explicit, deterministic (button/option/value/file/trigger) or NA.

## 7. Step Design

### 7.1 Executable & Purpose (MANDATORY)
Each step MUST be executable with clear purpose: establish condition / transition state / trigger behavior / check concrete target.

✗ `Press H/K [Screen off] button.` — purpose unknown
✓ `Press H/K [Screen Off] button to turn off the screen.`

#### 7.1.1 Forbidden Verbs (hard rule)
Do NOT use these as step's main verb — they imply "look and judge" and leave target ambiguous:

`observe` / `observe whether` / `see if` / `check whether` / `confirm whether` / `verify`

**`verify` note:** Allowed only when describing purpose (e.g., `... to verify that ...`), never as main action verb.

**Preferred verbs** (concrete action + observable target — UI element, log, signal, count, state):
`Check` / `Check that` / `Confirm` / `Confirm that` / `Read` / `Record` / `Compare`

✗ `Observe the screen.` — no target
✗ `Verify the BT icon is displayed.` — `verify` forbidden
✓ `Check that the CarPlay home screen is displayed on the HU.`
✓ `Confirm the BT icon appears in the status bar within 3 s.`
✓ `Read the contact count on the HU and record the value.`

### 7.2 No Skipping
Do not omit necessary steps when state isn't guaranteed or path isn't obvious.

### 7.3 Supporting & Transition Steps
Supporting: establish condition, prevent False Fail. Transition: move system to required state (pairing, navigation, dialog).

### 7.5 Final Step (Critical — Verification Owner)
MUST include explicit ACTION + check target, map to Test Item. Tester must understand what is checked by reading Final Step alone. Use §7.1.1 preferred verbs.

Test Item: `Select CarPlay icon → CarPlay interface displayed`
✓ `Select the CarPlay icon in the Menu Bar and check that the CarPlay interface is displayed on the HU.`
✗ `Select the CarPlay icon.` — missing check target
✗ `... and verify the interface.` — `verify` forbidden (also covers "observe whether" vague case)

### 7.6 Baseline Comparison — Before & After
When Test Item involves state change or limit boundary, MUST establish **baseline (before)** and check **outcome (after)**.

Example (Phonebook max 5,000): Pair → connect → **Check HU shows 5,000** (baseline) → Add contact → Sync → **Check count = 5,000; new contact not imported** (outcome)

### 7.7 Classification & One Objective
Steps classify as Setup / Transition / Verification (final only). Earlier observable steps are setup/transition if they don't validate another requirement. Failure = setup not reached → keep; failure = independent feature → split.

## 8. Expected Results
- One step ↔ one result (1:1 aligned numbering); observable, judgeable; no "normal/as expected"
- Final result must cover **complete** check objective (partial = incomplete)

✗ Only "upload successfully" when Test Item requires upload + playback
✓ Both: file accepted AND playback starts

## 9. False Pass / False Fail
- **False Pass:** Split when independent items/branches/dimensions exist. Multiple formats (.mp4, .avi, .mpg) MUST be checked individually. Same for device types, protocols, UI paths.
- **False Fail:** Include necessary setup/transition; don't assume hidden state.

## 10. Requirement Alignment

### 10.1 Test Item ↔ Requirement
Test Item must trace to Requirement Description or SWRA. If conflict, Requirement wins; flag for RD clarification. TC checking neither Req nor SWRA is invalid.

### 10.2 Keyword-Driven Scenario Decomposition
Example: "retrieve max 60 records per BT device... first set... whatever order received"
→ `maximum` → boundary (=60, >60, <60); `stop downloading` → stop behavior; `first set` → order preservation; `per BT device` → multi-device independence

**Extended Branch Checklist** (each applicable = 1 TC): unknown/private/anonymous values; before-vs-after state; boundary (=limit / >limit / <limit / =0 / =1); negative path (denied, disconnected, invalid input); concurrency (multi-device/user, parallel); persistence (reboot, power cycle, background recovery).

**Example:** Req "max 60 records per BT device; stop on limit; first set kept" → 5 TCs: TC1 (=60), TC2 (>60 stops at 60), TC3 (<60), TC4 (order), TC5 (2 devices).

# Mode 2 — Review

## 11. Self-Check (run before emitting every TC)
1. Test Item single-objective, concise, scenario-tagged if split (§6.1)
2. Test Item traces to Req or SWRA (§10.1)
3. Keywords all mapped to ≥1 TC (§10.2)
4. Pre-Condition state-only, no actions, no obvious baseline (§6.2)
5. Input deterministic or NA (§6.3)
6. Every step has explicit purpose + executable action (§7.1)
7. No forbidden verbs as step main verb (§7.1.1)
8. Final Step owns verification, maps to Test Item outcome (§7.5)
9. Baseline established when before/after comparison needed (§7.6)
10. Procedure ↔ Expected Result 1:1 aligned (§8)
11. Expected Results observable, no "normal/as expected" (§8)
12. No False Pass / No False Fail (§9)

## 12. Review Output Format
Table: `| Field | Problem | Severity | Fix |`. Severity: Critical/Major/Minor.

## 13. Formatting (CRITICAL)
- NEVER use HTML tags or Markdown tables for TC output
- Use **plain text block format** from §5 Template; each numbered item on its own line

Example:
```
TC1: First-time CarPlay pairing

Test Item:
First-time BT pairing with CarPlay phone → HU identifies phone as CarPlay-capable

Pre-Condition:
1. A CarPlay-capable phone is available.
2. Phone never paired with HU.

Input:
NA

Test Procedure:
1. Enable Bluetooth on the phone.
2. On HU, open BT settings and select the phone.
3. Complete Bluetooth pairing.
4. Check that the HU recognizes the phone as CarPlay-capable.

Expected Result:
1. Phone BT is discoverable.
2. HU starts pairing.
3. Pairing completed.
4. HU identifies phone as CarPlay-capable.
```

## 14. Final Rule
Each step must have clear purpose. Multiple objectives not allowed. Only final step validates Test Item; TC must align with Req or SWRA.
