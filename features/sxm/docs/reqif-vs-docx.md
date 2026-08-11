# ReqIF vs docx as the CFTS024 source of record — diff report

Run 2026-08-10 against all 202 SXM leaves. Sources:

| | file | SHA256 |
|---|---|---|
| docx (current) | `…CFTS 024_Specific HU Radio Functions_20250910_1239.docx` | `e5c12e9e…` |
| ReqIF (candidate) | `…CFTS 024_Specific HU Radio Functions_20250910_1224.reqifz` | `325dba60…` |

Same release (25PI3.5), exported 15 minutes apart.

## Field-by-field agreement

| field | result |
|---|---|
| declared id present in the source | **202 / 202** |
| clause text | **202 / 202 identical** (folded comparison, ratio ≥ 0.999) |
| printed section number | **not comparable directly** — see below |

The ReqIF carries **no printed section number**. Its outline is *positional*,
counting every object in the specification tree including unnumbered
description rows, so it differs systematically from the number printed in the
document's headings:

| docx printed § | ReqIF outline |
|---|---|
| §1.5.1 Seek Up | 1.5.16 |
| §1.5.10 Instant Replay | 1.5.25 |
| §1.5.10.1 Pause | 1.5.25.7 |

A straight swap would therefore lose the number every `spec_reference`, batch
table and framework Part N entry cites. **0/202 on that field is a numbering
difference, not a content disagreement** — no clause landed in a different
part of the document.

## The join that resolves it

All **200 / 200** docx headings exist in the ReqIF as objects: the heading's
`{anchor}` id is itself a clause id, `ReqIF.Name` is the heading title, and
`ReqIF.ChapterName` is populated on exactly those 200 objects. So the printed
number can be recovered without any bracket arithmetic:

1. docx → `(printed §, heading anchor id)`, parsed from the heading text
2. ReqIF → `clause id → (text, tree position)`
3. join: walk a clause's tree position up to its nearest ancestor that is a
   heading object, take that object's id, look up its printed §

Tested end to end: **202 / 202 leaves reproduce the current bracket map
exactly.**

## What the switch would and would not remove

Removed — the inference on the CFTS024 side:

- `PARA_ANCHOR_RE`, the `7-digit:` prefix parse that recovers a clause id from
  the head of a paragraph → replaced by the `ReqIF.ForeignID` attribute
- the **strictly-increasing heading anchor invariant** and the `bisect`
  bracket lookup → replaced by tree ancestry, which cannot be broken by an
  out-of-order anchor
- the assumption that a clause's text is "the paragraphs up to the next tagged
  line or heading" → replaced by `ReqIF.Text`

**Not** removed:

- `HEADING_RE`, the heading-text parse — still the only source of the printed
  number, and still needs to handle full-width brackets
- **anything on the 037 side.** A-SX01 (`(add)` after the id tail) and A-AM01
  (full-width brackets) are defects in the *037 Requirement Title*, which the
  ReqIF says nothing about. That fragility stays exactly where it is.

## Recommendation

Adopt the hybrid, not a swap: ReqIF as the clause source of record, docx
retained for heading numbers, and the existing bracket map kept as a
**verifier** — it is now a second independent derivation of the same mapping,
and a disagreement between the two is a signal that one of the two exports
moved. Re-running both and diffing is cheap (seconds) and is the check that
would catch a re-exported CFTS024 silently changing shape.
