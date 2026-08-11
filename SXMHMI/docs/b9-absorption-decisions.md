# B9 — R10-2 decision for the 1 unallocated clause

| clause | section | kind | (a) | (b) | outcome |
|---|---|---|---|---|---|
| 4872919 | 1.5.12.1.2 | SFR | pass | fail | coverage hole, and a contradiction — see A-SX18 |

`4872919` ("All Score updates") describes the same single-match score-update
flow as leaf 120's clause `4872918`, but specifies a different screen content:
`4872918` lists the games that have score updates, `4872919` lists the games
that are starting *as well as* the score updates.

Condition (b) fails not for the usual reason (the observable lies outside what
an HMI test can see) but because one test cannot satisfy both: absorbing would
require the ER to assert two different list contents simultaneously.

Leaf 120's TC-02 follows `4872918` as written and asserts that a game without a
score update is **not** listed. That assertion is exactly what `4872919` would
forbid, so it is the open risk carried by this decision, recorded in A-SX18.

Absorptions so far in this delivery: **1** (B8, `4872880` into leaf 094).
