# Data Request — SW Update (FOTA) Test Case Development

- **From**: Pei (SW Test / SWE.6, SW Update feature)
- **Date**: 2026-08-28
- **Subject**: Two data requests blocking system-level test case authoring for FOTA / SW Update
- **Open items**: DR-SU1 (1 requirement), DR-SU2 v2 (3 sub-requests)

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

Two requirements have external consequences that we cannot separate from an adjacent
requirement's consequences. Both are currently `PENDING`.

| Requirement | Title | What we cannot distinguish | What would resolve it |
|---|---|---|---|
| `SWE1-FOTA-179` | Start Silent Update Download Automatically | The automatic download request is indistinguishable from the overall silent background execution already covered by `SWE1-FOTA-175` — both present as "no user action, update completes on its own" | Either an observable sign that the download request was issued, **or** your confirmation that this requirement's verification may be folded into `175` |
| `SWE1-FOTA-181` | Start Silent Update Installation Immediately After Download | The qualifier "**immediately** after download" requires (i) the download-completion instant to be observable and (ii) a timing threshold for "immediately". Neither exists | Either an observable download-completion indication and a timing threshold, **or** your confirmation that the timing qualifier is not to be verified |

**We are not merging requirements on our own initiative.** Folding one requirement's
verification into another is a specification-side decision; if that is the right answer,
we need it from you.

**Note on scope**: this category is **not bounded by the 106 figure in §3.3**.
`SWE1-FOTA-181` does not belong to that population — its verification criteria do
mention external behaviour, so it was never in that set, yet it is still not fully
verifiable. **The size of this category has not been surveyed.**

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
| DR-SU2 (c) | Distinguishing means for `SWE1-FOTA-179` and `SWE1-FOTA-181` | 2 test cases, 5 placeholders |
