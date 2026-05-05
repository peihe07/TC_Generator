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

### 6.0 Test Set
Short English noun phrase, typically **1–3 words**. A Test Set captures the
functional capability inside the workbook Test Group; it is not a test
technique, procedure action, UI widget name, or sentence. Runtime ownership
and export behavior are defined in `TEST_SET_POLICY.md`.

- Map to SWRA / Req sub-feature capability, e.g. `Connection`, `Device List`, `System Information`, `ECU Certificate`
- Do **not** repeat the Test Group / module prefix already stored in the Test Group column. With Test Group = `Bluetooth`, use `Connection` / `Pairing` / `Power Control`, not `BT Connection` / `Bluetooth Pairing`
- Group by capability, not by sub-action. Different steps, UI paths, or sub-states of the same capability should share one Test Set
- Prefer broader shared capability when unsure; single-req Test Sets are allowed only for genuine outliers
- Same Test Set should imply a shared setup pattern and UI entry path where the requirements support it
- Workbook-imported Test Set values are hints only until Configure grouping or reviewer override confirms them
- Keep spelling case-sensitive and consistent across the project; no trailing spaces; no synonym drift
- Forbidden: action labels (`Verify XXX`, `Test Bluetooth`), full sentences, bracket tags, placeholders (`Req-xxx`, `Feature`, `Function` alone), empty / `None` / `Unclassified` / `Misc`
- ✓ `Bluetooth`, `System Information`, `ECU Certificate`, `Showroom Demo Mode`
- ✗ `Screenshot` and `Screen Shot` both used; ✗ `BT (Bluetooth)`; ✗ `Bluetooth Connection` when Test Group already equals `Bluetooth`

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

### 6.3 Input Test Data — field ownership
Data belongs to exactly one field. Do not duplicate the same value across
Pre-Condition, Input Test Data, and Procedure.

1. **Environment data** (file, device, external signal source) → Pre-Condition
   - ✓ `1. A USB drive containing valid .mp4 video files is connected`
2. **Interaction data** (button, option, UI value selected by the tester) → Procedure step
   - ✓ `Press [Screen Off] button`
3. **Independent dataset** (CAN signal values, boundary values, batch test data) → Input Test Data
   - ✓ `CAN: VinLockStatus = 0x01`
   - ✓ `File size: 200 MB / 201 MB`
   - ✓ `Test files: video_5MB.mp4, video_300MB.mp4`

If the data already belongs to Pre-Condition or Procedure, set Input Test Data
to `NA`. `NA` is valid for many UI-operation TCs and does not fail self-check.

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

### 7.8 Standard Setup Snippets
Project-level repeated setup steps SHOULD be managed as constants and reused
verbatim. Case, hyphenation, spacing, and wording variants are not allowed to
spread across TCs.

Examples (project-specific constants must be maintained together with tooling):
- `ENTER_DEALER_MODE`: `Press and Hold the top right and bottom left corners of the screen for 5 seconds to enter Dealer Mode`
- `ENTER_ENG_MODE`: `Press and Hold the top left and bottom right corners of the screen for 5 seconds to enter Eng Mode`
- `SCREEN_OFF`: `Press H/K [Screen Off] button to turn off the HU screen`
- `ENTER_APP_DRAWER`: `Press [Apps] on Menu Bar to open App Drawer`

Tooling (prompt builder / linter / export normalizer) should enforce the same
canonical strings. When adding a constant, update both this instruction and the
tooling constant table; do not introduce ad-hoc variants.

### 7.9 Tooling / CLI Step Format
When a step requires shell, adb, CAN tooling, or another external command, use
a two-line format:

- Description line: numbered step, business-level action / intent
- Command line: starts with `$`, unnumbered, immediately under the description
- ER line: describes observable result; do not repeat the command string

Example:

Procedure:
```text
3. Mount a tmpfs of 1 GB to occupy actual RAM
   $ mount -t tmpfs -o size=1024M tmpfs /data/local/tmp/ramtest

4. Fill tmpfs with zero-filled blocks to consume memory
   $ dd if=/dev/zero of=/data/local/tmp/ramtest/blob bs=10M count=100
```

ER:
```text
3. tmpfs is mounted at /data/local/tmp/ramtest
4. Available memory has decreased
```

### 7.10 Step Length & Intent Level
Manage step wording by role, not by a single hard length limit.

**A. Normal setup / transition step**
- Target length: ≤ 12 words
- Action + target only; no purpose clause unless §7.1 exception applies
- ✓ `Insert USB device`
- ✗ `Press the Screen Off button on the head unit so that we can later enter Eng Mode by pressing the corners`

**B. Final Step (§7.5 verification owner)**
- Must include verification intent: `check that ...`, `to verify ...`, or `... to check ...`
- Length may extend to ≤ 18 words because it carries action + check target
- ✓ `Select CarPlay icon in Menu Bar and check that the CarPlay interface is displayed on the HU`

**C. Setup step that requires intent (§7.1 exception)**
- If UI is multi-purpose, the step establishes a non-obvious precondition, or
  the target is opaque, keep a short `to ...` clause; length may extend to ≤ 18 words
- ✓ `Press and Hold the top right and bottom left corners of the screen for 5 seconds to enter Dealer Mode`
- ✓ `Mount tmpfs of 1 GB to occupy actual RAM`

Decision test: if removing the `to ...` clause still leaves the next step
unambiguous, remove it. Do not repeat previous state, explain background, or
write conditional branches inside one TC.

## 8. Expected Results
1:1 aligned with steps; observable, judgeable; no `normal` / `as expected`. Setup / transition may have ER to prove condition established. Final ER covers the **complete** Test Item outcome (partial = incomplete).

### 8.3 Multi-Phase ER Layout
When Procedure includes an environment-establishment phase (fault injection,
boundary setup, stress setup) and then the main verification phase:

- Separate phases with one blank line
- Keep 1:1 alignment with Procedure steps
- If the final verification must list sub-items, use `a./b./c.` sublevels and `-` bullets

Example:

```text
Procedure:
1. Access adb shell
2. Check current RAM usage
3. Mount tmpfs of 1 GB
4. Fill tmpfs to consume RAM
5. Re-check available memory
6. Press [Screen Off] button
7. Enter Dealer Mode
8. Select System Information

ER:
1. adb shell is accessed
2. RAM usage is visible
3. tmpfs is mounted at /data/local/tmp/ramtest
4. tmpfs is populated
5. Available memory has decreased

6. HU screen is OFF
7. Dealer Mode page is displayed
8. System Information includes:
   a. Radio Part Information
      - Hardware part number
      - Software version number
   b. SDAR Information
      - SDAR hardware version
      - SDAR firmware version
```

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
1. Test Set: noun phrase, capability-level, no Test Group prefix, consistent spelling, no `Unclassified` / `Misc` (§6.0)
2. tc_title: one of 3 shapes, 2–14 words, sibling token visible (§6.1)
3. Pre-Condition state/env only; Input Test Data field ownership correct, duplicate data moved to PC / Procedure or `NA` (§6.2-6.3)
4. Steps executable; no forbidden verbs; Final Step owns verification (§7.1, §7.5)
5. Standard setup snippets reused verbatim when applicable (§7.8)
6. CLI / tooling steps use description + `$` command format (§7.9)
7. Step length and intent level fit normal / final / necessary-intent categories (§7.10)
8. Baseline when before/after needed (§7.6)
9. Procedure ↔ ER 1:1; ER observable; complete outcome covered; multi-phase ER layout used when needed (§8, §8.3)
10. No FP / FF; supported paired with negative (§9)
11. Traces to Req/SWRA; no fabricated data (§10)
12. Design Method assigned AFTER procedure finalized (§15)
13. No trailing period on any line of `pre_conditions` / `input_test_data` / `test_procedure` / `expected_result` (§13)

## 12. Tool-Specific Output Contract (workbook export, not ASPICE rules)

These are application-side requirements for writing back into the Excel template.
Validation enforces them; LLM output MUST comply.

### 12.1 Required output keys (snake_case)
Every TC JSON object MUST include all 9 keys: `tc_title`, `pre_conditions`,
`input_test_data`, `test_procedure`, `expected_result`, `design_method`,
`priority`, `split_flag`, `split_reason`. Top-level response also carries
`reasoning` (§12.4) and optional `keywords`, `duplicate_of`,
`distinguishing_axis`.

### 12.2 Priority — exactly P0 / P1 / P2 / P3
Per `docs/test_case_priority.md` rubric. Never `High` / `Medium` / `Low` / `NA`.

| Level | Scope |
|---|---|
| **P0** | Critical/core: safety, boot/recovery, connection, audio output, eCall, vehicle-critical CAN signal, data-loss risk |
| **P1** | Major user-facing functionality or key operational logic flow |
| **P2** | Secondary/support functionality; failure has limited impact on major features |
| **P3** | Minor UI enhancement, low-impact customization, rare-use scenario, cosmetic detail |

### 12.3 TC ID format
Pattern: `{project}-{abbr}-{NNN}` — alphanumeric project + alphanumeric module
abbreviation + zero-padded 3-digit sequence (e.g. `PROJ-DM-001`). IDs MUST be
monotonically increasing within the same `{project}-{abbr}` group; the
generator handles assignment, the LLM does not emit `tc_id`.

### 12.4 `reasoning` field (Traditional Chinese, 2–5 sentences)
Top-level field on the response (not per-TC). Audit trail so reviewers can
align on the AI's interpretation without re-reading the source. Cover in
order (1 sentence each, skip if N/A):
1. **驗證目標** — core behavior / observable outcome under test.
2. **關鍵情境條件** — trigger preconditions / inputs / mode (echoes §6.1).
3. **為什麼這樣切** — if `tcs.length == 1`, justify why one TC suffices
   (do NOT write empty phrases like "不需拆分"); if `tcs.length ≥ 2`, cite
   the driving §-section (§6.1 / §9 / §10.2 …) and the split dimension.
4. **未涵蓋 / 刻意略過**（optional）— adjacent scenarios delegated to siblings
   or left for future review when spec is ambiguous.

### 12.5 `test_procedure` minimum
At least 2 numbered steps (Setup → Verification minimum). Single-step TCs are
rejected — even smoke tests need an explicit verification step.

### 12.6 `duplicate_of` encoding
Digits-only row-number string (e.g. `"11"`, never `"row 11"` or `11` as int),
matching a sibling shown as `[row #11]` in the Sibling Rows section. Strict
equivalence required: same trigger + outcome + input + verification target.
When in doubt, omit the field.

## 13. Formatting
No HTML / Markdown tables in TC output. Plain numbered text; one item per line; blank line between fields.

**No trailing period** in `pre_conditions`, `input_test_data`, `test_procedure`, `expected_result` — strip the final `.` (or `。`) at the end of every line. Mid-sentence periods are kept (e.g. `Press button. Wait 5s` is fine; `Press button. Wait 5s.` is NOT). Applies to every numbered item.

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
