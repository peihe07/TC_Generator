# RD-1 Questions — FW036 Media HMI TC Regeneration

Open questions for the requirements author, raised during regeneration of the
FW036 SWQT test case specification (rows 333+, 262 leaf FRs from
FMWIFSM037A03, sourced from Media HMI spec chapters 11–23).

Full detail for every item is in `tcgen_package/ANOMALIES.md` under the same
anomaly id. The **Impact** column is generated from the linter's JSON report,
not maintained by hand — it says what changes if you answer.

Status at time of writing: **171 TCs generated, 0 lint findings, 2 parents
blocked, 6 assumption markers.**

---

## Summary — five groups

| Group | Items | Why it matters |
|---|---|---|
| **1. Missing referenced artefacts** | A-009, A-015, A-016 | Two consecutive Pop Up List ids and one table are cited but do not exist. One leaf is fully blocked; a second is at risk. Strong evidence of a **Pop Up List version mismatch**, which is one answer that unblocks several items at once. |
| **2. Spec self-contradictions** | A-011, A-012, A-018, A-007 | Two clauses give opposite answers for the same situation, or prose contradicts its own table. One leaf blocked, 6 TCs generated on a declared reading that must be reworked if we read it wrong. |
| **3. Container naming defects (ch18)** | A-021, A-023 | The same popup has two names, and one clause names the wrong container (a circular "close and return to itself"). 9 TCs affected. |
| **4. Coverage gaps — 037 allocated no leaf** | A-008, A-010, A-020 | Spec tables and clauses with real content that no requirement leaf covers, so no TC can be written against them. Not blocking; these are **holes in the deliverable** you may want closed. |
| **5. Clause numbering / duplication** | A-013, A-017, A-019, A-022 | Three independent numbering gaps and two duplicated clause pairs in one deck. Raised as a **pattern**, not as three edits. |

---

## Group 1 — Missing referenced artefacts (answer these first)

These unblock generation.

| Id | Spec anchor | Question | Working assumption | Impact |
|---|---|---|---|---|
| **A-009** | 13.2 / `SMP1` | `SMP1) See Pop Up List: PU0996` — PU0996 is not in `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023)` (all 3 sheets, 1340 ids searched). Is PU0996 a typo pointing at the wrong id, **or** is it defined in a Pop Up List revision newer than Dec 2023? | None — parent is blocked. The clause delegates 100% of its content to the missing definition, so writing a TC would mean inventing the popup. | **BLOCKED:** `SWE1-MEDIA-COM-051-01`. Answering unblocks 1 leaf. |
| **A-015** | 18.1 / `APP1` | `APP1 … (See Pop up List: PU0997)` — PU0997 is **also** absent from the same file. Two *consecutive* ids missing while PU0998 in the same range is present. Is the Dec 2023 Pop Up List simply older than these two popups? | Treated as supplementary: APP1 states its own testable content, so RAD-070 generates normally (see `docs/framework.md`, delegation-proportion rule). | No TC blocked. But a "yes" here **also answers A-009** and unblocks COM-051. |
| **A-016** | 16.2.3.1 / `PRE2.3.1` | `(See Table PRE1.2)` — there is no Table PRE1.2. `PRE1.2` is a clause about the plus sign; the only table in the section is `PRE1.1) Presets per Bank by Radio Size`, which states no bank count. Should this read Table PRE1.1, or is a bank-count table missing from the deck? | The values 3 and 6 are taken from the PRE2.3.1 sentence itself. | No TC blocked. Answer confirms whether the numbers have a second source. |

**Recommended single question for this group:** *"Is the Dec 15 2023 Pop Up List
the current revision for this programme? Two ids we cite (PU0996, PU0997) are
absent from it."*

---

## Group 2 — Spec self-contradictions

Each of these was resolved with a **declared reading** so generation could
continue. If you rule the other way, the listed TCs are reworked.

| Id | Spec anchor | Question | Working assumption | Impact |
|---|---|---|---|---|
| **A-011** | 14.1.1.1 `BT1.1.1` vs 14.1.1.2 `BT1.1.2` | For a connected source with no valid audio files, BT1.1.1 says Browse Tab is **not** available and BT1.1.2 says it **is** (for USB/Disc). The page image shows BT1.1.1's "USB or Disc is inserted" struck out and broadened to "a source is connected" — did that edit forget to carve out USB/Disc? | specific-over-general: BT1.1.2 governs USB/Disc. BT1.1.1's residual scope has no instantiable subject, so its leaf is blocked. | **BLOCKED:** `COM-058-01`. **ASSUMPTION:** `COM-059-01`, `COM-059-02`. |
| **A-012** | 14.1.6 `BT1.6` vs 14.1.2.1 `BT1.2.1` | BT1.6 says the cursor **always** begins at the top of the list; BT1.2.1 says that for Presets / All Stations it begins at the currently tuned station. Is BT1.6's "always" meant to exclude those two lists? | specific-over-general: BT1.2.1 governs Presets / All Stations. The general TC is scoped to a USB track list so it stays unambiguous either way. | **ASSUMPTION:** `COM-061-01`, `COM-061-04`. |
| **A-018** | 17.1.1 `MPB1.1` vs Table `PRE1.1` | MPB1.1 allows a **maximum of 8** presets per bank; Table PRE1.1 caps every listed radio size at **6**. A bank of 8 is unreachable on any configuration. | table-over-prose (same canon as A-007): verified against the Table PRE1.1 value for the vehicle radio size. | **ASSUMPTION:** `RAD-062-01`. |
| **A-007** | 12.2.1 `PSB2.1` vs Table `PSB2.4` | PSB2.1 allows a **maximum of 5** pinned sources; Table PSB2.4 caps every radio size at **4**. Same shape as A-018. | table-over-prose. TCs express the limit symbolically as "the value defined for this radio size in Table PSB2.4", so they hold under either answer. | No marker — the TCs are valid either way. |

**Recommended single question for this group:** *"When a prose clause and its
own referenced table disagree on a limit, which is authoritative?"* — that one
ruling settles A-007 and A-018 together.

---

## Group 3 — Container naming defects (ch18)

ch18 describes four preset containers across the deck (Playing Tab Mixed
Presets Bank, Browse Presets List, Presets Pop-up, Edit Presets Pop-up). Test
cases must state which container each observation is made in, so container
names being wrong or ambiguous directly produces false-passing tests.

| Id | Spec anchor | Question | Working assumption | Impact |
|---|---|---|---|---|
| **A-021** | 18.1 `APP1` vs `APP2`, `APP10`–`APP13`, `APP17`, `APP18` | The popup is called **"All Presets Pop up"** in APP1 and **"Presets Pop Up"** everywhere else (including the page-30 screenshot caption). Same screen or two? If one, which name is canonical? | One container; each TC uses 037's own wording for its clause. | **ASSUMPTION:** all 5 of `RAD-070-01..05`. |
| **A-021** (second, narrower) | 18.1 `APP1` | APP1 lists a "Presets Shown" indicator as part of this popup, but in the screenshots that indicator appears on the **Edit Presets Pop Up**. Which is correct? | Followed APP1's text. | **ASSUMPTION:** `RAD-070-03` specifically. If the screenshot is right, **this TC verifies an object that does not exist in that container** and must be rewritten or withdrawn. |
| **A-023** | 18.8 `APP13` | *"The **Presets Pop Up** will have a 'Done' button and an [X] which both close the popup and return to the **Presets Pop Up** screen"* — circular as written. Should the first one read "Edit Presets Pop Up"? | Yes — 037's four leaves and the page-30 screenshots both place Done/X on the Edit Presets Pop Up. Two sources against one self-contradictory clause. | **ASSUMPTION:** `RAD-078-01..04`. |

---

## Group 4 — Coverage gaps (037 allocated no leaf)

These are not blockers and need no ruling to proceed. They are reported because
**no test case can exist for them**: with no requirement leaf there is no
req_id, and with no req_id there is no workbook row to write against. If these
configurations are in scope for FW036, 037 needs leaves for them.

| Id | What has no leaf | Note |
|---|---|---|
| **A-008** | Table PSB2.4: 4 of 7 radio sizes (7", 10.25", 12"L, 12"P). Both **max-3** configurations — the more interesting boundary — are uncovered. Table PSB2.3: 4 of 5 market variants (EMEA / LATAM / APAC / APAC-China). | Only NAFTA and three radio sizes are covered. |
| **A-010** | Table SMP2.2: 12"L and 12"P have no leaf; 7" and 10.25" are marked **N/A** with no stated meaning (no popup? no limit? unspecified?). Three readings give three different expected results. | The two N/A configurations are explicitly out of scope in the generated TC. |
| **A-020** | `MPB1.7` (HD Radio preset labels — **NA-relevant, a real gap**) and `MPB1.8.x` (FM-EU PSN labels — please confirm out of scope for a NAFTA programme). | These sit under a leaf about *layout*, so they cannot be attached to it without recording label requirements as layout requirements. |
| **A-013** | If BT4.1.1's missing item **2** was a real field, nothing covers it. | See Group 5. |
| **A-017** | If APP5–APP9 were real clauses, nothing covers them. | See Group 5. |

---

## Group 5 — Numbering gaps and duplicated clauses (pattern-level)

| Id | Spec anchor | Observation |
|---|---|---|
| **A-013** | 14.4.2 `BT4.1.1` | Field list runs **1), 3), 4)** — item 2 absent, in both the page image and the SYS1 export. |
| **A-017** | ch18 `APP` | Clauses run APP1–APP4, then **APP10**–APP18. APP5–APP9 absent. |
| **A-019** | ch17 `MPB` | Clauses run MPB1.1, 1.2, 1.3, 1.3.1, **1.5**, 1.5.1 … MPB1.4 absent. |

**Main question (pattern, not three edits):** *three independent numbering holes
in one deck — please confirm whether these are deliberate deletions or
omissions, and whether the deck has a known history of clauses being removed
without renumbering.* Each hole is a place where a requirement may have been
dropped silently; a single audit is more useful to us than three point fixes.

| Id | Spec anchor | Observation | Impact |
|---|---|---|---|
| **A-022** | 18.5 `APP10` ≡ 18.12 `APP17`; 18.6 `APP11` ≡ 18.13 `APP18` | Two clause pairs state the same requirement twice (APP10 adds a 500 ms figure APP17 omits; otherwise equivalent in trigger, input and verification target). 037 allocated a separate leaf to each. | Handled with `duplicate_of` rather than a second copy of the content; both leaves keep a workbook row for traceability, and the Remarks column flags the sync obligation. **Question:** are APP17/APP18 redundant restatements to be removed, or was a distinction intended that the wording lost? |
| **A-002**, **A-014** | 11.4.1.2 / 11.4.1.3; pages 25/26 | Duplicate item codes (`BTSA1.2` used twice; `BT4.2.1` used for two different clauses). Confirmed against page images — not OCR artefacts. The SYS1 R1L-L export already corrects the second one. | Informational. Outline numbers drive all mapping, so nothing is ambiguous in generation. Listed so a reviewer comparing against the 2023 PDF does not read the mismatch as our error. |

---

## Closed — no action needed

| Id | Resolution |
|---|---|
| **A-001** | 037 does not allocate a leaf to every SYS1 sub-section (10 of 158 affected). Handled in tooling; see `docs/framework.md` orphan coverage rule. |
| **A-003** | SYS1 (R1L-L Feb 2026) ↔ PDF (July 2023) version risk — closed by cross-check: 5 of 6 sampled done-region sections matched verbatim, 158/158 section numbers resolve. |
| **A-004** | No spec-confirmed control label for opening the App Drawer; step written without inventing one. Reviewer with HU access to confirm. |
| **A-005** | Done region (rows 10–332) uses `as the baseline` in recording steps, against §5.6. Frozen deliberately — rows 10–332 are out of scope for this regeneration. Count pinned at 8 in the test suite. |
| **A-006** | No enumerated USB drive-type list, so §7's negative-pair requirement has no trigger. Recorded as a question below. |

**A-006 question (low priority):** is there a defined set of drive types that
change the USB source label, and what label does a type outside that set get?
