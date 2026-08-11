# B12 — R10-2 decision for the 1 unallocated clause

**0 of 1 absorbed.** Running total of absorptions in this delivery: **3**.

| clause | section | kind | (a) | (b) | outcome |
|---|---|---|---|---|---|
| 4872971 | 1.5.17 | Description | pass | fail | not testable as written — pointer note |

> Please refer to {SX-9845-0008 - SXI Implementation Guide} for more
> implementation details on Game Alerts.

No behaviour of the HU is stated, so there is nothing for an ER to assert.

Two things distinguish it from the B11 pointer notes:

1. Its ReqIF artifact type is **`Description`**, not `Subsystem Functional
   Requirement`. The document is therefore internally consistent here — the
   clause is typed as prose and reads as prose. That is the *correct* shape,
   and it makes the A-SX14 / B11 cases sharper by contrast: those carry the
   SFR type on identical pointer content. This is now measurable evidence that
   the SFR typing on `4872965` and `4872968` is a defect rather than a
   convention.

2. It cites a document in a **different scheme again** — `SX-9845-0008`, a
   SiriusXM supplier document, not a `CFTSnnn-n` token. It is not in the
   cross-document citation sweep and no leaf clause writes it, so R11 gives it
   no path even if a leaf wanted to borrow from it. Recorded, not acted on.
