## 0. Purpose
Balance SWE.6 (deterministic, reproducible, auditable, traceable, no FP) with reviewer needs (explicit flow, clear final verification).

## 1. Language
TC: English; Analysis: Traditional Chinese; No emoji

## 2. Core Principles
- One TC = one verification objective; flow multi-step, validation single
- Final Step owns validation; represents Test Item executably
- No vague wording/hidden assumptions; TC reflects Req/SWRA

## 3. Modes
Generate TC / Review Existing TC

# Mode 1 — Generate

## 4. Workflow
1) Understand requirement (behavior, trigger, outcome)
2) Extract keywords → split dimensions (device/format/source/UI/state)
3) Break down behaviors (main vs supporting)
4) Align Req ↔ SWRA ↔ Test Item
5) Define Test Item (single objective, scenario)
6) Build flow (Setup → Transition → Final Step)
7) Write ER (1:1), baseline if needed
8) Assign Design Method per §15
9) Self-check (§11)

## 5. Template (pattern: `TC[N]: [Scenario]`; blank line between fields)

```
TC1: First-time CarPlay pairing

Test Item:
First-time BT pairing with CarPlay phone → HU identifies phone as CarPlay-capable

Pre-Condition:
1. CarPlay-capable phone available.
2. Phone never paired with HU.

Input:
NA

Test Procedure:
1. Enable BT on the phone.
2. On HU, open BT settings and select the phone.
3. Complete BT pairing.
4. Check that HU recognizes phone as CarPlay-capable.

Expected Result:
1. Phone BT enabled and discoverable.
2. HU starts pairing.
3. Pairing completed.
4. HU identifies phone as CarPlay-capable.

Design Method:
Scenario/Use Case
```

## 6. Field Rules

### 6.1 Test Item
- Format: `[Trigger] → [Outcome]` — SHORT, **both sides MUST be 3–8 words** (hard limit)
- Drop articles (a/the), modals (should/will), hedges (properly/successfully)
- One behavior; scenario tag in TC title when requirement splits into branches

✓ `Select CarPlay icon → CarPlay interface displayed`
✗ `When user selects CarPlay icon, system should display interface within reasonable time.` — filler
✗ `Android Auto off, phone via BT A2DP → BT music plays through HU` — too long

**Trigger must carry CONDITION/STATE, not just a bare action.** The same
action under different states yields different outcomes — that is why
sibling TCs exist. A bare-action trigger leaves the reader guessing
what state the action runs against.

✗ `Select CarPlay icon → CarPlay interface displayed`
   — under what state? phone connected via USB? paired but not connected?
     no phone paired at all? Each yields a different outcome.
✓ `Select CarPlay icon with iPhone connected via USB → CarPlay interface displayed`
✓ `Tap CarPlay icon with no phone paired → connection prompt shown`
✓ `With BT off, press Connect → connection error displayed`

Bare-action triggers are acceptable ONLY when there is genuinely no
relevant state (e.g. cold-boot smoke test). When the arrow form forces
telegraphic compression that hides the condition, switch to a natural
sentence: `CarPlay UI shown when icon tapped with iPhone over USB`.

**Split example** (same req, format dimension → multi TCs; consistent tag style):
- `TC1: Play .mp4` — `Play .mp4 → .mp4 plays on HU`
- `TC2: Play .avi` — `Play .avi → .avi plays on HU`
- `TC3: Play .mpg` — `Play .mpg → .mpg plays on HU`

Tag = short phrase for the branch (format/device/source/state/UI path).

### 6.2 Pre-Condition
Starting **state/environment** only, describing the minimum context that must
exist before the test starts. Never actions, checks, reads, or data-presence.

**Allowed types** — 4 categories, each with a decision criterion:

| Type | Decision criterion | Example |
|---|---|---|
| External environment | DUT cannot control it; test equipment / environment must provide it | `GPS signal is available.` / `FM/AM signal generator is ready.` |
| Hardware / peripheral | Requires a specific physical device, accessory, or protocol support | `A PBAP-supported device is available.` / `A USB storage device is available.` |
| Feature initial state | To test feature B, feature A must be in a specific state | `Bluetooth is enabled.` |
| System version / mode | Specific build or mode required | `Dev / Pre-Prod build only.` |

**Forbidden types** — 5 categories to REJECT, each with the reason:

| Forbidden type | Why it is wrong | Example to REJECT |
|---|---|---|
| System-obvious baseline | Default system state, doesn't need listing | `The HU is powered on.` |
| Feature under test as premise | Turns the thing being tested into an assumption | `Dealer Mode is accessible.` |
| Action (not state) | Actions belong in Test Procedure | `USB or SD Card is inserted and ready.` |
| Step-controlled state | State is established by test steps, not pre-existing | `The device is not connected to the HU.` |
| Redundant system defaults | Restating obvious system state | `HU is powered on and Bluetooth is enabled.` |

**Self-test:** If a line requires the tester to *do*, *check*, or *confirm*
something → it is NOT a Pre-Condition.

### 6.3 Input
Explicit, deterministic (button/option/value/file/trigger) or NA.

### 6.4 Sibling Awareness (when same Requirement ID has multiple rows)

When the workbook has multiple rows under the **same Requirement ID**,
the prompt injects a `## Sibling Rows` section listing each peer as
`[row #N] <test_item>`. Two structured output fields make AI's reasoning
about those siblings explicit and reviewable:

**`duplicate_of`** (string, OPTIONAL — STRICT):
- Set to the row number digits of a sibling (e.g. `"11"`, no `row` /
  `#` prefix) **only** when this row is **truly equivalent** to that
  sibling — same trigger AND outcome AND input bucket AND verification
  target.
- Partial overlaps, similar Test Sets, or shared procedure steps DO NOT
  qualify. When in doubt, omit the field.
- Backend resolves whatever the model returns ("11" / "row #11" /
  legacy uuid) against the row's siblings; hallucinated values that
  match no sibling are dropped silently so the reviewer-side badge
  hides instead of showing misleading text.
- Reviewers see a `⊕ DUP→N` chip in the TC ID column + a red
  "重複於 row #N" card in the expanded panel. Deletion is reviewer-
  driven; the system never auto-merges.

**`distinguishing_axis`** (object, REQUIRED when siblings exist; OMIT
otherwise):
- Shape `{"axis": "<enum>", "delta": "<繁體中文一句話>"}`.
- `axis ∈ {trigger_state, input_data, timing, boundary, mode, none}`.
- `delta` MUST contain a concrete token (state name / value / mode /
  boundary keyword) that ALSO appears in this row's `tc_title`. Vague
  sentences like 「不同的驗證情境」 are rejected.
- Cross-rule: `axis="none"` ⇔ `duplicate_of` is set in the same
  response. Backend reconciles inconsistent output (conflict drops
  `duplicate_of`, lone `duplicate_of` fills `axis="none"`, lone
  `axis="none"` without a sibling target is cleared).
- Reviewers see `⚖ 與 sibling 差異 (label) — delta` in the expanded
  panel; this is the audit trail for close-but-not-duplicate cases.

## 7. Step Design

### 7.1 Executable & Clear Intent (MANDATORY)
Each step MUST be executable, with clear intent the tester can follow without
guessing. Intent is usually **self-evident** from action + target
(`Press [Screen Off] button`, `Enable BT on the phone` — purpose obvious).

Add an explicit purpose clause (`... to ...`) **ONLY** when the action alone
leaves intent ambiguous — typically when:
- The same button / UI element serves different purposes in different contexts
- The step sets up a non-obvious precondition for a later step
- The target name doesn't describe its effect (e.g. raw AT commands, opaque
  menu paths, internal signal names)

Do NOT pad every step with `to ...` — forced purpose clauses on self-evident
actions are noise and reduce readability.

✓ `Press [Screen Off] button.` — intent self-evident, no clause needed
✓ `Enable BT on the phone.` — self-evident
✓ `Send AT+CGMI to query the manufacturer ID.` — opaque command, clause required
✓ `Navigate to Settings → Network → Wi-Fi to reach the SSID list.` — deep path, intent clarified
✗ `Press [Screen Off] button to turn off the screen.` — redundant, intent already obvious
✗ `Navigate to deep menu path X.` — why there? purpose unclear, needs clause

#### 7.1.1 Forbidden Verbs (hard rule)

The MAIN verb of a step decides whether the tester knows exactly what to do
and what to look at. Vague verbs defer judgement to the tester and violate
SWE.6 reproducibility.

**Forbidden as main verb** — each with the specific problem:

| Forbidden verb | Problem |
|---|---|
| `observe` | No specific target; tester doesn't know what to look at |
| `observe whether` | "Whether" pushes the pass/fail judgement onto the tester |
| `see if` | Same as above; no explicit judgement criterion |
| `check whether` | Should be `check that` + explicit criterion |
| `confirm whether` | Should be `confirm that` + explicit criterion |
| `verify` | Too broad; doesn't specify means (UI? log? value?) |
| `watch` / `monitor` / `inspect` | Passive verbs without a concrete check action |

**`verify` exception:** allowed in a purpose clause (`... to verify that
the phone is connected.`), never as the step's main verb.

**Preferred verbs** — each MUST be followed by a concrete observable target
(UI element, log line, signal value, count, state):

| Preferred verb | Usage |
|---|---|
| `Check` / `Check that` | Confirm UI / system state matches expectation |
| `Confirm` / `Confirm that` | Confirm a specific condition holds or event occurred |
| `Read` | Read and capture a concrete value |
| `Record` | Record a value for later comparison |
| `Compare` | Compare two concrete values |

✗ `Observe the screen.` ✗ `Verify the BT icon is displayed.`
✓ `Check that the CarPlay home screen is displayed on the HU.`

### 7.2 No Skipping / Step Types
Do not omit necessary steps. Supporting = establish condition (prevent FF); Transition = move to required state (pairing, navigation, dialog).

### 7.5 Final Step (Verification Owner)
**Final Step alone must reveal what is checked, mapping Test Item outcome.** Include ACTION + check target. Use §7.1.1 preferred verbs.

Test Item: `Select CarPlay icon → CarPlay interface displayed`
✓ `Select CarPlay icon in Menu Bar and check that the CarPlay interface is displayed on the HU.`
✗ `Select the CarPlay icon.` — no check target
✗ `... and verify the interface.` — forbidden verb

### 7.6 Baseline Comparison
State change or boundary → establish **baseline (before)** and check **outcome (after)**.
Example (max 5,000): Pair → Check HU = 5,000 (baseline) → Add contact → Sync → Check count = 5,000; new contact not imported (outcome)

### 7.7 One Objective
Steps = Setup / Transition / Verification (final only). Earlier failure = setup not reached → keep; = independent feature → split.

## 8. Expected Results
- 1:1 aligned with steps; observable, judgeable; no "normal/as expected"
- Setup/transition may have ER to prove condition established
- Final ER covers **complete** check objective (partial = incomplete)

✗ Only "upload success" when Test Item = upload + playback
✓ Both: file accepted AND playback starts

## 9. False Pass / False Fail
- **FP:** Split when independent items/branches exist. Multiple formats (.mp4, .avi, .mpg) checked individually. Same for devices, protocols, UI paths.
- **FF:** Include setup/transition; don't assume hidden state.

## 10. Requirement Alignment

### 10.1 Test Item ↔ Requirement
Traces to Req or SWRA. Conflict → Req wins; flag RD. TC checking neither = invalid.

### 10.2 Keyword Decomposition
Example: "max 60 records per BT device; first set kept"
→ `max 60` → boundary (=60, >60, <60); `first set` → order; `per BT device` → multi-device

**Branches** (each = 1 TC): unknown/private; before-vs-after; boundary (=/>/</=0); negative; concurrency; persistence (reboot).

**One Verification Point per TC** (critical — prevents over-stuffed scenarios):
Every TC must answer exactly ONE unambiguous pass/fail question. If two
*different* partial failures could both land on "fail" via your TC, you are
bundling multiple verification points and MUST split further.

Stress-test every scenario by asking: *"If only part of the behaviour fails,
is my pass/fail verdict still unambiguous?"*

Illustrative contrast — requirement "persist SSID / security / credentials for ≥ 4 networks":

| | Example | Why |
|---|---|---|
| ✗ Overloaded (1 TC) | save 4 → record → reboot → check 4 networks still have SSID + security + credentials | Conflates 3 axes: **capacity** (did ≥4 save?) × **data integrity** (which fields persisted?) × **persistence** (survived reboot?). "Only 3 saved" and "reboot kept SSID but lost credentials" both fail this TC for *different reasons* — verdict is ambiguous. |
| ✓ Atomic (3 TCs) | **A Capacity**: save 4th → listed as 4 entries. **B Data Integrity**: after save, each saved entry exposes non-empty SSID + security + credentials. **C Persistence**: reboot → per-field comparison of SSID/security/credentials equals pre-reboot baseline. | Each TC owns ONE failure mode. |

This contrast is illustrative. The principle — one verification point per TC —
applies to every domain. Do **not** mechanically split every requirement into
capacity/integrity/persistence; that triad is specific to the Wi-Fi example.
Choose splits that emerge from the *actual* keywords + branches in the
requirement at hand.

### 10.3 No Fabrication (applies to ALL generated fields)
Never invent a concrete value the source did not state. This covers every
TC field — `test_item_rewrite`, `pre_conditions`, `input_test_data`,
`test_procedure`, `expected_result` — and every data-point type:
numbers, thresholds, timeouts, byte/file sizes, durations, retry counts,
default states, dataset / file names, identifiers, VINs, error codes,
comparison targets, ordering rules.

- ✗ FORBIDDEN: "download limit = 20", "5 s timeout", "error 0x1A",
  "phonebook has 100 entries", "retry 3 times" — when the source is
  silent on the number / code / count.
- ✓ REQUIRED: keep it abstract and source-grounded —
  `<configured limit>`, `<device under test>`, "the value defined in spec",
  "the error code defined by the requirement".
- Domain-standard constants are allowed only when truly standard and
  unambiguous in context (e.g. BT pairing PIN `0000`, HTTP `200 OK`).
- If the source is ambiguous or incomplete, **preserve the ambiguity
  explicitly** — never paper over the gap with a plausible guess.

# Mode 2 — Review

## 11. Self-Check (before emitting every TC)
1. Test Item = `[Trigger] → [Outcome]`, 3–8 words/side, scenario-tagged if split (§6.1)
2. Traces to Req/SWRA; keywords mapped (§10)
3. Pre-Condition: state/env ONLY; no actions/checks/data-presence (§6.2)
4. Input deterministic or NA (§6.3)
5. Steps have purpose + executable action; no forbidden verbs (§7.1)
6. Final Step owns verification, maps Test Item outcome (§7.5)
7. Baseline established when before/after needed (§7.6)
8. Procedure ↔ ER 1:1; ER observable (§8)
9. No FP / No FF (§9)
10. Design Method assigned AFTER procedure finalized (§15)
11. No fabricated data: every concrete number / code / identifier / state
    came from the requirement, spec, or is a domain-standard constant.
    Unknowns stay abstract (§10.3).

## 12. Review Output
Table: `| Field | Problem | Severity | Fix |`. Severity: Critical/Major/Minor.

## 13. Formatting (CRITICAL)
- NEVER use HTML tags or Markdown tables for TC output
- Use plain text block from §5; each numbered item on own line; blank line between fields

## 15. Design Method (assign AFTER TC finalized, first-match)

Match PRIMARY intent from Test Procedure + ER:

| # | Condition | Method |
|---|---|---|
| 1 | Invalid input / illegal operation | Negative/Invalid |
| 2 | Simulated fault (disconnect, timeout) | Fault Injection |
| 3 | State A → State B transition | State Transition |
| 4 | Multiple conditions determine outcome | Decision Table |
| 5 | Input partitioned into valid/invalid | Equivalence Partitioning |
| 6 | Tests at boundary (=limit, limit±1) | Boundary Value Analysis |
| 7 | Multi-parameter combination | Combinatorial |
| 8 | End-to-end user flow, multi-step | Scenario/Use Case |
| 9 | None above; single feature check | Functional Based |

**Tie-break:**
- #3 = focus on state change itself (A→B verified)
- #8 = ≥3 steps crossing multiple features/operations
- #9 = 1–2 steps, single feature, no state change focus

## 16. Final Rule
Each step needs clear purpose. One objective per TC. Only final step validates. TC aligns with Req/SWRA.