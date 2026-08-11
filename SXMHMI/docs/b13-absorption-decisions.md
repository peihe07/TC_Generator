# B13 — R10-2 decisions for the 4 unallocated clauses

**0 of 4 absorbed.** Running total of absorptions in this delivery: **3**.

| clause | section | kind | (a) | (b) | outcome |
|---|---|---|---|---|---|
| 4873285 | 1.5.19 | SFR | pass | fail | coverage hole — bus/GCI |
| 4873286 | 1.5.19 | SFR | pass | fail | not a requirement on the HU |
| 4873288 | 1.5.20 | Description | pass | fail | section prose, correctly typed |
| 4873295 | 1.5.20 | SFR | pass | fail | **coverage hole — a display requirement with no leaf** |

## 4873285 — the GCI table send

> Once user exits "Channel Skip" … HU shall send the updated GCI table
> compiling the updated skipped channel list … See {CFTS22-1205} …

The observable is a table sent on the bus, which no HMI test sees. Same
disposition as the B8 bus-signal group. It also cites `CFTS22-1205` — note the
**two-digit** document number, a fourth citation shape after the 7-digit STLA
id, the `CFTSnnn-n` short form and B12's `SX-9845-0008`. Recorded, not acted on.

## 4873286 — a requirement on other ECUs

> HFM and VES shall not send any function requests to HU to tune to a skipped
> channel.

The subject is HFM and VES, not the HU. Nothing the HU does can satisfy or
violate it, so there is no HU-side observable to absorb. This is the first
unallocated clause that fails for *subject* rather than for observability.

## 4873288 — correctly typed section prose

Typed `Description`, and reads as one: it introduces what §1.5.20 covers and
defers the displays to the HMI documents. The same correct shape as B12's
`4872971`, which is what the A-SX14 addendum turns on.

## 4873295 — the one that matters

> If HU is playing satellite radio audio or in Travel Link mode and a Global
> Channel Information (GCI) update comes over the air … "Updating Channels
> Please Wait . . ." shall be displayed during the GCI update. No satellite
> radio audio shall be heard during this update. This message must be
> maintained in SDARS audio and Travel Link screens …

This is a fully specified, HMI-observable display requirement — message text,
trigger, audio suppression, persistence across screen transitions — and **no
leaf carries it**.

It is the exact structural twin of leaf 182 (`4873296`, the PSV update message),
which is the very next clause in the section and got a leaf. R10-2 (b) still
fails: the two updates are different over-the-air events, so 182's scenario
cannot produce a GCI update, and one test cannot observe both messages.

Unlike the bus and prose cases, nothing about this clause explains why it has no
leaf. **This is the strongest single-clause allocation gap found in the
delivery** and is raised for RD-1 accordingly.

**RULED (Pei, 2026-08-11): record the gap, do not self-supply a leaf.**
Registered as A-SX26; no row is written and no leaf id is invented. See that
entry for the reasoning.
