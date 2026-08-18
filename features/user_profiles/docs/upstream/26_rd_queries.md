> **WITHDRAWN — superseded by `27_rd_queries_v2.md` (2026-08-18).**
> **This version was never sent.** It is kept for the record only.
> Three defects were found at review before despatch (27 包 X-1／X-2／X-3):
> the appendix said *seven* leaves were displaced while listing four;
> it asserted an unproven `shifted by one position` pattern;
> and it identified the source document by filename only, without the
> `CR24798 (October 03 2023)` Source ID namespace that 037 cites.
> **Do not send this file.**
>
> **G-F（45 包）之處置：本檔不標指紋。**
> 指紋標的是「仍供人據以判斷之文件」；本檔已 WITHDRAWN 且從未寄出，
> 標了指紋反而會使它看起來像一份可用之現行文件。
> 其現行版為 `27_rd_queries_v2.md`（已標指紋）。

# RD Queries — User Profiles (FW036) — for upstream despatch

- Prepared by: execution layer | 2026-08-18 | **Tier 3 — to be sent by Pei**
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

---

## RD #5 — Scope of the "R1 High" account-label override

### Question

The specification carries a variant override note replacing the account label
for R1 High vehicles. **Does that override apply only to the single table row
it is anchored to, or to every occurrence of the same label in chapter 9?**

### Source and verbatim text

Document: `Personal Account HMI Logic and Flow R1L-R (February 10 2023)`,
PDF page 14, note attached to Table EDPR1:

> `****R1 High Only: "Stellantis Account" to be replaced with
> "Connected Account"`

Note: this sentence exists **only in the PDF**. The corresponding `Description`
column of the 037 workbook has dropped it (recorded in
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

1. `VARIANT_LABEL_OVERRIDES` in our lint rule (`lint_variant_labels.py`)
   must widen from the single row to the whole chapter.
2. The expected result of the §9.2 case (`SWE1-HMI-PROF-088`) currently reads
   `no Stellantis Connected Account button are shown` — the literal would change.
3. The §9.1 case (`SWE1-HMI-PROF-085`) already uses `Connected Account` under
   an R1 High pre-condition, so **it would not need to change** — but its
   base-variant counterpart would need re-checking.

### Our current handling (unchanged until answered)

We preserve the ambiguity rather than resolve it (§8.4.1, *ambiguous source →
preserve ambiguity*). Each section keeps its own verbatim literal, and the
§9.2 case records in its remarks that both forms denote the same button, and
that this case verifies the button's **absence** — for which the label form
does not affect the verdict.

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

Document: same as above, section 9.2 (EDPR2):

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

## Appendix — 037 title/description misalignment at §12.8 / §12.8.1

**For upstream information only. This is not a request, and nothing is
blocked by it.**

In the 037 workbook, seven leaves covering sections 12.8 and 12.8.1 have
`Title` values that are displaced relative to their `Description` values —
the titles appear shifted by one position across the group.

| Leaf | Title | Description subject |
|---|---|---|
| `SWE1-HMI-PROF-125-03` | Glove Box Lock Prompt on Valet Mode Entry | Status Bar interaction limits |
| `SWE1-HMI-PROF-125-04` | Glove Box Lock Button Greyed Out in Valet Mode | all non-interactable items greyed out |
| `SWE1-HMI-PROF-126-01` | Lock Out Specific Menu Areas in Valet Mode | PU0832 prompt on entering Valet Mode |
| `SWE1-HMI-PROF-126-02` | Status Bar Restrictions and Grey Out in Valet Mode | Glove Box Lock button greyed out |

The clearest single indicator: `125-03` is a section **12.8** leaf, but its
title describes a glove box prompt — and section 12.8 (PVAL8) does not mention
the glove box at all; the glove box is section 12.8.1.

**Our handling — no impact on delivered content.** We take the `Description`
column as the requirement unit and the `Title` column as an index label. That
decision is evidence-based, measured across all 180 leaves:

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

All test cases for these seven leaves were generated from the descriptions,
and their titles were authored by us rather than copied from 037, so the
misalignment does not propagate into delivered content.

**The only residual effect is for a human using 037 titles as an index** —
in these two sections, the title will lead to the wrong leaf.

Whether to correct the workbook is entirely upstream's call.
