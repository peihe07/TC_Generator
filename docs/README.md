# TC Generator Docs

## Runtime Docs

These files are loaded by backend prompts or directly define runtime behavior.
Rename or move them only with matching code and test updates.

- `ASPICE_SWE6_AI_Instruction.md` — generation instruction loaded by `backend/rules_loader.py`
- `TEST_CASE_DESIGN_METHOD.md` — design-method rules loaded by `backend/rules_loader.py`
- `TEST_CASE_PRIORITY.md` — priority rubric loaded by `backend/rules_loader.py`
- `ASPICE_SWE6_AI_Review.md` — review prompt / review-engine reference
- `TEST_SET_POLICY.md` — grouping, hint, override, and export policy

## Rule Doc Maintenance

`ASPICE_SWE6_AI_Instruction.md` and the other runtime rule docs are the single
authoritative source — do not fork a parallel "generic" copy that can drift out
of sync. When a rule is confirmed:

- Fold it into the authoritative doc under the matching section rather than
  starting a second source of truth.
- Keep section numbers contiguous and stable. Prompt builders cite sections by
  number (e.g. `§10`, `§11`, `§12`); renumbering existing sections breaks those
  references and tests. Append new rules as sub-sections (`§8.6`, `§8.7`).
- A feature-agnostic rule may be written with `<placeholder>` tokens so it can be
  reused across features; project-specific names, doc numbers, and market
  variants stay as placeholders.
- Meta / maintenance conventions (like this section) stay out of the runtime
  prompt docs — they waste prompt tokens and do not help generation.

## Developer Docs

- `API_CONTRACT.md` — frontend/backend API contract
- `WORKFLOW_MECHANISM_TABLE.md` — user action → frontend → backend → AI/state map
- `PIPELINE_DESIGN.md` — end-to-end generation pipeline design (draft)
- `CHANGELOG.md` — architecture notes, history, and current baselines
- `DESIGN_SYSTEM.md` — Win95-themed frontend design-system reference
- `TC_Generator_Architecture_Diagrams.html` — architecture visual reference
- `design-system/` — UI conventions and design-system assets
- `../frontend-modern/README.md` — separate modern UI variant setup, ports,
  and Docker commands

## Archive

- `archive/` — historical notes and merged patches that must not be loaded into
  runtime prompts

## Local / Ignored Data

- `test/` and `temp/` are local sample data / scratch fixtures and are ignored
  by git
