# Project Profile — FW036 / R1L SWE1_BT (Stellantis Atlantis High)

> **PRECEDENCE: this profile OVERRIDES the generic ASPICE SWE.6 instruction
> wherever the two conflict.** Generic rules stay in force for everything this
> profile does not address. Rules tagged **[OVERRIDE]** replace a specific
> generic rule (the replaced rule is cited); rules tagged **[ADD]** are
> project-specific additions.

## 0. Project identity

- Program: Stellantis R1LR_Atl-H (Atlantis High platform), 25PI3.5 / SR26
- Deliverable workbook: FMWIFSM036A01 ("FW036"); author name: PeiPYHsu
- Scope: SWE1-level Bluetooth module verification (SWE1_BT series)
- TC ID format: `NR1L-BT-[nnn]`. Splits of an already-assigned ID use `a/b`
  suffixes (e.g. `NR1L-BT-156a` / `NR1L-BT-156b`) so existing sequence numbers
  are never displaced. New TCs continue from the last assigned number; never
  renumber existing rows.

## 1. Requirements authority chain [ADD]

- Traceability chain: SWRA (Software Requirements Analysis) → CFTS (Customer
  Functional Test Specification) → SYSAD (System Architectural Design) →
  FW036 TC.
- When SWRA AC content conflicts with CFTS clause content, **CFTS wins**
  (§10.1 principle). Treat the SWRA AC as a generic wrapper in that case.
- NEVER resolve a SWRA↔CFTS mismatch by inventing content: write the TC from
  the CFTS clause and flag the mismatch as an **RD-1 item** in `remarks`.
- Do not write TCs for a batch until the CFTS documents that batch needs are
  confirmed available. Missing clause text → BLOCKED placeholder (§8), never
  guesswork.

## 2. Test Set vocabulary [OVERRIDE — replaces free-form Test Set labeling]

`test_set` MUST be exactly one of this fixed list — no other labels, no
variants, no new labels:

- Adapter & Device
- Connection
- Pairing
- Phonebook (PBAP)
- Phone (HFP)
- Media (A2DP)
- Data Control
- IVI Integration

## 3. FW036 house style (field rules)

### 3.1 Test Item [OVERRIDE — restricts the English-only output rule]

- The original SWRA bilingual When/And/Case/Then block is preserved
  **verbatim** in the workbook Test Item cell; the English `tc_title` is
  appended below it in parentheses by the workbook writer.
- Never rewrite, translate, trim, or "clean up" the original bilingual block.
  `tc_title` itself remains English per generic rules.

### 3.2 Pre-Conditions [OVERRIDE — exception to the system-obvious ban]

- The FIRST pre-condition line is always exactly:
  `HU is powered on and in FULL OPERATION MODE`
  (The generic rule banning system-obvious pre-conditions is waived for this
  one fixed opening line only.)
- All other generic pre-condition rules (state-only, no actions, no
  checks/reads, no data-presence) still apply to the remaining lines.

### 3.3 Design Method [OVERRIDE — replaces the 9-label §12 table]

Only two values exist in this workbook. Return exactly one of these fixed
strings, character-for-character:

- `功能測試 (Functional based ; no specific technique)`
- `基礎故障注入 (Fault Injection Lite)`

Mapping: if the PRIMARY intent of the finalized flow injects a fault or
abnormal condition (adapter disable, link loss, invalid input, resource kill,
timeout, proxy-not-ready) → `基礎故障注入 (Fault Injection Lite)`; everything
else → `功能測試 (Functional based ; no specific technique)`.

### 3.4 Steps [ADD]

- Step count: normal TC 4–7 steps; exception/recovery TC up to ~8 steps.
- Recovery rule: an AC2 entry with 「並恢復」 in its Then clause (or recovery
  stated in Verification Method) gets an explicit recovery phase (restore
  action + re-verification) at the end of the SAME TC.
- No blank lines between procedure steps.
- No tail sentences like "confirming per SWE1_BT_xxx".

### 3.5 Expected Results [ADD]

- The final ER must close with concrete observable values (screen text,
  signal value, state string, count) — never with SWE sub-ID references.

### 3.6 Spec Reference (workbook column 14) [OVERRIDE — replaces §10.7 format]

Two valid formats ONLY:

1. **Short CFTS form** — for SWEs with direct CFTS coverage:
   `CFTS085-XXXXXXX` (document code + 7-digit clause ID)
2. **Full long SYS3 form** — for SWEs without CFTS coverage:
   `SYS3_BT_FM-WI-FSM-011-A01 系統架構設計 System Architectural Design_SYSAD_V03-SYS-RA-[ID]`
   (always the full long form — never a shortened SYS3 variant)

Spec Reference is always **looked up from FW036 column 14** — never inferred,
never constructed from spec filenames or section numbers. If the lookup value
is absent or unconfirmed, flag it in `remarks` and leave the reference
pending; do not invent one.

### 3.7 Remarks (output key `remarks`) [ADD]

Include ONLY when necessary; MANDATORY in these cases:

- Any reference to CFTS021 content → add a provenance note that the source is
  OCR of a scanned document (e.g. `Source: CFTS021 (OCR of scanned JPEG);
  wording verified against the scanned image.`)
- Any workaround for the dead-code APK buttons (§6) → note the dead-code
  reason and the substitute path used
- BLOCKED TCs (§8) and RD-1 flags (§1)

Otherwise return an empty string.

## 4. Split policy [ADD — batch-level operator decision]

`split_mode` is decided per batch by the operator and applies uniformly to the
WHOLE batch (all connect/disconnect states and all mode variants included):

- `standard` — generic ASPICE splitting rules apply unchanged.
- `max_granularity` (「极致拆」) — one verification point per TC:
  connect-state and disconnect-state are separate TCs; every mode variant
  (e.g. Repeat All / Repeat One / Shuffle) is a separate TC.

Fixed exception in BOTH modes (§7.7): an AVRCP control→command→display triad
for one user action is ONE TC (control on HU → AVRCP command observed →
display update) — never split the triad.

## 5. BT step-writing conventions [ADD]

- Adapter disable injection is ALWAYS `adb shell svc bluetooth disable`;
  recovery via `adb shell svc bluetooth enable`, verified with `logcat` and
  `dumpsys bluetooth_manager`.
- CAN signal wording: `Read the <Signal> value on CAN and record as
  <Var>_initial` / `<Var>_after` — never "on the CAN tool". BTSA source
  selection observes `STATUS_TELEMATIC.CurrentSource = 23` and
  `HFM_BlueTooth_1_Selected`.
- Timing: any async connect/disconnect call MUST be followed by an explicit
  wait step confirmed via the test-APK broadcast listener BEFORE any state
  query. Never put the async call and the state query in the same step.
- HU-side actions reference the REAL test-APK button labels (from
  `fragment_cpaa.xml`), e.g. `hfpClient.disconnect(device)`,
  `注册所有BT广播监听`, `刷新已配对列表` — never invented English labels.

## 6. Test APK facts (com.test.btapp, app-system-debug.apk) [ADD]

- System-signed, holds BLUETOOTH_PRIVILEGED. Fragments: Cpaa / Phone /
  Music (AVRCP) / Connection / Adapter / Contacts.
- Permanently dead-code buttons (render but do nothing): `deleteData`,
  `downloadContacts`, `downloadCallLog` → NEVER use them in steps; work
  around via PBAP connect/disconnect and add a `remarks` note (§3.7).
- `getHfpDevice()` returns null after HU adapter disable, so all
  call-control methods silently return void. HU adapter disable is therefore
  an INVALID injection point for call-state tests. Sole exception:
  SWE1_BT_070, which specifically targets the proxy-not-ready path.

## 7. Standard fixtures [ADD]

- RFCOMM/SPP tests: Serial Bluetooth Terminal (Kai Morich), SPP UUID
  `00001101` — the project-standard fixture (used by BT_121/122, BT_131/132).
- Known pending fixture: a BTSA source with Repeat genuinely unavailable
  (required to execute BT_149/150).

## 8. BLOCKED placeholder [ADD]

When a TC cannot be written (missing CFTS text, unresolved scope, missing
fixture):

- Keep the row and its assigned ID; fill the content fields with the BLOCKED
  placeholder format; `remarks` states the blocking reason and the RD-1
  escalation (rendered red-highlighted downstream).
- Out-of-batch (OOB) sub-capabilities are preserved as explicit placeholder
  rows (pattern: R151a, R152a).
- Prior BLOCKED decisions on record: BT_091/092, BT_101/102, BT_113/114.
