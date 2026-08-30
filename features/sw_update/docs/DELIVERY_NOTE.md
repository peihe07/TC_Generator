# Delivery Note — SW Update (FW036 / CFTS057)

- **Feature**: SW Update (FOTA) — `SoftwareUpdate_FM-WI-FSM-037-A03_STLA_Report_SWRA.xlsx`
- **Workbook**: `FM-WI-FSM-036-A01 … _SWQT_SWUpdate_20260830.xlsx`
- **Date**: 2026-08-30
- **Author**: PeiPYHsu

---

## 1. What is in the book

> **Row order**: the book is sorted by **`Requirement or Design ID` ascending**
> (numerically, so `-10` follows `-9`), and test case IDs are assigned in row order,
> `newR1L-SU-001` … `-319`. Where one requirement has several test cases they are
> adjacent, in the order the facets were drafted.

| | Count |
|---|---:|
| Requirements in the source report | **311** |
| **Requirements with at least one test case** | **311 (100%)** |
| Test cases written | **319** |
| **Test cases complete and executable as they stand** | **124** |
| **Test cases carrying at least one `PENDING` placeholder** | **195** |
| Placeholder lines in total | **712** |

> **These two counts are kept apart on purpose.** 124 and 195 are not summed into a
> single "coverage" figure: the first is work you can run tomorrow, the second is work
> that is written in full but waits on an answer from your side.

### 1.1 100% coverage is not the same as every clause being verified

**Every one of the 311 requirements has at least one test case.** That is not the same
statement as "every sentence in the report is verified". Where a requirement contains
several independently triggerable actions, each needs its own test case, and those are
tracked separately in `COVERAGE_GAPS.md` — **that file is currently empty of unwritten
items**, but the distinction is what it exists to keep visible.

---

## 2. Who owns each gap

**195 test cases wait on something. They do not all wait on the same kind of thing.**

| Owner | What is missing | Test cases | Strongest example |
|---|---|---:|---|
| **Your specification** | A value, a criterion or a list the documents do not state | **31** | `175` — which conditions count as "safety-related" during a silent update |
| **Bench capability** | No way to observe, or no way to bring about, the condition | **120** | `184` — the silent-update rules apply "across all session flows", and the flows are not separable on a bench |
| **A splitting decision on your side** | Whether two requirements are one | **27** | `313` — an umbrella requirement over `315`–`320` |
| **Access to an external system** | The evidence lives on the OTA server or in another ECU | **17** | `330` — the session result is reported *to the OTA server*, and we have never established that we can read it there |

**The largest single block is bench capability, and most of it traces to one request:
DR-SU2 blocks 151 test cases.**

---

## 3. Why the placeholders were left in place

The seven data requests are attached (`docs/upstream_requests/DR-SU1_SU2_request.md`).
Each placeholder names the request it waits on, in the form
`PENDING: DR-SU{n} <what is missing>`.

**Nothing was guessed.** Where a threshold, a signal name or a pass criterion was not in
the source documents, no plausible value was written in its place. Where two of your own
documents disagree, we did not pick one — see `057`, where the same 30-minute limit is
counted from two different start points in the requirement report and in an embedded
drawing inside CFTS057.

**The attached request has been restated against this book.** It was first written on
2026-08-28 describing five requests blocking a handful of test cases; its closing section
lists what each part said then and what the measured figure is now.

---

## 4. Source-document defects preserved verbatim

Nine defects in the requirement text were carried through unchanged rather than
corrected, because correcting them would put our wording into a delivered test case.
They are listed in `DESCRIPTION_DEFECTS.md`; the ones that a reviewer will notice first:

| # | Requirement | What it is |
|---|---|---|
| D-5 | `346` | Sentence starts `he WiFiUpdateService` — the `T` is missing. **This is why lint reports one lower-case line start.** |
| D-6 | `333` | Sentence ends mid-clause: `…are not know` |
| D-7 | `117`, `242`, `243` | A footnote listing `$OperationalModeSts$` values is merged into the requirement sentence, in all three rows — one editing event, not three |
| D-8 | `145` | `the WiFi Update Servic/USB Update Service e` — one word split across two places |
| D-9 | `248` | `then notify the to start server initiated session` — the object of "notify" is missing. **We did not supply it**: `SWMC` and `WiFi Update Service` are two different requirements |

---

## 5. Columns left empty, and why

| Column | State | Reason |
|---|---|---|
| `B` | untouched | host of a shared formula in the master; writing it would break the formula |
| `C` | empty | not part of the agreed field set for this feature |
| `T`–`Z` | empty | vehicle-variant flags; no variant assignment was provided |
| `AB`–`AG` | empty | test execution results — filled during execution, not authoring |
| `AH` (remarks) | **empty** | our reasoning ledger (`REASONING.md`) is an internal record and is **not** folded into the delivered book |

---

## 6. How the book was produced

Written by surgical XML edit of the master workbook: only the target cells in
`xl/worksheets/sheet6.xml` were changed and **every other part was repacked byte for
byte**. Verified after writing:

- **47 of 48 parts byte-identical**; the one that differs is the sheet that was written
- data validation preserved: 4 standard + 1 `x14` (the `R` column dropdown)
- `calcChain.xml` and `sharedStrings.xml` present and unchanged
- all 7 `design_method` values match `下拉選單!$A$1:$A$9` character for character
- the source master's SHA-256 is unchanged — **it was never written to**

> ⚠ **One check remains that we cannot perform**: opening the book in Excel. Our checks
> are all at file level. On another feature a book passed every content check while the
> `R` column dropdown had been lost, so **please confirm on opening: no repair prompt,
> the `R`/`P` dropdowns work, and print settings survive.**

---

## 7. Attachments

1. `docs/PENDING_LIST.md` — every placeholder, by test case, requirement, request and kind
2. `docs/upstream_requests/DR-SU1_SU2_request.md` — the seven data requests
3. `docs/TESTRAIL_MAP.tsv` — test case ID ↔ row ↔ requirement ↔ test set ↔ priority
4. `DESCRIPTION_DEFECTS.md` — the nine source-text defects preserved verbatim
5. `COVERAGE_GAPS.md` — facets covered by delegation or indirectly, and by whom
