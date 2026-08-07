# Pending Passes — mechanical rework queued behind RD-1 rulings

Every change deferred while waiting for an answer, with the retrieval handle
that finds its targets. When a ruling lands, this is a work order, not a
research task.

Each pass states its **acceptance check** — a command whose output decides
whether the pass is complete. Do not mark a pass done on inspection.

After any pass: re-run `scripts/lint_tcs.py`, then `scripts/write_back.py`, and
compare the new workbook against the previous one. The write-back is
byte-reproducible, so the diff shows exactly what the pass changed and nothing
else.

Status legend: **WAITING** (needs an answer) · **READY** (answer known, work not
done) · **DONE**.

---

## P-1 — Tab Button label (A-026) · WAITING on RD-1 Group 0

**Question:** which of the seven vehicle models are R1 High and which are R1
Low? MN2 labels the tab `"Playing"` on R1 High and `"Playing: Source"` on R1
Low.

**Targets:** 77 TCs containing the literal `"Playing"`.

```bash
cd tcgen_package && python scripts/lint_tcs.py generated/ --data data | grep A-026
# A-026 tier-dependent tab labels ...: playing-r1high=77
```

| Ruling | Work |
|---|---|
| R1 High | None. The 77 TCs are correct; the **two done-region TCs** using `"Playing: <source>"` (COM-014-01, COM-032-01) become the anomaly — out of our scope, hand to whoever owns rows 10-332. |
| R1 Low | Replace `"Playing"` → `"Playing: <source>"` in all 77. Mechanical: the label appears in a fixed step prefix. |
| Mixed fleet | Neither literal is usable. Every affected TC needs a tier-neutral formulation, **and** the workbook's uniform all-`1` vehicle flags need revisiting for tier-specific rows. This is the expensive branch — raise scope before starting. |

**Acceptance:** the counters must be all-or-nothing — either `playing-r1low=0`
(nothing changed) or `playing-r1high=0` (all switched). A split result means the
pass missed rows. Under the mixed ruling both go to zero.

---

## P-2 — INT-034 vehicle flags (A-029) · WAITING on RD-1 Group 0

**Question:** same matrix as P-1, plus screen size — `MW9` applies to *"all R1
radios except R1 Low 7\""*.

**Targets:** the 5 TCs of `SWE1-MEDIA-INT-034`, currently flagged T–Z = `1` per
existing workbook convention.

```bash
cd tcgen_package && python scripts/lint_tcs.py generated/ --data data | grep "FLAGS PENDING"
```

| Ruling | Work |
|---|---|
| No model is R1 Low 7" | Remove the pending note from `write_back.remarks`; flags stay `1`. |
| Some models are R1 Low 7" | Set those models' flags to `0` on these 5 rows — **the first rows in the workbook not uniformly `1`**. `write_back.py` currently hard-codes `1` for T–Z; it needs a per-row flag map first. |

**Acceptance:** `grep "FLAGS PENDING"` returns nothing, and if flags changed,
`write_back.py` has a test covering non-uniform flags.

---

## P-3 — Assumption rework · WAITING, one row per open ruling

All targets are retrievable by marker:

```bash
cd tcgen_package && python scripts/lint_tcs.py generated/ --data data | grep ASSUMPTION
```

| Anomaly | Targets | If ruled our way | If ruled against |
|---|---|---|---|
| **A-011** BT1.1.1 vs BT1.1.2 | `COM-059-01/02` (marker), `COM-058-01` (blocked) | COM-059 stands. COM-058 still needs a stated scope or removal. | BT1.1.2 is dead text: **rewrite both COM-059 TCs**, and COM-058 unblocks. |
| **A-012** BT1.6 vs BT1.2.1 | `COM-061-01`, `COM-061-04` | No change. | Rewrite both against BT1.6. COM-065-02 is scoped to a USB track list and is unaffected either way. |
| **A-018** MPB1.1 = 8 vs Table PRE1.1 ≤ 6 | `RAD-062-01` | No change. | If 8 is correct and a radio size is missing from both tables, rewrite against the literal 8 — and A-007's TCs need re-examining too. |
| **A-021** container naming | `RAD-070-01..05`; **`RAD-070-03` separately** | No change. | Two screens → revisit container anchoring across all ch18 parents. If the indicator is on Edit Presets, **RAD-070-03 verifies an object that is not in its container** — rewrite or withdraw. |
| **A-023** APP13 names the wrong container | `RAD-078-01..04` | No change. | Rewrite all four against the Presets Pop-up. |
| **A-024** INT-017 mapping | `INT-017-01` | No change; consider correcting 037's HMI Source ID to 21.11. | Rewrite against SA15 (category ordering) — but then SA14's behaviour has no leaf at all. |
| **A-032** FF2 vs AP2.1 | none — scope convergence, no marker | No change. | Still no change: `PLA-087-01` states AutoPlay ON explicitly and holds either way. Listed so the ruling is not mistaken for untracked work. |

**Acceptance:** for each ruling, either the marker is removed (question closed,
no rework) or the listed req_ids are rewritten and the marker updated. No marker
may outlive its anomaly's resolution.

---

## P-4 — Blocked leaves · WAITING on RD-1 Group 1 / Group 2

| Anomaly | Leaf | Unblocks when |
|---|---|---|
| **A-009** | `COM-051-01` | A Pop Up List revision containing PU0996 arrives, **or** SMP1's reference is corrected. Then write the TC and remove the blocked marker; the row's Remarks and blank P/R are replaced by real values. |
| **A-011** | `COM-058-01` | The BT1.1.1/BT1.1.2 ruling gives BT1.1.1 an instantiable scope. |

**Acceptance:** `scripts/lint_tcs.py` reports 0 blocked parents, and the
write-back's row count goes from 277 TC + 2 blocked to 279 TC + 0 blocked.

---

## P-5 — Retroactive correction of rows 10-332 · READY, deliberately deferred

Needs no ruling. Deferred so that "the done region is untouched" held as a hard
invariant throughout the regeneration — see `write_back.py`'s third invariant.
**Run this only after the regeneration is delivered and accepted**, as a
separate change with its own ChangeHistory revision.

| Item | Work |
|---|---|
| **A-005** | 8 done-region ERs write `recorded as the baseline` in a recording step, against §5.6. Mechanical wording fix. The count is pinned in `tests/test_lint_tcs.py`; the pin must go to 0 and the exemption in `test_done_region_exemplars_pass_every_rule_except_the_known_deviation` must be removed. |
| **framework.md known anomaly 1** | One done-region `Playing Tab` TC traces to a ch23 leaf — move to `Media Widget`. |
| **framework.md known anomaly 2** | Done-region `Browse Tab` TCs trace to ch9 leaves (Tracks popup, filed under Play Controls). Decide: keep the historical classification or reclassify. |
| **A-026 spillover** | If P-1 rules R1 Low, the two done-region `"Playing"` TCs need the same fix. If it rules R1 High, the three `"Playing: <source>"` ones do. Either way the done region carries the opposite error to ours. |

**Acceptance:** the done-region regression test passes with no rule exemptions
and no pinned count.

---

## P-6 — Coverage gaps · WAITING, and not ours to close

037 has no leaf for these, so no TC can be written and no workbook row exists to
write against. Listed to keep them from being forgotten: **if 037 gains leaves,
each becomes a generation task**, not a rework pass.

| Anomaly | Missing coverage |
|---|---|
| A-008 | Table PSB2.4: 4 of 7 radio sizes (both max-3 configurations). Table PSB2.3: 4 of 5 market variants. |
| A-010 | Table SMP2.2: 12"L/12"P have no leaf; 7"/10.25" are `N/A` with no stated meaning. |
| A-020 | `MPB1.7` HD preset labels (NA-relevant); `MPB1.8.x` FM-EU PSN labels (confirm out of scope). |
| A-025 | `21.13` Radio Off with Door — unambiguous gap. Beats Audio and Virtual Venue depend on the Group 0 answer. |
| A-027 | `AP2.2` — AutoPlay **ON** resume. The OFF exception has a leaf; the primary case does not. |
| A-031 | `MW3.2` — first metadata line, including the HD sub-station format. |
| A-013 / A-017 / A-019 / A-028 | Four numbering or code-reuse defects. If any hole was a real clause, nothing covers it. |

**HD Radio note:** A-020 and A-031 are both HD Radio rules with no coverage. One
answer — "is HD Radio in scope for FW036?" — settles both.
