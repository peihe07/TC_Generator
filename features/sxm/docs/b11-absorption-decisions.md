# B11 — R10-2 decisions for the 3 unallocated clauses

**0 of 3 absorbed.** Running total of absorptions in this delivery: **3**
(B8 `4872880` → leaf 094; B10 `4872953` → 148, `4872955` → 149).

| clause | section | kind | (a) | (b) | outcome |
|---|---|---|---|---|---|
| 4872960 | 1.5.16 | SFR | pass | fail | coverage hole — configuration gate |
| 4872965 | 1.5.16 | SFR | pass | fail | not a testable requirement — pointer note |
| 4872968 | 1.5.16 | SFR | pass | fail | not a testable requirement — pointer note |

## 4872960 — the Canada configuration gate

> if `$Country_Code$` = [Canada] the HU shall not display the traffic and
> weather Jump function.

Condition (b) fails on the market axis: every leaf in this section is tested
under a configuration in which the Jump function *is* displayed, so no leaf's
scenario can show it hidden. Verifying that Jump works says nothing about
whether it is suppressed for another country code.

This is the third configuration-gate clause found unallocated — the same family
as `4872750` (B5, `$AM_Presence$`-style gate) — and it is the more consequential
kind, because the observable is a whole feature disappearing rather than a
field changing. If the delivery is expected to cover NAFTA-Canada at all, this
is a real hole with a market-visible consequence.

## 4872965 and 4872968 — pointer notes carrying an SFR artifact type

> Note: Please refer to SiriusXM SSP or EMMA documents for requirements on how
> long to retain and when to discard the latest traffic & weather recording…

> Please refer to SiriusXM SSP or SiriusXM EMMA documents for further details
> on implementation.

Neither states a behaviour of the HU. `4872965` explicitly delegates the
retention and discard rules to documents that are not in this delivery's source
set, and `4872968` delegates unspecified "further details". There is no
observable to absorb and no assertion an ER could carry.

Both are typed `Subsystem Functional Requirement` in the ReqIF attributes,
which is the A-SX14 shape again: the artifact type says requirement, the text
is a pointer. Counting them as coverage holes would overstate the gap; they are
recorded here as **not testable as written**.

Worth noting for the retention question specifically: leaf 157 replays "the
latest" broadcast, and how long "the latest" survives is exactly what `4872965`
declines to state. TC 157 therefore fixes the recording's availability in its
pre-conditions rather than asserting any retention period.
