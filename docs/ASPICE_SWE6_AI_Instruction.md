## 0. Purpose
Balance SWE.6 (deterministic, reproducible, auditable, traceable, no FP) with reviewer needs. Runtime rules + worked examples live in `backend/prompt_builder.py`; this doc is the human summary.

## 1. Language
TC workbook fields: English only. Reasoning fields: Traditional Chinese allowed. No emoji.

## 2. Core Principles
- One TC = one verification objective; flow multi-step, validation single
- Final Step owns validation; represents Test Item executably
- TC reflects Req / SWRA; no vague wording, no hidden assumptions

## 4. Workflow (Generate)
1. Understand requirement (behavior, trigger, outcome)
2. Extract keywords → split dimensions (device / format / source / UI / state / env)
3. Identify sibling axes; one branch = one TC
4. Align Req ↔ SWRA ↔ Test Item
5. Define Test Item (single objective)
6. Build flow (Setup → Transition → Final Step)
7. Write ER (1:1 with steps); baseline if needed
8. Assign Design Method per §15
9. Self-check (§11)

## 6. Field Rules

### 6.1 Test Item / tc_title — three acceptable shapes
Length **2–14 words**. Pick whichever makes the scenario clearest:

- **(a) Arrow** — `Trigger → Outcome`. Use when causality is the point. Trigger MUST carry CONDITION / STATE, not bare action. ✓ `CarPlay connected → CP Media icon shown in App Drawer`
- **(b) Sentence** — `[Outcome] when [trigger]` / `[Object] [state] under [condition]`. Use when natural sentence reads more clearly. ✓ `CP Media icon displayed when CarPlay is connected`
- **(c) Scenario tag** — short noun phrase naming branch / data / env / boundary. **PREFERRED** when siblings differ only by data / env / branch — matches reviewer Excel template. The tag IS the distinguishing token. ✓ `Cold boot`, `Power Cycle`, `Upload supported video file type: .mp4`, `Upload unsupported video file type: .mov`, `Initial Sync = 5,000`

Forbidden: modals (`should`, `will`), hedges (`properly`, `successfully`, `within reasonable time`).

**Sibling-distinction:** two sibling tc_titles that read identically (or differ only `displayed` vs `hidden`) = FAIL.

### 6.2 Pre-Condition
Starting **state / environment** only. Never actions, checks, reads, data-presence.

**Allowed types:** external env (`GPS signal is available.`); hardware / peripheral (`A PBAP-supported device is available.`); feature initial state (`Bluetooth is enabled.`); system version / mode (`Dev / Pre-Prod build only.`).

**Forbidden:** system defaults (`HU is powered on.`); feature under test as premise (`Dealer Mode is accessible.`); actions (`USB inserted and ready.` — belongs in Procedure); step-controlled state (`Device is not connected.`).

Self-test: requires *do / check / confirm* → NOT a Pre-Condition.

### 6.3 Input
Explicit deterministic value (button / option / value / file / trigger) or `NA`.

### 6.4 Sibling Awareness
On `## Sibling Rows` injection, output `duplicate_of` (only if truly equivalent: same trigger+outcome+input+verification target) and `distinguishing_axis` `{"axis": "<trigger_state|input_data|timing|boundary|mode|none>", "delta": "<繁中一句, 含 tc_title 具體 token>"}`. Rule: `axis="none"` ⇔ `duplicate_of` set. Full contract in code.

## 7. Step Design

### 7.1 Executable & Clear Intent
Each step MUST be executable with clear intent. Intent is usually **self-evident** from action + target (`Press [Screen Off] button`). Add `... to ...` ONLY when the same UI serves multiple purposes, the step sets up a non-obvious precondition, or the target is opaque (raw AT, deep menu, internal signal). Do NOT pad every step with `to ...`.

#### 7.1.1 Forbidden Verbs
**Never** as MAIN verb: `observe`, `observe whether`, `see if`, `check whether`, `confirm whether`, `verify`, `watch`, `monitor`, `inspect`. They defer judgement to the tester.

`verify` exception: allowed in purpose clause (`... to verify that ...`), never as main verb.

**Preferred verbs** (each + concrete observable target — UI / log / signal / count / state): `Check that`, `Confirm that`, `Read`, `Record`, `Compare`.

- ✗ `Verify the BT icon is displayed.`
- ✓ `Check that the CarPlay home screen is displayed on the HU.`

### 7.5 Final Step (Verification Owner)
Final Step alone reveals what is checked, mapping Test Item outcome. Include ACTION + check target. Use §7.1.1 preferred verbs.

- ✗ `Select the CarPlay icon.` (no check target)
- ✓ `Select CarPlay icon in Menu Bar and check that the CarPlay interface is displayed on the HU.`

### 7.6 Baseline Comparison
State change or boundary → establish **baseline (before)** AND check **outcome (after)** in the same TC.

### 7.7 One Objective
Steps = Setup / Transition / Verification (final only). Earlier failure = setup not reached → keep. Independent feature → split.

## 8. Expected Results
1:1 aligned with steps; observable, judgeable; no `normal` / `as expected`. Setup / transition may have ER to prove condition established. Final ER covers the **complete** Test Item outcome (partial = incomplete).

## 9. False Pass / False Fail
- **FP:** Split when independent items / branches exist (formats, devices, protocols, UI paths). Enumerated supported items → ALWAYS pair with at least one unsupported negative TC.
- **FF:** Include setup / transition; don't assume hidden state.

## 10. Requirement Alignment

### 10.1 Test Item ↔ Requirement
Traces to Req or SWRA. Conflict → Req wins; flag RD. TC checking neither = invalid.

### 10.2 Keyword Decomposition (sibling axes — each = 1 TC)
Format / type (pair supported + unsupported); device / source / protocol; boundary (=limit, limit±1, =0); negative / invalid; concurrency / interruption; persistence (reboot); **environment** (`Cold boot` / `Power Cycle` / `Low memory` / `Network loss` — prepend ONE env-establishing step, re-run the verification); mode / role / permission.

**One Verification Point per TC:** if two *different* partial failures both land on "fail" via your TC, you are bundling — split. Stress-test: *"If only part of the behaviour fails, is my pass/fail verdict still unambiguous?"*

### 10.3 No Fabrication
Never invent a value the source did not state (numbers, thresholds, timeouts, sizes, durations, retry counts, default states, file names, identifiers, error codes, ordering rules).

- ✗ `download limit = 20`, `5s timeout` (when source silent)
- ✓ `<configured limit>`, "value defined in spec"
- Domain constants OK (BT PIN `0000`, HTTP `200 OK`); ambiguous source → preserve ambiguity.

## 11. Self-Check (before emitting each TC)
1. tc_title: one of 3 shapes, 2–14 words, sibling token visible (§6.1)
2. Pre-Condition state/env only; Input deterministic or `NA` (§6.2-6.3)
3. Steps executable; no forbidden verbs; Final Step owns verification (§7.1, §7.5)
4. Baseline when before/after needed (§7.6)
5. Procedure ↔ ER 1:1; ER observable; complete outcome covered (§8)
6. No FP / FF; supported paired with negative (§9)
7. Traces to Req/SWRA; no fabricated data (§10)
8. Design Method assigned AFTER procedure finalized (§15)

## 13. Formatting
No HTML / Markdown tables in TC output. Plain numbered text; one item per line; blank line between fields.

## 15. Design Method (assign AFTER TC finalized, first-match)

| Condition | Method |
|---|---|
| Invalid input / illegal op | Negative / Invalid |
| Simulated fault (disconnect, timeout) | Fault Injection |
| State A → State B transition | State Transition |
| Multiple conditions → outcome | Decision Table |
| Input partitioned valid / invalid | Equivalence Partitioning |
| Boundary (=limit, limit±1) | Boundary Value Analysis |
| Multi-parameter combination | Combinatorial |
| End-to-end flow, ≥3 features | Scenario / Use Case |
| Single feature check | Functional Based |

Tie-break: State Transition = state-change focus; Scenario = ≥3 steps crossing features; Functional = 1–2 steps single feature.

## 16. Final Rule
One objective per TC. Only final step validates. TC aligns with Req/SWRA.
