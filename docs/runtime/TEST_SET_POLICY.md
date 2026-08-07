# Test Set Policy

This document is the runtime policy for Test Set classification, review, and
export. The short generation-facing summary lives in
`ASPICE_SWE6_AI_Instruction.md` §4.2.

## Purpose

Test Set is the capability-level grouping inside a workbook Test Group. It is
used for Configure grouping, generation context, Review filtering, and the
exported `Test Case Framework` sheet.

## Source Of Truth

- Imported workbook Col H is a hint only.
- A job's official Test Set assignment is created by Configure grouping,
  reviewer manual override, or export-time fill for missing values.
- Test Set classification uses the fixed classification model internally; it
  is independent of the generation model selected by the user.
- Export writes the chosen Test Set into Col H and builds `Test Case Framework`
  summary counts from exported rows.

## Naming Rules

- Use short English noun phrases, typically 1-3 words.
- Label the functional capability within the Test Group.
- Do not repeat the Test Group / module prefix already present in Col G.
- Group by capability, not by screen, button, action verb, or one-off sub-flow.
- Preserve reviewer hints only when they match the capability-level taxonomy.
- Prefer broader shared capability labels when requirements clearly belong
  together; single-req Test Sets are allowed only for genuine outliers.
- Keep spelling and casing stable across the project.
- Never use empty labels, `None`, `Unclassified`, `Misc`, `Feature`, `Function`,
  `Req-xxx`, or generated requirement-code placeholders as final labels.
- `Needs Classification` is a preview-only placeholder for rows the tool could
  not classify. It must not be applied or exported as the row's final Test Set.

## Examples

With Test Group = `Bluetooth`:

- Good: `Connection`, `Pairing`, `Power Control`, `Device List`
- Bad: `BT Connection`, `Bluetooth Pairing`, `BT Switch`

With Test Group = `Projection`:

- Good: `Projection Detection`, `Projection Launch`, `Bluetooth Audio Management`
- Bad: `Projection`, if all rows are collapsed there despite clear capability
  differences; `Unclassified`; `Needs Classification`; `REQ SWE1-PROJ`

## Implementation Touchpoints

- `backend/tools/parse.py`: imports original Test Set as `testSetHint`; official
  `testSet` starts blank.
- `backend/tools/group.py`: creates grouping preview and assignments; existing
  Test Set values can be preserved or passed as hints during regroup.
- `backend/prompt_builder.py`: builds Test Set classification prompt and
  generation context.
- `backend/api_server.py`: maps payload rows for export and fills missing Test
  Sets when needed.
- `backend/writer.py`: writes Test Set to Col H and framework sheet summaries.
