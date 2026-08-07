## 0. Purpose
Balance SWE.6 (deterministic, reproducible, auditable, traceable, no FP) with reviewer needs. Runtime rules + worked examples live in `backend/prompt_builder.py`; this doc is the human summary.

## 1. Language
TC workbook fields: English only. Reasoning fields: Traditional Chinese allowed. No emoji.

## 2. Core Principles
- One TC = one verification objective; flow multi-step, validation single
- Final Step owns validation; represents Test Item executably
- TC reflects Req / SWRA; no vague wording, no hidden assumptions

## 3. Workflow (Generate)
1. Understand requirement (behavior, trigger, outcome)
2. Extract keywords → split dimensions (device / format / source / UI / state / env)
3. Identify sibling axes; one branch = one TC
4. Align Req ↔ SWRA ↔ Test Item
5. Define Test Item (single objective)
6. Build flow (Setup → Transition → Final Step)
7. Write ER (1:1 with steps); baseline if needed
8. Assign Design Method per §12
9. Self-check (§9)

## 4. Field Rules

### 4.1 Framework Establishment (prerequisite for Test Set)
Before writing ANY TC for a feature, establish the three-layer framework
project-wide in `framework.md`. The framework is the navigation map for the
entire TC writing campaign; it must exist before TC writing begins, and any
new RD must map into it (if no fit, update the framework first).

Forbidden:
- One Test Set per RD parent (defeats grouping — Test Set count ≈ TC count)
- A "Misc" / "General" / "Unclassified" set catching unrelated capabilities
- Ad-hoc Test Set names per TC

#### 4.1.1 Three Layers

**Layer 1 — Test Group**: the HMI module / feature name (e.g. `Media`,
`Bluetooth`, `Climate`). Almost always identical to the spec document title;
no judgement required. Written to the workbook.

**Layer 2 — Test Set**: capability cluster within the Test Group (e.g.
`General Anatomy`, `Playing Tab` for Media; `Pairing`, `Phone Book` for
Bluetooth). Written to the workbook.

**Layer 3 — Spec section grouping**: framework-internal grouping aligned
to the spec's own section structure (e.g. `MN1`, `PT1`, `BT1.9` for Media).
NEVER written to the workbook. Lives only in `framework.md` and serves four
downstream purposes (§4.1.4).

#### 4.1.2 Establishment Workflow

1. **Identify Layer 1** — read the spec document title. Most features make
   this obvious (e.g. `Media HMI Logic and Flow` → Test Group = `Media`).
2. **Draft Layer 2 candidates** — take the **intersection** of:
   - spec table of contents (how the spec author chose to chapter the feature)
   - RD analysis report grouping (how the upstream SWE.1/SWE.5 author chose
     to cluster requirements)
   When both sources agree on a cluster, it is a strong Layer 2 candidate.
   When they disagree, prefer the cluster shape that gives more even
   coverage (see §4.1.3).
3. **Draft Layer 3 grouping** — map each Layer 2 to the spec sections it
   covers, using the spec's own section IDs (not invented labels).
4. **Sanity check Layer 2 granularity** — apply §4.1.3 anti-patterns; adjust
   Layer 2 boundaries (merge or split) before locking framework.
5. **Lock and write `framework.md`** — only Layer 1 + Layer 2 + Layer 3
   table. Do NOT list individual RD items at this stage; they enter during
   TC writing.

#### 4.1.3 Layer 2 Granularity — anti-patterns

The two failure modes that consistently break Test Set utility:

- **Too granular** — each RD parent becomes its own Test Set. The Test Set
  column ends up being a near-duplicate of the TC ID column, destroying its
  index value.
- **Too coarse** — a "Misc" / "General" / "Unclassified" set absorbs
  unrelated capabilities. Reviewers cannot use the Test Set column to
  navigate.

Decision test: "If I filter the workbook by this Test Set, do I get a
**meaningful cluster** of related TCs — not just one TC, and not the entire
workbook?" If no, adjust the Layer 2 boundary.

Practical sign of a healthy Layer 2: same Test Set implies a shared setup
pattern and a shared UI entry path.

#### 4.1.4 Why Layer 3 matters (even though it's not in the workbook)

Layer 3 is invisible in the deliverable but essential during TC writing.
Four downstream uses:

1. **TC sequencing** — TCs within the same Layer 3 should be written
   contiguously. Reviewers (and the TC author) avoid repeatedly switching
   spec chapters and RD groupings.
2. **Sibling identification** — RDs within the same Layer 3 are sibling
   candidates by default. When the prompt builder injects `## Sibling Rows`,
   Layer 3 membership is a strong prior signal.
3. **Coverage analysis** — Layer 3 is the unit of completeness check. "Have
   we covered every RD under PT1?" is answerable; "Have we covered every
   RD under Playing Tab?" mixes too many spec sections.
4. **Scope drift prevention** — when writing a TC, knowing the RD's Layer 3
   helps enforce §8.5 (Pre-Condition scope) and §8.2.1 (don't expand into
   sibling Reqs). Adjacent Layer 3 groups own adjacent behaviors; Layer 3
   makes that boundary visible.

#### 4.1.5 Workbook export

Only Layer 1 and Layer 2 appear in the workbook (as Test Group and Test Set
columns respectively). Layer 3 is documentation-internal; do not export it,
do not store it in a workbook column, do not concatenate it into the Test
Set name.

### 4.2 Test Set
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

### 4.3 Test Item / tc_title — three acceptable shapes
Length **2–14 words**. Pick whichever makes the scenario clearest:

- **(a) Arrow** — `Trigger → Outcome`. Use when causality is the point. Trigger MUST carry CONDITION / STATE, not bare action. ✓ `CarPlay connected → CP Media icon shown in App Drawer`
- **(b) Sentence** — `[Outcome] when [trigger]` / `[Object] [state] under [condition]`. Use when natural sentence reads more clearly. ✓ `CP Media icon displayed when CarPlay is connected`
- **(c) Scenario tag** — short noun phrase naming branch / data / env / boundary. **PREFERRED** when siblings differ only by data / env / branch — matches reviewer Excel template. The tag IS the distinguishing token. ✓ `Cold boot`, `Power Cycle`, `Upload supported video file type: .mp4`, `Upload unsupported video file type: .mov`, `Initial Sync = 5,000`

Forbidden: modals (`should`, `will`, `shall`), hedges (`properly`, `successfully`, `within reasonable time`).

**Sibling-distinction:** two sibling tc_titles that read identically (or differ only `displayed` vs `hidden`) = FAIL.

### 4.4 Pre-Condition
Starting **state / environment** only. Never actions, checks, reads, data-presence.

**Allowed types:** external env (`GPS signal is available.`); hardware / peripheral (`A PBAP-supported device is available.`); feature initial state (`Bluetooth is enabled.`); system version / mode (`Dev / Pre-Prod build only.`).

**Forbidden:** system defaults (`HU is powered on.`); feature under test as premise (`Dealer Mode is accessible.`); actions (`USB inserted and ready.` — belongs in Procedure); step-controlled state (`Device is not connected.`).

Self-test: requires *do / check / confirm* → NOT a Pre-Condition.

### 4.5 Input Test Data — field ownership
Data belongs to exactly one field. Do not duplicate the same value across
Pre-Condition, Input Test Data, and Procedure.

1. **Environment data** (file, device, external signal source) → Pre-Condition
   - ✓ `1. A USB drive containing valid .mp4 video files is connected`
2. **Interaction data** (button, option, UI value selected by the tester) → Procedure step
   - ✓ `Press "Screen Off" button`
3. **Independent dataset** (CAN signal values, boundary values, batch test data) → Input Test Data
   - ✓ `CAN: VinLockStatus = 0x01`
   - ✓ `File size: 200 MB / 201 MB`
   - ✓ `Test files: video_5MB.mp4, video_300MB.mp4`

If the data already belongs to Pre-Condition or Procedure, set Input Test Data
to `NA`. `NA` is valid for many UI-operation TCs and does not fail self-check.

### 4.6 Sibling Awareness
On `## Sibling Rows` injection, output `duplicate_of` (only if truly equivalent: same trigger+outcome+input+verification target) and `distinguishing_axis` `{"axis": "<trigger_state|input_data|timing|boundary|mode|none>", "delta": "<繁中一句, 含 tc_title 具體 token>"}`. Rule: `axis="none"` ⇔ `duplicate_of` set. Full contract in code.

## 5. Step Design

### 5.1 Executable & Clear Intent
Each step MUST be executable with clear intent. Intent is usually **self-evident** from action + target (`Press "Screen Off" button`). Add `... to ...` ONLY when the same UI serves multiple purposes, the step sets up a non-obvious precondition, or the target is opaque (raw AT, deep menu, internal signal). Do NOT pad every step with `to ...`.

**Forbidden verbs** as MAIN verb: `observe`, `observe whether`, `see if`, `check whether`, `confirm whether`, `verify`, `watch`, `monitor`, `inspect`. They defer judgement to the tester.

`verify` exception: allowed in purpose clause (`... to verify that ...`), never as main verb.

**Preferred verbs** (each + concrete observable target — UI / log / signal / count / state): `Check that`, `Confirm that`, `Read`, `Record`, `Compare`.

- ✗ `Verify the BT icon is displayed.`
- ✓ `Check that the CarPlay home screen is displayed on the HU.`

### 5.2 Step Length & Intent Level
Manage step wording by role, not by a single hard length limit.

**A. Normal setup / transition step**
- Target length: ≤ 12 words
- Action + target only; no purpose clause unless §5.1 exception applies
- ✓ `Insert USB device`
- ✗ `Press the Screen Off button on the head unit so that we can later enter Eng Mode by pressing the corners`

**B. Final Step (§5.5 verification owner)**
- Must include verification intent: `check that ...`, `to verify ...`, or `... to check ...`
- Length may extend to ≤ 18 words because it carries action + check target
- ✓ `Select CarPlay icon in Menu Bar and check that the CarPlay interface is displayed on the HU`

**C. Setup step that requires intent (§5.1 exception)**
- If UI is multi-purpose, the step establishes a non-obvious precondition, or
  the target is opaque, keep a short `to ...` clause; length may extend to ≤ 18 words
- ✓ `Press and Hold the top right and bottom left corners of the screen for 5 seconds to enter Dealer Mode`
- ✓ `Mount tmpfs of 1 GB to occupy actual RAM`

Decision test: if removing the `to ...` clause still leaves the next step
unambiguous, remove it. Do not repeat previous state, explain background, or
write conditional branches inside one TC.

### 5.3 Standard Setup Snippets
Project-level repeated setup steps SHOULD be managed as constants and reused
verbatim. Case, hyphenation, spacing, and wording variants are not allowed to
spread across TCs.

Examples (project-specific constants must be maintained together with tooling):
- `ENTER_DEALER_MODE`: `Press and Hold the top right and bottom left corners of the screen for 5 seconds to enter Dealer Mode`
- `ENTER_ENG_MODE`: `Press and Hold the top left and bottom right corners of the screen for 5 seconds to enter Eng Mode`
- `SCREEN_OFF`: `Press H/K "Screen Off" button to turn off the HU screen`
- `ENTER_APP_DRAWER`: `Press "Apps" on Menu Bar to open App Drawer`

Tooling (prompt builder / linter / export normalizer) should enforce the same
canonical strings. When adding a constant, update both this instruction and the
tooling constant table; do not introduce ad-hoc variants.

### 5.4 Tooling / CLI Step Format
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

### 5.5 Final Step (Verification Owner)
Final Step alone reveals what is checked, mapping Test Item outcome. Include ACTION + check target. Use §5.1 preferred verbs.

- ✗ `Select the CarPlay icon.` (no check target)
- ✓ `Select CarPlay icon in Menu Bar and check that the CarPlay interface is displayed on the HU.`

### 5.6 Baseline Comparison
State change or boundary → establish **baseline (before)** AND check **outcome (after)** in the same TC.

**Baseline wording**: Use the word `baseline` only in the comparison step in the final ER, not in the recording step. The recording step describes what is read; the comparison step is where the baseline label belongs. Avoid the redundant pattern `record the baseline ... as baseline`.

- ✗ `Read and record the baseline A2DP and HFP status as baseline`
- ✓ Recording step: `Locate the phone and record its A2DP and HFP status shown in the list`
- ✓ Comparison ER: `The phone's HFP status remains the same as recorded in step 2`

### 5.7 One Objective
Steps = Setup / Transition / Verification (final only). Earlier failure = setup not reached → keep. Independent feature → split.

**One trigger → multiple consequential outcomes belong in ONE TC, not split.** The trigger is the verification unit; outcomes that necessarily follow from the same trigger are facts to be checked, not separate TCs. Cover them as multiple ER lines.

- ✗ Splitting `Disconnect CarPlay → Phone icon restored` and `Disconnect CarPlay → BT paging starts` into two TCs (same trigger, both consequences of the same disconnect)
- ✓ One TC `User disconnects CarPlay → native restored and BT paging started` with both ER lines
- Split criterion remains: different **triggers**, different **inputs**, different **scopes** — not different outcomes of the same trigger.

## 6. Expected Results
1:1 aligned with steps; observable, judgeable; no `normal` / `as expected`. Setup / transition may have ER to prove condition established. Final ER covers the **complete** Test Item outcome (partial = incomplete).

**No modal verbs in ER**: `shall`, `will`, `should`, `would` are RD source-document
language and MUST be transformed into passive observable statements in TC ER.

- ✗ `The Main Menu Bar shall be visible` (RD original)
- ✓ `The Main Menu Bar is displayed on the Media screen` (TC ER)
- ✗ `Tab Area will display content corresponding to the selected Tab`
- ✓ `The Tab Area shows content corresponding to the selected Tab Button`

### 6.1 Multi-Phase ER Layout
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
6. Press "Screen Off" button
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

## 7. False Pass / False Fail
- **FP:** Split when independent items / branches exist (formats, devices, protocols, UI paths). Enumerated supported items → ALWAYS pair with at least one unsupported negative TC.
- **FF:** Include setup / transition; don't assume hidden state.

## 8. Requirement Alignment

### 8.1 Test Item ↔ Requirement
Traces to Req or SWRA. Conflict → Req wins; flag RD. TC checking neither = invalid.

### 8.2 RD Decomposition Discipline
TC authors MUST NOT re-decompose, consolidate, or invent RD items. The
upstream RD analysis report (e.g. SWE.1 / SWE.5) is authoritative on
"what counts as a requirement unit". TC authors decide only "how many
verifications a unit needs".

This discipline has two directions — both must hold.

#### 8.2.1 Do not expand scope into sibling Reqs
If RD has split a behavior into a separate Requirement ID elsewhere in the
analysis report, the current TC MUST NOT cover that behavior.

- Check the RD analysis report BEFORE deciding TC scope
- A TC under Req-A should not test what Req-B already owns
- When in doubt, narrow the TC to the literal text of the current Req only
- Reasoning field should explicitly cite which sibling Req IDs cover the
  out-of-scope behaviors

**Workflow before writing each TC:**
1. Read the current Req's literal text
2. Scan the RD analysis report for sibling Reqs with related behaviors
3. If a sibling Req owns a behavior, exclude it from the current TC
4. Note the delegation in the `reasoning` field

Anti-pattern: cramming related behaviors into one TC "for completeness" —
this creates duplicate traceability and double-test maintenance burden.

- ✗ TC under `Display Tab Buttons` testing tab label content (`-005` owns this)
- ✗ TC under `Display Tab Buttons` testing Browse availability (`-057` owns this)
- ✓ TC under `Display Tab Buttons` testing only the existence of Tab Buttons region

#### 8.2.2 Do not consolidate — RD sub-id ≠ TC count
A single RD sub-id may need to be covered by multiple TCs when its
description bundles independent partial failures. The RD is the requirement
unit; the TC is the verification unit; the two counts need not be 1:1.

**Decision test for a given RD sub-id**: apply the §8.3 stress-test —
"If only part of the behaviour fails, is my pass/fail verdict still
unambiguous?" If two independent partial failures both land on `fail` via
the same TC, split into multiple TCs, all tracing to the same RD sub-id.

- ✓ One RD sub-id "Manual Group Switch Required" describing both
  (a) no-auto-switch when last song ends and (b) user-selected switch
  succeeds → 2 TCs, both trace to that sub-id
- ✗ Merging the two facets into one TC with multi-line ER "to honour the
  RD's single sub-id" — this bundles two independent partial failures
  (§7, §8.3)

**Inverse direction is forbidden**: TC authors must not merge multiple RD
sub-ids into one TC. RD-level consolidation belongs to the RD authors,
not the TC authors (§8.2.1).

**Split condition when a sub-id bundles controls**: the same physical/logical
control element → keep one TC with a multi-row ER; different control entities →
split into independent TCs; independent partial failures under one sub-id →
split and record.

**Workbook handling**: when one RD sub-id yields multiple TCs, both TCs
list the same `Requirement or Design ID`; TC IDs (`{project}-{abbr}-{NNN}`,
§10.3) remain independently sequenced.

### 8.3 Keyword Decomposition (sibling axes — each = 1 TC)
Format / type (pair supported + unsupported); device / source / protocol; boundary (=limit, limit±1, =0); negative / invalid; concurrency / interruption; persistence (reboot); **environment** (`Cold boot` / `Power Cycle` / `Low memory` / `Network loss` — prepend ONE env-establishing step, re-run the verification); mode / role / permission.

**One Verification Point per TC:** if two *different* partial failures both land on "fail" via your TC, you are bundling — split. Stress-test: *"If only part of the behaviour fails, is my pass/fail verdict still unambiguous?"*

### 8.4 No Fabrication

#### 8.4.1 No data fabrication
Never invent a value the source did not state (numbers, thresholds, timeouts, sizes, durations, retry counts, default states, file names, identifiers, error codes, ordering rules).

- ✗ `download limit = 20`, `5s timeout` (when source silent)
- ✓ `<configured limit>`, "value defined in spec"
- Domain constants OK (BT PIN `0000`, HTTP `200 OK`); ambiguous source → preserve ambiguity.

#### 8.4.2 No scope fabrication
Do not test what the current spec does not own. If a behavior is defined in
a referenced external spec (e.g. Menu Bar HMI Logic referenced by Media HMI),
that behavior belongs to its own SWE requirements, not the current one.

- ✗ MEDIA Req cites `1 – Main Menu Bar` → testing Menu Bar's ICS/Nav config rules
- ✓ MEDIA Req cites `1 – Main Menu Bar` → testing only its presence on the Media screen

**Decision test**: "Is the rule I'm about to test defined in the spec the
current Req traces to, or in a referenced external spec?"
- Defined in current Req's spec → in scope
- Defined only in external spec → out of scope, belongs to that spec's owner

If the external spec has no parallel SWE requirements in the project (true
coverage gap), surface it as a coverage hole in `reasoning` — do NOT silently
absorb it into the current TC.

### 8.5 Pre-Condition Scope Drift
A Pre-Condition entry is valid only if it is a trigger condition the current
TC directly verifies. Environmental stability conditions owned by other RDs
do NOT belong in Pre-Condition — testers naturally ensure the environment is
stable before execution.

Exception: if the state itself is the spec-defined trigger condition for the
TC, it IS a valid Pre-Condition.

**Decision test**: "Is this state a trigger condition the TC directly
verifies, or just an implicit environment-stability premise needed for the
test to run?" Former → Pre-Condition. Latter → drop.

- ✗ `Browse Tab anatomy TC` writes "USB catalog has finished building" in
  Pre-Condition — catalog behavior is owned by BT1.9 / `COM-070~073`
  (implicit environment premise, belongs to another RD)
- ✗ `Track list popup` internal-behavior TC (e.g. cursor position, view
  reset) writes "USB catalog has finished building" — Tracks button
  availability is owned by PLA-011; catalog state belongs to another RD
- ✓ `Tracks button available state` writes "USB catalog has finished
  building" — catalog state IS the spec-defined trigger condition the TC
  directly verifies (SS4.2 dependency)
- ✗ `audio file is short enough to end during continuous scrolling` —
  test-implementation convenience, not a spec trigger; testers naturally
  prepare suitable test material

### 8.6 Spec Reference Hierarchy
When a traceability index export and the original spec source disagree, the
**original spec source wins**. Do not retract a requirement merely because it is
absent from the index export — check the source spec directly first. TC scope is
bounded by the literal spec section it verifies; behaviors from external or
adjacent specs must not be pulled in unless the current RD explicitly references
them.

### 8.7 Cross-Domain Behavioral Patterns
Feature-agnostic rules that hold across domains:

#### 8.7.1 Spec-sourced thresholds
Every trigger / release threshold MUST come from the spec and appear as a
**concrete value** in the Pre-Condition, never vague language ("in motion",
"approximately"). General form: `<condition> >= <trigger value>` to trigger,
`<condition> <= <release value>` to release, each citing its Req ID.

#### 8.7.2 Disambiguate similar operations
Semantically close operations (cancel vs stop, pause vs mute) MUST have their
end states distinguished in the ER, each citing its Req ID; the ER must not
state only a shared vague outcome.

#### 8.7.3 Variant label overrides
Market / variant-specific UI label overrides MUST be applied consistently across
all related steps, noting the source requirement (e.g. `<variant-ref>`).

#### 8.7.4 Selectable-but-styled
A visual state (greyed-out, dimmed) does NOT imply non-operability; the ER must
not assert operability that contradicts the spec. Follow the behavior the spec
explicitly states.

## 9. Self-Check (before emitting each TC)
1. Test Set: noun phrase, capability-level, matches `framework.md`, no Test Group prefix, consistent spelling, no `Unclassified` / `Misc` (§4.1, §4.2)
2. tc_title: one of 3 shapes, 2–14 words, sibling token visible, no modals (§4.3)
3. Pre-Condition state/env only (§4.4); each entry is a spec trigger condition, not an implicit environment-stability premise (§8.5)
4. Input Test Data field ownership correct, duplicate data moved to PC / Procedure or `NA` (§4.5)
5. Steps executable; no forbidden verbs (§5.1); Final Step owns verification (§5.5)
6. Step length and intent level fit normal / final / necessary-intent categories (§5.2)
7. Standard setup snippets reused verbatim when applicable (§5.3)
8. CLI / tooling steps use description + `$` command format (§5.4)
9. Baseline when before/after needed (§5.6)
10. Procedure ↔ ER 1:1; ER observable; no modal verbs in ER; complete outcome covered (§6); multi-phase ER layout used when needed (§6.1)
11. No FP / FF; supported paired with negative (§7)
12. Traces to Req/SWRA (§8.1); respects RD upstream decomposition without expanding into siblings (§8.2.1); allows RD sub-id ≠ TC count when partial failures are independent (§8.2.2); no fabricated data (§8.4.1); no scope fabrication (§8.4.2)
13. Design Method assigned AFTER procedure finalized (§12)
14. No trailing period on any line of `pre_conditions` / `input_test_data` / `test_procedure` / `expected_result` (§11)
15. UI element labels use `"..."` double quotes, never `[...]` square brackets (§11)
16. `specification_reference` lists every spec section the TC directly verifies (§10.7)
17. Source spec wins over index export (§8.6); thresholds are spec-sourced concrete values, similar operations disambiguated in ER, variant labels applied consistently, styled elements not assumed inoperable (§8.7)

## 10. Tool-Specific Output Contract (workbook export, not ASPICE rules)

These are application-side requirements for writing back into the Excel template.
Validation enforces them; LLM output MUST comply.

### 10.1 Required output keys (snake_case)
Every TC JSON object MUST include all 10 keys: `tc_title`, `pre_conditions`,
`input_test_data`, `test_procedure`, `expected_result`, `specification_reference`,
`design_method`, `priority`, `split_flag`, `split_reason`. Top-level response
also carries `reasoning` (§10.4) and optional `keywords`, `duplicate_of`,
`distinguishing_axis`.

### 10.2 Priority — exactly P0 / P1 / P2 / P3
Per `docs/TEST_CASE_PRIORITY.md` rubric. Never `High` / `Medium` / `Low` / `NA`.

| Level | Scope |
|---|---|
| **P0** | Critical/core: safety, boot/recovery, connection, audio output, eCall, vehicle-critical CAN signal, data-loss risk |
| **P1** | Major user-facing functionality or key operational logic flow |
| **P2** | Secondary/support functionality; failure has limited impact on major features |
| **P3** | Minor UI enhancement, low-impact customization, rare-use scenario, cosmetic detail |

### 10.3 TC ID format
Pattern: `{project}-{abbr}-{NNN}` — alphanumeric project + alphanumeric module
abbreviation + zero-padded 3-digit sequence (e.g. `PROJ-DM-001`). IDs MUST be
monotonically increasing within the same `{project}-{abbr}` group; the
generator handles assignment, the LLM does not emit `tc_id`.

### 10.4 `reasoning` field (Traditional Chinese, 2–5 sentences)
Top-level field on the response (not per-TC). Audit trail so reviewers can
align on the AI's interpretation without re-reading the source. Cover in
order (1 sentence each, skip if N/A):
1. **驗證目標** — core behavior / observable outcome under test.
2. **關鍵情境條件** — trigger preconditions / inputs / mode (echoes §4.3).
3. **為什麼這樣切** — if `tcs.length == 1`, justify why one TC suffices
   (do NOT write empty phrases like "不需拆分"); if `tcs.length ≥ 2`, cite
   the driving §-section (§4.3 / §7 / §8.3 …) and the split dimension.
4. **未涵蓋 / 刻意略過**(optional)— adjacent scenarios delegated to siblings
   or left for future review when spec is ambiguous. When a narrow-scope
   route is chosen (testing only the literal text of the current Req),
   explicitly list which sibling Req IDs cover the out-of-scope behaviors
   (per §8.2.1).

### 10.5 `test_procedure` minimum
At least 2 numbered steps (Setup → Verification minimum). Single-step TCs are
rejected — even smoke tests need an explicit verification step.

### 10.6 `duplicate_of` encoding
Digits-only row-number string (e.g. `"11"`, never `"row 11"` or `11` as int),
matching a sibling shown as `[row #11]` in the Sibling Rows section. Strict
equivalence required: same trigger + outcome + input + verification target.
When in doubt, omit the field.

### 10.7 `specification_reference` (workbook column)
String list of source spec references that anchor this TC. Required when
TC content depends on spec content (almost always).

**Format per entry**: `{spec_filename}_{section_id}`
- e.g. `Media_HMI_Logic_and_Flow_R1_SR24_Post_2A_(July_25th,_2023)_4.1`
- e.g. `Menu Bar and App Drawer HMI Logic and Flow R1 SR24 3A (September 11 2023)_2.5`

**Rules:**
- List every spec section the TC directly verifies or relies on as setup
- Use the SourceID format from SYS1 / Polarion when available
- Order from most-specific (lowest section number) to general
- Multiple specs allowed when TC spans multiple spec files
- Do NOT cite specs only used as background context (those go in `reasoning`)
- Do NOT cite RD analysis docs (SWE.1 / SWE.5) — those are not spec sources

## 11. Formatting
No HTML / Markdown tables in TC output. Plain numbered text; one item per line; blank line between fields.

**No trailing period** in `pre_conditions`, `input_test_data`, `test_procedure`, `expected_result` — strip the final `.` (or `。`) at the end of every line. Mid-sentence periods are kept (e.g. `Press button. Wait 5s` is fine; `Press button. Wait 5s.` is NOT). Applies to every numbered item.

**UI element labels use double quotes**, never square brackets. Applies to on-screen buttons, menu bar items, popup buttons, hard-key (H/K) buttons, tab names, and any literal label the tester reads off the UI. Display text and indicators that are values rather than tappable elements (e.g. source indicator `"AA"`, status text `"Music Muted"`) follow the same convention.

- ✓ `Press "Media" on Menu Bar`
- ✓ `Press H/K "Screen Off" button`
- ✓ `Press "OK" in the popup`
- ✓ `The source indicator displays "AA"`
- ✗ `Press [Media] on Menu Bar`
- ✗ `Press 'Screen Off' button` (single quotes)
- ✗ `Press <Apps> button` (angle brackets)

Square brackets `[...]` are reserved for placeholder syntax in this document only (e.g. `[Outcome] when [trigger]` in §4.3) and for sibling row markers (e.g. `[row #11]` in §10.6). They MUST NOT appear in TC output fields.

## 12. Design Method (assign AFTER TC finalized, first-match)

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

## 13. Final Rule
One objective per TC. Only final step validates. TC aligns with Req/SWRA.
