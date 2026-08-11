# CFTS024 cross-chapter twin list — SXM §1.5.x vs AMFM §1.3.x

Pre-pilot check required by A-SX04: every SXM leaf's clause text compared
against every AMFM leaf's clause text; pairs at similarity ≥0.95 listed.
Comparison is on folded text (case, punctuation and id tags normalised).
Source: `data/twin_pairs.json`, regenerate before the pilot batch.

**202 SXM leaves compared → 11 twins ≥0.95: 9 identical, 2 divergent.**

## Divergent pairs — the ones A-SX04's condition was written for

Both differences are band-family terminology, not behaviour. §8.6 still gives
the SAT clause authority, which here means the TC uses the SAT wording; no SAT
clause carries a behaviour its analog twin lacks.

| SXM leaf | SAT clause | AMFM leaf | analog clause | ratio | difference |
|---|---|---|---|---|---|
| SWE-RA-SXM-020 | `4872780` §1.5.2 | SWE-RA-RAD-011 | `4872413` §1.3.2 | 0.9595 | `Tuner` → `Satellite Audio` |
| SWE-RA-SXM-024 | `4872786` §1.5.3 | SWE-RA-RAD-026 | `4872442` §1.3.4 | 0.9676 | `executed` → `initiated`, `a tuner` → `Satellite Audio` |

## Identical pairs (ratio 1.000)

Same requirement stated once per band chapter under two ids. Each feature
cites its own chapter's clause; nothing is cross-cited (A-SX04).

| SXM leaf | SAT clause | §  | AMFM leaf | analog clause | § |
|---|---|---|---|---|---|
| SWE-RA-SXM-037 | `4872805` | 1.5.7 Preset Save | SWE-RA-RAD-036 | `4872475` | 1.3.8 Preset Save |
| SWE-RA-SXM-108 | `4872899` | 1.5.12.1 Browse Presets | SWE-RA-RAD-022 | `4872429` | 1.3.3.1 Browse Category- Presets |
| SWE-RA-SXM-110 | `4872901` | 1.5.12.1 Browse Presets | SWE-RA-RAD-023 | `4872430` | 1.3.3.1 Browse Category- Presets |
| SWE-RA-SXM-132 | `4872934` | 1.5.13 Scroll Up/Down | SWE-RA-RAD-040 | `4872493` | 1.3.10 Scroll Up/Down |
| SWE-RA-SXM-140 | `4872943` | 1.5.14 Page Up/Down | SWE-RA-RAD-043 | `4872499` | 1.3.11 Page Up/Down |
| SWE-RA-SXM-142 | `4872945` | 1.5.14 Page Up/Down | SWE-RA-RAD-044 | `4872500` | 1.3.11 Page Up/Down |
| SWE-RA-SXM-143 | `4872946` | 1.5.14 Page Up/Down | SWE-RA-RAD-045 | `4872501` | 1.3.11 Page Up/Down |
| SWE-RA-SXM-148 | `4872952` | 1.5.15 Enter or Item Select | SWE-RA-RAD-047 | `4872506` | 1.3.12 Enter or Item Select |
| SWE-RA-SXM-149 | `4872954` | 1.5.15 Enter or Item Select | SWE-RA-RAD-049 | `4872508` | 1.3.12 Enter or Item Select |

## Remarks text for the affected SXM rows

Per the A-SX04 ruling, each SXM row above carries the analog **clause id**,
never an AMFM TC id:

```
Analog-chapter twin: CFTS024-<analog id> (covered in the AM/FM deliverable)
```

## RD-1 FYI item

CFTS024 states 11 requirements twice — once in the analog tuner chapter
(§1.3.x) and once in the satellite chapter (§1.5.x) — under different clause
ids. An amendment to one chapter leaves the other stale with no mechanical
signal. Reported as an observation; no local action is taken.
