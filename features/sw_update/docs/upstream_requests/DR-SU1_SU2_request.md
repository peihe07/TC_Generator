# Data Request — SW Update (FOTA) Test Case Development

- **From**: Pei (SW Test / SWE.6, SW Update feature)
- **Date**: 2026-08-28
- **Subject**: Two data requests blocking system-level test case authoring for FOTA / SW Update
- **Open items**: DR-SU1 (1 requirement), DR-SU2 v3 (4 sub-requests), DR-SU3 (2 requirements), **DR-SU4 (6 requirements — highest priority)**, DR-SU5 (1 requirement + 1 facet)
- **Revision**: 2026-08-29 — DR-SU2 (c) now lists three requirements (`184` added);
  DR-SU2 (d) added (trigger means for `315`/`318`); DR-SU3 added (umbrella requirements)

---

## 1. Background

We are authoring system-level test cases for the SW Update (FOTA) feature against
`SoftwareUpdate_FM-WI-FSM-037-A03` (311 in-scope requirements) and
`CFTS_057 Reflash`. Test cases must be executable on a bench: every step and every
expected result has to name something a tester can actually observe.

Two gaps block that. Both are properties of the source documents, not of our method,
and neither can be closed by re-reading what we already hold — we have exhausted the
material available to us (evidence in §4).

Where a step cannot be written, we mark it `PENDING` rather than inventing an
observation. **We do not guess at log tags, diagnostic DIDs, service interfaces or
timing thresholds.** The `PENDING` markers stay in the deliverable until this request
is answered, so the gaps remain visible rather than silently filled.

---

## 2. DR-SU1 — Safety-related notification conditions during a silent update

**Requirement**: `SWE1-FOTA-176` (and `CFTS057-4907477`) states that during a Silent
Update the update service shall allow user notification **only when required to
satisfy safety-related requirements**.

**Gap**: Neither document enumerates which conditions are safety-related.

**What we need**: The list of safety-related conditions that permit a notification
during a silent update session — ideally as a specification-side condition table
(a supplement to CFTS_057, or the relevant SYSAD safety requirements section).

**Impact**: One test case (`newR1L-SU-003`) currently carries three `PENDING`
placeholders and is not executable. Its procedure requires a step that brings one
safety-related condition into effect; without the list, no such step can be written.

**Priority**: High — this is in the first authored batch.

---

## 3. DR-SU2 v2 — Observability at system test level

### 3.1 What has been resolved

`Error_Code_List.xlsx` (approved for use on 2026-08-28) supplies the **negative path**:
80 error codes across the update stages (Precondition, Package Header check & unpack,
Rollback Protection, Security check, Install M-CPU / V-CPU / SXM). Where an update
fails, is interrupted or is rejected, there is now a named code to expect.

**This request is therefore reduced, not withdrawn.** Three items remain.

### 3.2 (a) How error codes are surfaced on the head unit — **required to use the codes above**

We have the codes; we do not know where a tester reads them. The error code list
header says "After HU start-up, suddenly …", which suggests an on-screen presentation,
but the route is not stated.

**What we need**: For each code (or for the list as a whole) — is it shown on a screen,
in a pop-up, in an engineering/service menu, or only in a log? If a screen: which one,
and what triggers it?

**Impact**: Until answered, every test step that would read a code stays `PENDING`.
The codes are usable as *expected values* but not yet as *observations*.

### 3.3 (b) Positive-state observation for the Wi-Fi FOTA session

`Error_Code_List.xlsx` covers the **USB / SWDL** path and only the failure side. For the
Wi-Fi FOTA path we still have no defined observation for the in-progress states:
session establishment, download in progress, Download Descriptor parsing.

**What we need**: Any of — a log tag list, a diagnostic DID table, a service interface
definition, or a mapping from these internal states to an indirect HMI consequence.

**Impact**: 5 requirements are confirmed to have no external observable at all
(`SWE1-FOTA-363` – `367`, Telematics Client). A further population of up to 106
requirements matches the same profile but has **not yet been assessed row by row** —
the 106 is an upper bound on this category, not a count of confirmed cases.

### 3.4 (c) Means of distinguishing two specific requirements

Three requirements have external consequences we cannot separate from an adjacent
requirement's consequences, or qualifiers we cannot measure. All three are currently
`PENDING`.

| Requirement | Title | What we cannot distinguish | What would resolve it |
|---|---|---|---|
| `SWE1-FOTA-179` | Start Silent Update Download Automatically | The automatic download request is indistinguishable from the overall silent background execution already covered by `SWE1-FOTA-175` — both present as "no user action, update completes on its own" | Either an observable sign that the download request was issued, **or** your confirmation that this requirement's verification may be folded into `175` |
| `SWE1-FOTA-181` | Start Silent Update Installation Immediately After Download | The qualifier "**immediately** after download" requires (i) the download-completion instant to be observable and (ii) a timing threshold for "immediately". Neither exists | Either an observable download-completion indication and a timing threshold, **or** your confirmation that the timing qualifier is not to be verified |
| `SWE1-FOTA-184` | Apply Silent Update Rules Across All Session Flows | The requirement states the silent rules apply "across update check, deployment package download and installation processing". On a bench the three phases have **no observable boundary** — a silent update shows nothing on screen, so nothing marks where the check ends and the download begins. Each individual violation this requirement would catch (prompt, progress notification, confirmation screen) is already covered by the test cases for `175`, `180` and `182` | Either an observable way to tell the three phases apart, **or** your confirmation that this requirement's verification may be folded into `SWE1-FOTA-175` |

**We are not merging requirements on our own initiative.** Folding one requirement's
verification into another is a specification-side decision; if that is the right answer,
we need it from you.

**Note on scope**: this category is **not bounded by the 106 figure in §3.3**.
`SWE1-FOTA-181` does not belong to that population — its verification criteria do
mention external behaviour, so it was never in that set, yet it is still not fully
verifiable. **The size of this category has not been surveyed.**

### 3.5 (d) Means of *triggering* two conditions on the bench — **not** means of observing them

Two requirements describe conditions we can observe the outcome of, but **cannot bring
about** on a test bench. This is the opposite problem from §3.3: there we can make it
happen but cannot see it; here we can see it but cannot make it happen.

| Requirement | Title | What we cannot trigger | What would resolve it |
|---|---|---|---|
| `SWE1-FOTA-315` | Socket Read/Write Error Handling | A socket read or write error during OTA server communication. The outcome is observable (the update does not complete and the head unit stays operable); we have no way to inject the error | A fault-injection tool or a test mode that forces a socket read/write failure during an update session |
| `SWE1-FOTA-318` | Emergency State Handling | The vehicle emergency state (accident detection). We have no accident-detection signal available on the bench, and this feature has no CAN database binding, so we cannot construct one | A means of placing the vehicle into the emergency state on the bench — a test mode, a simulated signal with a documented name and value range, or a bench procedure |

**We will not fabricate a signal.** Naming a CAN signal we cannot trace to a source
document would put an invented value into a delivered test case.

**Two further requirements need the same kind of answer — a way to make an update
fail:**

| Requirement | Title | What we cannot trigger | What would resolve it |
|---|---|---|---|
| `SWE1-FOTA-093` | ROV Rollback Pop-up | An ROV update that fails **and then rolls back successfully**. The outcome is observable (a "Reverted" pop-up); we cannot cause the failure | A bench procedure or test mode that makes an ROV update fail with a successful rollback |
| `SWE1-FOTA-094` | ROV Failure Pop-up | An ROV update that fails **without a successful rollback**. The outcome is observable (a "Walk Home Scenario" pop-up); we cannot cause the failure | The same, for the no-rollback case |

These two are the same shape as `315`/`318`: **we know what to look for, we cannot
bring it about.** Note that the two need to be distinguishable from each other — one
requires the rollback to succeed, the other requires it not to.

---

## 3A. DR-SU3 — Confirmation that two requirements' verification may be folded in

Two requirements are written as *umbrella* statements: they say a component shall
coordinate the handling of conditions that are themselves defined in other requirements,
and they list those requirements by ID.

| Requirement | Title | Lists | What we are asking |
|---|---|---|---|
| `SWE1-FOTA-313` | Interruption Condition Coordination | `4907667`–`4907672` (the six interruption conditions, i.e. `SWE1-FOTA-315`–`320`) | Whether this requirement's verification is fully covered by the test cases for those six, or whether it has a verification point of its own we have missed |
| `SWE1-FOTA-327` | Download Resume Condition Handling | `4907683`, `4907684` (i.e. `SWE1-FOTA-328`, `329`) | The same question |

**Why we are asking rather than deciding.** Taking `313` apart sentence by sentence,
everything it states is carried by the six requirements it lists, or by
`SWE1-FOTA-358` (status reporting). What remains is the coordination itself — and we
could not identify any situation where all six pass individually yet coordination fails,
that is also grounded in the wording of `313`. But **folding one requirement's
verification into others is a specification-side decision**, not ours to make.

If you confirm, these requirements will have no test case of their own and we will
record where their coverage sits. If you disagree, please tell us what `313` and `327`
verify that their listed requirements do not.

---

## 3B. DR-SU4 — What counts as "handled" for an interruption, and how to judge it on a bench

**High priority — this blocks all six interruption-handling test cases.**

`SWE1-FOTA-315` through `320` each require the system to *detect and handle* an
interruption (socket error, network loss, user-disabled network, emergency state,
power loss, host disconnection). We can trigger four of the six and observe that the
update does not complete. **What we cannot determine from the specification is what
"handled" looks like from outside the head unit.**

### 3B.1 Request 1 — the observable form of "the OTA client continues operation"

`CFTS057-4907673` states, immediately before Table 4-6:

> These are RECOMMENDED actions; however the interrupts themselves **shall be
> gracefully handled so that the OTA client continues operation**.

This is the closest requirement we found to a pass criterion, and its timing matches
(it is about the interruption itself, not about recovery afterwards). **But its subject
is the OTA client, and a system test observes the head unit.**

The only requirement we found about the head unit is `CFTS057-4907440`:

> OTA client shall be a low priority process **when active** such that it does not
> impact normal functionality of the host system (ex, navigation/radio shall not be
> impacted).

Its subject matches, but its timing does not — it governs the normal path while an
update is running, not the state after an interruption.

**The two requirements each cover one half and their scopes do not overlap.** We are
not willing to combine them into a statement neither document makes.

**Please confirm:** what is the observable indication, on the head unit, that
"the OTA client continues operation" after an interruption?

### 3B.2 Request 2 — how to judge when the phase of the interruption cannot be determined

Table 4-6 prescribes different actions depending on the session state when the
interruption occurred:

| State when interrupted | Action | Software version afterwards |
|---|---|---|
| Before / during management session | Abort, retry at next polling interval | unchanged |
| During download session, before update agent starts | Save state, abort, **retry when the vehicle recovers** | may change |
| **During deployment or update process** | **Complete the deployment** | **changes** |

A silent update displays nothing, so **there is no external indication of which phase
the update was in when the interruption occurred.** The tester can neither choose the
phase nor determine afterwards which one applied.

Our test cases therefore cannot assert that the software version is unchanged: a system
that follows the third row is compliant, and that assertion would fail it.

**Please confirm:** at system test level, how should correct interruption handling be
judged, given that the tester can neither control nor determine which phase the
interruption fell in?

### 3B.2a Addendum (2026-08-30) — one boundary has since been found, and it is narrower than the request

An embedded object in CFTS057 (`4908702`, a Wi-Fi download session flow chart that is
not part of the document text) states three thresholds verbatim:

- `T = 5 minutes since last data received`
- `T = 30 minutes after timed mode has expired`
- a retry counter `I`, reset at `0`, with the user prompted at `I => 7`

and, for an interruption, `HU shall terminate the download session for the duration of
ignition cycle with increment in counter, I += 1` (or `… and reset the counter, I = 0`).

**This tells us when a download session ends. It does not tell us which phase an
interruption fell in.** It also applies to the Wi-Fi download path only, while
`4907673` is written for interruptions in general, including USB and cellular. We are
therefore not treating these values as an answer to Request 2, and we are not carrying
them over to other paths.

**Request 2 remains open, restated narrowly:** outside the Wi-Fi download path, and at
the boundary between the download session and deployment, how should correct
interruption handling be judged at system test level?

**One inconsistency we need resolved before we can use the 30 minutes at all:**
requirement `SWE1-FOTA-057` measures it as the *session duration* within the current
ignition cycle, while the flow chart measures it *from the expiry of timed mode*. These
are two different waits on the bench.

### 3B.3 What we did instead, pending your answer

We removed the version comparison from the pass criterion and kept it as a recorded
value. The pass criterion itself is now marked `PENDING` in all six test cases.
**None of the six is deliverable until this is answered.** We would rather hand you
six visibly blocked test cases than six that quietly pass the wrong thing.

---

## 3C. DR-SU5 — Bench procedure for comparing two update types on one head unit

`SWE1-FOTA-131` requires the WiFi Update Service to retrieve the update type
configuration from the server and **control the applicable update flow according to
that configuration**. What this requirement owns is not the behaviour of any one update
type — those belong to other requirements — but the fact that **the server's setting
determines which flow is applied**.

Verifying that needs **two runs of the same head unit against campaigns of different
types**, because one campaign carries one type. The second run has to start from a
state comparable to the first, and here we are stuck:

1. Nothing in the material we hold describes a rollback or downgrade procedure.
2. **Rollback Protection is itself a requirement area for this feature** — a system
   whose requirements are to *prevent* rollback is not one where we may assume the
   bench can roll back.
3. Even if a rollback were possible, **nothing in the specification lets us confirm
   that the head unit is back in a state equivalent to before the first run** — and
   without that, a difference between the two runs cannot be attributed to the update
   type rather than to leftover state.

**Request 1**: When the same head unit is run against two campaigns of different update
types in sequence, how should the two starting states be made comparable — a clean
reflash, two head units, or another procedure?

**Request 2**: The same requirement also states that the HMI shall provide a
**consistent user interaction flow across the supported update types**. We have not
written a test case for that part, because "consistent" is not defined. **Which aspects
must be identical across update types, and which are allowed to differ?**

We have marked the test case `PENDING` rather than writing a step we cannot execute.
The wording we used is "return the head unit to a comparable starting state" rather
than "restore the previous software version", so that your answer is not constrained
to a downgrade.

---

## 4. Evidence — the diagnostics side has been exhausted

Before raising §3.3, we checked every diagnostics-side source available to us for a
FOTA / OTA / software-update observation definition:

| Source | Scope examined | FOTA / OTA / SW-update observation definitions found |
|---|---:|---:|
| `DTCs Matrix Core List Rev. 1.6.xlsx` | 254 DTCs | **0** — no CFTS057 among the lead CFTS entries |
| `CFTS_004 General Diagnostic Requirements` (Jun 2026) + SYSAD | 554 objects / 168 DIDs / 112 routines | **0** — `FOTA` appears only in the SYSAD abbreviation table; `OTA` only in an SXM package-swap NRC |
| `SWE1_Diagnostics_V1.xlsx` (037 A03) | 395 requirement rows | **0** — the single hit was a false positive on a buzzer row |

This is a complete enumeration of what we hold, not a sample. If a diagnostics
definition for FOTA exists, it is in a document we have not been given.

---

## 5. Attachments

1. `Error_Code_List.xlsx` — the approved error code list (for reference; already held)
2. `ERROR_CODES.md` — our transcription, 80 codes with stage and platform qualifiers
3. The three sources listed in §4, if the enumeration needs to be re-checked

---

## 6. Summary of what is requested

| # | Request | Blocks |
|---|---|---|
| DR-SU1 | List of safety-related notification conditions for silent updates | 1 test case, 3 placeholders |
| DR-SU2 (a) | How error codes are surfaced on the head unit | Every step that reads a code |
| DR-SU2 (b) | Positive-state observation for the Wi-Fi FOTA session | 5 confirmed rows, up to 106 in the same profile |
| DR-SU2 (c) | Distinguishing means for `SWE1-FOTA-179`, `181` and `184` | 3 test cases, 8 placeholders |
| DR-SU2 (d) | **Trigger** means for `SWE1-FOTA-315`, `318`, `093` and `094` | 4 test cases, 12 placeholders |
| DR-SU3 | Confirmation that `SWE1-FOTA-313` and `327` fold into the requirements they list | 1 test case, 3 placeholders (`327` not yet drafted) |
| **DR-SU4** | **What "handled" looks like on the head unit, and how to judge it when the interruption's phase is undeterminable** | **6 test cases — none deliverable** |
| DR-SU5 | Bench procedure for comparing two update types on one head unit; definition of "consistent" across types | 1 test case, 3 placeholders; 1 facet not drafted |
