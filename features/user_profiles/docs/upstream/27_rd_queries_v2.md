# RD Queries — User Profiles (FW036) — for upstream despatch


<!-- fingerprint:begin -->
## 語料指紋（G-F，45 包）—— 標記輪次：**45**

> **本表是本檔之保鮮期。** 引用本檔前先跑：`stamp_static_doc.py --verify <本檔>`；
> **不符即「已過期，拒絕採信」**，須重出後再引。
> 指紋之範圍為**全欄**（保守）—— 誤判過期只是多重出一次，誤判新鮮則是拿舊資料下判斷。

| tc_id | digest |
|---|---|
| `NR1L-UserProfiles-017` | `6b4a62612255` |
| `NR1L-UserProfiles-020` | `a9e1265287c4` |
| `NR1L-UserProfiles-057` | `ba4460649b81` |
| `NR1L-UserProfiles-058` | `63ab6afdd115` |
| `NR1L-UserProfiles-059` | `6828f798a73d` |
| `NR1L-UserProfiles-060` | `7fd59e8962f7` |
| `NR1L-UserProfiles-061` | `d6c8ad3818d4` |
| `NR1L-UserProfiles-062` | `e1e1333848ca` |
| `NR1L-UserProfiles-063` | `bd5493966dc1` |
| `NR1L-UserProfiles-074` | `62751c9dc2bb` |
| `NR1L-UserProfiles-077` | `a68dc2c03602` |

<!-- fingerprint:end -->

> **Version 2 — 2026-08-18.** Supersedes `26_rd_queries.md` (version 1,
> 2026-08-18), which was withdrawn before despatch.
> Changes in this version: appendix leaf count corrected (X-1); unproven
> "shifted by one position" claim removed (X-2); source document now carries
> both its filename and its Source ID namespace (X-3).
> **Version 1 was never sent.**

- Prepared by: execution layer | **Tier 3 — to be sent by Pei**
- Scope of this despatch: **RD #5 and RD #6 only.**
  DR #3 and DR #7 were closed as **OUT-OF-SCOPE** by ruling R-U56 and are
  **not** part of this despatch.
- Both queries below share one property that qualifies them for despatch:
  **the leaf exists in 037, the test case is already written, and the answer
  changes what is already written.**

> **Note on scope (R-U56).** Where the specification contains content for
> which 037 has produced no requirement leaf, we do not raise a coverage gap
> and do not request clarification — deciding what ought to be a requirement
> belongs to SWE.1 / SWE.5, not to test-case authoring. The two queries below
> are of the opposite kind: they concern leaves that **do** exist.

## Source document (both queries)

One artifact, two identifiers — please note that these denote the **same**
document:

| | |
|---|---|
| **Filename** | `SYS1_HMI_Personal Account HMI Logic and Flow R1L-R (February 10 2023)` (`.xlsx` structure / `.pdf` body text) |
| **Source ID namespace** (as cited throughout 037) | `Personal_Account_HMI_Logic_and_Flow_R1_SR24_Post2A_CR24798_(October_03_2023)_{section}` |

We verified at intake that all 169 rows of the specification's `Source ID`
column fall inside the `CR24798 (October 03 2023)` namespace, and that the
135 unique section ids cited by 037 resolve into it with zero misses. Section
numbers quoted below are namespace section numbers.

---

## RD #5 — Scope of the "R1 High" account-label override

### Question

The specification carries a variant override note replacing the account label
for R1 High vehicles. **Does that override apply only to the single table row
it is anchored to, or to every occurrence of the same label in chapter 9?**

### Source and verbatim text

PDF page 14, note attached to Table EDPR1:

> `****R1 High Only: "Stellantis Account" to be replaced with
> "Connected Account"`

Note: this sentence exists **only in the PDF**. The corresponding `Description`
column of the 037 workbook has dropped it (recorded on our side in
`data/xlsx_missing_clauses.tsv`). A generation pass reading the workbook alone
would emit the wrong literal for R1 High vehicles.

### Positional evidence (coordinate re-location)

The `****` marker was located by coordinate measurement on PDF page 14:

| Item | Position |
|---|---|
| The `****` note itself | x = 101.4, y = 275.9 – 286.7 |
| The `****" Stellantis Account"` row inside Table EDPR1 | y = 289.8 |
| Every other row of Table EDPR1 | carries **no** `****` marker |

So the note is anchored, **on the page**, to that one row. What the layout
cannot tell us is whether the intent is row-level or chapter-wide.

### The two readings and what each affects

| Reading | Consequence |
|---|---|
| **(a) Row-level** — applies only to the Table EDPR1 entry | Current implementation. §9.1 and §9.2 keep their own literals (`Stellantis Connected Account`) |
| **(b) Chapter-wide** — applies to every same-named label in ch.9 | §9.1 and §9.2 expected results must be rewritten for R1 High |

### What changes if the answer is (b)

1. The variant-label rule in our lint (`VARIANT_LABEL_OVERRIDES`) must widen
   from the single row to the whole chapter.
2. The §9.2 case (`SWE1-HMI-PROF-088`) currently expects
   `no Stellantis Connected Account button are shown` — that literal changes.
3. The §9.1 case (`SWE1-HMI-PROF-085`) already uses `Connected Account` under
   an R1 High pre-condition, so **it would not need to change** — but its
   base-variant counterpart would need re-checking.

### Our current handling (unchanged until answered)

We preserve the ambiguity rather than resolve it. Each section keeps its own
verbatim literal, and the §9.2 case records in its remarks that both forms
denote the same button, and that this case verifies the button's **absence** —
for which the label form does not affect the verdict.

**No answer is blocking.** The question is asked because the answer would
change already-delivered content, not because work is stalled.

---

## RD #6 — Is the combination "region with the brand app × vehicle without connected-profile support" deployable?

### Question

Section 9.2 states two independent conditions. We have written one test case
per condition. **Can the second condition be observed in isolation on a real
vehicle** — that is, does a vehicle exist (or can one be configured) that is
in a region **with** the `<Brand>` app but **does not support** the connected
profile feature?

### Source and verbatim text

Section 9.2 (EDPR2):

> `Don't show the Connected Profile options/info or Stellantis Connected
> Account button for regions without the <Brand> app. Do not show Connected
> Profile options/info or Stellantis Connected Account button if the vehicle
> does not support the connected profile feature.`

Two conditions:

1. region without the `<Brand>` app
2. vehicle does not support the connected profile feature

### Why the question arises

The two conditions produce the **same** observable outcome. To keep the two
test cases distinguishable — so that a failure identifies **which** condition
did not take effect — the case for condition 2 carries the pre-condition

> `The vehicle is in a region with the brand app`

**That pre-condition is inferred, not stated by the specification.** The
specification never asserts that such a combination exists.

### Evidence that the two conditions are genuinely distinct

This is not merely a wording difference. Section 11.3 (CPA1) uses a different
term for a different thing:

> `The Connected Account line item will always be displayed on the "Edit
> Profile" tab if the vehicle is equipped with connectivity. Do not show if
> the vehicle does not support connectivity.`

`connectivity` (a hardware capability) and `the connected profile feature`
(a feature entitlement) are not the same. Section 9.2 itself proves it:
if "does not support the connected profile feature" meant simply "has no
connectivity", then condition 1 — *region without the app* — would have
nowhere to sit, since a connected vehicle in a region without the app still
lacks the feature.

### What changes with the answer

| Answer | Consequence |
|---|---|
| **The combination exists / is configurable** | No change. The test case is deployable as written; we would welcome the typical cause (trim, option package, telematics subscription state) for the pre-condition wording |
| **The combination cannot occur** | The test case is **not deleted** — condition 2 is written in the specification. Its remarks would instead record it as a **specified but non-deployable condition**, and we would raise a follow-up asking whether condition 2 is redundant wording |

**The test case is not deleted either way.** Whether a scenario can be staged
and whether a stated condition deserves verification are two different
questions.

---

## Appendix — 037 title/description mismatch at §12.8 / §12.8.1

**For upstream information only. This is not a request, and nothing is
blocked by it.**

Sections 12.8 and 12.8.1 are covered by **seven** leaves in the 037 workbook.
In **four** of the seven, the `Title` names a subject that belongs to a
**different** leaf's `Description`:

| Leaf | Section | `Description` subject | `Title` names instead | Whose description that is |
|---|---|---|---|---|
| `SWE1-HMI-PROF-125-03` | 12.8 | Status Bar interaction limited to Valet Profile and HVAC icons | Glove Box Lock prompt on Valet entry | `126-01` |
| `SWE1-HMI-PROF-125-04` | 12.8 | all non-interactable items greyed out | Glove Box Lock **button** greyed out | `126-02` |
| `SWE1-HMI-PROF-126-01` | 12.8.1 | PU0832 shown when prompting to enter Valet Mode | lock-out of specific menu areas | `125-02` (in part) |
| `SWE1-HMI-PROF-126-02` | 12.8.1 | Glove Box Lock button rendered greyed-out | Status Bar restrictions and grey-out | `125-03` (in part) |

The remaining **three** are consistent — each title names a subject that is
present in its own description:

| Leaf | Section | Title | Note |
|---|---|---|---|
| `SWE1-HMI-PROF-125-01` | 12.8 | Device Manager Disabled in Valet Mode | consistent, though it names only the exception clause of its description (whose main clause is "only HVAC and Media remain accessible") |
| `SWE1-HMI-PROF-125-02` | 12.8 | Disable Projection, HFP, and VR in Valet Mode | consistent, though its description also covers the locked-out menu areas |
| `SWE1-HMI-PROF-126-03` | 12.8.1 | Electronic Glove Box Lock Logic in Valet Mode | consistent |

**We describe this only as a mismatch, not as a pattern.** We have not
established that the titles are displaced by a fixed offset, and the four
rows above do not form one: `125-03` and `125-04` take their titles from the
12.8.1 group, while `126-01` and `126-02` take theirs from the 12.8 group.
Whether this arose from a single editing operation is not something our
evidence can show.

The clearest single indicator that the titles cannot be authoritative:
`125-03` is a section **12.8** leaf, but its title describes a glove box
prompt — and section 12.8 (PVAL8) does not mention the glove box at all;
the glove box is section 12.8.1.

### Our handling — no impact on delivered content

We take the `Description` column as the requirement unit and the `Title`
column as an index label. That decision is evidence-based, measured across
all 180 leaves of this feature:

| Measure | Result |
|---|---|
| Descriptions beginning with the specification clause id (`PVAL8.)` etc.) | **105 / 180** |
| Titles beginning with a clause id | **0 / 180** |
| Descriptions whose first 60 characters appear verbatim in the clause | **120 / 180** |
| Average vocabulary coverage against the clause text | Description **0.859** vs Title **0.667** |

The decisive argument is not statistical: for section 12.8 (PVAL8), the four
leaves' **descriptions** partition the clause's six assertions with no overlap
and no omission. Titles cannot do this — under a title-as-unit reading, the
clause's "status bar interaction is limited" assertion would have no leaf at
all, while the glove box prompt would have two.

All seven test cases for these leaves were generated from the descriptions,
and their test-case titles were authored by us rather than copied from 037,
so the mismatch does not propagate into delivered content.

**The only residual effect is for a human using 037 titles as an index** —
in these two sections, the title will lead to the wrong leaf.

Whether to correct the workbook is entirely upstream's call.
