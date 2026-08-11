# B10 — R10-2 decisions for the 2 unallocated clauses

**2 of 2 absorbed.** Absorptions in this delivery now total **3** (B8's
`4872880` into leaf 094, and these two).

| clause | section | kind | (a) | (b) | outcome |
|---|---|---|---|---|---|
| 4872953 | 1.5.15 | SFR | pass | **pass** | **absorbed into leaf 148** |
| 4872955 | 1.5.15 | SFR | pass | **pass** | **absorbed into leaf 149** |

## Why (b) holds

Leaf 148's clause `4872952` states only that the HU *enters* the Genre Seek
state. `4872953` is what that state does, and its exception — only stations
matching the selected genre are valid — is the entire content of "genre" seek.
Left unallocated, the genre restriction would not be tested anywhere: leaf 148
alone would pass on an HU that enters the state and then seeks across every
station in the tuner.

The two are consecutive observations of one operation. Select an item for Genre
Seek; the state is entered (`4872952`); the seek runs and the stations it lands
on are the next thing the tester sees (`4872953`). No second scenario, no
second setup. `4872955` into leaf 149 is the same reading with Scan.

This is the same strong form as the B8 absorption: the absorbed clause is what
makes the allocated clause's test meaningful, rather than merely being
convenient to observe alongside it.

## What the absorption does not carry — see A-SX21

`4872953` defines the base behaviour by reference to `CFTS024-165` ("the same
manner as the Seek Up function"). That citation belongs to the absorbed clause,
not to leaf 148's own clause, and R11 licenses cite-form only for tokens the
allocated clause writes. The `cross-reference` gate blocked it.

The ERs were therefore narrowed to the absorbed clause's own contribution: every
station landed on belongs to the selected genre, and none outside it does. The
seek's *exhaustiveness* — that it reaches every station of the genre — is Seek
Up's behaviour and is not asserted.

Net coverage change is still positive: these two clauses had no test at all
before, and the genre restriction now has one.
