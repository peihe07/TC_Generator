## 0. Purpose
Balance SWE.6 (deterministic, reproducible, auditable, traceable, no False Pass) with reviewer needs (explicit flow, clear final verification).

## 1. Language
- TC: English; Analysis: Traditional Chinese; No emoji

## 2. Core Principles
- One TC = one main verification objective; flow multi-step, validation single
- Final Step owns validation; represents Test Item executably
- No vague wording, no hidden assumptions; TC reflects Req or SWRA intent

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
7) Write ER (1:1), baseline if comparison needed
8) Assign Design Method based on finalized flow (§14)
9) Self-check (§11)

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

Design Method:
[Method Name]
```

## 6. Field Rules

### 6.1 Test Item
- Format: `[Trigger] → [Outcome]` — SHORT, both sides 3–8 words
- Drop articles (a/the), modals (should/will), hedges (properly/successfully)
- One behavior; scenario tag when split

✓ `Select CarPlay icon → CarPlay interface displayed`
✓ `BT A2DP connected (Android Auto off) → music plays through HU`
✗ `When user selects CarPlay icon, system should display interface within reasonable time.` — filler
✗ `Android Auto is disconnected and the phone is connected to HU via BT for A2DP → BT music playback works properly through HU` — too long, trim

### 6.2 Pre-Condition
ONLY the starting **state/environment**. Never actions, checks, reads, or data-presence verifications. Anything requiring operation, reading a value, or confirming data exists → move to Test Procedure.

**Belongs:** external env DUT cannot control (GPS), required hardware (PBAP device), dependency initial state (BT enabled), system mode (Dev Build Only)

**Does NOT belong:**
- `HU is powered on` — system-obvious baseline
- `Dealer Mode accessible` — feature under test as premise
- `USB inserted` / `BT is connected` — action-result; move to Steps
- `HU phonebook has 5,000 entries` / `device has N contacts` — data-presence; set up + read in a baseline step

**Test:** If a line requires the tester to do / check / confirm anything → NOT a Pre-Condition.

### 6.3 Input
Explicit, deterministic (button/option/value/file/trigger) or NA.

## 7. Step Design

### 7.1 Executable & Purpose (MANDATORY)
Each step MUST be executable with clear purpose: establish condition / transition state / trigger behavior / check concrete target.

✗ `Press H/K [Screen off] button.` — purpose unknown
✓ `Press H/K [Screen Off] button to turn off the screen.`

#### 7.1.1 Forbidden Verbs (hard rule)
NOT as main verb: `observe` / `observe whether` / `see if` / `check whether` / `confirm whether` / `verify`
(`verify` OK only in purpose clause `... to verify that ...`)

Preferred: `Check (that)` / `Confirm (that)` / `Read` / `Record` / `Compare`

✗ `Observe the screen.` ✗ `Verify the BT icon is displayed.`
✓ `Check that the CarPlay home screen is displayed on the HU.`

### 7.2 No Skipping
Do not omit necessary steps when state isn't guaranteed or path isn't obvious.

### 7.3 Supporting & Transition Steps
Supporting: establish condition, prevent False Fail. Transition: move system to required state (pairing, navigation, dialog).

### 7.5 Final Step (Verification Owner)
MUST include ACTION + check target, map to Test Item. Tester understands what is checked by reading Final Step alone. Use §7.1.1 preferred verbs.

Test Item: `Select CarPlay icon → CarPlay interface displayed`
✓ `Select CarPlay icon in Menu Bar and check that the CarPlay interface is displayed on the HU.`
✗ `Select the CarPlay icon.` — missing check target
✗ `... and verify the interface.` — `verify` forbidden

### 7.6 Baseline Comparison
When Test Item involves state change or limit boundary, MUST establish **baseline (before)** and check **outcome (after)**.
Example (Phonebook max 5,000): Pair → Check HU shows 5,000 (baseline) → Add contact → Sync → Check count = 5,000; new contact not imported (outcome)

### 7.7 Classification & One Objective
Steps = Setup / Transition / Verification (final only). Earlier observable steps are setup/transition if not validating another requirement. Failure = setup not reached → keep; = independent feature → split.

## 8. Expected Results
- One step ↔ one result (1:1 aligned); observable, judgeable; no "normal/as expected"
- Final result covers **complete** check objective (partial = incomplete)

✗ Only "upload successfully" when Test Item = upload + playback
✓ Both: file accepted AND playback starts

## 9. False Pass / False Fail
- **FP:** Split when independent items/branches/dimensions exist. Multiple formats (.mp4, .avi, .mpg) checked individually. Same for device types, protocols, UI paths.
- **FF:** Include setup/transition; don't assume hidden state.

## 10. Requirement Alignment

### 10.1 Test Item ↔ Requirement
Test Item traces to Req or SWRA. Conflict → Req wins; flag for RD. TC checking neither is invalid.

### 10.2 Keyword Decomposition
Example: "retrieve max 60 records per BT device... first set... whatever order received"
→ `maximum` → boundary (=60, >60, <60); `stop downloading` → stop; `first set` → order; `per BT device` → multi-device

**Branch Checklist** (each applicable = 1 TC): unknown/private; before-vs-after; boundary (=limit/>limit/<limit/=0); negative; concurrency; persistence (reboot/power cycle).

# Mode 2 — Review

## 11. Self-Check (run before emitting every TC)
1. Test Item = `[Trigger] → [Outcome]`, SHORT (3–8 words/side), scenario-tagged if split (§6.1)
2. Test Item traces to Req or SWRA; all keywords mapped (§10.1, §10.2)
3. Pre-Condition: state/environment ONLY; no actions, checks, data-presence (§6.2)
4. Input deterministic or NA (§6.3)
5. Every step has purpose + executable action; no forbidden verbs (§7.1, §7.1.1)
6. Final Step owns verification, maps to Test Item outcome (§7.5)
7. Baseline established when before/after comparison needed (§7.6)
8. Procedure ↔ ER 1:1 aligned; ER observable, no "normal/as expected" (§8)
9. No False Pass / No False Fail (§9)
10. Design Method assigned AFTER finalizing procedure, based on actual flow (§14)

## 12. Review Output Format
Table: `| Field | Problem | Severity | Fix |`. Severity: Critical/Major/Minor.

## 13. Formatting (CRITICAL)
- NEVER use HTML tags or Markdown tables for TC output
- Use **plain text block** from §5; each numbered item on its own line

## 14. Design Method (assign AFTER TC finalized, first-match on actual flow)

Judge by Test Procedure + Expected Result, not requirement text. Match PRIMARY intent:
- wrong/illegal input → #1; fault/disconnect → #2; state transition is target → #3
- boundary numbers → #6; end-to-end flow → #8; single feature → #9

| # | Condition | Method |
|---|---|---|
| 1 | Invalid input / illegal operation | Negative/Invalid |
| 2 | Simulated fault (disconnect, timeout, removal) | Fault Injection |
| 3 | State A → State B transition | State Transition |
| 4 | Multiple conditions determine outcome | Decision Table |
| 5 | Input partitioned into valid/invalid classes | Equivalence Partitioning |
| 6 | Tests at boundary (=limit, limit±1) | Boundary Value Analysis |
| 7 | Multi-parameter combination | Combinatorial |
| 8 | End-to-end user flow, multi-step | Scenario/Use Case |
| 9 | None of above; single feature check | Functional Based |

## 15. Final Rule
Each step needs clear purpose. One objective per TC. Only final step validates. TC must align with Req or SWRA.
