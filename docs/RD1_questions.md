# RD-1 Questions — FW036 Media HMI TC Regeneration

| | |
|---|---|
| Prepared | 2026-08-07 |
| Prepared by | Pei (SWQT, FW036 Media HMI) |
| Sent to | _(fill in: RD author / requirements owner)_ |
| Sent on | _(fill in)_ |
| Response received | _(fill in)_ |

Open questions for the requirements author, raised during regeneration of the
FW036 SWQT test case specification (rows 333+, 262 leaf FRs from
FMWIFSM037A03, sourced from Media HMI spec chapters 11–23).

Full detail for every item is in `tcgen_package/ANOMALIES.md` under the same
anomaly id; the work each answer triggers on our side is queued in
`docs/pending_passes.md`, so a ruling becomes a work order rather than a
re-investigation. The **Impact** column is generated from the linter's JSON report,
not maintained by hand — it says what changes if you answer.

Status at time of writing: **171 TCs generated, 0 lint findings, 2 parents
blocked, 6 assumption markers, 1 open question affecting 76 TCs (Group 0).**

---

## Summary — five groups

| Group | Items | Why it matters |
|---|---|---|
| **0. Radio tier — blocks a mechanical fix to 76 TCs** | **A-026**, A-025(a) | The Media Tab Button is labelled `"Playing"` on R1 High and `"Playing: Source"` on R1 Low. **76 of 171 generated TCs use the literal `"Playing"`.** The done region uses both forms, so it cannot settle the question. Answer this first — it is one sentence for you and 76 rows for us. |
| **1. Missing referenced artefacts** | A-009, A-015, A-016 | Two consecutive Pop Up List ids and one table are cited but do not exist. One leaf is fully blocked; a second is at risk. Strong evidence of a **Pop Up List version mismatch**, which is one answer that unblocks several items at once. |
| **2. Spec self-contradictions** | A-011, A-012, A-018, A-007 | Two clauses give opposite answers for the same situation, or prose contradicts its own table. One leaf blocked, 6 TCs generated on a declared reading that must be reworked if we read it wrong. |
| **3. Container identity and naming** | A-021, A-023, A-030 | One set of presets is shown in **five** containers whose contents genuinely differ. Two clauses name containers wrongly or ambiguously, and it is unresolved whether ch18's and ch23's "All Presets Pop up" are the same screen. 9 TCs carry markers. |
| **4. Coverage gaps — 037 allocated no leaf** | A-008, A-010, A-020 | Spec tables and clauses with real content that no requirement leaf covers, so no TC can be written against them. Not blocking; these are **holes in the deliverable** you may want closed. |
| **5. Clause numbering / duplication** | A-013, A-017, A-019, A-022 | Three independent numbering gaps and two duplicated clause pairs in one deck. Raised as a **pattern**, not as three edits. |

---

## Group 0 — Radio tier (answer this first)

This is the highest-impact question in the document: one sentence from you
resolves a mechanical change to 76 test cases.

`4.2 (MN2)` defines the Media Tab Button label as **`"Playing"` (R1High Only)**
or **`"Playing: Source"` (R1Low Only)**. Every test case that navigates to that
tab must press the right label.

**We could not determine the tier from the inputs, and we did not guess in the
document — but generation had already anchored on the done region, which turns
out to use both forms:**

| Form | Done-region TCs (rows 10–332, human-authored) |
|---|---|
| `"Playing"` (R1 High) | `SWE1-MEDIA-COM-001-05`, `COM-002-02` |
| `"Playing: <source>"` (R1 Low) | `SWE1-MEDIA-COM-014-01`, `COM-032-01` (×3) |

Evidence in both directions:

| Points to R1 **Low** | Points to **mixed / High** |
|---|---|
| SYS1 export is `R1L-L` | Spec 1.2: deck "covers requirements for R1 High and Low radios" |
| CFTS input is `R1LR_Atl-H` | Workbook covers `HDCC27`/`DT27` (**Atl-Hi**) and five **Atl-Mi** models |
| Spec 1.9 lists exclusions specific to `R1L-R` | All 322 done-region rows set every vehicle flag (T–Z) to `1` |

**The strongest evidence is that the workbook contradicts itself.** Two facts
about rows 10–332 cannot both be right:

- Those rows use **both** tab-button labels — so the label is being treated as
  tier-specific.
- All 322 of those rows set **every** vehicle flag (T–Z, covering both Atl-Hi
  and Atl-Mi models) to `1` — so every TC is being declared applicable to every
  model regardless of tier.

If the label is tier-specific, the flags should not be uniformly `1` on the rows
that hard-code one form. If the uniform flags are correct and every row applies
to every model, then no row should hard-code a tier-specific label at all.

This reframes the question. It is not that we failed to determine the vehicle
tier — it is that **the established practice in this workbook has never ruled on
it**, and the eight done-region rows carrying a hard-coded label are themselves
awaiting that ruling. Our 76 rows are not a new error; they extend an existing
undecided convention, and this is the first time it has been raised.

**Questions:**

1. **Which of the seven vehicle models in the workbook are R1 High, and which
   are R1 Low?**
2. If the fleet is mixed, how should a tier-dependent UI label be written in a
   test case that applies to all seven models — the workbook has no
   tier-specific mechanism today beyond the per-model flag columns.
3. **A third axis, same ruling (A-029):** `23.9 (MW9)` reads *"for all R1
   radios **except R1 Low 7\"**"*, so screen size matters within a tier, not
   just the tier. `23.8 (MW8)` adds another R1 Low-specific rule. **Please give
   the tier *and* screen size for each of the seven models** — one matrix
   settles A-026's 76 TCs, SA19.x's applicability, and whether
   `SWE1-MEDIA-INT-034` (5 TCs, swipe gestures) applies to every model. Those
   5 TCs currently set all vehicle flags to `1` per existing workbook
   convention, flagged in their Remarks as pending this answer.
4. Secondary, same ruling: `SA19.x` Virtual Venue is marked *(R1H Only)*. Is it
   in scope for any model in this programme? (If yes, see A-025 in Group 4 and
   the missing profiles document in Group 1.)

**Impact:** `A-026` — **76 of 171 generated TCs** contain the literal
`"Playing"` label. Under a "R1 Low" or "mixed" answer they need the label
changed; the change is mechanical and cheap once the ruling lands, which is why
we are holding rather than guessing.

---

## Group 1 — Missing referenced artefacts (answer these first)

These unblock generation.

| Id | Spec anchor | Question | Working assumption | Impact |
|---|---|---|---|---|
| **A-009** | 13.2 / `SMP1` | `SMP1) See Pop Up List: PU0996` — PU0996 is not in `Pop Up List HMI R1 SR24 Post 2A (Dec 15, 2023)` (all 3 sheets, 1340 ids searched). Is PU0996 a typo pointing at the wrong id, **or** is it defined in a Pop Up List revision newer than Dec 2023? | None — parent is blocked. The clause delegates 100% of its content to the missing definition, so writing a TC would mean inventing the popup. | **BLOCKED:** `SWE1-MEDIA-COM-051-01`. Answering unblocks 1 leaf. |
| **A-015** | 18.1 / `APP1` | `APP1 … (See Pop up List: PU0997)` — PU0997 is **also** absent from the same file. Two *consecutive* ids missing while PU0998 in the same range is present. Is the Dec 2023 Pop Up List simply older than these two popups? | Treated as supplementary: APP1 states its own testable content, so RAD-070 generates normally (see `docs/framework.md`, delegation-proportion rule). | No TC blocked. But a "yes" here **also answers A-009** and unblocks COM-051. |
| **A-025(b)** | 21.15 / `SA19.2`, 21.16 / `SA19.3` | Both delegate to **`Virtual_Venues_Profiles_V1.0`** for venue names and venue info popup content. That document is not among our inputs. Same class as the missing Pop Up List ids: even if 037 gains leaves for these clauses, no TC can be written without the file. | None — no leaf exists yet either. | Blocks any future Virtual Venue coverage. Only relevant if the answer to Group 0 puts R1H models in scope. |
| **A-016** | 16.2.3.1 / `PRE2.3.1` | `(See Table PRE1.2)` — there is no Table PRE1.2. `PRE1.2` is a clause about the plus sign; the only table in the section is `PRE1.1) Presets per Bank by Radio Size`, which states no bank count. Should this read Table PRE1.1, or is a bank-count table missing from the deck? | The values 3 and 6 are taken from the PRE2.3.1 sentence itself. | No TC blocked. Answer confirms whether the numbers have a second source. |

**Recommended single question for this group:** *"Is our input set complete and
current? Two Pop Up List ids we cite (PU0996, PU0997) are absent from the
Dec 15 2023 revision, and `Virtual_Venues_Profiles_V1.0` — cited by SA19.2 and
SA19.3 — was never supplied to us."*

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

| **A-032** | 20.3 `FF2` vs 22.2.1 `AP2.1` | FF2 says a USB inserted with nothing selected **will automatically play**, with no condition attached; AP2.1 says that **if AutoPlay is OFF** it will not. Should FF2 read "…and AutoPlay is ON"? | specific-over-general (third instance of the canon, after A-011 and A-012): AP2.1 names the setting and sits in the chapter that owns it. `PLA-087-01` states AutoPlay ON in its Pre-Condition so it holds either way; the OFF case is covered by AP2.1's own leaf (`PLA-094-01`). | No marker — scope convergence, not a bet. |

**A pattern worth naming:** A-011, A-012 and A-032 are the same drafting shape —
a general clause written without the qualifier that a more specific clause
elsewhere supplies. Three instances suggests reviewing for others rather than
fixing these three.

**Recommended single question for this group — stated as a position to confirm,
not an open problem to re-solve:**

> *"Where a prose clause and its own referenced table disagree on a limit, we
> are treating the **table** as authoritative — it is the more specific source
> and is broken down per configuration. Please confirm, or tell us to use the
> prose figure instead."*

One ruling settles A-007 and A-018 together. Phrasing it this way keeps the
cost of agreeing to a single word, and puts our working assumption formally on
record if no answer comes back.

---

## Group 3 — Container identity and naming

**The full picture: one set of presets, five containers, three unresolved
identity questions.** The same stored presets are displayed in the Playing Tab
Mixed Presets Bank (ch17), the Browse Presets List (ch16), the Presets Pop-up
and Edit Presets Pop-up (ch18), and the Media Widget with its own popup (ch23).
Their contents differ in ways that matter — the Browse Presets List has delete
buttons the Mixed Presets Bank does not; an unsaved slot shows a *greyed* delete
button in one container and *no* delete button in another; the same indicator
reads `"Number of Presets Shown"` in one and `"Presets Shown"` in another.

Test cases therefore have to state which container each observation is made in,
and quote that container's own strings. Where the deck names containers
inconsistently, that discipline produces confident-looking but wrong tests —
which is why these are grouped and asked together.

| Id | Spec anchor | Question | Working assumption | Impact |
|---|---|---|---|---|
| **A-021** | 18.1 `APP1` vs `APP2`, `APP10`–`APP13`, `APP17`, `APP18` | The popup is called **"All Presets Pop up"** in APP1 and **"Presets Pop Up"** everywhere else (including the page-30 screenshot caption). Same screen or two? If one, which name is canonical? | One container; each TC uses 037's own wording for its clause. | **ASSUMPTION:** all 5 of `RAD-070-01..05`. |
| **A-021** (second, narrower) | 18.1 `APP1` | APP1 lists a "Presets Shown" indicator as part of this popup, but in the screenshots that indicator appears on the **Edit Presets Pop Up**. Which is correct? | Followed APP1's text. | **ASSUMPTION:** `RAD-070-03` specifically. If the screenshot is right, **this TC verifies an object that does not exist in that container** and must be rewritten or withdrawn. |
| **A-030** | 23.7 `MW8` vs 18.1 `APP1` | Both chapters open an "All Presets Pop up" from an "All Presets" button — one from the Media Widget, one from the Playing Tab. The page-38 screenshot of the widget's popup shows **no "Edit Presets" button**, which ch18's has per APP12. Two different screens, or one screen presented differently depending on entry point? | Neither assumed. ch23 TCs verify only what ch23 states and import no APP behaviour (§8.4.2); container anchoring uses the **entry path** (*"the popup opened from the 'All Presets' button in the Media Widget"*) rather than a name, which holds under either reading. | No marker — the ambiguous element was excluded from the verification target rather than resolved. |
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
| **A-025** *(feature-level — not a table row or a sub-clause, a whole settings block)* | **21.13 Radio Off with Door** — no gating stated anywhere, no leaf, and page 34 shows it as a complete settings screen with On/Off. This one is an unambiguous gap. | Nine ch21 sections have no leaf; the other eight are classified in ANOMALIES.md as either not-a-gap (21.11, see A-024) or gated-and-undetermined (Beats Audio, Virtual Venue — both moved to Group 0/1). Only 21.13 is reported as a plain omission. |
| **A-027** | `22.2.2 (AP2.2)` — *"if user listens to iPod and then plugs it in, the system will continue playing the item selected **if AutoPlay is ON**"* — has no leaf, while its own child `22.2.2.1` (the AutoPlay **OFF** case) does. | The exception is covered and the primary case is not. **Question:** should AP2.2 gain a leaf? |
| **A-031** | `23.3.2 (MW3.2)` — the **first** line of widget metadata (song title or frequency; HD sub-station format `106.7-2 HD`) — has no leaf, while the second line (MW3.3), the empty case (MW3.4) and the consistency rule (MW3.1) all do. | Same shape as A-027. **This is also the second uncovered HD Radio rule**, after `MPB1.7` in A-020. **Question:** should MW3.2 gain a leaf — and is HD Radio in scope for FW036 at all? One answer covers both holes. |
| **A-013** | If BT4.1.1's missing item **2** was a real field, nothing covers it. | See Group 5. |
| **A-017** | If APP5–APP9 were real clauses, nothing covers them. | See Group 5. |
| **A-006** *(low priority)* | 11.3.1 / `USB1` names only iPod as a label-changing drive type and enumerates no supported set, so §7's "enumerated items need a negative pair" has no trigger to fire on. | **Question:** is there a defined set of drive types that change the USB source label, and what label does a type outside that set get? |

---

## Group 5 — Numbering gaps and duplicated clauses (pattern-level)

| Id | Spec anchor | Observation |
|---|---|---|
| **A-013** | 14.4.2 `BT4.1.1` | Field list runs **1), 3), 4)** — item 2 absent, in both the page image and the SYS1 export. |
| **A-017** | ch18 `APP` | Clauses run APP1–APP4, then **APP10**–APP18. APP5–APP9 absent. |
| **A-019** | ch17 `MPB` | Clauses run MPB1.1, 1.2, 1.3, 1.3.1, **1.5**, 1.5.1 … MPB1.4 absent. |
| **A-028** | ch23 `MW` | `MW8` labels **two** unrelated clauses (23.7 All Presets button, 23.8 CarPlay placement), and the two sub-clauses indented under the first one are numbered `MW7.1` / `MW7.2` while a separate `MW7` exists at 23.6. |

**Main question (pattern, not four edits):** *four independent numbering or code-reuse defects
in one deck — please confirm whether these are deliberate deletions or
omissions, and whether the deck has a known history of clauses being removed
without renumbering.* Each hole is a place where a requirement may have been
dropped silently; a single audit is more useful to us than three point fixes.

| Id | Spec anchor | Observation | Impact |
|---|---|---|---|
| **A-022** | 18.5 `APP10` ≡ 18.12 `APP17`; 18.6 `APP11` ≡ 18.13 `APP18` | Two clause pairs state the same requirement twice (APP10 adds a 500 ms figure APP17 omits; otherwise equivalent in trigger, input and verification target). 037 allocated a separate leaf to each. | Handled with `duplicate_of` rather than a second copy of the content; both leaves keep a workbook row for traceability, and the Remarks column flags the sync obligation. **Questions:** (a) are APP17/APP18 redundant restatements to be removed, or was a distinction intended that the wording lost? (b) **Does the 500 ms long-press duration in APP10 apply to APP17 as well?** We have assumed it does and used 500 ms in both TCs — if the answer to (a) is "a distinction was intended", that assumption becomes unsupported and the duration for APP17 is undefined. |
| **A-002**, **A-014** | 11.4.1.2 / 11.4.1.3; pages 25/26 | Duplicate item codes (`BTSA1.2` used twice; `BT4.2.1` used for two different clauses). Confirmed against page images — not OCR artefacts. The SYS1 R1L-L export already corrects the second one. | Informational. Outline numbers drive all mapping, so nothing is ambiguous in generation. Listed so a reviewer comparing against the 2023 PDF does not read the mismatch as our error. |

---

## For reviewers only — no ruling needed

| Id | What to know |
|---|---|
| **A-033** | Display order and play order differ in USB folder browse and both are correct. Display (`FB2.1`): folders, then playlists, then songs, each alphabetical. Play (`FF4` and the page-32 examples): the current folder's own songs **first**, then its subfolders. For a root holding `Pop`, `Rock`, `Dancing`, `Get Low`, the list shows Pop, Rock, Dancing, Get Low while playback runs Dancing, Get Low, then Pop's contents, then Rock's. Both rules have leaves and TCs; the scenario tags say which order each TC verifies. |

## Closed / for information

Audience note: everything above is for the requirements author. The two items
below are not — they are listed so nobody mistakes them for our errors.

| Id | Audience | Resolution |
|---|---|---|
| **A-002**, **A-014** | Reviewers comparing our TCs against the 2023 PDF | Duplicate item codes in the source (`BTSA1.2` used for two clauses; `BT4.2.1` used for both the "No items" clause and the List Display Reference table). Confirmed against the page images — not OCR artefacts, and the SYS1 R1L-L export already corrects the second one. Outline numbers drive all our mapping, so nothing is ambiguous in generation. |
| **A-003** | Supports the Group 1 version argument | SYS1 (R1L-L, Feb 2026) ↔ PDF (July 2023) version risk was cross-checked and closed: 5 of 6 sampled done-region sections matched verbatim, and all 158 remaining section numbers resolve. The source *text* is consistent across the two revisions — which is why the missing Pop Up List ids in Group 1 point at the Pop Up List specifically, not at a general version drift. |
| **A-004** | A tester with HU access, not the RD author | No spec-confirmed control label for opening the App Drawer, so the step is written as "Open the App Drawer" rather than inventing a quoted label. Someone with the unit should supply the real label. |

Internal tooling and process decisions taken during regeneration (orphan
sub-section routing, the frozen §5.6 deviation in rows 10–332, and others) are
recorded in `tcgen_package/ANOMALIES.md` and need no input from the
requirements author.
