# B5 R10-2 absorption decision list — §1.5, 14 unallocated clauses

A-SX08 checkpoint, second cell. The decision test was run per clause, not per
group. Leaf 001 is the only leaf §1.5 carries; its cited clause is `4872752`
(Channel Art image display).

Test: absorb **iff** (a) same spec section **and** (b) the clause elaborates
the leaf's cited clause.

| clause | kind | what it binds | (a) same section | (b) elaborates 4872752 | outcome |
|---|---|---|---|---|---|
| `4872749` | Description | Description artifact, not a requirement | ✅ pass | ❌ fail | coverage hole |
| `4872750` | SFR | SXM display and functionality if the chip is equipped | ✅ pass | ❌ fail | coverage hole |
| `4872751` | SFR | US as the default region without navigation | ✅ pass | ❌ fail | coverage hole |
| `4872753` | SFR | testing per RX-9835-0011 / RX-9835-0071 | ✅ pass | ❌ fail | coverage hole |
| `4872754` | SFR | NavTraffic TA test procedure SX-9835-0051 | ✅ pass | ❌ fail | coverage hole |
| `4872755` | SFR | X65 SRM receiver PDS SX-9840-0017 | ✅ pass | ❌ fail | coverage hole |
| `4872756` | SFR | SXM-provided EMMA interface documents | ✅ pass | ❌ fail | coverage hole |
| `4872757` | SFR | SXi message specification SX-9845-0097 | ✅ pass | ❌ fail | coverage hole |
| `4872758` | SFR | SXi UART link layer SX-9845-0098 | ✅ pass | ❌ fail | coverage hole |
| `4872759` | SFR | antenna SX-9845-0105 / RF bench SX-9835-0046 | ✅ pass | ❌ fail | coverage hole |
| `4872760` | SFR | 360L UX SX-9840-0067-2.8 / EMMA migration | ✅ pass | ❌ fail | coverage hole |
| `4872761` | SFR | SXi extended metadata identifiers SX-9845-0150 | ✅ pass | ❌ fail | coverage hole |
| `4872762` | SFR | MFFR SX-9845-0156 / Audio Service UI SX-9845-0203 | ✅ pass | ❌ fail | coverage hole |
| `4872763` | SFR | four SX album-art documents | ✅ pass | ❌ fail | coverage hole |

**Absorbed: 0 of 14.** No `[A-SX08]` marker was emitted anywhere in B5, and
no `specification_reference` in the batch carries a second same-document
clause — the multi-cite path is therefore also unexercised.

## Why (b) fails, clause by group

- **Type approval, interface, protocol, hardware, product and metadata
  conformance (11 clauses)** bind the implementation to SiriusXM and Chrysler
  specifications the corpus does not hold. None describes HU behaviour, and
  none elaborates the display of channel art.
- **`4872763` is the near miss** — it is also about imagery, but it binds
  *album* art to four supplier documents. Parallel conformance, not an
  elaboration of the channel art clause. Absorbing it would claim coverage of
  documents that are not in `inputs/`.
- **`4872749`** is a Description artifact (section preamble).
- **`4872750` and `4872751`** are configuration statements, not elaborations
  of channel art.

## Coverage holes, and the one worth an upstream question

All 14 are recorded as coverage holes. One is different in kind:

**`4872750` — "HU shall provide SXM related display and functionality if SXM
chip is equipped"** is an observable configuration gate, the same shape as
AMFM's `$AM_Presence$` leaves (001/002), which the 037 there *did* allocate
leaves to. Here it has none. If any of the 14 should carry a leaf, it is this
one — that is the RD-1 Q-SX question, asked as allocation policy rather than
as an assertion of omission.

The remaining 13 raise the policy question in the other direction: whether
supplier-conformance requirements are meant to reach SWE.6 validation at all,
given that verifying them requires specifications outside this delivery.
