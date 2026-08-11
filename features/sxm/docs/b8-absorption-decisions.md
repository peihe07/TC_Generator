# B8 — R10-2 decisions for the 9 unallocated clauses

Same form as `b5-absorption-decisions.md`: every clause listed individually,
condition (a) = same section as a leaf, condition (b) = the clause's observable
is exercised by that leaf's own scenario, so one test verifies both.

**1 of 9 absorbed** — the first absorption in this delivery, and the first
`[A-SX08]` marker emitted.

| clause | section | kind | (a) | (b) | outcome |
|---|---|---|---|---|---|
| 4872880 | 1.5.11 | SFR | pass | **pass** | **absorbed into leaf 094** |
| 4872884 | 1.5.11 | SFR | pass | fail | coverage hole (see note 1) |
| 4872893 | 1.5.12 | SFR | pass | fail | coverage hole |
| 4872895 | 1.5.12 | SFR | pass | fail | coverage hole (bus) |
| 4872905 | 1.5.12.1.1 | SFR | pass | fail | coverage hole (bus) |
| 4872906 | 1.5.12.1.1 | SFR | pass | fail | coverage hole (bus) |
| 4872907 | 1.5.12.1.1 | SFR | pass | fail | coverage hole (bus) |
| 4872908 | 1.5.12.1.1 | SFR | pass | fail | coverage hole (bus) |
| 4872909 | 1.5.12.1.1 | SFR | pass | fail | coverage hole (bus) |

## The one absorption — 4872880 into leaf 094

Leaf 094's clause (`4872879`) reads *"HU shall allow selection of all possible
SAT Browse categories"* and then defers to the HMI Logic and Flow documents.
Taken alone it has no pass criterion: "all possible" is unbounded, so any set
of categories satisfies it and a tester cannot fail the HU.

`4872880`, the very next clause in the same section, is the enumeration —
All channels, Presets, Favorites, Game Zone, Traffic and Weather, Featured.

Condition (b) holds in the strong form: the two are not merely observable in
one test, the second is what makes the first testable at all. One act of
opening Browse and reading the offered categories verifies both, and no second
scenario exists that would verify `4872880` separately without repeating 094.

The absorbing TC cites both clauses, own clause first, and the assumption
carries `[A-SX08]` naming `CFTS024-4872880`, which is what the `absorption-cite`
gate checks.

## Why the other eight fail (b)

**Note 1 — `4872884`, Satellite Genre Channel Browse.** This one fails (a) in
substance even though it passes formally: it is in §1.5.11, but the behaviour
it states (list all genres; select one to obtain its stations) is the behaviour
of leaves **111 and 112**, which live in §1.5.12.1.1. The clause is therefore
*covered* by TCs — just not by TCs in its own section, and R10-2 does not reach
across sections. No test is missing in practice; the traceability row is.

**`4872893`, sort by Artist.** Sibling of leaf 105 (sort by Genre) in the same
section. Different sort key, independent behaviour — verifying the genre sort
says nothing about the artist sort. This is a **genuine coverage hole**: the
alphabetical artist sort will not be tested by this delivery.

**The six bus clauses — `4872895`, `4872905`–`4872909`.** All state CAN signal
values: `TGW_Src_Cab_Stat`, `TGW_Src1Stat`/`TGW_Src2Stat`, `IR1_TRK_FILE`,
`IR1_PST_DSK`/`IR2_PST_DSK`, and the `CFTS024-540/541/543/544` signal set.
None is observable through the HMI, which is what every test in this workbook
observes, so no leaf's scenario can exercise them and (b) cannot hold for any
of them.

This is not a per-clause accident. Measured across the whole requirement set:
**0 of 202 leaves has a clause that mentions a bus signal.** 037 allocated no
bus-signal clause to any leaf in this feature. That is consistent with the
signals being verified by a different discipline rather than overlooked, but
it is an inference, not a ruling.

**For RD-1:** are bus-signal requirements in scope of the SWE.6 workbook at
all? If they are not, these six should be recorded as out-of-scope rather than
as coverage holes, and the same question applies to every §1.5.x section that
ends in a signal block. If they are, they need leaves — which 037 does not
currently provide for any of them.
