"""Prompt builder for TC generation (ASPICE_SWE6_AI_Instruction.md §10)."""
from spec_matcher import extract_pdm_codes


REQUIRED_OUTPUT_KEYS = [
    "tc_title",
    "pre_conditions",
    "input_test_data",
    "test_procedure",
    "expected_result",
    "design_method",
    "priority",
    "split_flag",
    "split_reason",
]


_SYSTEM_BASE = (
    "You are an ASPICE SWE.6 test case writer. "
    "Return ONLY valid JSON, no markdown fences."
)
_SYSTEM_BASE_BATCH = (
    "You are an ASPICE SWE.6 test case writer. "
    "Return ONLY valid JSON object(s), no markdown fences."
)


def build_system_prompt() -> str:
    """純文字 system prompt（保留以利舊測試/相容）。"""
    return _SYSTEM_BASE


def build_batch_system_prompt() -> str:
    return _SYSTEM_BASE_BATCH


_HARD_CONSTRAINTS = """
## HARD CONSTRAINTS (non-negotiable; violation = failure)

1. **All TC output fields that will be written back to the workbook MUST be in
   English.** This includes `tc_title`, `pre_conditions`,
   `input_test_data`, `test_procedure`, `expected_result`, `design_method`,
   `priority`, `split_flag`, and `split_reason`. Requirements may be bilingual
   (Chinese + English); read both but produce these TC fields in English only.
   Proper nouns / API names / protocol names (HFP, A2DP, BLE, etc.) stay
   as-is. Analytical explanation fields such as `reasoning`, `meaning`, or
   scenario descriptions may be written in Traditional Chinese when explicitly
   requested below.
2. **tc_title is MANDATORY for EVERY TC** — a concise, scenario-based phrase
   that tells the reviewer *what this TC is verifying* at a glance. It replaces
   the old `test_item_rewrite` field and is appended in parentheses below the
   original Test Item when writing back to the workbook. Must not be blank,
   must not copy the source verbatim. Length target: **2–14 words total**
   (Scenario tag form may be as short as 2 words, e.g. `Cold boot`).
   Three acceptable shapes (pick whichever makes the scenario clearest):
     (a) **Arrow form** — `Trigger → Observable Outcome` (e.g.
         `CarPlay connected → CP Media icon shown in App Drawer`). Recommended
         when causality is the point being verified.
     (b) **Sentence form** — `[Outcome] when [trigger]` / `[Object] [state]
         under [condition]` / `[Object] [behavior] in [location]` (e.g.
         `CP Media icon displayed when CarPlay is connected`,
         `AA App icon hidden without AA connection`). Recommended when a
         natural sentence reads more clearly than an arrow.
     (c) **Scenario tag form** — short noun phrase naming the branch /
         data point / environment being exercised (e.g.
         `Upload supported video file type: .mp4`,
         `Upload unsupported video file type: .mov`,
         `Cold boot`, `Power Cycle`, `Low memory`,
         `Add Contact After Deletion to Return to 5,000`,
         `Initial Sync = 5,000`,
         `Per BT Device — Independent Limit`).
         **PREFERRED** when this TC is one of many siblings under the same
         requirement and the only thing distinguishing it from siblings is
         the data point / environment / branch / boundary value being
         exercised. Matches the format reviewer-approved Excel templates
         actually use (e.g. `(Cold boot)`, `(Upload supported video file
         type: .mp4)`). The tag MUST contain the distinguishing token
         (format extension, env keyword, boundary value, mode name) so
         siblings remain self-evidently different from tc_title alone.
   Drop articles only when they hurt readability; modals (should/will) and
   hedges (properly/successfully/within reasonable time) are always forbidden.
   **The distinguishing state / trigger MUST appear in tc_title** — NEVER
   write the inspection action alone (`Open Media category`, `Navigate to
   Settings`); those belong in `test_procedure`. When two sibling TCs differ
   only by a state precondition (connected vs disconnected, enabled vs
   disabled, present vs absent, before vs after, valid vs invalid), that
   distinguishing state MUST be visible in the title; otherwise the sibling
   titles become indistinguishable. For Scenario tag form (c), the tag
   itself IS the distinguishing token — no separate trigger/outcome needed.
   Do NOT add outer parentheses in the generated field; presentation-layer
   wrapping is handled downstream when writing back to the workbook.
3. **test_procedure and expected_result must have the SAME number of
   numbered items (1:1 mapping).** If procedure has N steps, expected_result
   must also have exactly N items, aligned in order.
4. **pre_conditions only describes states / environment.** Never include
   actions (no "click", "enter", "send" — those belong in test_procedure),
   checks/reads, or data-presence verifications (no "HU has 5,000 entries",
   "phonebook contains N contacts" — set up + read in a baseline step). §6.2.
5. **design_method is assigned AFTER the procedure and expected_result are
   finalized**, judged from the ACTUAL flow (not the requirement text). Use
   §15 first-match on PRIMARY intent. Prefer these 9 short English labels:
   Negative / Fault Injection / State Transition / Decision Table / EP / BVA
   / Combinatorial / Scenario / Functional. The system will normalize them to
   the canonical dropdown values.
6. **Application output contract: `priority` MUST be one of P0 / P1 / P2 / P3.**
   This is a tool-specific workbook/export requirement, not an ASPICE SWE.6
   rule from the instruction doc. Follow the priority rubric in
   `docs/test_case_priority.md` when it is loaded in the rules text:
   P0 = critical/core functionality, safety, boot/recovery, connection,
   audio output, eCall, vehicle-critical CAN signal, or data loss risk;
   P1 = major user-facing functionality or key operational logic flow;
   P2 = secondary/support functionality whose failure has limited impact
   on major features; P3 = minor UI enhancement, low-impact customization,
   rare-use scenario, or cosmetic detail. Do NOT return "High", "Medium",
   "Low", "NA", or any other value — always use exactly P0, P1, P2, or P3.
7. All field keys are snake_case (tc_title, pre_conditions,
   input_test_data, test_procedure, expected_result, design_method,
   priority, split_flag, split_reason).
8. **Every test_procedure step MUST be a single, concrete, executable action
   with explicit target + value.** FORBIDDEN: bare vague phrases (`verify
   the feature`, `operate normally`), multiple actions glued by "and/then"
   in one step, placeholder tokens ("<some value>", "xxx", "TBD"), steps
   that only restate the expected result. REQUIRED: one action per step,
   name the exact UI element / API / signal, include the exact value / data
   used (e.g. "Send AT+BLDN with number 0912345678", not "Send a call").
   For verification steps, use `Check that / Confirm that / Read / Record /
   Compare` + explicit observable target (see constraint 9a).
9. **Every expected_result item MUST be observable and measurable** — state
   what appears on screen, what log/signal is emitted, what state changes,
   or what value is returned. No "works correctly", no "no error".
9a. **Forbidden step verbs (§7.1.1):** NEVER use `observe`, `observe whether`,
   `see if`, `check whether`, `confirm whether`, `verify`, `watch`, `monitor`,
   or `inspect` as the MAIN action verb of a test_procedure step — they
   defer judgement to the tester and leave the target ambiguous.
   Always pair a preferred verb (`Check that / Confirm that / Read /
   Record / Compare`) with an explicit observable target (UI element, log
   line, signal value, count, state). `verify` may appear only to describe
   purpose (e.g. `... to verify that ...`), never as the step's main verb.
10. **input_test_data lists concrete values only** (numbers, strings, file
    names, enum values). If no data is needed, write "N/A" — never leave
    it empty and never describe actions here.
10a. **NEVER fabricate specific numeric values, counts, limits, timeouts,
    file sizes, byte counts, durations, etc. that the requirement does NOT
    state.** If the requirement says "the maximum download count" /
    "限制最大下載數量" without giving a number, you MUST refer to it
    abstractly:
      ✗ FORBIDDEN: "download limit set to 20", "20 records", "5 seconds",
        "1024 bytes", "100 entries" — when 20 / 5 / 1024 / 100 came from
        nowhere.
      ✓ REQUIRED: use the configured maximum / use the configured limit
        value / `<configured limit N>` / "the value defined in spec" —
        leave the actual value to be filled in at execution time.
    The same applies to expected_result: write "matches the configured
    download limit", NOT "matches 20".
    Concrete values are ONLY allowed when (a) the requirement / spec /
    test_item explicitly states the value, or (b) it's a domain-standard
    constant (e.g. BT pairing PIN `0000`, HTTP `200 OK`).
    When no value is stated, also document that in input_test_data:
    `download_limit: <configured maximum, per spec>`.
10b. **NEVER fabricate any other unstated data point either.** If the
    requirement / spec / reviewer pre-fill does NOT explicitly provide a
    concrete condition, dataset, status, identifier, error code, retry count,
    ordering rule, timeout behaviour, threshold, capacity, or comparison
    target, do NOT invent one to make the TC look complete.
      ✗ FORBIDDEN: adding made-up contact counts, file names, VINs, device
        IDs, error codes, default states, retry limits, or "expected" return
        values that never appeared in the source.
      ✓ REQUIRED: keep it abstract and source-grounded, e.g.
        `<configured dataset>`, `<device under test>`, "the error code
        defined in spec", "the state defined by the requirement".
    If the source is ambiguous or incomplete, preserve the ambiguity
    explicitly instead of guessing.
11. **Follow the ASPICE SWE.6 AI Instruction loaded above verbatim.** The
    instruction doc is authoritative. Apply the relevant sections — §2 Core
    Principles, §6 Field Rules, §7 Step Design (incl. §7.5 Final Step /
    §7.6 Baseline), §8 Expected Results, §9 False Pass/Fail, §10 Requirement
    Alignment, §11 Review Checklist — do not paraphrase, skip, or relax.
"""


_WRITING_DISCIPLINE = """
## WRITING DISCIPLINE (run this self-check BEFORE emitting each TC)

For every TC you are about to output, silently verify:

[TC Title]
  [ ] tc_title is filled (MANDATORY for every TC), 2–14 words, and uses
      one of three shapes:
        - Arrow form (`Trigger → Observable Outcome`) — pick when
          causality is the point being verified, and ONLY when both
          sides read clearly without telegraphic compression. If
          fitting the arrow form forces you to drop nouns/objects/
          context and the result reads ambiguously
          (`Sync max → entries on HU`), switch to a sentence or tag.
        - Sentence form (`[Outcome] when [trigger]`, `[Object] [state]
          under [condition]`, `[Object] [behavior] in [location]`) —
          pick when a natural sentence reads more clearly than arrow.
        - Scenario tag form — short noun phrase naming the branch /
          data point / environment / boundary (e.g.
          `Upload supported video file type: .mp4`, `Cold boot`,
          `Power Cycle`, `Initial Sync = 5,000`). PREFERRED when
          siblings differ only by data / env / branch — matches the
          reviewer-approved Excel template format.
      No modals (should/will), no hedges (properly/successfully/within
      reasonable time) (§6.1).
  [ ] For Arrow form (a) and Sentence form (b): trigger side MUST
      include the CONDITION / STATE / CONTEXT, not a bare action.
      A bare action (`Select X`, `Press Y`, `Open Z`) without the
      state it operates under is ambiguous — the same action under
      different states yields different outcomes (that is why
      sibling TCs exist). Patterns: `[action] while/with/after
      [state] → [outcome]`, or front-load the state
      (`With BT off, press Connect → ...`). Bare-action triggers
      are acceptable ONLY when there is genuinely no relevant state
      (e.g. cold-boot smoke test).
  [ ] For Scenario tag form (c): the tag itself IS the distinguishing
      token — no separate trigger/outcome required. The tag MUST
      contain the differentiating keyword (format extension, env
      name, boundary value, mode label, role), so the tag alone tells
      the reviewer which sibling this TC is.
  [ ] The distinguishing state / trigger / tag is visible in the title
      — NEVER the bare inspection action (`Open X`, `Navigate to Y`);
      those belong in test_procedure.
  [ ] Sibling-distinction check: if this TC has a sibling that differs
      only by a state precondition (connected↔disconnected, enabled↔
      disabled, present↔absent, before↔after, valid↔invalid), or by
      data / environment (`.mp4`↔`.avi`, `Cold boot`↔`Power Cycle`,
      `=5000`↔`>5000`), the distinguishing token MUST appear in the
      title. Two sibling TCs whose tc_title reads identically (or
      differs only in "displayed" vs "hidden") is a FAIL — rewrite
      with the real trigger or tag.
  [ ] Do NOT add outer parentheses in the generated field; the
      workbook writer wraps it below the original Test Item.

[Pre-Conditions]
  [ ] Only describes state/environment — no actions, no checks/reads,
      no data-presence (§6.2).
  [ ] Not system-obvious (`HU powered on`) and not the feature under test
      stated as a premise.

[Test Procedure — Step Design]
  [ ] Every step has explicit actor, action verb, target, and (when
      applicable) value/data.
  [ ] Every step has clear intent. Intent is usually SELF-EVIDENT from
      action + target (`Press [Screen Off] button`, `Enable BT on the
      phone`). Add an explicit purpose clause (`... to ...`) ONLY when
      action alone leaves intent ambiguous — same UI serving multiple
      purposes, non-obvious setup for a later step, or opaque target
      names (raw AT commands, deep menu paths, internal signals). Do NOT
      pad every step with `to ...` — forced clauses on self-evident
      actions are noise (§7.1).
  [ ] No forbidden vague verbs as a step's MAIN verb — NEVER use `observe`,
      `observe whether`, `see if`, `check whether`, `confirm whether`,
      `verify`, `watch`, `monitor`, or `inspect`. Use `Check that /
      Confirm that / Read / Record / Compare` + explicit observable target
      (§7.1.1). `verify` is allowed only in a purpose clause
      (`... to verify that ...`), never as the step's main verb.
  [ ] No "and/then"-chained actions in one step; no placeholder tokens
      ("<some value>", "xxx", "TBD"); no step that only restates the
      expected result.
  [ ] Only the FINAL step validates the Test Item outcome. Earlier steps
      may have observable ER (to prove setup/transition succeeded) but
      must not pre-verify the main outcome (§7.7).
  [ ] For state-change or boundary requirements, establish a BASELINE
      (before state) in an earlier step and compare against OUTCOME
      (after state) in the final step (§7.6).

[Input Test Data]
  [ ] Concrete values only (numbers, strings, file names, enum values),
      or `N/A` — never empty, never describes actions (§6.3).

[Expected Result]
  [ ] Count matches test_procedure exactly, aligned 1:1 (§8).
  [ ] Every item is observable (UI / log / signal / API response / state);
      no "normal", "as expected", "works correctly".
  [ ] Final ER covers the COMPLETE Test Item outcome, not just a partial
      success (§8).

[No Fabrication — applies to ALL fields (§10.3)]
  [ ] No FABRICATED numeric values: every concrete number, limit, duration,
      count, byte/size, or threshold comes from the requirement, spec,
      or is a domain-standard constant. If the req says "maximum N"
      without a number, write `<configured maximum>` / "the configured
      limit" — NEVER invent 20 / 100 / 5s.
  [ ] No FABRICATED unstated data: do not invent dataset names, file
      names, identifiers, error codes, retry counts, default states,
      comparison targets, or other concrete details the source never
      stated. Preserve unknowns abstractly.

[Output Contract]
  [ ] design_method assigned AFTER procedure+ER are finalized, judged
      from the ACTUAL flow (not the requirement text), via §15
      first-match on PRIMARY intent. Short English labels preferred;
      the system normalizes them to canonical dropdown values.
  [ ] priority is exactly P0 / P1 / P2 / P3 (tool-specific workbook
      contract, not from the ASPICE doc). Use the loaded
      `docs/test_case_priority.md` rubric when available.
  [ ] All workbook-bound TC fields are English-only. Traditional Chinese
      is allowed only in explicit analysis fields (`reasoning`, `meaning`,
      `name`, `description`) when requested.
  [ ] Each TC is self-contained: its own pre-conditions, procedure, ER.
      NEVER write cross-references like "same as TC1 but...".

If any check fails, FIX the TC before outputting. Do not emit a TC that
would fail the §11 11-item self-check in the instruction doc.
"""


_CALIBRATION_EXAMPLES = """
## CALIBRATION EXAMPLES (reference only — quality bar, not templates)

Three reviewer-approved patterns. Do NOT copy sentence structure, domain
keywords, or concrete values (5000, 60, .mp4) into unrelated requirements.
Apply the same QUALITY BAR to any domain.

---

### Example 1 — Pre-Condition is STATE, not action or feature-under-test

Bad:
  tc_title: The system should properly support maximum phonebook entries
  pre_conditions:
    1. The HU is powered on.
    2. Dealer Mode is accessible.
    3. USB or SD Card is inserted and ready.
    4. The device has 5,000 phonebook entries registered.
    5. The device is not connected to the HU.

Reviewer flagged:
  - tc_title hedges ("should", "properly"), not `Trigger → Outcome` (§6.1)
  - #1 system-obvious; #2 feature under test as premise; #3 action belongs
    in procedure; #5 controlled by test steps, not a precondition (§6.2)

Good:
  tc_title: Sync at configured maximum → all entries on HU
  pre_conditions:
    1. A PBAP-supported device is available.
    2. The device contains phonebook entries equal to the configured
       maximum defined in spec.

---

### Example 2 — State change needs baseline (before) + outcome (after)

Requirement: "After the HU phonebook has synchronized to its maximum
capacity, adding a new contact on the paired device shall not increase
the HU phonebook count; the new contact shall not be imported."

Bad:
  tc_title: Verify adding new contacts beyond maximum works correctly
  test_procedure:
    1. Add one new contact on the device.
    2. Re-trigger phonebook synchronization.
    3. Open the Phonebook screen on the HU.
  expected_result:
    1. The new contact is saved on the device.
    2. Phonebook update is triggered on the HU.
    3. The HU phonebook remains at 5,000 entries.

Reviewer flagged:
  - No baseline: reviewer comment "動作前確認+動作後確認 才有對比".
    Without Step 2 checking the starting count, "still 5,000" after the
    action could be coincidence (§7.6).
  - 3 steps conflate setup + transition; no verification that the
    configured-maximum starting state was really reached before the
    action (§7.7).
  - tc_title: "works correctly" is vague, not `Trigger → Outcome` (§6.1).
  - pre_conditions would need to assume state from prior runs instead of
    establishing it in-procedure (§6.2).

Good:
  tc_title: Add contact beyond maximum → count unchanged, not imported
  pre_conditions:
    1. A PBAP-supported device is available.
    2. HU phonebook has already been synchronized to the configured
       maximum (per spec).
  test_procedure:
    1. Pair the PBAP-supported device with the HU via Bluetooth.
    2. Check the HU phonebook contains exactly the configured maximum
       number of entries as baseline.
    3. Add one new contact on the device.
    4. Trigger phonebook synchronization/update.
    5. Wait until phonebook synchronization/update is completed.
    6. Open the Phonebook screen on the HU.
    7. Search for the newly added contact; compare the HU phonebook
       count against the baseline recorded in Step 2.
  expected_result (aligned 1:1, each observable):
    1. Device paired and connected.
    2. HU displays exactly the configured maximum entries (baseline recorded).
    3. New contact created on device.
    4. Sync/update starts.
    5. Sync/update completes.
    6. Phonebook screen opens.
    7. New contact not found on HU; count equals the Step 2 baseline.

Note on concrete values: "5000 / 60 / 180" are allowed in real TCs when
the requirement/spec defines them (as in this requirement). When the req
says only "maximum" with no number, keep it abstract ("configured
maximum") — never fabricate a value (§10.3).

---

### Example 3 — Enumerated supported items → one TC per item

Requirement: "Dealer Mode shall only allow the supported video file types
to be uploaded. Supported formats: .mp4, .avi, .mpg, .wmv, .3gp, .mkv."

Bad (1 TC lumping all 6 formats):
  tc_title: Plays supported file types
  test_procedure (abbreviated):
    1. Press H/K [Screen off] button.
    2. ... enter Dealer Mode.
    5. Select "Upload Showroom Demo Video from USB" to upload supported
       file types.
    8. Select "Showroom Demo Video" on App Drawer page.

Reviewer flagged:
  - FALSE PASS: if .mp4 uploads but .mkv silently fails, this TC still
    passes — per-format regressions are invisible (§9, §10.2).
  - Lost traceability: requirement names 6 formats, TC only verifies
    "supported file types" as a collective.
  - tc_title too short, not `Trigger → Outcome` (§6.1).
  - Early steps lack intent; final step does not state the verification
    target (§7.1, §7.5).

Good (6 TCs, one per format — `.mp4` shown in full; others identical
pattern with extension swapped):

  tc_title: Upload .mp4 to Dealer Mode → .mp4 plays on HU
  pre_conditions:
    1. Dev / Pre-Prod build.
    2. USB storage device containing a .mp4 video file prepared.
  test_procedure:
    1. Press H/K [Screen Off] button to turn off the screen.
    2. Press and hold the top-right and bottom-left corners of the
       screen for 5 seconds to enter Dealer Mode.
    3. Select "Showroom Demo Mode information".
    4. Select "File Browser".
    5. Insert the prepared USB storage device.
    6. Select "Upload Showroom Demo Video from USB".
    7. Select the .mp4 video file and confirm upload.
    8. Tap "X" to exit Dealer Mode.
    9. Open App Drawer.
    10. Select "Showroom Demo Video" and check that playback of the
        uploaded .mp4 video starts on the HU.
  expected_result (1:1 with procedure, each observable):
    1. Screen turned off.  2. Dealer Mode entered.
    3. Info page displayed.  4. File Browser page displayed.
    5. USB detected.  6. Upload option available.
    7. .mp4 file accepted.  8. Dealer Mode exited.
    9. App Drawer displayed.
    10. .mp4 video displayed and playback starts.

  Sibling TCs (same procedure pattern, swap extension). Two equally
  valid title shapes — Scenario tag form (c) is what the reviewer
  template actually uses and is PREFERRED for enumerated formats:

    Scenario tag form (PREFERRED — matches reviewer template):
      tc_title: Upload supported video file type: .mp4
      tc_title: Upload supported video file type: .avi
      tc_title: Upload supported video file type: .mpg
      tc_title: Upload supported video file type: .wmv
      tc_title: Upload supported video file type: .3gp
      tc_title: Upload supported video file type: .mkv
      tc_title: Upload unsupported video file type: .mov   ← negative pair

    Arrow form (also acceptable when causality is the focus):
      tc_title: Upload .mp4 to Dealer Mode → .mp4 plays on HU
      tc_title: Upload .avi to Dealer Mode → .avi plays on HU
      ...

  Note:
  - Purpose clauses ("to turn off the screen", "to enter Dealer Mode")
    added only where needed; self-evident steps ("Select File Browser")
    have no clause (§7.1).
  - When supported items are enumerated, ALWAYS pair the supported-set
    with at least one unsupported negative TC (e.g. `.mov`). Reviewers
    expect the negative branch to be explicit, not implied.
  - Scenario tag form (c): the format extension IS the distinguishing
    token; siblings remain self-evidently different from tc_title alone
    (§6.1).

---

### Example 4 — Trigger must be the causal state, not the inspection action

Requirement: "CP Media source icon shall appear in the App Drawer > Media
category when CarPlay is connected, and shall disappear when CarPlay is
disconnected."

Bad (two sibling TCs with indistinguishable rewrites):
  TC-A tc_title: Open Media category → CP Media icon displayed
  TC-B tc_title: Open Media category → CP Media icon hidden

Reviewer flagged:
  - Both Triggers are the SAME inspection action (`Open Media category`).
    Reading only `tc_title`, you cannot tell which scenario
    each TC is verifying.
  - The real distinguishing condition — CarPlay connection state — was
    dropped to fit the word count. `Open Media category` is what the
    tester DOES to observe the result; it is not what is being tested.
  - Sibling-distinction rule (§6.1) requires the differing state to live
    in the Trigger.

Good:
  TC-A tc_title: CarPlay connected → CP Media icon shown in App Drawer
  TC-B tc_title: CarPlay disconnected → CP Media icon hidden from App Drawer

  Now the two rewrites are self-evidently different scenarios, and the
  inspection action (opening the Media category) stays where it
  belongs — in each TC's test_procedure.

---

### Example 5 — Same requirement, environment dimension → sibling TCs

Requirement: "The radio HU shall allow a user to see system information."

This is a basic "open the page and verify fields" feature, but reviewers
expect the SAME feature to be re-verified under several environment
conditions, because regressions often surface only after cold boot,
power cycle, or low-memory pressure. The reviewer-approved Excel
template shows this pattern explicitly: one base TC plus one sibling
per environment axis, distinguished by Scenario tag form (c).

Bad (1 TC, only happy path):
  tc_title: View system information

Reviewer flagged:
  - Misses environment-axis siblings. A page that renders fine on a
    warm boot can fail to populate after cold boot or power cycle.
    Without per-environment TCs, regressions in those paths are
    invisible (§9 FP, §10.2 branches).

Good (4 sibling TCs, Scenario tag form):

  TC-1 (base — warm-boot happy path):
    tc_title: View system information
    test_procedure:
      1. Press [Screen Off] button.
      2. Press and hold the designated corners for 5 seconds to enter
         the target mode.
      3. Select "System Information" and check displayed fields.
    expected_result:
      1. HU screen is OFF.
      2. Mode page is displayed.
      3. All required system information fields are displayed.

  TC-2 (env axis: cold boot):
    tc_title: Cold boot
    test_procedure:
      1. Cold boot the HU.
      2. Press [Screen Off] button.
      3. Press and hold the designated corners for 5 seconds to enter
         the target mode.
      4. Select "System Information" and check displayed fields.
    expected_result:
      1. HU cold boots normally without error.
      2. HU screen is OFF.
      3. Mode page is displayed.
      4. All required system information fields are displayed.

  TC-3 (env axis: power cycle):
    tc_title: Power Cycle
    test_procedure:
      1. Power cycle the HU.
      2. Press [Screen Off] button.
      3. ... (rest identical to TC-1)
    expected_result:
      1. HU reconnects normally without error.
      2. ... (rest aligned)

  TC-4 (env axis: low memory):
    tc_title: Low memory
    test_procedure:
      1. Drive the HU into a low-memory state (per spec / test setup).
      2. Press [Screen Off] button.
      3. ... (rest identical)
    expected_result:
      1. HU is in the low-memory state defined for this test.
      2. ... (rest aligned)

Notes:
  - tc_title uses Scenario tag form (c) — the env keyword IS the
    distinguishing token. No arrow / sentence needed.
  - The base TC (no env tag) covers the warm-boot happy path; each
    env sibling prepends ONE environment-establishing step plus its
    matching ER, then re-runs the same verification.
  - Same pattern applies to other environment axes when relevant to
    the requirement: Reboot persistence, Background app load, Network
    loss, Storage full, etc. Pick the axes that actually matter for
    the feature under test — do NOT mechanically add all of them.
  - Reviewer rationale: "page renders" is not the same guarantee as
    "page recovers"; environment siblings catch persistence /
    initialization regressions that the base TC cannot.

---

Key takeaways (apply to any domain):
1. Pre-conditions are STATE; actions go in steps.
2. State-change requirements need BASELINE + OUTCOME in the procedure.
3. Enumerated supported items → one TC per item; prevents False Pass.
   Pair the supported set with at least one unsupported negative.
4. Trigger = causal condition, NOT inspection action. Sibling TCs must
   be distinguishable from tc_title alone.
5. Environment dimension (Cold boot / Power Cycle / Low memory / etc.)
   is a sibling axis — use Scenario tag form (c) to name the env, and
   prepend ONE environment-establishing step to each env sibling.
"""


def build_system_blocks(rules_text: str, batch: bool = False) -> str:
    """
    建構 system prompt（OpenAI chat completions 格式為單一字串）。
    規則放在 prefix，OpenAI 會自動對 ≥1024 tokens 重複前綴套用 prompt cache。
    Hard constraints 放在最後（recency bias），強化關鍵不變量。
    """
    base = _SYSTEM_BASE_BATCH if batch else _SYSTEM_BASE
    if not rules_text:
        return (
            f"{_HARD_CONSTRAINTS}\n{_WRITING_DISCIPLINE}\n"
            f"{_CALIBRATION_EXAMPLES}\n\n---\n\n{base}"
        )
    return (
        f"## ASPICE SWE.6 Rules (authoritative — follow strictly)\n\n{rules_text}\n\n"
        f"{_HARD_CONSTRAINTS}\n{_WRITING_DISCIPLINE}\n"
        f"{_CALIBRATION_EXAMPLES}\n\n---\n\n{base}"
    )


def _get_spec_context(row: dict, spec_index: dict | None) -> str:
    """Extract relevant spec context for a single row."""
    segments = []
    matched_context = row.get("matched_spec_context") or row.get("matchedSpecContext")
    if matched_context and str(matched_context).strip():
        segments.append(str(matched_context).strip())
    candidate_context = (
        row.get("reference_candidate_context")
        or row.get("referenceCandidateContext")
    )
    if candidate_context and str(candidate_context).strip():
        segments.append(
            "Reference candidates below were NOT automatically matched. "
            "Judge relevance from the source row before using them; ignore unrelated candidates.\n"
            f"{str(candidate_context).strip()}"
        )

    if spec_index:
        codes = extract_pdm_codes(row["test_item"])
        for code in codes:
            if code in spec_index:
                entry = spec_index[code]
                text = entry.get("full_text") or entry.get("description", "")
                if text:
                    segments.append(f"[Spec file: {code}] {text}")

    return "\n".join(segments) if segments else "N/A"


def build_user_prompt(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for single TC generation."""
    spec_context = _get_spec_context(row, spec_index)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)
    regenerate_reason = _coalesce_row_value(row, "regenerate_reason", "regenerateReason")
    regenerate_section = ""
    if regenerate_reason != "N/A":
        regenerate_section = (
            "\n## Reviewer Regenerate Reason\n"
            f"{regenerate_reason}\n\n"
            "Use this reason as the primary correction target while still obeying "
            "all ASPICE SWE.6 writing rules. Fix the stated problem directly; do "
            "not ignore it or introduce unrelated changes.\n"
        )

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    sibling_section = _format_sibling_section(row)
    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirement
- Requirement ID: {row.get('req_id') or row.get('reqId') or ''}
- Original Test Item: {row['test_item']}
{regenerate_section}{sibling_section}

## Spec Context
{spec_context}{rules_section}

## Output
Return JSON with keys: {output_keys}

Do NOT invent unstated values or data points. If the requirement/spec does
not provide an exact number, limit, threshold, dataset, state, code, or
other concrete detail, keep it abstract and source-grounded instead of
guessing. Use placeholders such as `<configured limit>` / `<configured
maximum, per spec>` only when the source clearly indicates such a configured
value exists but does not state the number.

Before emitting, run the WRITING DISCIPLINE self-check listed in the system prompt."""


def build_quick_generate_prompt(
    test_item: str,
    context: str | None,
    rules_text: str,
) -> str:
    """Build prompt for quick (ad-hoc) single TC generation."""
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)
    context_section = f"\n## Additional Context\n{context}" if context else ""
    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    return f"""## Task
Generate a single test case for the following test item. Follow all rules strictly.

## Test Item
{test_item}{context_section}{rules_section}

## Output
Return JSON with keys: {output_keys}

Before emitting, run the WRITING DISCIPLINE self-check listed in the system prompt."""


def build_decompose_prompt(requirement: str, rules_text: str,
                           domain_block: str | None = None) -> str:
    """Build prompt to decompose a requirement into distinct test scenarios.

    `domain_block` (Stage 1 Domain Pack) is GROUND TRUTH: decompose to cover
    every spec/domain-defined branch & enumeration value, but never invent a
    state/mode the domain does not define.
    """
    rules_section = (
        f"\n\n## Rules (for context, these will guide TC generation after decomposition)\n{rules_text}"
        if rules_text else ""
    )
    domain_section = (
        f"\n\n## Domain Pack (GROUND TRUTH — decompose to cover every enumeration "
        f"value / branch listed here; do NOT invent states/modes beyond it)\n{domain_block}"
        if domain_block else ""
    )
    return f"""## Task{domain_section}
Analyze the following software requirement following the ASPICE SWE.6 reviewer workflow:

1. Extract the key concepts ("keywords") from the requirement. For each keyword, state its meaning in this context and which scenario ids will verify it.
2. Decompose the requirement into distinct, independent test scenarios. Each scenario must have exactly ONE verification point — a single unambiguous pass/fail question (see §10.2 "One Verification Point per TC").
3. For every scenario, run a PARTIAL-FAILURE stress test: imagine the system
   succeeds on part of the behaviour and fails on another part. If two
   different partial failures would both land on "fail" for *different*
   reasons, the scenario is bundling multiple verification points — split it
   further until each scenario owns exactly one failure mode.

Every keyword must map to at least one scenario id — if a concept has no coverage, add a scenario for it.

Do NOT invent missing data while analyzing. If the requirement does not state
an exact number, threshold, dataset, state, code, or other concrete detail,
preserve that ambiguity explicitly instead of guessing.

## Language
The `meaning`, `reasoning`, `name`, and `description` fields MUST be written
in Traditional Chinese (繁體中文) so the Taiwanese reviewer can audit the
decomposition logic in their native language. Keep the `keyword` and
`test_item` fields in the source language of the requirement (do not
translate) so downstream TC generation stays consistent with the spec.

## Requirement
{requirement}{rules_section}

## Output
Return ONLY valid JSON (no markdown fences) with this exact structure:
{{
  "keywords": [
    {{
      "keyword": "<short keyword from the requirement — source language>",
      "meaning": "<此關鍵字在本需求中的意義（繁體中文）>",
      "scenarios": [1, 2]
    }}
  ],
  "reasoning": "<說明你如何識別出這些 scenario、為什麼這樣拆（繁體中文）>",
  "scenarios": [
    {{
      "id": 1,
      "name": "<簡短的 scenario 名稱（繁體中文）>",
      "description": "<這個 scenario 驗證什麼的一句話說明（繁體中文）>",
      "verification_question": "<單一 yes/no 判斷問句；若整條 req 通過 SIT 後這題答 yes 即 pass、答 no 即 fail（繁體中文）>",
      "fail_examples": [
        "<一種能讓此 scenario fail 的具體 partial-failure 描述（繁體中文）>",
        "<另一種 partial-failure；若想不出第二種，代表 scenario 可能太窄，重新檢視>"
      ],
      "test_item": "<rewritten test item statement — source language>"
    }}
  ]
}}

Self-check before returning: for each scenario, the two `fail_examples` should
fail for the SAME underlying reason (same verification point). If they fail
for *different* reasons, split the scenario into two."""


def build_batch_prompt(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for batch TC generation."""
    items = []
    for i, row in enumerate(rows):
        spec_context = _get_spec_context(row, spec_index)
        items.append(
            f"### TC {i + 1}\n"
            f"- Req ID: {row.get('req_id') or row.get('reqId') or ''}\n"
            f"- Test Set: {row.get('test_set', context.get('test_set', 'N/A'))}\n"
            f"- Test Item: {row['test_item']}\n"
            f"- Spec: {spec_context}"
        )
    batch_text = "\n\n".join(items)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirements
{batch_text}{rules_section}

## Output
Return a JSON object with key `tcs` whose value is an array of TC objects.
Each TC object has keys: {output_keys}

Before emitting, run the WRITING DISCIPLINE self-check listed in the system
prompt for EVERY TC in the batch."""


# ---------------------------------------------------------------------------
# Multi-TC prompts: AI 自行判斷一個 requirement 要拆成幾筆 TC，回傳陣列。
# 不再硬性 1 req = 1 TC，由 AI 針對不同 condition / branch / boundary 自行切分。
# ---------------------------------------------------------------------------


def _coalesce_row_value(row: dict, *keys: str) -> str:
    for key in keys:
        value = row.get(key)
        if value is not None and str(value).strip():
            return str(value).strip()
    return "N/A"


def _format_sibling_section(row: dict) -> str:
    """同 reqId 多列時 inject 的 prompt 段落。沒 sibling 回空字串。

    `row['siblings']` 預期為 list of dicts with `id`/`row_num`/`test_item`，
    由 api_server._prepare_generation_rows 填入。
    """
    siblings = row.get("siblings") or []
    if not siblings:
        return ""
    items = []
    for s in siblings:
        row_num = s.get("row_num")
        # 把 row_num 直接當 bracketed identifier，AI 也只回 row_num（純數字字串）。
        # row_num 是 Excel 列號，對 AI 易讀、對 reviewer 也能在 workbook 直接對照；
        # 用 uuid 反而 AI 容易 hallucinate 而 lookup 失敗。
        ident = (
            f"row #{int(row_num)}"
            if isinstance(row_num, int) and row_num > 0
            else "row ?"
        )
        text = str(s.get("test_item") or "").strip().replace("\n", " ")
        if len(text) > 300:
            text = text[:297] + "..."
        items.append(f"- [{ident}] {text or '(empty test_item)'}")
    body = "\n".join(items)
    return (
        "\n\n## Sibling Rows (same Requirement ID)\n"
        f"This Requirement ID appears on {len(siblings) + 1} rows total. "
        "Other rows under the same Requirement ID:\n"
        f"{body}\n\n"
        "When designing THIS TC:\n"
        "- Make `tc_title` trigger CLEARLY distinguish this scenario from "
        "siblings (§6.1 sibling-distinction rule). The differing state / "
        "input / mode MUST be visible in the title.\n"
        "- Do NOT duplicate verification logic siblings already cover.\n"
        "- If — and only if — this row is **truly equivalent** to a sibling "
        "(same trigger AND outcome AND input category AND verification "
        "target), set `duplicate_of` in the response to that sibling's "
        "**row number as a string** — for a sibling shown as `[row #11]`, "
        "set `\"duplicate_of\": \"11\"` (digits only, no `row` prefix). "
        "Reviewers will see a duplicate badge linked to that workbook row "
        "and decide whether to delete. STRICT: partial overlaps, similar "
        "Test Sets, or shared procedure steps DO NOT qualify. When in "
        "doubt, omit the field.\n"
        "- **MANDATORY when siblings exist**: produce a `distinguishing_axis` "
        "object in the response describing how THIS row differs from the "
        "siblings as a whole. Schema: "
        "`{\"axis\": \"trigger_state|input_data|timing|boundary|mode|none\", "
        "\"delta\": \"<繁中一句話：本列與 sibling 的具體差異>\"}`. "
        "Use `axis: \"none\"` ONLY when this row is a true duplicate — in "
        "that case `duplicate_of` MUST also be set. The `delta` sentence "
        "MUST cite a concrete token (state name, data value, mode, "
        "boundary) that also appears in this row's `tc_title`; vague "
        "wording like 「不同情境」/「另一場景」is rejected."
    )


def _format_source_workbook_row(row: dict, context: dict) -> str:
    """Format workbook fields AI must consider before deciding multi-TC split."""
    test_group = _coalesce_row_value(row, "test_group", "testGroup")
    if test_group == "N/A":
        test_group = str(context.get("test_group") or "N/A").strip() or "N/A"
    test_set = _coalesce_row_value(row, "test_set", "testSet")
    if test_set == "N/A":
        test_set = str(context.get("test_set") or "N/A").strip() or "N/A"

    fields = [
        ("Requirement ID", _coalesce_row_value(row, "req_id", "reqId")),
        ("Test Group Theme", test_group),
        ("Test Set", test_set),
        ("Test Item", _coalesce_row_value(row, "test_item", "testItem")),
        ("Reviewer Regenerate Reason", _coalesce_row_value(row, "regenerate_reason", "regenerateReason")),
        ("Pre-Conditions", _coalesce_row_value(row, "pre_conditions", "preConditions")),
        ("Test Procedure", _coalesce_row_value(row, "test_procedure", "testProcedure")),
        ("Expected Result", _coalesce_row_value(row, "expected_result", "expectedResult")),
    ]
    body = "\n".join(f"- {label}: {value}" for label, value in fields)
    return (
        "## Source Workbook Row (authoritative context for split analysis)\n"
        "Use Test Group Theme as the feature/topic context. Consider Test Set, "
        "Test Item, Pre-Conditions, Test Procedure, and Expected Result together "
        "before deciding whether this requirement needs 1 or multiple TCs.\n"
        f"{body}"
        f"{_format_sibling_section(row)}"
    )



_MULTI_TC_GUIDANCE = """
## Splitting Policy (strictly follow ASPICE SWE.6 rules loaded above)

Return as many TCs as the rules require — **no upper cap**. The number of TCs
is driven entirely by what the requirement mandates, not by an arbitrary limit.

Apply these authoritative rules from `ASPICE_SWE6_AI_Instruction.md`:

- **§6.1 Test Item** — If the requirement can be validated by more than
  one scenario, EACH distinct scenario is its own TC. `tc_title` is the
  single scenario-identifying field (mandatory, 2–14 words; arrow form,
  natural sentence, or scenario tag) and MUST visibly distinguish siblings — e.g.
  `Initial sync at 5,000 → all entries on HU`,
  `Initial sync > 5,000 → count capped at configured maximum`.
- **§10.2 Keyword-Driven Scenario Decomposition** — Identify the key concepts
  in the requirement (limits, per-device rules, order-preservation, stop
  conditions, etc.) and ensure **every keyword maps to at least one TC**.
  A concept with no TC coverage is a gap that must be closed by adding a TC.
- **§9 False Pass prevention** — When the requirement explicitly lists
  multiple supported items (file formats, device types, markets, input
  classes, etc.), produce ONE TC per item. Never combine them. e.g. supported
  video formats `.mp4 / .avi / .mpg / .wmv / .3gp / .mkv` → 6 separate TCs.
- **§10.2 Branch Checklist** — Scan for implicit branches the
  requirement rarely states explicitly (unknown / private / withheld values,
  before-vs-after states, boundary =/>/<, negative paths, concurrency,
  persistence after reboot) and add TCs for each that the requirement covers.
- **§7.6 Baseline Comparison** — When a TC involves before/after comparison,
  that TC's procedure must establish a baseline before the change action.

Splitting decision tree:
1. Does the requirement enumerate supported items (§9)? → one TC per item.
2. Does it describe multiple distinct scenarios / conditions / boundaries?
   → one TC per scenario (§6.1).
3. Does it imply extended branches (unknown / error / negative)?
   → add TCs for each covered branch (§10.2, plus Design Method guide).
4. Only a single atomic behaviour with no branches? → return exactly one TC.

Additional hard constraints:
- Each TC is self-contained: its own pre-conditions, procedure, expected result.
  NEVER write "same as TC1 but…" cross-references.
- `design_method` for each TC is assigned AFTER its procedure + expected_result
  are finalized — judged from the ACTUAL flow, not the requirement text. Use
  §15 first-match on PRIMARY intent (negative → fault → state → decision →
  EP → BVA → combinatorial → scenario → functional). Prefer the short English
  label; the system will normalize it to the canonical dropdown value. Cross-ref:
  `Test Case Design Method 判斷規則.md`.
- Every TC must pass the §11 11-item self-check in the instruction doc.
"""


def build_multi_tc_user_prompt(
    row: dict,
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for multi-TC-per-req generation (single row input)."""
    spec_context = _get_spec_context(row, spec_index)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    source_row = _format_source_workbook_row(row, context)
    return f"""## Context
- Project: {context['project']}
- Test Group Theme: {context['test_group']}

{source_row}

## Spec Context
{spec_context}{rules_section}
{_MULTI_TC_GUIDANCE}
## Output
Return a JSON object with these top-level keys:
- `reasoning` (string, 繁體中文): 用 **2–5 句**完整說明你對此需求的解讀，
  讓 reviewer 不必回去看原文就能對齊判斷。內容必須涵蓋下列元素，按
  以下順序組織（每點 1 句即可，缺項則略過）：
    1. **驗證目標**：此 TC（或這組 TC）核心要驗證的行為或外顯結果是什麼。
    2. **關鍵情境條件**：觸發行為的前置狀態 / 輸入 / 模式（呼應 §6.1 trigger
       必帶條件的精神）。能寫多項就條列。
    3. **為什麼這樣切**：
       - 若 `tcs` 長度 = 1（原子需求）：用一句說明為什麼一筆 TC 已足夠涵蓋
         （例：「無分支、無列舉項、無狀態切換，單一場景即可完整驗證。」）。
         **不要寫「不需拆分」這種空話**，要點出*為什麼*不需拆。
       - 若 `tcs` 長度 ≥ 2：明確引用驅動拆分的 ASPICE 節號（§6.1 / §9 /
         §10.2 等），並指出拆分維度（格式 / 狀態 / 輸入分群 / 失敗類型 …）。
    4. **未涵蓋或刻意略過的部分**（optional, 僅當有取捨時寫）：說明哪些相鄰
       場景被 sibling rows 接走、或因 spec 未明確而留給後續 review。

  範例（原子）：「驗證 Dealer Mode 切換 Engineering Configuration 開關後，
  系統參數於 disable 時還原為預設值。觸發點為使用者在 Dealer Mode UI
  按下 toggle，前提是當前已是 enable 狀態並有自訂值。單一狀態切換、無
  列舉項，因此一筆 TC 即可完整覆蓋；後續 power cycle 行為由其他需求接手。」

  範例（拆分）：「驗證系統可上傳並播放 spec 列舉的 6 種影片格式
  (.mp4/.avi/.mpg/.wmv/.3gp/.mkv)。觸發點為使用者在 Showroom 模式下選擇
  USB 中對應格式檔案。依 §9 列舉項規則拆為 6 筆 TC，避免單筆「supported
  formats」造成 False Pass（任一格式靜默失敗時也會通過）。Codec 內部解碼
  細節（例如 H.265 vs H.264）非本需求範圍，由媒體框架層需求驗證。」

  用途：讓 reviewer 一眼確認 AI 對需求的理解、判斷取捨、與拆分依據是否
  與自己一致；也作為 audit trail 紀錄 AI 的決策邏輯。
- `keywords` (array, optional): keyword analysis per §10.2, each entry
  `{{"keyword": "...", "meaning": "<繁中>", "covered_by": [1, 2]}}` where the
  numbers are 1-based indices into `tcs`.
- `duplicate_of` (string, OPTIONAL — strict criteria): set to the **row
  number string** of a sibling listed in the **Sibling Rows** section
  (e.g. `"duplicate_of": "11"` for a sibling shown as `[row #11]` —
  digits only, no `row` prefix), ONLY when this row is **truly equivalent**
  to that sibling. STRICT criteria — ALL of these MUST match the sibling,
  not just some:
    - Same trigger (same action AND same precondition / state)
    - Same observable outcome
    - Same input data category
    - Same verification target
  If only the *procedure* or *Test Set* overlaps, or the trigger / outcome
  differs in any way (different state, different mode, different data
  bucket), DO NOT mark `duplicate_of` — those are sibling scenarios, not
  duplicates. When in doubt, omit the field. Leave the field absent or
  empty when there are no siblings or no true duplicate.
- `distinguishing_axis` (object, REQUIRED when sibling rows exist; OMIT
  otherwise): forces an explicit declaration of how this row differs from
  its siblings, so reviewers can audit close-but-not-duplicate cases.
  Shape: `{{"axis": "<one of: trigger_state, input_data, timing, boundary,
  mode, none>", "delta": "<繁體中文一句話，描述 THIS 列 vs. sibling 的
  具體差異>"}}`. Rules:
    - `axis: "none"` ⇔ true duplicate; `duplicate_of` MUST also be set in
      the same response. Mismatch (one set, the other not) is invalid.
    - `delta` MUST contain a concrete token (state name / value / mode /
      boundary keyword) that ALSO appears in this row's `tc_title`. Vague
      sentences like 「不同的驗證情境」 are rejected.
    - When there are no siblings, omit this field entirely.
- `tcs` (array): produce as many TCs as the rules require — do not collapse
  distinct scenarios to save output. Each TC object has keys: {output_keys}.
  `tc_title` is MANDATORY for every TC (§6.1) regardless of whether the
  requirement was split.

All output fields English for workbook-bound TC content. Traditional Chinese
is allowed only for analysis fields such as `reasoning` and keyword
`meaning`.

Do NOT invent unstated values or data points. If the requirement/spec/reviewer
pre-fill does not provide an exact number, limit, threshold, dataset, state,
code, or other concrete detail, preserve the ambiguity explicitly instead of
guessing. Use abstract wording such as configured/per spec when the source
implies a configurable value but does not state the literal number.

Example (requirement that enumerates 3 supported formats would return 3 TCs):
{{"reasoning": "§9 列舉 3 種格式，各一筆 TC 避免 False Pass 風險。",
  "keywords": [
    {{"keyword": "supported formats", "meaning": "系統允許的影片格式",
      "covered_by": [1, 2, 3]}}
  ],
  "tcs": [
    {{... TC for format 1 ...}},
    {{... TC for format 2 ...}},
    {{... TC for format 3 ...}}
  ]}}

Before emitting, run the WRITING DISCIPLINE self-check listed in the system
prompt for EVERY TC. Every TC must have a non-empty `tc_title` (§6.1)."""


def build_test_set_classification_prompt(
    reqs: list[dict],
    test_group: str | None = None,
) -> str:
    """Rows 分成若干 Test Set 的 prompt（per-row identity preserved）。

    Args:
        reqs: list of dicts. Each item supplies a unique key via `id`
            (preferred row-level UUID) or `req_id` (fallback when caller
            intentionally classifies at requirement level), plus `test_item`.
            When the same `req_id` appears across multiple rows with
            different `test_item` content, pass distinct `id`s so each row
            is classified independently rather than collapsing.
        test_group: 當前 workbook 的 Test Group（例如 "Bluetooth"、"DeviceManager"）。
            傳入後 AI 會被明確要求 label 不要再重複這個 feature 前綴。

    Returns:
        User prompt 字串，AI 需回 JSON
        `{"assignments": [{"id": "...", "test_set": "..."}, ...]}`，`id`
        為呼叫端提供的唯一 key（row uuid 或 req_id）。
    """
    items = []
    for i, r in enumerate(reqs, 1):
        test_item = str(r.get("test_item") or "").strip().replace("\n", " ")
        if len(test_item) > 400:
            test_item = test_item[:397] + "..."
        current_test_set = str(r.get("current_test_set") or "").strip()
        hint = f" (current Test Set hint: {current_test_set})" if current_test_set else ""
        # 優先用 row-level id；缺則退回 req_id（向後相容）。req_id 仍以
        # metadata 欄位附帶，讓 AI 看得出哪些列來自同一需求。
        key = str(r.get("id") or r.get("req_id") or "").strip()
        req_id_meta = str(r.get("req_id") or "").strip()
        req_meta = (
            f" (req {req_id_meta})"
            if req_id_meta and req_id_meta != key
            else ""
        )
        items.append(f"{i}. [{key}]{req_meta} {test_item}{hint}")
    body = "\n".join(items)

    group_clean = (test_group or "").strip()
    if group_clean:
        group_context = (
            f'\n\n## Feature group context\nAll requirements below belong to the '
            f'Test Group **"{group_clean}"**. This is ALREADY recorded in a '
            f'separate column — do NOT repeat it in the Test Set label. For '
            f'example, with Test Group = "Bluetooth", use labels like '
            f'`Connection`, `Pairing`, `Power Control`, `Device List` — NOT '
            f'`BT Connection`, `Bluetooth Pairing`, `BT Switch`.\n'
        )
    else:
        group_context = ""

    return f"""## Task
Group the following requirements into coherent **Test Sets**. A Test Set is a
short thematic label (typically 1–3 words, English) that captures the
**functional capability** the requirement belongs to — NOT the specific
sub-flow, UI element, or action verb.{group_context}

Rules for choosing labels:
- **Group by capability, not by sub-action.** When several requirements
  describe different steps or UI paths of the same capability, label them
  with the shared capability. Examples:
    * "Pairing", "Auto-reconnect", "Manual connect", "Disconnect" →
      all belong to one Test Set: "Connection"
    * "Enable", "Disable", "Toggle state" → one Test Set: "Power Control"
      (or "Switch" if that is the capability under test, not a widget name)
    * "Add device to list", "Remove device from list", "Show paired list"
      → one Test Set: "Device List"
- **Do NOT prefix the label with the feature/module name** (e.g. "BT",
  "Bluetooth", "DeviceManager", "HMI"). The feature group is tracked in a
  separate column; labels should describe the capability WITHIN that group.
- If a requirement includes a `current Test Set hint`, treat it as reviewer /
  workbook context, not a binding answer. Preserve it when it already matches
  the capability-level grouping; otherwise merge, rename, or regroup it to
  make the whole workbook taxonomy consistent.
- Derive labels from what the requirements actually describe; do NOT invent a
  fixed taxonomy up front, but DO zoom out one level: ask "what user-facing
  capability is this exercising?" rather than "which screen or button?".
- Requirements that exercise the same capability MUST share the same Test Set
  label, even if they touch different UI entry points or sub-states. Aim for
  5–15 requirements per label when the data supports it; avoid splitting a
  capability into Pairing / Reconnect / Disconnect unless the CFTS really
  only covers one of them.
- If unsure between a narrow label and a broader shared capability, default to
  the broader capability.
- Single-req Test Sets are allowed ONLY when the requirement is a genuine
  outlier that doesn't fit any capability shared with other reqs. Otherwise
  merge it into the closest related capability.
- Prefer short noun phrases (no trailing "Testing", no "Req-xxx" placeholders,
  no generic words like "Feature" or "Function" alone).
- Every requirement must be assigned exactly one Test Set — no empty, no
  "None", no "Unclassified", no "Misc", no duplicates on the same req_id.

## Requirements
{body}

## Output
Return ONLY valid JSON (no markdown fences):
{{"assignments": [
  {{"id": "<exact id from the bracketed prefix>", "test_set": "<short label>"}},
  ...
]}}

The `id` MUST match the bracketed prefix verbatim. The `(req <req_id>)` suffix
is metadata only — do NOT echo it back as the `id`. Each input line MUST
appear exactly once in the output; the array length must equal the input
count ({len(reqs)})."""


def build_multi_tc_batch_prompt(
    rows: list[dict],
    context: dict,
    spec_index: dict | None,
    rules_text: str,
) -> str:
    """Build user prompt for multi-TC batch generation (N rows → N TC arrays)."""
    items = []
    for i, row in enumerate(rows):
        spec_context = _get_spec_context(row, spec_index)
        source_row = _format_source_workbook_row(row, context)
        item = (
            f"### Requirement {i + 1}\n"
            f"{source_row}\n"
            f"- Spec: {spec_context}"
        )
        items.append(item)
    batch_text = "\n\n".join(items)
    output_keys = ", ".join(REQUIRED_OUTPUT_KEYS)

    rules_section = f"\n\n## Rules\n{rules_text}" if rules_text else ""
    return f"""## Context
- Project: {context['project']}
- Test Group: {context['test_group']}
- Test Set: {context.get('test_set', 'N/A')}

## Requirements
{batch_text}{rules_section}
{_MULTI_TC_GUIDANCE}
## Output
Return a JSON object `{{"requirements": [...]}}`; the outer array has exactly
one entry per input requirement, in the same order. Each entry has the shape:
`{{"req_id": "...", "reasoning": "<繁中>", "keywords": [...], "tcs": [...]}}`
- `reasoning` (繁體中文，2–5 句): 完整說明對該需求的解讀，依序涵蓋：
  (1) 驗證目標、(2) 關鍵情境條件 / 觸發、(3) 為何切成這個 TC 數
  （原子需求要說「為什麼一筆已足夠」，例：「無分支、無列舉、無狀態切換」；
  拆分需引用 §6.1 / §9 / §10.2 等節號並指出拆分維度）、(4) 若有刻意略過
  的相鄰場景或交給 sibling rows 接手者，請點出。**禁止只寫「不需拆分」
  這種空話**。目的：讓 reviewer 不必回去看原文就能對齊判斷，亦做為 audit
  trail。
- `keywords` (optional): per-req keyword analysis (§10.2),
  `{{"keyword": "...", "meaning": "<繁中>", "covered_by": [1, 2]}}`.
- `duplicate_of` (string, optional, STRICT): the **row number string** of
  a sibling row this row is truly equivalent to (same trigger / outcome /
  input bucket / verification target). For `[row #11]` write
  `"duplicate_of": "11"`. Omit when there are no siblings or no exact
  duplicate. Used to flag rows for reviewer-side deletion; partial
  overlaps must NOT be marked.
- `distinguishing_axis` (object, REQUIRED when this requirement has
  siblings; OMIT otherwise): explicit declaration of how this row differs
  from its siblings. Shape: `{{"axis": "<trigger_state|input_data|
  timing|boundary|mode|none>", "delta": "<繁中一句話，含具體 token>"}}`.
  `axis: "none"` ⇔ `duplicate_of` set (mismatch is invalid). `delta`
  must cite a concrete token that also appears in this row's `tc_title`.
- `tcs`: as many TC objects as the rules demand (no cap).
Each TC object has keys: {output_keys}. `tc_title` is MANDATORY for every
TC (§6.1), regardless of whether the requirement was split.

Example (requirement 1 enumerates 6 formats → 6 TCs; requirement 2 is atomic → 1 TC):
{{"requirements": [
  {{"req_id": "REQ-001",
    "reasoning": "§9 列出 6 種支援格式，各一筆 TC。",
    "keywords": [], "tcs": [{{...}}, {{...}}, {{...}}, {{...}}, {{...}}, {{...}}]}},
  {{"req_id": "REQ-002",
    "reasoning": "單一原子行為，不需拆分。",
    "keywords": [], "tcs": [{{...}}]}}
]}}

Before emitting, run the WRITING DISCIPLINE self-check listed in the system
prompt for EVERY TC in EVERY requirement group. Every TC must have a
non-empty `tc_title` (§6.1)."""
