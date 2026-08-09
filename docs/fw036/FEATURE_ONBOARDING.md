# FEATURE_ONBOARDING — FW036 TC Generation Process Canon

How a new feature (with or without an HMI spec, with or without existing
workbook content) enters the pipeline. Distilled from the Media and Home
runs. This file is the process authority; feature RUNBOOKs instantiate it.

---

## 0. Decision authority matrix — THE core of this canon

Every decision in the pipeline belongs to exactly one tier. When in doubt,
escalate one tier up — never down.

### Tier 0 — AUTO (recon script decides; humans only see the result)

- `workbook_state` detection when segmentation is unambiguous
- Column mapping via header-text match (report match count, e.g. 32/32)
- Design-method vocabulary extraction from the 下拉選單 sheet
- Leaf inventory, coverage-gap counts, done-region req_id sets
- Spec text-layer availability (`pdftotext` yield test)
- spec_id → section/outline mapping build (fail-loud on miss)

Output convention: `[AUTO]` entries in DECISIONS.md. No sign-off needed,
but they are recorded so an audit can see what was machine-determined.

### Tier 1 — Claude Code, cleared to proceed (canon-bound, gate-checked)

No discussion needed. Claude Code executes per this canon + feature RUNBOOK
+ profile, and the gates (lint, write-back invariants) catch drift:

- Porting/adapting pipeline scripts; `feature.yaml` wiring
- Building data artifacts (outline map, spec split, exemplars, sibling map)
- Batch context assembly
- **Generation of all post-pilot batches** (pilot itself is Tier 2)
- Lint runs; write-back runs (invariants ABORT on violation — an aborted
  run escalates to Tier 2, it is never "fixed" by weakening the invariant)
- ANOMALIES.md **registration** (recording a finding with evidence and a
  proposed disposition — NOT ruling on it)
- DECISIONS.md `[AUTO]` entries; git commits per repo convention
- Regenerating any derived artifact

### Tier 2 — discuss with Claude (chat), Pei signs

Judgment calls that shape scope, traceability, or audit posture. Claude
prepares a recommendation with evidence; Pei rules. The ruling is written
into DECISIONS.md or ANOMALIES.md verbatim:

- All `[PROPOSED]` entries in DECISIONS.md (batch sign-off, one pass)
- framework.md Part N Test Set derivation and granularity
- Profile `[OVERRIDE]` clauses — anything that displaces a docs.md generic
  rule needs an explicit, cited override
- Anomaly dispositions (PENDING → RESOLVED)
- **Pilot batch review** (the one mandatory human quality gate)
- Boundary cases: blocked-parent proportion, scope carve-out vs assumption
  marker, negative-pair sufficiency, cross-feature exemplar admissibility
- Any write-back invariant violation
- Splitting or merging a Test Set after generation has started

### Tier 3 — Pei only (not delegable)

- Final xlsx submission through controlled document management
- Release tag creation (SHA256 ↔ commit binding)
- Sending RD-1 questions / spec-file requests upstream
- Anything that signs the controlled document

### Escalation triggers — Claude Code MUST stop and file, never improvise

1. Spec lookup unresolved (missing section, missing PU id, missing file)
2. `workbook_state` segmentation ambiguous (mixed qualifying/placeholder
   rows inside one segment)
3. Write-back invariant violation
4. A needed rule has no profile/canon coverage (candidate new [OVERRIDE])
5. Fabrication pressure: any value the source does not state (§8.4)
6. Done-region content that contradicts the spec (A-026 pattern)

Filing = a DECISIONS.md or ANOMALIES.md entry with evidence + proposed
disposition, then continue with unaffected work.

---

## 1. Phase map

```
Phase 0  Intake     — collect files; classify spec_mode; run new_feature.py
Phase 1  Recon      — automated survey → RECON.md + DECISIONS.md (pre-filled)
Phase 2  Rulings    — Pei reviews DECISIONS.md [PROPOSED] items, signs   (Tier 2)
Phase 3  Framework  — framework.md Part N + profile file                 (Tier 2)
Phase 4  Data build — scripts + feature.yaml → data artifacts            (Tier 1)
Phase 5  Pilot      — one batch → Pei review → prompt adjustments        (Tier 2)
Phase 6  Batch      — generate → lint → write-back                       (Tier 1)
Phase 7  Delivery   — tag + submission + RD-1                            (Tier 3)
```

Phases 0–1 and 4 are fully delegable start-to-finish. The human time cost
of a new feature is: one DECISIONS.md pass (Phase 2), one framework/profile
review (Phase 3), one pilot review (Phase 5), delivery (Phase 7).

---

## 2. workbook_state — automated classification (Phase 1)

For every data row after the header:

1. **Filled row**: Test Item or TC ID non-empty.
2. **Qualifying done row**: author non-empty AND Procedure has ≥2 numbered
   steps AND content is non-placeholder. (Media lesson: draft rows with
   `Procedure = "Test"` are filled but NOT done.)
3. Segment qualifying rows → classify:

| State | Definition | Precedent |
|---|---|---|
| `BLANK` | zero filled rows | — |
| `PARTIAL_CLEAN` | contiguous done region + trailing blank/draft | Media (10–332 done, 333+ draft) |
| `PARTIAL_INTERLEAVED` | done and regen segments alternate | Home (3 Arif segments, 2+1 gaps) |
| `FULL` | all rows qualify | audit-only mode, no generation |

Ambiguous segmentation → Tier 2 with suspect row numbers listed.

### Per-state strategy binding

| Decision | BLANK | PARTIAL_CLEAN | PARTIAL_INTERLEAVED | FULL |
|---|---|---|---|---|
| Style authority | fallback chain (§3) | done region | done region | done region |
| Write-back | append from first data row | positional freeze + rewrite tail | in-place segment rewrite + **content-hash** invariant | none |
| Done invariant | n/a | positional hash | ordered content hash | full hash |
| Draft rows | n/a | discard & regenerate (default) | discard & regenerate (default) | n/a |

### BLANK fallback chain (style decisions when no done region exists)

`done region → nearest FW036 sibling feature done region (STYLE ONLY) →
docs.md generic rules`

Bindings under BLANK:

- Test Item = standard §4.3 tc_title (no precedent to defer to)
- Test Group / Test Set columns = **FILL** per framework Part N
  (TEST_SET_POLICY is itself the default when no precedent overrides it)
- spec_reference = constructed from spec_mode template (§10.7)
- Cross-feature exemplars carry marker `cross-feature: style only`; every
  literal (label, number, popup text, state name) MUST be re-traced to the
  current feature's spec — enforced as a lint rule, not by discipline
  (A-026 lesson)

---

## 3. spec_mode — source taxonomy (Phase 0)

| Mode | Source shape | Text pipeline | spec_reference | Precedent |
|---|---|---|---|---|
| A | Polarion/SYS1 export | outline map from export | `{filename}_{outline}` | Media, Home |
| B | PDF with text layer | pdftotext + section regex | `{filename}_{section}` | Home (hybrid A+B) |
| C | Scanned PDF | OCR pipeline + PNG render | via SYS1 if available, else OCR-anchored | Media images |
| D | CFTS / Word | doc extraction; reference is **looked up, never constructed** | CFTS clause id / SYS3 long form | BT profile §3.6 |
| E | No spec (037/SWRA only) | none | Verification Criteria column; expect heavy BLOCKED + RD-1 | — |

A feature may combine modes (Home = A for text + C for figure pages).
Images are always rendered for figure/table pages regardless of mode —
anatomy layouts and tables often exist only in images.

---

## 4. DECISIONS.md contract (Phase 1 output, Phase 2 gate)

- Template: `docs/fw036/templates/DECISIONS.md`
- Every entry is `[AUTO]`, `[PROPOSED: value — rationale]`, or `[PEI]`
- Phase 2 = Pei edits disagreements in place, fills `[PEI]` items, signs
  the sign-off block. **An unsigned DECISIONS.md blocks Phase 4+.**
- A `[PROPOSED]` left untouched at sign-off becomes binding as proposed —
  this is the mechanism that reduces questions without removing control.

---

## 5. Standing gates (all features, all states)

- Lint is a hard gate; the vocabulary/whitelist parts read from
  `feature.yaml` + profile
- Write-back invariants (traceability / completeness / done-region hash)
  abort rather than warn; weakening an invariant is a Tier 2 decision
- Every leaf gets a row: TC rows, or BLOCKED placeholder rows with Remarks
  (completeness invariant, both directions)
- One project = one `docs/fw036/framework.md`; features are Parts
- Profiles live in `docs/runtime/profiles/FW036_R1L_<Feature>_Profile.md`
- Feature directories live at repo root, self-contained, mirroring
  `mediaHMI/` layout; scaffold via `scripts/new_feature.py`
