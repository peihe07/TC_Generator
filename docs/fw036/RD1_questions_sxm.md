# RD-1 Questions — SXM (FW036)

Sent to upstream requirement authors. Same handling as the AMFM draft:
send at or before delivery (RUNBOOK Phase 7). Class-2 items are marked
**EXPEDITED** — they carry a live risk in a generated assertion, so a late
answer costs a rework rather than a footnote.

## Q-SX1 — Four Game Zone categories, or two renamed with both drafts surviving? (from A-SX17)

Context: three pairs of clauses in §1.5.12.1.2 and §1.5.12.1.4 carry bodies
that are identical or differ only in the category name.

| pair | clause ids | leaves | body |
|---|---|---|---|
| Add Teams / Select Teams | 4872913 / 4872914 | 115 / 116 | word for word identical |
| Edit Teams / Edit Selection | 4872915 / 4872916 | 117 / 118 | word for word identical |
| Edit Favorites / Edit FAVs | 4872927 / 4872930 | 126 / 129 | same two delete options; 4872930 additionally names the `Delete All` function |

Because the two clauses of each pair are siblings in one section, no
section-ownership carve is available; each test case therefore enters through
its own category name, the sole textual difference. Six delivered rows carry
`Same-text sibling: CFTS024-<paired id>` in Remarks.

Questions:
1. Are `Add Teams` and `Select Teams` two distinct categories in the HMI, or
   one category that was renamed with both drafts left in the document? Same
   question for `Edit Teams` / `Edit Selection` and `Edit Favorites` /
   `Edit FAVs`.
2. If a pair is one category, which name is live and should the other clause
   be withdrawn?

Consequence if unanswered: the delivery promises to test four Game Zone
add/edit paths and two Favorites edit paths. If any of them does not exist in
the HMI, that test case fails on a document defect, not a software defect.

Status: DRAFT.

## Q-SX2 — Which score-update listing is live, 4872918 or 4872919? (from A-SX18) — **EXPEDITED (class 2)**

Context: two adjacent clauses in §1.5.12.1.2 describe the same single-match
score-update flow and disagree on what the resulting screen lists.

- `4872918` (allocated to leaf 120): the `Browse GameZone - On Air` screen
  lists **all the games that have score updates**.
- `4872919` (unallocated, "All Score updates"): the same screen lists **all
  the games that are starting as well as the score updates**.

Ruled locally under §8.6 — the 037 allocates `4872918`, so its text governs and
leaf 120's TC-02 asserts that a game *without* a score update is not listed.
The weaker positive-only formulation was considered and rejected: it opens a
false-pass hole, since a screen that lists everything would satisfy it.

Questions:
1. Which of the two clauses is live? Is `4872919` a superseded draft of
   `4872918`?
2. If `4872919` is live, is `4872918` withdrawn — and should the On Air screen
   list starting games and score updates together?

Why expedited: the answer changes a delivered assertion, not a note. If
`4872919` is live, leaf 120's TC-02 negative assertion is wrong as written. The
affected test case carries an `[A-SX18]` marker so the amendment is a grep and
a one-line edit rather than a re-derivation.

Status: DRAFT — expedite ahead of the class-3 items.

## Q-SX3 — VR trigger path: the 037 titles declare it (from A-SX19)

Context: five leaves' clauses include a Voice Recognition trigger path, and the
VR scope was ruled out of this workbook and delegated to the CFTS028 delivery,
with an escape hatch — a leaf whose 037 title itself states VR returns for
individual ruling. **The escape hatch fired 5/5** — every one of the five
titles states VR — so applied literally it would have voided the exclusion
rather than catching an exception. The exclusion was re-ruled knowingly on
that measurement (DECISIONS Amendment 11) and stands: CFTS028 owns the VR
requirements and authoring VR test cases here risks double coverage of
another delivery's scope.

Evidence line, measured over the five leaves (002, 003, 006, 014, 030):

> **All five 037 titles contain `or a VR Command` verbatim.** The measured
> divergence between title and clause is not the VR wording — it is title
> truncation at the end of the first sentence, which drops the second
> sentence's behaviour (state entry, adjacent-channel move, wrap-around).

This is the opposite direction from the AMFM S3 class, where titles omitted the
VR wording that only the CFTS clause carried. SXM does not continue that
pattern: here the requirement document itself declares the VR scope, and the
exclusion removes from test a path the 037 states.

Questions:
1. Is the VR trigger path for these five behaviours verified by the CFTS028
   (Voice Recognition) delivery, and under which requirement ids?
2. If it is not, the five behaviours' VR path is verified nowhere — should
   these leaves carry a VR test case in this workbook after all?
3. Is the truncation of the 037 titles at the first sentence intended, or an
   export artefact? It affects more than these five leaves.

Status: DRAFT — EXPEDITED (class 2), expedite alongside Q-SX2. The answer can
change delivered content (the A-SX18 shape), so it is not a wording item.
The five test cases carry the exclusion note and an `[A-SX19]`
marker; if the answer is that VR belongs here, the amendment is scoped to those
five reasonings and their expected results.
